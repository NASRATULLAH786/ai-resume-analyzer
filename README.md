# AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![AI Analysis](https://img.shields.io/badge/AI-Resume%20Evaluation-orange)
![Automation](https://img.shields.io/badge/Workflow-Automation-blue)

---

# AI Resume Analyzer

AI Resume Analyzer is an AI-powered candidate evaluation and recruitment workflow automation platform built using FastAPI, SQLite, and frontend dashboard technologies.

The system automates resume screening, technical skill detection, candidate scoring, and hiring recommendation workflows to improve recruitment efficiency.

---

# Problem Statement

Recruiters and hiring teams manually review large numbers of resumes every day.

Manual candidate evaluation creates several challenges:

- inconsistent resume screening
- delayed hiring processes
- inefficient skill matching
- repetitive recruitment workflows
- difficulty prioritizing candidates
- human error during evaluation

Organizations need scalable systems to automate candidate analysis and improve hiring efficiency.

---

# Solution

This platform automates candidate evaluation workflows by:

- analyzing resume content
- detecting technical skills
- calculating candidate scores
- determining experience level
- generating hiring suggestions
- storing resume evaluation history
- improving recruitment workflow efficiency

---

# Key Features

- AI-style resume analysis
- Candidate scoring engine
- Technical skill detection
- Resume evaluation workflows
- Hiring recommendation generation
- Resume analysis history
- FastAPI backend APIs
- Interactive frontend dashboard
- Swagger API documentation
- SQLite database integration
- Workflow automation simulation
- REST API architecture

---

# Technologies Used

## Backend

- Python
- FastAPI
- SQLAlchemy
- Uvicorn

## Database

- SQLite

## Frontend

- HTML
- CSS
- JavaScript

## APIs & Architecture

- REST APIs
- JSON-based workflows

---

# System Workflow

1. User submits candidate resume
2. Backend analyzes resume content
3. Workflow engine detects technical skills
4. Candidate score is calculated
5. Experience level is determined
6. AI suggestions are generated
7. Resume analysis is stored in database
8. Hiring workflow history becomes available for review

---

# Architecture Diagram

![Architecture Diagram](architecture/system-design.png)

```text
Frontend Dashboard
        ↓
FastAPI Backend
        ↓
Resume Analysis Engine
        ↓
SQLite Database
        ↓
Candidate Review UI
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/analyze-resume` | Analyze candidate resume |
| GET | `/analyses` | Retrieve resume analysis history |

---

# Example Request

```json
{
  "resume_text": "Python developer with experience in FastAPI, SQL, REST APIs, automation workflows, JavaScript, and AI tools."
}
```

---

# Example Response

```json
{
  "message": "Resume analyzed and saved successfully",
  "analysis": {
    "id": 1,
    "score": 74,
    "level": "Moderate",
    "skills_found": [
      "python",
      "fastapi",
      "sql",
      "api",
      "javascript",
      "automation",
      "ai",
      "database"
    ],
    "suggestions": [
      "Add your GitHub profile or project links.",
      "Add practical projects with short explanations."
    ],
    "status": "processed"
  }
}
```

---

# Screenshots

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Analysis Result

![Analysis Result](screenshots/analysis-result.png)

## Analysis History

![History](screenshots/history.png)

## API Documentation

![API Docs](screenshots/api-docs.png)

---

# Demo Video

[Watch Demo Video](demo/ai-resume-analyzer-demo.mp4)

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/NASRATULLAH786/ai-resume-analyzer.git
cd ai-resume-analyzer
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend Server

```bash
uvicorn app.main:app --reload --port 8083
```

---

## Open Swagger API Docs

```text
http://127.0.0.1:8083/docs
```

---

## Open Frontend

Open:

```text
frontend/index.html
```

---

# Environment Variables

Create local `.env` file:

```env
GROQ_API_KEY=
DATABASE_URL=sqlite:///./resume_analysis.db
MODEL_NAME=llama3-70b-8192
APP_ENV=development
```

---

# Project Structure

```text
ai-resume-analyzer/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── services/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── screenshots/
│
├── architecture/
│
├── demo/
│
├── requirements.txt
├── README.md
└── .env
```

---

# Technical Challenges

- Resume skill extraction
- Candidate scoring workflows
- Experience classification
- Frontend/backend synchronization
- Resume evaluation consistency
- Database persistence
- Error handling
- REST API integration
- Workflow scalability

---

# Future Improvements

- Real LLM integration
- PDF resume upload support
- OCR-based resume extraction
- Recruiter dashboard
- Multi-candidate comparison
- Resume ranking system
- Cloud deployment
- Analytics dashboard
- Semantic candidate matching
- ATS integration

---

# Project Impact

This project demonstrates practical AI automation engineering skills including:

- backend API development
- workflow automation
- AI evaluation systems
- operational workflow design
- frontend/backend integration
- database-driven workflow systems
- candidate analysis automation
- REST API architecture
- scalable backend system design

---

# Author

Nasratullah

GitHub:
https://github.com/NASRATULLAH786

---
