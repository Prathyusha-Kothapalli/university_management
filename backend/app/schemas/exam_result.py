from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ExamResultCreate(BaseModel):
    exam_id: UUID
    student_id: UUID
    marks_obtained: float
    grade: str | None = None
    remarks: str | None = None


class ExamResultUpdate(BaseModel):
    exam_id: UUID | None = None
    student_id: UUID | None = None
    marks_obtained: float | None = None
    grade: str | None = None
    remarks: str | None = None


class ExamResultResponse(BaseModel):
    id: UUID
    exam_id: UUID
    student_id: UUID
    marks_obtained: float
    grade: str | None
    remarks: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
