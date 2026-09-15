"""
Examinations & Result Management - Pydantic Validation Schemas
Module: app.domains.exams.schemas
"""
from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class ExamsSchemaEntity1Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 1")
    category: str = Field(default="Category_1", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=1 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity1Create(ExamsSchemaEntity1Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity1Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity1Response(ExamsSchemaEntity1Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity2Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 2")
    category: str = Field(default="Category_2", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=2 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity2Create(ExamsSchemaEntity2Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity2Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity2Response(ExamsSchemaEntity2Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity3Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 3")
    category: str = Field(default="Category_3", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=3 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity3Create(ExamsSchemaEntity3Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity3Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity3Response(ExamsSchemaEntity3Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity4Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 4")
    category: str = Field(default="Category_4", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=4 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity4Create(ExamsSchemaEntity4Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity4Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity4Response(ExamsSchemaEntity4Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity5Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 5")
    category: str = Field(default="Category_5", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=5 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity5Create(ExamsSchemaEntity5Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity5Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity5Response(ExamsSchemaEntity5Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity6Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 6")
    category: str = Field(default="Category_6", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=6 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity6Create(ExamsSchemaEntity6Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity6Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity6Response(ExamsSchemaEntity6Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity7Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 7")
    category: str = Field(default="Category_7", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=7 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity7Create(ExamsSchemaEntity7Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity7Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity7Response(ExamsSchemaEntity7Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity8Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 8")
    category: str = Field(default="Category_8", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=8 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity8Create(ExamsSchemaEntity8Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity8Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity8Response(ExamsSchemaEntity8Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity9Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 9")
    category: str = Field(default="Category_9", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=9 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity9Create(ExamsSchemaEntity9Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity9Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity9Response(ExamsSchemaEntity9Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity10Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 10")
    category: str = Field(default="Category_10", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=10 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity10Create(ExamsSchemaEntity10Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity10Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity10Response(ExamsSchemaEntity10Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity11Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 11")
    category: str = Field(default="Category_11", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=11 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity11Create(ExamsSchemaEntity11Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity11Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity11Response(ExamsSchemaEntity11Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity12Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 12")
    category: str = Field(default="Category_12", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=12 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity12Create(ExamsSchemaEntity12Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity12Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity12Response(ExamsSchemaEntity12Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity13Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 13")
    category: str = Field(default="Category_13", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=13 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity13Create(ExamsSchemaEntity13Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity13Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity13Response(ExamsSchemaEntity13Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity14Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 14")
    category: str = Field(default="Category_14", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=14 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity14Create(ExamsSchemaEntity14Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity14Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity14Response(ExamsSchemaEntity14Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity15Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 15")
    category: str = Field(default="Category_15", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=15 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity15Create(ExamsSchemaEntity15Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity15Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity15Response(ExamsSchemaEntity15Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity16Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 16")
    category: str = Field(default="Category_16", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=16 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity16Create(ExamsSchemaEntity16Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity16Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity16Response(ExamsSchemaEntity16Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity17Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 17")
    category: str = Field(default="Category_17", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=17 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity17Create(ExamsSchemaEntity17Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity17Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity17Response(ExamsSchemaEntity17Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity18Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 18")
    category: str = Field(default="Category_18", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=18 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity18Create(ExamsSchemaEntity18Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity18Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity18Response(ExamsSchemaEntity18Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity19Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 19")
    category: str = Field(default="Category_19", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=19 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity19Create(ExamsSchemaEntity19Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity19Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity19Response(ExamsSchemaEntity19Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity20Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 20")
    category: str = Field(default="Category_20", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=20 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity20Create(ExamsSchemaEntity20Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity20Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity20Response(ExamsSchemaEntity20Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity21Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 21")
    category: str = Field(default="Category_21", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=21 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity21Create(ExamsSchemaEntity21Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity21Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity21Response(ExamsSchemaEntity21Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity22Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 22")
    category: str = Field(default="Category_22", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=22 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity22Create(ExamsSchemaEntity22Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity22Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity22Response(ExamsSchemaEntity22Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity23Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 23")
    category: str = Field(default="Category_23", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=23 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity23Create(ExamsSchemaEntity23Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity23Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity23Response(ExamsSchemaEntity23Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity24Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 24")
    category: str = Field(default="Category_24", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=24 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity24Create(ExamsSchemaEntity24Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity24Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity24Response(ExamsSchemaEntity24Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity25Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 25")
    category: str = Field(default="Category_25", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=25 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity25Create(ExamsSchemaEntity25Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity25Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity25Response(ExamsSchemaEntity25Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity26Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 26")
    category: str = Field(default="Category_26", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=26 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity26Create(ExamsSchemaEntity26Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity26Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity26Response(ExamsSchemaEntity26Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity27Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 27")
    category: str = Field(default="Category_27", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=27 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity27Create(ExamsSchemaEntity27Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity27Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity27Response(ExamsSchemaEntity27Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity28Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 28")
    category: str = Field(default="Category_28", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=28 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity28Create(ExamsSchemaEntity28Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity28Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity28Response(ExamsSchemaEntity28Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity29Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 29")
    category: str = Field(default="Category_29", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=29 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity29Create(ExamsSchemaEntity29Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity29Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity29Response(ExamsSchemaEntity29Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity30Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 30")
    category: str = Field(default="Category_30", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=30 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity30Create(ExamsSchemaEntity30Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity30Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity30Response(ExamsSchemaEntity30Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity31Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 31")
    category: str = Field(default="Category_31", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=31 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity31Create(ExamsSchemaEntity31Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity31Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity31Response(ExamsSchemaEntity31Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity32Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 32")
    category: str = Field(default="Category_32", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=32 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity32Create(ExamsSchemaEntity32Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity32Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity32Response(ExamsSchemaEntity32Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity33Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 33")
    category: str = Field(default="Category_33", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=33 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity33Create(ExamsSchemaEntity33Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity33Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity33Response(ExamsSchemaEntity33Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity34Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 34")
    category: str = Field(default="Category_34", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=34 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity34Create(ExamsSchemaEntity34Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity34Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity34Response(ExamsSchemaEntity34Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity35Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 35")
    category: str = Field(default="Category_35", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=35 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity35Create(ExamsSchemaEntity35Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity35Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity35Response(ExamsSchemaEntity35Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity36Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 36")
    category: str = Field(default="Category_36", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=36 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity36Create(ExamsSchemaEntity36Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity36Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity36Response(ExamsSchemaEntity36Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity37Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 37")
    category: str = Field(default="Category_37", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=37 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity37Create(ExamsSchemaEntity37Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity37Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity37Response(ExamsSchemaEntity37Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity38Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 38")
    category: str = Field(default="Category_38", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=38 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity38Create(ExamsSchemaEntity38Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity38Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity38Response(ExamsSchemaEntity38Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity39Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 39")
    category: str = Field(default="Category_39", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=39 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity39Create(ExamsSchemaEntity39Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity39Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity39Response(ExamsSchemaEntity39Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity40Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 40")
    category: str = Field(default="Category_40", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=40 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity40Create(ExamsSchemaEntity40Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity40Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity40Response(ExamsSchemaEntity40Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity41Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 41")
    category: str = Field(default="Category_41", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=41 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity41Create(ExamsSchemaEntity41Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity41Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity41Response(ExamsSchemaEntity41Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity42Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 42")
    category: str = Field(default="Category_42", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=42 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity42Create(ExamsSchemaEntity42Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity42Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity42Response(ExamsSchemaEntity42Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity43Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 43")
    category: str = Field(default="Category_43", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=43 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity43Create(ExamsSchemaEntity43Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity43Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity43Response(ExamsSchemaEntity43Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity44Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 44")
    category: str = Field(default="Category_44", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=44 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity44Create(ExamsSchemaEntity44Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity44Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity44Response(ExamsSchemaEntity44Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity45Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 45")
    category: str = Field(default="Category_45", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=45 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity45Create(ExamsSchemaEntity45Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity45Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity45Response(ExamsSchemaEntity45Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity46Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 46")
    category: str = Field(default="Category_46", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=46 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity46Create(ExamsSchemaEntity46Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity46Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity46Response(ExamsSchemaEntity46Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity47Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 47")
    category: str = Field(default="Category_47", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=47 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity47Create(ExamsSchemaEntity47Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity47Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity47Response(ExamsSchemaEntity47Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity48Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 48")
    category: str = Field(default="Category_48", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=48 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity48Create(ExamsSchemaEntity48Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity48Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity48Response(ExamsSchemaEntity48Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity49Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 49")
    category: str = Field(default="Category_49", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=49 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity49Create(ExamsSchemaEntity49Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity49Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity49Response(ExamsSchemaEntity49Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity50Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 50")
    category: str = Field(default="Category_50", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=50 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity50Create(ExamsSchemaEntity50Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity50Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity50Response(ExamsSchemaEntity50Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

