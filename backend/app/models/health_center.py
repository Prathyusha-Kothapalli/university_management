from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Text, DateTime, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    student_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )
    doctor_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    diagnosis: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    prescription: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    blood_group: Mapped[Optional[str]] = mapped_column(
        String(10),
        nullable=True,
    )
    allergies: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
    )
    visit_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class HealthAppointment(Base):
    __tablename__ = "health_appointments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    student_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )
    doctor_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    appointment_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    reason: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        String(50),
        default="SCHEDULED",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class PharmacyItem(Base):
    __tablename__ = "pharmacy_items"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    medicine_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )
    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    stock_quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    unit_price: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False,
    )
    reorder_level: Mapped[int] = mapped_column(
        Integer,
        default=10,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )


class HealthEmergencyAlert(Base):
    __tablename__ = "health_emergency_alerts"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    student_id: Mapped[UUID] = mapped_column(
        nullable=False,
    )
    location: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    emergency_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        String(50),
        default="OPEN",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
