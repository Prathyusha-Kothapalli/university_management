from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field


class VehicleFuelLogCreate(BaseModel):
    vehicle_id: UUID
    fuel_liters: float
    cost_amount: float
    odometer_reading: float


class VehicleFuelLogResponse(VehicleFuelLogCreate):
    id: UUID
    filled_by_id: UUID
    logged_at: datetime

    class Config:
        from_attributes = True


class VehicleMaintenanceLogCreate(BaseModel):
    vehicle_id: UUID
    service_type: str # OIL_CHANGE, TIRE_ROTATION, ENGINE_OVERHAUL
    description: str
    cost_amount: float = 0.0
    scheduled_date: datetime = Field(default_factory=datetime.utcnow)


class VehicleMaintenanceLogResponse(VehicleMaintenanceLogCreate):
    id: UUID
    status: str
    completed_date: Optional[datetime] = None

    class Config:
        from_attributes = True


class HostelTicketCreate(BaseModel):
    hostel_room_id: UUID
    student_id: UUID
    issue_category: str # PLUMBING, ELECTRICAL, FURNITURE
    priority: str = "MEDIUM"
    description: str


class HostelTicketResponse(HostelTicketCreate):
    id: UUID
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
