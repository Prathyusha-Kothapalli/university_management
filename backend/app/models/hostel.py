from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Hostel(Base):
    __tablename__ = "hostels"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    campus_id: Mapped[UUID] = mapped_column(
        ForeignKey("campuses.id"),
        nullable=False,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    type: Mapped[str] = mapped_column(
        String(50),
        default="BOYS",
        nullable=False
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        default=100,
        nullable=False
    )

    warden_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
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

    campus = relationship("Campus")

    rooms = relationship(
        "HostelRoom",
        back_populates="hostel",
        cascade="all, delete-orphan"
    )
