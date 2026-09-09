from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Classroom(Base):
    __tablename__ = "classrooms"

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
        String(100),
        nullable=False
    )

    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
        index=True
    )

    building: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    floor: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    room_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="CLASSROOM"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
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

    campus = relationship(
        "Campus",
        back_populates="classrooms"
    )

    timetables = relationship(
        "Timetable",
        back_populates="classroom",
        cascade="all, delete-orphan"
    )