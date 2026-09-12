import uuid
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.exam import Exam
from app.schemas.exam import (
    ExamCreate,
    ExamUpdate,
    ExamResponse,
)


router = APIRouter(
    prefix="/exams",
    tags=["Exams"]
)


class QuestionCreate(BaseModel):
    course_code: str
    prompt: str
    bloom_level: str = "Apply"  # Remember, Understand, Apply, Analyze, Evaluate, Create
    difficulty: str = "Medium"  # Easy, Medium, Hard
    marks: int = 5
    topic: str = "General"


class PaperGenerateRequest(BaseModel):
    course_code: str
    total_marks: int = 50
    easy_ratio: float = 0.3
    medium_ratio: float = 0.5
    hard_ratio: float = 0.2


class ProctorTelemetry(BaseModel):
    student_id: UUID
    tab_switch_count: int = 0
    face_count_detected: int = 1
    mic_audio_db: float = 12.5
    browser_focus_lost_seconds: float = 0.0


# In-memory storage for questions, generated papers, and proctor logs
QUESTION_BANK = []
PROCTOR_LOGS = {}


@router.post(
    "/",
    response_model=ExamResponse
)
def create_exam(
    exam_data: ExamCreate,
    db: Session = Depends(get_db)
):
    try:
        exam = Exam(
            **exam_data.model_dump()
        )

        db.add(exam)
        db.commit()
        db.refresh(exam)

        return exam

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ExamResponse]
)
def get_exams(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Exam)
    )

    return result.scalars().all()


@router.post("/questions")
def add_question_to_bank(q: QuestionCreate):
    q_id = str(uuid.uuid4())
    entry = {
        "id": q_id,
        "course_code": q.course_code,
        "prompt": q.prompt,
        "bloom_level": q.bloom_level,
        "difficulty": q.difficulty,
        "marks": q.marks,
        "topic": q.topic,
        "created_at": "2026-09-11T11:55:00Z"
    }
    QUESTION_BANK.append(entry)

    return {
        "message": "Question added to bank",
        "question": entry
    }


@router.get("/questions")
def get_question_bank(course_code: Optional[str] = None):
    if course_code:
        filtered = [q for q in QUESTION_BANK if q["course_code"] == course_code]
    else:
        filtered = QUESTION_BANK

    return {
        "total_questions": len(filtered),
        "questions": filtered
    }


@router.post("/generate-paper")
def generate_exam_paper(req: PaperGenerateRequest):
    course_questions = [q for q in QUESTION_BANK if q["course_code"] == req.course_code]

    if not course_questions:
        # Default generated paper structure for preview
        course_questions = [
            {"id": "q-101", "prompt": "Define Multi-Agent Orchestration.", "bloom_level": "Remember", "difficulty": "Easy", "marks": 10},
            {"id": "q-102", "prompt": "Analyze vector embedding similarity mechanisms.", "bloom_level": "Analyze", "difficulty": "Medium", "marks": 15},
            {"id": "q-103", "prompt": "Design a high-concurrency micro-tenant architecture.", "bloom_level": "Create", "difficulty": "Hard", "marks": 25},
        ]

    paper_id = str(uuid.uuid4())
    total_marks = sum(q["marks"] for q in course_questions)

    return {
        "paper_id": paper_id,
        "course_code": req.course_code,
        "target_total_marks": req.total_marks,
        "generated_total_marks": total_marks,
        "questions_count": len(course_questions),
        "questions": course_questions,
        "generated_at": "2026-09-11T11:55:00Z"
    }


@router.post("/{exam_id}/proctor-log")
def log_proctor_telemetry(exam_id: UUID, telemetry: ProctorTelemetry):
    exam_str = str(exam_id)
    student_str = str(telemetry.student_id)

    if exam_str not in PROCTOR_LOGS:
        PROCTOR_LOGS[exam_str] = []

    # Calculate integrity threat score
    threat_score = 0
    flags = []

    if telemetry.tab_switch_count > 3:
        threat_score += 35
        flags.append("EXCESSIVE_TAB_SWITCHING")

    if telemetry.face_count_detected == 0:
        threat_score += 40
        flags.append("NO_FACE_DETECTED")
    elif telemetry.face_count_detected > 1:
        threat_score += 50
        flags.append("MULTIPLE_FACES_DETECTED")

    if telemetry.browser_focus_lost_seconds > 15.0:
        threat_score += 25
        flags.append("BROWSER_UNFOCUSED")

    log_entry = {
        "id": str(uuid.uuid4()),
        "exam_id": exam_str,
        "student_id": student_str,
        "telemetry": telemetry.model_dump(),
        "integrity_threat_score": min(threat_score, 100),
        "anomaly_flags": flags,
        "timestamp": "2026-09-11T11:55:00Z"
    }

    PROCTOR_LOGS[exam_str].append(log_entry)

    return {
        "message": "Proctoring telemetry logged",
        "log": log_entry
    }


@router.get("/{exam_id}/proctor-log")
def get_proctor_logs(exam_id: UUID):
    exam_str = str(exam_id)
    logs = PROCTOR_LOGS.get(exam_str, [])

    return {
        "exam_id": exam_str,
        "total_log_entries": len(logs),
        "flagged_sessions_count": len([l for l in logs if l["integrity_threat_score"] > 30]),
        "logs": logs
    }


@router.get(
    "/{exam_id}",
    response_model=ExamResponse
)
def get_exam(
    exam_id: UUID,
    db: Session = Depends(get_db)
):
    exam = db.get(
        Exam,
        exam_id
    )

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    return exam


@router.put(
    "/{exam_id}",
    response_model=ExamResponse
)
def update_exam(
    exam_id: UUID,
    exam_data: ExamUpdate,
    db: Session = Depends(get_db)
):
    exam = db.get(
        Exam,
        exam_id
    )

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    try:
        update_data = exam_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(exam, key):
                setattr(
                    exam,
                    key,
                    value
                )

        db.commit()
        db.refresh(exam)

        return exam

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{exam_id}")
def delete_exam(
    exam_id: UUID,
    db: Session = Depends(get_db)
):
    exam = db.get(
        Exam,
        exam_id
    )

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    db.delete(exam)
    db.commit()

    return {
        "message": "Exam deleted successfully"
    }

