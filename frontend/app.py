import streamlit as st
import requests
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder


st.title("🏥 Hospital Voice Helpdesk")

tab1, tab2, tab3 = st.tabs(
    ["Helpdesk", "Summarizer", "History"]
)

# ---------------- HELP DESK ----------------

with tab1:

    st.subheader("Hospital Helpdesk")

    query = st.text_input(
        "Ask your question",
        placeholder="Where is cardiology?"
    )

    if st.button("Get Answer"):

        if query.strip():

            try:

                res = requests.post(
                    "http://127.0.0.1:8000/chat",
                    params={"query": query},
                    timeout=5
                )

                st.success(
                    res.json()["response"]
                )

            except:
                st.error(
                    "Backend server is not available."
                )

    st.markdown("---")

    # ---------------- VOICE INPUT ----------------

    st.subheader("🎤 Voice Input")

    audio_bytes = audio_recorder()

    if audio_bytes:

        with open("voice.wav", "wb") as f:
            f.write(audio_bytes)

        st.success("Voice recorded successfully")

        recognizer = sr.Recognizer()

        try:

            with sr.AudioFile("voice.wav") as source:

                audio_data = recognizer.record(source)

                text = recognizer.recognize_google(
                    audio_data
                )

                st.info(f"Recognized Text: {text}")

                try:

                    res = requests.post(
                        "http://127.0.0.1:8000/chat",
                        params={"query": text},
                        timeout=5
                    )

                    st.success(
                        res.json()["response"]
                    )

                except:
                    st.error(
                        "Backend server not available."
                    )

        except Exception as e:

            st.error(f"Speech recognition error: {e}")

# ---------------- SUMMARIZER ----------------

with tab2:

    st.subheader("Text Summarizer")

    text = st.text_area(
        "Enter long text",
        height=200
    )

    if st.button("Summarize"):

        if text.strip():

            try:

                res = requests.post(
                    "http://127.0.0.1:8000/summarize",
                    params={"text": text},
                    timeout=60
                )

                st.info(
                    res.json()["summary"]
                )

            except:
                st.error(
                    "Backend server is not available."
                )

# ---------------- HISTORY ----------------

with tab3:

    st.subheader("Chat History")

    try:

        res = requests.get(
            "http://127.0.0.1:8000/history",
            timeout=5
        )

        history = res.json()

        if history:

            for item in reversed(history):

                st.markdown(
                    f"**Q:** {item['query']}"
                )

                st.markdown(
                    f"**A:** {item['response']}"
                )

                st.divider()

        else:

            st.write("No history available.")

    except:

        st.warning(
            "History not available right now."
        )