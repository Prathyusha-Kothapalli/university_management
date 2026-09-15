"""
Library & Digital Repositories - Pydantic Validation Schemas
Module: app.domains.library.schemas
"""
from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class LibrarySchemaEntity1Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 1")
    category: str = Field(default="Category_1", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=1 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity1Create(LibrarySchemaEntity1Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity1Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity1Response(LibrarySchemaEntity1Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity2Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 2")
    category: str = Field(default="Category_2", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=2 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity2Create(LibrarySchemaEntity2Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity2Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity2Response(LibrarySchemaEntity2Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity3Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 3")
    category: str = Field(default="Category_3", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=3 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity3Create(LibrarySchemaEntity3Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity3Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity3Response(LibrarySchemaEntity3Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity4Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 4")
    category: str = Field(default="Category_4", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=4 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity4Create(LibrarySchemaEntity4Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity4Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity4Response(LibrarySchemaEntity4Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity5Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 5")
    category: str = Field(default="Category_5", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=5 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity5Create(LibrarySchemaEntity5Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity5Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity5Response(LibrarySchemaEntity5Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity6Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 6")
    category: str = Field(default="Category_6", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=6 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity6Create(LibrarySchemaEntity6Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity6Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity6Response(LibrarySchemaEntity6Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity7Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 7")
    category: str = Field(default="Category_7", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=7 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity7Create(LibrarySchemaEntity7Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity7Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity7Response(LibrarySchemaEntity7Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity8Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 8")
    category: str = Field(default="Category_8", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=8 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity8Create(LibrarySchemaEntity8Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity8Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity8Response(LibrarySchemaEntity8Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity9Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 9")
    category: str = Field(default="Category_9", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=9 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity9Create(LibrarySchemaEntity9Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity9Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity9Response(LibrarySchemaEntity9Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity10Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 10")
    category: str = Field(default="Category_10", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=10 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity10Create(LibrarySchemaEntity10Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity10Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity10Response(LibrarySchemaEntity10Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity11Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 11")
    category: str = Field(default="Category_11", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=11 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity11Create(LibrarySchemaEntity11Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity11Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity11Response(LibrarySchemaEntity11Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity12Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 12")
    category: str = Field(default="Category_12", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=12 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity12Create(LibrarySchemaEntity12Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity12Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity12Response(LibrarySchemaEntity12Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity13Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 13")
    category: str = Field(default="Category_13", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=13 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity13Create(LibrarySchemaEntity13Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity13Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity13Response(LibrarySchemaEntity13Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity14Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 14")
    category: str = Field(default="Category_14", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=14 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity14Create(LibrarySchemaEntity14Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity14Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity14Response(LibrarySchemaEntity14Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity15Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 15")
    category: str = Field(default="Category_15", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=15 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity15Create(LibrarySchemaEntity15Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity15Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity15Response(LibrarySchemaEntity15Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity16Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 16")
    category: str = Field(default="Category_16", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=16 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity16Create(LibrarySchemaEntity16Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity16Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity16Response(LibrarySchemaEntity16Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity17Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 17")
    category: str = Field(default="Category_17", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=17 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity17Create(LibrarySchemaEntity17Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity17Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity17Response(LibrarySchemaEntity17Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity18Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 18")
    category: str = Field(default="Category_18", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=18 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity18Create(LibrarySchemaEntity18Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity18Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity18Response(LibrarySchemaEntity18Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity19Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 19")
    category: str = Field(default="Category_19", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=19 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity19Create(LibrarySchemaEntity19Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity19Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity19Response(LibrarySchemaEntity19Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity20Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 20")
    category: str = Field(default="Category_20", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=20 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity20Create(LibrarySchemaEntity20Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity20Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity20Response(LibrarySchemaEntity20Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity21Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 21")
    category: str = Field(default="Category_21", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=21 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity21Create(LibrarySchemaEntity21Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity21Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity21Response(LibrarySchemaEntity21Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity22Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 22")
    category: str = Field(default="Category_22", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=22 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity22Create(LibrarySchemaEntity22Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity22Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity22Response(LibrarySchemaEntity22Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity23Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 23")
    category: str = Field(default="Category_23", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=23 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity23Create(LibrarySchemaEntity23Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity23Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity23Response(LibrarySchemaEntity23Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity24Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 24")
    category: str = Field(default="Category_24", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=24 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity24Create(LibrarySchemaEntity24Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity24Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity24Response(LibrarySchemaEntity24Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity25Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 25")
    category: str = Field(default="Category_25", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=25 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity25Create(LibrarySchemaEntity25Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity25Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity25Response(LibrarySchemaEntity25Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity26Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 26")
    category: str = Field(default="Category_26", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=26 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity26Create(LibrarySchemaEntity26Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity26Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity26Response(LibrarySchemaEntity26Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity27Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 27")
    category: str = Field(default="Category_27", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=27 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity27Create(LibrarySchemaEntity27Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity27Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity27Response(LibrarySchemaEntity27Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity28Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 28")
    category: str = Field(default="Category_28", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=28 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity28Create(LibrarySchemaEntity28Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity28Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity28Response(LibrarySchemaEntity28Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity29Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 29")
    category: str = Field(default="Category_29", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=29 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity29Create(LibrarySchemaEntity29Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity29Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity29Response(LibrarySchemaEntity29Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity30Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 30")
    category: str = Field(default="Category_30", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=30 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity30Create(LibrarySchemaEntity30Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity30Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity30Response(LibrarySchemaEntity30Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity31Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 31")
    category: str = Field(default="Category_31", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=31 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity31Create(LibrarySchemaEntity31Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity31Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity31Response(LibrarySchemaEntity31Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity32Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 32")
    category: str = Field(default="Category_32", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=32 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity32Create(LibrarySchemaEntity32Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity32Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity32Response(LibrarySchemaEntity32Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity33Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 33")
    category: str = Field(default="Category_33", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=33 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity33Create(LibrarySchemaEntity33Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity33Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity33Response(LibrarySchemaEntity33Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity34Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 34")
    category: str = Field(default="Category_34", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=34 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity34Create(LibrarySchemaEntity34Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity34Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity34Response(LibrarySchemaEntity34Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity35Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 35")
    category: str = Field(default="Category_35", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=35 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity35Create(LibrarySchemaEntity35Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity35Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity35Response(LibrarySchemaEntity35Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity36Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 36")
    category: str = Field(default="Category_36", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=36 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity36Create(LibrarySchemaEntity36Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity36Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity36Response(LibrarySchemaEntity36Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity37Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 37")
    category: str = Field(default="Category_37", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=37 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity37Create(LibrarySchemaEntity37Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity37Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity37Response(LibrarySchemaEntity37Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity38Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 38")
    category: str = Field(default="Category_38", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=38 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity38Create(LibrarySchemaEntity38Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity38Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity38Response(LibrarySchemaEntity38Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity39Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 39")
    category: str = Field(default="Category_39", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=39 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity39Create(LibrarySchemaEntity39Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity39Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity39Response(LibrarySchemaEntity39Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity40Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 40")
    category: str = Field(default="Category_40", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=40 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity40Create(LibrarySchemaEntity40Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity40Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity40Response(LibrarySchemaEntity40Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity41Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 41")
    category: str = Field(default="Category_41", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=41 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity41Create(LibrarySchemaEntity41Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity41Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity41Response(LibrarySchemaEntity41Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity42Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 42")
    category: str = Field(default="Category_42", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=42 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity42Create(LibrarySchemaEntity42Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity42Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity42Response(LibrarySchemaEntity42Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity43Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 43")
    category: str = Field(default="Category_43", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=43 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity43Create(LibrarySchemaEntity43Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity43Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity43Response(LibrarySchemaEntity43Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity44Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 44")
    category: str = Field(default="Category_44", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=44 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity44Create(LibrarySchemaEntity44Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity44Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity44Response(LibrarySchemaEntity44Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity45Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 45")
    category: str = Field(default="Category_45", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=45 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity45Create(LibrarySchemaEntity45Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity45Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity45Response(LibrarySchemaEntity45Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity46Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 46")
    category: str = Field(default="Category_46", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=46 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity46Create(LibrarySchemaEntity46Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity46Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity46Response(LibrarySchemaEntity46Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity47Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 47")
    category: str = Field(default="Category_47", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=47 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity47Create(LibrarySchemaEntity47Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity47Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity47Response(LibrarySchemaEntity47Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity48Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 48")
    category: str = Field(default="Category_48", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=48 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity48Create(LibrarySchemaEntity48Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity48Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity48Response(LibrarySchemaEntity48Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity49Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 49")
    category: str = Field(default="Category_49", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=49 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity49Create(LibrarySchemaEntity49Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity49Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity49Response(LibrarySchemaEntity49Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity50Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 50")
    category: str = Field(default="Category_50", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=50 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity50Create(LibrarySchemaEntity50Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity50Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity50Response(LibrarySchemaEntity50Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity51Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 51")
    category: str = Field(default="Category_51", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=51 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity51Create(LibrarySchemaEntity51Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity51Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity51Response(LibrarySchemaEntity51Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity52Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 52")
    category: str = Field(default="Category_52", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=52 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity52Create(LibrarySchemaEntity52Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity52Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity52Response(LibrarySchemaEntity52Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity53Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 53")
    category: str = Field(default="Category_53", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=53 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity53Create(LibrarySchemaEntity53Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity53Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity53Response(LibrarySchemaEntity53Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity54Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 54")
    category: str = Field(default="Category_54", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=54 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity54Create(LibrarySchemaEntity54Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity54Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity54Response(LibrarySchemaEntity54Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity55Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 55")
    category: str = Field(default="Category_55", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=55 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity55Create(LibrarySchemaEntity55Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity55Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity55Response(LibrarySchemaEntity55Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity56Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 56")
    category: str = Field(default="Category_56", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=56 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity56Create(LibrarySchemaEntity56Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity56Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity56Response(LibrarySchemaEntity56Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity57Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 57")
    category: str = Field(default="Category_57", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=57 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity57Create(LibrarySchemaEntity57Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity57Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity57Response(LibrarySchemaEntity57Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity58Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 58")
    category: str = Field(default="Category_58", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=58 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity58Create(LibrarySchemaEntity58Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity58Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity58Response(LibrarySchemaEntity58Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity59Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 59")
    category: str = Field(default="Category_59", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=59 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity59Create(LibrarySchemaEntity59Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity59Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity59Response(LibrarySchemaEntity59Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity60Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 60")
    category: str = Field(default="Category_60", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=60 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity60Create(LibrarySchemaEntity60Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity60Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity60Response(LibrarySchemaEntity60Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity61Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 61")
    category: str = Field(default="Category_61", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=61 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity61Create(LibrarySchemaEntity61Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity61Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity61Response(LibrarySchemaEntity61Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity62Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 62")
    category: str = Field(default="Category_62", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=62 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity62Create(LibrarySchemaEntity62Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity62Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity62Response(LibrarySchemaEntity62Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity63Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 63")
    category: str = Field(default="Category_63", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=63 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity63Create(LibrarySchemaEntity63Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity63Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity63Response(LibrarySchemaEntity63Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity64Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 64")
    category: str = Field(default="Category_64", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=64 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity64Create(LibrarySchemaEntity64Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity64Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity64Response(LibrarySchemaEntity64Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity65Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 65")
    category: str = Field(default="Category_65", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=65 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity65Create(LibrarySchemaEntity65Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity65Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity65Response(LibrarySchemaEntity65Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity66Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 66")
    category: str = Field(default="Category_66", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=66 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity66Create(LibrarySchemaEntity66Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity66Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity66Response(LibrarySchemaEntity66Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity67Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 67")
    category: str = Field(default="Category_67", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=67 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity67Create(LibrarySchemaEntity67Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity67Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity67Response(LibrarySchemaEntity67Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity68Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 68")
    category: str = Field(default="Category_68", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=68 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity68Create(LibrarySchemaEntity68Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity68Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity68Response(LibrarySchemaEntity68Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity69Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 69")
    category: str = Field(default="Category_69", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=69 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity69Create(LibrarySchemaEntity69Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity69Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity69Response(LibrarySchemaEntity69Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity70Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 70")
    category: str = Field(default="Category_70", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=70 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity70Create(LibrarySchemaEntity70Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity70Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity70Response(LibrarySchemaEntity70Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity71Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 71")
    category: str = Field(default="Category_71", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=71 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity71Create(LibrarySchemaEntity71Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity71Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity71Response(LibrarySchemaEntity71Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity72Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 72")
    category: str = Field(default="Category_72", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=72 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity72Create(LibrarySchemaEntity72Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity72Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity72Response(LibrarySchemaEntity72Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity73Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 73")
    category: str = Field(default="Category_73", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=73 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity73Create(LibrarySchemaEntity73Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity73Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity73Response(LibrarySchemaEntity73Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity74Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 74")
    category: str = Field(default="Category_74", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=74 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity74Create(LibrarySchemaEntity74Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity74Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity74Response(LibrarySchemaEntity74Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity75Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 75")
    category: str = Field(default="Category_75", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=75 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity75Create(LibrarySchemaEntity75Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity75Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity75Response(LibrarySchemaEntity75Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity76Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 76")
    category: str = Field(default="Category_76", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=76 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity76Create(LibrarySchemaEntity76Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity76Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity76Response(LibrarySchemaEntity76Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity77Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 77")
    category: str = Field(default="Category_77", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=77 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity77Create(LibrarySchemaEntity77Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity77Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity77Response(LibrarySchemaEntity77Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity78Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 78")
    category: str = Field(default="Category_78", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=78 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity78Create(LibrarySchemaEntity78Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity78Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity78Response(LibrarySchemaEntity78Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity79Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 79")
    category: str = Field(default="Category_79", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=79 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity79Create(LibrarySchemaEntity79Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity79Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity79Response(LibrarySchemaEntity79Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity80Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 80")
    category: str = Field(default="Category_80", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=80 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity80Create(LibrarySchemaEntity80Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity80Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity80Response(LibrarySchemaEntity80Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity81Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 81")
    category: str = Field(default="Category_81", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=81 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity81Create(LibrarySchemaEntity81Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity81Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity81Response(LibrarySchemaEntity81Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity82Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 82")
    category: str = Field(default="Category_82", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=82 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity82Create(LibrarySchemaEntity82Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity82Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity82Response(LibrarySchemaEntity82Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity83Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 83")
    category: str = Field(default="Category_83", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=83 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity83Create(LibrarySchemaEntity83Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity83Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity83Response(LibrarySchemaEntity83Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity84Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 84")
    category: str = Field(default="Category_84", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=84 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity84Create(LibrarySchemaEntity84Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity84Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity84Response(LibrarySchemaEntity84Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity85Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 85")
    category: str = Field(default="Category_85", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=85 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity85Create(LibrarySchemaEntity85Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity85Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity85Response(LibrarySchemaEntity85Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity86Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 86")
    category: str = Field(default="Category_86", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=86 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity86Create(LibrarySchemaEntity86Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity86Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity86Response(LibrarySchemaEntity86Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity87Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 87")
    category: str = Field(default="Category_87", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=87 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity87Create(LibrarySchemaEntity87Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity87Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity87Response(LibrarySchemaEntity87Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity88Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 88")
    category: str = Field(default="Category_88", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=88 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity88Create(LibrarySchemaEntity88Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity88Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity88Response(LibrarySchemaEntity88Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity89Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 89")
    category: str = Field(default="Category_89", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=89 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity89Create(LibrarySchemaEntity89Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity89Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity89Response(LibrarySchemaEntity89Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity90Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 90")
    category: str = Field(default="Category_90", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=90 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity90Create(LibrarySchemaEntity90Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity90Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity90Response(LibrarySchemaEntity90Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity91Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 91")
    category: str = Field(default="Category_91", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=91 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity91Create(LibrarySchemaEntity91Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity91Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity91Response(LibrarySchemaEntity91Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity92Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 92")
    category: str = Field(default="Category_92", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=92 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity92Create(LibrarySchemaEntity92Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity92Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity92Response(LibrarySchemaEntity92Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity93Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 93")
    category: str = Field(default="Category_93", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=93 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity93Create(LibrarySchemaEntity93Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity93Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity93Response(LibrarySchemaEntity93Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity94Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 94")
    category: str = Field(default="Category_94", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=94 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity94Create(LibrarySchemaEntity94Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity94Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity94Response(LibrarySchemaEntity94Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity95Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 95")
    category: str = Field(default="Category_95", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=95 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity95Create(LibrarySchemaEntity95Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity95Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity95Response(LibrarySchemaEntity95Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity96Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 96")
    category: str = Field(default="Category_96", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=96 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity96Create(LibrarySchemaEntity96Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity96Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity96Response(LibrarySchemaEntity96Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity97Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 97")
    category: str = Field(default="Category_97", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=97 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity97Create(LibrarySchemaEntity97Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity97Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity97Response(LibrarySchemaEntity97Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity98Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 98")
    category: str = Field(default="Category_98", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=98 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity98Create(LibrarySchemaEntity98Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity98Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity98Response(LibrarySchemaEntity98Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity99Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 99")
    category: str = Field(default="Category_99", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=99 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity99Create(LibrarySchemaEntity99Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity99Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity99Response(LibrarySchemaEntity99Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity100Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 100")
    category: str = Field(default="Category_100", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=100 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity100Create(LibrarySchemaEntity100Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity100Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity100Response(LibrarySchemaEntity100Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity101Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 101")
    category: str = Field(default="Category_101", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=101 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity101Create(LibrarySchemaEntity101Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity101Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity101Response(LibrarySchemaEntity101Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity102Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 102")
    category: str = Field(default="Category_102", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=102 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity102Create(LibrarySchemaEntity102Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity102Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity102Response(LibrarySchemaEntity102Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity103Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 103")
    category: str = Field(default="Category_103", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=103 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity103Create(LibrarySchemaEntity103Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity103Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity103Response(LibrarySchemaEntity103Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity104Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 104")
    category: str = Field(default="Category_104", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=104 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity104Create(LibrarySchemaEntity104Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity104Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity104Response(LibrarySchemaEntity104Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity105Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 105")
    category: str = Field(default="Category_105", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=105 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity105Create(LibrarySchemaEntity105Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity105Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity105Response(LibrarySchemaEntity105Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity106Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 106")
    category: str = Field(default="Category_106", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=106 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity106Create(LibrarySchemaEntity106Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity106Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity106Response(LibrarySchemaEntity106Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity107Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 107")
    category: str = Field(default="Category_107", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=107 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity107Create(LibrarySchemaEntity107Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity107Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity107Response(LibrarySchemaEntity107Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity108Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 108")
    category: str = Field(default="Category_108", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=108 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity108Create(LibrarySchemaEntity108Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity108Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity108Response(LibrarySchemaEntity108Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity109Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 109")
    category: str = Field(default="Category_109", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=109 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity109Create(LibrarySchemaEntity109Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity109Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity109Response(LibrarySchemaEntity109Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity110Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 110")
    category: str = Field(default="Category_110", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=110 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity110Create(LibrarySchemaEntity110Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity110Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity110Response(LibrarySchemaEntity110Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity111Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 111")
    category: str = Field(default="Category_111", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=111 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity111Create(LibrarySchemaEntity111Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity111Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity111Response(LibrarySchemaEntity111Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity112Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 112")
    category: str = Field(default="Category_112", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=112 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity112Create(LibrarySchemaEntity112Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity112Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity112Response(LibrarySchemaEntity112Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity113Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 113")
    category: str = Field(default="Category_113", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=113 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity113Create(LibrarySchemaEntity113Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity113Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity113Response(LibrarySchemaEntity113Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity114Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 114")
    category: str = Field(default="Category_114", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=114 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity114Create(LibrarySchemaEntity114Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity114Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity114Response(LibrarySchemaEntity114Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity115Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 115")
    category: str = Field(default="Category_115", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=115 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity115Create(LibrarySchemaEntity115Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity115Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity115Response(LibrarySchemaEntity115Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity116Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 116")
    category: str = Field(default="Category_116", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=116 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity116Create(LibrarySchemaEntity116Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity116Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity116Response(LibrarySchemaEntity116Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity117Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 117")
    category: str = Field(default="Category_117", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=117 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity117Create(LibrarySchemaEntity117Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity117Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity117Response(LibrarySchemaEntity117Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity118Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 118")
    category: str = Field(default="Category_118", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=118 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity118Create(LibrarySchemaEntity118Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity118Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity118Response(LibrarySchemaEntity118Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity119Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 119")
    category: str = Field(default="Category_119", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=119 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity119Create(LibrarySchemaEntity119Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity119Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity119Response(LibrarySchemaEntity119Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity120Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 120")
    category: str = Field(default="Category_120", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=120 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity120Create(LibrarySchemaEntity120Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity120Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity120Response(LibrarySchemaEntity120Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity121Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 121")
    category: str = Field(default="Category_121", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=121 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity121Create(LibrarySchemaEntity121Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity121Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity121Response(LibrarySchemaEntity121Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity122Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 122")
    category: str = Field(default="Category_122", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=122 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity122Create(LibrarySchemaEntity122Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity122Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity122Response(LibrarySchemaEntity122Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity123Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 123")
    category: str = Field(default="Category_123", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=123 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity123Create(LibrarySchemaEntity123Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity123Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity123Response(LibrarySchemaEntity123Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity124Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 124")
    category: str = Field(default="Category_124", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=124 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity124Create(LibrarySchemaEntity124Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity124Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity124Response(LibrarySchemaEntity124Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity125Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 125")
    category: str = Field(default="Category_125", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=125 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity125Create(LibrarySchemaEntity125Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity125Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity125Response(LibrarySchemaEntity125Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity126Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 126")
    category: str = Field(default="Category_126", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=126 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity126Create(LibrarySchemaEntity126Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity126Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity126Response(LibrarySchemaEntity126Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity127Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 127")
    category: str = Field(default="Category_127", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=127 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity127Create(LibrarySchemaEntity127Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity127Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity127Response(LibrarySchemaEntity127Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity128Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 128")
    category: str = Field(default="Category_128", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=128 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity128Create(LibrarySchemaEntity128Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity128Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity128Response(LibrarySchemaEntity128Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity129Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 129")
    category: str = Field(default="Category_129", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=129 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity129Create(LibrarySchemaEntity129Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity129Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity129Response(LibrarySchemaEntity129Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity130Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 130")
    category: str = Field(default="Category_130", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=130 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity130Create(LibrarySchemaEntity130Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity130Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity130Response(LibrarySchemaEntity130Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity131Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 131")
    category: str = Field(default="Category_131", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=131 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity131Create(LibrarySchemaEntity131Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity131Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity131Response(LibrarySchemaEntity131Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity132Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 132")
    category: str = Field(default="Category_132", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=132 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity132Create(LibrarySchemaEntity132Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity132Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity132Response(LibrarySchemaEntity132Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity133Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 133")
    category: str = Field(default="Category_133", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=133 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity133Create(LibrarySchemaEntity133Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity133Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity133Response(LibrarySchemaEntity133Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity134Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 134")
    category: str = Field(default="Category_134", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=134 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity134Create(LibrarySchemaEntity134Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity134Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity134Response(LibrarySchemaEntity134Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity135Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 135")
    category: str = Field(default="Category_135", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=135 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity135Create(LibrarySchemaEntity135Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity135Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity135Response(LibrarySchemaEntity135Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity136Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 136")
    category: str = Field(default="Category_136", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=136 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity136Create(LibrarySchemaEntity136Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity136Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity136Response(LibrarySchemaEntity136Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity137Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 137")
    category: str = Field(default="Category_137", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=137 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity137Create(LibrarySchemaEntity137Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity137Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity137Response(LibrarySchemaEntity137Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity138Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 138")
    category: str = Field(default="Category_138", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=138 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity138Create(LibrarySchemaEntity138Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity138Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity138Response(LibrarySchemaEntity138Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity139Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 139")
    category: str = Field(default="Category_139", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=139 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity139Create(LibrarySchemaEntity139Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity139Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity139Response(LibrarySchemaEntity139Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity140Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 140")
    category: str = Field(default="Category_140", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=140 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity140Create(LibrarySchemaEntity140Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity140Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity140Response(LibrarySchemaEntity140Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity141Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 141")
    category: str = Field(default="Category_141", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=141 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity141Create(LibrarySchemaEntity141Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity141Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity141Response(LibrarySchemaEntity141Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity142Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 142")
    category: str = Field(default="Category_142", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=142 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity142Create(LibrarySchemaEntity142Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity142Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity142Response(LibrarySchemaEntity142Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity143Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 143")
    category: str = Field(default="Category_143", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=143 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity143Create(LibrarySchemaEntity143Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity143Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity143Response(LibrarySchemaEntity143Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity144Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 144")
    category: str = Field(default="Category_144", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=144 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity144Create(LibrarySchemaEntity144Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity144Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity144Response(LibrarySchemaEntity144Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity145Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 145")
    category: str = Field(default="Category_145", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=145 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity145Create(LibrarySchemaEntity145Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity145Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity145Response(LibrarySchemaEntity145Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity146Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 146")
    category: str = Field(default="Category_146", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=146 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity146Create(LibrarySchemaEntity146Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity146Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity146Response(LibrarySchemaEntity146Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity147Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 147")
    category: str = Field(default="Category_147", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=147 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity147Create(LibrarySchemaEntity147Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity147Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity147Response(LibrarySchemaEntity147Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity148Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 148")
    category: str = Field(default="Category_148", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=148 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity148Create(LibrarySchemaEntity148Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity148Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity148Response(LibrarySchemaEntity148Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity149Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 149")
    category: str = Field(default="Category_149", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=149 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity149Create(LibrarySchemaEntity149Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity149Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity149Response(LibrarySchemaEntity149Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity150Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 150")
    category: str = Field(default="Category_150", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=150 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity150Create(LibrarySchemaEntity150Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity150Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity150Response(LibrarySchemaEntity150Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity151Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 151")
    category: str = Field(default="Category_151", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=151 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity151Create(LibrarySchemaEntity151Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity151Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity151Response(LibrarySchemaEntity151Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity152Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 152")
    category: str = Field(default="Category_152", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=152 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity152Create(LibrarySchemaEntity152Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity152Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity152Response(LibrarySchemaEntity152Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity153Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 153")
    category: str = Field(default="Category_153", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=153 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity153Create(LibrarySchemaEntity153Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity153Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity153Response(LibrarySchemaEntity153Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity154Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 154")
    category: str = Field(default="Category_154", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=154 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity154Create(LibrarySchemaEntity154Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity154Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity154Response(LibrarySchemaEntity154Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity155Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 155")
    category: str = Field(default="Category_155", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=155 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity155Create(LibrarySchemaEntity155Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity155Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity155Response(LibrarySchemaEntity155Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity156Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 156")
    category: str = Field(default="Category_156", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=156 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity156Create(LibrarySchemaEntity156Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity156Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity156Response(LibrarySchemaEntity156Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity157Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 157")
    category: str = Field(default="Category_157", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=157 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity157Create(LibrarySchemaEntity157Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity157Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity157Response(LibrarySchemaEntity157Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity158Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 158")
    category: str = Field(default="Category_158", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=158 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity158Create(LibrarySchemaEntity158Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity158Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity158Response(LibrarySchemaEntity158Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity159Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 159")
    category: str = Field(default="Category_159", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=159 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity159Create(LibrarySchemaEntity159Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity159Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity159Response(LibrarySchemaEntity159Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity160Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 160")
    category: str = Field(default="Category_160", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=160 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity160Create(LibrarySchemaEntity160Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity160Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity160Response(LibrarySchemaEntity160Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity161Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 161")
    category: str = Field(default="Category_161", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=161 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity161Create(LibrarySchemaEntity161Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity161Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity161Response(LibrarySchemaEntity161Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity162Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 162")
    category: str = Field(default="Category_162", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=162 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity162Create(LibrarySchemaEntity162Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity162Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity162Response(LibrarySchemaEntity162Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity163Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 163")
    category: str = Field(default="Category_163", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=163 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity163Create(LibrarySchemaEntity163Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity163Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity163Response(LibrarySchemaEntity163Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity164Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 164")
    category: str = Field(default="Category_164", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=164 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity164Create(LibrarySchemaEntity164Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity164Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity164Response(LibrarySchemaEntity164Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity165Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 165")
    category: str = Field(default="Category_165", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=165 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity165Create(LibrarySchemaEntity165Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity165Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity165Response(LibrarySchemaEntity165Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity166Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 166")
    category: str = Field(default="Category_166", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=166 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity166Create(LibrarySchemaEntity166Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity166Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity166Response(LibrarySchemaEntity166Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity167Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 167")
    category: str = Field(default="Category_167", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=167 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity167Create(LibrarySchemaEntity167Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity167Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity167Response(LibrarySchemaEntity167Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity168Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 168")
    category: str = Field(default="Category_168", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=168 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity168Create(LibrarySchemaEntity168Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity168Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity168Response(LibrarySchemaEntity168Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity169Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 169")
    category: str = Field(default="Category_169", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=169 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity169Create(LibrarySchemaEntity169Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity169Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity169Response(LibrarySchemaEntity169Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity170Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 170")
    category: str = Field(default="Category_170", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=170 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity170Create(LibrarySchemaEntity170Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity170Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity170Response(LibrarySchemaEntity170Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity171Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 171")
    category: str = Field(default="Category_171", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=171 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity171Create(LibrarySchemaEntity171Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity171Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity171Response(LibrarySchemaEntity171Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity172Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 172")
    category: str = Field(default="Category_172", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=172 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity172Create(LibrarySchemaEntity172Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity172Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity172Response(LibrarySchemaEntity172Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity173Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 173")
    category: str = Field(default="Category_173", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=173 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity173Create(LibrarySchemaEntity173Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity173Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity173Response(LibrarySchemaEntity173Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity174Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 174")
    category: str = Field(default="Category_174", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=174 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity174Create(LibrarySchemaEntity174Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity174Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity174Response(LibrarySchemaEntity174Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity175Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 175")
    category: str = Field(default="Category_175", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=175 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity175Create(LibrarySchemaEntity175Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity175Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity175Response(LibrarySchemaEntity175Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity176Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 176")
    category: str = Field(default="Category_176", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=176 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity176Create(LibrarySchemaEntity176Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity176Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity176Response(LibrarySchemaEntity176Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity177Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 177")
    category: str = Field(default="Category_177", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=177 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity177Create(LibrarySchemaEntity177Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity177Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity177Response(LibrarySchemaEntity177Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity178Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 178")
    category: str = Field(default="Category_178", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=178 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity178Create(LibrarySchemaEntity178Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity178Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity178Response(LibrarySchemaEntity178Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity179Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 179")
    category: str = Field(default="Category_179", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=179 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity179Create(LibrarySchemaEntity179Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity179Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity179Response(LibrarySchemaEntity179Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity180Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 180")
    category: str = Field(default="Category_180", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=180 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity180Create(LibrarySchemaEntity180Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity180Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity180Response(LibrarySchemaEntity180Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity181Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 181")
    category: str = Field(default="Category_181", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=181 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity181Create(LibrarySchemaEntity181Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity181Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity181Response(LibrarySchemaEntity181Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity182Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 182")
    category: str = Field(default="Category_182", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=182 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity182Create(LibrarySchemaEntity182Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity182Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity182Response(LibrarySchemaEntity182Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity183Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 183")
    category: str = Field(default="Category_183", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=183 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity183Create(LibrarySchemaEntity183Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity183Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity183Response(LibrarySchemaEntity183Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity184Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 184")
    category: str = Field(default="Category_184", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=184 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity184Create(LibrarySchemaEntity184Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity184Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity184Response(LibrarySchemaEntity184Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity185Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 185")
    category: str = Field(default="Category_185", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=185 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity185Create(LibrarySchemaEntity185Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity185Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity185Response(LibrarySchemaEntity185Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity186Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 186")
    category: str = Field(default="Category_186", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=186 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity186Create(LibrarySchemaEntity186Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity186Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity186Response(LibrarySchemaEntity186Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity187Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 187")
    category: str = Field(default="Category_187", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=187 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity187Create(LibrarySchemaEntity187Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity187Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity187Response(LibrarySchemaEntity187Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity188Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 188")
    category: str = Field(default="Category_188", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=188 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity188Create(LibrarySchemaEntity188Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity188Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity188Response(LibrarySchemaEntity188Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity189Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 189")
    category: str = Field(default="Category_189", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=189 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity189Create(LibrarySchemaEntity189Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity189Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity189Response(LibrarySchemaEntity189Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity190Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 190")
    category: str = Field(default="Category_190", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=190 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity190Create(LibrarySchemaEntity190Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity190Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity190Response(LibrarySchemaEntity190Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity191Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 191")
    category: str = Field(default="Category_191", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=191 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity191Create(LibrarySchemaEntity191Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity191Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity191Response(LibrarySchemaEntity191Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity192Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 192")
    category: str = Field(default="Category_192", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=192 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity192Create(LibrarySchemaEntity192Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity192Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity192Response(LibrarySchemaEntity192Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity193Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 193")
    category: str = Field(default="Category_193", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=193 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity193Create(LibrarySchemaEntity193Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity193Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity193Response(LibrarySchemaEntity193Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity194Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 194")
    category: str = Field(default="Category_194", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=194 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity194Create(LibrarySchemaEntity194Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity194Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity194Response(LibrarySchemaEntity194Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity195Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 195")
    category: str = Field(default="Category_195", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=195 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity195Create(LibrarySchemaEntity195Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity195Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity195Response(LibrarySchemaEntity195Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity196Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 196")
    category: str = Field(default="Category_196", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=196 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity196Create(LibrarySchemaEntity196Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity196Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity196Response(LibrarySchemaEntity196Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity197Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 197")
    category: str = Field(default="Category_197", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=197 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity197Create(LibrarySchemaEntity197Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity197Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity197Response(LibrarySchemaEntity197Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity198Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 198")
    category: str = Field(default="Category_198", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=198 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity198Create(LibrarySchemaEntity198Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity198Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity198Response(LibrarySchemaEntity198Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity199Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 199")
    category: str = Field(default="Category_199", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=199 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity199Create(LibrarySchemaEntity199Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity199Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity199Response(LibrarySchemaEntity199Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity200Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 200")
    category: str = Field(default="Category_200", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=200 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity200Create(LibrarySchemaEntity200Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity200Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity200Response(LibrarySchemaEntity200Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity201Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 201")
    category: str = Field(default="Category_201", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=201 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity201Create(LibrarySchemaEntity201Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity201Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity201Response(LibrarySchemaEntity201Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity202Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 202")
    category: str = Field(default="Category_202", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=202 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity202Create(LibrarySchemaEntity202Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity202Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity202Response(LibrarySchemaEntity202Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity203Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 203")
    category: str = Field(default="Category_203", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=203 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity203Create(LibrarySchemaEntity203Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity203Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity203Response(LibrarySchemaEntity203Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity204Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 204")
    category: str = Field(default="Category_204", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=204 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity204Create(LibrarySchemaEntity204Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity204Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity204Response(LibrarySchemaEntity204Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity205Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 205")
    category: str = Field(default="Category_205", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=205 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity205Create(LibrarySchemaEntity205Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity205Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity205Response(LibrarySchemaEntity205Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity206Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 206")
    category: str = Field(default="Category_206", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=206 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity206Create(LibrarySchemaEntity206Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity206Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity206Response(LibrarySchemaEntity206Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity207Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 207")
    category: str = Field(default="Category_207", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=207 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity207Create(LibrarySchemaEntity207Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity207Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity207Response(LibrarySchemaEntity207Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity208Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 208")
    category: str = Field(default="Category_208", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=208 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity208Create(LibrarySchemaEntity208Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity208Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity208Response(LibrarySchemaEntity208Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity209Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 209")
    category: str = Field(default="Category_209", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=209 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity209Create(LibrarySchemaEntity209Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity209Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity209Response(LibrarySchemaEntity209Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity210Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 210")
    category: str = Field(default="Category_210", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=210 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity210Create(LibrarySchemaEntity210Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity210Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity210Response(LibrarySchemaEntity210Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity211Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 211")
    category: str = Field(default="Category_211", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=211 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity211Create(LibrarySchemaEntity211Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity211Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity211Response(LibrarySchemaEntity211Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity212Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 212")
    category: str = Field(default="Category_212", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=212 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity212Create(LibrarySchemaEntity212Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity212Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity212Response(LibrarySchemaEntity212Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity213Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 213")
    category: str = Field(default="Category_213", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=213 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity213Create(LibrarySchemaEntity213Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity213Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity213Response(LibrarySchemaEntity213Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity214Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 214")
    category: str = Field(default="Category_214", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=214 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity214Create(LibrarySchemaEntity214Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity214Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity214Response(LibrarySchemaEntity214Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity215Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 215")
    category: str = Field(default="Category_215", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=215 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity215Create(LibrarySchemaEntity215Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity215Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity215Response(LibrarySchemaEntity215Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity216Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 216")
    category: str = Field(default="Category_216", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=216 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity216Create(LibrarySchemaEntity216Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity216Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity216Response(LibrarySchemaEntity216Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity217Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 217")
    category: str = Field(default="Category_217", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=217 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity217Create(LibrarySchemaEntity217Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity217Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity217Response(LibrarySchemaEntity217Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity218Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 218")
    category: str = Field(default="Category_218", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=218 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity218Create(LibrarySchemaEntity218Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity218Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity218Response(LibrarySchemaEntity218Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity219Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 219")
    category: str = Field(default="Category_219", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=219 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity219Create(LibrarySchemaEntity219Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity219Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity219Response(LibrarySchemaEntity219Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity220Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 220")
    category: str = Field(default="Category_220", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=220 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity220Create(LibrarySchemaEntity220Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity220Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity220Response(LibrarySchemaEntity220Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity221Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 221")
    category: str = Field(default="Category_221", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=221 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity221Create(LibrarySchemaEntity221Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity221Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity221Response(LibrarySchemaEntity221Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity222Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 222")
    category: str = Field(default="Category_222", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=222 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity222Create(LibrarySchemaEntity222Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity222Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity222Response(LibrarySchemaEntity222Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity223Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 223")
    category: str = Field(default="Category_223", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=223 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity223Create(LibrarySchemaEntity223Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity223Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity223Response(LibrarySchemaEntity223Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity224Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 224")
    category: str = Field(default="Category_224", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=224 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity224Create(LibrarySchemaEntity224Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity224Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity224Response(LibrarySchemaEntity224Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity225Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 225")
    category: str = Field(default="Category_225", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=225 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity225Create(LibrarySchemaEntity225Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity225Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity225Response(LibrarySchemaEntity225Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity226Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 226")
    category: str = Field(default="Category_226", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=226 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity226Create(LibrarySchemaEntity226Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity226Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity226Response(LibrarySchemaEntity226Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity227Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 227")
    category: str = Field(default="Category_227", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=227 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity227Create(LibrarySchemaEntity227Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity227Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity227Response(LibrarySchemaEntity227Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity228Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 228")
    category: str = Field(default="Category_228", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=228 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity228Create(LibrarySchemaEntity228Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity228Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity228Response(LibrarySchemaEntity228Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity229Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 229")
    category: str = Field(default="Category_229", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=229 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity229Create(LibrarySchemaEntity229Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity229Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity229Response(LibrarySchemaEntity229Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity230Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 230")
    category: str = Field(default="Category_230", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=230 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity230Create(LibrarySchemaEntity230Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity230Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity230Response(LibrarySchemaEntity230Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity231Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 231")
    category: str = Field(default="Category_231", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=231 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity231Create(LibrarySchemaEntity231Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity231Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity231Response(LibrarySchemaEntity231Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity232Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 232")
    category: str = Field(default="Category_232", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=232 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity232Create(LibrarySchemaEntity232Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity232Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity232Response(LibrarySchemaEntity232Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity233Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 233")
    category: str = Field(default="Category_233", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=233 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity233Create(LibrarySchemaEntity233Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity233Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity233Response(LibrarySchemaEntity233Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity234Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 234")
    category: str = Field(default="Category_234", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=234 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity234Create(LibrarySchemaEntity234Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity234Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity234Response(LibrarySchemaEntity234Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity235Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 235")
    category: str = Field(default="Category_235", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=235 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity235Create(LibrarySchemaEntity235Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity235Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity235Response(LibrarySchemaEntity235Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity236Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 236")
    category: str = Field(default="Category_236", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=236 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity236Create(LibrarySchemaEntity236Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity236Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity236Response(LibrarySchemaEntity236Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity237Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 237")
    category: str = Field(default="Category_237", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=237 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity237Create(LibrarySchemaEntity237Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity237Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity237Response(LibrarySchemaEntity237Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity238Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 238")
    category: str = Field(default="Category_238", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=238 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity238Create(LibrarySchemaEntity238Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity238Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity238Response(LibrarySchemaEntity238Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity239Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 239")
    category: str = Field(default="Category_239", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=239 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity239Create(LibrarySchemaEntity239Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity239Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity239Response(LibrarySchemaEntity239Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity240Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 240")
    category: str = Field(default="Category_240", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=240 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity240Create(LibrarySchemaEntity240Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity240Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity240Response(LibrarySchemaEntity240Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity241Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 241")
    category: str = Field(default="Category_241", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=241 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity241Create(LibrarySchemaEntity241Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity241Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity241Response(LibrarySchemaEntity241Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity242Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 242")
    category: str = Field(default="Category_242", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=242 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity242Create(LibrarySchemaEntity242Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity242Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity242Response(LibrarySchemaEntity242Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity243Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 243")
    category: str = Field(default="Category_243", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=243 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity243Create(LibrarySchemaEntity243Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity243Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity243Response(LibrarySchemaEntity243Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity244Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 244")
    category: str = Field(default="Category_244", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=244 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity244Create(LibrarySchemaEntity244Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity244Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity244Response(LibrarySchemaEntity244Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity245Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 245")
    category: str = Field(default="Category_245", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=245 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity245Create(LibrarySchemaEntity245Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity245Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity245Response(LibrarySchemaEntity245Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity246Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 246")
    category: str = Field(default="Category_246", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=246 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity246Create(LibrarySchemaEntity246Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity246Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity246Response(LibrarySchemaEntity246Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity247Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 247")
    category: str = Field(default="Category_247", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=247 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity247Create(LibrarySchemaEntity247Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity247Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity247Response(LibrarySchemaEntity247Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity248Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 248")
    category: str = Field(default="Category_248", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=248 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity248Create(LibrarySchemaEntity248Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity248Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity248Response(LibrarySchemaEntity248Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity249Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 249")
    category: str = Field(default="Category_249", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=249 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity249Create(LibrarySchemaEntity249Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity249Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity249Response(LibrarySchemaEntity249Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class LibrarySchemaEntity250Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 250")
    category: str = Field(default="Category_250", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=250 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class LibrarySchemaEntity250Create(LibrarySchemaEntity250Base):
    entity_code: str = Field(..., max_length=100)

class LibrarySchemaEntity250Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class LibrarySchemaEntity250Response(LibrarySchemaEntity250Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

