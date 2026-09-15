from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    faculty_id: Mapped[UUID] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    max_marks: Mapped[float] = mapped_column(
        Float,
        default=100.0,
        nullable=False
    )

    due_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
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

    faculty = relationship("Faculty")

    submissions = relationship(
        "AssignmentSubmission",
        back_populates="assignment",
        cascade="all, delete-orphan"
    )
