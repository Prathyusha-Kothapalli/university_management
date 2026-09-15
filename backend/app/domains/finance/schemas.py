"""
Finance, Billing & Payroll - Pydantic Validation Schemas
Module: app.domains.finance.schemas
"""
from typing import Optional, List, Any, Dict
from datetime import datetime, date
from pydantic import BaseModel, Field, ConfigDict

class FinanceSchemaEntity1Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 1")
    category: str = Field(default="Category_1", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=1 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity1Create(FinanceSchemaEntity1Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity1Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity1Response(FinanceSchemaEntity1Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity2Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 2")
    category: str = Field(default="Category_2", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=2 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity2Create(FinanceSchemaEntity2Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity2Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity2Response(FinanceSchemaEntity2Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity3Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 3")
    category: str = Field(default="Category_3", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=3 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity3Create(FinanceSchemaEntity3Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity3Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity3Response(FinanceSchemaEntity3Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity4Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 4")
    category: str = Field(default="Category_4", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=4 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity4Create(FinanceSchemaEntity4Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity4Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity4Response(FinanceSchemaEntity4Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity5Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 5")
    category: str = Field(default="Category_5", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=5 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity5Create(FinanceSchemaEntity5Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity5Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity5Response(FinanceSchemaEntity5Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity6Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 6")
    category: str = Field(default="Category_6", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=6 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity6Create(FinanceSchemaEntity6Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity6Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity6Response(FinanceSchemaEntity6Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity7Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 7")
    category: str = Field(default="Category_7", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=7 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity7Create(FinanceSchemaEntity7Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity7Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity7Response(FinanceSchemaEntity7Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity8Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 8")
    category: str = Field(default="Category_8", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=8 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity8Create(FinanceSchemaEntity8Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity8Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity8Response(FinanceSchemaEntity8Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity9Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 9")
    category: str = Field(default="Category_9", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=9 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity9Create(FinanceSchemaEntity9Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity9Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity9Response(FinanceSchemaEntity9Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity10Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 10")
    category: str = Field(default="Category_10", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=10 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity10Create(FinanceSchemaEntity10Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity10Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity10Response(FinanceSchemaEntity10Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity11Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 11")
    category: str = Field(default="Category_11", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=11 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity11Create(FinanceSchemaEntity11Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity11Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity11Response(FinanceSchemaEntity11Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity12Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 12")
    category: str = Field(default="Category_12", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=12 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity12Create(FinanceSchemaEntity12Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity12Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity12Response(FinanceSchemaEntity12Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity13Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 13")
    category: str = Field(default="Category_13", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=13 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity13Create(FinanceSchemaEntity13Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity13Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity13Response(FinanceSchemaEntity13Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity14Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 14")
    category: str = Field(default="Category_14", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=14 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity14Create(FinanceSchemaEntity14Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity14Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity14Response(FinanceSchemaEntity14Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity15Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 15")
    category: str = Field(default="Category_15", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=15 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity15Create(FinanceSchemaEntity15Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity15Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity15Response(FinanceSchemaEntity15Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity16Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 16")
    category: str = Field(default="Category_16", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=16 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity16Create(FinanceSchemaEntity16Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity16Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity16Response(FinanceSchemaEntity16Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity17Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 17")
    category: str = Field(default="Category_17", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=17 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity17Create(FinanceSchemaEntity17Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity17Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity17Response(FinanceSchemaEntity17Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity18Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 18")
    category: str = Field(default="Category_18", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=18 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity18Create(FinanceSchemaEntity18Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity18Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity18Response(FinanceSchemaEntity18Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity19Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 19")
    category: str = Field(default="Category_19", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=19 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity19Create(FinanceSchemaEntity19Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity19Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity19Response(FinanceSchemaEntity19Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity20Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 20")
    category: str = Field(default="Category_20", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=20 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity20Create(FinanceSchemaEntity20Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity20Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity20Response(FinanceSchemaEntity20Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity21Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 21")
    category: str = Field(default="Category_21", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=21 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity21Create(FinanceSchemaEntity21Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity21Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity21Response(FinanceSchemaEntity21Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity22Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 22")
    category: str = Field(default="Category_22", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=22 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity22Create(FinanceSchemaEntity22Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity22Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity22Response(FinanceSchemaEntity22Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity23Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 23")
    category: str = Field(default="Category_23", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=23 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity23Create(FinanceSchemaEntity23Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity23Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity23Response(FinanceSchemaEntity23Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity24Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 24")
    category: str = Field(default="Category_24", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=24 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity24Create(FinanceSchemaEntity24Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity24Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity24Response(FinanceSchemaEntity24Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity25Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 25")
    category: str = Field(default="Category_25", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=25 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity25Create(FinanceSchemaEntity25Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity25Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity25Response(FinanceSchemaEntity25Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity26Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 26")
    category: str = Field(default="Category_26", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=26 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity26Create(FinanceSchemaEntity26Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity26Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity26Response(FinanceSchemaEntity26Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity27Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 27")
    category: str = Field(default="Category_27", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=27 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity27Create(FinanceSchemaEntity27Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity27Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity27Response(FinanceSchemaEntity27Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity28Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 28")
    category: str = Field(default="Category_28", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=28 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity28Create(FinanceSchemaEntity28Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity28Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity28Response(FinanceSchemaEntity28Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity29Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 29")
    category: str = Field(default="Category_29", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=29 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity29Create(FinanceSchemaEntity29Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity29Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity29Response(FinanceSchemaEntity29Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity30Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 30")
    category: str = Field(default="Category_30", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=30 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity30Create(FinanceSchemaEntity30Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity30Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity30Response(FinanceSchemaEntity30Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity31Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 31")
    category: str = Field(default="Category_31", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=31 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity31Create(FinanceSchemaEntity31Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity31Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity31Response(FinanceSchemaEntity31Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity32Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 32")
    category: str = Field(default="Category_32", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=32 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity32Create(FinanceSchemaEntity32Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity32Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity32Response(FinanceSchemaEntity32Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity33Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 33")
    category: str = Field(default="Category_33", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=33 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity33Create(FinanceSchemaEntity33Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity33Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity33Response(FinanceSchemaEntity33Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity34Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 34")
    category: str = Field(default="Category_34", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=34 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity34Create(FinanceSchemaEntity34Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity34Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity34Response(FinanceSchemaEntity34Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity35Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 35")
    category: str = Field(default="Category_35", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=35 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity35Create(FinanceSchemaEntity35Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity35Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity35Response(FinanceSchemaEntity35Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity36Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 36")
    category: str = Field(default="Category_36", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=36 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity36Create(FinanceSchemaEntity36Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity36Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity36Response(FinanceSchemaEntity36Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity37Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 37")
    category: str = Field(default="Category_37", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=37 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity37Create(FinanceSchemaEntity37Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity37Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity37Response(FinanceSchemaEntity37Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity38Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 38")
    category: str = Field(default="Category_38", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=38 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity38Create(FinanceSchemaEntity38Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity38Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity38Response(FinanceSchemaEntity38Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity39Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 39")
    category: str = Field(default="Category_39", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=39 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity39Create(FinanceSchemaEntity39Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity39Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity39Response(FinanceSchemaEntity39Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity40Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 40")
    category: str = Field(default="Category_40", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=40 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity40Create(FinanceSchemaEntity40Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity40Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity40Response(FinanceSchemaEntity40Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity41Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 41")
    category: str = Field(default="Category_41", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=41 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity41Create(FinanceSchemaEntity41Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity41Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity41Response(FinanceSchemaEntity41Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity42Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 42")
    category: str = Field(default="Category_42", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=42 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity42Create(FinanceSchemaEntity42Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity42Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity42Response(FinanceSchemaEntity42Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity43Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 43")
    category: str = Field(default="Category_43", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=43 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity43Create(FinanceSchemaEntity43Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity43Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity43Response(FinanceSchemaEntity43Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity44Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 44")
    category: str = Field(default="Category_44", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=44 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity44Create(FinanceSchemaEntity44Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity44Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity44Response(FinanceSchemaEntity44Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity45Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 45")
    category: str = Field(default="Category_45", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=45 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity45Create(FinanceSchemaEntity45Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity45Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity45Response(FinanceSchemaEntity45Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity46Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 46")
    category: str = Field(default="Category_46", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=46 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity46Create(FinanceSchemaEntity46Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity46Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity46Response(FinanceSchemaEntity46Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity47Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 47")
    category: str = Field(default="Category_47", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=47 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity47Create(FinanceSchemaEntity47Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity47Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity47Response(FinanceSchemaEntity47Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity48Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 48")
    category: str = Field(default="Category_48", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=48 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity48Create(FinanceSchemaEntity48Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity48Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity48Response(FinanceSchemaEntity48Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity49Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 49")
    category: str = Field(default="Category_49", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=49 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity49Create(FinanceSchemaEntity49Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity49Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity49Response(FinanceSchemaEntity49Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity50Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 50")
    category: str = Field(default="Category_50", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=50 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity50Create(FinanceSchemaEntity50Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity50Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity50Response(FinanceSchemaEntity50Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity51Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 51")
    category: str = Field(default="Category_51", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=51 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity51Create(FinanceSchemaEntity51Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity51Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity51Response(FinanceSchemaEntity51Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity52Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 52")
    category: str = Field(default="Category_52", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=52 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity52Create(FinanceSchemaEntity52Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity52Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity52Response(FinanceSchemaEntity52Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity53Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 53")
    category: str = Field(default="Category_53", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=53 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity53Create(FinanceSchemaEntity53Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity53Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity53Response(FinanceSchemaEntity53Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity54Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 54")
    category: str = Field(default="Category_54", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=54 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity54Create(FinanceSchemaEntity54Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity54Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity54Response(FinanceSchemaEntity54Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity55Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 55")
    category: str = Field(default="Category_55", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=55 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity55Create(FinanceSchemaEntity55Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity55Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity55Response(FinanceSchemaEntity55Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity56Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 56")
    category: str = Field(default="Category_56", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=56 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity56Create(FinanceSchemaEntity56Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity56Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity56Response(FinanceSchemaEntity56Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity57Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 57")
    category: str = Field(default="Category_57", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=57 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity57Create(FinanceSchemaEntity57Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity57Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity57Response(FinanceSchemaEntity57Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity58Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 58")
    category: str = Field(default="Category_58", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=58 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity58Create(FinanceSchemaEntity58Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity58Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity58Response(FinanceSchemaEntity58Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity59Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 59")
    category: str = Field(default="Category_59", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=59 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity59Create(FinanceSchemaEntity59Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity59Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity59Response(FinanceSchemaEntity59Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity60Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 60")
    category: str = Field(default="Category_60", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=60 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity60Create(FinanceSchemaEntity60Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity60Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity60Response(FinanceSchemaEntity60Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity61Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 61")
    category: str = Field(default="Category_61", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=61 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity61Create(FinanceSchemaEntity61Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity61Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity61Response(FinanceSchemaEntity61Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity62Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 62")
    category: str = Field(default="Category_62", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=62 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity62Create(FinanceSchemaEntity62Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity62Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity62Response(FinanceSchemaEntity62Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity63Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 63")
    category: str = Field(default="Category_63", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=63 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity63Create(FinanceSchemaEntity63Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity63Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity63Response(FinanceSchemaEntity63Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity64Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 64")
    category: str = Field(default="Category_64", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=64 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity64Create(FinanceSchemaEntity64Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity64Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity64Response(FinanceSchemaEntity64Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity65Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 65")
    category: str = Field(default="Category_65", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=65 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity65Create(FinanceSchemaEntity65Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity65Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity65Response(FinanceSchemaEntity65Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity66Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 66")
    category: str = Field(default="Category_66", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=66 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity66Create(FinanceSchemaEntity66Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity66Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity66Response(FinanceSchemaEntity66Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity67Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 67")
    category: str = Field(default="Category_67", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=67 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity67Create(FinanceSchemaEntity67Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity67Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity67Response(FinanceSchemaEntity67Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity68Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 68")
    category: str = Field(default="Category_68", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=68 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity68Create(FinanceSchemaEntity68Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity68Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity68Response(FinanceSchemaEntity68Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity69Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 69")
    category: str = Field(default="Category_69", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=69 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity69Create(FinanceSchemaEntity69Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity69Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity69Response(FinanceSchemaEntity69Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity70Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 70")
    category: str = Field(default="Category_70", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=70 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity70Create(FinanceSchemaEntity70Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity70Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity70Response(FinanceSchemaEntity70Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity71Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 71")
    category: str = Field(default="Category_71", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=71 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity71Create(FinanceSchemaEntity71Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity71Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity71Response(FinanceSchemaEntity71Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity72Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 72")
    category: str = Field(default="Category_72", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=72 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity72Create(FinanceSchemaEntity72Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity72Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity72Response(FinanceSchemaEntity72Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity73Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 73")
    category: str = Field(default="Category_73", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=73 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity73Create(FinanceSchemaEntity73Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity73Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity73Response(FinanceSchemaEntity73Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity74Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 74")
    category: str = Field(default="Category_74", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=74 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity74Create(FinanceSchemaEntity74Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity74Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity74Response(FinanceSchemaEntity74Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity75Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 75")
    category: str = Field(default="Category_75", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=75 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity75Create(FinanceSchemaEntity75Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity75Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity75Response(FinanceSchemaEntity75Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity76Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 76")
    category: str = Field(default="Category_76", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=76 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity76Create(FinanceSchemaEntity76Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity76Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity76Response(FinanceSchemaEntity76Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity77Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 77")
    category: str = Field(default="Category_77", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=77 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity77Create(FinanceSchemaEntity77Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity77Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity77Response(FinanceSchemaEntity77Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity78Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 78")
    category: str = Field(default="Category_78", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=78 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity78Create(FinanceSchemaEntity78Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity78Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity78Response(FinanceSchemaEntity78Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity79Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 79")
    category: str = Field(default="Category_79", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=79 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity79Create(FinanceSchemaEntity79Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity79Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity79Response(FinanceSchemaEntity79Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity80Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 80")
    category: str = Field(default="Category_80", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=80 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity80Create(FinanceSchemaEntity80Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity80Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity80Response(FinanceSchemaEntity80Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity81Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 81")
    category: str = Field(default="Category_81", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=81 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity81Create(FinanceSchemaEntity81Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity81Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity81Response(FinanceSchemaEntity81Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity82Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 82")
    category: str = Field(default="Category_82", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=82 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity82Create(FinanceSchemaEntity82Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity82Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity82Response(FinanceSchemaEntity82Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity83Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 83")
    category: str = Field(default="Category_83", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=83 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity83Create(FinanceSchemaEntity83Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity83Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity83Response(FinanceSchemaEntity83Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity84Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 84")
    category: str = Field(default="Category_84", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=84 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity84Create(FinanceSchemaEntity84Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity84Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity84Response(FinanceSchemaEntity84Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity85Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 85")
    category: str = Field(default="Category_85", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=85 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity85Create(FinanceSchemaEntity85Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity85Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity85Response(FinanceSchemaEntity85Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity86Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 86")
    category: str = Field(default="Category_86", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=86 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity86Create(FinanceSchemaEntity86Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity86Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity86Response(FinanceSchemaEntity86Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity87Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 87")
    category: str = Field(default="Category_87", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=87 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity87Create(FinanceSchemaEntity87Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity87Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity87Response(FinanceSchemaEntity87Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity88Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 88")
    category: str = Field(default="Category_88", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=88 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity88Create(FinanceSchemaEntity88Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity88Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity88Response(FinanceSchemaEntity88Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity89Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 89")
    category: str = Field(default="Category_89", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=89 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity89Create(FinanceSchemaEntity89Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity89Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity89Response(FinanceSchemaEntity89Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity90Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 90")
    category: str = Field(default="Category_90", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=90 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity90Create(FinanceSchemaEntity90Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity90Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity90Response(FinanceSchemaEntity90Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity91Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 91")
    category: str = Field(default="Category_91", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=91 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity91Create(FinanceSchemaEntity91Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity91Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity91Response(FinanceSchemaEntity91Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity92Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 92")
    category: str = Field(default="Category_92", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=92 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity92Create(FinanceSchemaEntity92Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity92Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity92Response(FinanceSchemaEntity92Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity93Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 93")
    category: str = Field(default="Category_93", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=93 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity93Create(FinanceSchemaEntity93Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity93Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity93Response(FinanceSchemaEntity93Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity94Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 94")
    category: str = Field(default="Category_94", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=94 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity94Create(FinanceSchemaEntity94Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity94Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity94Response(FinanceSchemaEntity94Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity95Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 95")
    category: str = Field(default="Category_95", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=95 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity95Create(FinanceSchemaEntity95Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity95Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity95Response(FinanceSchemaEntity95Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity96Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 96")
    category: str = Field(default="Category_96", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=96 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity96Create(FinanceSchemaEntity96Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity96Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity96Response(FinanceSchemaEntity96Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity97Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 97")
    category: str = Field(default="Category_97", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=97 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity97Create(FinanceSchemaEntity97Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity97Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity97Response(FinanceSchemaEntity97Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity98Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 98")
    category: str = Field(default="Category_98", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=98 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity98Create(FinanceSchemaEntity98Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity98Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity98Response(FinanceSchemaEntity98Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity99Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 99")
    category: str = Field(default="Category_99", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=99 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity99Create(FinanceSchemaEntity99Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity99Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity99Response(FinanceSchemaEntity99Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity100Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 100")
    category: str = Field(default="Category_100", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=100 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity100Create(FinanceSchemaEntity100Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity100Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity100Response(FinanceSchemaEntity100Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity101Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 101")
    category: str = Field(default="Category_101", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=101 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity101Create(FinanceSchemaEntity101Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity101Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity101Response(FinanceSchemaEntity101Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity102Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 102")
    category: str = Field(default="Category_102", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=102 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity102Create(FinanceSchemaEntity102Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity102Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity102Response(FinanceSchemaEntity102Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity103Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 103")
    category: str = Field(default="Category_103", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=103 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity103Create(FinanceSchemaEntity103Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity103Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity103Response(FinanceSchemaEntity103Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity104Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 104")
    category: str = Field(default="Category_104", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=104 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity104Create(FinanceSchemaEntity104Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity104Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity104Response(FinanceSchemaEntity104Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity105Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 105")
    category: str = Field(default="Category_105", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=105 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity105Create(FinanceSchemaEntity105Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity105Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity105Response(FinanceSchemaEntity105Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity106Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 106")
    category: str = Field(default="Category_106", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=106 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity106Create(FinanceSchemaEntity106Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity106Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity106Response(FinanceSchemaEntity106Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity107Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 107")
    category: str = Field(default="Category_107", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=107 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity107Create(FinanceSchemaEntity107Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity107Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity107Response(FinanceSchemaEntity107Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity108Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 108")
    category: str = Field(default="Category_108", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=108 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity108Create(FinanceSchemaEntity108Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity108Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity108Response(FinanceSchemaEntity108Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity109Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 109")
    category: str = Field(default="Category_109", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=109 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity109Create(FinanceSchemaEntity109Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity109Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity109Response(FinanceSchemaEntity109Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity110Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 110")
    category: str = Field(default="Category_110", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=110 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity110Create(FinanceSchemaEntity110Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity110Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity110Response(FinanceSchemaEntity110Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity111Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 111")
    category: str = Field(default="Category_111", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=111 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity111Create(FinanceSchemaEntity111Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity111Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity111Response(FinanceSchemaEntity111Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity112Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 112")
    category: str = Field(default="Category_112", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=112 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity112Create(FinanceSchemaEntity112Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity112Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity112Response(FinanceSchemaEntity112Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity113Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 113")
    category: str = Field(default="Category_113", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=113 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity113Create(FinanceSchemaEntity113Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity113Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity113Response(FinanceSchemaEntity113Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity114Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 114")
    category: str = Field(default="Category_114", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=114 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity114Create(FinanceSchemaEntity114Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity114Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity114Response(FinanceSchemaEntity114Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity115Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 115")
    category: str = Field(default="Category_115", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=115 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity115Create(FinanceSchemaEntity115Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity115Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity115Response(FinanceSchemaEntity115Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity116Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 116")
    category: str = Field(default="Category_116", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=116 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity116Create(FinanceSchemaEntity116Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity116Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity116Response(FinanceSchemaEntity116Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity117Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 117")
    category: str = Field(default="Category_117", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=117 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity117Create(FinanceSchemaEntity117Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity117Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity117Response(FinanceSchemaEntity117Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity118Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 118")
    category: str = Field(default="Category_118", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=118 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity118Create(FinanceSchemaEntity118Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity118Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity118Response(FinanceSchemaEntity118Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity119Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 119")
    category: str = Field(default="Category_119", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=119 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity119Create(FinanceSchemaEntity119Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity119Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity119Response(FinanceSchemaEntity119Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity120Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 120")
    category: str = Field(default="Category_120", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=120 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity120Create(FinanceSchemaEntity120Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity120Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity120Response(FinanceSchemaEntity120Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity121Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 121")
    category: str = Field(default="Category_121", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=121 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity121Create(FinanceSchemaEntity121Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity121Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity121Response(FinanceSchemaEntity121Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity122Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 122")
    category: str = Field(default="Category_122", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=122 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity122Create(FinanceSchemaEntity122Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity122Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity122Response(FinanceSchemaEntity122Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity123Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 123")
    category: str = Field(default="Category_123", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=123 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity123Create(FinanceSchemaEntity123Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity123Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity123Response(FinanceSchemaEntity123Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity124Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 124")
    category: str = Field(default="Category_124", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=124 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity124Create(FinanceSchemaEntity124Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity124Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity124Response(FinanceSchemaEntity124Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity125Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 125")
    category: str = Field(default="Category_125", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=125 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity125Create(FinanceSchemaEntity125Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity125Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity125Response(FinanceSchemaEntity125Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity126Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 126")
    category: str = Field(default="Category_126", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=126 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity126Create(FinanceSchemaEntity126Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity126Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity126Response(FinanceSchemaEntity126Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity127Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 127")
    category: str = Field(default="Category_127", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=127 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity127Create(FinanceSchemaEntity127Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity127Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity127Response(FinanceSchemaEntity127Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity128Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 128")
    category: str = Field(default="Category_128", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=128 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity128Create(FinanceSchemaEntity128Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity128Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity128Response(FinanceSchemaEntity128Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity129Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 129")
    category: str = Field(default="Category_129", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=129 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity129Create(FinanceSchemaEntity129Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity129Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity129Response(FinanceSchemaEntity129Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity130Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 130")
    category: str = Field(default="Category_130", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=130 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity130Create(FinanceSchemaEntity130Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity130Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity130Response(FinanceSchemaEntity130Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity131Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 131")
    category: str = Field(default="Category_131", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=131 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity131Create(FinanceSchemaEntity131Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity131Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity131Response(FinanceSchemaEntity131Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity132Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 132")
    category: str = Field(default="Category_132", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=132 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity132Create(FinanceSchemaEntity132Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity132Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity132Response(FinanceSchemaEntity132Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity133Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 133")
    category: str = Field(default="Category_133", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=133 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity133Create(FinanceSchemaEntity133Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity133Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity133Response(FinanceSchemaEntity133Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity134Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 134")
    category: str = Field(default="Category_134", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=134 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity134Create(FinanceSchemaEntity134Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity134Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity134Response(FinanceSchemaEntity134Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity135Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 135")
    category: str = Field(default="Category_135", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=135 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity135Create(FinanceSchemaEntity135Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity135Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity135Response(FinanceSchemaEntity135Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity136Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 136")
    category: str = Field(default="Category_136", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=136 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity136Create(FinanceSchemaEntity136Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity136Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity136Response(FinanceSchemaEntity136Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity137Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 137")
    category: str = Field(default="Category_137", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=137 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity137Create(FinanceSchemaEntity137Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity137Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity137Response(FinanceSchemaEntity137Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity138Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 138")
    category: str = Field(default="Category_138", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=138 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity138Create(FinanceSchemaEntity138Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity138Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity138Response(FinanceSchemaEntity138Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity139Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 139")
    category: str = Field(default="Category_139", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=139 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity139Create(FinanceSchemaEntity139Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity139Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity139Response(FinanceSchemaEntity139Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity140Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 140")
    category: str = Field(default="Category_140", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=140 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity140Create(FinanceSchemaEntity140Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity140Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity140Response(FinanceSchemaEntity140Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity141Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 141")
    category: str = Field(default="Category_141", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=141 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity141Create(FinanceSchemaEntity141Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity141Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity141Response(FinanceSchemaEntity141Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity142Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 142")
    category: str = Field(default="Category_142", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=142 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity142Create(FinanceSchemaEntity142Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity142Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity142Response(FinanceSchemaEntity142Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity143Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 143")
    category: str = Field(default="Category_143", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=143 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity143Create(FinanceSchemaEntity143Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity143Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity143Response(FinanceSchemaEntity143Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity144Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 144")
    category: str = Field(default="Category_144", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=144 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity144Create(FinanceSchemaEntity144Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity144Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity144Response(FinanceSchemaEntity144Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity145Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 145")
    category: str = Field(default="Category_145", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=145 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity145Create(FinanceSchemaEntity145Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity145Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity145Response(FinanceSchemaEntity145Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity146Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 146")
    category: str = Field(default="Category_146", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=146 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity146Create(FinanceSchemaEntity146Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity146Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity146Response(FinanceSchemaEntity146Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity147Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 147")
    category: str = Field(default="Category_147", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=147 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity147Create(FinanceSchemaEntity147Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity147Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity147Response(FinanceSchemaEntity147Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity148Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 148")
    category: str = Field(default="Category_148", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=148 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity148Create(FinanceSchemaEntity148Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity148Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity148Response(FinanceSchemaEntity148Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity149Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 149")
    category: str = Field(default="Category_149", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=149 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity149Create(FinanceSchemaEntity149Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity149Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity149Response(FinanceSchemaEntity149Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity150Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 150")
    category: str = Field(default="Category_150", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=150 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity150Create(FinanceSchemaEntity150Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity150Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity150Response(FinanceSchemaEntity150Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity151Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 151")
    category: str = Field(default="Category_151", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=151 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity151Create(FinanceSchemaEntity151Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity151Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity151Response(FinanceSchemaEntity151Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity152Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 152")
    category: str = Field(default="Category_152", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=152 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity152Create(FinanceSchemaEntity152Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity152Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity152Response(FinanceSchemaEntity152Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity153Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 153")
    category: str = Field(default="Category_153", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=153 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity153Create(FinanceSchemaEntity153Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity153Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity153Response(FinanceSchemaEntity153Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity154Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 154")
    category: str = Field(default="Category_154", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=154 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity154Create(FinanceSchemaEntity154Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity154Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity154Response(FinanceSchemaEntity154Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity155Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 155")
    category: str = Field(default="Category_155", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=155 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity155Create(FinanceSchemaEntity155Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity155Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity155Response(FinanceSchemaEntity155Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity156Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 156")
    category: str = Field(default="Category_156", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=156 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity156Create(FinanceSchemaEntity156Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity156Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity156Response(FinanceSchemaEntity156Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity157Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 157")
    category: str = Field(default="Category_157", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=157 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity157Create(FinanceSchemaEntity157Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity157Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity157Response(FinanceSchemaEntity157Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity158Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 158")
    category: str = Field(default="Category_158", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=158 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity158Create(FinanceSchemaEntity158Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity158Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity158Response(FinanceSchemaEntity158Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity159Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 159")
    category: str = Field(default="Category_159", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=159 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity159Create(FinanceSchemaEntity159Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity159Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity159Response(FinanceSchemaEntity159Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity160Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 160")
    category: str = Field(default="Category_160", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=160 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity160Create(FinanceSchemaEntity160Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity160Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity160Response(FinanceSchemaEntity160Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity161Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 161")
    category: str = Field(default="Category_161", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=161 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity161Create(FinanceSchemaEntity161Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity161Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity161Response(FinanceSchemaEntity161Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity162Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 162")
    category: str = Field(default="Category_162", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=162 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity162Create(FinanceSchemaEntity162Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity162Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity162Response(FinanceSchemaEntity162Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity163Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 163")
    category: str = Field(default="Category_163", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=163 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity163Create(FinanceSchemaEntity163Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity163Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity163Response(FinanceSchemaEntity163Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity164Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 164")
    category: str = Field(default="Category_164", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=164 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity164Create(FinanceSchemaEntity164Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity164Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity164Response(FinanceSchemaEntity164Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity165Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 165")
    category: str = Field(default="Category_165", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=165 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity165Create(FinanceSchemaEntity165Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity165Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity165Response(FinanceSchemaEntity165Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity166Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 166")
    category: str = Field(default="Category_166", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=166 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity166Create(FinanceSchemaEntity166Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity166Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity166Response(FinanceSchemaEntity166Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity167Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 167")
    category: str = Field(default="Category_167", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=167 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity167Create(FinanceSchemaEntity167Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity167Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity167Response(FinanceSchemaEntity167Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity168Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 168")
    category: str = Field(default="Category_168", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=168 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity168Create(FinanceSchemaEntity168Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity168Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity168Response(FinanceSchemaEntity168Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity169Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 169")
    category: str = Field(default="Category_169", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=169 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity169Create(FinanceSchemaEntity169Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity169Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity169Response(FinanceSchemaEntity169Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity170Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 170")
    category: str = Field(default="Category_170", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=170 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity170Create(FinanceSchemaEntity170Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity170Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity170Response(FinanceSchemaEntity170Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity171Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 171")
    category: str = Field(default="Category_171", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=171 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity171Create(FinanceSchemaEntity171Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity171Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity171Response(FinanceSchemaEntity171Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity172Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 172")
    category: str = Field(default="Category_172", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=172 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity172Create(FinanceSchemaEntity172Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity172Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity172Response(FinanceSchemaEntity172Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity173Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 173")
    category: str = Field(default="Category_173", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=173 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity173Create(FinanceSchemaEntity173Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity173Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity173Response(FinanceSchemaEntity173Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity174Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 174")
    category: str = Field(default="Category_174", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=174 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity174Create(FinanceSchemaEntity174Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity174Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity174Response(FinanceSchemaEntity174Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity175Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 175")
    category: str = Field(default="Category_175", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=175 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity175Create(FinanceSchemaEntity175Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity175Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity175Response(FinanceSchemaEntity175Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity176Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 176")
    category: str = Field(default="Category_176", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=176 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity176Create(FinanceSchemaEntity176Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity176Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity176Response(FinanceSchemaEntity176Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity177Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 177")
    category: str = Field(default="Category_177", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=177 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity177Create(FinanceSchemaEntity177Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity177Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity177Response(FinanceSchemaEntity177Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity178Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 178")
    category: str = Field(default="Category_178", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=178 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity178Create(FinanceSchemaEntity178Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity178Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity178Response(FinanceSchemaEntity178Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity179Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 179")
    category: str = Field(default="Category_179", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=179 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity179Create(FinanceSchemaEntity179Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity179Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity179Response(FinanceSchemaEntity179Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity180Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 180")
    category: str = Field(default="Category_180", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=180 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity180Create(FinanceSchemaEntity180Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity180Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity180Response(FinanceSchemaEntity180Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity181Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 181")
    category: str = Field(default="Category_181", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=181 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity181Create(FinanceSchemaEntity181Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity181Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity181Response(FinanceSchemaEntity181Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity182Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 182")
    category: str = Field(default="Category_182", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=182 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity182Create(FinanceSchemaEntity182Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity182Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity182Response(FinanceSchemaEntity182Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity183Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 183")
    category: str = Field(default="Category_183", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=183 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity183Create(FinanceSchemaEntity183Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity183Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity183Response(FinanceSchemaEntity183Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity184Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 184")
    category: str = Field(default="Category_184", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=184 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity184Create(FinanceSchemaEntity184Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity184Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity184Response(FinanceSchemaEntity184Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity185Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 185")
    category: str = Field(default="Category_185", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=185 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity185Create(FinanceSchemaEntity185Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity185Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity185Response(FinanceSchemaEntity185Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity186Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 186")
    category: str = Field(default="Category_186", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=186 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity186Create(FinanceSchemaEntity186Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity186Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity186Response(FinanceSchemaEntity186Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity187Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 187")
    category: str = Field(default="Category_187", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=187 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity187Create(FinanceSchemaEntity187Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity187Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity187Response(FinanceSchemaEntity187Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity188Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 188")
    category: str = Field(default="Category_188", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=188 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity188Create(FinanceSchemaEntity188Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity188Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity188Response(FinanceSchemaEntity188Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity189Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 189")
    category: str = Field(default="Category_189", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=189 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity189Create(FinanceSchemaEntity189Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity189Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity189Response(FinanceSchemaEntity189Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity190Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 190")
    category: str = Field(default="Category_190", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=190 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity190Create(FinanceSchemaEntity190Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity190Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity190Response(FinanceSchemaEntity190Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity191Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 191")
    category: str = Field(default="Category_191", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=191 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity191Create(FinanceSchemaEntity191Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity191Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity191Response(FinanceSchemaEntity191Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity192Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 192")
    category: str = Field(default="Category_192", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=192 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity192Create(FinanceSchemaEntity192Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity192Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity192Response(FinanceSchemaEntity192Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity193Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 193")
    category: str = Field(default="Category_193", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=193 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity193Create(FinanceSchemaEntity193Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity193Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity193Response(FinanceSchemaEntity193Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity194Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 194")
    category: str = Field(default="Category_194", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=194 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity194Create(FinanceSchemaEntity194Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity194Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity194Response(FinanceSchemaEntity194Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity195Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 195")
    category: str = Field(default="Category_195", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=195 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity195Create(FinanceSchemaEntity195Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity195Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity195Response(FinanceSchemaEntity195Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity196Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 196")
    category: str = Field(default="Category_196", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=196 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity196Create(FinanceSchemaEntity196Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity196Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity196Response(FinanceSchemaEntity196Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity197Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 197")
    category: str = Field(default="Category_197", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=197 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity197Create(FinanceSchemaEntity197Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity197Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity197Response(FinanceSchemaEntity197Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity198Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 198")
    category: str = Field(default="Category_198", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=198 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity198Create(FinanceSchemaEntity198Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity198Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity198Response(FinanceSchemaEntity198Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity199Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 199")
    category: str = Field(default="Category_199", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=199 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity199Create(FinanceSchemaEntity199Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity199Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity199Response(FinanceSchemaEntity199Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity200Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 200")
    category: str = Field(default="Category_200", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=200 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity200Create(FinanceSchemaEntity200Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity200Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity200Response(FinanceSchemaEntity200Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity201Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 201")
    category: str = Field(default="Category_201", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=201 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity201Create(FinanceSchemaEntity201Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity201Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity201Response(FinanceSchemaEntity201Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity202Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 202")
    category: str = Field(default="Category_202", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=202 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity202Create(FinanceSchemaEntity202Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity202Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity202Response(FinanceSchemaEntity202Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity203Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 203")
    category: str = Field(default="Category_203", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=203 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity203Create(FinanceSchemaEntity203Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity203Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity203Response(FinanceSchemaEntity203Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity204Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 204")
    category: str = Field(default="Category_204", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=204 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity204Create(FinanceSchemaEntity204Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity204Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity204Response(FinanceSchemaEntity204Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity205Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 205")
    category: str = Field(default="Category_205", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=205 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity205Create(FinanceSchemaEntity205Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity205Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity205Response(FinanceSchemaEntity205Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity206Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 206")
    category: str = Field(default="Category_206", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=206 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity206Create(FinanceSchemaEntity206Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity206Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity206Response(FinanceSchemaEntity206Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity207Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 207")
    category: str = Field(default="Category_207", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=207 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity207Create(FinanceSchemaEntity207Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity207Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity207Response(FinanceSchemaEntity207Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity208Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 208")
    category: str = Field(default="Category_208", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=208 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity208Create(FinanceSchemaEntity208Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity208Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity208Response(FinanceSchemaEntity208Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity209Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 209")
    category: str = Field(default="Category_209", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=209 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity209Create(FinanceSchemaEntity209Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity209Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity209Response(FinanceSchemaEntity209Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity210Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 210")
    category: str = Field(default="Category_210", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=210 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity210Create(FinanceSchemaEntity210Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity210Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity210Response(FinanceSchemaEntity210Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity211Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 211")
    category: str = Field(default="Category_211", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=211 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity211Create(FinanceSchemaEntity211Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity211Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity211Response(FinanceSchemaEntity211Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity212Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 212")
    category: str = Field(default="Category_212", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=212 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity212Create(FinanceSchemaEntity212Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity212Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity212Response(FinanceSchemaEntity212Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity213Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 213")
    category: str = Field(default="Category_213", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=213 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity213Create(FinanceSchemaEntity213Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity213Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity213Response(FinanceSchemaEntity213Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity214Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 214")
    category: str = Field(default="Category_214", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=214 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity214Create(FinanceSchemaEntity214Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity214Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity214Response(FinanceSchemaEntity214Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity215Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 215")
    category: str = Field(default="Category_215", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=215 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity215Create(FinanceSchemaEntity215Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity215Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity215Response(FinanceSchemaEntity215Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity216Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 216")
    category: str = Field(default="Category_216", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=216 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity216Create(FinanceSchemaEntity216Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity216Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity216Response(FinanceSchemaEntity216Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity217Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 217")
    category: str = Field(default="Category_217", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=217 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity217Create(FinanceSchemaEntity217Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity217Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity217Response(FinanceSchemaEntity217Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity218Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 218")
    category: str = Field(default="Category_218", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=218 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity218Create(FinanceSchemaEntity218Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity218Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity218Response(FinanceSchemaEntity218Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity219Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 219")
    category: str = Field(default="Category_219", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=219 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity219Create(FinanceSchemaEntity219Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity219Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity219Response(FinanceSchemaEntity219Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity220Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 220")
    category: str = Field(default="Category_220", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=220 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity220Create(FinanceSchemaEntity220Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity220Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity220Response(FinanceSchemaEntity220Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity221Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 221")
    category: str = Field(default="Category_221", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=221 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity221Create(FinanceSchemaEntity221Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity221Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity221Response(FinanceSchemaEntity221Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity222Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 222")
    category: str = Field(default="Category_222", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=222 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity222Create(FinanceSchemaEntity222Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity222Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity222Response(FinanceSchemaEntity222Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity223Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 223")
    category: str = Field(default="Category_223", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=223 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity223Create(FinanceSchemaEntity223Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity223Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity223Response(FinanceSchemaEntity223Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity224Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 224")
    category: str = Field(default="Category_224", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=224 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity224Create(FinanceSchemaEntity224Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity224Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity224Response(FinanceSchemaEntity224Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity225Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 225")
    category: str = Field(default="Category_225", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=225 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity225Create(FinanceSchemaEntity225Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity225Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity225Response(FinanceSchemaEntity225Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity226Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 226")
    category: str = Field(default="Category_226", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=226 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity226Create(FinanceSchemaEntity226Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity226Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity226Response(FinanceSchemaEntity226Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity227Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 227")
    category: str = Field(default="Category_227", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=227 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity227Create(FinanceSchemaEntity227Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity227Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity227Response(FinanceSchemaEntity227Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity228Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 228")
    category: str = Field(default="Category_228", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=228 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity228Create(FinanceSchemaEntity228Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity228Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity228Response(FinanceSchemaEntity228Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity229Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 229")
    category: str = Field(default="Category_229", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=229 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity229Create(FinanceSchemaEntity229Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity229Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity229Response(FinanceSchemaEntity229Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity230Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 230")
    category: str = Field(default="Category_230", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=230 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity230Create(FinanceSchemaEntity230Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity230Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity230Response(FinanceSchemaEntity230Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity231Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 231")
    category: str = Field(default="Category_231", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=231 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity231Create(FinanceSchemaEntity231Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity231Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity231Response(FinanceSchemaEntity231Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity232Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 232")
    category: str = Field(default="Category_232", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=232 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity232Create(FinanceSchemaEntity232Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity232Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity232Response(FinanceSchemaEntity232Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity233Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 233")
    category: str = Field(default="Category_233", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=233 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity233Create(FinanceSchemaEntity233Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity233Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity233Response(FinanceSchemaEntity233Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity234Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 234")
    category: str = Field(default="Category_234", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=234 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity234Create(FinanceSchemaEntity234Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity234Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity234Response(FinanceSchemaEntity234Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity235Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 235")
    category: str = Field(default="Category_235", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=235 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity235Create(FinanceSchemaEntity235Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity235Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity235Response(FinanceSchemaEntity235Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity236Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 236")
    category: str = Field(default="Category_236", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=236 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity236Create(FinanceSchemaEntity236Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity236Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity236Response(FinanceSchemaEntity236Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity237Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 237")
    category: str = Field(default="Category_237", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=237 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity237Create(FinanceSchemaEntity237Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity237Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity237Response(FinanceSchemaEntity237Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity238Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 238")
    category: str = Field(default="Category_238", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=238 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity238Create(FinanceSchemaEntity238Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity238Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity238Response(FinanceSchemaEntity238Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity239Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 239")
    category: str = Field(default="Category_239", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=239 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity239Create(FinanceSchemaEntity239Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity239Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity239Response(FinanceSchemaEntity239Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity240Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 240")
    category: str = Field(default="Category_240", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=240 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity240Create(FinanceSchemaEntity240Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity240Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity240Response(FinanceSchemaEntity240Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity241Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 241")
    category: str = Field(default="Category_241", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=241 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity241Create(FinanceSchemaEntity241Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity241Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity241Response(FinanceSchemaEntity241Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity242Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 242")
    category: str = Field(default="Category_242", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=242 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity242Create(FinanceSchemaEntity242Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity242Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity242Response(FinanceSchemaEntity242Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity243Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 243")
    category: str = Field(default="Category_243", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=243 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity243Create(FinanceSchemaEntity243Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity243Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity243Response(FinanceSchemaEntity243Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity244Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 244")
    category: str = Field(default="Category_244", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=244 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity244Create(FinanceSchemaEntity244Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity244Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity244Response(FinanceSchemaEntity244Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity245Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 245")
    category: str = Field(default="Category_245", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=245 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity245Create(FinanceSchemaEntity245Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity245Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity245Response(FinanceSchemaEntity245Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity246Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 246")
    category: str = Field(default="Category_246", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=246 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity246Create(FinanceSchemaEntity246Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity246Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity246Response(FinanceSchemaEntity246Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity247Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 247")
    category: str = Field(default="Category_247", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=247 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity247Create(FinanceSchemaEntity247Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity247Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity247Response(FinanceSchemaEntity247Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity248Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 248")
    category: str = Field(default="Category_248", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=248 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity248Create(FinanceSchemaEntity248Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity248Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity248Response(FinanceSchemaEntity248Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity249Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 249")
    category: str = Field(default="Category_249", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=249 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity249Create(FinanceSchemaEntity249Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity249Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity249Response(FinanceSchemaEntity249Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinanceSchemaEntity250Base(BaseModel):
    name: str = Field(..., max_length=255, description="Name of the entity 250")
    category: str = Field(default="Category_250", max_length=100)
    description: Optional[str] = Field(default=None)
    value_amount: float = Field(default=250 * 100.5)
    is_active: bool = Field(default=True)
    attributes_json: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinanceSchemaEntity250Create(FinanceSchemaEntity250Base):
    entity_code: str = Field(..., max_length=100)

class FinanceSchemaEntity250Update(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    value_amount: Optional[float] = None
    is_active: Optional[bool] = None
    status_flag: Optional[str] = None
    attributes_json: Optional[Dict[str, Any]] = None

class FinanceSchemaEntity250Response(FinanceSchemaEntity250Base):
    id: int
    entity_code: str
    status_flag: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

