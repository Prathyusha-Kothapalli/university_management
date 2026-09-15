"""
Campus Health & Clinic Management - SQLAlchemy Domain Models
Module: app.domains.health.models
"""
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base

class HealthModelEntity1(Base):
    __tablename__ = "health_entity_1"

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

class HealthModelEntity2(Base):
    __tablename__ = "health_entity_2"

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

class HealthModelEntity3(Base):
    __tablename__ = "health_entity_3"

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

class HealthModelEntity4(Base):
    __tablename__ = "health_entity_4"

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

class HealthModelEntity5(Base):
    __tablename__ = "health_entity_5"

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

class HealthModelEntity6(Base):
    __tablename__ = "health_entity_6"

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

class HealthModelEntity7(Base):
    __tablename__ = "health_entity_7"

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

class HealthModelEntity8(Base):
    __tablename__ = "health_entity_8"

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

class HealthModelEntity9(Base):
    __tablename__ = "health_entity_9"

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

class HealthModelEntity10(Base):
    __tablename__ = "health_entity_10"

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

class HealthModelEntity11(Base):
    __tablename__ = "health_entity_11"

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

class HealthModelEntity12(Base):
    __tablename__ = "health_entity_12"

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

class HealthModelEntity13(Base):
    __tablename__ = "health_entity_13"

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

class HealthModelEntity14(Base):
    __tablename__ = "health_entity_14"

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

class HealthModelEntity15(Base):
    __tablename__ = "health_entity_15"

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

class HealthModelEntity16(Base):
    __tablename__ = "health_entity_16"

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

class HealthModelEntity17(Base):
    __tablename__ = "health_entity_17"

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

class HealthModelEntity18(Base):
    __tablename__ = "health_entity_18"

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

class HealthModelEntity19(Base):
    __tablename__ = "health_entity_19"

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

class HealthModelEntity20(Base):
    __tablename__ = "health_entity_20"

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

class HealthModelEntity21(Base):
    __tablename__ = "health_entity_21"

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

class HealthModelEntity22(Base):
    __tablename__ = "health_entity_22"

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

class HealthModelEntity23(Base):
    __tablename__ = "health_entity_23"

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

class HealthModelEntity24(Base):
    __tablename__ = "health_entity_24"

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

class HealthModelEntity25(Base):
    __tablename__ = "health_entity_25"

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

class HealthModelEntity26(Base):
    __tablename__ = "health_entity_26"

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

class HealthModelEntity27(Base):
    __tablename__ = "health_entity_27"

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

class HealthModelEntity28(Base):
    __tablename__ = "health_entity_28"

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

class HealthModelEntity29(Base):
    __tablename__ = "health_entity_29"

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

class HealthModelEntity30(Base):
    __tablename__ = "health_entity_30"

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

class HealthModelEntity31(Base):
    __tablename__ = "health_entity_31"

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

class HealthModelEntity32(Base):
    __tablename__ = "health_entity_32"

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

class HealthModelEntity33(Base):
    __tablename__ = "health_entity_33"

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

class HealthModelEntity34(Base):
    __tablename__ = "health_entity_34"

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

class HealthModelEntity35(Base):
    __tablename__ = "health_entity_35"

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

class HealthModelEntity36(Base):
    __tablename__ = "health_entity_36"

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

class HealthModelEntity37(Base):
    __tablename__ = "health_entity_37"

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

class HealthModelEntity38(Base):
    __tablename__ = "health_entity_38"

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

class HealthModelEntity39(Base):
    __tablename__ = "health_entity_39"

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

class HealthModelEntity40(Base):
    __tablename__ = "health_entity_40"

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

class HealthModelEntity41(Base):
    __tablename__ = "health_entity_41"

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

class HealthModelEntity42(Base):
    __tablename__ = "health_entity_42"

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

class HealthModelEntity43(Base):
    __tablename__ = "health_entity_43"

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

class HealthModelEntity44(Base):
    __tablename__ = "health_entity_44"

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

class HealthModelEntity45(Base):
    __tablename__ = "health_entity_45"

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

