import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AdmissionApplication(Base):
    __tablename__ = "admission_applications"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    applicant_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    phone: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    program_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("programs.id"),
        nullable=False,
    )

    university_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("universities.id"),
        nullable=False,
        index=True,
    )

    academic_year: Mapped[str] = mapped_column(
        String(20),
        default="2026-2027",
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30), # DRAFT, SUBMITTED, UNDER_REVIEW, EXAM_REGISTERED, OFFERED, ENROLLED, REJECTED
        default="SUBMITTED",
        nullable=False,
        index=True,
    )

    gpa_score: Mapped[float] = mapped_column(
        Float,
        default=3.5,
        nullable=False,
    )

    entrance_exam_score: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True,
    )

    merit_rank: Mapped[Optional[int]] = mapped_column(
        Float,
        nullable=True,
    )

    documents_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    reviewer_notes: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
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
