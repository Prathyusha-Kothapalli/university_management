"""
Campus Health & Clinic Management - Pydantic Validation Schemas
Module: app.domains.health.schemas
"""

from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class HealthBase(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the health entity")
    category: str = Field(default="General", max_length=100)
    description: Optional[str] = Field(default=None)
    metadata_info: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthCreate(HealthBase):
    entity_code: str = Field(..., max_length=50)

class HealthUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata_info: Optional[Dict[str, Any]] = None

class HealthResponse(HealthBase):
    id: int
    entity_code: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule1Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule2Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule3Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule4Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule5Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule6Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule7Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule8Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule9Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule10Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule11Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule12Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule13Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule14Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule15Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule16Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule17Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule18Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class HealthSubModule19Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
