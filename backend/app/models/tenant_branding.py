from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class TenantBranding(Base):
    __tablename__ = "tenant_brandings"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False,
        unique=True,
        index=True
    )

    primary_color: Mapped[str] = mapped_column(
        String(20),
        default="#1E40AF"
    )

    secondary_color: Mapped[str] = mapped_column(
        String(20),
        default="#3B82F6"
    )

    accent_color: Mapped[str] = mapped_column(
        String(20),
        default="#10B981"
    )

    logo_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    favicon_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    custom_domain: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    portal_domain: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    custom_css: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    portal_title: Mapped[str] = mapped_column(
        String(150),
        default="UniSphere Portal"
    )

    email_sender_name: Mapped[str] = mapped_column(
        String(150),
        default="UniSphere Portal"
    )

    support_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    is_whitelabel_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False
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
