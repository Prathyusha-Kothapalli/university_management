from datetime import datetime, time
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ExamSchedule(Base):
    __tablename__ = "exam_schedules"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    exam_id: Mapped[UUID] = mapped_column(
        ForeignKey("exams.id"),
        nullable=False,
        index=True
    )

    classroom_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("classrooms.id"),
        nullable=True,
        index=True
    )

    invigilator_faculty_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=True,
        index=True
    )

    exam_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    start_time: Mapped[time | None] = mapped_column(
        Time,
        nullable=True
    )

    end_time: Mapped[time | None] = mapped_column(
        Time,
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

    exam = relationship(
        "Exam",
        back_populates="schedules"
    )

    classroom = relationship("Classroom")

    invigilator = relationship("Faculty")
