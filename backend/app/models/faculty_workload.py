import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Float, Integer, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class FacultyWorkload(Base):
    __tablename__ = "faculty_workloads"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    faculty_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("faculty.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    academic_year_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("academic_years.id"),
        nullable=False,
    )

    teaching_hours: Mapped[float] = mapped_column(
        Float,
        default=12.0,
        nullable=False,
    )

    research_hours: Mapped[float] = mapped_column(
        Float,
        default=8.0,
        nullable=False,
    )

    admin_hours: Mapped[float] = mapped_column(
        Float,
        default=4.0,
        nullable=False,
    )

    total_credit_load: Mapped[float] = mapped_column(
        Float,
        default=24.0,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20), # BALANCED, OVERLOADED, UNDERLOADED
        default="BALANCED",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
