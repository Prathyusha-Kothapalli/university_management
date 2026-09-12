from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AssignmentCreate(BaseModel):
    course_offering_id: UUID
    faculty_id: UUID
    title: str
    description: str | None = None
    max_marks: float = 100.0
    due_date: datetime


class AssignmentUpdate(BaseModel):
    course_offering_id: UUID | None = None
    faculty_id: UUID | None = None
    title: str | None = None
    description: str | None = None
    max_marks: float | None = None
    due_date: datetime | None = None


class AssignmentResponse(BaseModel):
    id: UUID
    course_offering_id: UUID
    faculty_id: UUID
    title: str
    description: str | None
    max_marks: float
    due_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
