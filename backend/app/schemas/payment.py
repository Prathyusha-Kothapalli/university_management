from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PaymentCreate(BaseModel):
    student_fee_id: UUID
    student_id: UUID
    amount: float
    payment_date: datetime | None = None
    payment_method: str = "ONLINE"
    transaction_id: str | None = None
    status: str = "SUCCESS"


class PaymentUpdate(BaseModel):
    student_fee_id: UUID | None = None
    student_id: UUID | None = None
    amount: float | None = None
    payment_date: datetime | None = None
    payment_method: str | None = None
    transaction_id: str | None = None
    status: str | None = None


class PaymentResponse(BaseModel):
    id: UUID
    student_fee_id: UUID
    student_id: UUID
    amount: float
    payment_date: datetime
    payment_method: str
    transaction_id: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
