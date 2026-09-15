"""
Transport & Fleet Logistics - SQLAlchemy Domain Models
Module: app.domains.transport.models
"""
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base

class TransportModelEntity1(Base):
    __tablename__ = "transport_entity_1"

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

class TransportModelEntity2(Base):
    __tablename__ = "transport_entity_2"

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

class TransportModelEntity3(Base):
    __tablename__ = "transport_entity_3"

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

class TransportModelEntity4(Base):
    __tablename__ = "transport_entity_4"

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

class TransportModelEntity5(Base):
    __tablename__ = "transport_entity_5"

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

class TransportModelEntity6(Base):
    __tablename__ = "transport_entity_6"

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

class TransportModelEntity7(Base):
    __tablename__ = "transport_entity_7"

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

class TransportModelEntity8(Base):
    __tablename__ = "transport_entity_8"

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

class TransportModelEntity9(Base):
    __tablename__ = "transport_entity_9"

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

class TransportModelEntity10(Base):
    __tablename__ = "transport_entity_10"

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

class TransportModelEntity11(Base):
    __tablename__ = "transport_entity_11"

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

class TransportModelEntity12(Base):
    __tablename__ = "transport_entity_12"

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

class TransportModelEntity13(Base):
    __tablename__ = "transport_entity_13"

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

class TransportModelEntity14(Base):
    __tablename__ = "transport_entity_14"

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

class TransportModelEntity15(Base):
    __tablename__ = "transport_entity_15"

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

class TransportModelEntity16(Base):
    __tablename__ = "transport_entity_16"

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

class TransportModelEntity17(Base):
    __tablename__ = "transport_entity_17"

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

class TransportModelEntity18(Base):
    __tablename__ = "transport_entity_18"

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

class TransportModelEntity19(Base):
    __tablename__ = "transport_entity_19"

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

class TransportModelEntity20(Base):
    __tablename__ = "transport_entity_20"

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

class TransportModelEntity21(Base):
    __tablename__ = "transport_entity_21"

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

class TransportModelEntity22(Base):
    __tablename__ = "transport_entity_22"

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

class TransportModelEntity23(Base):
    __tablename__ = "transport_entity_23"

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

class TransportModelEntity24(Base):
    __tablename__ = "transport_entity_24"

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

class TransportModelEntity25(Base):
    __tablename__ = "transport_entity_25"

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

class TransportModelEntity26(Base):
    __tablename__ = "transport_entity_26"

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

class TransportModelEntity27(Base):
    __tablename__ = "transport_entity_27"

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

class TransportModelEntity28(Base):
    __tablename__ = "transport_entity_28"

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

class TransportModelEntity29(Base):
    __tablename__ = "transport_entity_29"

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

class TransportModelEntity30(Base):
    __tablename__ = "transport_entity_30"

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

class TransportModelEntity31(Base):
    __tablename__ = "transport_entity_31"

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

class TransportModelEntity32(Base):
    __tablename__ = "transport_entity_32"

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

class TransportModelEntity33(Base):
    __tablename__ = "transport_entity_33"

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

class TransportModelEntity34(Base):
    __tablename__ = "transport_entity_34"

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

class TransportModelEntity35(Base):
    __tablename__ = "transport_entity_35"

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

class TransportModelEntity36(Base):
    __tablename__ = "transport_entity_36"

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

class TransportModelEntity37(Base):
    __tablename__ = "transport_entity_37"

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

class TransportModelEntity38(Base):
    __tablename__ = "transport_entity_38"

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

class TransportModelEntity39(Base):
    __tablename__ = "transport_entity_39"

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

class TransportModelEntity40(Base):
    __tablename__ = "transport_entity_40"

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

class TransportModelEntity41(Base):
    __tablename__ = "transport_entity_41"

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

class TransportModelEntity42(Base):
    __tablename__ = "transport_entity_42"

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

class TransportModelEntity43(Base):
    __tablename__ = "transport_entity_43"

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

class TransportModelEntity44(Base):
    __tablename__ = "transport_entity_44"

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

class TransportModelEntity45(Base):
    __tablename__ = "transport_entity_45"

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

class TransportModelEntity46(Base):
    __tablename__ = "transport_entity_46"

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

class TransportModelEntity47(Base):
    __tablename__ = "transport_entity_47"

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

class TransportModelEntity48(Base):
    __tablename__ = "transport_entity_48"

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

class TransportModelEntity49(Base):
    __tablename__ = "transport_entity_49"

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

