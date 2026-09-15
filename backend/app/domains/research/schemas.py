"""
Research, Grants & Lab Inventory - Pydantic Validation Schemas
Module: app.domains.research.schemas
"""

from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class ResearchBase(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the research entity")
    category: str = Field(default="General", max_length=100)
    description: Optional[str] = Field(default=None)
    metadata_info: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ResearchCreate(ResearchBase):
    entity_code: str = Field(..., max_length=50)

class ResearchUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata_info: Optional[Dict[str, Any]] = None

class ResearchResponse(ResearchBase):
    id: int
    entity_code: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule1Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule2Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule3Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule4Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule5Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule6Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule7Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule8Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule9Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule10Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule11Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule12Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule13Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule14Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule15Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule16Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule17Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule18Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ResearchSubModule19Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
