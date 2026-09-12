from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class LibraryFine(Base):
    __tablename__ = "library_fines"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    book_issue_id: Mapped[UUID] = mapped_column(
        ForeignKey("book_issues.id"),
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

    reason: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="UNPAID",
        nullable=False
    )

    paid_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
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

    book_issue = relationship(
        "BookIssue",
        back_populates="fines"
    )

    student = relationship("Student")
