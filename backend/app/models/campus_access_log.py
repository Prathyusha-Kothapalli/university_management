import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class CampusAccessLog(Base):
    __tablename__ = "campus_access_logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    card_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    gate_name: Mapped[str] = mapped_column(
        String(100),
        default="Main Gate Turnstile 1",
        nullable=False,
    )

    access_type: Mapped[str] = mapped_column(
        String(10), # ENTRY, EXIT
        default="ENTRY",
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20), # GRANTED, DENIED, EXPIRED
        default="GRANTED",
        nullable=False,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
