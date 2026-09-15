from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ExamResult(Base):
    __tablename__ = "exam_results"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    exam_id: Mapped[UUID] = mapped_column(
        ForeignKey("exams.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    marks_obtained: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    grade: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    remarks: Mapped[str | None] = mapped_column(
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

    exam = relationship(
        "Exam",
        back_populates="results"
    )

    student = relationship("Student")
