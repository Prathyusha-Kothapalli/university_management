from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class AcademicHold(Base):
    __tablename__ = "academic_holds"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    hold_type: Mapped[str] = mapped_column(
        String(50), # FINANCIAL, DISCIPLINARY, DOCUMENT_MISSING, ADVISORY
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    placed_by_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class StudentConductCase(Base):
    __tablename__ = "student_conduct_cases"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    incident_title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    incident_description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    severity: Mapped[str] = mapped_column(
        String(20), # MINOR, MODERATE, SEVERE, CRITICAL
        default="MINOR"
    )

    action_taken: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    reported_by_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30), # UNDER_INVESTIGATION, RESOLVED, APPEALED
        default="UNDER_INVESTIGATION"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class StudentAchievement(Base):
    __tablename__ = "student_achievements"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50), # ACADEMIC_HONORS, HACKATHON, SPORTS, LEADERSHIP, COMMUNITY
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    issued_by: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    awarded_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )


class SupportCase(Base):
    __tablename__ = "support_cases"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    subject: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50), # ACADEMIC_ADVISING, MENTAL_HEALTH, FINANCIAL_HELP, HOSTEL_ISSUE
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        String(20), # LOW, MEDIUM, HIGH, URGENT
        default="MEDIUM"
    )

    status: Mapped[str] = mapped_column(
        String(30), # OPEN, IN_PROGRESS, RESOLVED, CLOSED
        default="OPEN"
    )

    assigned_advisor_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    details: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class AcademicGoal(Base):
    __tablename__ = "academic_goals"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    target_gpa: Mapped[float] = mapped_column(
        Float,
        default=3.5
    )

    target_credits: Mapped[int] = mapped_column(
        Integer,
        default=120
    )

    career_path: Mapped[str] = mapped_column(
        String(100),
        default="Software Engineering"
    )

    is_achieved: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
