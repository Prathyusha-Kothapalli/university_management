from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class CodeSubmissionAst(Base):
    __tablename__ = "code_submission_asts"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    submission_id: Mapped[UUID] = mapped_column(
        ForeignKey("assignment_submissions.id"),
        nullable=False,
        index=True
    )

    ast_json: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    cyclomatic_complexity: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    linter_warnings: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


class PlagiarismScanReport(Base):
    __tablename__ = "plagiarism_scan_reports"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    submission_a_id: Mapped[UUID] = mapped_column(
        ForeignKey("assignment_submissions.id"),
        nullable=False,
        index=True
    )

    submission_b_id: Mapped[UUID] = mapped_column(
        ForeignKey("assignment_submissions.id"),
        nullable=False
    )

    similarity_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    matched_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    is_flagged: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    scanned_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
