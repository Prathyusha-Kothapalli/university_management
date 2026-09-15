from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class University(Base):
    __tablename__ = "universities"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    contact_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    contact_phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
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

    campuses = relationship(
        "Campus",
        back_populates="university",
        cascade="all, delete-orphan"
    )

    departments = relationship(
        "Department",
        back_populates="university"
    )

    academic_years = relationship(
        "AcademicYear",
        back_populates="university",
        cascade="all, delete-orphan"
    )