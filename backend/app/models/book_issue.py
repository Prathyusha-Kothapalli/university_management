from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class BookIssue(Base):
    __tablename__ = "book_issues"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    book_id: Mapped[UUID] = mapped_column(
        ForeignKey("library_books.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    issue_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    due_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    return_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="ISSUED",
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

    book = relationship(
        "LibraryBook",
        back_populates="issues"
    )

    student = relationship("Student")

    fines = relationship(
        "LibraryFine",
        back_populates="book_issue",
        cascade="all, delete-orphan"
    )
