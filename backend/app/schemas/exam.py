from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ExamCreate(BaseModel):
    course_offering_id: UUID
    title: str
    exam_type: str
    total_marks: float = 100.0
    passing_marks: float = 40.0


class ExamUpdate(BaseModel):
    course_offering_id: UUID | None = None
    title: str | None = None
    exam_type: str | None = None
    total_marks: float | None = None
    passing_marks: float | None = None


class ExamResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    title: str
    exam_type: str
    total_marks: float
    passing_marks: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
