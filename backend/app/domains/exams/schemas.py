"""
Examinations & Result Management - Pydantic Validation Schemas
Module: app.domains.exams.schemas
"""

from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class ExamsBase(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the exams entity")
    category: str = Field(default="General", max_length=100)
    description: Optional[str] = Field(default=None)
    metadata_info: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsCreate(ExamsBase):
    entity_code: str = Field(..., max_length=50)

class ExamsUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata_info: Optional[Dict[str, Any]] = None

class ExamsResponse(ExamsBase):
    id: int
    entity_code: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule1Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule2Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule3Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule4Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule5Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule6Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule7Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule8Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule9Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule10Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule11Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule12Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule13Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule14Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule15Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule16Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule17Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule18Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ExamsSubModule19Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
