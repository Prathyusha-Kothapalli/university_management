import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.exam_expansion import (
    QuestionBankItemCreate,
    QuestionBankItemResponse,
    ExamPaperCreate,
    ExamPaperResponse,
    ProctorTelemetryCreate,
    ProctorTelemetryResponse,
)
from app.services import exam_expansion_service

router = APIRouter(prefix="/exam-expansion", tags=["Exam Expansion"])


@router.post("/question-bank", response_model=QuestionBankItemResponse, status_code=status.HTTP_201_CREATED)
def create_question_item(
    data: QuestionBankItemCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Add a question item to the institutional question bank."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return exam_expansion_service.create_question_item(
        db=db,
        created_by_id=user_id,
        data=data,
    )


@router.post("/exam-papers", response_model=ExamPaperResponse, status_code=status.HTTP_201_CREATED)
def generate_exam_paper(
    data: ExamPaperCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Assemble and generate an official examination paper."""
    user_id = uuid.UUID(current_user["id"]) if isinstance(current_user["id"], str) else current_user["id"]
    return exam_expansion_service.generate_exam_paper(
        db=db,
        created_by_id=user_id,
        data=data,
    )


@router.post("/proctor-telemetry", response_model=ProctorTelemetryResponse, status_code=status.HTTP_201_CREATED)
def log_proctor_anomaly(
    data: ProctorTelemetryCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Log an AI proctoring telemetry anomaly event during an online exam session."""
    return exam_expansion_service.log_proctor_telemetry(
        db=db,
        data=data,
    )
