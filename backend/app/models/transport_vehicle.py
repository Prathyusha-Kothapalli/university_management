from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class TransportVehicle(Base):
    __tablename__ = "transport_vehicles"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    route_id: Mapped[UUID] = mapped_column(
        ForeignKey("transport_routes.id"),
        nullable=False,
        index=True
    )

    vehicle_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        default=40,
        nullable=False
    )

    driver_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    driver_phone: Mapped[str | None] = mapped_column(
        String(50),
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

    route = relationship(
        "TransportRoute",
        back_populates="vehicles"
    )
