import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class MeritList(Base):
    __tablename__ = "merit_lists"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    program_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("programs.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    round_number: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    cutoff_percentage: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    total_seats: Mapped[int] = mapped_column(
        Integer,
        default=60,
        nullable=False,
    )

    filled_seats: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20), # DRAFT, PUBLISHED, CLOSED
        default="PUBLISHED",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
