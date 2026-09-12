from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class VehicleFuelLog(Base):
    __tablename__ = "vehicle_fuel_logs"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        ForeignKey("transport_vehicles.id"),
        nullable=False,
        index=True
    )

    fuel_liters: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    cost_amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    odometer_reading: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    filled_by_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class VehicleMaintenanceLog(Base):
    __tablename__ = "vehicle_maintenance_logs"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        ForeignKey("transport_vehicles.id"),
        nullable=False,
        index=True
    )

    service_type: Mapped[str] = mapped_column(
        String(50), # OIL_CHANGE, TIRE_ROTATION, ENGINE_OVERHAUL, BRAKE_INSPECTION
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    cost_amount: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    status: Mapped[str] = mapped_column(
        String(20), # SCHEDULED, IN_PROGRESS, COMPLETED
        default="SCHEDULED"
    )

    scheduled_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    completed_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )


class HostelMaintenanceTicket(Base):
    __tablename__ = "hostel_maintenance_tickets"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_room_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostel_rooms.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )

    issue_category: Mapped[str] = mapped_column(
        String(50), # PLUMBING, ELECTRICAL, FURNITURE, CLEANING, AC_HVAC
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        String(20), # LOW, MEDIUM, HIGH, EMERGENCY
        default="MEDIUM"
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30), # OPEN, ASSIGNED, RESOLVED, CLOSED
        default="OPEN"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
