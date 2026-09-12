from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class CourseOutcome(Base):
    __tablename__ = "course_outcomes"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    code: Mapped[str] = mapped_column(
        String(20), # e.g. CO1, CO2, CO101
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    bloom_taxonomy_level: Mapped[str] = mapped_column(
        String(30), # REMEMBER, UNDERSTAND, APPLY, ANALYZE, EVALUATE, CREATE
        default="APPLY"
    )

    target_attainment_pct: Mapped[float] = mapped_column(
        Float,
        default=75.0
    )


class ProgramOutcome(Base):
    __tablename__ = "program_outcomes"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    program_id: Mapped[UUID] = mapped_column(
        ForeignKey("programs.id"),
        nullable=False,
        index=True
    )

    code: Mapped[str] = mapped_column(
        String(20), # e.g. PO1, PO2, PO-CS-01
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(150),
        default="Program Outcome"
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


class CoPoMapping(Base):
    __tablename__ = "co_po_mappings"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_outcome_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_outcomes.id"),
        nullable=False,
        index=True
    )

    program_outcome_id: Mapped[UUID] = mapped_column(
        ForeignKey("program_outcomes.id"),
        nullable=False,
        index=True
    )

    weight: Mapped[int] = mapped_column(
        Integer, # 1=LOW, 2=MEDIUM, 3=HIGH
        default=3
    )


class WaitlistEntry(Base):
    __tablename__ = "waitlist_entries"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    position: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20), # WAITING, PROMOTED, EXPIRED, CANCELLED
        default="WAITING"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
