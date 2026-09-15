from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class HostelBuilding(Base):
    __tablename__ = "hostel_buildings"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    building_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    total_floors: Mapped[int] = mapped_column(
        Integer,
        default=3,
        nullable=False
    )

    total_capacity: Mapped[int] = mapped_column(
        Integer,
        default=100,
        nullable=False
    )

    warden_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="ACTIVE",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    hostel = relationship("Hostel")
    floors = relationship("HostelFloor", back_populates="building", cascade="all, delete-orphan")


class HostelFloor(Base):
    __tablename__ = "hostel_floors"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    building_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_buildings.id"),
        nullable=False,
        index=True
    )

    floor_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    floor_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    room_count: Mapped[int] = mapped_column(
        Integer,
        default=10,
        nullable=False
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        default=20,
        nullable=False
    )

    gender_type: Mapped[str] = mapped_column(
        String(50),
        default="ALL",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    building = relationship("HostelBuilding", back_populates="floors")


class HostelBed(Base):
    __tablename__ = "hostel_beds"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    room_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=False,
        index=True
    )

    bed_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="AVAILABLE",  # AVAILABLE, OCCUPIED, RESERVED, MAINTENANCE, BLOCKED
        nullable=False
    )

    current_student_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("students.id"),
        nullable=True,
        index=True
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    room = relationship("HostelRoom")
    student = relationship("Student")


class HostelApplication(Base):
    __tablename__ = "hostel_applications"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    preferred_room_type: Mapped[str] = mapped_column(
        String(50),
        default="DOUBLE",
        nullable=False
    )

    application_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="SUBMITTED",  # SUBMITTED, ELIGIBILITY_PASSED, DOCS_VERIFIED, APPROVED, REJECTED, WAITLISTED, ALLOCATED, ACTIVATED
        nullable=False
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    medical_conditions: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    student = relationship("Student")
    hostel = relationship("Hostel")


class HostelTransfer(Base):
    __tablename__ = "hostel_transfers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    current_room_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=False
    )

    target_room_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",  # PENDING, APPROVED, REJECTED, COMPLETED
        nullable=False
    )

    approved_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    transfer_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    student = relationship("Student")


class HostelCheckIn(Base):
    __tablename__ = "hostel_checkins"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    allocation_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_allocations.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    room_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=False
    )

    checkin_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    key_issued: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    checked_in_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    student = relationship("Student")
    room = relationship("HostelRoom")


class HostelCheckOut(Base):
    __tablename__ = "hostel_checkouts"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    allocation_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_allocations.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    checkout_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        String(255),
        default="SEMESTER_END",
        nullable=False
    )

    key_returned: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    room_inspection_passed: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    dues_cleared: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    checked_out_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    student = relationship("Student")


class HostelAttendance(Base):
    __tablename__ = "hostel_attendance"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    room_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=False,
        index=True
    )

    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        index=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PRESENT",  # PRESENT, ABSENT, LATE_ENTRY, ON_LEAVE
        nullable=False
    )

    entry_time: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    recorded_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    student = relationship("Student")
    room = relationship("HostelRoom")


class HostelVisitor(Base):
    __tablename__ = "hostel_visitors"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    visitor_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    relation: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    contact_phone: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    purpose: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    check_in_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    check_out_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="APPROVED",  # PENDING, APPROVED, REJECTED, CHECKED_OUT
        nullable=False
    )

    approved_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    student = relationship("Student")


class HostelComplaint(Base):
    __tablename__ = "hostel_complaints"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    room_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100),
        default="PLUMBING",  # PLUMBING, ELECTRICAL, FURNITURE, CLEANLINESS, NOISE, MESS, OTHER
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="MEDIUM",  # LOW, MEDIUM, HIGH, CRITICAL
        nullable=False
    )

    subject: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="OPEN",  # OPEN, ASSIGNED, IN_PROGRESS, RESOLVED, CLOSED, REOPENED
        nullable=False
    )

    assigned_to_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    resolution_notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    student = relationship("Student")
    hostel = relationship("Hostel")


class HostelMaintenanceRequest(Base):
    __tablename__ = "hostel_maintenance_requests"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    room_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=True
    )

    issue_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="MEDIUM",
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",  # PENDING, IN_PROGRESS, COMPLETED, CANCELLED
        nullable=False
    )

    technician_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    estimated_cost: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    actual_cost: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    hostel = relationship("Hostel")
    room = relationship("HostelRoom")


class HostelStaff(Base):
    __tablename__ = "hostel_staff"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    role_title: Mapped[str] = mapped_column(
        String(100),
        default="WARDEN",  # WARDEN, ASSISTANT_WARDEN, SECURITY, MAINTENANCE, CLEANER
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    shift: Mapped[str] = mapped_column(
        String(50),
        default="DAY",  # DAY, NIGHT, ROTATING
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship("User")
    hostel = relationship("Hostel")


class HostelShift(Base):
    __tablename__ = "hostel_shifts"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    staff_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_staff.id"),
        nullable=False,
        index=True
    )

    shift_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    shift_type: Mapped[str] = mapped_column(
        String(50),
        default="DAY",
        nullable=False
    )

    start_time: Mapped[str] = mapped_column(
        String(20),
        default="08:00",
        nullable=False
    )

    end_time: Mapped[str] = mapped_column(
        String(20),
        default="16:00",
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="SCHEDULED",  # SCHEDULED, COMPLETED, ABSENT, SWAPPED
        nullable=False
    )

    staff = relationship("HostelStaff")


class HostelInventory(Base):
    __tablename__ = "hostel_inventory"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    item_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100),
        default="FURNITURE",  # FURNITURE, BEDDING, ELECTRICAL, CLEANING, SAFETY
        nullable=False
    )

    total_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    allocated_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    damaged_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    hostel = relationship("Hostel")


class HostelMess(Base):
    __tablename__ = "hostel_mess"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    day_of_week: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    meal_type: Mapped[str] = mapped_column(
        String(50),
        default="LUNCH",  # BREAKFAST, LUNCH, DINNER, SNACKS
        nullable=False
    )

    menu_items: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    timing: Mapped[str] = mapped_column(
        String(100),
        default="12:30 PM - 02:30 PM",
        nullable=False
    )

    hostel = relationship("Hostel")


class HostelMealFeedback(Base):
    __tablename__ = "hostel_meal_feedbacks"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    mess_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_mess.id"),
        nullable=False,
        index=True
    )

    rating: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False
    )

    quality_score: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False
    )

    cleanliness_score: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False
    )

    comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    student = relationship("Student")
    mess = relationship("HostelMess")


class HostelIncident(Base):
    __tablename__ = "hostel_incidents"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("students.id"),
        nullable=True,
        index=True
    )

    incident_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        default="MEDIUM",  # LOW, MEDIUM, HIGH, EMERGENCY
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    action_taken: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    reported_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="REPORTED",  # REPORTED, INVESTIGATING, RESOLVED, CLOSED
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    hostel = relationship("Hostel")
    student = relationship("Student")


class HostelAnnouncement(Base):
    __tablename__ = "hostel_announcements"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    target_audience: Mapped[str] = mapped_column(
        String(50),
        default="ALL",  # ALL, STUDENTS, WARDENS, STAFF
        nullable=False
    )

    is_emergency: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    posted_by_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    hostel = relationship("Hostel")
