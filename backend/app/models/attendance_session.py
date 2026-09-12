from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class AttendanceSession(Base):
    __tablename__ = "attendance_sessions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    timetable_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("timetables.id"),
        nullable=True,
        index=True
    )

    session_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    topic: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="OPEN",
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

    course_offering = relationship(
        "CourseOffering",
        back_populates="attendance_sessions"
    )

    timetable = relationship(
        "Timetable",
        back_populates="attendance_sessions"
    )

    attendance_records = relationship(
        "AttendanceRecord",
        back_populates="attendance_session",
        cascade="all, delete-orphan"
    )