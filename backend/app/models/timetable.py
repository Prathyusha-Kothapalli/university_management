from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Timetable(Base):
    __tablename__ = "timetables"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    classroom_id: Mapped[UUID] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=False,
        index=True
    )

    day_of_week: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(
        Time,
        nullable=False
    )

    end_time: Mapped[datetime] = mapped_column(
        Time,
        nullable=False
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

    course_offering = relationship(
        "CourseOffering",
        back_populates="timetables"
    )

    classroom = relationship(
        "Classroom",
        back_populates="timetables"
    )

    attendance_sessions = relationship(
    "AttendanceSession",
    back_populates="timetable"
    )