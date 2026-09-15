from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class AssignmentSubmission(Base):
    __tablename__ = "assignment_submissions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    assignment_id: Mapped[UUID] = mapped_column(
        ForeignKey("assignments.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    submission_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    file_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    remarks: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    marks_obtained: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    graded_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="SUBMITTED",
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

    assignment = relationship(
        "Assignment",
        back_populates="submissions"
    )

    student = relationship("Student")