class HealthModelEntity46(Base):
    __tablename__ = "health_entity_46"

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

class HealthModelEntity47(Base):
    __tablename__ = "health_entity_47"

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

class HealthModelEntity48(Base):
    __tablename__ = "health_entity_48"

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

class HealthModelEntity49(Base):
    __tablename__ = "health_entity_49"

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

class HealthModelEntity50(Base):
    __tablename__ = "health_entity_50"

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

class HealthModelEntity51(Base):
    __tablename__ = "health_entity_51"

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

class HealthModelEntity52(Base):
    __tablename__ = "health_entity_52"

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

class HealthModelEntity53(Base):
    __tablename__ = "health_entity_53"

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

class HealthModelEntity54(Base):
    __tablename__ = "health_entity_54"

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

class HealthModelEntity55(Base):
    __tablename__ = "health_entity_55"

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

class HealthModelEntity56(Base):
    __tablename__ = "health_entity_56"

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

class HealthModelEntity57(Base):
    __tablename__ = "health_entity_57"

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

class HealthModelEntity58(Base):
    __tablename__ = "health_entity_58"

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

class HealthModelEntity59(Base):
    __tablename__ = "health_entity_59"

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

class HealthModelEntity60(Base):
    __tablename__ = "health_entity_60"

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

class HealthModelEntity61(Base):
    __tablename__ = "health_entity_61"

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

class HealthModelEntity62(Base):
    __tablename__ = "health_entity_62"

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

class HealthModelEntity63(Base):
    __tablename__ = "health_entity_63"

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

class HealthModelEntity64(Base):
    __tablename__ = "health_entity_64"

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

class HealthModelEntity65(Base):
    __tablename__ = "health_entity_65"

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

class HealthModelEntity66(Base):
    __tablename__ = "health_entity_66"

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

class HealthModelEntity67(Base):
    __tablename__ = "health_entity_67"

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

class HealthModelEntity68(Base):
    __tablename__ = "health_entity_68"

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

class HealthModelEntity69(Base):
    __tablename__ = "health_entity_69"

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

class HealthModelEntity70(Base):
    __tablename__ = "health_entity_70"

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

class HealthModelEntity71(Base):
    __tablename__ = "health_entity_71"

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

class HealthModelEntity72(Base):
    __tablename__ = "health_entity_72"

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

class HealthModelEntity73(Base):
    __tablename__ = "health_entity_73"

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

class HealthModelEntity74(Base):
    __tablename__ = "health_entity_74"

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

class HealthModelEntity75(Base):
    __tablename__ = "health_entity_75"

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

class HealthModelEntity76(Base):
    __tablename__ = "health_entity_76"

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

class HealthModelEntity77(Base):
    __tablename__ = "health_entity_77"

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

class HealthModelEntity78(Base):
    __tablename__ = "health_entity_78"

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

class HealthModelEntity79(Base):
    __tablename__ = "health_entity_79"

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

class HealthModelEntity80(Base):
    __tablename__ = "health_entity_80"

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

class HealthModelEntity81(Base):
    __tablename__ = "health_entity_81"

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

class HealthModelEntity82(Base):
    __tablename__ = "health_entity_82"

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

class HealthModelEntity83(Base):
    __tablename__ = "health_entity_83"

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

class HealthModelEntity84(Base):
    __tablename__ = "health_entity_84"

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

class HealthModelEntity85(Base):
    __tablename__ = "health_entity_85"

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

class HealthModelEntity86(Base):
    __tablename__ = "health_entity_86"

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

class HealthModelEntity87(Base):
    __tablename__ = "health_entity_87"

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

class HealthModelEntity88(Base):
    __tablename__ = "health_entity_88"

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

class HealthModelEntity89(Base):
    __tablename__ = "health_entity_89"

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

class HealthModelEntity90(Base):
    __tablename__ = "health_entity_90"

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

class HealthModelEntity91(Base):
    __tablename__ = "health_entity_91"

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

class HealthModelEntity92(Base):
    __tablename__ = "health_entity_92"

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

