from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class TenantInvitation(Base):
    __tablename__ = "tenant_invitations"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    role_name: Mapped[str] = mapped_column(
        String(50),
        default="student",
        nullable=False
    )

    invitation_token: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )

    invited_by_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    is_accepted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    accepted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