class TransportModelEntity50(Base):
    __tablename__ = "transport_entity_50"

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

class TransportModelEntity51(Base):
    __tablename__ = "transport_entity_51"

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

class TransportModelEntity52(Base):
    __tablename__ = "transport_entity_52"

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

class TransportModelEntity53(Base):
    __tablename__ = "transport_entity_53"

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

class TransportModelEntity54(Base):
    __tablename__ = "transport_entity_54"

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

class TransportModelEntity55(Base):
    __tablename__ = "transport_entity_55"

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

class TransportModelEntity56(Base):
    __tablename__ = "transport_entity_56"

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

class TransportModelEntity57(Base):
    __tablename__ = "transport_entity_57"

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

class TransportModelEntity58(Base):
    __tablename__ = "transport_entity_58"

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

class TransportModelEntity59(Base):
    __tablename__ = "transport_entity_59"

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

class TransportModelEntity60(Base):
    __tablename__ = "transport_entity_60"

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

class TransportModelEntity61(Base):
    __tablename__ = "transport_entity_61"

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

class TransportModelEntity62(Base):
    __tablename__ = "transport_entity_62"

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

class TransportModelEntity63(Base):
    __tablename__ = "transport_entity_63"

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

class TransportModelEntity64(Base):
    __tablename__ = "transport_entity_64"

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

class TransportModelEntity65(Base):
    __tablename__ = "transport_entity_65"

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

class TransportModelEntity66(Base):
    __tablename__ = "transport_entity_66"

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

class TransportModelEntity67(Base):
    __tablename__ = "transport_entity_67"

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

class TransportModelEntity68(Base):
    __tablename__ = "transport_entity_68"

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

class TransportModelEntity69(Base):
    __tablename__ = "transport_entity_69"

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

class TransportModelEntity70(Base):
    __tablename__ = "transport_entity_70"

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

class TransportModelEntity71(Base):
    __tablename__ = "transport_entity_71"

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

class TransportModelEntity72(Base):
    __tablename__ = "transport_entity_72"

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

class TransportModelEntity73(Base):
    __tablename__ = "transport_entity_73"

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

class TransportModelEntity74(Base):
    __tablename__ = "transport_entity_74"

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

class TransportModelEntity75(Base):
    __tablename__ = "transport_entity_75"

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

class TransportModelEntity76(Base):
    __tablename__ = "transport_entity_76"

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

class TransportModelEntity77(Base):
    __tablename__ = "transport_entity_77"

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

class TransportModelEntity78(Base):
    __tablename__ = "transport_entity_78"

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

class TransportModelEntity79(Base):
    __tablename__ = "transport_entity_79"

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

class TransportModelEntity80(Base):
    __tablename__ = "transport_entity_80"

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

class TransportModelEntity81(Base):
    __tablename__ = "transport_entity_81"

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

class TransportModelEntity82(Base):
    __tablename__ = "transport_entity_82"

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

class TransportModelEntity83(Base):
    __tablename__ = "transport_entity_83"

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

class TransportModelEntity84(Base):
    __tablename__ = "transport_entity_84"

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

class TransportModelEntity85(Base):
    __tablename__ = "transport_entity_85"

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

class TransportModelEntity86(Base):
    __tablename__ = "transport_entity_86"

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

class TransportModelEntity87(Base):
    __tablename__ = "transport_entity_87"

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

class TransportModelEntity88(Base):
    __tablename__ = "transport_entity_88"

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

class TransportModelEntity89(Base):
    __tablename__ = "transport_entity_89"

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

class TransportModelEntity90(Base):
    __tablename__ = "transport_entity_90"

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

class TransportModelEntity91(Base):
    __tablename__ = "transport_entity_91"

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

class TransportModelEntity92(Base):
    __tablename__ = "transport_entity_92"

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

class TransportModelEntity93(Base):
    __tablename__ = "transport_entity_93"

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

class TransportModelEntity94(Base):
    __tablename__ = "transport_entity_94"

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

class TransportModelEntity95(Base):
    __tablename__ = "transport_entity_95"

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

class TransportModelEntity96(Base):
    __tablename__ = "transport_entity_96"

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

class TransportModelEntity97(Base):
    __tablename__ = "transport_entity_97"

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

class TransportModelEntity98(Base):
    __tablename__ = "transport_entity_98"

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

class TransportModelEntity99(Base):
    __tablename__ = "transport_entity_99"

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

