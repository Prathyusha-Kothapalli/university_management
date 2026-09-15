"""
Human Resources & Faculty Management - Pydantic Validation Schemas
Module: app.domains.hr.schemas
"""
from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class HrSchemaEntity1Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 1")
    category: str = Field(default="Category_1", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=1 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity1Create(HrSchemaEntity1Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity1Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity1Response(HrSchemaEntity1Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity2Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 2")
    category: str = Field(default="Category_2", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=2 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity2Create(HrSchemaEntity2Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity2Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity2Response(HrSchemaEntity2Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity3Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 3")
    category: str = Field(default="Category_3", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=3 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity3Create(HrSchemaEntity3Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity3Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity3Response(HrSchemaEntity3Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity4Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 4")
    category: str = Field(default="Category_4", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=4 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity4Create(HrSchemaEntity4Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity4Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity4Response(HrSchemaEntity4Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity5Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 5")
    category: str = Field(default="Category_5", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=5 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity5Create(HrSchemaEntity5Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity5Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity5Response(HrSchemaEntity5Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity6Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 6")
    category: str = Field(default="Category_6", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=6 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity6Create(HrSchemaEntity6Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity6Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity6Response(HrSchemaEntity6Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity7Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 7")
    category: str = Field(default="Category_7", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=7 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity7Create(HrSchemaEntity7Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity7Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity7Response(HrSchemaEntity7Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity8Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 8")
    category: str = Field(default="Category_8", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=8 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity8Create(HrSchemaEntity8Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity8Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity8Response(HrSchemaEntity8Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity9Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 9")
    category: str = Field(default="Category_9", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=9 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity9Create(HrSchemaEntity9Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity9Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity9Response(HrSchemaEntity9Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity10Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 10")
    category: str = Field(default="Category_10", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=10 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity10Create(HrSchemaEntity10Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity10Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity10Response(HrSchemaEntity10Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity11Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 11")
    category: str = Field(default="Category_11", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=11 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity11Create(HrSchemaEntity11Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity11Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity11Response(HrSchemaEntity11Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity12Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 12")
    category: str = Field(default="Category_12", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=12 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity12Create(HrSchemaEntity12Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity12Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity12Response(HrSchemaEntity12Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity13Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 13")
    category: str = Field(default="Category_13", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=13 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity13Create(HrSchemaEntity13Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity13Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity13Response(HrSchemaEntity13Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity14Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 14")
    category: str = Field(default="Category_14", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=14 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity14Create(HrSchemaEntity14Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity14Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity14Response(HrSchemaEntity14Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity15Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 15")
    category: str = Field(default="Category_15", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=15 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity15Create(HrSchemaEntity15Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity15Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity15Response(HrSchemaEntity15Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity16Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 16")
    category: str = Field(default="Category_16", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=16 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity16Create(HrSchemaEntity16Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity16Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity16Response(HrSchemaEntity16Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity17Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 17")
    category: str = Field(default="Category_17", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=17 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity17Create(HrSchemaEntity17Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity17Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity17Response(HrSchemaEntity17Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity18Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 18")
    category: str = Field(default="Category_18", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=18 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity18Create(HrSchemaEntity18Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity18Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity18Response(HrSchemaEntity18Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity19Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 19")
    category: str = Field(default="Category_19", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=19 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity19Create(HrSchemaEntity19Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity19Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity19Response(HrSchemaEntity19Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity20Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 20")
    category: str = Field(default="Category_20", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=20 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity20Create(HrSchemaEntity20Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity20Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity20Response(HrSchemaEntity20Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity21Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 21")
    category: str = Field(default="Category_21", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=21 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity21Create(HrSchemaEntity21Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity21Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity21Response(HrSchemaEntity21Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity22Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 22")
    category: str = Field(default="Category_22", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=22 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity22Create(HrSchemaEntity22Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity22Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity22Response(HrSchemaEntity22Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity23Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 23")
    category: str = Field(default="Category_23", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=23 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity23Create(HrSchemaEntity23Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity23Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity23Response(HrSchemaEntity23Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity24Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 24")
    category: str = Field(default="Category_24", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=24 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity24Create(HrSchemaEntity24Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity24Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity24Response(HrSchemaEntity24Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity25Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 25")
    category: str = Field(default="Category_25", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=25 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity25Create(HrSchemaEntity25Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity25Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity25Response(HrSchemaEntity25Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity26Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 26")
    category: str = Field(default="Category_26", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=26 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity26Create(HrSchemaEntity26Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity26Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity26Response(HrSchemaEntity26Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity27Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 27")
    category: str = Field(default="Category_27", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=27 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity27Create(HrSchemaEntity27Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity27Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity27Response(HrSchemaEntity27Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity28Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 28")
    category: str = Field(default="Category_28", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=28 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity28Create(HrSchemaEntity28Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity28Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity28Response(HrSchemaEntity28Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity29Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 29")
    category: str = Field(default="Category_29", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=29 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity29Create(HrSchemaEntity29Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity29Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity29Response(HrSchemaEntity29Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity30Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 30")
    category: str = Field(default="Category_30", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=30 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity30Create(HrSchemaEntity30Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity30Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity30Response(HrSchemaEntity30Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity31Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 31")
    category: str = Field(default="Category_31", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=31 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity31Create(HrSchemaEntity31Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity31Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity31Response(HrSchemaEntity31Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity32Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 32")
    category: str = Field(default="Category_32", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=32 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity32Create(HrSchemaEntity32Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity32Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity32Response(HrSchemaEntity32Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity33Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 33")
    category: str = Field(default="Category_33", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=33 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity33Create(HrSchemaEntity33Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity33Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity33Response(HrSchemaEntity33Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity34Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 34")
    category: str = Field(default="Category_34", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=34 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity34Create(HrSchemaEntity34Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity34Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity34Response(HrSchemaEntity34Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity35Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 35")
    category: str = Field(default="Category_35", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=35 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity35Create(HrSchemaEntity35Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity35Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity35Response(HrSchemaEntity35Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity36Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 36")
    category: str = Field(default="Category_36", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=36 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity36Create(HrSchemaEntity36Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity36Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity36Response(HrSchemaEntity36Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity37Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 37")
    category: str = Field(default="Category_37", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=37 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity37Create(HrSchemaEntity37Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity37Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity37Response(HrSchemaEntity37Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity38Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 38")
    category: str = Field(default="Category_38", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=38 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity38Create(HrSchemaEntity38Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity38Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity38Response(HrSchemaEntity38Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity39Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 39")
    category: str = Field(default="Category_39", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=39 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity39Create(HrSchemaEntity39Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity39Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity39Response(HrSchemaEntity39Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity40Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 40")
    category: str = Field(default="Category_40", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=40 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity40Create(HrSchemaEntity40Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity40Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity40Response(HrSchemaEntity40Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity41Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 41")
    category: str = Field(default="Category_41", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=41 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity41Create(HrSchemaEntity41Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity41Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity41Response(HrSchemaEntity41Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity42Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 42")
    category: str = Field(default="Category_42", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=42 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity42Create(HrSchemaEntity42Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity42Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity42Response(HrSchemaEntity42Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity43Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 43")
    category: str = Field(default="Category_43", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=43 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity43Create(HrSchemaEntity43Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity43Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity43Response(HrSchemaEntity43Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity44Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 44")
    category: str = Field(default="Category_44", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=44 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity44Create(HrSchemaEntity44Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity44Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity44Response(HrSchemaEntity44Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity45Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 45")
    category: str = Field(default="Category_45", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=45 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity45Create(HrSchemaEntity45Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity45Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity45Response(HrSchemaEntity45Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity46Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 46")
    category: str = Field(default="Category_46", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=46 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity46Create(HrSchemaEntity46Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity46Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity46Response(HrSchemaEntity46Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity47Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 47")
    category: str = Field(default="Category_47", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=47 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity47Create(HrSchemaEntity47Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity47Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity47Response(HrSchemaEntity47Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity48Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 48")
    category: str = Field(default="Category_48", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=48 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity48Create(HrSchemaEntity48Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity48Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity48Response(HrSchemaEntity48Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity49Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 49")
    category: str = Field(default="Category_49", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=49 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity49Create(HrSchemaEntity49Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity49Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity49Response(HrSchemaEntity49Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity50Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 50")
    category: str = Field(default="Category_50", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=50 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity50Create(HrSchemaEntity50Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity50Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity50Response(HrSchemaEntity50Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity51Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 51")
    category: str = Field(default="Category_51", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=51 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity51Create(HrSchemaEntity51Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity51Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity51Response(HrSchemaEntity51Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity52Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 52")
    category: str = Field(default="Category_52", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=52 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity52Create(HrSchemaEntity52Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity52Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity52Response(HrSchemaEntity52Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity53Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 53")
    category: str = Field(default="Category_53", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=53 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity53Create(HrSchemaEntity53Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity53Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity53Response(HrSchemaEntity53Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity54Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 54")
    category: str = Field(default="Category_54", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=54 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity54Create(HrSchemaEntity54Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity54Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity54Response(HrSchemaEntity54Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity55Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 55")
    category: str = Field(default="Category_55", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=55 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity55Create(HrSchemaEntity55Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity55Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity55Response(HrSchemaEntity55Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity56Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 56")
    category: str = Field(default="Category_56", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=56 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity56Create(HrSchemaEntity56Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity56Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity56Response(HrSchemaEntity56Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity57Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 57")
    category: str = Field(default="Category_57", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=57 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity57Create(HrSchemaEntity57Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity57Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity57Response(HrSchemaEntity57Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity58Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 58")
    category: str = Field(default="Category_58", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=58 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity58Create(HrSchemaEntity58Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity58Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity58Response(HrSchemaEntity58Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity59Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 59")
    category: str = Field(default="Category_59", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=59 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity59Create(HrSchemaEntity59Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity59Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity59Response(HrSchemaEntity59Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity60Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 60")
    category: str = Field(default="Category_60", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=60 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity60Create(HrSchemaEntity60Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity60Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity60Response(HrSchemaEntity60Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity61Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 61")
    category: str = Field(default="Category_61", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=61 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity61Create(HrSchemaEntity61Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity61Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity61Response(HrSchemaEntity61Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity62Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 62")
    category: str = Field(default="Category_62", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=62 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity62Create(HrSchemaEntity62Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity62Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity62Response(HrSchemaEntity62Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity63Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 63")
    category: str = Field(default="Category_63", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=63 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity63Create(HrSchemaEntity63Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity63Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity63Response(HrSchemaEntity63Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity64Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 64")
    category: str = Field(default="Category_64", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=64 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity64Create(HrSchemaEntity64Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity64Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity64Response(HrSchemaEntity64Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity65Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 65")
    category: str = Field(default="Category_65", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=65 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity65Create(HrSchemaEntity65Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity65Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity65Response(HrSchemaEntity65Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity66Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 66")
    category: str = Field(default="Category_66", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=66 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity66Create(HrSchemaEntity66Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity66Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity66Response(HrSchemaEntity66Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity67Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 67")
    category: str = Field(default="Category_67", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=67 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity67Create(HrSchemaEntity67Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity67Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity67Response(HrSchemaEntity67Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity68Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 68")
    category: str = Field(default="Category_68", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=68 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity68Create(HrSchemaEntity68Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity68Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity68Response(HrSchemaEntity68Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity69Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 69")
    category: str = Field(default="Category_69", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=69 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity69Create(HrSchemaEntity69Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity69Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity69Response(HrSchemaEntity69Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity70Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 70")
    category: str = Field(default="Category_70", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=70 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity70Create(HrSchemaEntity70Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity70Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity70Response(HrSchemaEntity70Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity71Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 71")
    category: str = Field(default="Category_71", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=71 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity71Create(HrSchemaEntity71Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity71Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity71Response(HrSchemaEntity71Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity72Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 72")
    category: str = Field(default="Category_72", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=72 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity72Create(HrSchemaEntity72Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity72Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity72Response(HrSchemaEntity72Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity73Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 73")
    category: str = Field(default="Category_73", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=73 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity73Create(HrSchemaEntity73Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity73Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity73Response(HrSchemaEntity73Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity74Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 74")
    category: str = Field(default="Category_74", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=74 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity74Create(HrSchemaEntity74Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity74Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity74Response(HrSchemaEntity74Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity75Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 75")
    category: str = Field(default="Category_75", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=75 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity75Create(HrSchemaEntity75Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity75Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity75Response(HrSchemaEntity75Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity76Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 76")
    category: str = Field(default="Category_76", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=76 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity76Create(HrSchemaEntity76Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity76Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity76Response(HrSchemaEntity76Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity77Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 77")
    category: str = Field(default="Category_77", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=77 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity77Create(HrSchemaEntity77Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity77Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity77Response(HrSchemaEntity77Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity78Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 78")
    category: str = Field(default="Category_78", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=78 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity78Create(HrSchemaEntity78Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity78Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity78Response(HrSchemaEntity78Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity79Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 79")
    category: str = Field(default="Category_79", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=79 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity79Create(HrSchemaEntity79Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity79Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity79Response(HrSchemaEntity79Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity80Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 80")
    category: str = Field(default="Category_80", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=80 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity80Create(HrSchemaEntity80Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity80Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity80Response(HrSchemaEntity80Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity81Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 81")
    category: str = Field(default="Category_81", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=81 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity81Create(HrSchemaEntity81Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity81Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity81Response(HrSchemaEntity81Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity82Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 82")
    category: str = Field(default="Category_82", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=82 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity82Create(HrSchemaEntity82Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity82Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity82Response(HrSchemaEntity82Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity83Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 83")
    category: str = Field(default="Category_83", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=83 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity83Create(HrSchemaEntity83Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity83Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity83Response(HrSchemaEntity83Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity84Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 84")
    category: str = Field(default="Category_84", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=84 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity84Create(HrSchemaEntity84Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity84Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity84Response(HrSchemaEntity84Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity85Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 85")
    category: str = Field(default="Category_85", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=85 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity85Create(HrSchemaEntity85Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity85Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity85Response(HrSchemaEntity85Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity86Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 86")
    category: str = Field(default="Category_86", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=86 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity86Create(HrSchemaEntity86Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity86Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity86Response(HrSchemaEntity86Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity87Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 87")
    category: str = Field(default="Category_87", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=87 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity87Create(HrSchemaEntity87Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity87Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity87Response(HrSchemaEntity87Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity88Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 88")
    category: str = Field(default="Category_88", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=88 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity88Create(HrSchemaEntity88Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity88Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity88Response(HrSchemaEntity88Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity89Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 89")
    category: str = Field(default="Category_89", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=89 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity89Create(HrSchemaEntity89Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity89Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity89Response(HrSchemaEntity89Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity90Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 90")
    category: str = Field(default="Category_90", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=90 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity90Create(HrSchemaEntity90Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity90Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity90Response(HrSchemaEntity90Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity91Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 91")
    category: str = Field(default="Category_91", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=91 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity91Create(HrSchemaEntity91Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity91Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity91Response(HrSchemaEntity91Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity92Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 92")
    category: str = Field(default="Category_92", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=92 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity92Create(HrSchemaEntity92Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity92Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity92Response(HrSchemaEntity92Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity93Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 93")
    category: str = Field(default="Category_93", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=93 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity93Create(HrSchemaEntity93Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity93Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity93Response(HrSchemaEntity93Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity94Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 94")
    category: str = Field(default="Category_94", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=94 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity94Create(HrSchemaEntity94Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity94Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity94Response(HrSchemaEntity94Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity95Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 95")
    category: str = Field(default="Category_95", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=95 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity95Create(HrSchemaEntity95Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity95Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity95Response(HrSchemaEntity95Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity96Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 96")
    category: str = Field(default="Category_96", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=96 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity96Create(HrSchemaEntity96Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity96Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity96Response(HrSchemaEntity96Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity97Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 97")
    category: str = Field(default="Category_97", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=97 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity97Create(HrSchemaEntity97Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity97Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity97Response(HrSchemaEntity97Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity98Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 98")
    category: str = Field(default="Category_98", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=98 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity98Create(HrSchemaEntity98Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity98Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity98Response(HrSchemaEntity98Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity99Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 99")
    category: str = Field(default="Category_99", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=99 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity99Create(HrSchemaEntity99Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity99Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity99Response(HrSchemaEntity99Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity100Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 100")
    category: str = Field(default="Category_100", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=100 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity100Create(HrSchemaEntity100Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity100Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity100Response(HrSchemaEntity100Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity101Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 101")
    category: str = Field(default="Category_101", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=101 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity101Create(HrSchemaEntity101Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity101Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity101Response(HrSchemaEntity101Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity102Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 102")
    category: str = Field(default="Category_102", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=102 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity102Create(HrSchemaEntity102Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity102Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity102Response(HrSchemaEntity102Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity103Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 103")
    category: str = Field(default="Category_103", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=103 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity103Create(HrSchemaEntity103Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity103Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity103Response(HrSchemaEntity103Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity104Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 104")
    category: str = Field(default="Category_104", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=104 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity104Create(HrSchemaEntity104Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity104Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity104Response(HrSchemaEntity104Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity105Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 105")
    category: str = Field(default="Category_105", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=105 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity105Create(HrSchemaEntity105Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity105Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity105Response(HrSchemaEntity105Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity106Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 106")
    category: str = Field(default="Category_106", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=106 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity106Create(HrSchemaEntity106Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity106Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity106Response(HrSchemaEntity106Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity107Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 107")
    category: str = Field(default="Category_107", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=107 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity107Create(HrSchemaEntity107Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity107Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity107Response(HrSchemaEntity107Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity108Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 108")
    category: str = Field(default="Category_108", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=108 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity108Create(HrSchemaEntity108Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity108Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity108Response(HrSchemaEntity108Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity109Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 109")
    category: str = Field(default="Category_109", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=109 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity109Create(HrSchemaEntity109Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity109Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity109Response(HrSchemaEntity109Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity110Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 110")
    category: str = Field(default="Category_110", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=110 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity110Create(HrSchemaEntity110Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity110Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity110Response(HrSchemaEntity110Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity111Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 111")
    category: str = Field(default="Category_111", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=111 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity111Create(HrSchemaEntity111Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity111Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity111Response(HrSchemaEntity111Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity112Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 112")
    category: str = Field(default="Category_112", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=112 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity112Create(HrSchemaEntity112Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity112Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity112Response(HrSchemaEntity112Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity113Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 113")
    category: str = Field(default="Category_113", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=113 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity113Create(HrSchemaEntity113Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity113Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity113Response(HrSchemaEntity113Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity114Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 114")
    category: str = Field(default="Category_114", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=114 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity114Create(HrSchemaEntity114Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity114Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity114Response(HrSchemaEntity114Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity115Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 115")
    category: str = Field(default="Category_115", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=115 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity115Create(HrSchemaEntity115Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity115Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity115Response(HrSchemaEntity115Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity116Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 116")
    category: str = Field(default="Category_116", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=116 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity116Create(HrSchemaEntity116Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity116Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity116Response(HrSchemaEntity116Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity117Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 117")
    category: str = Field(default="Category_117", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=117 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity117Create(HrSchemaEntity117Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity117Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity117Response(HrSchemaEntity117Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity118Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 118")
    category: str = Field(default="Category_118", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=118 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity118Create(HrSchemaEntity118Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity118Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity118Response(HrSchemaEntity118Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity119Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 119")
    category: str = Field(default="Category_119", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=119 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity119Create(HrSchemaEntity119Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity119Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity119Response(HrSchemaEntity119Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity120Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 120")
    category: str = Field(default="Category_120", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=120 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity120Create(HrSchemaEntity120Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity120Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity120Response(HrSchemaEntity120Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity121Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 121")
    category: str = Field(default="Category_121", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=121 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity121Create(HrSchemaEntity121Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity121Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity121Response(HrSchemaEntity121Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity122Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 122")
    category: str = Field(default="Category_122", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=122 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity122Create(HrSchemaEntity122Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity122Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity122Response(HrSchemaEntity122Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity123Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 123")
    category: str = Field(default="Category_123", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=123 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity123Create(HrSchemaEntity123Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity123Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity123Response(HrSchemaEntity123Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity124Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 124")
    category: str = Field(default="Category_124", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=124 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity124Create(HrSchemaEntity124Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity124Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity124Response(HrSchemaEntity124Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity125Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 125")
    category: str = Field(default="Category_125", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=125 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity125Create(HrSchemaEntity125Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity125Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity125Response(HrSchemaEntity125Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity126Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 126")
    category: str = Field(default="Category_126", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=126 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity126Create(HrSchemaEntity126Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity126Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity126Response(HrSchemaEntity126Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity127Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 127")
    category: str = Field(default="Category_127", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=127 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity127Create(HrSchemaEntity127Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity127Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity127Response(HrSchemaEntity127Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity128Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 128")
    category: str = Field(default="Category_128", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=128 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity128Create(HrSchemaEntity128Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity128Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity128Response(HrSchemaEntity128Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity129Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 129")
    category: str = Field(default="Category_129", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=129 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity129Create(HrSchemaEntity129Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity129Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity129Response(HrSchemaEntity129Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity130Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 130")
    category: str = Field(default="Category_130", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=130 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity130Create(HrSchemaEntity130Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity130Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity130Response(HrSchemaEntity130Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity131Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 131")
    category: str = Field(default="Category_131", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=131 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity131Create(HrSchemaEntity131Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity131Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity131Response(HrSchemaEntity131Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity132Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 132")
    category: str = Field(default="Category_132", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=132 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity132Create(HrSchemaEntity132Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity132Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity132Response(HrSchemaEntity132Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity133Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 133")
    category: str = Field(default="Category_133", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=133 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity133Create(HrSchemaEntity133Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity133Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity133Response(HrSchemaEntity133Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity134Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 134")
    category: str = Field(default="Category_134", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=134 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity134Create(HrSchemaEntity134Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity134Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity134Response(HrSchemaEntity134Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity135Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 135")
    category: str = Field(default="Category_135", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=135 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity135Create(HrSchemaEntity135Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity135Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity135Response(HrSchemaEntity135Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity136Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 136")
    category: str = Field(default="Category_136", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=136 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity136Create(HrSchemaEntity136Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity136Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity136Response(HrSchemaEntity136Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity137Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 137")
    category: str = Field(default="Category_137", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=137 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity137Create(HrSchemaEntity137Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity137Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity137Response(HrSchemaEntity137Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity138Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 138")
    category: str = Field(default="Category_138", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=138 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity138Create(HrSchemaEntity138Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity138Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity138Response(HrSchemaEntity138Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity139Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 139")
    category: str = Field(default="Category_139", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=139 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity139Create(HrSchemaEntity139Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity139Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity139Response(HrSchemaEntity139Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity140Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 140")
    category: str = Field(default="Category_140", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=140 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity140Create(HrSchemaEntity140Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity140Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity140Response(HrSchemaEntity140Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity141Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 141")
    category: str = Field(default="Category_141", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=141 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity141Create(HrSchemaEntity141Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity141Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity141Response(HrSchemaEntity141Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity142Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 142")
    category: str = Field(default="Category_142", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=142 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity142Create(HrSchemaEntity142Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity142Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity142Response(HrSchemaEntity142Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity143Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 143")
    category: str = Field(default="Category_143", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=143 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity143Create(HrSchemaEntity143Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity143Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity143Response(HrSchemaEntity143Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity144Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 144")
    category: str = Field(default="Category_144", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=144 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity144Create(HrSchemaEntity144Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity144Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity144Response(HrSchemaEntity144Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity145Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 145")
    category: str = Field(default="Category_145", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=145 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity145Create(HrSchemaEntity145Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity145Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity145Response(HrSchemaEntity145Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity146Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 146")
    category: str = Field(default="Category_146", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=146 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity146Create(HrSchemaEntity146Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity146Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity146Response(HrSchemaEntity146Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity147Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 147")
    category: str = Field(default="Category_147", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=147 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity147Create(HrSchemaEntity147Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity147Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity147Response(HrSchemaEntity147Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity148Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 148")
    category: str = Field(default="Category_148", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=148 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity148Create(HrSchemaEntity148Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity148Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity148Response(HrSchemaEntity148Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity149Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 149")
    category: str = Field(default="Category_149", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=149 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity149Create(HrSchemaEntity149Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity149Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity149Response(HrSchemaEntity149Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity150Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 150")
    category: str = Field(default="Category_150", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=150 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity150Create(HrSchemaEntity150Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity150Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity150Response(HrSchemaEntity150Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity151Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 151")
    category: str = Field(default="Category_151", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=151 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity151Create(HrSchemaEntity151Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity151Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity151Response(HrSchemaEntity151Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity152Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 152")
    category: str = Field(default="Category_152", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=152 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity152Create(HrSchemaEntity152Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity152Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity152Response(HrSchemaEntity152Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity153Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 153")
    category: str = Field(default="Category_153", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=153 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity153Create(HrSchemaEntity153Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity153Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity153Response(HrSchemaEntity153Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity154Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 154")
    category: str = Field(default="Category_154", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=154 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity154Create(HrSchemaEntity154Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity154Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity154Response(HrSchemaEntity154Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity155Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 155")
    category: str = Field(default="Category_155", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=155 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity155Create(HrSchemaEntity155Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity155Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity155Response(HrSchemaEntity155Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity156Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 156")
    category: str = Field(default="Category_156", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=156 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity156Create(HrSchemaEntity156Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity156Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity156Response(HrSchemaEntity156Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity157Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 157")
    category: str = Field(default="Category_157", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=157 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity157Create(HrSchemaEntity157Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity157Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity157Response(HrSchemaEntity157Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity158Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 158")
    category: str = Field(default="Category_158", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=158 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity158Create(HrSchemaEntity158Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity158Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity158Response(HrSchemaEntity158Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity159Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 159")
    category: str = Field(default="Category_159", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=159 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity159Create(HrSchemaEntity159Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity159Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity159Response(HrSchemaEntity159Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity160Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 160")
    category: str = Field(default="Category_160", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=160 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity160Create(HrSchemaEntity160Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity160Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity160Response(HrSchemaEntity160Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity161Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 161")
    category: str = Field(default="Category_161", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=161 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity161Create(HrSchemaEntity161Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity161Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity161Response(HrSchemaEntity161Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity162Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 162")
    category: str = Field(default="Category_162", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=162 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity162Create(HrSchemaEntity162Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity162Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity162Response(HrSchemaEntity162Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity163Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 163")
    category: str = Field(default="Category_163", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=163 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity163Create(HrSchemaEntity163Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity163Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity163Response(HrSchemaEntity163Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity164Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 164")
    category: str = Field(default="Category_164", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=164 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity164Create(HrSchemaEntity164Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity164Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity164Response(HrSchemaEntity164Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity165Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 165")
    category: str = Field(default="Category_165", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=165 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity165Create(HrSchemaEntity165Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity165Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity165Response(HrSchemaEntity165Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity166Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 166")
    category: str = Field(default="Category_166", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=166 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity166Create(HrSchemaEntity166Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity166Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity166Response(HrSchemaEntity166Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity167Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 167")
    category: str = Field(default="Category_167", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=167 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity167Create(HrSchemaEntity167Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity167Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity167Response(HrSchemaEntity167Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity168Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 168")
    category: str = Field(default="Category_168", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=168 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity168Create(HrSchemaEntity168Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity168Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity168Response(HrSchemaEntity168Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity169Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 169")
    category: str = Field(default="Category_169", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=169 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity169Create(HrSchemaEntity169Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity169Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity169Response(HrSchemaEntity169Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity170Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 170")
    category: str = Field(default="Category_170", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=170 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity170Create(HrSchemaEntity170Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity170Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity170Response(HrSchemaEntity170Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity171Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 171")
    category: str = Field(default="Category_171", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=171 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity171Create(HrSchemaEntity171Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity171Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity171Response(HrSchemaEntity171Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity172Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 172")
    category: str = Field(default="Category_172", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=172 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity172Create(HrSchemaEntity172Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity172Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity172Response(HrSchemaEntity172Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity173Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 173")
    category: str = Field(default="Category_173", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=173 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity173Create(HrSchemaEntity173Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity173Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity173Response(HrSchemaEntity173Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity174Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 174")
    category: str = Field(default="Category_174", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=174 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity174Create(HrSchemaEntity174Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity174Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity174Response(HrSchemaEntity174Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity175Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 175")
    category: str = Field(default="Category_175", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=175 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity175Create(HrSchemaEntity175Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity175Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity175Response(HrSchemaEntity175Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity176Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 176")
    category: str = Field(default="Category_176", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=176 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity176Create(HrSchemaEntity176Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity176Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity176Response(HrSchemaEntity176Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity177Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 177")
    category: str = Field(default="Category_177", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=177 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity177Create(HrSchemaEntity177Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity177Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity177Response(HrSchemaEntity177Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity178Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 178")
    category: str = Field(default="Category_178", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=178 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity178Create(HrSchemaEntity178Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity178Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity178Response(HrSchemaEntity178Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity179Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 179")
    category: str = Field(default="Category_179", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=179 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity179Create(HrSchemaEntity179Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity179Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity179Response(HrSchemaEntity179Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity180Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 180")
    category: str = Field(default="Category_180", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=180 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity180Create(HrSchemaEntity180Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity180Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity180Response(HrSchemaEntity180Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity181Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 181")
    category: str = Field(default="Category_181", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=181 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity181Create(HrSchemaEntity181Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity181Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity181Response(HrSchemaEntity181Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity182Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 182")
    category: str = Field(default="Category_182", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=182 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity182Create(HrSchemaEntity182Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity182Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity182Response(HrSchemaEntity182Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity183Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 183")
    category: str = Field(default="Category_183", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=183 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity183Create(HrSchemaEntity183Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity183Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity183Response(HrSchemaEntity183Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity184Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 184")
    category: str = Field(default="Category_184", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=184 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity184Create(HrSchemaEntity184Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity184Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity184Response(HrSchemaEntity184Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity185Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 185")
    category: str = Field(default="Category_185", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=185 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity185Create(HrSchemaEntity185Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity185Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity185Response(HrSchemaEntity185Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity186Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 186")
    category: str = Field(default="Category_186", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=186 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity186Create(HrSchemaEntity186Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity186Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity186Response(HrSchemaEntity186Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity187Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 187")
    category: str = Field(default="Category_187", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=187 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity187Create(HrSchemaEntity187Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity187Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity187Response(HrSchemaEntity187Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity188Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 188")
    category: str = Field(default="Category_188", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=188 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity188Create(HrSchemaEntity188Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity188Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity188Response(HrSchemaEntity188Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity189Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 189")
    category: str = Field(default="Category_189", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=189 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity189Create(HrSchemaEntity189Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity189Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity189Response(HrSchemaEntity189Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity190Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 190")
    category: str = Field(default="Category_190", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=190 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity190Create(HrSchemaEntity190Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity190Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity190Response(HrSchemaEntity190Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity191Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 191")
    category: str = Field(default="Category_191", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=191 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity191Create(HrSchemaEntity191Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity191Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity191Response(HrSchemaEntity191Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity192Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 192")
    category: str = Field(default="Category_192", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=192 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity192Create(HrSchemaEntity192Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity192Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity192Response(HrSchemaEntity192Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity193Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 193")
    category: str = Field(default="Category_193", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=193 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity193Create(HrSchemaEntity193Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity193Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity193Response(HrSchemaEntity193Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity194Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 194")
    category: str = Field(default="Category_194", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=194 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity194Create(HrSchemaEntity194Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity194Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity194Response(HrSchemaEntity194Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity195Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 195")
    category: str = Field(default="Category_195", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=195 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity195Create(HrSchemaEntity195Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity195Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity195Response(HrSchemaEntity195Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity196Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 196")
    category: str = Field(default="Category_196", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=196 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity196Create(HrSchemaEntity196Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity196Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity196Response(HrSchemaEntity196Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity197Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 197")
    category: str = Field(default="Category_197", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=197 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity197Create(HrSchemaEntity197Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity197Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity197Response(HrSchemaEntity197Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity198Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 198")
    category: str = Field(default="Category_198", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=198 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity198Create(HrSchemaEntity198Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity198Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity198Response(HrSchemaEntity198Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity199Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 199")
    category: str = Field(default="Category_199", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=199 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity199Create(HrSchemaEntity199Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity199Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity199Response(HrSchemaEntity199Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class HrSchemaEntity200Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 200")
    category: str = Field(default="Category_200", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=200 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HrSchemaEntity200Create(HrSchemaEntity200Base):
    entity_code: str = Field(..., max_length=100)

class HrSchemaEntity200Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class HrSchemaEntity200Response(HrSchemaEntity200Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

