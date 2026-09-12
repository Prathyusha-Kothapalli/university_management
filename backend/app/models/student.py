from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False
    )

    program_id: Mapped[UUID] = mapped_column(
        ForeignKey("programs.id"),
        nullable=False
    )

    admission_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    enrollment_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    current_semester_id: Mapped[UUID] = mapped_column(
        ForeignKey("semesters.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="active",
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

    user = relationship("User")

    university = relationship("University")

    department = relationship("Department")

    program = relationship("Program")

    current_semester = relationship("Semester")

    guardians = relationship(
        "StudentGuardian",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    attendance_records = relationship(
        "AttendanceRecord",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    course_enrollments = relationship(
        "CourseEnrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )