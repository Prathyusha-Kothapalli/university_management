from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class HostelRoom(Base):
    __tablename__ = "hostel_rooms"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    hostel_id: Mapped[UUID] = mapped_column(
        ForeignKey("hostels.id"),
        nullable=False,
        index=True
    )

    room_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    floor: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        default=2,
        nullable=False
    )

    occupied_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    monthly_fee: Mapped[float] = mapped_column(
        Float,
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

    hostel = relationship(
        "Hostel",
        back_populates="rooms"
    )

    allocations = relationship(
        "HostelAllocation",
        back_populates="room",
        cascade="all, delete-orphan"
    )
