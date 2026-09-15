from datetime import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field


class InstallmentPlanCreate(BaseModel):
    student_fee_id: UUID
    total_installments: int = 3
    frequency_months: int = 1
    total_amount: float


class InstallmentSchema(BaseModel):
    id: UUID
    installment_number: int
    amount: float
    due_date: datetime
    status: str
    paid_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class InstallmentPlanResponse(BaseModel):
    id: UUID
    student_fee_id: UUID
    total_installments: int
    frequency_months: int
    total_amount: float
    is_approved: bool
    created_at: datetime
    installments: List[InstallmentSchema] = []

    class Config:
        from_attributes = True


class GatewayConfigCreate(BaseModel):
    provider_name: str # STRIPE, RAZORPAY, PAYPAL
    api_key_masked: str
    webhook_secret_masked: Optional[str] = None
    environment_mode: str = "SANDBOX"


class GatewayConfigResponse(GatewayConfigCreate):
    id: UUID
    is_active: bool

    class Config:
        from_attributes = True


class PaymentWebhookPayload(BaseModel):
    payment_id: UUID
    gateway_reference: str
    provider_name: str
    status: str # SUCCESS, FAILED
    raw_response: Optional[Dict[str, Any]] = None
