from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class FacultyQualification(Base):
    __tablename__ = "faculty_qualifications"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    faculty_id: Mapped[UUID] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=False,
        index=True
    )

    degree_name: Mapped[str] = mapped_column(
        String(100), # Ph.D., M.Tech, M.Sc., B.Tech
        nullable=False
    )

    field_of_study: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    institution: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    year_awarded: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


class FacultyAppraisal(Base):
    __tablename__ = "faculty_appraisals"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    faculty_id: Mapped[UUID] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=False,
        index=True
    )

    academic_year_id: Mapped[UUID] = mapped_column(
        ForeignKey("academic_years.id"),
        nullable=False
    )

    teaching_score: Mapped[float] = mapped_column(
        Float,
        default=4.5
    )

    research_score: Mapped[float] = mapped_column(
        Float,
        default=4.0
    )

    service_score: Mapped[float] = mapped_column(
        Float,
        default=4.2
    )

    overall_rating: Mapped[float] = mapped_column(
        Float,
        default=4.3
    )

    self_assessment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    reviewer_comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="SUBMITTED"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class ResearchProject(Base):
    __tablename__ = "research_projects"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    lead_faculty_id: Mapped[UUID] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )

    grant_agency: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    grant_amount: Mapped[float] = mapped_column(
        Float,
        default=50000.0
    )

    status: Mapped[str] = mapped_column(
        String(30), # PROPOSED, APPROVED, IN_PROGRESS, COMPLETED
        default="IN_PROGRESS"
    )

    start_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )

    end_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )


class ResearchPublication(Base):
    __tablename__ = "research_publications"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    faculty_id: Mapped[UUID] = mapped_column(
        ForeignKey("faculty.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    journal_conference: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    doi: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    citation_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    impact_factor: Mapped[float] = mapped_column(
        Float,
        default=2.5
    )

    is_peer_reviewed: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    publication_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )
