from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CourseOffering(Base):
    __tablename__ = "course_offerings"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_id: Mapped[UUID] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False,
        index=True
    )

    academic_year_id: Mapped[UUID] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False,
        index=True
    )

    semester_id: Mapped[UUID] = mapped_column(
        ForeignKey("semesters.id"),
        nullable=False,
        index=True
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

    course = relationship(
        "Course",
        back_populates="offerings"
    )

    faculty_assignments = relationship(
        "CourseFaculty",
        back_populates="course_offering",
        cascade="all, delete-orphan"
    )

    enrollments = relationship(
        "CourseEnrollment",
        back_populates="course_offering",
        cascade="all, delete-orphan"
    )

    attendance_sessions = relationship(
    "AttendanceSession",
    back_populates="course_offering",
    cascade="all, delete-orphan"
    )

    timetables = relationship(
    "Timetable",
    back_populates="course_offering",
    cascade="all, delete-orphan"
    )