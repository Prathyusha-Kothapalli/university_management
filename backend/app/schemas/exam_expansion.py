from datetime import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field


class QuestionBankItemCreate(BaseModel):
    course_id: UUID
    question_type: str = "MCQ" # MCQ, SHORT_ANSWER, ESSAY, CODING
    difficulty_level: str = "MEDIUM"
    question_text: str
    options: Optional[Dict[str, Any]] = None
    correct_answer: str
    points: float = 1.0


class QuestionBankItemResponse(QuestionBankItemCreate):
    id: UUID
    created_by_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class ExamPaperCreate(BaseModel):
    course_offering_id: UUID
    title: str
    total_marks: float = 100.0
    duration_minutes: int = 120
    question_ids: List[UUID] = []


class ExamPaperResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    title: str
    total_marks: float
    duration_minutes: int
    is_published: bool
    created_by_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class ProctorTelemetryCreate(BaseModel):
    student_id: UUID
    exam_paper_id: UUID
    anomaly_type: str # FACE_NOT_DETECTED, MULTIPLE_FACES, NOISE_DETECTED
    confidence_score: float = 0.95
    snapshot_url: Optional[str] = None


class ProctorTelemetryResponse(ProctorTelemetryCreate):
    id: UUID
    logged_at: datetime

    class Config:
        from_attributes = True
