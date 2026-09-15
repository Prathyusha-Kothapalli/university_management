import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Float, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class ScholarshipApplication(Base):
    __tablename__ = "scholarship_applications"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    student_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    scholarship_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    scholarship_type: Mapped[str] = mapped_column(
        String(50), # MERIT, NEED_BASED, ATHLETIC, DEPARTMENT
        default="MERIT",
        nullable=False,
    )

    amount_awarded: Mapped[float] = mapped_column(
        Float,
        default=5000.0,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30), # PENDING, APPROVED, REJECTED, DISBURSED
        default="PENDING",
        nullable=False,
    )

    justification: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
