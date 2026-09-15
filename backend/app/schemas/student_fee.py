from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class StudentFeeCreate(BaseModel):
    student_id: UUID
    fee_structure_id: UUID
    total_amount: float
    paid_amount: float = 0.0
    due_date: datetime
    status: str = "PENDING"


class StudentFeeUpdate(BaseModel):
    student_id: UUID | None = None
    fee_structure_id: UUID | None = None
    total_amount: float | None = None
    paid_amount: float | None = None
    due_date: datetime | None = None
    status: str | None = None


class StudentFeeResponse(BaseModel):
    id: UUID
    student_id: UUID
    fee_structure_id: UUID
    total_amount: float
    paid_amount: float
    due_date: datetime
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
