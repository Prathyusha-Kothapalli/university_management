from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Transcript(Base):
    __tablename__ = "transcripts"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
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

    gpa: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    cgpa: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    total_credits: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="ISSUED",
        nullable=False
    )

    issue_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
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

    student = relationship("Student")

    academic_year = relationship("AcademicYear")

    semester = relationship("Semester")
