from datetime import datetime
import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.resume_analyzer import analyze_resume
from app.database import SessionLocal, ResumeAnalysis


app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered resume evaluation and candidate analysis workflow platform.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeRequest(BaseModel):
    resume_text: str = Field(
        ...,
        min_length=30,
        description="Resume content to analyze.",
        example="Python developer with experience in FastAPI, SQL, automation workflows, REST APIs, and AI tools.",
    )


@app.get(
    "/",
    summary="Health check",
    description="Checks whether the AI Resume Analyzer backend is running.",
)
def home():
    return {
        "message": "AI Resume Analyzer Running",
        "status": "active",
        "timestamp": datetime.utcnow(),
    }


@app.post(
    "/analyze-resume",
    summary="Analyze candidate resume",
    description="Analyzes resume skills, calculates candidate score, determines experience level, and stores analysis history.",
)
def analyze(request: ResumeRequest):
    try:
        result = analyze_resume(request.resume_text)

        required_fields = [
            "score",
            "level",
            "skills_found",
            "suggestions",
        ]

        for field in required_fields:
            if field not in result:
                raise HTTPException(
                    status_code=500,
                    detail=f"Missing required analysis field: {field}",
                )

        db = SessionLocal()

        record = ResumeAnalysis(
            resume_text=request.resume_text,
            score=result["score"],
            level=result["level"],
            skills_found=json.dumps(result["skills_found"]),
            suggestions=json.dumps(result["suggestions"]),
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return {
            "message": "Resume analyzed and saved successfully",
            "analysis": {
                "id": record.id,
                "score": record.score,
                "level": record.level,
                "skills_found": result["skills_found"],
                "suggestions": result["suggestions"],
                "status": "processed",
            },
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if "db" in locals():
            db.close()


@app.get(
    "/analyses",
    summary="Get resume analysis history",
    description="Returns all stored candidate resume analyses.",
)
def get_analyses():
    try:
        db = SessionLocal()
        records = db.query(ResumeAnalysis).all()

        return [
            {
                "id": record.id,
                "score": record.score,
                "level": record.level,
                "skills_found": json.loads(record.skills_found),
                "suggestions": json.loads(record.suggestions),
            }
            for record in records
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if "db" in locals():
            db.close()