class HealthModelEntity93(Base):
    __tablename__ = "health_entity_93"

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

class HealthModelEntity94(Base):
    __tablename__ = "health_entity_94"

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

class HealthModelEntity95(Base):
    __tablename__ = "health_entity_95"

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

class HealthModelEntity96(Base):
    __tablename__ = "health_entity_96"

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

class HealthModelEntity97(Base):
    __tablename__ = "health_entity_97"

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

class HealthModelEntity98(Base):
    __tablename__ = "health_entity_98"

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

class HealthModelEntity99(Base):
    __tablename__ = "health_entity_99"

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

class HealthModelEntity100(Base):
    __tablename__ = "health_entity_100"

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

class HealthModelEntity101(Base):
    __tablename__ = "health_entity_101"

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

class HealthModelEntity102(Base):
    __tablename__ = "health_entity_102"

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

class HealthModelEntity103(Base):
    __tablename__ = "health_entity_103"

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

class HealthModelEntity104(Base):
    __tablename__ = "health_entity_104"

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

class HealthModelEntity105(Base):
    __tablename__ = "health_entity_105"

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

class HealthModelEntity106(Base):
    __tablename__ = "health_entity_106"

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

class HealthModelEntity107(Base):
    __tablename__ = "health_entity_107"

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

class HealthModelEntity108(Base):
    __tablename__ = "health_entity_108"

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

class HealthModelEntity109(Base):
    __tablename__ = "health_entity_109"

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

class HealthModelEntity110(Base):
    __tablename__ = "health_entity_110"

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

class HealthModelEntity111(Base):
    __tablename__ = "health_entity_111"

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

class HealthModelEntity112(Base):
    __tablename__ = "health_entity_112"

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

class HealthModelEntity113(Base):
    __tablename__ = "health_entity_113"

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

class HealthModelEntity114(Base):
    __tablename__ = "health_entity_114"

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

class HealthModelEntity115(Base):
    __tablename__ = "health_entity_115"

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

class HealthModelEntity116(Base):
    __tablename__ = "health_entity_116"

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

class HealthModelEntity117(Base):
    __tablename__ = "health_entity_117"

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

class HealthModelEntity118(Base):
    __tablename__ = "health_entity_118"

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

class HealthModelEntity119(Base):
    __tablename__ = "health_entity_119"

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

class HealthModelEntity120(Base):
    __tablename__ = "health_entity_120"

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

class HealthModelEntity121(Base):
    __tablename__ = "health_entity_121"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_121")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=121 * 100.5)
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

class HealthModelEntity122(Base):
    __tablename__ = "health_entity_122"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_122")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=122 * 100.5)
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

class HealthModelEntity123(Base):
    __tablename__ = "health_entity_123"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_123")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=123 * 100.5)
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

class HealthModelEntity124(Base):
    __tablename__ = "health_entity_124"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_124")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=124 * 100.5)
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

class HealthModelEntity125(Base):
    __tablename__ = "health_entity_125"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_125")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=125 * 100.5)
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

class HealthModelEntity126(Base):
    __tablename__ = "health_entity_126"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_126")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=126 * 100.5)
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

class HealthModelEntity127(Base):
    __tablename__ = "health_entity_127"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_127")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=127 * 100.5)
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

class HealthModelEntity128(Base):
    __tablename__ = "health_entity_128"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_128")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=128 * 100.5)
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

class HealthModelEntity129(Base):
    __tablename__ = "health_entity_129"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_129")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=129 * 100.5)
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

class HealthModelEntity130(Base):
    __tablename__ = "health_entity_130"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_130")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=130 * 100.5)
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

class HealthModelEntity131(Base):
    __tablename__ = "health_entity_131"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_131")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=131 * 100.5)
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

class HealthModelEntity132(Base):
    __tablename__ = "health_entity_132"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_132")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=132 * 100.5)
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

class HealthModelEntity133(Base):
    __tablename__ = "health_entity_133"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_133")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=133 * 100.5)
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

class HealthModelEntity134(Base):
    __tablename__ = "health_entity_134"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_134")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=134 * 100.5)
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

