from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class PlacementDrive(Base):
    __tablename__ = "placement_drives"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False,
        index=True
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    job_title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    eligibility_criteria: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    package_details: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    drive_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    deadline: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="UPCOMING",
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

    university = relationship("University")

    applications = relationship(
        "PlacementApplication",
        back_populates="placement_drive",
        cascade="all, delete-orphan"
    )
