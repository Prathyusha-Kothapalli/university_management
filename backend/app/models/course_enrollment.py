from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    enrollment_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="ENROLLED",
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
        back_populates="enrollments"
    )

    student = relationship(
        "Student",
        back_populates="course_enrollments"
    )