from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BookIssueCreate(BaseModel):
    book_id: UUID
    student_id: UUID
    issue_date: datetime | None = None
    due_date: datetime
    return_date: datetime | None = None
    status: str = "ISSUED"


class BookIssueUpdate(BaseModel):
    book_id: UUID | None = None
    student_id: UUID | None = None
    issue_date: datetime | None = None
    due_date: datetime | None = None
    return_date: datetime | None = None
    status: str | None = None


class BookIssueResponse(BaseModel):
    id: UUID
    book_id: UUID
    student_id: UUID
    issue_date: datetime
    due_date: datetime
    return_date: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
