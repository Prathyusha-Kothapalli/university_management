import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class EntranceExamResult(Base):
    __tablename__ = "entrance_exam_results"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    application_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("admission_applications.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    exam_code: Mapped[str] = mapped_column(
        String(50), # UNISPHERE_SAT_2026
        nullable=False,
    )

    total_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    percentile: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    result_status: Mapped[str] = mapped_column(
        String(20), # PASSED, FAILED, QUALIFIED
        default="QUALIFIED",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
