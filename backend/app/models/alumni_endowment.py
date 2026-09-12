from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class AlumniProfile(Base):
    __tablename__ = "alumni_profiles"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    graduation_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    current_company: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    current_designation: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(250),
        nullable=True
    )

    is_mentor_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


class EndowmentFund(Base):
    __tablename__ = "endowment_funds"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    fund_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    target_amount_usd: Mapped[float] = mapped_column(
        Float,
        default=100000.0
    )

    current_amount_usd: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    category: Mapped[str] = mapped_column(
        String(50), # SCHOLARSHIP, RESEARCH_CHAIR, CAMPUS_EXPANSION, ATHLETICS
        default="SCHOLARSHIP"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


class AlumniDonation(Base):
    __tablename__ = "alumni_donations"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    alumni_profile_id: Mapped[UUID] = mapped_column(
        ForeignKey("alumni_profiles.id"),
        nullable=False,
        index=True
    )

    fund_id: Mapped[UUID] = mapped_column(
        ForeignKey("endowment_funds.id"),
        nullable=False
    )

    amount_usd: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    payment_reference: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    donated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