class TransportModelEntity100(Base):
    __tablename__ = "transport_entity_100"

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

class TransportModelEntity101(Base):
    __tablename__ = "transport_entity_101"

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

class TransportModelEntity102(Base):
    __tablename__ = "transport_entity_102"

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

class TransportModelEntity103(Base):
    __tablename__ = "transport_entity_103"

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

class TransportModelEntity104(Base):
    __tablename__ = "transport_entity_104"

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

class TransportModelEntity105(Base):
    __tablename__ = "transport_entity_105"

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

class TransportModelEntity106(Base):
    __tablename__ = "transport_entity_106"

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

class TransportModelEntity107(Base):
    __tablename__ = "transport_entity_107"

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

class TransportModelEntity108(Base):
    __tablename__ = "transport_entity_108"

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

class TransportModelEntity109(Base):
    __tablename__ = "transport_entity_109"

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

class TransportModelEntity110(Base):
    __tablename__ = "transport_entity_110"

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

class TransportModelEntity111(Base):
    __tablename__ = "transport_entity_111"

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

class TransportModelEntity112(Base):
    __tablename__ = "transport_entity_112"

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

class TransportModelEntity113(Base):
    __tablename__ = "transport_entity_113"

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

class TransportModelEntity114(Base):
    __tablename__ = "transport_entity_114"

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

class TransportModelEntity115(Base):
    __tablename__ = "transport_entity_115"

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

class TransportModelEntity116(Base):
    __tablename__ = "transport_entity_116"

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

class TransportModelEntity117(Base):
    __tablename__ = "transport_entity_117"

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

class TransportModelEntity118(Base):
    __tablename__ = "transport_entity_118"

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

class TransportModelEntity119(Base):
    __tablename__ = "transport_entity_119"

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

class TransportModelEntity120(Base):
    __tablename__ = "transport_entity_120"

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

class TransportModelEntity121(Base):
    __tablename__ = "transport_entity_121"

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

class TransportModelEntity122(Base):
    __tablename__ = "transport_entity_122"

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

class TransportModelEntity123(Base):
    __tablename__ = "transport_entity_123"

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

class TransportModelEntity124(Base):
    __tablename__ = "transport_entity_124"

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

class TransportModelEntity125(Base):
    __tablename__ = "transport_entity_125"

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

class TransportModelEntity126(Base):
    __tablename__ = "transport_entity_126"

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

class TransportModelEntity127(Base):
    __tablename__ = "transport_entity_127"

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

class TransportModelEntity128(Base):
    __tablename__ = "transport_entity_128"

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

class TransportModelEntity129(Base):
    __tablename__ = "transport_entity_129"

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

class TransportModelEntity130(Base):
    __tablename__ = "transport_entity_130"

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

class TransportModelEntity131(Base):
    __tablename__ = "transport_entity_131"

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

class TransportModelEntity132(Base):
    __tablename__ = "transport_entity_132"

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

class TransportModelEntity133(Base):
    __tablename__ = "transport_entity_133"

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

class TransportModelEntity134(Base):
    __tablename__ = "transport_entity_134"

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

class TransportModelEntity135(Base):
    __tablename__ = "transport_entity_135"

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

class TransportModelEntity136(Base):
    __tablename__ = "transport_entity_136"

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

class TransportModelEntity137(Base):
    __tablename__ = "transport_entity_137"

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

class TransportModelEntity138(Base):
    __tablename__ = "transport_entity_138"

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

class TransportModelEntity139(Base):
    __tablename__ = "transport_entity_139"

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

class TransportModelEntity140(Base):
    __tablename__ = "transport_entity_140"

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

class TransportModelEntity141(Base):
    __tablename__ = "transport_entity_141"

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

class TransportModelEntity142(Base):
    __tablename__ = "transport_entity_142"

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

class TransportModelEntity143(Base):
    __tablename__ = "transport_entity_143"

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

class TransportModelEntity144(Base):
    __tablename__ = "transport_entity_144"

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

class TransportModelEntity145(Base):
    __tablename__ = "transport_entity_145"

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

class TransportModelEntity146(Base):
    __tablename__ = "transport_entity_146"

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

class TransportModelEntity147(Base):
    __tablename__ = "transport_entity_147"

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

class TransportModelEntity148(Base):
    __tablename__ = "transport_entity_148"

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

class TransportModelEntity149(Base):
    __tablename__ = "transport_entity_149"

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

class TransportModelEntity150(Base):
    __tablename__ = "transport_entity_150"

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

