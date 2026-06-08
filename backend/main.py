from fastapi import FastAPI
import json
import os
from transformers import pipeline

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "hospital_data.json"
)

HISTORY_FILE = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "history.json"
)

with open(DATA_FILE, "r", encoding="utf-8") as f:
    hospital_data = json.load(f)

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)


@app.get("/")
def home():
    return {"message": "Hospital Helpdesk API running"}


def find_department(text):
    text = text.lower()

    aliases = {
        "lab": "laboratory",
        "medicine": "general_medicine",
        "ent": "ent"
    }

    for word, dept in aliases.items():
        if word in text:
            return dept

    for dept in hospital_data["departments"]:
        if dept in text:
            return dept

    return None


def detect_intent(text):
    text = text.lower()

    if "where" in text or "location" in text:
        return "location"

    if "time" in text or "timing" in text:
        return "timing"

    if "contact" in text or "number" in text:
        return "contact"

    return "unknown"


def save_history(query, response):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    history.append({
        "query": query,
        "response": response
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)


@app.post("/chat")
def chat(query: str):
    dept = find_department(query)
    intent = detect_intent(query)

    if not dept:
        response = (
            "Sorry, I could not find that department."
        )

        save_history(query, response)

        return {"response": response}

    info = hospital_data["departments"][dept]

    if intent == "location":
        response = (
            f"{dept.replace('_', ' ').title()} "
            f"is located at {info['location']}."
        )

    elif intent == "timing":
        response = (
            f"{dept.replace('_', ' ').title()} "
            f"is open from {info['timing']}."
        )

    elif intent == "contact":
        response = (
            f"{dept.replace('_', ' ').title()} "
            f"contact number is {info['contact']}."
        )

    else:
        response = (
            "Please ask about location, timing, "
            "or contact."
        )

    save_history(query, response)

    return {"response": response}


@app.post("/summarize")
def summarize(text: str):

    result = summarizer(
        text,
        max_length=35,
        min_length=10,
        do_sample=False
    )

    return {
        "summary": result[0]["summary_text"]
    }


@app.get("/history")
def get_history():
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    return history