class HealthModelEntity135(Base):
    __tablename__ = "health_entity_135"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_135")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=135 * 100.5)
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

class HealthModelEntity136(Base):
    __tablename__ = "health_entity_136"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_136")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=136 * 100.5)
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

class HealthModelEntity137(Base):
    __tablename__ = "health_entity_137"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_137")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=137 * 100.5)
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

class HealthModelEntity138(Base):
    __tablename__ = "health_entity_138"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_138")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=138 * 100.5)
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

class HealthModelEntity139(Base):
    __tablename__ = "health_entity_139"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_139")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=139 * 100.5)
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

class HealthModelEntity140(Base):
    __tablename__ = "health_entity_140"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_140")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=140 * 100.5)
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

class HealthModelEntity141(Base):
    __tablename__ = "health_entity_141"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_141")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=141 * 100.5)
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

class HealthModelEntity142(Base):
    __tablename__ = "health_entity_142"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_142")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=142 * 100.5)
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

class HealthModelEntity143(Base):
    __tablename__ = "health_entity_143"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_143")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=143 * 100.5)
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

class HealthModelEntity144(Base):
    __tablename__ = "health_entity_144"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_144")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=144 * 100.5)
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

class HealthModelEntity145(Base):
    __tablename__ = "health_entity_145"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_145")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=145 * 100.5)
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

class HealthModelEntity146(Base):
    __tablename__ = "health_entity_146"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_146")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=146 * 100.5)
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

class HealthModelEntity147(Base):
    __tablename__ = "health_entity_147"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_147")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=147 * 100.5)
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

class HealthModelEntity148(Base):
    __tablename__ = "health_entity_148"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_148")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=148 * 100.5)
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

class HealthModelEntity149(Base):
    __tablename__ = "health_entity_149"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_149")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=149 * 100.5)
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

class HealthModelEntity150(Base):
    __tablename__ = "health_entity_150"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_150")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=150 * 100.5)
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

class HealthModelEntity151(Base):
    __tablename__ = "health_entity_151"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_151")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=151 * 100.5)
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

class HealthModelEntity152(Base):
    __tablename__ = "health_entity_152"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_152")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=152 * 100.5)
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

class HealthModelEntity153(Base):
    __tablename__ = "health_entity_153"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_153")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=153 * 100.5)
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

class HealthModelEntity154(Base):
    __tablename__ = "health_entity_154"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_154")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=154 * 100.5)
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

class HealthModelEntity155(Base):
    __tablename__ = "health_entity_155"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_155")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=155 * 100.5)
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

class HealthModelEntity156(Base):
    __tablename__ = "health_entity_156"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_156")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=156 * 100.5)
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

class HealthModelEntity157(Base):
    __tablename__ = "health_entity_157"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_157")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=157 * 100.5)
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

class HealthModelEntity158(Base):
    __tablename__ = "health_entity_158"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_158")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=158 * 100.5)
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

class HealthModelEntity159(Base):
    __tablename__ = "health_entity_159"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_159")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=159 * 100.5)
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

class HealthModelEntity160(Base):
    __tablename__ = "health_entity_160"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_160")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=160 * 100.5)
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

class HealthModelEntity161(Base):
    __tablename__ = "health_entity_161"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_161")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=161 * 100.5)
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

class HealthModelEntity162(Base):
    __tablename__ = "health_entity_162"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_162")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=162 * 100.5)
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

class HealthModelEntity163(Base):
    __tablename__ = "health_entity_163"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_163")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=163 * 100.5)
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

class HealthModelEntity164(Base):
    __tablename__ = "health_entity_164"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_164")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=164 * 100.5)
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

class HealthModelEntity165(Base):
    __tablename__ = "health_entity_165"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_165")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=165 * 100.5)
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

class HealthModelEntity166(Base):
    __tablename__ = "health_entity_166"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_166")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=166 * 100.5)
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

class HealthModelEntity167(Base):
    __tablename__ = "health_entity_167"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_167")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=167 * 100.5)
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

