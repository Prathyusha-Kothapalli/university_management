from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_fee_id: Mapped[UUID] = mapped_column(
        ForeignKey("student_fees.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    payment_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
        default="ONLINE",
        nullable=False
    )

    transaction_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="SUCCESS",
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

    student_fee = relationship(
        "StudentFee",
        back_populates="payments"
    )

    student = relationship("Student")
