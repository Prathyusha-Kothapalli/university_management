from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Integer, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class UserSession(Base):
    __tablename__ = "user_sessions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    session_token: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        unique=True,
        index=True
    )

    refresh_token_hash: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False
    )

    user_agent: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    device_type: Mapped[str] = mapped_column(
        String(50),
        default="unknown"
    )

    operating_system: Mapped[str] = mapped_column(
        String(100),
        default="unknown"
    )

    browser: Mapped[str] = mapped_column(
        String(100),
        default="unknown"
    )

    country: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    anomaly_risk_score: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    is_trusted_device: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    last_active_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
