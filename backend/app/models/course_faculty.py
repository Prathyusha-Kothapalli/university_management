from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CourseFaculty(Base):
    __tablename__ = "course_faculty"

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

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    course_offering = relationship(
        "CourseOffering",
        back_populates="faculty_assignments"
    )

    faculty = relationship(
        "Faculty",
        back_populates="course_assignments"
    )