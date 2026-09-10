from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class FeeStructure(Base):
    __tablename__ = "fee_structures"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False,
        index=True
    )

    program_id: Mapped[UUID] = mapped_column(
        ForeignKey("programs.id"),
        nullable=False,
        index=True
    )

    academic_year_id: Mapped[UUID] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Float,
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

    university = relationship("University")

    program = relationship("Program")

    academic_year = relationship("AcademicYear")

    student_fees = relationship(
        "StudentFee",
        back_populates="fee_structure",
        cascade="all, delete-orphan"
    )
