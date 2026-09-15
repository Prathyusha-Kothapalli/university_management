"""
Sports & Extracurricular Activities - Database Domain Models
Module: app.domains.sports.models
Description: Sports facility booking, inter-college tournament rosters, equipment checkout, club membership tracking, event budget management, achievement badges.
"""

from datetime import datetime, date
from typing import Optional, List, Dict, Any
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base

class SportsCoreEntity(Base):
    __tablename__ = "sports_core_entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="General")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    metadata_info: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    records = relationship("SportsDetailRecord", back_populates="core_entity", cascade="all, delete-orphan")
    logs = relationship("SportsAuditLog", back_populates="core_entity", cascade="all, delete-orphan")


class SportsDetailRecord(Base):
    __tablename__ = "sports_detail_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    core_entity_id: Mapped[int] = mapped_column(Integer, ForeignKey("sports_core_entities.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    record_type: Mapped[str] = mapped_column(String(100), nullable=False)
    value_numeric: Mapped[float] = mapped_column(Float, default=0.0)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_flagged: Mapped[bool] = mapped_column(Boolean, default=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    core_entity = relationship("SportsCoreEntity", back_populates="records")


class SportsAuditLog(Base):
    __tablename__ = "sports_audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    core_entity_id: Mapped[int] = mapped_column(Integer, ForeignKey("sports_core_entities.id"), nullable=False)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    performed_by: Mapped[str] = mapped_column(String(100), nullable=False)
    payload_snapshot: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    core_entity = relationship("SportsCoreEntity", back_populates="logs")


class SportsSubModule1(Base):
    __tablename__ = "sports_submodule_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule2(Base):
    __tablename__ = "sports_submodule_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule3(Base):
    __tablename__ = "sports_submodule_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule4(Base):
    __tablename__ = "sports_submodule_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule5(Base):
    __tablename__ = "sports_submodule_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule6(Base):
    __tablename__ = "sports_submodule_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule7(Base):
    __tablename__ = "sports_submodule_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule8(Base):
    __tablename__ = "sports_submodule_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule9(Base):
    __tablename__ = "sports_submodule_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule10(Base):
    __tablename__ = "sports_submodule_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule11(Base):
    __tablename__ = "sports_submodule_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule12(Base):
    __tablename__ = "sports_submodule_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule13(Base):
    __tablename__ = "sports_submodule_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule14(Base):
    __tablename__ = "sports_submodule_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule15(Base):
    __tablename__ = "sports_submodule_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule16(Base):
    __tablename__ = "sports_submodule_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule17(Base):
    __tablename__ = "sports_submodule_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule18(Base):
    __tablename__ = "sports_submodule_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class SportsSubModule19(Base):
    __tablename__ = "sports_submodule_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    reference_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    configuration: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    remarks: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "reference_number": self.reference_number,
            "label": self.label,
            "priority": self.priority,
            "is_active": self.is_active,
            "configuration": self.configuration,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
