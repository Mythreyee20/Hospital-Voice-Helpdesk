# 🏥 Hospital Voice Helpdesk

## Project Code
PRJ-014

## Category
Voice Assistants

## Domain
Hospital

## Objective
To build a hospital helpdesk application that helps users get department location, timings, contact details, and summarization support through simple text and voice-based interaction.

---

# 🗓 Week 1

## Week 1 Goal
Set up the text pipeline, sample dataset, API endpoints, and a simple user interface.

---

## Work Completed

### Sample Hospital Dataset
A structured JSON dataset was created with:
- department names
- locations
- timings
- contact numbers

### FastAPI Backend
A backend API was developed using FastAPI.

Implemented endpoints:
- `GET /` — API health check
- `POST /chat` — receives user query and returns response

### Intent Detection
Basic keyword-based intent detection was implemented for:
- location
- timing
- contact

### Department Matching
The system identifies the department mentioned in the query.

Example:
- Where is cardiology?
- Radiology timing
- Emergency contact number

### Streamlit Interface
A simple Streamlit-based interface was created for user interaction.

---

## Technologies Used

- Python
- FastAPI
- Streamlit
- Transformers
- JSON

---

## Testing

The following were tested:
- API startup
- valid department queries
- unknown department handling
- frontend to backend communication

### Preprocessing
User input is converted to lowercase before department matching and intent detection.

### Sample Inference
Sample queries such as:
- “Where is cardiology?”
- “Radiology timing”

were tested to verify correct response generation.

### Sample Output

**Input:** Where is cardiology?  
**Output:** Cardiology is located at 2nd Floor, Block A.

---

## Week 1 Status

The system successfully:
- accepts text input
- detects department and intent
- generates relevant responses

---

# 🗓 Week 2

## Week 2 Goal
Add one NLP feature using Transformers and evaluate output quality.

---

## Work Completed

### Summarization Feature
A text summarization feature was implemented using the Hugging Face Transformers library.

### Model Used
`google/pegasus-xsum`

### New API Endpoint
- `POST /summarize`

The endpoint accepts text input and returns a concise AI-generated summary.

### Prompt / Model Tuning
The following parameters were used:
- `max_length = 35`
- `min_length = 10`
- `do_sample = False`

---

## Testing

The summarization feature was tested using:
- short input text
- long descriptive text
- unrelated text
- response latency observation

### Sample Input
The cardiology department specializes in diagnosing and treating heart-related diseases. The department provides ECG testing, emergency cardiac treatment, specialist consultations, and rehabilitation programs for patients using advanced medical technology and expert cardiac care services.

### Sample Output
Chennai City Hospital provides advanced cardiac care and treatment services for heart-related diseases.

---

## Week 2 Status

The system successfully:
- accepts longer text input
- generates concise summaries
- performs NLP inference using Transformers

---

# 🗓 Week 3

## Week 3 Goal
Add history, voice support, documentation, and a polished demo workflow.

---

## Work Completed

### Chat History
A history feature was added.

User queries and system responses are stored in `history.json`.

### History API
A new endpoint was implemented:

- `GET /history`

The endpoint returns previous queries and responses.

### Streamlit History Tab
A dedicated History tab was added to the frontend.

The tab displays:
- previous user queries
- previous system responses

### Voice Input Support
A basic microphone input feature was added using Streamlit audio recording support.

The system allows users to record voice input for interaction and future speech-to-text expansion.

### Improved Frontend
The frontend was organized into three tabs:
- Helpdesk
- Summarizer
- History

This improved the overall demo workflow and usability.

---

## Testing

End-to-end testing was performed for:
- frontend to backend communication
- helpdesk query response
- summarization workflow
- history retrieval
- invalid query handling

### Presentation-ready Examples
The following demo examples were prepared:
- Where is cardiology?
- Radiology timing
- Where is cafeteria?
- Emergency department summarization

---

## Week 3 Status

The system successfully:
- stores previous interactions
- retrieves chat history
- supports voice recording
- provides a polished demo workflow
- supports presentation-ready testing

---

# Project Structure

hospital-voice-helpdesk/

- backend/
  - main.py

- frontend/
  - app.py

- data/
  - hospital_data.json
  - history.json

---

# Final Features

- hospital helpdesk chatbot
- department location support
- timing and contact support
- intent detection
- transformer-based summarization
- voice input support
- chat history
- FastAPI backend
- Streamlit frontend

---

# Setup Instructions

## Install Required Packages

```bash
pip install fastapi uvicorn streamlit transformers torch requests
pip install audio-recorder-streamlit

```

---

# Run Backend

cd backend
uvicorn main:app --reload

 # Run Frontend
Open another terminal:

cd frontend
streamlit run app.py

# Final Status

The project successfully covers:

Week 1 implementation and testing
Week 2 implementation and testing
Week 3 implementation and testing

The application is working end-to-end and is ready for demonstration.