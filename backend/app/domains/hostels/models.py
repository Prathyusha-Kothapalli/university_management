"""
Student Life & Hostel Operations - SQLAlchemy Domain Models
Module: app.domains.hostels.models
"""
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base

class HostelsModelEntity1(Base):
    __tablename__ = "hostels_entity_1"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_1")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=1 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity2(Base):
    __tablename__ = "hostels_entity_2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_2")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=2 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity3(Base):
    __tablename__ = "hostels_entity_3"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_3")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=3 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity4(Base):
    __tablename__ = "hostels_entity_4"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_4")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=4 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity5(Base):
    __tablename__ = "hostels_entity_5"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_5")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=5 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity6(Base):
    __tablename__ = "hostels_entity_6"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_6")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=6 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity7(Base):
    __tablename__ = "hostels_entity_7"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_7")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=7 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity8(Base):
    __tablename__ = "hostels_entity_8"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_8")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=8 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity9(Base):
    __tablename__ = "hostels_entity_9"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_9")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=9 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity10(Base):
    __tablename__ = "hostels_entity_10"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_10")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=10 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity11(Base):
    __tablename__ = "hostels_entity_11"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_11")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=11 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity12(Base):
    __tablename__ = "hostels_entity_12"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_12")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=12 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity13(Base):
    __tablename__ = "hostels_entity_13"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_13")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=13 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity14(Base):
    __tablename__ = "hostels_entity_14"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_14")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=14 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity15(Base):
    __tablename__ = "hostels_entity_15"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_15")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=15 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity16(Base):
    __tablename__ = "hostels_entity_16"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_16")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=16 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity17(Base):
    __tablename__ = "hostels_entity_17"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_17")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=17 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity18(Base):
    __tablename__ = "hostels_entity_18"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_18")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=18 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity19(Base):
    __tablename__ = "hostels_entity_19"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_19")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=19 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity20(Base):
    __tablename__ = "hostels_entity_20"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_20")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=20 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity21(Base):
    __tablename__ = "hostels_entity_21"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_21")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=21 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity22(Base):
    __tablename__ = "hostels_entity_22"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_22")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=22 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity23(Base):
    __tablename__ = "hostels_entity_23"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_23")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=23 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity24(Base):
    __tablename__ = "hostels_entity_24"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_24")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=24 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity25(Base):
    __tablename__ = "hostels_entity_25"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_25")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=25 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity26(Base):
    __tablename__ = "hostels_entity_26"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_26")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=26 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity27(Base):
    __tablename__ = "hostels_entity_27"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_27")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=27 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity28(Base):
    __tablename__ = "hostels_entity_28"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_28")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=28 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity29(Base):
    __tablename__ = "hostels_entity_29"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_29")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=29 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity30(Base):
    __tablename__ = "hostels_entity_30"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_30")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=30 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity31(Base):
    __tablename__ = "hostels_entity_31"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_31")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=31 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity32(Base):
    __tablename__ = "hostels_entity_32"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_32")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=32 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity33(Base):
    __tablename__ = "hostels_entity_33"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_33")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=33 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity34(Base):
    __tablename__ = "hostels_entity_34"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_34")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=34 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity35(Base):
    __tablename__ = "hostels_entity_35"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_35")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=35 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity36(Base):
    __tablename__ = "hostels_entity_36"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_36")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=36 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity37(Base):
    __tablename__ = "hostels_entity_37"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_37")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=37 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity38(Base):
    __tablename__ = "hostels_entity_38"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_38")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=38 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity39(Base):
    __tablename__ = "hostels_entity_39"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_39")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=39 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity40(Base):
    __tablename__ = "hostels_entity_40"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_40")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=40 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity41(Base):
    __tablename__ = "hostels_entity_41"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_41")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=41 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity42(Base):
    __tablename__ = "hostels_entity_42"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_42")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=42 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity43(Base):
    __tablename__ = "hostels_entity_43"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_43")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=43 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity44(Base):
    __tablename__ = "hostels_entity_44"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_44")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=44 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity45(Base):
    __tablename__ = "hostels_entity_45"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_45")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=45 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity46(Base):
    __tablename__ = "hostels_entity_46"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_46")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=46 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity47(Base):
    __tablename__ = "hostels_entity_47"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_47")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=47 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity48(Base):
    __tablename__ = "hostels_entity_48"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_48")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=48 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity49(Base):
    __tablename__ = "hostels_entity_49"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_49")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=49 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity50(Base):
    __tablename__ = "hostels_entity_50"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_50")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=50 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity51(Base):
    __tablename__ = "hostels_entity_51"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_51")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=51 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity52(Base):
    __tablename__ = "hostels_entity_52"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_52")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=52 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity53(Base):
    __tablename__ = "hostels_entity_53"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_53")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=53 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity54(Base):
    __tablename__ = "hostels_entity_54"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_54")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=54 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity55(Base):
    __tablename__ = "hostels_entity_55"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_55")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=55 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity56(Base):
    __tablename__ = "hostels_entity_56"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_56")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=56 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity57(Base):
    __tablename__ = "hostels_entity_57"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_57")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=57 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity58(Base):
    __tablename__ = "hostels_entity_58"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_58")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=58 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity59(Base):
    __tablename__ = "hostels_entity_59"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_59")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=59 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity60(Base):
    __tablename__ = "hostels_entity_60"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_60")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=60 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity61(Base):
    __tablename__ = "hostels_entity_61"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_61")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=61 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity62(Base):
    __tablename__ = "hostels_entity_62"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_62")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=62 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity63(Base):
    __tablename__ = "hostels_entity_63"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_63")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=63 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity64(Base):
    __tablename__ = "hostels_entity_64"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_64")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=64 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity65(Base):
    __tablename__ = "hostels_entity_65"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_65")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=65 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity66(Base):
    __tablename__ = "hostels_entity_66"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_66")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=66 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity67(Base):
    __tablename__ = "hostels_entity_67"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_67")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=67 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity68(Base):
    __tablename__ = "hostels_entity_68"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_68")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=68 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity69(Base):
    __tablename__ = "hostels_entity_69"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_69")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=69 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity70(Base):
    __tablename__ = "hostels_entity_70"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_70")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=70 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity71(Base):
    __tablename__ = "hostels_entity_71"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_71")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=71 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity72(Base):
    __tablename__ = "hostels_entity_72"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_72")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=72 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity73(Base):
    __tablename__ = "hostels_entity_73"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_73")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=73 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity74(Base):
    __tablename__ = "hostels_entity_74"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_74")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=74 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity75(Base):
    __tablename__ = "hostels_entity_75"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_75")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=75 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity76(Base):
    __tablename__ = "hostels_entity_76"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_76")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=76 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity77(Base):
    __tablename__ = "hostels_entity_77"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_77")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=77 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity78(Base):
    __tablename__ = "hostels_entity_78"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_78")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=78 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity79(Base):
    __tablename__ = "hostels_entity_79"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_79")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=79 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity80(Base):
    __tablename__ = "hostels_entity_80"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_80")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=80 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity81(Base):
    __tablename__ = "hostels_entity_81"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_81")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=81 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity82(Base):
    __tablename__ = "hostels_entity_82"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_82")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=82 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity83(Base):
    __tablename__ = "hostels_entity_83"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_83")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=83 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity84(Base):
    __tablename__ = "hostels_entity_84"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_84")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=84 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity85(Base):
    __tablename__ = "hostels_entity_85"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_85")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=85 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity86(Base):
    __tablename__ = "hostels_entity_86"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_86")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=86 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity87(Base):
    __tablename__ = "hostels_entity_87"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_87")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=87 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity88(Base):
    __tablename__ = "hostels_entity_88"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_88")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=88 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity89(Base):
    __tablename__ = "hostels_entity_89"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_89")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=89 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity90(Base):
    __tablename__ = "hostels_entity_90"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_90")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=90 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity91(Base):
    __tablename__ = "hostels_entity_91"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_91")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=91 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity92(Base):
    __tablename__ = "hostels_entity_92"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_92")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=92 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity93(Base):
    __tablename__ = "hostels_entity_93"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_93")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=93 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity94(Base):
    __tablename__ = "hostels_entity_94"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_94")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=94 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity95(Base):
    __tablename__ = "hostels_entity_95"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_95")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=95 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity96(Base):
    __tablename__ = "hostels_entity_96"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_96")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=96 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity97(Base):
    __tablename__ = "hostels_entity_97"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_97")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=97 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity98(Base):
    __tablename__ = "hostels_entity_98"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_98")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=98 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity99(Base):
    __tablename__ = "hostels_entity_99"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_99")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=99 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity100(Base):
    __tablename__ = "hostels_entity_100"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_100")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=100 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity101(Base):
    __tablename__ = "hostels_entity_101"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_101")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=101 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity102(Base):
    __tablename__ = "hostels_entity_102"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_102")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=102 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity103(Base):
    __tablename__ = "hostels_entity_103"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_103")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=103 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity104(Base):
    __tablename__ = "hostels_entity_104"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_104")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=104 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity105(Base):
    __tablename__ = "hostels_entity_105"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_105")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=105 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity106(Base):
    __tablename__ = "hostels_entity_106"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_106")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=106 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity107(Base):
    __tablename__ = "hostels_entity_107"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_107")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=107 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity108(Base):
    __tablename__ = "hostels_entity_108"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_108")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=108 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity109(Base):
    __tablename__ = "hostels_entity_109"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_109")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=109 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity110(Base):
    __tablename__ = "hostels_entity_110"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_110")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=110 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity111(Base):
    __tablename__ = "hostels_entity_111"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_111")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=111 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity112(Base):
    __tablename__ = "hostels_entity_112"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_112")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=112 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity113(Base):
    __tablename__ = "hostels_entity_113"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_113")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=113 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity114(Base):
    __tablename__ = "hostels_entity_114"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_114")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=114 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity115(Base):
    __tablename__ = "hostels_entity_115"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_115")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=115 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity116(Base):
    __tablename__ = "hostels_entity_116"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_116")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=116 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity117(Base):
    __tablename__ = "hostels_entity_117"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_117")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=117 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity118(Base):
    __tablename__ = "hostels_entity_118"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_118")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=118 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity119(Base):
    __tablename__ = "hostels_entity_119"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_119")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=119 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

class HostelsModelEntity120(Base):
    __tablename__ = "hostels_entity_120"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_120")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=120 * 100.5)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    status_flag: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    attributes_json: Mapped[Optional[dict]] = mapped_column(JSON, default=dict)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_code": self.entity_code,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "value_amount": self.value_amount,
            "is_active": self.is_active,
            "status_flag": self.status_flag,
            "attributes_json": self.attributes_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

