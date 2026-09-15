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

class ExamsSchemaEntity51Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 51")
    category: str = Field(default="Category_51", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=51 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity51Create(ExamsSchemaEntity51Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity51Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity51Response(ExamsSchemaEntity51Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity52Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 52")
    category: str = Field(default="Category_52", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=52 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity52Create(ExamsSchemaEntity52Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity52Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity52Response(ExamsSchemaEntity52Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity53Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 53")
    category: str = Field(default="Category_53", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=53 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity53Create(ExamsSchemaEntity53Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity53Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity53Response(ExamsSchemaEntity53Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity54Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 54")
    category: str = Field(default="Category_54", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=54 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity54Create(ExamsSchemaEntity54Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity54Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity54Response(ExamsSchemaEntity54Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity55Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 55")
    category: str = Field(default="Category_55", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=55 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity55Create(ExamsSchemaEntity55Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity55Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity55Response(ExamsSchemaEntity55Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity56Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 56")
    category: str = Field(default="Category_56", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=56 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity56Create(ExamsSchemaEntity56Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity56Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity56Response(ExamsSchemaEntity56Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity57Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 57")
    category: str = Field(default="Category_57", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=57 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity57Create(ExamsSchemaEntity57Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity57Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity57Response(ExamsSchemaEntity57Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity58Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 58")
    category: str = Field(default="Category_58", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=58 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity58Create(ExamsSchemaEntity58Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity58Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity58Response(ExamsSchemaEntity58Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity59Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 59")
    category: str = Field(default="Category_59", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=59 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity59Create(ExamsSchemaEntity59Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity59Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity59Response(ExamsSchemaEntity59Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity60Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 60")
    category: str = Field(default="Category_60", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=60 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity60Create(ExamsSchemaEntity60Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity60Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity60Response(ExamsSchemaEntity60Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity61Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 61")
    category: str = Field(default="Category_61", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=61 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity61Create(ExamsSchemaEntity61Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity61Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity61Response(ExamsSchemaEntity61Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity62Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 62")
    category: str = Field(default="Category_62", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=62 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity62Create(ExamsSchemaEntity62Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity62Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity62Response(ExamsSchemaEntity62Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity63Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 63")
    category: str = Field(default="Category_63", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=63 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity63Create(ExamsSchemaEntity63Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity63Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity63Response(ExamsSchemaEntity63Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity64Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 64")
    category: str = Field(default="Category_64", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=64 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity64Create(ExamsSchemaEntity64Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity64Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity64Response(ExamsSchemaEntity64Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity65Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 65")
    category: str = Field(default="Category_65", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=65 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity65Create(ExamsSchemaEntity65Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity65Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity65Response(ExamsSchemaEntity65Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity66Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 66")
    category: str = Field(default="Category_66", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=66 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity66Create(ExamsSchemaEntity66Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity66Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity66Response(ExamsSchemaEntity66Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity67Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 67")
    category: str = Field(default="Category_67", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=67 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity67Create(ExamsSchemaEntity67Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity67Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity67Response(ExamsSchemaEntity67Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity68Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 68")
    category: str = Field(default="Category_68", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=68 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity68Create(ExamsSchemaEntity68Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity68Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity68Response(ExamsSchemaEntity68Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity69Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 69")
    category: str = Field(default="Category_69", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=69 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity69Create(ExamsSchemaEntity69Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity69Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity69Response(ExamsSchemaEntity69Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity70Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 70")
    category: str = Field(default="Category_70", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=70 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity70Create(ExamsSchemaEntity70Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity70Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity70Response(ExamsSchemaEntity70Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity71Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 71")
    category: str = Field(default="Category_71", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=71 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity71Create(ExamsSchemaEntity71Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity71Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity71Response(ExamsSchemaEntity71Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity72Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 72")
    category: str = Field(default="Category_72", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=72 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity72Create(ExamsSchemaEntity72Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity72Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity72Response(ExamsSchemaEntity72Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity73Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 73")
    category: str = Field(default="Category_73", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=73 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity73Create(ExamsSchemaEntity73Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity73Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity73Response(ExamsSchemaEntity73Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity74Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 74")
    category: str = Field(default="Category_74", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=74 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity74Create(ExamsSchemaEntity74Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity74Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity74Response(ExamsSchemaEntity74Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity75Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 75")
    category: str = Field(default="Category_75", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=75 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity75Create(ExamsSchemaEntity75Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity75Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity75Response(ExamsSchemaEntity75Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity76Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 76")
    category: str = Field(default="Category_76", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=76 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity76Create(ExamsSchemaEntity76Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity76Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity76Response(ExamsSchemaEntity76Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity77Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 77")
    category: str = Field(default="Category_77", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=77 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity77Create(ExamsSchemaEntity77Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity77Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity77Response(ExamsSchemaEntity77Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity78Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 78")
    category: str = Field(default="Category_78", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=78 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity78Create(ExamsSchemaEntity78Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity78Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity78Response(ExamsSchemaEntity78Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity79Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 79")
    category: str = Field(default="Category_79", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=79 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity79Create(ExamsSchemaEntity79Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity79Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity79Response(ExamsSchemaEntity79Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity80Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 80")
    category: str = Field(default="Category_80", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=80 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity80Create(ExamsSchemaEntity80Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity80Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity80Response(ExamsSchemaEntity80Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity81Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 81")
    category: str = Field(default="Category_81", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=81 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity81Create(ExamsSchemaEntity81Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity81Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity81Response(ExamsSchemaEntity81Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity82Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 82")
    category: str = Field(default="Category_82", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=82 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity82Create(ExamsSchemaEntity82Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity82Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity82Response(ExamsSchemaEntity82Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity83Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 83")
    category: str = Field(default="Category_83", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=83 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity83Create(ExamsSchemaEntity83Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity83Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity83Response(ExamsSchemaEntity83Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity84Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 84")
    category: str = Field(default="Category_84", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=84 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity84Create(ExamsSchemaEntity84Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity84Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity84Response(ExamsSchemaEntity84Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity85Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 85")
    category: str = Field(default="Category_85", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=85 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity85Create(ExamsSchemaEntity85Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity85Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity85Response(ExamsSchemaEntity85Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity86Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 86")
    category: str = Field(default="Category_86", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=86 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity86Create(ExamsSchemaEntity86Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity86Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity86Response(ExamsSchemaEntity86Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity87Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 87")
    category: str = Field(default="Category_87", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=87 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity87Create(ExamsSchemaEntity87Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity87Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity87Response(ExamsSchemaEntity87Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity88Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 88")
    category: str = Field(default="Category_88", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=88 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity88Create(ExamsSchemaEntity88Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity88Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity88Response(ExamsSchemaEntity88Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity89Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 89")
    category: str = Field(default="Category_89", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=89 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity89Create(ExamsSchemaEntity89Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity89Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity89Response(ExamsSchemaEntity89Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity90Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 90")
    category: str = Field(default="Category_90", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=90 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity90Create(ExamsSchemaEntity90Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity90Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity90Response(ExamsSchemaEntity90Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity91Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 91")
    category: str = Field(default="Category_91", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=91 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity91Create(ExamsSchemaEntity91Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity91Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity91Response(ExamsSchemaEntity91Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity92Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 92")
    category: str = Field(default="Category_92", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=92 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity92Create(ExamsSchemaEntity92Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity92Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity92Response(ExamsSchemaEntity92Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity93Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 93")
    category: str = Field(default="Category_93", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=93 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity93Create(ExamsSchemaEntity93Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity93Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity93Response(ExamsSchemaEntity93Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity94Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 94")
    category: str = Field(default="Category_94", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=94 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity94Create(ExamsSchemaEntity94Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity94Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity94Response(ExamsSchemaEntity94Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity95Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 95")
    category: str = Field(default="Category_95", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=95 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity95Create(ExamsSchemaEntity95Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity95Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity95Response(ExamsSchemaEntity95Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity96Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 96")
    category: str = Field(default="Category_96", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=96 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity96Create(ExamsSchemaEntity96Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity96Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity96Response(ExamsSchemaEntity96Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity97Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 97")
    category: str = Field(default="Category_97", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=97 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity97Create(ExamsSchemaEntity97Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity97Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity97Response(ExamsSchemaEntity97Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity98Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 98")
    category: str = Field(default="Category_98", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=98 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity98Create(ExamsSchemaEntity98Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity98Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity98Response(ExamsSchemaEntity98Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity99Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 99")
    category: str = Field(default="Category_99", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=99 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity99Create(ExamsSchemaEntity99Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity99Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity99Response(ExamsSchemaEntity99Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity100Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 100")
    category: str = Field(default="Category_100", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=100 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity100Create(ExamsSchemaEntity100Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity100Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity100Response(ExamsSchemaEntity100Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity101Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 101")
    category: str = Field(default="Category_101", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=101 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity101Create(ExamsSchemaEntity101Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity101Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity101Response(ExamsSchemaEntity101Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity102Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 102")
    category: str = Field(default="Category_102", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=102 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity102Create(ExamsSchemaEntity102Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity102Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity102Response(ExamsSchemaEntity102Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity103Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 103")
    category: str = Field(default="Category_103", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=103 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity103Create(ExamsSchemaEntity103Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity103Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity103Response(ExamsSchemaEntity103Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity104Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 104")
    category: str = Field(default="Category_104", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=104 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity104Create(ExamsSchemaEntity104Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity104Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity104Response(ExamsSchemaEntity104Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity105Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 105")
    category: str = Field(default="Category_105", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=105 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity105Create(ExamsSchemaEntity105Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity105Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity105Response(ExamsSchemaEntity105Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity106Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 106")
    category: str = Field(default="Category_106", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=106 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity106Create(ExamsSchemaEntity106Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity106Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity106Response(ExamsSchemaEntity106Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity107Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 107")
    category: str = Field(default="Category_107", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=107 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity107Create(ExamsSchemaEntity107Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity107Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity107Response(ExamsSchemaEntity107Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity108Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 108")
    category: str = Field(default="Category_108", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=108 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity108Create(ExamsSchemaEntity108Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity108Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity108Response(ExamsSchemaEntity108Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity109Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 109")
    category: str = Field(default="Category_109", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=109 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity109Create(ExamsSchemaEntity109Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity109Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity109Response(ExamsSchemaEntity109Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity110Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 110")
    category: str = Field(default="Category_110", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=110 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity110Create(ExamsSchemaEntity110Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity110Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity110Response(ExamsSchemaEntity110Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity111Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 111")
    category: str = Field(default="Category_111", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=111 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity111Create(ExamsSchemaEntity111Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity111Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity111Response(ExamsSchemaEntity111Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity112Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 112")
    category: str = Field(default="Category_112", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=112 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity112Create(ExamsSchemaEntity112Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity112Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity112Response(ExamsSchemaEntity112Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity113Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 113")
    category: str = Field(default="Category_113", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=113 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity113Create(ExamsSchemaEntity113Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity113Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity113Response(ExamsSchemaEntity113Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity114Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 114")
    category: str = Field(default="Category_114", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=114 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity114Create(ExamsSchemaEntity114Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity114Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity114Response(ExamsSchemaEntity114Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity115Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 115")
    category: str = Field(default="Category_115", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=115 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity115Create(ExamsSchemaEntity115Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity115Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity115Response(ExamsSchemaEntity115Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity116Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 116")
    category: str = Field(default="Category_116", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=116 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity116Create(ExamsSchemaEntity116Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity116Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity116Response(ExamsSchemaEntity116Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity117Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 117")
    category: str = Field(default="Category_117", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=117 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity117Create(ExamsSchemaEntity117Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity117Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity117Response(ExamsSchemaEntity117Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity118Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 118")
    category: str = Field(default="Category_118", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=118 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity118Create(ExamsSchemaEntity118Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity118Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity118Response(ExamsSchemaEntity118Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity119Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 119")
    category: str = Field(default="Category_119", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=119 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity119Create(ExamsSchemaEntity119Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity119Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity119Response(ExamsSchemaEntity119Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity120Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 120")
    category: str = Field(default="Category_120", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=120 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity120Create(ExamsSchemaEntity120Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity120Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity120Response(ExamsSchemaEntity120Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity121Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 121")
    category: str = Field(default="Category_121", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=121 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity121Create(ExamsSchemaEntity121Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity121Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity121Response(ExamsSchemaEntity121Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity122Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 122")
    category: str = Field(default="Category_122", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=122 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity122Create(ExamsSchemaEntity122Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity122Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity122Response(ExamsSchemaEntity122Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity123Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 123")
    category: str = Field(default="Category_123", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=123 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity123Create(ExamsSchemaEntity123Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity123Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity123Response(ExamsSchemaEntity123Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity124Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 124")
    category: str = Field(default="Category_124", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=124 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity124Create(ExamsSchemaEntity124Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity124Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity124Response(ExamsSchemaEntity124Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity125Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 125")
    category: str = Field(default="Category_125", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=125 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity125Create(ExamsSchemaEntity125Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity125Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity125Response(ExamsSchemaEntity125Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity126Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 126")
    category: str = Field(default="Category_126", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=126 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity126Create(ExamsSchemaEntity126Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity126Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity126Response(ExamsSchemaEntity126Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity127Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 127")
    category: str = Field(default="Category_127", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=127 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity127Create(ExamsSchemaEntity127Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity127Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity127Response(ExamsSchemaEntity127Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity128Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 128")
    category: str = Field(default="Category_128", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=128 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity128Create(ExamsSchemaEntity128Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity128Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity128Response(ExamsSchemaEntity128Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity129Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 129")
    category: str = Field(default="Category_129", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=129 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity129Create(ExamsSchemaEntity129Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity129Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity129Response(ExamsSchemaEntity129Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity130Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 130")
    category: str = Field(default="Category_130", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=130 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity130Create(ExamsSchemaEntity130Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity130Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity130Response(ExamsSchemaEntity130Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity131Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 131")
    category: str = Field(default="Category_131", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=131 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity131Create(ExamsSchemaEntity131Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity131Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity131Response(ExamsSchemaEntity131Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity132Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 132")
    category: str = Field(default="Category_132", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=132 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity132Create(ExamsSchemaEntity132Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity132Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity132Response(ExamsSchemaEntity132Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity133Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 133")
    category: str = Field(default="Category_133", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=133 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity133Create(ExamsSchemaEntity133Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity133Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity133Response(ExamsSchemaEntity133Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity134Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 134")
    category: str = Field(default="Category_134", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=134 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity134Create(ExamsSchemaEntity134Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity134Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity134Response(ExamsSchemaEntity134Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity135Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 135")
    category: str = Field(default="Category_135", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=135 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity135Create(ExamsSchemaEntity135Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity135Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity135Response(ExamsSchemaEntity135Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity136Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 136")
    category: str = Field(default="Category_136", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=136 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity136Create(ExamsSchemaEntity136Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity136Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity136Response(ExamsSchemaEntity136Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity137Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 137")
    category: str = Field(default="Category_137", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=137 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity137Create(ExamsSchemaEntity137Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity137Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity137Response(ExamsSchemaEntity137Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity138Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 138")
    category: str = Field(default="Category_138", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=138 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity138Create(ExamsSchemaEntity138Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity138Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity138Response(ExamsSchemaEntity138Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity139Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 139")
    category: str = Field(default="Category_139", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=139 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity139Create(ExamsSchemaEntity139Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity139Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity139Response(ExamsSchemaEntity139Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity140Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 140")
    category: str = Field(default="Category_140", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=140 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity140Create(ExamsSchemaEntity140Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity140Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity140Response(ExamsSchemaEntity140Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity141Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 141")
    category: str = Field(default="Category_141", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=141 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity141Create(ExamsSchemaEntity141Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity141Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity141Response(ExamsSchemaEntity141Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity142Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 142")
    category: str = Field(default="Category_142", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=142 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity142Create(ExamsSchemaEntity142Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity142Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity142Response(ExamsSchemaEntity142Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity143Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 143")
    category: str = Field(default="Category_143", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=143 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity143Create(ExamsSchemaEntity143Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity143Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity143Response(ExamsSchemaEntity143Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity144Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 144")
    category: str = Field(default="Category_144", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=144 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity144Create(ExamsSchemaEntity144Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity144Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity144Response(ExamsSchemaEntity144Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity145Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 145")
    category: str = Field(default="Category_145", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=145 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity145Create(ExamsSchemaEntity145Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity145Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity145Response(ExamsSchemaEntity145Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity146Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 146")
    category: str = Field(default="Category_146", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=146 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity146Create(ExamsSchemaEntity146Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity146Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity146Response(ExamsSchemaEntity146Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity147Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 147")
    category: str = Field(default="Category_147", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=147 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity147Create(ExamsSchemaEntity147Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity147Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity147Response(ExamsSchemaEntity147Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity148Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 148")
    category: str = Field(default="Category_148", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=148 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity148Create(ExamsSchemaEntity148Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity148Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity148Response(ExamsSchemaEntity148Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity149Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 149")
    category: str = Field(default="Category_149", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=149 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity149Create(ExamsSchemaEntity149Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity149Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity149Response(ExamsSchemaEntity149Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity150Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 150")
    category: str = Field(default="Category_150", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=150 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity150Create(ExamsSchemaEntity150Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity150Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity150Response(ExamsSchemaEntity150Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity151Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 151")
    category: str = Field(default="Category_151", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=151 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity151Create(ExamsSchemaEntity151Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity151Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity151Response(ExamsSchemaEntity151Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity152Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 152")
    category: str = Field(default="Category_152", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=152 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity152Create(ExamsSchemaEntity152Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity152Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity152Response(ExamsSchemaEntity152Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity153Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 153")
    category: str = Field(default="Category_153", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=153 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity153Create(ExamsSchemaEntity153Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity153Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity153Response(ExamsSchemaEntity153Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity154Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 154")
    category: str = Field(default="Category_154", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=154 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity154Create(ExamsSchemaEntity154Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity154Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity154Response(ExamsSchemaEntity154Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity155Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 155")
    category: str = Field(default="Category_155", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=155 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity155Create(ExamsSchemaEntity155Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity155Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity155Response(ExamsSchemaEntity155Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity156Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 156")
    category: str = Field(default="Category_156", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=156 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity156Create(ExamsSchemaEntity156Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity156Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity156Response(ExamsSchemaEntity156Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity157Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 157")
    category: str = Field(default="Category_157", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=157 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity157Create(ExamsSchemaEntity157Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity157Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity157Response(ExamsSchemaEntity157Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity158Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 158")
    category: str = Field(default="Category_158", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=158 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity158Create(ExamsSchemaEntity158Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity158Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity158Response(ExamsSchemaEntity158Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity159Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 159")
    category: str = Field(default="Category_159", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=159 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity159Create(ExamsSchemaEntity159Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity159Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity159Response(ExamsSchemaEntity159Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity160Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 160")
    category: str = Field(default="Category_160", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=160 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity160Create(ExamsSchemaEntity160Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity160Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity160Response(ExamsSchemaEntity160Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity161Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 161")
    category: str = Field(default="Category_161", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=161 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity161Create(ExamsSchemaEntity161Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity161Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity161Response(ExamsSchemaEntity161Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity162Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 162")
    category: str = Field(default="Category_162", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=162 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity162Create(ExamsSchemaEntity162Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity162Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity162Response(ExamsSchemaEntity162Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity163Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 163")
    category: str = Field(default="Category_163", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=163 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity163Create(ExamsSchemaEntity163Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity163Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity163Response(ExamsSchemaEntity163Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity164Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 164")
    category: str = Field(default="Category_164", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=164 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity164Create(ExamsSchemaEntity164Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity164Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity164Response(ExamsSchemaEntity164Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity165Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 165")
    category: str = Field(default="Category_165", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=165 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity165Create(ExamsSchemaEntity165Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity165Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity165Response(ExamsSchemaEntity165Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity166Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 166")
    category: str = Field(default="Category_166", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=166 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity166Create(ExamsSchemaEntity166Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity166Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity166Response(ExamsSchemaEntity166Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity167Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 167")
    category: str = Field(default="Category_167", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=167 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity167Create(ExamsSchemaEntity167Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity167Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity167Response(ExamsSchemaEntity167Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity168Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 168")
    category: str = Field(default="Category_168", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=168 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity168Create(ExamsSchemaEntity168Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity168Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity168Response(ExamsSchemaEntity168Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity169Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 169")
    category: str = Field(default="Category_169", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=169 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity169Create(ExamsSchemaEntity169Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity169Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity169Response(ExamsSchemaEntity169Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity170Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 170")
    category: str = Field(default="Category_170", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=170 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity170Create(ExamsSchemaEntity170Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity170Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity170Response(ExamsSchemaEntity170Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity171Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 171")
    category: str = Field(default="Category_171", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=171 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity171Create(ExamsSchemaEntity171Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity171Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity171Response(ExamsSchemaEntity171Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity172Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 172")
    category: str = Field(default="Category_172", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=172 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity172Create(ExamsSchemaEntity172Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity172Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity172Response(ExamsSchemaEntity172Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity173Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 173")
    category: str = Field(default="Category_173", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=173 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity173Create(ExamsSchemaEntity173Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity173Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity173Response(ExamsSchemaEntity173Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity174Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 174")
    category: str = Field(default="Category_174", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=174 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity174Create(ExamsSchemaEntity174Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity174Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity174Response(ExamsSchemaEntity174Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity175Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 175")
    category: str = Field(default="Category_175", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=175 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity175Create(ExamsSchemaEntity175Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity175Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity175Response(ExamsSchemaEntity175Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity176Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 176")
    category: str = Field(default="Category_176", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=176 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity176Create(ExamsSchemaEntity176Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity176Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity176Response(ExamsSchemaEntity176Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity177Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 177")
    category: str = Field(default="Category_177", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=177 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity177Create(ExamsSchemaEntity177Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity177Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity177Response(ExamsSchemaEntity177Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity178Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 178")
    category: str = Field(default="Category_178", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=178 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity178Create(ExamsSchemaEntity178Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity178Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity178Response(ExamsSchemaEntity178Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity179Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 179")
    category: str = Field(default="Category_179", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=179 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity179Create(ExamsSchemaEntity179Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity179Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity179Response(ExamsSchemaEntity179Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity180Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 180")
    category: str = Field(default="Category_180", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=180 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity180Create(ExamsSchemaEntity180Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity180Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity180Response(ExamsSchemaEntity180Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity181Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 181")
    category: str = Field(default="Category_181", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=181 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity181Create(ExamsSchemaEntity181Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity181Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity181Response(ExamsSchemaEntity181Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity182Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 182")
    category: str = Field(default="Category_182", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=182 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity182Create(ExamsSchemaEntity182Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity182Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity182Response(ExamsSchemaEntity182Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity183Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 183")
    category: str = Field(default="Category_183", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=183 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity183Create(ExamsSchemaEntity183Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity183Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity183Response(ExamsSchemaEntity183Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity184Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 184")
    category: str = Field(default="Category_184", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=184 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity184Create(ExamsSchemaEntity184Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity184Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity184Response(ExamsSchemaEntity184Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity185Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 185")
    category: str = Field(default="Category_185", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=185 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity185Create(ExamsSchemaEntity185Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity185Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity185Response(ExamsSchemaEntity185Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity186Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 186")
    category: str = Field(default="Category_186", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=186 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity186Create(ExamsSchemaEntity186Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity186Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity186Response(ExamsSchemaEntity186Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity187Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 187")
    category: str = Field(default="Category_187", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=187 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity187Create(ExamsSchemaEntity187Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity187Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity187Response(ExamsSchemaEntity187Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity188Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 188")
    category: str = Field(default="Category_188", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=188 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity188Create(ExamsSchemaEntity188Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity188Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity188Response(ExamsSchemaEntity188Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity189Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 189")
    category: str = Field(default="Category_189", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=189 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity189Create(ExamsSchemaEntity189Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity189Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity189Response(ExamsSchemaEntity189Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity190Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 190")
    category: str = Field(default="Category_190", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=190 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity190Create(ExamsSchemaEntity190Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity190Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity190Response(ExamsSchemaEntity190Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity191Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 191")
    category: str = Field(default="Category_191", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=191 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity191Create(ExamsSchemaEntity191Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity191Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity191Response(ExamsSchemaEntity191Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity192Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 192")
    category: str = Field(default="Category_192", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=192 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity192Create(ExamsSchemaEntity192Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity192Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity192Response(ExamsSchemaEntity192Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity193Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 193")
    category: str = Field(default="Category_193", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=193 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity193Create(ExamsSchemaEntity193Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity193Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity193Response(ExamsSchemaEntity193Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity194Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 194")
    category: str = Field(default="Category_194", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=194 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity194Create(ExamsSchemaEntity194Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity194Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity194Response(ExamsSchemaEntity194Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity195Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 195")
    category: str = Field(default="Category_195", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=195 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity195Create(ExamsSchemaEntity195Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity195Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity195Response(ExamsSchemaEntity195Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity196Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 196")
    category: str = Field(default="Category_196", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=196 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity196Create(ExamsSchemaEntity196Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity196Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity196Response(ExamsSchemaEntity196Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity197Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 197")
    category: str = Field(default="Category_197", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=197 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity197Create(ExamsSchemaEntity197Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity197Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity197Response(ExamsSchemaEntity197Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity198Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 198")
    category: str = Field(default="Category_198", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=198 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity198Create(ExamsSchemaEntity198Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity198Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity198Response(ExamsSchemaEntity198Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity199Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 199")
    category: str = Field(default="Category_199", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=199 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity199Create(ExamsSchemaEntity199Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity199Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity199Response(ExamsSchemaEntity199Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ExamsSchemaEntity200Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 200")
    category: str = Field(default="Category_200", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=200 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class ExamsSchemaEntity200Create(ExamsSchemaEntity200Base):
    entity_code: str = Field(..., max_length=100)

class ExamsSchemaEntity200Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class ExamsSchemaEntity200Response(ExamsSchemaEntity200Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

