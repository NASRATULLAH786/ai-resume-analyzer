from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

from app.resume_analyzer import analyze_resume
from app.database import SessionLocal, ResumeAnalysis

app = FastAPI(title="AI Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeRequest(BaseModel):
    resume_text: str


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Running"}


@app.post("/analyze-resume")
def analyze(request: ResumeRequest):
    result = analyze_resume(request.resume_text)

    db = SessionLocal()

    record = ResumeAnalysis(
        resume_text=request.resume_text,
        score=result["score"],
        level=result["level"],
        skills_found=json.dumps(result["skills_found"]),
        suggestions=json.dumps(result["suggestions"])
    )

    db.add(record)
    db.commit()
    db.close()

    return result


@app.get("/analyses")
def get_analyses():
    db = SessionLocal()
    records = db.query(ResumeAnalysis).all()

    results = []

    for record in records:
        results.append({
            "id": record.id,
            "score": record.score,
            "level": record.level,
            "skills_found": json.loads(record.skills_found),
            "suggestions": json.loads(record.suggestions)
        })

    db.close()

    return results