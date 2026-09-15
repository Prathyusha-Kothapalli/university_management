from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


class AlumniProfileCreate(BaseModel):
    student_id: UUID
    graduation_year: int
    current_company: str
    current_designation: str
    linkedin_url: Optional[str] = None
    is_mentor_available: bool = True


class AlumniProfileResponse(AlumniProfileCreate):
    id: UUID

    class Config:
        from_attributes = True


class EndowmentFundCreate(BaseModel):
    fund_name: str
    target_amount_usd: float = 100000.0
    category: str = "SCHOLARSHIP"


class EndowmentFundResponse(EndowmentFundCreate):
    id: UUID
    current_amount_usd: float
    is_active: bool

    class Config:
        from_attributes = True


class DonationCreate(BaseModel):
    alumni_profile_id: UUID
    fund_id: UUID
    amount_usd: float
    payment_reference: str


class DonationResponse(DonationCreate):
    id: UUID
    donated_at: datetime

    class Config:
        from_attributes = True
