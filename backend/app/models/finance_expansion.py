from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class FeeInstallmentPlan(Base):
    __tablename__ = "fee_installment_plans"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_fee_id: Mapped[UUID] = mapped_column(
        ForeignKey("student_fees.id"),
        nullable=False,
        index=True
    )

    total_installments: Mapped[int] = mapped_column(
        Integer,
        default=3
    )

    frequency_months: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    total_amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    is_approved: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    installments: Mapped[list["FeeInstallment"]] = relationship(cascade="all, delete-orphan")


class FeeInstallment(Base):
    __tablename__ = "fee_installments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    installment_plan_id: Mapped[UUID] = mapped_column(
        ForeignKey("fee_installment_plans.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    installment_number: Mapped[int] = mapped_column(
        Integer,
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

    status: Mapped[str] = mapped_column(
        String(20), # PENDING, PAID, OVERDUE, WAIVED
        default="PENDING"
    )

    paid_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )


class PaymentGatewayConfig(Base):
    __tablename__ = "payment_gateway_configs"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    provider_name: Mapped[str] = mapped_column(
        String(50), # STRIPE, RAZORPAY, PAYPAL, BILLDESK
        nullable=False
    )

    api_key_masked: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    webhook_secret_masked: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    environment_mode: Mapped[str] = mapped_column(
        String(20), # SANDBOX, PRODUCTION
        default="SANDBOX"
    )


class PaymentTransaction(Base):
    __tablename__ = "payment_transactions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    payment_id: Mapped[UUID] = mapped_column(
        ForeignKey("payments.id"),
        nullable=False,
        index=True
    )

    gateway_reference: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True
    )

    provider_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30), # INITIATED, SUCCESS, FAILED, REFUNDED
        default="INITIATED"
    )

    raw_response: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
