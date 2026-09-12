from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TranscriptCreate(BaseModel):
    student_id: UUID
    academic_year_id: UUID
    semester_id: UUID
    gpa: float
    cgpa: float
    total_credits: int = 0
    status: str = "ISSUED"
    issue_date: datetime | None = None


class TranscriptUpdate(BaseModel):
    student_id: UUID | None = None
    academic_year_id: UUID | None = None
    semester_id: UUID | None = None
    gpa: float | None = None
    cgpa: float | None = None
    total_credits: int | None = None
    status: str | None = None
    issue_date: datetime | None = None


class TranscriptResponse(BaseModel):
    id: UUID
    student_id: UUID
    academic_year_id: UUID
    semester_id: UUID
    gpa: float
    cgpa: float
    total_credits: int
    status: str
    issue_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
