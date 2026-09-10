from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    exam_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    total_marks: Mapped[float] = mapped_column(
        Float,
        default=100.0,
        nullable=False
    )

    passing_marks: Mapped[float] = mapped_column(
        Float,
        default=40.0,
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

    course_offering = relationship("CourseOffering")

    schedules = relationship(
        "ExamSchedule",
        back_populates="exam",
        cascade="all, delete-orphan"
    )

    results = relationship(
        "ExamResult",
        back_populates="exam",
        cascade="all, delete-orphan"
    )
