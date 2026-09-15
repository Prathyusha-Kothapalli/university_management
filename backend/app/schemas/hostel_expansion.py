from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


# --- Building Schemas ---
class HostelBuildingBase(BaseModel):
    building_name: str
    code: str
    total_floors: int = 3
    total_capacity: int = 100
    warden_name: Optional[str] = None
    status: str = "ACTIVE"


class HostelBuildingCreate(HostelBuildingBase):
    hostel_id: UUID


class HostelBuildingUpdate(BaseModel):
    building_name: Optional[str] = None
    code: Optional[str] = None
    total_floors: Optional[int] = None
    total_capacity: Optional[int] = None
    warden_name: Optional[str] = None
    status: Optional[str] = None


class HostelBuildingResponse(HostelBuildingBase):
    id: UUID
    hostel_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


# --- Floor Schemas ---
class HostelFloorCreate(BaseModel):
    building_id: UUID
    floor_number: int
    floor_name: str
    room_count: int = 10
    capacity: int = 20
    gender_type: str = "ALL"


class HostelFloorResponse(HostelFloorCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


# --- Bed Schemas ---
class HostelBedBase(BaseModel):
    bed_number: str
    status: str = "AVAILABLE"  # AVAILABLE, OCCUPIED, RESERVED, MAINTENANCE, BLOCKED
    notes: Optional[str] = None


class HostelBedCreate(HostelBedBase):
    room_id: UUID


class HostelBedUpdate(BaseModel):
    bed_number: Optional[str] = None
    status: Optional[str] = None
    current_student_id: Optional[UUID] = None
    notes: Optional[str] = None


class HostelBedResponse(HostelBedBase):
    id: UUID
    room_id: UUID
    current_student_id: Optional[UUID] = None
    created_at: datetime

    class Config:
        from_attributes = True


# --- Application Schemas ---
class HostelApplicationCreate(BaseModel):
    student_id: UUID
    hostel_id: UUID
    preferred_room_type: str = "DOUBLE"
    remarks: Optional[str] = None
    medical_conditions: Optional[str] = None


class HostelApplicationStatusUpdate(BaseModel):
    status: str
    remarks: Optional[str] = None


class HostelApplicationResponse(BaseModel):
    id: UUID
    student_id: UUID
    hostel_id: UUID
    preferred_room_type: str
    application_date: datetime
    status: str
    remarks: Optional[str] = None
    medical_conditions: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


# --- Transfer Schemas ---
class HostelTransferCreate(BaseModel):
    student_id: UUID
    current_room_id: UUID
    target_room_id: UUID
    reason: str


class HostelTransferStatusUpdate(BaseModel):
    status: str
    approved_by_id: Optional[UUID] = None


class HostelTransferResponse(BaseModel):
    id: UUID
    student_id: UUID
    current_room_id: UUID
    target_room_id: UUID
    reason: str
    status: str
    approved_by_id: Optional[UUID] = None
    transfer_date: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True


# --- CheckIn & CheckOut Schemas ---
class HostelCheckInCreate(BaseModel):
    allocation_id: UUID
    student_id: UUID
    room_id: UUID
    key_issued: bool = True
    notes: Optional[str] = None


class HostelCheckInResponse(HostelCheckInCreate):
    id: UUID
    checkin_time: datetime

    class Config:
        from_attributes = True


class HostelCheckOutCreate(BaseModel):
    allocation_id: UUID
    student_id: UUID
    reason: str = "SEMESTER_END"
    key_returned: bool = True
    room_inspection_passed: bool = True
    dues_cleared: bool = True


class HostelCheckOutResponse(HostelCheckOutCreate):
    id: UUID
    checkout_time: datetime

    class Config:
        from_attributes = True


# --- Attendance Schemas ---
class HostelAttendanceRecordCreate(BaseModel):
    student_id: UUID
    room_id: UUID
    date: datetime
    status: str = "PRESENT"  # PRESENT, ABSENT, LATE_ENTRY, ON_LEAVE
    entry_time: Optional[str] = None
    notes: Optional[str] = None


class HostelAttendanceResponse(HostelAttendanceRecordCreate):
    id: UUID

    class Config:
        from_attributes = True


# --- Visitor Schemas ---
class HostelVisitorCreate(BaseModel):
    student_id: UUID
    visitor_name: str
    relation: str
    contact_phone: str
    purpose: str


class HostelVisitorStatusUpdate(BaseModel):
    status: str
    check_out_time: Optional[datetime] = None


class HostelVisitorResponse(HostelVisitorCreate):
    id: UUID
    check_in_time: datetime
    check_out_time: Optional[datetime] = None
    status: str

    class Config:
        from_attributes = True


# --- Complaint Schemas ---
class HostelComplaintCreate(BaseModel):
    student_id: UUID
    hostel_id: UUID
    room_number: str
    category: str = "PLUMBING"
    priority: str = "MEDIUM"
    subject: str
    description: str


class HostelComplaintUpdate(BaseModel):
    status: Optional[str] = None
    assigned_to_id: Optional[UUID] = None
    resolution_notes: Optional[str] = None


class HostelComplaintResponse(HostelComplaintCreate):
    id: UUID
    status: str
    assigned_to_id: Optional[UUID] = None
    resolution_notes: Optional[str] = None
    created_at: datetime
    resolved_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# --- Maintenance Schemas ---
class HostelMaintenanceCreate(BaseModel):
    hostel_id: UUID
    room_id: Optional[UUID] = None
    issue_type: str
    description: str
    priority: str = "MEDIUM"
    technician_name: Optional[str] = None
    estimated_cost: float = 0.0


class HostelMaintenanceUpdate(BaseModel):
    status: Optional[str] = None
    technician_name: Optional[str] = None
    actual_cost: Optional[float] = None


class HostelMaintenanceResponse(HostelMaintenanceCreate):
    id: UUID
    status: str
    actual_cost: float
    created_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# --- Mess & Feedback Schemas ---
class HostelMessCreate(BaseModel):
    hostel_id: UUID
    day_of_week: str
    meal_type: str = "LUNCH"
    menu_items: str
    timing: str = "12:30 PM - 02:30 PM"


class HostelMessResponse(HostelMessCreate):
    id: UUID

    class Config:
        from_attributes = True


class HostelMealFeedbackCreate(BaseModel):
    student_id: UUID
    mess_id: UUID
    rating: int = 5
    quality_score: int = 5
    cleanliness_score: int = 5
    comments: Optional[str] = None


class HostelMealFeedbackResponse(HostelMealFeedbackCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


# --- Incident Schemas ---
class HostelIncidentCreate(BaseModel):
    hostel_id: UUID
    student_id: Optional[UUID] = None
    incident_type: str
    severity: str = "MEDIUM"
    description: str
    action_taken: Optional[str] = None


class HostelIncidentResponse(HostelIncidentCreate):
    id: UUID
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# --- Announcement Schemas ---
class HostelAnnouncementCreate(BaseModel):
    hostel_id: Optional[UUID] = None
    title: str
    content: str
    target_audience: str = "ALL"
    is_emergency: bool = False


class HostelAnnouncementResponse(HostelAnnouncementCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


# --- Dashboard Overview Response ---
class HostelDashboardOverview(BaseModel):
    total_hostels: int
    total_buildings: int
    total_floors: int
    total_rooms: int
    total_beds: int
    occupied_beds: int
    available_beds: int
    reserved_beds: int
    maintenance_beds: int
    vacant_rooms: int
    partially_occupied_rooms: int
    full_rooms: int
    occupancy_percentage: float
    current_residents: int
    pending_applications: int
    pending_allocations: int
    pending_room_transfers: int
    open_complaints: int
    maintenance_requests: int
    outstanding_hostel_fees: float


class HostelKpiCards(BaseModel):
    total_students: int
    total_residents: int
    available_beds: int
    occupied_beds: int
    occupancy_rate: float
    pending_applications: int
    pending_allocations: int
    open_complaints: int
    maintenance_requests: int
    fee_due: float
    visitors_today: int
    checkins_today: int
    checkouts_today: int


class HostelAnalyticsResponse(BaseModel):
    occupancy_by_hostel: Dict[str, int]
    occupancy_by_building: Dict[str, int]
    occupancy_by_room_type: Dict[str, int]
    occupied_vs_available: Dict[str, int]
    monthly_occupancy_trend: List[Dict[str, Any]]
    gender_wise_occupancy: Dict[str, int]
    fee_analytics: Dict[str, float]
    complaint_resolution_metrics: Dict[str, int]
    mess_satisfaction_score: float
