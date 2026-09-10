from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class StudentFee(Base):
    __tablename__ = "student_fees"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    fee_structure_id: Mapped[UUID] = mapped_column(
        ForeignKey("fee_structures.id"),
        nullable=False,
        index=True
    )

    total_amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    paid_amount: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    due_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",
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

    fee_structure = relationship(
        "FeeStructure",
        back_populates="student_fees"
    )

    payments = relationship(
        "Payment",
        back_populates="student_fee",
        cascade="all, delete-orphan"
    )
