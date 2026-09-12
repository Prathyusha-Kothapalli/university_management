from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


# --- Medical Record ---
class MedicalRecordCreate(BaseModel):
    student_id: UUID
    doctor_name: str
    diagnosis: str
    prescription: Optional[str] = None
    blood_group: Optional[str] = None
    allergies: Optional[str] = None


class MedicalRecordUpdate(BaseModel):
    doctor_name: Optional[str] = None
    diagnosis: Optional[str] = None
    prescription: Optional[str] = None
    blood_group: Optional[str] = None
    allergies: Optional[str] = None


class MedicalRecordResponse(BaseModel):
    id: UUID
    student_id: UUID
    doctor_name: str
    diagnosis: str
    prescription: Optional[str]
    blood_group: Optional[str]
    allergies: Optional[str]
    visit_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Health Appointment ---
class HealthAppointmentCreate(BaseModel):
    student_id: UUID
    doctor_name: str
    appointment_date: datetime
    reason: str


class HealthAppointmentUpdate(BaseModel):
    doctor_name: Optional[str] = None
    appointment_date: Optional[datetime] = None
    reason: Optional[str] = None
    status: Optional[str] = None


class HealthAppointmentResponse(BaseModel):
    id: UUID
    student_id: UUID
    doctor_name: str
    appointment_date: datetime
    reason: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Pharmacy Item ---
class PharmacyItemCreate(BaseModel):
    medicine_name: str
    category: str
    stock_quantity: int = 0
    unit_price: float = 0.0
    reorder_level: int = 10


class PharmacyItemUpdate(BaseModel):
    medicine_name: Optional[str] = None
    category: Optional[str] = None
    stock_quantity: Optional[int] = None
    unit_price: Optional[float] = None
    reorder_level: Optional[int] = None


class PharmacyItemResponse(BaseModel):
    id: UUID
    medicine_name: str
    category: str
    stock_quantity: int
    unit_price: float
    reorder_level: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Emergency Alert ---
class HealthEmergencyAlertCreate(BaseModel):
    student_id: UUID
    location: str
    emergency_type: str


class HealthEmergencyAlertResponse(BaseModel):
    id: UUID
    student_id: UUID
    location: str
    emergency_type: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
