from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AssignmentSubmissionCreate(BaseModel):
    assignment_id: UUID
    student_id: UUID
    submission_date: datetime | None = None
    file_url: str | None = None
    remarks: str | None = None
    marks_obtained: float | None = None
    graded_at: datetime | None = None
    status: str = "SUBMITTED"


class AssignmentSubmissionUpdate(BaseModel):
    assignment_id: UUID | None = None
    student_id: UUID | None = None
    submission_date: datetime | None = None
    file_url: str | None = None
    remarks: str | None = None
    marks_obtained: float | None = None
    graded_at: datetime | None = None
    status: str | None = None


class AssignmentSubmissionResponse(BaseModel):
    id: UUID
    assignment_id: UUID
    student_id: UUID
    submission_date: datetime
    file_url: str | None
    remarks: str | None
    marks_obtained: float | None
    graded_at: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