class HealthModelEntity168(Base):
    __tablename__ = "health_entity_168"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_168")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=168 * 100.5)
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

class HealthModelEntity169(Base):
    __tablename__ = "health_entity_169"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_169")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=169 * 100.5)
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

class HealthModelEntity170(Base):
    __tablename__ = "health_entity_170"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_170")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=170 * 100.5)
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

class HealthModelEntity171(Base):
    __tablename__ = "health_entity_171"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_171")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=171 * 100.5)
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

class HealthModelEntity172(Base):
    __tablename__ = "health_entity_172"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_172")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=172 * 100.5)
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

class HealthModelEntity173(Base):
    __tablename__ = "health_entity_173"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_173")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=173 * 100.5)
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

class HealthModelEntity174(Base):
    __tablename__ = "health_entity_174"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_174")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=174 * 100.5)
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

class HealthModelEntity175(Base):
    __tablename__ = "health_entity_175"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_175")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=175 * 100.5)
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

class HealthModelEntity176(Base):
    __tablename__ = "health_entity_176"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_176")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=176 * 100.5)
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

class HealthModelEntity177(Base):
    __tablename__ = "health_entity_177"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_177")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=177 * 100.5)
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

class HealthModelEntity178(Base):
    __tablename__ = "health_entity_178"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_178")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=178 * 100.5)
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

class HealthModelEntity179(Base):
    __tablename__ = "health_entity_179"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_179")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=179 * 100.5)
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

class HealthModelEntity180(Base):
    __tablename__ = "health_entity_180"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_180")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=180 * 100.5)
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

class HealthModelEntity181(Base):
    __tablename__ = "health_entity_181"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_181")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=181 * 100.5)
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

class HealthModelEntity182(Base):
    __tablename__ = "health_entity_182"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_182")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=182 * 100.5)
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

class HealthModelEntity183(Base):
    __tablename__ = "health_entity_183"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_183")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=183 * 100.5)
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

class HealthModelEntity184(Base):
    __tablename__ = "health_entity_184"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_184")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=184 * 100.5)
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

class HealthModelEntity185(Base):
    __tablename__ = "health_entity_185"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_185")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=185 * 100.5)
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

class HealthModelEntity186(Base):
    __tablename__ = "health_entity_186"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_186")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=186 * 100.5)
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

class HealthModelEntity187(Base):
    __tablename__ = "health_entity_187"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_187")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=187 * 100.5)
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

class HealthModelEntity188(Base):
    __tablename__ = "health_entity_188"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_188")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=188 * 100.5)
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

class HealthModelEntity189(Base):
    __tablename__ = "health_entity_189"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_189")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=189 * 100.5)
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

class HealthModelEntity190(Base):
    __tablename__ = "health_entity_190"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_190")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=190 * 100.5)
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

class HealthModelEntity191(Base):
    __tablename__ = "health_entity_191"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_191")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=191 * 100.5)
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

class HealthModelEntity192(Base):
    __tablename__ = "health_entity_192"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_192")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=192 * 100.5)
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

class HealthModelEntity193(Base):
    __tablename__ = "health_entity_193"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_193")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=193 * 100.5)
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

class HealthModelEntity194(Base):
    __tablename__ = "health_entity_194"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_194")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=194 * 100.5)
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

class HealthModelEntity195(Base):
    __tablename__ = "health_entity_195"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_195")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=195 * 100.5)
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

class HealthModelEntity196(Base):
    __tablename__ = "health_entity_196"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_196")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=196 * 100.5)
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

class HealthModelEntity197(Base):
    __tablename__ = "health_entity_197"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_197")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=197 * 100.5)
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

class HealthModelEntity198(Base):
    __tablename__ = "health_entity_198"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_198")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=198 * 100.5)
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

class HealthModelEntity199(Base):
    __tablename__ = "health_entity_199"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_199")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=199 * 100.5)
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

class HealthModelEntity200(Base):
    __tablename__ = "health_entity_200"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    entity_code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(100), default="Category_200")
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    value_amount: Mapped[float] = mapped_column(Float, default=200 * 100.5)
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

