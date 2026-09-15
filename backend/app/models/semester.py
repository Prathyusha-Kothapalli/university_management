from datetime import date, datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Semester(Base):
    __tablename__ = "semesters"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    academic_year_id: Mapped[UUID] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    semester_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    is_current: Mapped[bool] = mapped_column(
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

    academic_year = relationship(
        "AcademicYear",
        back_populates="semesters"
    )