# Student Backend API — FastAPI + Gemini 

This backend provides a simple AI-powered text analysis endpoint for student support applications.  
It summarizes student text and classifies sentiment using **Google Gemini 2.5 Flash**.

---

## Features

### ✔ AI-powered text analysis  
- Summarizes text in **one line**.  
- Sentiment detection (**positive / negative / neutral**).  
- Uses **google-genai** with model:  
  `models/gemini-2.5-flash`.

### ✔ Secure environment configuration  
- `.env` used to safely load the Gemini API key via `pydantic-settings`.

### ✔ Clean modular codebase  
- `ai_service.py` → AI logic  
- `feature.py` → FastAPI route logic  
- `config.py` → environment loading  
- `schemas.py` → request/response models  
- `logging_config.py` → centralized logging  
- `main.py` → application entry point  

### ✔ Logging  
- Logs incoming requests, AI response, and error fallbacks.

---


---

## Installation & Setup

### 1️. Clone the repository

```bash
git clone <repo-url>
cd student_backend_api
```
### 2.  Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key to .env
```bash
python -m uvicorn app.main:app --reload
```

## Running the Server

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

## API Endpoints

### 🟩 POST /feature/

Analyze text using Gemini.

#### Request Body

```json
{
  "text": "I am stressed about work but feeling hopeful."
}
