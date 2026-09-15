"""
Academic & Curriculum Management - Pydantic Validation Schemas
Module: app.domains.academics.schemas
"""

from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class AcademicsBase(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the academics entity")
    category: str = Field(default="General", max_length=100)
    description: Optional[str] = Field(default=None)
    metadata_info: Optional[Dict[str, Any]] = Field(default_factory=dict)

class AcademicsCreate(AcademicsBase):
    entity_code: str = Field(..., max_length=50)

class AcademicsUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata_info: Optional[Dict[str, Any]] = None

class AcademicsResponse(AcademicsBase):
    id: int
    entity_code: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule1Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule2Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule3Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule4Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule5Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule6Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule7Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule8Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule9Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule10Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule11Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule12Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule13Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule14Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule15Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule16Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule17Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule18Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AcademicsSubModule19Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
