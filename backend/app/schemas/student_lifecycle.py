from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


class AcademicHoldCreate(BaseModel):
    student_id: UUID
    hold_type: str = "FINANCIAL" # FINANCIAL, DISCIPLINARY, DOCUMENT_MISSING
    reason: str


class AcademicHoldResponse(AcademicHoldCreate):
    id: UUID
    placed_by_id: UUID
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class StudentConductCaseCreate(BaseModel):
    student_id: UUID
    incident_title: str
    incident_description: str
    severity: str = "MINOR"
    action_taken: str


class StudentConductCaseResponse(StudentConductCaseCreate):
    id: UUID
    reported_by_id: UUID
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class SupportCaseCreate(BaseModel):
    student_id: UUID
    subject: str
    category: str = "ACADEMIC_ADVISING"
    priority: str = "MEDIUM"
    details: str


class SupportCaseResponse(SupportCaseCreate):
    id: UUID
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
