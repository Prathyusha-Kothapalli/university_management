"""
Executive & Departmental Dashboards - Pydantic Validation Schemas
Module: app.domains.dashboards.schemas
"""
from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class DashboardsSchemaEntity1Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 1")
    category: str = Field(default="Category_1", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=1 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity1Create(DashboardsSchemaEntity1Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity1Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity1Response(DashboardsSchemaEntity1Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity2Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 2")
    category: str = Field(default="Category_2", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=2 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity2Create(DashboardsSchemaEntity2Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity2Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity2Response(DashboardsSchemaEntity2Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity3Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 3")
    category: str = Field(default="Category_3", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=3 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity3Create(DashboardsSchemaEntity3Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity3Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity3Response(DashboardsSchemaEntity3Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity4Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 4")
    category: str = Field(default="Category_4", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=4 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity4Create(DashboardsSchemaEntity4Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity4Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity4Response(DashboardsSchemaEntity4Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity5Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 5")
    category: str = Field(default="Category_5", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=5 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity5Create(DashboardsSchemaEntity5Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity5Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity5Response(DashboardsSchemaEntity5Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity6Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 6")
    category: str = Field(default="Category_6", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=6 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity6Create(DashboardsSchemaEntity6Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity6Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity6Response(DashboardsSchemaEntity6Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity7Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 7")
    category: str = Field(default="Category_7", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=7 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity7Create(DashboardsSchemaEntity7Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity7Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity7Response(DashboardsSchemaEntity7Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity8Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 8")
    category: str = Field(default="Category_8", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=8 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity8Create(DashboardsSchemaEntity8Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity8Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity8Response(DashboardsSchemaEntity8Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity9Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 9")
    category: str = Field(default="Category_9", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=9 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity9Create(DashboardsSchemaEntity9Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity9Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity9Response(DashboardsSchemaEntity9Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity10Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 10")
    category: str = Field(default="Category_10", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=10 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity10Create(DashboardsSchemaEntity10Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity10Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity10Response(DashboardsSchemaEntity10Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity11Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 11")
    category: str = Field(default="Category_11", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=11 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity11Create(DashboardsSchemaEntity11Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity11Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity11Response(DashboardsSchemaEntity11Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity12Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 12")
    category: str = Field(default="Category_12", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=12 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity12Create(DashboardsSchemaEntity12Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity12Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity12Response(DashboardsSchemaEntity12Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity13Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 13")
    category: str = Field(default="Category_13", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=13 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity13Create(DashboardsSchemaEntity13Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity13Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity13Response(DashboardsSchemaEntity13Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity14Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 14")
    category: str = Field(default="Category_14", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=14 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity14Create(DashboardsSchemaEntity14Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity14Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity14Response(DashboardsSchemaEntity14Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity15Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 15")
    category: str = Field(default="Category_15", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=15 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity15Create(DashboardsSchemaEntity15Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity15Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity15Response(DashboardsSchemaEntity15Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity16Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 16")
    category: str = Field(default="Category_16", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=16 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity16Create(DashboardsSchemaEntity16Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity16Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity16Response(DashboardsSchemaEntity16Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity17Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 17")
    category: str = Field(default="Category_17", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=17 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity17Create(DashboardsSchemaEntity17Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity17Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity17Response(DashboardsSchemaEntity17Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity18Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 18")
    category: str = Field(default="Category_18", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=18 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity18Create(DashboardsSchemaEntity18Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity18Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity18Response(DashboardsSchemaEntity18Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity19Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 19")
    category: str = Field(default="Category_19", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=19 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity19Create(DashboardsSchemaEntity19Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity19Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity19Response(DashboardsSchemaEntity19Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity20Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 20")
    category: str = Field(default="Category_20", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=20 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity20Create(DashboardsSchemaEntity20Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity20Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity20Response(DashboardsSchemaEntity20Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity21Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 21")
    category: str = Field(default="Category_21", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=21 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity21Create(DashboardsSchemaEntity21Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity21Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity21Response(DashboardsSchemaEntity21Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity22Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 22")
    category: str = Field(default="Category_22", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=22 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity22Create(DashboardsSchemaEntity22Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity22Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity22Response(DashboardsSchemaEntity22Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity23Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 23")
    category: str = Field(default="Category_23", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=23 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity23Create(DashboardsSchemaEntity23Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity23Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity23Response(DashboardsSchemaEntity23Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity24Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 24")
    category: str = Field(default="Category_24", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=24 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity24Create(DashboardsSchemaEntity24Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity24Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity24Response(DashboardsSchemaEntity24Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity25Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 25")
    category: str = Field(default="Category_25", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=25 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity25Create(DashboardsSchemaEntity25Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity25Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity25Response(DashboardsSchemaEntity25Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity26Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 26")
    category: str = Field(default="Category_26", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=26 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity26Create(DashboardsSchemaEntity26Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity26Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity26Response(DashboardsSchemaEntity26Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity27Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 27")
    category: str = Field(default="Category_27", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=27 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity27Create(DashboardsSchemaEntity27Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity27Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity27Response(DashboardsSchemaEntity27Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity28Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 28")
    category: str = Field(default="Category_28", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=28 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity28Create(DashboardsSchemaEntity28Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity28Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity28Response(DashboardsSchemaEntity28Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity29Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 29")
    category: str = Field(default="Category_29", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=29 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity29Create(DashboardsSchemaEntity29Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity29Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity29Response(DashboardsSchemaEntity29Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity30Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 30")
    category: str = Field(default="Category_30", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=30 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity30Create(DashboardsSchemaEntity30Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity30Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity30Response(DashboardsSchemaEntity30Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity31Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 31")
    category: str = Field(default="Category_31", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=31 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity31Create(DashboardsSchemaEntity31Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity31Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity31Response(DashboardsSchemaEntity31Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity32Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 32")
    category: str = Field(default="Category_32", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=32 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity32Create(DashboardsSchemaEntity32Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity32Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity32Response(DashboardsSchemaEntity32Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity33Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 33")
    category: str = Field(default="Category_33", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=33 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity33Create(DashboardsSchemaEntity33Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity33Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity33Response(DashboardsSchemaEntity33Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity34Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 34")
    category: str = Field(default="Category_34", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=34 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity34Create(DashboardsSchemaEntity34Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity34Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity34Response(DashboardsSchemaEntity34Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity35Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 35")
    category: str = Field(default="Category_35", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=35 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity35Create(DashboardsSchemaEntity35Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity35Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity35Response(DashboardsSchemaEntity35Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity36Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 36")
    category: str = Field(default="Category_36", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=36 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity36Create(DashboardsSchemaEntity36Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity36Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity36Response(DashboardsSchemaEntity36Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity37Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 37")
    category: str = Field(default="Category_37", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=37 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity37Create(DashboardsSchemaEntity37Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity37Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity37Response(DashboardsSchemaEntity37Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity38Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 38")
    category: str = Field(default="Category_38", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=38 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity38Create(DashboardsSchemaEntity38Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity38Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity38Response(DashboardsSchemaEntity38Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity39Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 39")
    category: str = Field(default="Category_39", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=39 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity39Create(DashboardsSchemaEntity39Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity39Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity39Response(DashboardsSchemaEntity39Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity40Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 40")
    category: str = Field(default="Category_40", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=40 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity40Create(DashboardsSchemaEntity40Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity40Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity40Response(DashboardsSchemaEntity40Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity41Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 41")
    category: str = Field(default="Category_41", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=41 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity41Create(DashboardsSchemaEntity41Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity41Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity41Response(DashboardsSchemaEntity41Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity42Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 42")
    category: str = Field(default="Category_42", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=42 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity42Create(DashboardsSchemaEntity42Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity42Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity42Response(DashboardsSchemaEntity42Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity43Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 43")
    category: str = Field(default="Category_43", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=43 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity43Create(DashboardsSchemaEntity43Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity43Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity43Response(DashboardsSchemaEntity43Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity44Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 44")
    category: str = Field(default="Category_44", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=44 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity44Create(DashboardsSchemaEntity44Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity44Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity44Response(DashboardsSchemaEntity44Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity45Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 45")
    category: str = Field(default="Category_45", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=45 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity45Create(DashboardsSchemaEntity45Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity45Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity45Response(DashboardsSchemaEntity45Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity46Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 46")
    category: str = Field(default="Category_46", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=46 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity46Create(DashboardsSchemaEntity46Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity46Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity46Response(DashboardsSchemaEntity46Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity47Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 47")
    category: str = Field(default="Category_47", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=47 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity47Create(DashboardsSchemaEntity47Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity47Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity47Response(DashboardsSchemaEntity47Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity48Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 48")
    category: str = Field(default="Category_48", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=48 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity48Create(DashboardsSchemaEntity48Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity48Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity48Response(DashboardsSchemaEntity48Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity49Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 49")
    category: str = Field(default="Category_49", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=49 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity49Create(DashboardsSchemaEntity49Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity49Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity49Response(DashboardsSchemaEntity49Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity50Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 50")
    category: str = Field(default="Category_50", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=50 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity50Create(DashboardsSchemaEntity50Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity50Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity50Response(DashboardsSchemaEntity50Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity51Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 51")
    category: str = Field(default="Category_51", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=51 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity51Create(DashboardsSchemaEntity51Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity51Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity51Response(DashboardsSchemaEntity51Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity52Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 52")
    category: str = Field(default="Category_52", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=52 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity52Create(DashboardsSchemaEntity52Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity52Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity52Response(DashboardsSchemaEntity52Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity53Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 53")
    category: str = Field(default="Category_53", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=53 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity53Create(DashboardsSchemaEntity53Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity53Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity53Response(DashboardsSchemaEntity53Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity54Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 54")
    category: str = Field(default="Category_54", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=54 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity54Create(DashboardsSchemaEntity54Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity54Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity54Response(DashboardsSchemaEntity54Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity55Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 55")
    category: str = Field(default="Category_55", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=55 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity55Create(DashboardsSchemaEntity55Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity55Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity55Response(DashboardsSchemaEntity55Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity56Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 56")
    category: str = Field(default="Category_56", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=56 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity56Create(DashboardsSchemaEntity56Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity56Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity56Response(DashboardsSchemaEntity56Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity57Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 57")
    category: str = Field(default="Category_57", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=57 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity57Create(DashboardsSchemaEntity57Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity57Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity57Response(DashboardsSchemaEntity57Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity58Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 58")
    category: str = Field(default="Category_58", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=58 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity58Create(DashboardsSchemaEntity58Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity58Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity58Response(DashboardsSchemaEntity58Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity59Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 59")
    category: str = Field(default="Category_59", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=59 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity59Create(DashboardsSchemaEntity59Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity59Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity59Response(DashboardsSchemaEntity59Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity60Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 60")
    category: str = Field(default="Category_60", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=60 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity60Create(DashboardsSchemaEntity60Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity60Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity60Response(DashboardsSchemaEntity60Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity61Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 61")
    category: str = Field(default="Category_61", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=61 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity61Create(DashboardsSchemaEntity61Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity61Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity61Response(DashboardsSchemaEntity61Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity62Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 62")
    category: str = Field(default="Category_62", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=62 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity62Create(DashboardsSchemaEntity62Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity62Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity62Response(DashboardsSchemaEntity62Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity63Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 63")
    category: str = Field(default="Category_63", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=63 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity63Create(DashboardsSchemaEntity63Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity63Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity63Response(DashboardsSchemaEntity63Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity64Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 64")
    category: str = Field(default="Category_64", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=64 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity64Create(DashboardsSchemaEntity64Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity64Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity64Response(DashboardsSchemaEntity64Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity65Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 65")
    category: str = Field(default="Category_65", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=65 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity65Create(DashboardsSchemaEntity65Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity65Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity65Response(DashboardsSchemaEntity65Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity66Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 66")
    category: str = Field(default="Category_66", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=66 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity66Create(DashboardsSchemaEntity66Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity66Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity66Response(DashboardsSchemaEntity66Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity67Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 67")
    category: str = Field(default="Category_67", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=67 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity67Create(DashboardsSchemaEntity67Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity67Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity67Response(DashboardsSchemaEntity67Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity68Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 68")
    category: str = Field(default="Category_68", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=68 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity68Create(DashboardsSchemaEntity68Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity68Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity68Response(DashboardsSchemaEntity68Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity69Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 69")
    category: str = Field(default="Category_69", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=69 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity69Create(DashboardsSchemaEntity69Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity69Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity69Response(DashboardsSchemaEntity69Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity70Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 70")
    category: str = Field(default="Category_70", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=70 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity70Create(DashboardsSchemaEntity70Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity70Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity70Response(DashboardsSchemaEntity70Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity71Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 71")
    category: str = Field(default="Category_71", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=71 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity71Create(DashboardsSchemaEntity71Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity71Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity71Response(DashboardsSchemaEntity71Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity72Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 72")
    category: str = Field(default="Category_72", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=72 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity72Create(DashboardsSchemaEntity72Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity72Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity72Response(DashboardsSchemaEntity72Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity73Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 73")
    category: str = Field(default="Category_73", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=73 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity73Create(DashboardsSchemaEntity73Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity73Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity73Response(DashboardsSchemaEntity73Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity74Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 74")
    category: str = Field(default="Category_74", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=74 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity74Create(DashboardsSchemaEntity74Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity74Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity74Response(DashboardsSchemaEntity74Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity75Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 75")
    category: str = Field(default="Category_75", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=75 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity75Create(DashboardsSchemaEntity75Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity75Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity75Response(DashboardsSchemaEntity75Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity76Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 76")
    category: str = Field(default="Category_76", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=76 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity76Create(DashboardsSchemaEntity76Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity76Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity76Response(DashboardsSchemaEntity76Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity77Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 77")
    category: str = Field(default="Category_77", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=77 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity77Create(DashboardsSchemaEntity77Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity77Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity77Response(DashboardsSchemaEntity77Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity78Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 78")
    category: str = Field(default="Category_78", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=78 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity78Create(DashboardsSchemaEntity78Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity78Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity78Response(DashboardsSchemaEntity78Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity79Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 79")
    category: str = Field(default="Category_79", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=79 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity79Create(DashboardsSchemaEntity79Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity79Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity79Response(DashboardsSchemaEntity79Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity80Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 80")
    category: str = Field(default="Category_80", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=80 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity80Create(DashboardsSchemaEntity80Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity80Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity80Response(DashboardsSchemaEntity80Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity81Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 81")
    category: str = Field(default="Category_81", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=81 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity81Create(DashboardsSchemaEntity81Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity81Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity81Response(DashboardsSchemaEntity81Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity82Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 82")
    category: str = Field(default="Category_82", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=82 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity82Create(DashboardsSchemaEntity82Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity82Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity82Response(DashboardsSchemaEntity82Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity83Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 83")
    category: str = Field(default="Category_83", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=83 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity83Create(DashboardsSchemaEntity83Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity83Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity83Response(DashboardsSchemaEntity83Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity84Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 84")
    category: str = Field(default="Category_84", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=84 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity84Create(DashboardsSchemaEntity84Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity84Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity84Response(DashboardsSchemaEntity84Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity85Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 85")
    category: str = Field(default="Category_85", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=85 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity85Create(DashboardsSchemaEntity85Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity85Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity85Response(DashboardsSchemaEntity85Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity86Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 86")
    category: str = Field(default="Category_86", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=86 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity86Create(DashboardsSchemaEntity86Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity86Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity86Response(DashboardsSchemaEntity86Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity87Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 87")
    category: str = Field(default="Category_87", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=87 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity87Create(DashboardsSchemaEntity87Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity87Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity87Response(DashboardsSchemaEntity87Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity88Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 88")
    category: str = Field(default="Category_88", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=88 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity88Create(DashboardsSchemaEntity88Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity88Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity88Response(DashboardsSchemaEntity88Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity89Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 89")
    category: str = Field(default="Category_89", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=89 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity89Create(DashboardsSchemaEntity89Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity89Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity89Response(DashboardsSchemaEntity89Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity90Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 90")
    category: str = Field(default="Category_90", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=90 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity90Create(DashboardsSchemaEntity90Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity90Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity90Response(DashboardsSchemaEntity90Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity91Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 91")
    category: str = Field(default="Category_91", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=91 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity91Create(DashboardsSchemaEntity91Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity91Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity91Response(DashboardsSchemaEntity91Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity92Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 92")
    category: str = Field(default="Category_92", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=92 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity92Create(DashboardsSchemaEntity92Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity92Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity92Response(DashboardsSchemaEntity92Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity93Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 93")
    category: str = Field(default="Category_93", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=93 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity93Create(DashboardsSchemaEntity93Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity93Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity93Response(DashboardsSchemaEntity93Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity94Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 94")
    category: str = Field(default="Category_94", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=94 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity94Create(DashboardsSchemaEntity94Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity94Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity94Response(DashboardsSchemaEntity94Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity95Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 95")
    category: str = Field(default="Category_95", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=95 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity95Create(DashboardsSchemaEntity95Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity95Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity95Response(DashboardsSchemaEntity95Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity96Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 96")
    category: str = Field(default="Category_96", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=96 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity96Create(DashboardsSchemaEntity96Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity96Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity96Response(DashboardsSchemaEntity96Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity97Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 97")
    category: str = Field(default="Category_97", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=97 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity97Create(DashboardsSchemaEntity97Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity97Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity97Response(DashboardsSchemaEntity97Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity98Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 98")
    category: str = Field(default="Category_98", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=98 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity98Create(DashboardsSchemaEntity98Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity98Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity98Response(DashboardsSchemaEntity98Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity99Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 99")
    category: str = Field(default="Category_99", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=99 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity99Create(DashboardsSchemaEntity99Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity99Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity99Response(DashboardsSchemaEntity99Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity100Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 100")
    category: str = Field(default="Category_100", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=100 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity100Create(DashboardsSchemaEntity100Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity100Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity100Response(DashboardsSchemaEntity100Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity101Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 101")
    category: str = Field(default="Category_101", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=101 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity101Create(DashboardsSchemaEntity101Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity101Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity101Response(DashboardsSchemaEntity101Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity102Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 102")
    category: str = Field(default="Category_102", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=102 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity102Create(DashboardsSchemaEntity102Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity102Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity102Response(DashboardsSchemaEntity102Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity103Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 103")
    category: str = Field(default="Category_103", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=103 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity103Create(DashboardsSchemaEntity103Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity103Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity103Response(DashboardsSchemaEntity103Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity104Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 104")
    category: str = Field(default="Category_104", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=104 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity104Create(DashboardsSchemaEntity104Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity104Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity104Response(DashboardsSchemaEntity104Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity105Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 105")
    category: str = Field(default="Category_105", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=105 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity105Create(DashboardsSchemaEntity105Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity105Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity105Response(DashboardsSchemaEntity105Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity106Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 106")
    category: str = Field(default="Category_106", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=106 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity106Create(DashboardsSchemaEntity106Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity106Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity106Response(DashboardsSchemaEntity106Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity107Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 107")
    category: str = Field(default="Category_107", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=107 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity107Create(DashboardsSchemaEntity107Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity107Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity107Response(DashboardsSchemaEntity107Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity108Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 108")
    category: str = Field(default="Category_108", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=108 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity108Create(DashboardsSchemaEntity108Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity108Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity108Response(DashboardsSchemaEntity108Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity109Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 109")
    category: str = Field(default="Category_109", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=109 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity109Create(DashboardsSchemaEntity109Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity109Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity109Response(DashboardsSchemaEntity109Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity110Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 110")
    category: str = Field(default="Category_110", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=110 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity110Create(DashboardsSchemaEntity110Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity110Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity110Response(DashboardsSchemaEntity110Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity111Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 111")
    category: str = Field(default="Category_111", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=111 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity111Create(DashboardsSchemaEntity111Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity111Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity111Response(DashboardsSchemaEntity111Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity112Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 112")
    category: str = Field(default="Category_112", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=112 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity112Create(DashboardsSchemaEntity112Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity112Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity112Response(DashboardsSchemaEntity112Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity113Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 113")
    category: str = Field(default="Category_113", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=113 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity113Create(DashboardsSchemaEntity113Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity113Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity113Response(DashboardsSchemaEntity113Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity114Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 114")
    category: str = Field(default="Category_114", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=114 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity114Create(DashboardsSchemaEntity114Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity114Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity114Response(DashboardsSchemaEntity114Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity115Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 115")
    category: str = Field(default="Category_115", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=115 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity115Create(DashboardsSchemaEntity115Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity115Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity115Response(DashboardsSchemaEntity115Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity116Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 116")
    category: str = Field(default="Category_116", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=116 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity116Create(DashboardsSchemaEntity116Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity116Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity116Response(DashboardsSchemaEntity116Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity117Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 117")
    category: str = Field(default="Category_117", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=117 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity117Create(DashboardsSchemaEntity117Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity117Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity117Response(DashboardsSchemaEntity117Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity118Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 118")
    category: str = Field(default="Category_118", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=118 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity118Create(DashboardsSchemaEntity118Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity118Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity118Response(DashboardsSchemaEntity118Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity119Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 119")
    category: str = Field(default="Category_119", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=119 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity119Create(DashboardsSchemaEntity119Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity119Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity119Response(DashboardsSchemaEntity119Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity120Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 120")
    category: str = Field(default="Category_120", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=120 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity120Create(DashboardsSchemaEntity120Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity120Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity120Response(DashboardsSchemaEntity120Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity121Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 121")
    category: str = Field(default="Category_121", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=121 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity121Create(DashboardsSchemaEntity121Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity121Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity121Response(DashboardsSchemaEntity121Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity122Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 122")
    category: str = Field(default="Category_122", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=122 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity122Create(DashboardsSchemaEntity122Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity122Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity122Response(DashboardsSchemaEntity122Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity123Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 123")
    category: str = Field(default="Category_123", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=123 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity123Create(DashboardsSchemaEntity123Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity123Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity123Response(DashboardsSchemaEntity123Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity124Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 124")
    category: str = Field(default="Category_124", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=124 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity124Create(DashboardsSchemaEntity124Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity124Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity124Response(DashboardsSchemaEntity124Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity125Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 125")
    category: str = Field(default="Category_125", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=125 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity125Create(DashboardsSchemaEntity125Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity125Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity125Response(DashboardsSchemaEntity125Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity126Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 126")
    category: str = Field(default="Category_126", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=126 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity126Create(DashboardsSchemaEntity126Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity126Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity126Response(DashboardsSchemaEntity126Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity127Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 127")
    category: str = Field(default="Category_127", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=127 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity127Create(DashboardsSchemaEntity127Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity127Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity127Response(DashboardsSchemaEntity127Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity128Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 128")
    category: str = Field(default="Category_128", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=128 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity128Create(DashboardsSchemaEntity128Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity128Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity128Response(DashboardsSchemaEntity128Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity129Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 129")
    category: str = Field(default="Category_129", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=129 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity129Create(DashboardsSchemaEntity129Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity129Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity129Response(DashboardsSchemaEntity129Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity130Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 130")
    category: str = Field(default="Category_130", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=130 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity130Create(DashboardsSchemaEntity130Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity130Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity130Response(DashboardsSchemaEntity130Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity131Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 131")
    category: str = Field(default="Category_131", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=131 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity131Create(DashboardsSchemaEntity131Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity131Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity131Response(DashboardsSchemaEntity131Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity132Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 132")
    category: str = Field(default="Category_132", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=132 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity132Create(DashboardsSchemaEntity132Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity132Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity132Response(DashboardsSchemaEntity132Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity133Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 133")
    category: str = Field(default="Category_133", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=133 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity133Create(DashboardsSchemaEntity133Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity133Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity133Response(DashboardsSchemaEntity133Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity134Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 134")
    category: str = Field(default="Category_134", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=134 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity134Create(DashboardsSchemaEntity134Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity134Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity134Response(DashboardsSchemaEntity134Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity135Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 135")
    category: str = Field(default="Category_135", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=135 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity135Create(DashboardsSchemaEntity135Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity135Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity135Response(DashboardsSchemaEntity135Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity136Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 136")
    category: str = Field(default="Category_136", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=136 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity136Create(DashboardsSchemaEntity136Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity136Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity136Response(DashboardsSchemaEntity136Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity137Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 137")
    category: str = Field(default="Category_137", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=137 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity137Create(DashboardsSchemaEntity137Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity137Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity137Response(DashboardsSchemaEntity137Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity138Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 138")
    category: str = Field(default="Category_138", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=138 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity138Create(DashboardsSchemaEntity138Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity138Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity138Response(DashboardsSchemaEntity138Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity139Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 139")
    category: str = Field(default="Category_139", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=139 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity139Create(DashboardsSchemaEntity139Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity139Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity139Response(DashboardsSchemaEntity139Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity140Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 140")
    category: str = Field(default="Category_140", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=140 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity140Create(DashboardsSchemaEntity140Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity140Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity140Response(DashboardsSchemaEntity140Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity141Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 141")
    category: str = Field(default="Category_141", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=141 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity141Create(DashboardsSchemaEntity141Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity141Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity141Response(DashboardsSchemaEntity141Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity142Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 142")
    category: str = Field(default="Category_142", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=142 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity142Create(DashboardsSchemaEntity142Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity142Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity142Response(DashboardsSchemaEntity142Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity143Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 143")
    category: str = Field(default="Category_143", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=143 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity143Create(DashboardsSchemaEntity143Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity143Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity143Response(DashboardsSchemaEntity143Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity144Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 144")
    category: str = Field(default="Category_144", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=144 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity144Create(DashboardsSchemaEntity144Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity144Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity144Response(DashboardsSchemaEntity144Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity145Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 145")
    category: str = Field(default="Category_145", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=145 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity145Create(DashboardsSchemaEntity145Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity145Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity145Response(DashboardsSchemaEntity145Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity146Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 146")
    category: str = Field(default="Category_146", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=146 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity146Create(DashboardsSchemaEntity146Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity146Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity146Response(DashboardsSchemaEntity146Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity147Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 147")
    category: str = Field(default="Category_147", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=147 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity147Create(DashboardsSchemaEntity147Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity147Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity147Response(DashboardsSchemaEntity147Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity148Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 148")
    category: str = Field(default="Category_148", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=148 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity148Create(DashboardsSchemaEntity148Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity148Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity148Response(DashboardsSchemaEntity148Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity149Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 149")
    category: str = Field(default="Category_149", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=149 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity149Create(DashboardsSchemaEntity149Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity149Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity149Response(DashboardsSchemaEntity149Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity150Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 150")
    category: str = Field(default="Category_150", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=150 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity150Create(DashboardsSchemaEntity150Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity150Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity150Response(DashboardsSchemaEntity150Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity151Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 151")
    category: str = Field(default="Category_151", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=151 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity151Create(DashboardsSchemaEntity151Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity151Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity151Response(DashboardsSchemaEntity151Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity152Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 152")
    category: str = Field(default="Category_152", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=152 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity152Create(DashboardsSchemaEntity152Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity152Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity152Response(DashboardsSchemaEntity152Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity153Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 153")
    category: str = Field(default="Category_153", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=153 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity153Create(DashboardsSchemaEntity153Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity153Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity153Response(DashboardsSchemaEntity153Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity154Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 154")
    category: str = Field(default="Category_154", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=154 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity154Create(DashboardsSchemaEntity154Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity154Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity154Response(DashboardsSchemaEntity154Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity155Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 155")
    category: str = Field(default="Category_155", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=155 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity155Create(DashboardsSchemaEntity155Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity155Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity155Response(DashboardsSchemaEntity155Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity156Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 156")
    category: str = Field(default="Category_156", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=156 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity156Create(DashboardsSchemaEntity156Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity156Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity156Response(DashboardsSchemaEntity156Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity157Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 157")
    category: str = Field(default="Category_157", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=157 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity157Create(DashboardsSchemaEntity157Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity157Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity157Response(DashboardsSchemaEntity157Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity158Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 158")
    category: str = Field(default="Category_158", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=158 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity158Create(DashboardsSchemaEntity158Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity158Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity158Response(DashboardsSchemaEntity158Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity159Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 159")
    category: str = Field(default="Category_159", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=159 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity159Create(DashboardsSchemaEntity159Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity159Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity159Response(DashboardsSchemaEntity159Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity160Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 160")
    category: str = Field(default="Category_160", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=160 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity160Create(DashboardsSchemaEntity160Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity160Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity160Response(DashboardsSchemaEntity160Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity161Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 161")
    category: str = Field(default="Category_161", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=161 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity161Create(DashboardsSchemaEntity161Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity161Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity161Response(DashboardsSchemaEntity161Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity162Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 162")
    category: str = Field(default="Category_162", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=162 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity162Create(DashboardsSchemaEntity162Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity162Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity162Response(DashboardsSchemaEntity162Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity163Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 163")
    category: str = Field(default="Category_163", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=163 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity163Create(DashboardsSchemaEntity163Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity163Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity163Response(DashboardsSchemaEntity163Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity164Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 164")
    category: str = Field(default="Category_164", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=164 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity164Create(DashboardsSchemaEntity164Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity164Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity164Response(DashboardsSchemaEntity164Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity165Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 165")
    category: str = Field(default="Category_165", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=165 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity165Create(DashboardsSchemaEntity165Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity165Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity165Response(DashboardsSchemaEntity165Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity166Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 166")
    category: str = Field(default="Category_166", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=166 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity166Create(DashboardsSchemaEntity166Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity166Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity166Response(DashboardsSchemaEntity166Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity167Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 167")
    category: str = Field(default="Category_167", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=167 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity167Create(DashboardsSchemaEntity167Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity167Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity167Response(DashboardsSchemaEntity167Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity168Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 168")
    category: str = Field(default="Category_168", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=168 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity168Create(DashboardsSchemaEntity168Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity168Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity168Response(DashboardsSchemaEntity168Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity169Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 169")
    category: str = Field(default="Category_169", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=169 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity169Create(DashboardsSchemaEntity169Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity169Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity169Response(DashboardsSchemaEntity169Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity170Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 170")
    category: str = Field(default="Category_170", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=170 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity170Create(DashboardsSchemaEntity170Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity170Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity170Response(DashboardsSchemaEntity170Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity171Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 171")
    category: str = Field(default="Category_171", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=171 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity171Create(DashboardsSchemaEntity171Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity171Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity171Response(DashboardsSchemaEntity171Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity172Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 172")
    category: str = Field(default="Category_172", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=172 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity172Create(DashboardsSchemaEntity172Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity172Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity172Response(DashboardsSchemaEntity172Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity173Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 173")
    category: str = Field(default="Category_173", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=173 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity173Create(DashboardsSchemaEntity173Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity173Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity173Response(DashboardsSchemaEntity173Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity174Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 174")
    category: str = Field(default="Category_174", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=174 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity174Create(DashboardsSchemaEntity174Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity174Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity174Response(DashboardsSchemaEntity174Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity175Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 175")
    category: str = Field(default="Category_175", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=175 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity175Create(DashboardsSchemaEntity175Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity175Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity175Response(DashboardsSchemaEntity175Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity176Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 176")
    category: str = Field(default="Category_176", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=176 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity176Create(DashboardsSchemaEntity176Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity176Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity176Response(DashboardsSchemaEntity176Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity177Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 177")
    category: str = Field(default="Category_177", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=177 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity177Create(DashboardsSchemaEntity177Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity177Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity177Response(DashboardsSchemaEntity177Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity178Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 178")
    category: str = Field(default="Category_178", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=178 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity178Create(DashboardsSchemaEntity178Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity178Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity178Response(DashboardsSchemaEntity178Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity179Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 179")
    category: str = Field(default="Category_179", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=179 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity179Create(DashboardsSchemaEntity179Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity179Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity179Response(DashboardsSchemaEntity179Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity180Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 180")
    category: str = Field(default="Category_180", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=180 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity180Create(DashboardsSchemaEntity180Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity180Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity180Response(DashboardsSchemaEntity180Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity181Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 181")
    category: str = Field(default="Category_181", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=181 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity181Create(DashboardsSchemaEntity181Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity181Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity181Response(DashboardsSchemaEntity181Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity182Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 182")
    category: str = Field(default="Category_182", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=182 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity182Create(DashboardsSchemaEntity182Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity182Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity182Response(DashboardsSchemaEntity182Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity183Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 183")
    category: str = Field(default="Category_183", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=183 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity183Create(DashboardsSchemaEntity183Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity183Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity183Response(DashboardsSchemaEntity183Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity184Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 184")
    category: str = Field(default="Category_184", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=184 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity184Create(DashboardsSchemaEntity184Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity184Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity184Response(DashboardsSchemaEntity184Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity185Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 185")
    category: str = Field(default="Category_185", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=185 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity185Create(DashboardsSchemaEntity185Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity185Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity185Response(DashboardsSchemaEntity185Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity186Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 186")
    category: str = Field(default="Category_186", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=186 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity186Create(DashboardsSchemaEntity186Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity186Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity186Response(DashboardsSchemaEntity186Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity187Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 187")
    category: str = Field(default="Category_187", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=187 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity187Create(DashboardsSchemaEntity187Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity187Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity187Response(DashboardsSchemaEntity187Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity188Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 188")
    category: str = Field(default="Category_188", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=188 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity188Create(DashboardsSchemaEntity188Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity188Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity188Response(DashboardsSchemaEntity188Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity189Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 189")
    category: str = Field(default="Category_189", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=189 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity189Create(DashboardsSchemaEntity189Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity189Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity189Response(DashboardsSchemaEntity189Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity190Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 190")
    category: str = Field(default="Category_190", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=190 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity190Create(DashboardsSchemaEntity190Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity190Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity190Response(DashboardsSchemaEntity190Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity191Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 191")
    category: str = Field(default="Category_191", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=191 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity191Create(DashboardsSchemaEntity191Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity191Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity191Response(DashboardsSchemaEntity191Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity192Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 192")
    category: str = Field(default="Category_192", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=192 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity192Create(DashboardsSchemaEntity192Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity192Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity192Response(DashboardsSchemaEntity192Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity193Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 193")
    category: str = Field(default="Category_193", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=193 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity193Create(DashboardsSchemaEntity193Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity193Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity193Response(DashboardsSchemaEntity193Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity194Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 194")
    category: str = Field(default="Category_194", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=194 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity194Create(DashboardsSchemaEntity194Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity194Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity194Response(DashboardsSchemaEntity194Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity195Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 195")
    category: str = Field(default="Category_195", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=195 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity195Create(DashboardsSchemaEntity195Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity195Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity195Response(DashboardsSchemaEntity195Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity196Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 196")
    category: str = Field(default="Category_196", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=196 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity196Create(DashboardsSchemaEntity196Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity196Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity196Response(DashboardsSchemaEntity196Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity197Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 197")
    category: str = Field(default="Category_197", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=197 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity197Create(DashboardsSchemaEntity197Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity197Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity197Response(DashboardsSchemaEntity197Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity198Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 198")
    category: str = Field(default="Category_198", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=198 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity198Create(DashboardsSchemaEntity198Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity198Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity198Response(DashboardsSchemaEntity198Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity199Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 199")
    category: str = Field(default="Category_199", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=199 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity199Create(DashboardsSchemaEntity199Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity199Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity199Response(DashboardsSchemaEntity199Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity200Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 200")
    category: str = Field(default="Category_200", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=200 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity200Create(DashboardsSchemaEntity200Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity200Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity200Response(DashboardsSchemaEntity200Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity201Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 201")
    category: str = Field(default="Category_201", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=201 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity201Create(DashboardsSchemaEntity201Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity201Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity201Response(DashboardsSchemaEntity201Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity202Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 202")
    category: str = Field(default="Category_202", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=202 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity202Create(DashboardsSchemaEntity202Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity202Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity202Response(DashboardsSchemaEntity202Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity203Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 203")
    category: str = Field(default="Category_203", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=203 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity203Create(DashboardsSchemaEntity203Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity203Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity203Response(DashboardsSchemaEntity203Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity204Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 204")
    category: str = Field(default="Category_204", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=204 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity204Create(DashboardsSchemaEntity204Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity204Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity204Response(DashboardsSchemaEntity204Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity205Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 205")
    category: str = Field(default="Category_205", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=205 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity205Create(DashboardsSchemaEntity205Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity205Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity205Response(DashboardsSchemaEntity205Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity206Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 206")
    category: str = Field(default="Category_206", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=206 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity206Create(DashboardsSchemaEntity206Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity206Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity206Response(DashboardsSchemaEntity206Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity207Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 207")
    category: str = Field(default="Category_207", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=207 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity207Create(DashboardsSchemaEntity207Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity207Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity207Response(DashboardsSchemaEntity207Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity208Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 208")
    category: str = Field(default="Category_208", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=208 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity208Create(DashboardsSchemaEntity208Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity208Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity208Response(DashboardsSchemaEntity208Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity209Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 209")
    category: str = Field(default="Category_209", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=209 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity209Create(DashboardsSchemaEntity209Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity209Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity209Response(DashboardsSchemaEntity209Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity210Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 210")
    category: str = Field(default="Category_210", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=210 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity210Create(DashboardsSchemaEntity210Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity210Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity210Response(DashboardsSchemaEntity210Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity211Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 211")
    category: str = Field(default="Category_211", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=211 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity211Create(DashboardsSchemaEntity211Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity211Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity211Response(DashboardsSchemaEntity211Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity212Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 212")
    category: str = Field(default="Category_212", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=212 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity212Create(DashboardsSchemaEntity212Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity212Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity212Response(DashboardsSchemaEntity212Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity213Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 213")
    category: str = Field(default="Category_213", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=213 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity213Create(DashboardsSchemaEntity213Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity213Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity213Response(DashboardsSchemaEntity213Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity214Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 214")
    category: str = Field(default="Category_214", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=214 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity214Create(DashboardsSchemaEntity214Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity214Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity214Response(DashboardsSchemaEntity214Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity215Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 215")
    category: str = Field(default="Category_215", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=215 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity215Create(DashboardsSchemaEntity215Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity215Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity215Response(DashboardsSchemaEntity215Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity216Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 216")
    category: str = Field(default="Category_216", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=216 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity216Create(DashboardsSchemaEntity216Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity216Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity216Response(DashboardsSchemaEntity216Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity217Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 217")
    category: str = Field(default="Category_217", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=217 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity217Create(DashboardsSchemaEntity217Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity217Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity217Response(DashboardsSchemaEntity217Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity218Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 218")
    category: str = Field(default="Category_218", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=218 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity218Create(DashboardsSchemaEntity218Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity218Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity218Response(DashboardsSchemaEntity218Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity219Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 219")
    category: str = Field(default="Category_219", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=219 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity219Create(DashboardsSchemaEntity219Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity219Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity219Response(DashboardsSchemaEntity219Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity220Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 220")
    category: str = Field(default="Category_220", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=220 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity220Create(DashboardsSchemaEntity220Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity220Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity220Response(DashboardsSchemaEntity220Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity221Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 221")
    category: str = Field(default="Category_221", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=221 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity221Create(DashboardsSchemaEntity221Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity221Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity221Response(DashboardsSchemaEntity221Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity222Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 222")
    category: str = Field(default="Category_222", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=222 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity222Create(DashboardsSchemaEntity222Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity222Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity222Response(DashboardsSchemaEntity222Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity223Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 223")
    category: str = Field(default="Category_223", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=223 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity223Create(DashboardsSchemaEntity223Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity223Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity223Response(DashboardsSchemaEntity223Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity224Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 224")
    category: str = Field(default="Category_224", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=224 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity224Create(DashboardsSchemaEntity224Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity224Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity224Response(DashboardsSchemaEntity224Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity225Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 225")
    category: str = Field(default="Category_225", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=225 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity225Create(DashboardsSchemaEntity225Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity225Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity225Response(DashboardsSchemaEntity225Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity226Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 226")
    category: str = Field(default="Category_226", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=226 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity226Create(DashboardsSchemaEntity226Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity226Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity226Response(DashboardsSchemaEntity226Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity227Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 227")
    category: str = Field(default="Category_227", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=227 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity227Create(DashboardsSchemaEntity227Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity227Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity227Response(DashboardsSchemaEntity227Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity228Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 228")
    category: str = Field(default="Category_228", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=228 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity228Create(DashboardsSchemaEntity228Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity228Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity228Response(DashboardsSchemaEntity228Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity229Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 229")
    category: str = Field(default="Category_229", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=229 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity229Create(DashboardsSchemaEntity229Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity229Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity229Response(DashboardsSchemaEntity229Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity230Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 230")
    category: str = Field(default="Category_230", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=230 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity230Create(DashboardsSchemaEntity230Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity230Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity230Response(DashboardsSchemaEntity230Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity231Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 231")
    category: str = Field(default="Category_231", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=231 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity231Create(DashboardsSchemaEntity231Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity231Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity231Response(DashboardsSchemaEntity231Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity232Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 232")
    category: str = Field(default="Category_232", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=232 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity232Create(DashboardsSchemaEntity232Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity232Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity232Response(DashboardsSchemaEntity232Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity233Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 233")
    category: str = Field(default="Category_233", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=233 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity233Create(DashboardsSchemaEntity233Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity233Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity233Response(DashboardsSchemaEntity233Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity234Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 234")
    category: str = Field(default="Category_234", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=234 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity234Create(DashboardsSchemaEntity234Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity234Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity234Response(DashboardsSchemaEntity234Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity235Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 235")
    category: str = Field(default="Category_235", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=235 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity235Create(DashboardsSchemaEntity235Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity235Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity235Response(DashboardsSchemaEntity235Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity236Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 236")
    category: str = Field(default="Category_236", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=236 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity236Create(DashboardsSchemaEntity236Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity236Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity236Response(DashboardsSchemaEntity236Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity237Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 237")
    category: str = Field(default="Category_237", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=237 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity237Create(DashboardsSchemaEntity237Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity237Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity237Response(DashboardsSchemaEntity237Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity238Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 238")
    category: str = Field(default="Category_238", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=238 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity238Create(DashboardsSchemaEntity238Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity238Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity238Response(DashboardsSchemaEntity238Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity239Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 239")
    category: str = Field(default="Category_239", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=239 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity239Create(DashboardsSchemaEntity239Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity239Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity239Response(DashboardsSchemaEntity239Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity240Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 240")
    category: str = Field(default="Category_240", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=240 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity240Create(DashboardsSchemaEntity240Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity240Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity240Response(DashboardsSchemaEntity240Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity241Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 241")
    category: str = Field(default="Category_241", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=241 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity241Create(DashboardsSchemaEntity241Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity241Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity241Response(DashboardsSchemaEntity241Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity242Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 242")
    category: str = Field(default="Category_242", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=242 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity242Create(DashboardsSchemaEntity242Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity242Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity242Response(DashboardsSchemaEntity242Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity243Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 243")
    category: str = Field(default="Category_243", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=243 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity243Create(DashboardsSchemaEntity243Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity243Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity243Response(DashboardsSchemaEntity243Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity244Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 244")
    category: str = Field(default="Category_244", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=244 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity244Create(DashboardsSchemaEntity244Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity244Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity244Response(DashboardsSchemaEntity244Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity245Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 245")
    category: str = Field(default="Category_245", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=245 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity245Create(DashboardsSchemaEntity245Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity245Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity245Response(DashboardsSchemaEntity245Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity246Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 246")
    category: str = Field(default="Category_246", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=246 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity246Create(DashboardsSchemaEntity246Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity246Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity246Response(DashboardsSchemaEntity246Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity247Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 247")
    category: str = Field(default="Category_247", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=247 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity247Create(DashboardsSchemaEntity247Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity247Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity247Response(DashboardsSchemaEntity247Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity248Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 248")
    category: str = Field(default="Category_248", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=248 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity248Create(DashboardsSchemaEntity248Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity248Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity248Response(DashboardsSchemaEntity248Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity249Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 249")
    category: str = Field(default="Category_249", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=249 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity249Create(DashboardsSchemaEntity249Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity249Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity249Response(DashboardsSchemaEntity249Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DashboardsSchemaEntity250Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 250")
    category: str = Field(default="Category_250", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=250 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DashboardsSchemaEntity250Create(DashboardsSchemaEntity250Base):
    entity_code: str = Field(..., max_length=100)

class DashboardsSchemaEntity250Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class DashboardsSchemaEntity250Response(DashboardsSchemaEntity250Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

