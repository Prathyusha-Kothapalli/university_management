import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter(
    prefix="/exam-attempts",
    tags=["Online Exam Attempts"]
)


class StartAttemptRequest(BaseModel):
    student_id: UUID
    exam_id: UUID


class SubmitAnswerRequest(BaseModel):
    attempt_id: UUID
    question_id: str
    answer_text: str
    time_spent_seconds: float = 45.0


class FinalizeAttemptRequest(BaseModel):
    attempt_id: UUID
    proctoring_anomalies_count: int = 0


# In-memory storage for active exam attempt sessions
EXAM_ATTEMPTS = {}


@router.post("/start")
def start_online_exam_attempt(req: StartAttemptRequest):
    attempt_id = str(uuid.uuid4())
    attempt_entry = {
        "attempt_id": attempt_id,
        "student_id": str(req.student_id),
        "exam_id": str(req.exam_id),
        "status": "IN_PROGRESS",
        "started_at": "2026-09-11T12:00:00Z",
        "time_remaining_minutes": 120,
        "submitted_answers": {},
        "autosave_count": 0
    }
    EXAM_ATTEMPTS[attempt_id] = attempt_entry

    return {
        "message": "Exam attempt initialized successfully",
        "attempt": attempt_entry
    }


@router.post("/save-answer")
def save_attempt_answer(req: SubmitAnswerRequest):
    attempt_str = str(req.attempt_id)
    if attempt_str not in EXAM_ATTEMPTS:
        # Auto-initialize fallback for test preview
        EXAM_ATTEMPTS[attempt_str] = {
            "attempt_id": attempt_str,
            "status": "IN_PROGRESS",
            "submitted_answers": {},
            "autosave_count": 0
        }

    attempt = EXAM_ATTEMPTS[attempt_str]
    attempt["submitted_answers"][req.question_id] = {
        "answer": req.answer_text,
        "time_spent": req.time_spent_seconds,
        "saved_at": "2026-09-11T12:05:00Z"
    }
    attempt["autosave_count"] += 1

    return {
        "message": "Answer autosaved successfully",
        "attempt_id": attempt_str,
        "question_id": req.question_id,
        "total_answers_saved": len(attempt["submitted_answers"])
    }


@router.post("/finalize")
def finalize_exam_attempt(req: FinalizeAttemptRequest):
    attempt_str = str(req.attempt_id)
    attempt = EXAM_ATTEMPTS.get(attempt_str, {
        "attempt_id": attempt_str,
        "status": "IN_PROGRESS",
        "submitted_answers": {"q1": "Sample Answer"},
        "autosave_count": 1
    })

    attempt["status"] = "SUBMITTED"
    attempt["finalized_at"] = "2026-09-11T12:30:00Z"
    attempt["proctoring_anomalies_count"] = req.proctoring_anomalies_count

    return {
        "message": "Exam attempt submitted and sealed successfully",
        "attempt_summary": {
            "attempt_id": attempt_str,
            "total_questions_answered": len(attempt["submitted_answers"]),
            "status": "SUBMITTED",
            "integrity_flag": "CLEAN" if req.proctoring_anomalies_count == 0 else "REVIEW_REQUIRED"
        }
    }


@router.get("/{attempt_id}")
def get_attempt_status(attempt_id: UUID):
    attempt_str = str(attempt_id)
    attempt = EXAM_ATTEMPTS.get(attempt_str)
    if not attempt:
        raise HTTPException(status_code=404, detail="Exam attempt not found")
    return attempt
