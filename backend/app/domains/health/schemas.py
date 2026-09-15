"""
Campus Health & Clinic Management - Pydantic Validation Schemas
Module: app.domains.health.schemas
"""
from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class HealthSchemaEntity1Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 1")
    category: str = Field(default="Category_1", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=1 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity1Create(HealthSchemaEntity1Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity1Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity1Response(HealthSchemaEntity1Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity2Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 2")
    category: str = Field(default="Category_2", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=2 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity2Create(HealthSchemaEntity2Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity2Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity2Response(HealthSchemaEntity2Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity3Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 3")
    category: str = Field(default="Category_3", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=3 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity3Create(HealthSchemaEntity3Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity3Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity3Response(HealthSchemaEntity3Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity4Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 4")
    category: str = Field(default="Category_4", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=4 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity4Create(HealthSchemaEntity4Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity4Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity4Response(HealthSchemaEntity4Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity5Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 5")
    category: str = Field(default="Category_5", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=5 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity5Create(HealthSchemaEntity5Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity5Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity5Response(HealthSchemaEntity5Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity6Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 6")
    category: str = Field(default="Category_6", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=6 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity6Create(HealthSchemaEntity6Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity6Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity6Response(HealthSchemaEntity6Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity7Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 7")
    category: str = Field(default="Category_7", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=7 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity7Create(HealthSchemaEntity7Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity7Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity7Response(HealthSchemaEntity7Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity8Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 8")
    category: str = Field(default="Category_8", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=8 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity8Create(HealthSchemaEntity8Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity8Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity8Response(HealthSchemaEntity8Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity9Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 9")
    category: str = Field(default="Category_9", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=9 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity9Create(HealthSchemaEntity9Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity9Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity9Response(HealthSchemaEntity9Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity10Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 10")
    category: str = Field(default="Category_10", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=10 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity10Create(HealthSchemaEntity10Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity10Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity10Response(HealthSchemaEntity10Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity11Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 11")
    category: str = Field(default="Category_11", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=11 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity11Create(HealthSchemaEntity11Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity11Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity11Response(HealthSchemaEntity11Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity12Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 12")
    category: str = Field(default="Category_12", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=12 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity12Create(HealthSchemaEntity12Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity12Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity12Response(HealthSchemaEntity12Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity13Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 13")
    category: str = Field(default="Category_13", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=13 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity13Create(HealthSchemaEntity13Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity13Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity13Response(HealthSchemaEntity13Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity14Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 14")
    category: str = Field(default="Category_14", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=14 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity14Create(HealthSchemaEntity14Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity14Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity14Response(HealthSchemaEntity14Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity15Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 15")
    category: str = Field(default="Category_15", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=15 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity15Create(HealthSchemaEntity15Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity15Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity15Response(HealthSchemaEntity15Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity16Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 16")
    category: str = Field(default="Category_16", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=16 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity16Create(HealthSchemaEntity16Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity16Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity16Response(HealthSchemaEntity16Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity17Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 17")
    category: str = Field(default="Category_17", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=17 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity17Create(HealthSchemaEntity17Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity17Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity17Response(HealthSchemaEntity17Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity18Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 18")
    category: str = Field(default="Category_18", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=18 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity18Create(HealthSchemaEntity18Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity18Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity18Response(HealthSchemaEntity18Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity19Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 19")
    category: str = Field(default="Category_19", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=19 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity19Create(HealthSchemaEntity19Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity19Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity19Response(HealthSchemaEntity19Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity20Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 20")
    category: str = Field(default="Category_20", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=20 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity20Create(HealthSchemaEntity20Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity20Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity20Response(HealthSchemaEntity20Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity21Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 21")
    category: str = Field(default="Category_21", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=21 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity21Create(HealthSchemaEntity21Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity21Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity21Response(HealthSchemaEntity21Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity22Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 22")
    category: str = Field(default="Category_22", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=22 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity22Create(HealthSchemaEntity22Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity22Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity22Response(HealthSchemaEntity22Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity23Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 23")
    category: str = Field(default="Category_23", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=23 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity23Create(HealthSchemaEntity23Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity23Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity23Response(HealthSchemaEntity23Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity24Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 24")
    category: str = Field(default="Category_24", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=24 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity24Create(HealthSchemaEntity24Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity24Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity24Response(HealthSchemaEntity24Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity25Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 25")
    category: str = Field(default="Category_25", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=25 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity25Create(HealthSchemaEntity25Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity25Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity25Response(HealthSchemaEntity25Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity26Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 26")
    category: str = Field(default="Category_26", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=26 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity26Create(HealthSchemaEntity26Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity26Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity26Response(HealthSchemaEntity26Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity27Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 27")
    category: str = Field(default="Category_27", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=27 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity27Create(HealthSchemaEntity27Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity27Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity27Response(HealthSchemaEntity27Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity28Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 28")
    category: str = Field(default="Category_28", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=28 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity28Create(HealthSchemaEntity28Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity28Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity28Response(HealthSchemaEntity28Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity29Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 29")
    category: str = Field(default="Category_29", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=29 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity29Create(HealthSchemaEntity29Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity29Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity29Response(HealthSchemaEntity29Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity30Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 30")
    category: str = Field(default="Category_30", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=30 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity30Create(HealthSchemaEntity30Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity30Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity30Response(HealthSchemaEntity30Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity31Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 31")
    category: str = Field(default="Category_31", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=31 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity31Create(HealthSchemaEntity31Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity31Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity31Response(HealthSchemaEntity31Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity32Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 32")
    category: str = Field(default="Category_32", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=32 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity32Create(HealthSchemaEntity32Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity32Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity32Response(HealthSchemaEntity32Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity33Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 33")
    category: str = Field(default="Category_33", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=33 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity33Create(HealthSchemaEntity33Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity33Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity33Response(HealthSchemaEntity33Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity34Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 34")
    category: str = Field(default="Category_34", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=34 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity34Create(HealthSchemaEntity34Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity34Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity34Response(HealthSchemaEntity34Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity35Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 35")
    category: str = Field(default="Category_35", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=35 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity35Create(HealthSchemaEntity35Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity35Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity35Response(HealthSchemaEntity35Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity36Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 36")
    category: str = Field(default="Category_36", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=36 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity36Create(HealthSchemaEntity36Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity36Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity36Response(HealthSchemaEntity36Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity37Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 37")
    category: str = Field(default="Category_37", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=37 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity37Create(HealthSchemaEntity37Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity37Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity37Response(HealthSchemaEntity37Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity38Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 38")
    category: str = Field(default="Category_38", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=38 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity38Create(HealthSchemaEntity38Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity38Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity38Response(HealthSchemaEntity38Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity39Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 39")
    category: str = Field(default="Category_39", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=39 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity39Create(HealthSchemaEntity39Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity39Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity39Response(HealthSchemaEntity39Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity40Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 40")
    category: str = Field(default="Category_40", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=40 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity40Create(HealthSchemaEntity40Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity40Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity40Response(HealthSchemaEntity40Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity41Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 41")
    category: str = Field(default="Category_41", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=41 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity41Create(HealthSchemaEntity41Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity41Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity41Response(HealthSchemaEntity41Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity42Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 42")
    category: str = Field(default="Category_42", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=42 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity42Create(HealthSchemaEntity42Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity42Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity42Response(HealthSchemaEntity42Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity43Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 43")
    category: str = Field(default="Category_43", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=43 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity43Create(HealthSchemaEntity43Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity43Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity43Response(HealthSchemaEntity43Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity44Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 44")
    category: str = Field(default="Category_44", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=44 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity44Create(HealthSchemaEntity44Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity44Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity44Response(HealthSchemaEntity44Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity45Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 45")
    category: str = Field(default="Category_45", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=45 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity45Create(HealthSchemaEntity45Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity45Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity45Response(HealthSchemaEntity45Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity46Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 46")
    category: str = Field(default="Category_46", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=46 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity46Create(HealthSchemaEntity46Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity46Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity46Response(HealthSchemaEntity46Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity47Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 47")
    category: str = Field(default="Category_47", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=47 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity47Create(HealthSchemaEntity47Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity47Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity47Response(HealthSchemaEntity47Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity48Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 48")
    category: str = Field(default="Category_48", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=48 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity48Create(HealthSchemaEntity48Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity48Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity48Response(HealthSchemaEntity48Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity49Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 49")
    category: str = Field(default="Category_49", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=49 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity49Create(HealthSchemaEntity49Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity49Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity49Response(HealthSchemaEntity49Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity50Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 50")
    category: str = Field(default="Category_50", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=50 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity50Create(HealthSchemaEntity50Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity50Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity50Response(HealthSchemaEntity50Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity51Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 51")
    category: str = Field(default="Category_51", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=51 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity51Create(HealthSchemaEntity51Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity51Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity51Response(HealthSchemaEntity51Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity52Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 52")
    category: str = Field(default="Category_52", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=52 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity52Create(HealthSchemaEntity52Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity52Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity52Response(HealthSchemaEntity52Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity53Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 53")
    category: str = Field(default="Category_53", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=53 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity53Create(HealthSchemaEntity53Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity53Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity53Response(HealthSchemaEntity53Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity54Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 54")
    category: str = Field(default="Category_54", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=54 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity54Create(HealthSchemaEntity54Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity54Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity54Response(HealthSchemaEntity54Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity55Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 55")
    category: str = Field(default="Category_55", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=55 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity55Create(HealthSchemaEntity55Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity55Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity55Response(HealthSchemaEntity55Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity56Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 56")
    category: str = Field(default="Category_56", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=56 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity56Create(HealthSchemaEntity56Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity56Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity56Response(HealthSchemaEntity56Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity57Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 57")
    category: str = Field(default="Category_57", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=57 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity57Create(HealthSchemaEntity57Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity57Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity57Response(HealthSchemaEntity57Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity58Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 58")
    category: str = Field(default="Category_58", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=58 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity58Create(HealthSchemaEntity58Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity58Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity58Response(HealthSchemaEntity58Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity59Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 59")
    category: str = Field(default="Category_59", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=59 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity59Create(HealthSchemaEntity59Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity59Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity59Response(HealthSchemaEntity59Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity60Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 60")
    category: str = Field(default="Category_60", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=60 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity60Create(HealthSchemaEntity60Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity60Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity60Response(HealthSchemaEntity60Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity61Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 61")
    category: str = Field(default="Category_61", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=61 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity61Create(HealthSchemaEntity61Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity61Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity61Response(HealthSchemaEntity61Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity62Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 62")
    category: str = Field(default="Category_62", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=62 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity62Create(HealthSchemaEntity62Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity62Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity62Response(HealthSchemaEntity62Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity63Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 63")
    category: str = Field(default="Category_63", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=63 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity63Create(HealthSchemaEntity63Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity63Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity63Response(HealthSchemaEntity63Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity64Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 64")
    category: str = Field(default="Category_64", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=64 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity64Create(HealthSchemaEntity64Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity64Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity64Response(HealthSchemaEntity64Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity65Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 65")
    category: str = Field(default="Category_65", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=65 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity65Create(HealthSchemaEntity65Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity65Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity65Response(HealthSchemaEntity65Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity66Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 66")
    category: str = Field(default="Category_66", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=66 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity66Create(HealthSchemaEntity66Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity66Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity66Response(HealthSchemaEntity66Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity67Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 67")
    category: str = Field(default="Category_67", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=67 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity67Create(HealthSchemaEntity67Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity67Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity67Response(HealthSchemaEntity67Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity68Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 68")
    category: str = Field(default="Category_68", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=68 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity68Create(HealthSchemaEntity68Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity68Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity68Response(HealthSchemaEntity68Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity69Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 69")
    category: str = Field(default="Category_69", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=69 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity69Create(HealthSchemaEntity69Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity69Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity69Response(HealthSchemaEntity69Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity70Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 70")
    category: str = Field(default="Category_70", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=70 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity70Create(HealthSchemaEntity70Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity70Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity70Response(HealthSchemaEntity70Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity71Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 71")
    category: str = Field(default="Category_71", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=71 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity71Create(HealthSchemaEntity71Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity71Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity71Response(HealthSchemaEntity71Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity72Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 72")
    category: str = Field(default="Category_72", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=72 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity72Create(HealthSchemaEntity72Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity72Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity72Response(HealthSchemaEntity72Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity73Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 73")
    category: str = Field(default="Category_73", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=73 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity73Create(HealthSchemaEntity73Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity73Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity73Response(HealthSchemaEntity73Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity74Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 74")
    category: str = Field(default="Category_74", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=74 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity74Create(HealthSchemaEntity74Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity74Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity74Response(HealthSchemaEntity74Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity75Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 75")
    category: str = Field(default="Category_75", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=75 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity75Create(HealthSchemaEntity75Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity75Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity75Response(HealthSchemaEntity75Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity76Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 76")
    category: str = Field(default="Category_76", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=76 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity76Create(HealthSchemaEntity76Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity76Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity76Response(HealthSchemaEntity76Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity77Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 77")
    category: str = Field(default="Category_77", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=77 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity77Create(HealthSchemaEntity77Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity77Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity77Response(HealthSchemaEntity77Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity78Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 78")
    category: str = Field(default="Category_78", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=78 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity78Create(HealthSchemaEntity78Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity78Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity78Response(HealthSchemaEntity78Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity79Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 79")
    category: str = Field(default="Category_79", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=79 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity79Create(HealthSchemaEntity79Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity79Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity79Response(HealthSchemaEntity79Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity80Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 80")
    category: str = Field(default="Category_80", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=80 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity80Create(HealthSchemaEntity80Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity80Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity80Response(HealthSchemaEntity80Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity81Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 81")
    category: str = Field(default="Category_81", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=81 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity81Create(HealthSchemaEntity81Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity81Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity81Response(HealthSchemaEntity81Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity82Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 82")
    category: str = Field(default="Category_82", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=82 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity82Create(HealthSchemaEntity82Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity82Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity82Response(HealthSchemaEntity82Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity83Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 83")
    category: str = Field(default="Category_83", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=83 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity83Create(HealthSchemaEntity83Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity83Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity83Response(HealthSchemaEntity83Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity84Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 84")
    category: str = Field(default="Category_84", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=84 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity84Create(HealthSchemaEntity84Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity84Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity84Response(HealthSchemaEntity84Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity85Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 85")
    category: str = Field(default="Category_85", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=85 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity85Create(HealthSchemaEntity85Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity85Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity85Response(HealthSchemaEntity85Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity86Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 86")
    category: str = Field(default="Category_86", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=86 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity86Create(HealthSchemaEntity86Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity86Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity86Response(HealthSchemaEntity86Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity87Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 87")
    category: str = Field(default="Category_87", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=87 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity87Create(HealthSchemaEntity87Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity87Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity87Response(HealthSchemaEntity87Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity88Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 88")
    category: str = Field(default="Category_88", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=88 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity88Create(HealthSchemaEntity88Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity88Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity88Response(HealthSchemaEntity88Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity89Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 89")
    category: str = Field(default="Category_89", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=89 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity89Create(HealthSchemaEntity89Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity89Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity89Response(HealthSchemaEntity89Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity90Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 90")
    category: str = Field(default="Category_90", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=90 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity90Create(HealthSchemaEntity90Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity90Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity90Response(HealthSchemaEntity90Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity91Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 91")
    category: str = Field(default="Category_91", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=91 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity91Create(HealthSchemaEntity91Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity91Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity91Response(HealthSchemaEntity91Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity92Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 92")
    category: str = Field(default="Category_92", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=92 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity92Create(HealthSchemaEntity92Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity92Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity92Response(HealthSchemaEntity92Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity93Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 93")
    category: str = Field(default="Category_93", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=93 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity93Create(HealthSchemaEntity93Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity93Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity93Response(HealthSchemaEntity93Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity94Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 94")
    category: str = Field(default="Category_94", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=94 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity94Create(HealthSchemaEntity94Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity94Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity94Response(HealthSchemaEntity94Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity95Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 95")
    category: str = Field(default="Category_95", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=95 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity95Create(HealthSchemaEntity95Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity95Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity95Response(HealthSchemaEntity95Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity96Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 96")
    category: str = Field(default="Category_96", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=96 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity96Create(HealthSchemaEntity96Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity96Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity96Response(HealthSchemaEntity96Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity97Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 97")
    category: str = Field(default="Category_97", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=97 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity97Create(HealthSchemaEntity97Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity97Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity97Response(HealthSchemaEntity97Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity98Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 98")
    category: str = Field(default="Category_98", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=98 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity98Create(HealthSchemaEntity98Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity98Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity98Response(HealthSchemaEntity98Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity99Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 99")
    category: str = Field(default="Category_99", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=99 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity99Create(HealthSchemaEntity99Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity99Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity99Response(HealthSchemaEntity99Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity100Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 100")
    category: str = Field(default="Category_100", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=100 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity100Create(HealthSchemaEntity100Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity100Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity100Response(HealthSchemaEntity100Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity101Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 101")
    category: str = Field(default="Category_101", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=101 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity101Create(HealthSchemaEntity101Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity101Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity101Response(HealthSchemaEntity101Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity102Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 102")
    category: str = Field(default="Category_102", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=102 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity102Create(HealthSchemaEntity102Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity102Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity102Response(HealthSchemaEntity102Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity103Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 103")
    category: str = Field(default="Category_103", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=103 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity103Create(HealthSchemaEntity103Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity103Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity103Response(HealthSchemaEntity103Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity104Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 104")
    category: str = Field(default="Category_104", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=104 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity104Create(HealthSchemaEntity104Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity104Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity104Response(HealthSchemaEntity104Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity105Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 105")
    category: str = Field(default="Category_105", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=105 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity105Create(HealthSchemaEntity105Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity105Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity105Response(HealthSchemaEntity105Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity106Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 106")
    category: str = Field(default="Category_106", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=106 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity106Create(HealthSchemaEntity106Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity106Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity106Response(HealthSchemaEntity106Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity107Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 107")
    category: str = Field(default="Category_107", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=107 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity107Create(HealthSchemaEntity107Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity107Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity107Response(HealthSchemaEntity107Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity108Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 108")
    category: str = Field(default="Category_108", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=108 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity108Create(HealthSchemaEntity108Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity108Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity108Response(HealthSchemaEntity108Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity109Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 109")
    category: str = Field(default="Category_109", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=109 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity109Create(HealthSchemaEntity109Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity109Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity109Response(HealthSchemaEntity109Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity110Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 110")
    category: str = Field(default="Category_110", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=110 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity110Create(HealthSchemaEntity110Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity110Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity110Response(HealthSchemaEntity110Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity111Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 111")
    category: str = Field(default="Category_111", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=111 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity111Create(HealthSchemaEntity111Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity111Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity111Response(HealthSchemaEntity111Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity112Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 112")
    category: str = Field(default="Category_112", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=112 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity112Create(HealthSchemaEntity112Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity112Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity112Response(HealthSchemaEntity112Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity113Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 113")
    category: str = Field(default="Category_113", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=113 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity113Create(HealthSchemaEntity113Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity113Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity113Response(HealthSchemaEntity113Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity114Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 114")
    category: str = Field(default="Category_114", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=114 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity114Create(HealthSchemaEntity114Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity114Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity114Response(HealthSchemaEntity114Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity115Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 115")
    category: str = Field(default="Category_115", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=115 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity115Create(HealthSchemaEntity115Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity115Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity115Response(HealthSchemaEntity115Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity116Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 116")
    category: str = Field(default="Category_116", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=116 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity116Create(HealthSchemaEntity116Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity116Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity116Response(HealthSchemaEntity116Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity117Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 117")
    category: str = Field(default="Category_117", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=117 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity117Create(HealthSchemaEntity117Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity117Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity117Response(HealthSchemaEntity117Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity118Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 118")
    category: str = Field(default="Category_118", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=118 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity118Create(HealthSchemaEntity118Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity118Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity118Response(HealthSchemaEntity118Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity119Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 119")
    category: str = Field(default="Category_119", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=119 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity119Create(HealthSchemaEntity119Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity119Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity119Response(HealthSchemaEntity119Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HealthSchemaEntity120Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 120")
    category: str = Field(default="Category_120", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=120 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HealthSchemaEntity120Create(HealthSchemaEntity120Base):
    entity_code: str = Field(..., max_length=100)

class HealthSchemaEntity120Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HealthSchemaEntity120Response(HealthSchemaEntity120Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