class TransportModelEntity151(Base):
    __tablename__ = "transport_entity_151"

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

class TransportModelEntity152(Base):
    __tablename__ = "transport_entity_152"

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

class TransportModelEntity153(Base):
    __tablename__ = "transport_entity_153"

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

class TransportModelEntity154(Base):
    __tablename__ = "transport_entity_154"

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

class TransportModelEntity155(Base):
    __tablename__ = "transport_entity_155"

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

class TransportModelEntity156(Base):
    __tablename__ = "transport_entity_156"

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

class TransportModelEntity157(Base):
    __tablename__ = "transport_entity_157"

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

class TransportModelEntity158(Base):
    __tablename__ = "transport_entity_158"

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

class TransportModelEntity159(Base):
    __tablename__ = "transport_entity_159"

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

class TransportModelEntity160(Base):
    __tablename__ = "transport_entity_160"

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

class TransportModelEntity161(Base):
    __tablename__ = "transport_entity_161"

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

class TransportModelEntity162(Base):
    __tablename__ = "transport_entity_162"

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

class TransportModelEntity163(Base):
    __tablename__ = "transport_entity_163"

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

class TransportModelEntity164(Base):
    __tablename__ = "transport_entity_164"

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

class TransportModelEntity165(Base):
    __tablename__ = "transport_entity_165"

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

class TransportModelEntity166(Base):
    __tablename__ = "transport_entity_166"

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

class TransportModelEntity167(Base):
    __tablename__ = "transport_entity_167"

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

class TransportModelEntity168(Base):
    __tablename__ = "transport_entity_168"

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

class TransportModelEntity169(Base):
    __tablename__ = "transport_entity_169"

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

class TransportModelEntity170(Base):
    __tablename__ = "transport_entity_170"

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

class TransportModelEntity171(Base):
    __tablename__ = "transport_entity_171"

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

class TransportModelEntity172(Base):
    __tablename__ = "transport_entity_172"

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

class TransportModelEntity173(Base):
    __tablename__ = "transport_entity_173"

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

class TransportModelEntity174(Base):
    __tablename__ = "transport_entity_174"

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

class TransportModelEntity175(Base):
    __tablename__ = "transport_entity_175"

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

class TransportModelEntity176(Base):
    __tablename__ = "transport_entity_176"

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

class TransportModelEntity177(Base):
    __tablename__ = "transport_entity_177"

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

class TransportModelEntity178(Base):
    __tablename__ = "transport_entity_178"

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

class TransportModelEntity179(Base):
    __tablename__ = "transport_entity_179"

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

class TransportModelEntity180(Base):
    __tablename__ = "transport_entity_180"

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

class TransportModelEntity181(Base):
    __tablename__ = "transport_entity_181"

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

class TransportModelEntity182(Base):
    __tablename__ = "transport_entity_182"

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

class TransportModelEntity183(Base):
    __tablename__ = "transport_entity_183"

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

class TransportModelEntity184(Base):
    __tablename__ = "transport_entity_184"

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

class TransportModelEntity185(Base):
    __tablename__ = "transport_entity_185"

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

class TransportModelEntity186(Base):
    __tablename__ = "transport_entity_186"

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

class TransportModelEntity187(Base):
    __tablename__ = "transport_entity_187"

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

class TransportModelEntity188(Base):
    __tablename__ = "transport_entity_188"

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

class TransportModelEntity189(Base):
    __tablename__ = "transport_entity_189"

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

class TransportModelEntity190(Base):
    __tablename__ = "transport_entity_190"

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

class TransportModelEntity191(Base):
    __tablename__ = "transport_entity_191"

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

class TransportModelEntity192(Base):
    __tablename__ = "transport_entity_192"

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

class TransportModelEntity193(Base):
    __tablename__ = "transport_entity_193"

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

class TransportModelEntity194(Base):
    __tablename__ = "transport_entity_194"

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

class TransportModelEntity195(Base):
    __tablename__ = "transport_entity_195"

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

class TransportModelEntity196(Base):
    __tablename__ = "transport_entity_196"

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

class TransportModelEntity197(Base):
    __tablename__ = "transport_entity_197"

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

class TransportModelEntity198(Base):
    __tablename__ = "transport_entity_198"

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

class TransportModelEntity199(Base):
    __tablename__ = "transport_entity_199"

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

class TransportModelEntity200(Base):
    __tablename__ = "transport_entity_200"

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

