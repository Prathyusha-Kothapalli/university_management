"""
Executive & Departmental Dashboards - Pydantic Validation Schemas
Module: app.domains.dashboards.schemas
"""

from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class DashboardsBase(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the dashboards entity")
    category: str = Field(default="General", max_length=100)
    description: Optional[str] = Field(default=None)
    metadata_info: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsCreate(DashboardsBase):
    entity_code: str = Field(..., max_length=50)

class DashboardsUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata_info: Optional[Dict[str, Any]] = None

class DashboardsResponse(DashboardsBase):
    id: int
    entity_code: str
    status: str
    is_deleted: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule1Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule2Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule3Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule4Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule5Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule6Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule7Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule8Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule9Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule10Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule11Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule12Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule13Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule14Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule15Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule16Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule17Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule18Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class DashboardsSubModule19Schema(BaseModel):
    id: Optional[int] = None
    reference_number: str
    label: str
    priority: int = 1
    is_active: bool = True
    configuration: Optional[Dict[str, Any]] = None
    remarks: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
