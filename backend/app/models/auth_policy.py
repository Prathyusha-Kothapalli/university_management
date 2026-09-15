from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class AuthPolicy(Base):
    __tablename__ = "auth_policies"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("universities.id"),
        nullable=True,
        index=True
    )

    min_length: Mapped[int] = mapped_column(
        Integer,
        default=8,
        nullable=False
    )

    require_uppercase: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    require_lowercase: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    require_digits: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    require_symbols: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    max_login_attempts: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False
    )

    lockout_duration_minutes: Mapped[int] = mapped_column(
        Integer,
        default=15,
        nullable=False
    )

    session_idle_timeout_minutes: Mapped[int] = mapped_column(
        Integer,
        default=30,
        nullable=False
    )

    mfa_required_roles: Mapped[str] = mapped_column(
        String(255),
        default="admin,hod",
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
