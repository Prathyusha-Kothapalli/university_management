from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class FacultyDepartment(Base):
    __tablename__ = "faculty_departments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    faculty_id: Mapped[UUID] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=False
    )

    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False
    )

    is_primary: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
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

    faculty = relationship(
        "Faculty",
        back_populates="departments"
    )

    department = relationship("Department")