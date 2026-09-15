from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class LostItem(Base):
    __tablename__ = "lost_items"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    reporter_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )
    item_title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )
    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    location_lost: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    date_lost: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    contact_number: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )
    status: Mapped[str] = mapped_column(
        String(50),
        default="OPEN",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )


class ItemClaim(Base):
    __tablename__ = "item_claims"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    item_id: Mapped[UUID] = mapped_column(
        ForeignKey("lost_items.id"),
        nullable=False,
        index=True,
    )
    claimant_id: Mapped[UUID] = mapped_column(
        nullable=False,
    )
    proof_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
