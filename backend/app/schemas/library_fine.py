from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LibraryFineCreate(BaseModel):
    book_issue_id: UUID
    student_id: UUID
    amount: float
    reason: str | None = None
    status: str = "UNPAID"
    paid_date: datetime | None = None


class LibraryFineUpdate(BaseModel):
    book_issue_id: UUID | None = None
    student_id: UUID | None = None
    amount: float | None = None
    reason: str | None = None
    status: str | None = None
    paid_date: datetime | None = None


class LibraryFineResponse(BaseModel):
    id: UUID
    book_issue_id: UUID
    student_id: UUID
    amount: float
    reason: str | None
    status: str
    paid_date: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
