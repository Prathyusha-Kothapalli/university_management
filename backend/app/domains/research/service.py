"""
Research, Grants & Lab Inventory - Service Business Logic Layer
Module: app.domains.research.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.research.models import *
from app.domains.research.schemas import *

class ResearchDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity1]:
        return self.db.query(ResearchModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[ResearchModelEntity1]:
        return self.db.query(ResearchModelEntity1).filter(ResearchModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: ResearchSchemaEntity1Create) -> ResearchModelEntity1:
        db_obj = ResearchModelEntity1(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_1(self, entity_id: int, payload: ResearchSchemaEntity1Update) -> Optional[ResearchModelEntity1]:
        db_obj = self.get_entity_1_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_1(self, entity_id: int) -> bool:
        db_obj = self.get_entity_1_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity2]:
        return self.db.query(ResearchModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[ResearchModelEntity2]:
        return self.db.query(ResearchModelEntity2).filter(ResearchModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: ResearchSchemaEntity2Create) -> ResearchModelEntity2:
        db_obj = ResearchModelEntity2(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_2(self, entity_id: int, payload: ResearchSchemaEntity2Update) -> Optional[ResearchModelEntity2]:
        db_obj = self.get_entity_2_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_2(self, entity_id: int) -> bool:
        db_obj = self.get_entity_2_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity3]:
        return self.db.query(ResearchModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[ResearchModelEntity3]:
        return self.db.query(ResearchModelEntity3).filter(ResearchModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: ResearchSchemaEntity3Create) -> ResearchModelEntity3:
        db_obj = ResearchModelEntity3(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_3(self, entity_id: int, payload: ResearchSchemaEntity3Update) -> Optional[ResearchModelEntity3]:
        db_obj = self.get_entity_3_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_3(self, entity_id: int) -> bool:
        db_obj = self.get_entity_3_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity4]:
        return self.db.query(ResearchModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[ResearchModelEntity4]:
        return self.db.query(ResearchModelEntity4).filter(ResearchModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: ResearchSchemaEntity4Create) -> ResearchModelEntity4:
        db_obj = ResearchModelEntity4(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_4(self, entity_id: int, payload: ResearchSchemaEntity4Update) -> Optional[ResearchModelEntity4]:
        db_obj = self.get_entity_4_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_4(self, entity_id: int) -> bool:
        db_obj = self.get_entity_4_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity5]:
        return self.db.query(ResearchModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[ResearchModelEntity5]:
        return self.db.query(ResearchModelEntity5).filter(ResearchModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: ResearchSchemaEntity5Create) -> ResearchModelEntity5:
        db_obj = ResearchModelEntity5(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_5(self, entity_id: int, payload: ResearchSchemaEntity5Update) -> Optional[ResearchModelEntity5]:
        db_obj = self.get_entity_5_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_5(self, entity_id: int) -> bool:
        db_obj = self.get_entity_5_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity6]:
        return self.db.query(ResearchModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[ResearchModelEntity6]:
        return self.db.query(ResearchModelEntity6).filter(ResearchModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: ResearchSchemaEntity6Create) -> ResearchModelEntity6:
        db_obj = ResearchModelEntity6(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_6(self, entity_id: int, payload: ResearchSchemaEntity6Update) -> Optional[ResearchModelEntity6]:
        db_obj = self.get_entity_6_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_6(self, entity_id: int) -> bool:
        db_obj = self.get_entity_6_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity7]:
        return self.db.query(ResearchModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[ResearchModelEntity7]:
        return self.db.query(ResearchModelEntity7).filter(ResearchModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: ResearchSchemaEntity7Create) -> ResearchModelEntity7:
        db_obj = ResearchModelEntity7(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_7(self, entity_id: int, payload: ResearchSchemaEntity7Update) -> Optional[ResearchModelEntity7]:
        db_obj = self.get_entity_7_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_7(self, entity_id: int) -> bool:
        db_obj = self.get_entity_7_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity8]:
        return self.db.query(ResearchModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[ResearchModelEntity8]:
        return self.db.query(ResearchModelEntity8).filter(ResearchModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: ResearchSchemaEntity8Create) -> ResearchModelEntity8:
        db_obj = ResearchModelEntity8(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_8(self, entity_id: int, payload: ResearchSchemaEntity8Update) -> Optional[ResearchModelEntity8]:
        db_obj = self.get_entity_8_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_8(self, entity_id: int) -> bool:
        db_obj = self.get_entity_8_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity9]:
        return self.db.query(ResearchModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[ResearchModelEntity9]:
        return self.db.query(ResearchModelEntity9).filter(ResearchModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: ResearchSchemaEntity9Create) -> ResearchModelEntity9:
        db_obj = ResearchModelEntity9(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_9(self, entity_id: int, payload: ResearchSchemaEntity9Update) -> Optional[ResearchModelEntity9]:
        db_obj = self.get_entity_9_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_9(self, entity_id: int) -> bool:
        db_obj = self.get_entity_9_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity10]:
        return self.db.query(ResearchModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[ResearchModelEntity10]:
        return self.db.query(ResearchModelEntity10).filter(ResearchModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: ResearchSchemaEntity10Create) -> ResearchModelEntity10:
        db_obj = ResearchModelEntity10(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_10(self, entity_id: int, payload: ResearchSchemaEntity10Update) -> Optional[ResearchModelEntity10]:
        db_obj = self.get_entity_10_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_10(self, entity_id: int) -> bool:
        db_obj = self.get_entity_10_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity11]:
        return self.db.query(ResearchModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[ResearchModelEntity11]:
        return self.db.query(ResearchModelEntity11).filter(ResearchModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: ResearchSchemaEntity11Create) -> ResearchModelEntity11:
        db_obj = ResearchModelEntity11(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_11(self, entity_id: int, payload: ResearchSchemaEntity11Update) -> Optional[ResearchModelEntity11]:
        db_obj = self.get_entity_11_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_11(self, entity_id: int) -> bool:
        db_obj = self.get_entity_11_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity12]:
        return self.db.query(ResearchModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[ResearchModelEntity12]:
        return self.db.query(ResearchModelEntity12).filter(ResearchModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: ResearchSchemaEntity12Create) -> ResearchModelEntity12:
        db_obj = ResearchModelEntity12(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_12(self, entity_id: int, payload: ResearchSchemaEntity12Update) -> Optional[ResearchModelEntity12]:
        db_obj = self.get_entity_12_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_12(self, entity_id: int) -> bool:
        db_obj = self.get_entity_12_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity13]:
        return self.db.query(ResearchModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[ResearchModelEntity13]:
        return self.db.query(ResearchModelEntity13).filter(ResearchModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: ResearchSchemaEntity13Create) -> ResearchModelEntity13:
        db_obj = ResearchModelEntity13(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_13(self, entity_id: int, payload: ResearchSchemaEntity13Update) -> Optional[ResearchModelEntity13]:
        db_obj = self.get_entity_13_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_13(self, entity_id: int) -> bool:
        db_obj = self.get_entity_13_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity14]:
        return self.db.query(ResearchModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[ResearchModelEntity14]:
        return self.db.query(ResearchModelEntity14).filter(ResearchModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: ResearchSchemaEntity14Create) -> ResearchModelEntity14:
        db_obj = ResearchModelEntity14(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_14(self, entity_id: int, payload: ResearchSchemaEntity14Update) -> Optional[ResearchModelEntity14]:
        db_obj = self.get_entity_14_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_14(self, entity_id: int) -> bool:
        db_obj = self.get_entity_14_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity15]:
        return self.db.query(ResearchModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[ResearchModelEntity15]:
        return self.db.query(ResearchModelEntity15).filter(ResearchModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: ResearchSchemaEntity15Create) -> ResearchModelEntity15:
        db_obj = ResearchModelEntity15(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_15(self, entity_id: int, payload: ResearchSchemaEntity15Update) -> Optional[ResearchModelEntity15]:
        db_obj = self.get_entity_15_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_15(self, entity_id: int) -> bool:
        db_obj = self.get_entity_15_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity16]:
        return self.db.query(ResearchModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[ResearchModelEntity16]:
        return self.db.query(ResearchModelEntity16).filter(ResearchModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: ResearchSchemaEntity16Create) -> ResearchModelEntity16:
        db_obj = ResearchModelEntity16(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_16(self, entity_id: int, payload: ResearchSchemaEntity16Update) -> Optional[ResearchModelEntity16]:
        db_obj = self.get_entity_16_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_16(self, entity_id: int) -> bool:
        db_obj = self.get_entity_16_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity17]:
        return self.db.query(ResearchModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[ResearchModelEntity17]:
        return self.db.query(ResearchModelEntity17).filter(ResearchModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: ResearchSchemaEntity17Create) -> ResearchModelEntity17:
        db_obj = ResearchModelEntity17(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_17(self, entity_id: int, payload: ResearchSchemaEntity17Update) -> Optional[ResearchModelEntity17]:
        db_obj = self.get_entity_17_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_17(self, entity_id: int) -> bool:
        db_obj = self.get_entity_17_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity18]:
        return self.db.query(ResearchModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[ResearchModelEntity18]:
        return self.db.query(ResearchModelEntity18).filter(ResearchModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: ResearchSchemaEntity18Create) -> ResearchModelEntity18:
        db_obj = ResearchModelEntity18(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_18(self, entity_id: int, payload: ResearchSchemaEntity18Update) -> Optional[ResearchModelEntity18]:
        db_obj = self.get_entity_18_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_18(self, entity_id: int) -> bool:
        db_obj = self.get_entity_18_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity19]:
        return self.db.query(ResearchModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[ResearchModelEntity19]:
        return self.db.query(ResearchModelEntity19).filter(ResearchModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: ResearchSchemaEntity19Create) -> ResearchModelEntity19:
        db_obj = ResearchModelEntity19(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_19(self, entity_id: int, payload: ResearchSchemaEntity19Update) -> Optional[ResearchModelEntity19]:
        db_obj = self.get_entity_19_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_19(self, entity_id: int) -> bool:
        db_obj = self.get_entity_19_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity20]:
        return self.db.query(ResearchModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[ResearchModelEntity20]:
        return self.db.query(ResearchModelEntity20).filter(ResearchModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: ResearchSchemaEntity20Create) -> ResearchModelEntity20:
        db_obj = ResearchModelEntity20(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_20(self, entity_id: int, payload: ResearchSchemaEntity20Update) -> Optional[ResearchModelEntity20]:
        db_obj = self.get_entity_20_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_20(self, entity_id: int) -> bool:
        db_obj = self.get_entity_20_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity21]:
        return self.db.query(ResearchModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[ResearchModelEntity21]:
        return self.db.query(ResearchModelEntity21).filter(ResearchModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: ResearchSchemaEntity21Create) -> ResearchModelEntity21:
        db_obj = ResearchModelEntity21(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_21(self, entity_id: int, payload: ResearchSchemaEntity21Update) -> Optional[ResearchModelEntity21]:
        db_obj = self.get_entity_21_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_21(self, entity_id: int) -> bool:
        db_obj = self.get_entity_21_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity22]:
        return self.db.query(ResearchModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[ResearchModelEntity22]:
        return self.db.query(ResearchModelEntity22).filter(ResearchModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: ResearchSchemaEntity22Create) -> ResearchModelEntity22:
        db_obj = ResearchModelEntity22(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_22(self, entity_id: int, payload: ResearchSchemaEntity22Update) -> Optional[ResearchModelEntity22]:
        db_obj = self.get_entity_22_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_22(self, entity_id: int) -> bool:
        db_obj = self.get_entity_22_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity23]:
        return self.db.query(ResearchModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[ResearchModelEntity23]:
        return self.db.query(ResearchModelEntity23).filter(ResearchModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: ResearchSchemaEntity23Create) -> ResearchModelEntity23:
        db_obj = ResearchModelEntity23(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_23(self, entity_id: int, payload: ResearchSchemaEntity23Update) -> Optional[ResearchModelEntity23]:
        db_obj = self.get_entity_23_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_23(self, entity_id: int) -> bool:
        db_obj = self.get_entity_23_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity24]:
        return self.db.query(ResearchModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[ResearchModelEntity24]:
        return self.db.query(ResearchModelEntity24).filter(ResearchModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: ResearchSchemaEntity24Create) -> ResearchModelEntity24:
        db_obj = ResearchModelEntity24(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_24(self, entity_id: int, payload: ResearchSchemaEntity24Update) -> Optional[ResearchModelEntity24]:
        db_obj = self.get_entity_24_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_24(self, entity_id: int) -> bool:
        db_obj = self.get_entity_24_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity25]:
        return self.db.query(ResearchModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[ResearchModelEntity25]:
        return self.db.query(ResearchModelEntity25).filter(ResearchModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: ResearchSchemaEntity25Create) -> ResearchModelEntity25:
        db_obj = ResearchModelEntity25(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_25(self, entity_id: int, payload: ResearchSchemaEntity25Update) -> Optional[ResearchModelEntity25]:
        db_obj = self.get_entity_25_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_25(self, entity_id: int) -> bool:
        db_obj = self.get_entity_25_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity26]:
        return self.db.query(ResearchModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[ResearchModelEntity26]:
        return self.db.query(ResearchModelEntity26).filter(ResearchModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: ResearchSchemaEntity26Create) -> ResearchModelEntity26:
        db_obj = ResearchModelEntity26(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_26(self, entity_id: int, payload: ResearchSchemaEntity26Update) -> Optional[ResearchModelEntity26]:
        db_obj = self.get_entity_26_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_26(self, entity_id: int) -> bool:
        db_obj = self.get_entity_26_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity27]:
        return self.db.query(ResearchModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[ResearchModelEntity27]:
        return self.db.query(ResearchModelEntity27).filter(ResearchModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: ResearchSchemaEntity27Create) -> ResearchModelEntity27:
        db_obj = ResearchModelEntity27(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_27(self, entity_id: int, payload: ResearchSchemaEntity27Update) -> Optional[ResearchModelEntity27]:
        db_obj = self.get_entity_27_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_27(self, entity_id: int) -> bool:
        db_obj = self.get_entity_27_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity28]:
        return self.db.query(ResearchModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[ResearchModelEntity28]:
        return self.db.query(ResearchModelEntity28).filter(ResearchModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: ResearchSchemaEntity28Create) -> ResearchModelEntity28:
        db_obj = ResearchModelEntity28(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_28(self, entity_id: int, payload: ResearchSchemaEntity28Update) -> Optional[ResearchModelEntity28]:
        db_obj = self.get_entity_28_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_28(self, entity_id: int) -> bool:
        db_obj = self.get_entity_28_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity29]:
        return self.db.query(ResearchModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[ResearchModelEntity29]:
        return self.db.query(ResearchModelEntity29).filter(ResearchModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: ResearchSchemaEntity29Create) -> ResearchModelEntity29:
        db_obj = ResearchModelEntity29(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_29(self, entity_id: int, payload: ResearchSchemaEntity29Update) -> Optional[ResearchModelEntity29]:
        db_obj = self.get_entity_29_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_29(self, entity_id: int) -> bool:
        db_obj = self.get_entity_29_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity30]:
        return self.db.query(ResearchModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[ResearchModelEntity30]:
        return self.db.query(ResearchModelEntity30).filter(ResearchModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: ResearchSchemaEntity30Create) -> ResearchModelEntity30:
        db_obj = ResearchModelEntity30(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_30(self, entity_id: int, payload: ResearchSchemaEntity30Update) -> Optional[ResearchModelEntity30]:
        db_obj = self.get_entity_30_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_30(self, entity_id: int) -> bool:
        db_obj = self.get_entity_30_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity31]:
        return self.db.query(ResearchModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[ResearchModelEntity31]:
        return self.db.query(ResearchModelEntity31).filter(ResearchModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: ResearchSchemaEntity31Create) -> ResearchModelEntity31:
        db_obj = ResearchModelEntity31(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_31(self, entity_id: int, payload: ResearchSchemaEntity31Update) -> Optional[ResearchModelEntity31]:
        db_obj = self.get_entity_31_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_31(self, entity_id: int) -> bool:
        db_obj = self.get_entity_31_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity32]:
        return self.db.query(ResearchModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[ResearchModelEntity32]:
        return self.db.query(ResearchModelEntity32).filter(ResearchModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: ResearchSchemaEntity32Create) -> ResearchModelEntity32:
        db_obj = ResearchModelEntity32(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_32(self, entity_id: int, payload: ResearchSchemaEntity32Update) -> Optional[ResearchModelEntity32]:
        db_obj = self.get_entity_32_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_32(self, entity_id: int) -> bool:
        db_obj = self.get_entity_32_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity33]:
        return self.db.query(ResearchModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[ResearchModelEntity33]:
        return self.db.query(ResearchModelEntity33).filter(ResearchModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: ResearchSchemaEntity33Create) -> ResearchModelEntity33:
        db_obj = ResearchModelEntity33(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_33(self, entity_id: int, payload: ResearchSchemaEntity33Update) -> Optional[ResearchModelEntity33]:
        db_obj = self.get_entity_33_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_33(self, entity_id: int) -> bool:
        db_obj = self.get_entity_33_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity34]:
        return self.db.query(ResearchModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[ResearchModelEntity34]:
        return self.db.query(ResearchModelEntity34).filter(ResearchModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: ResearchSchemaEntity34Create) -> ResearchModelEntity34:
        db_obj = ResearchModelEntity34(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_34(self, entity_id: int, payload: ResearchSchemaEntity34Update) -> Optional[ResearchModelEntity34]:
        db_obj = self.get_entity_34_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_34(self, entity_id: int) -> bool:
        db_obj = self.get_entity_34_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity35]:
        return self.db.query(ResearchModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[ResearchModelEntity35]:
        return self.db.query(ResearchModelEntity35).filter(ResearchModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: ResearchSchemaEntity35Create) -> ResearchModelEntity35:
        db_obj = ResearchModelEntity35(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_35(self, entity_id: int, payload: ResearchSchemaEntity35Update) -> Optional[ResearchModelEntity35]:
        db_obj = self.get_entity_35_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_35(self, entity_id: int) -> bool:
        db_obj = self.get_entity_35_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity36]:
        return self.db.query(ResearchModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[ResearchModelEntity36]:
        return self.db.query(ResearchModelEntity36).filter(ResearchModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: ResearchSchemaEntity36Create) -> ResearchModelEntity36:
        db_obj = ResearchModelEntity36(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_36(self, entity_id: int, payload: ResearchSchemaEntity36Update) -> Optional[ResearchModelEntity36]:
        db_obj = self.get_entity_36_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_36(self, entity_id: int) -> bool:
        db_obj = self.get_entity_36_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity37]:
        return self.db.query(ResearchModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[ResearchModelEntity37]:
        return self.db.query(ResearchModelEntity37).filter(ResearchModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: ResearchSchemaEntity37Create) -> ResearchModelEntity37:
        db_obj = ResearchModelEntity37(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_37(self, entity_id: int, payload: ResearchSchemaEntity37Update) -> Optional[ResearchModelEntity37]:
        db_obj = self.get_entity_37_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_37(self, entity_id: int) -> bool:
        db_obj = self.get_entity_37_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity38]:
        return self.db.query(ResearchModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[ResearchModelEntity38]:
        return self.db.query(ResearchModelEntity38).filter(ResearchModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: ResearchSchemaEntity38Create) -> ResearchModelEntity38:
        db_obj = ResearchModelEntity38(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_38(self, entity_id: int, payload: ResearchSchemaEntity38Update) -> Optional[ResearchModelEntity38]:
        db_obj = self.get_entity_38_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_38(self, entity_id: int) -> bool:
        db_obj = self.get_entity_38_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity39]:
        return self.db.query(ResearchModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[ResearchModelEntity39]:
        return self.db.query(ResearchModelEntity39).filter(ResearchModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: ResearchSchemaEntity39Create) -> ResearchModelEntity39:
        db_obj = ResearchModelEntity39(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_39(self, entity_id: int, payload: ResearchSchemaEntity39Update) -> Optional[ResearchModelEntity39]:
        db_obj = self.get_entity_39_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_39(self, entity_id: int) -> bool:
        db_obj = self.get_entity_39_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity40]:
        return self.db.query(ResearchModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[ResearchModelEntity40]:
        return self.db.query(ResearchModelEntity40).filter(ResearchModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: ResearchSchemaEntity40Create) -> ResearchModelEntity40:
        db_obj = ResearchModelEntity40(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_40(self, entity_id: int, payload: ResearchSchemaEntity40Update) -> Optional[ResearchModelEntity40]:
        db_obj = self.get_entity_40_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_40(self, entity_id: int) -> bool:
        db_obj = self.get_entity_40_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity41]:
        return self.db.query(ResearchModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[ResearchModelEntity41]:
        return self.db.query(ResearchModelEntity41).filter(ResearchModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: ResearchSchemaEntity41Create) -> ResearchModelEntity41:
        db_obj = ResearchModelEntity41(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_41(self, entity_id: int, payload: ResearchSchemaEntity41Update) -> Optional[ResearchModelEntity41]:
        db_obj = self.get_entity_41_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_41(self, entity_id: int) -> bool:
        db_obj = self.get_entity_41_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity42]:
        return self.db.query(ResearchModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[ResearchModelEntity42]:
        return self.db.query(ResearchModelEntity42).filter(ResearchModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: ResearchSchemaEntity42Create) -> ResearchModelEntity42:
        db_obj = ResearchModelEntity42(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_42(self, entity_id: int, payload: ResearchSchemaEntity42Update) -> Optional[ResearchModelEntity42]:
        db_obj = self.get_entity_42_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_42(self, entity_id: int) -> bool:
        db_obj = self.get_entity_42_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity43]:
        return self.db.query(ResearchModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[ResearchModelEntity43]:
        return self.db.query(ResearchModelEntity43).filter(ResearchModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: ResearchSchemaEntity43Create) -> ResearchModelEntity43:
        db_obj = ResearchModelEntity43(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_43(self, entity_id: int, payload: ResearchSchemaEntity43Update) -> Optional[ResearchModelEntity43]:
        db_obj = self.get_entity_43_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_43(self, entity_id: int) -> bool:
        db_obj = self.get_entity_43_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity44]:
        return self.db.query(ResearchModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[ResearchModelEntity44]:
        return self.db.query(ResearchModelEntity44).filter(ResearchModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: ResearchSchemaEntity44Create) -> ResearchModelEntity44:
        db_obj = ResearchModelEntity44(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_44(self, entity_id: int, payload: ResearchSchemaEntity44Update) -> Optional[ResearchModelEntity44]:
        db_obj = self.get_entity_44_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_44(self, entity_id: int) -> bool:
        db_obj = self.get_entity_44_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity45]:
        return self.db.query(ResearchModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[ResearchModelEntity45]:
        return self.db.query(ResearchModelEntity45).filter(ResearchModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: ResearchSchemaEntity45Create) -> ResearchModelEntity45:
        db_obj = ResearchModelEntity45(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_45(self, entity_id: int, payload: ResearchSchemaEntity45Update) -> Optional[ResearchModelEntity45]:
        db_obj = self.get_entity_45_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_45(self, entity_id: int) -> bool:
        db_obj = self.get_entity_45_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity46]:
        return self.db.query(ResearchModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[ResearchModelEntity46]:
        return self.db.query(ResearchModelEntity46).filter(ResearchModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: ResearchSchemaEntity46Create) -> ResearchModelEntity46:
        db_obj = ResearchModelEntity46(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_46(self, entity_id: int, payload: ResearchSchemaEntity46Update) -> Optional[ResearchModelEntity46]:
        db_obj = self.get_entity_46_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_46(self, entity_id: int) -> bool:
        db_obj = self.get_entity_46_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity47]:
        return self.db.query(ResearchModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[ResearchModelEntity47]:
        return self.db.query(ResearchModelEntity47).filter(ResearchModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: ResearchSchemaEntity47Create) -> ResearchModelEntity47:
        db_obj = ResearchModelEntity47(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_47(self, entity_id: int, payload: ResearchSchemaEntity47Update) -> Optional[ResearchModelEntity47]:
        db_obj = self.get_entity_47_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_47(self, entity_id: int) -> bool:
        db_obj = self.get_entity_47_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity48]:
        return self.db.query(ResearchModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[ResearchModelEntity48]:
        return self.db.query(ResearchModelEntity48).filter(ResearchModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: ResearchSchemaEntity48Create) -> ResearchModelEntity48:
        db_obj = ResearchModelEntity48(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_48(self, entity_id: int, payload: ResearchSchemaEntity48Update) -> Optional[ResearchModelEntity48]:
        db_obj = self.get_entity_48_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_48(self, entity_id: int) -> bool:
        db_obj = self.get_entity_48_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity49]:
        return self.db.query(ResearchModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[ResearchModelEntity49]:
        return self.db.query(ResearchModelEntity49).filter(ResearchModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: ResearchSchemaEntity49Create) -> ResearchModelEntity49:
        db_obj = ResearchModelEntity49(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_49(self, entity_id: int, payload: ResearchSchemaEntity49Update) -> Optional[ResearchModelEntity49]:
        db_obj = self.get_entity_49_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_49(self, entity_id: int) -> bool:
        db_obj = self.get_entity_49_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity50]:
        return self.db.query(ResearchModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[ResearchModelEntity50]:
        return self.db.query(ResearchModelEntity50).filter(ResearchModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: ResearchSchemaEntity50Create) -> ResearchModelEntity50:
        db_obj = ResearchModelEntity50(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_50(self, entity_id: int, payload: ResearchSchemaEntity50Update) -> Optional[ResearchModelEntity50]:
        db_obj = self.get_entity_50_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_50(self, entity_id: int) -> bool:
        db_obj = self.get_entity_50_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_51_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity51]:
        return self.db.query(ResearchModelEntity51).offset(skip).limit(limit).all()

    def get_entity_51_by_id(self, entity_id: int) -> Optional[ResearchModelEntity51]:
        return self.db.query(ResearchModelEntity51).filter(ResearchModelEntity51.id == entity_id).first()

    def create_entity_51(self, payload: ResearchSchemaEntity51Create) -> ResearchModelEntity51:
        db_obj = ResearchModelEntity51(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_51(self, entity_id: int, payload: ResearchSchemaEntity51Update) -> Optional[ResearchModelEntity51]:
        db_obj = self.get_entity_51_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_51(self, entity_id: int) -> bool:
        db_obj = self.get_entity_51_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_52_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity52]:
        return self.db.query(ResearchModelEntity52).offset(skip).limit(limit).all()

    def get_entity_52_by_id(self, entity_id: int) -> Optional[ResearchModelEntity52]:
        return self.db.query(ResearchModelEntity52).filter(ResearchModelEntity52.id == entity_id).first()

    def create_entity_52(self, payload: ResearchSchemaEntity52Create) -> ResearchModelEntity52:
        db_obj = ResearchModelEntity52(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_52(self, entity_id: int, payload: ResearchSchemaEntity52Update) -> Optional[ResearchModelEntity52]:
        db_obj = self.get_entity_52_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_52(self, entity_id: int) -> bool:
        db_obj = self.get_entity_52_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_53_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity53]:
        return self.db.query(ResearchModelEntity53).offset(skip).limit(limit).all()

    def get_entity_53_by_id(self, entity_id: int) -> Optional[ResearchModelEntity53]:
        return self.db.query(ResearchModelEntity53).filter(ResearchModelEntity53.id == entity_id).first()

    def create_entity_53(self, payload: ResearchSchemaEntity53Create) -> ResearchModelEntity53:
        db_obj = ResearchModelEntity53(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_53(self, entity_id: int, payload: ResearchSchemaEntity53Update) -> Optional[ResearchModelEntity53]:
        db_obj = self.get_entity_53_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_53(self, entity_id: int) -> bool:
        db_obj = self.get_entity_53_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_54_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity54]:
        return self.db.query(ResearchModelEntity54).offset(skip).limit(limit).all()

    def get_entity_54_by_id(self, entity_id: int) -> Optional[ResearchModelEntity54]:
        return self.db.query(ResearchModelEntity54).filter(ResearchModelEntity54.id == entity_id).first()

    def create_entity_54(self, payload: ResearchSchemaEntity54Create) -> ResearchModelEntity54:
        db_obj = ResearchModelEntity54(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_54(self, entity_id: int, payload: ResearchSchemaEntity54Update) -> Optional[ResearchModelEntity54]:
        db_obj = self.get_entity_54_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_54(self, entity_id: int) -> bool:
        db_obj = self.get_entity_54_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_55_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity55]:
        return self.db.query(ResearchModelEntity55).offset(skip).limit(limit).all()

    def get_entity_55_by_id(self, entity_id: int) -> Optional[ResearchModelEntity55]:
        return self.db.query(ResearchModelEntity55).filter(ResearchModelEntity55.id == entity_id).first()

    def create_entity_55(self, payload: ResearchSchemaEntity55Create) -> ResearchModelEntity55:
        db_obj = ResearchModelEntity55(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_55(self, entity_id: int, payload: ResearchSchemaEntity55Update) -> Optional[ResearchModelEntity55]:
        db_obj = self.get_entity_55_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_55(self, entity_id: int) -> bool:
        db_obj = self.get_entity_55_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_56_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity56]:
        return self.db.query(ResearchModelEntity56).offset(skip).limit(limit).all()

    def get_entity_56_by_id(self, entity_id: int) -> Optional[ResearchModelEntity56]:
        return self.db.query(ResearchModelEntity56).filter(ResearchModelEntity56.id == entity_id).first()

    def create_entity_56(self, payload: ResearchSchemaEntity56Create) -> ResearchModelEntity56:
        db_obj = ResearchModelEntity56(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_56(self, entity_id: int, payload: ResearchSchemaEntity56Update) -> Optional[ResearchModelEntity56]:
        db_obj = self.get_entity_56_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_56(self, entity_id: int) -> bool:
        db_obj = self.get_entity_56_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_57_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity57]:
        return self.db.query(ResearchModelEntity57).offset(skip).limit(limit).all()

    def get_entity_57_by_id(self, entity_id: int) -> Optional[ResearchModelEntity57]:
        return self.db.query(ResearchModelEntity57).filter(ResearchModelEntity57.id == entity_id).first()

    def create_entity_57(self, payload: ResearchSchemaEntity57Create) -> ResearchModelEntity57:
        db_obj = ResearchModelEntity57(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_57(self, entity_id: int, payload: ResearchSchemaEntity57Update) -> Optional[ResearchModelEntity57]:
        db_obj = self.get_entity_57_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_57(self, entity_id: int) -> bool:
        db_obj = self.get_entity_57_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_58_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity58]:
        return self.db.query(ResearchModelEntity58).offset(skip).limit(limit).all()

    def get_entity_58_by_id(self, entity_id: int) -> Optional[ResearchModelEntity58]:
        return self.db.query(ResearchModelEntity58).filter(ResearchModelEntity58.id == entity_id).first()

    def create_entity_58(self, payload: ResearchSchemaEntity58Create) -> ResearchModelEntity58:
        db_obj = ResearchModelEntity58(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_58(self, entity_id: int, payload: ResearchSchemaEntity58Update) -> Optional[ResearchModelEntity58]:
        db_obj = self.get_entity_58_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_58(self, entity_id: int) -> bool:
        db_obj = self.get_entity_58_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_59_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity59]:
        return self.db.query(ResearchModelEntity59).offset(skip).limit(limit).all()

    def get_entity_59_by_id(self, entity_id: int) -> Optional[ResearchModelEntity59]:
        return self.db.query(ResearchModelEntity59).filter(ResearchModelEntity59.id == entity_id).first()

    def create_entity_59(self, payload: ResearchSchemaEntity59Create) -> ResearchModelEntity59:
        db_obj = ResearchModelEntity59(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_59(self, entity_id: int, payload: ResearchSchemaEntity59Update) -> Optional[ResearchModelEntity59]:
        db_obj = self.get_entity_59_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_59(self, entity_id: int) -> bool:
        db_obj = self.get_entity_59_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_60_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity60]:
        return self.db.query(ResearchModelEntity60).offset(skip).limit(limit).all()

    def get_entity_60_by_id(self, entity_id: int) -> Optional[ResearchModelEntity60]:
        return self.db.query(ResearchModelEntity60).filter(ResearchModelEntity60.id == entity_id).first()

    def create_entity_60(self, payload: ResearchSchemaEntity60Create) -> ResearchModelEntity60:
        db_obj = ResearchModelEntity60(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_60(self, entity_id: int, payload: ResearchSchemaEntity60Update) -> Optional[ResearchModelEntity60]:
        db_obj = self.get_entity_60_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_60(self, entity_id: int) -> bool:
        db_obj = self.get_entity_60_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_61_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity61]:
        return self.db.query(ResearchModelEntity61).offset(skip).limit(limit).all()

    def get_entity_61_by_id(self, entity_id: int) -> Optional[ResearchModelEntity61]:
        return self.db.query(ResearchModelEntity61).filter(ResearchModelEntity61.id == entity_id).first()

    def create_entity_61(self, payload: ResearchSchemaEntity61Create) -> ResearchModelEntity61:
        db_obj = ResearchModelEntity61(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_61(self, entity_id: int, payload: ResearchSchemaEntity61Update) -> Optional[ResearchModelEntity61]:
        db_obj = self.get_entity_61_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_61(self, entity_id: int) -> bool:
        db_obj = self.get_entity_61_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_62_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity62]:
        return self.db.query(ResearchModelEntity62).offset(skip).limit(limit).all()

    def get_entity_62_by_id(self, entity_id: int) -> Optional[ResearchModelEntity62]:
        return self.db.query(ResearchModelEntity62).filter(ResearchModelEntity62.id == entity_id).first()

    def create_entity_62(self, payload: ResearchSchemaEntity62Create) -> ResearchModelEntity62:
        db_obj = ResearchModelEntity62(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_62(self, entity_id: int, payload: ResearchSchemaEntity62Update) -> Optional[ResearchModelEntity62]:
        db_obj = self.get_entity_62_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_62(self, entity_id: int) -> bool:
        db_obj = self.get_entity_62_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_63_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity63]:
        return self.db.query(ResearchModelEntity63).offset(skip).limit(limit).all()

    def get_entity_63_by_id(self, entity_id: int) -> Optional[ResearchModelEntity63]:
        return self.db.query(ResearchModelEntity63).filter(ResearchModelEntity63.id == entity_id).first()

    def create_entity_63(self, payload: ResearchSchemaEntity63Create) -> ResearchModelEntity63:
        db_obj = ResearchModelEntity63(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_63(self, entity_id: int, payload: ResearchSchemaEntity63Update) -> Optional[ResearchModelEntity63]:
        db_obj = self.get_entity_63_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_63(self, entity_id: int) -> bool:
        db_obj = self.get_entity_63_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_64_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity64]:
        return self.db.query(ResearchModelEntity64).offset(skip).limit(limit).all()

    def get_entity_64_by_id(self, entity_id: int) -> Optional[ResearchModelEntity64]:
        return self.db.query(ResearchModelEntity64).filter(ResearchModelEntity64.id == entity_id).first()

    def create_entity_64(self, payload: ResearchSchemaEntity64Create) -> ResearchModelEntity64:
        db_obj = ResearchModelEntity64(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_64(self, entity_id: int, payload: ResearchSchemaEntity64Update) -> Optional[ResearchModelEntity64]:
        db_obj = self.get_entity_64_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_64(self, entity_id: int) -> bool:
        db_obj = self.get_entity_64_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_65_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity65]:
        return self.db.query(ResearchModelEntity65).offset(skip).limit(limit).all()

    def get_entity_65_by_id(self, entity_id: int) -> Optional[ResearchModelEntity65]:
        return self.db.query(ResearchModelEntity65).filter(ResearchModelEntity65.id == entity_id).first()

    def create_entity_65(self, payload: ResearchSchemaEntity65Create) -> ResearchModelEntity65:
        db_obj = ResearchModelEntity65(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_65(self, entity_id: int, payload: ResearchSchemaEntity65Update) -> Optional[ResearchModelEntity65]:
        db_obj = self.get_entity_65_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_65(self, entity_id: int) -> bool:
        db_obj = self.get_entity_65_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_66_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity66]:
        return self.db.query(ResearchModelEntity66).offset(skip).limit(limit).all()

    def get_entity_66_by_id(self, entity_id: int) -> Optional[ResearchModelEntity66]:
        return self.db.query(ResearchModelEntity66).filter(ResearchModelEntity66.id == entity_id).first()

    def create_entity_66(self, payload: ResearchSchemaEntity66Create) -> ResearchModelEntity66:
        db_obj = ResearchModelEntity66(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_66(self, entity_id: int, payload: ResearchSchemaEntity66Update) -> Optional[ResearchModelEntity66]:
        db_obj = self.get_entity_66_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_66(self, entity_id: int) -> bool:
        db_obj = self.get_entity_66_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_67_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity67]:
        return self.db.query(ResearchModelEntity67).offset(skip).limit(limit).all()

    def get_entity_67_by_id(self, entity_id: int) -> Optional[ResearchModelEntity67]:
        return self.db.query(ResearchModelEntity67).filter(ResearchModelEntity67.id == entity_id).first()

    def create_entity_67(self, payload: ResearchSchemaEntity67Create) -> ResearchModelEntity67:
        db_obj = ResearchModelEntity67(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_67(self, entity_id: int, payload: ResearchSchemaEntity67Update) -> Optional[ResearchModelEntity67]:
        db_obj = self.get_entity_67_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_67(self, entity_id: int) -> bool:
        db_obj = self.get_entity_67_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_68_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity68]:
        return self.db.query(ResearchModelEntity68).offset(skip).limit(limit).all()

    def get_entity_68_by_id(self, entity_id: int) -> Optional[ResearchModelEntity68]:
        return self.db.query(ResearchModelEntity68).filter(ResearchModelEntity68.id == entity_id).first()

    def create_entity_68(self, payload: ResearchSchemaEntity68Create) -> ResearchModelEntity68:
        db_obj = ResearchModelEntity68(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_68(self, entity_id: int, payload: ResearchSchemaEntity68Update) -> Optional[ResearchModelEntity68]:
        db_obj = self.get_entity_68_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_68(self, entity_id: int) -> bool:
        db_obj = self.get_entity_68_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_69_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity69]:
        return self.db.query(ResearchModelEntity69).offset(skip).limit(limit).all()

    def get_entity_69_by_id(self, entity_id: int) -> Optional[ResearchModelEntity69]:
        return self.db.query(ResearchModelEntity69).filter(ResearchModelEntity69.id == entity_id).first()

    def create_entity_69(self, payload: ResearchSchemaEntity69Create) -> ResearchModelEntity69:
        db_obj = ResearchModelEntity69(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_69(self, entity_id: int, payload: ResearchSchemaEntity69Update) -> Optional[ResearchModelEntity69]:
        db_obj = self.get_entity_69_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_69(self, entity_id: int) -> bool:
        db_obj = self.get_entity_69_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_70_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity70]:
        return self.db.query(ResearchModelEntity70).offset(skip).limit(limit).all()

    def get_entity_70_by_id(self, entity_id: int) -> Optional[ResearchModelEntity70]:
        return self.db.query(ResearchModelEntity70).filter(ResearchModelEntity70.id == entity_id).first()

    def create_entity_70(self, payload: ResearchSchemaEntity70Create) -> ResearchModelEntity70:
        db_obj = ResearchModelEntity70(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_70(self, entity_id: int, payload: ResearchSchemaEntity70Update) -> Optional[ResearchModelEntity70]:
        db_obj = self.get_entity_70_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_70(self, entity_id: int) -> bool:
        db_obj = self.get_entity_70_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_71_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity71]:
        return self.db.query(ResearchModelEntity71).offset(skip).limit(limit).all()

    def get_entity_71_by_id(self, entity_id: int) -> Optional[ResearchModelEntity71]:
        return self.db.query(ResearchModelEntity71).filter(ResearchModelEntity71.id == entity_id).first()

    def create_entity_71(self, payload: ResearchSchemaEntity71Create) -> ResearchModelEntity71:
        db_obj = ResearchModelEntity71(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_71(self, entity_id: int, payload: ResearchSchemaEntity71Update) -> Optional[ResearchModelEntity71]:
        db_obj = self.get_entity_71_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_71(self, entity_id: int) -> bool:
        db_obj = self.get_entity_71_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_72_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity72]:
        return self.db.query(ResearchModelEntity72).offset(skip).limit(limit).all()

    def get_entity_72_by_id(self, entity_id: int) -> Optional[ResearchModelEntity72]:
        return self.db.query(ResearchModelEntity72).filter(ResearchModelEntity72.id == entity_id).first()

    def create_entity_72(self, payload: ResearchSchemaEntity72Create) -> ResearchModelEntity72:
        db_obj = ResearchModelEntity72(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_72(self, entity_id: int, payload: ResearchSchemaEntity72Update) -> Optional[ResearchModelEntity72]:
        db_obj = self.get_entity_72_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_72(self, entity_id: int) -> bool:
        db_obj = self.get_entity_72_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_73_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity73]:
        return self.db.query(ResearchModelEntity73).offset(skip).limit(limit).all()

    def get_entity_73_by_id(self, entity_id: int) -> Optional[ResearchModelEntity73]:
        return self.db.query(ResearchModelEntity73).filter(ResearchModelEntity73.id == entity_id).first()

    def create_entity_73(self, payload: ResearchSchemaEntity73Create) -> ResearchModelEntity73:
        db_obj = ResearchModelEntity73(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_73(self, entity_id: int, payload: ResearchSchemaEntity73Update) -> Optional[ResearchModelEntity73]:
        db_obj = self.get_entity_73_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_73(self, entity_id: int) -> bool:
        db_obj = self.get_entity_73_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_74_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity74]:
        return self.db.query(ResearchModelEntity74).offset(skip).limit(limit).all()

    def get_entity_74_by_id(self, entity_id: int) -> Optional[ResearchModelEntity74]:
        return self.db.query(ResearchModelEntity74).filter(ResearchModelEntity74.id == entity_id).first()

    def create_entity_74(self, payload: ResearchSchemaEntity74Create) -> ResearchModelEntity74:
        db_obj = ResearchModelEntity74(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_74(self, entity_id: int, payload: ResearchSchemaEntity74Update) -> Optional[ResearchModelEntity74]:
        db_obj = self.get_entity_74_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_74(self, entity_id: int) -> bool:
        db_obj = self.get_entity_74_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_75_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity75]:
        return self.db.query(ResearchModelEntity75).offset(skip).limit(limit).all()

    def get_entity_75_by_id(self, entity_id: int) -> Optional[ResearchModelEntity75]:
        return self.db.query(ResearchModelEntity75).filter(ResearchModelEntity75.id == entity_id).first()

    def create_entity_75(self, payload: ResearchSchemaEntity75Create) -> ResearchModelEntity75:
        db_obj = ResearchModelEntity75(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_75(self, entity_id: int, payload: ResearchSchemaEntity75Update) -> Optional[ResearchModelEntity75]:
        db_obj = self.get_entity_75_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_75(self, entity_id: int) -> bool:
        db_obj = self.get_entity_75_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_76_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity76]:
        return self.db.query(ResearchModelEntity76).offset(skip).limit(limit).all()

    def get_entity_76_by_id(self, entity_id: int) -> Optional[ResearchModelEntity76]:
        return self.db.query(ResearchModelEntity76).filter(ResearchModelEntity76.id == entity_id).first()

    def create_entity_76(self, payload: ResearchSchemaEntity76Create) -> ResearchModelEntity76:
        db_obj = ResearchModelEntity76(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_76(self, entity_id: int, payload: ResearchSchemaEntity76Update) -> Optional[ResearchModelEntity76]:
        db_obj = self.get_entity_76_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_76(self, entity_id: int) -> bool:
        db_obj = self.get_entity_76_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_77_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity77]:
        return self.db.query(ResearchModelEntity77).offset(skip).limit(limit).all()

    def get_entity_77_by_id(self, entity_id: int) -> Optional[ResearchModelEntity77]:
        return self.db.query(ResearchModelEntity77).filter(ResearchModelEntity77.id == entity_id).first()

    def create_entity_77(self, payload: ResearchSchemaEntity77Create) -> ResearchModelEntity77:
        db_obj = ResearchModelEntity77(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_77(self, entity_id: int, payload: ResearchSchemaEntity77Update) -> Optional[ResearchModelEntity77]:
        db_obj = self.get_entity_77_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_77(self, entity_id: int) -> bool:
        db_obj = self.get_entity_77_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_78_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity78]:
        return self.db.query(ResearchModelEntity78).offset(skip).limit(limit).all()

    def get_entity_78_by_id(self, entity_id: int) -> Optional[ResearchModelEntity78]:
        return self.db.query(ResearchModelEntity78).filter(ResearchModelEntity78.id == entity_id).first()

    def create_entity_78(self, payload: ResearchSchemaEntity78Create) -> ResearchModelEntity78:
        db_obj = ResearchModelEntity78(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_78(self, entity_id: int, payload: ResearchSchemaEntity78Update) -> Optional[ResearchModelEntity78]:
        db_obj = self.get_entity_78_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_78(self, entity_id: int) -> bool:
        db_obj = self.get_entity_78_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_79_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity79]:
        return self.db.query(ResearchModelEntity79).offset(skip).limit(limit).all()

    def get_entity_79_by_id(self, entity_id: int) -> Optional[ResearchModelEntity79]:
        return self.db.query(ResearchModelEntity79).filter(ResearchModelEntity79.id == entity_id).first()

    def create_entity_79(self, payload: ResearchSchemaEntity79Create) -> ResearchModelEntity79:
        db_obj = ResearchModelEntity79(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_79(self, entity_id: int, payload: ResearchSchemaEntity79Update) -> Optional[ResearchModelEntity79]:
        db_obj = self.get_entity_79_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_79(self, entity_id: int) -> bool:
        db_obj = self.get_entity_79_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_80_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity80]:
        return self.db.query(ResearchModelEntity80).offset(skip).limit(limit).all()

    def get_entity_80_by_id(self, entity_id: int) -> Optional[ResearchModelEntity80]:
        return self.db.query(ResearchModelEntity80).filter(ResearchModelEntity80.id == entity_id).first()

    def create_entity_80(self, payload: ResearchSchemaEntity80Create) -> ResearchModelEntity80:
        db_obj = ResearchModelEntity80(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_80(self, entity_id: int, payload: ResearchSchemaEntity80Update) -> Optional[ResearchModelEntity80]:
        db_obj = self.get_entity_80_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_80(self, entity_id: int) -> bool:
        db_obj = self.get_entity_80_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_81_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity81]:
        return self.db.query(ResearchModelEntity81).offset(skip).limit(limit).all()

    def get_entity_81_by_id(self, entity_id: int) -> Optional[ResearchModelEntity81]:
        return self.db.query(ResearchModelEntity81).filter(ResearchModelEntity81.id == entity_id).first()

    def create_entity_81(self, payload: ResearchSchemaEntity81Create) -> ResearchModelEntity81:
        db_obj = ResearchModelEntity81(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_81(self, entity_id: int, payload: ResearchSchemaEntity81Update) -> Optional[ResearchModelEntity81]:
        db_obj = self.get_entity_81_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_81(self, entity_id: int) -> bool:
        db_obj = self.get_entity_81_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_82_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity82]:
        return self.db.query(ResearchModelEntity82).offset(skip).limit(limit).all()

    def get_entity_82_by_id(self, entity_id: int) -> Optional[ResearchModelEntity82]:
        return self.db.query(ResearchModelEntity82).filter(ResearchModelEntity82.id == entity_id).first()

    def create_entity_82(self, payload: ResearchSchemaEntity82Create) -> ResearchModelEntity82:
        db_obj = ResearchModelEntity82(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_82(self, entity_id: int, payload: ResearchSchemaEntity82Update) -> Optional[ResearchModelEntity82]:
        db_obj = self.get_entity_82_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_82(self, entity_id: int) -> bool:
        db_obj = self.get_entity_82_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_83_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity83]:
        return self.db.query(ResearchModelEntity83).offset(skip).limit(limit).all()

    def get_entity_83_by_id(self, entity_id: int) -> Optional[ResearchModelEntity83]:
        return self.db.query(ResearchModelEntity83).filter(ResearchModelEntity83.id == entity_id).first()

    def create_entity_83(self, payload: ResearchSchemaEntity83Create) -> ResearchModelEntity83:
        db_obj = ResearchModelEntity83(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_83(self, entity_id: int, payload: ResearchSchemaEntity83Update) -> Optional[ResearchModelEntity83]:
        db_obj = self.get_entity_83_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_83(self, entity_id: int) -> bool:
        db_obj = self.get_entity_83_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_84_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity84]:
        return self.db.query(ResearchModelEntity84).offset(skip).limit(limit).all()

    def get_entity_84_by_id(self, entity_id: int) -> Optional[ResearchModelEntity84]:
        return self.db.query(ResearchModelEntity84).filter(ResearchModelEntity84.id == entity_id).first()

    def create_entity_84(self, payload: ResearchSchemaEntity84Create) -> ResearchModelEntity84:
        db_obj = ResearchModelEntity84(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_84(self, entity_id: int, payload: ResearchSchemaEntity84Update) -> Optional[ResearchModelEntity84]:
        db_obj = self.get_entity_84_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_84(self, entity_id: int) -> bool:
        db_obj = self.get_entity_84_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_85_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity85]:
        return self.db.query(ResearchModelEntity85).offset(skip).limit(limit).all()

    def get_entity_85_by_id(self, entity_id: int) -> Optional[ResearchModelEntity85]:
        return self.db.query(ResearchModelEntity85).filter(ResearchModelEntity85.id == entity_id).first()

    def create_entity_85(self, payload: ResearchSchemaEntity85Create) -> ResearchModelEntity85:
        db_obj = ResearchModelEntity85(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_85(self, entity_id: int, payload: ResearchSchemaEntity85Update) -> Optional[ResearchModelEntity85]:
        db_obj = self.get_entity_85_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_85(self, entity_id: int) -> bool:
        db_obj = self.get_entity_85_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_86_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity86]:
        return self.db.query(ResearchModelEntity86).offset(skip).limit(limit).all()

    def get_entity_86_by_id(self, entity_id: int) -> Optional[ResearchModelEntity86]:
        return self.db.query(ResearchModelEntity86).filter(ResearchModelEntity86.id == entity_id).first()

    def create_entity_86(self, payload: ResearchSchemaEntity86Create) -> ResearchModelEntity86:
        db_obj = ResearchModelEntity86(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_86(self, entity_id: int, payload: ResearchSchemaEntity86Update) -> Optional[ResearchModelEntity86]:
        db_obj = self.get_entity_86_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_86(self, entity_id: int) -> bool:
        db_obj = self.get_entity_86_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_87_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity87]:
        return self.db.query(ResearchModelEntity87).offset(skip).limit(limit).all()

    def get_entity_87_by_id(self, entity_id: int) -> Optional[ResearchModelEntity87]:
        return self.db.query(ResearchModelEntity87).filter(ResearchModelEntity87.id == entity_id).first()

    def create_entity_87(self, payload: ResearchSchemaEntity87Create) -> ResearchModelEntity87:
        db_obj = ResearchModelEntity87(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_87(self, entity_id: int, payload: ResearchSchemaEntity87Update) -> Optional[ResearchModelEntity87]:
        db_obj = self.get_entity_87_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_87(self, entity_id: int) -> bool:
        db_obj = self.get_entity_87_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_88_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity88]:
        return self.db.query(ResearchModelEntity88).offset(skip).limit(limit).all()

    def get_entity_88_by_id(self, entity_id: int) -> Optional[ResearchModelEntity88]:
        return self.db.query(ResearchModelEntity88).filter(ResearchModelEntity88.id == entity_id).first()

    def create_entity_88(self, payload: ResearchSchemaEntity88Create) -> ResearchModelEntity88:
        db_obj = ResearchModelEntity88(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_88(self, entity_id: int, payload: ResearchSchemaEntity88Update) -> Optional[ResearchModelEntity88]:
        db_obj = self.get_entity_88_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_88(self, entity_id: int) -> bool:
        db_obj = self.get_entity_88_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_89_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity89]:
        return self.db.query(ResearchModelEntity89).offset(skip).limit(limit).all()

    def get_entity_89_by_id(self, entity_id: int) -> Optional[ResearchModelEntity89]:
        return self.db.query(ResearchModelEntity89).filter(ResearchModelEntity89.id == entity_id).first()

    def create_entity_89(self, payload: ResearchSchemaEntity89Create) -> ResearchModelEntity89:
        db_obj = ResearchModelEntity89(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_89(self, entity_id: int, payload: ResearchSchemaEntity89Update) -> Optional[ResearchModelEntity89]:
        db_obj = self.get_entity_89_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_89(self, entity_id: int) -> bool:
        db_obj = self.get_entity_89_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_90_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity90]:
        return self.db.query(ResearchModelEntity90).offset(skip).limit(limit).all()

    def get_entity_90_by_id(self, entity_id: int) -> Optional[ResearchModelEntity90]:
        return self.db.query(ResearchModelEntity90).filter(ResearchModelEntity90.id == entity_id).first()

    def create_entity_90(self, payload: ResearchSchemaEntity90Create) -> ResearchModelEntity90:
        db_obj = ResearchModelEntity90(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_90(self, entity_id: int, payload: ResearchSchemaEntity90Update) -> Optional[ResearchModelEntity90]:
        db_obj = self.get_entity_90_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_90(self, entity_id: int) -> bool:
        db_obj = self.get_entity_90_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_91_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity91]:
        return self.db.query(ResearchModelEntity91).offset(skip).limit(limit).all()

    def get_entity_91_by_id(self, entity_id: int) -> Optional[ResearchModelEntity91]:
        return self.db.query(ResearchModelEntity91).filter(ResearchModelEntity91.id == entity_id).first()

    def create_entity_91(self, payload: ResearchSchemaEntity91Create) -> ResearchModelEntity91:
        db_obj = ResearchModelEntity91(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_91(self, entity_id: int, payload: ResearchSchemaEntity91Update) -> Optional[ResearchModelEntity91]:
        db_obj = self.get_entity_91_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_91(self, entity_id: int) -> bool:
        db_obj = self.get_entity_91_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_92_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity92]:
        return self.db.query(ResearchModelEntity92).offset(skip).limit(limit).all()

    def get_entity_92_by_id(self, entity_id: int) -> Optional[ResearchModelEntity92]:
        return self.db.query(ResearchModelEntity92).filter(ResearchModelEntity92.id == entity_id).first()

    def create_entity_92(self, payload: ResearchSchemaEntity92Create) -> ResearchModelEntity92:
        db_obj = ResearchModelEntity92(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_92(self, entity_id: int, payload: ResearchSchemaEntity92Update) -> Optional[ResearchModelEntity92]:
        db_obj = self.get_entity_92_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_92(self, entity_id: int) -> bool:
        db_obj = self.get_entity_92_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_93_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity93]:
        return self.db.query(ResearchModelEntity93).offset(skip).limit(limit).all()

    def get_entity_93_by_id(self, entity_id: int) -> Optional[ResearchModelEntity93]:
        return self.db.query(ResearchModelEntity93).filter(ResearchModelEntity93.id == entity_id).first()

    def create_entity_93(self, payload: ResearchSchemaEntity93Create) -> ResearchModelEntity93:
        db_obj = ResearchModelEntity93(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_93(self, entity_id: int, payload: ResearchSchemaEntity93Update) -> Optional[ResearchModelEntity93]:
        db_obj = self.get_entity_93_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_93(self, entity_id: int) -> bool:
        db_obj = self.get_entity_93_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_94_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity94]:
        return self.db.query(ResearchModelEntity94).offset(skip).limit(limit).all()

    def get_entity_94_by_id(self, entity_id: int) -> Optional[ResearchModelEntity94]:
        return self.db.query(ResearchModelEntity94).filter(ResearchModelEntity94.id == entity_id).first()

    def create_entity_94(self, payload: ResearchSchemaEntity94Create) -> ResearchModelEntity94:
        db_obj = ResearchModelEntity94(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_94(self, entity_id: int, payload: ResearchSchemaEntity94Update) -> Optional[ResearchModelEntity94]:
        db_obj = self.get_entity_94_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_94(self, entity_id: int) -> bool:
        db_obj = self.get_entity_94_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_95_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity95]:
        return self.db.query(ResearchModelEntity95).offset(skip).limit(limit).all()

    def get_entity_95_by_id(self, entity_id: int) -> Optional[ResearchModelEntity95]:
        return self.db.query(ResearchModelEntity95).filter(ResearchModelEntity95.id == entity_id).first()

    def create_entity_95(self, payload: ResearchSchemaEntity95Create) -> ResearchModelEntity95:
        db_obj = ResearchModelEntity95(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_95(self, entity_id: int, payload: ResearchSchemaEntity95Update) -> Optional[ResearchModelEntity95]:
        db_obj = self.get_entity_95_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_95(self, entity_id: int) -> bool:
        db_obj = self.get_entity_95_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_96_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity96]:
        return self.db.query(ResearchModelEntity96).offset(skip).limit(limit).all()

    def get_entity_96_by_id(self, entity_id: int) -> Optional[ResearchModelEntity96]:
        return self.db.query(ResearchModelEntity96).filter(ResearchModelEntity96.id == entity_id).first()

    def create_entity_96(self, payload: ResearchSchemaEntity96Create) -> ResearchModelEntity96:
        db_obj = ResearchModelEntity96(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_96(self, entity_id: int, payload: ResearchSchemaEntity96Update) -> Optional[ResearchModelEntity96]:
        db_obj = self.get_entity_96_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_96(self, entity_id: int) -> bool:
        db_obj = self.get_entity_96_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_97_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity97]:
        return self.db.query(ResearchModelEntity97).offset(skip).limit(limit).all()

    def get_entity_97_by_id(self, entity_id: int) -> Optional[ResearchModelEntity97]:
        return self.db.query(ResearchModelEntity97).filter(ResearchModelEntity97.id == entity_id).first()

    def create_entity_97(self, payload: ResearchSchemaEntity97Create) -> ResearchModelEntity97:
        db_obj = ResearchModelEntity97(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_97(self, entity_id: int, payload: ResearchSchemaEntity97Update) -> Optional[ResearchModelEntity97]:
        db_obj = self.get_entity_97_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_97(self, entity_id: int) -> bool:
        db_obj = self.get_entity_97_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_98_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity98]:
        return self.db.query(ResearchModelEntity98).offset(skip).limit(limit).all()

    def get_entity_98_by_id(self, entity_id: int) -> Optional[ResearchModelEntity98]:
        return self.db.query(ResearchModelEntity98).filter(ResearchModelEntity98.id == entity_id).first()

    def create_entity_98(self, payload: ResearchSchemaEntity98Create) -> ResearchModelEntity98:
        db_obj = ResearchModelEntity98(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_98(self, entity_id: int, payload: ResearchSchemaEntity98Update) -> Optional[ResearchModelEntity98]:
        db_obj = self.get_entity_98_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_98(self, entity_id: int) -> bool:
        db_obj = self.get_entity_98_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_99_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity99]:
        return self.db.query(ResearchModelEntity99).offset(skip).limit(limit).all()

    def get_entity_99_by_id(self, entity_id: int) -> Optional[ResearchModelEntity99]:
        return self.db.query(ResearchModelEntity99).filter(ResearchModelEntity99.id == entity_id).first()

    def create_entity_99(self, payload: ResearchSchemaEntity99Create) -> ResearchModelEntity99:
        db_obj = ResearchModelEntity99(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_99(self, entity_id: int, payload: ResearchSchemaEntity99Update) -> Optional[ResearchModelEntity99]:
        db_obj = self.get_entity_99_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_99(self, entity_id: int) -> bool:
        db_obj = self.get_entity_99_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_100_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity100]:
        return self.db.query(ResearchModelEntity100).offset(skip).limit(limit).all()

    def get_entity_100_by_id(self, entity_id: int) -> Optional[ResearchModelEntity100]:
        return self.db.query(ResearchModelEntity100).filter(ResearchModelEntity100.id == entity_id).first()

    def create_entity_100(self, payload: ResearchSchemaEntity100Create) -> ResearchModelEntity100:
        db_obj = ResearchModelEntity100(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_100(self, entity_id: int, payload: ResearchSchemaEntity100Update) -> Optional[ResearchModelEntity100]:
        db_obj = self.get_entity_100_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_100(self, entity_id: int) -> bool:
        db_obj = self.get_entity_100_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_101_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity101]:
        return self.db.query(ResearchModelEntity101).offset(skip).limit(limit).all()

    def get_entity_101_by_id(self, entity_id: int) -> Optional[ResearchModelEntity101]:
        return self.db.query(ResearchModelEntity101).filter(ResearchModelEntity101.id == entity_id).first()

    def create_entity_101(self, payload: ResearchSchemaEntity101Create) -> ResearchModelEntity101:
        db_obj = ResearchModelEntity101(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_101(self, entity_id: int, payload: ResearchSchemaEntity101Update) -> Optional[ResearchModelEntity101]:
        db_obj = self.get_entity_101_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_101(self, entity_id: int) -> bool:
        db_obj = self.get_entity_101_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_102_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity102]:
        return self.db.query(ResearchModelEntity102).offset(skip).limit(limit).all()

    def get_entity_102_by_id(self, entity_id: int) -> Optional[ResearchModelEntity102]:
        return self.db.query(ResearchModelEntity102).filter(ResearchModelEntity102.id == entity_id).first()

    def create_entity_102(self, payload: ResearchSchemaEntity102Create) -> ResearchModelEntity102:
        db_obj = ResearchModelEntity102(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_102(self, entity_id: int, payload: ResearchSchemaEntity102Update) -> Optional[ResearchModelEntity102]:
        db_obj = self.get_entity_102_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_102(self, entity_id: int) -> bool:
        db_obj = self.get_entity_102_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_103_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity103]:
        return self.db.query(ResearchModelEntity103).offset(skip).limit(limit).all()

    def get_entity_103_by_id(self, entity_id: int) -> Optional[ResearchModelEntity103]:
        return self.db.query(ResearchModelEntity103).filter(ResearchModelEntity103.id == entity_id).first()

    def create_entity_103(self, payload: ResearchSchemaEntity103Create) -> ResearchModelEntity103:
        db_obj = ResearchModelEntity103(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_103(self, entity_id: int, payload: ResearchSchemaEntity103Update) -> Optional[ResearchModelEntity103]:
        db_obj = self.get_entity_103_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_103(self, entity_id: int) -> bool:
        db_obj = self.get_entity_103_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_104_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity104]:
        return self.db.query(ResearchModelEntity104).offset(skip).limit(limit).all()

    def get_entity_104_by_id(self, entity_id: int) -> Optional[ResearchModelEntity104]:
        return self.db.query(ResearchModelEntity104).filter(ResearchModelEntity104.id == entity_id).first()

    def create_entity_104(self, payload: ResearchSchemaEntity104Create) -> ResearchModelEntity104:
        db_obj = ResearchModelEntity104(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_104(self, entity_id: int, payload: ResearchSchemaEntity104Update) -> Optional[ResearchModelEntity104]:
        db_obj = self.get_entity_104_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_104(self, entity_id: int) -> bool:
        db_obj = self.get_entity_104_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_105_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity105]:
        return self.db.query(ResearchModelEntity105).offset(skip).limit(limit).all()

    def get_entity_105_by_id(self, entity_id: int) -> Optional[ResearchModelEntity105]:
        return self.db.query(ResearchModelEntity105).filter(ResearchModelEntity105.id == entity_id).first()

    def create_entity_105(self, payload: ResearchSchemaEntity105Create) -> ResearchModelEntity105:
        db_obj = ResearchModelEntity105(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_105(self, entity_id: int, payload: ResearchSchemaEntity105Update) -> Optional[ResearchModelEntity105]:
        db_obj = self.get_entity_105_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_105(self, entity_id: int) -> bool:
        db_obj = self.get_entity_105_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_106_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity106]:
        return self.db.query(ResearchModelEntity106).offset(skip).limit(limit).all()

    def get_entity_106_by_id(self, entity_id: int) -> Optional[ResearchModelEntity106]:
        return self.db.query(ResearchModelEntity106).filter(ResearchModelEntity106.id == entity_id).first()

    def create_entity_106(self, payload: ResearchSchemaEntity106Create) -> ResearchModelEntity106:
        db_obj = ResearchModelEntity106(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_106(self, entity_id: int, payload: ResearchSchemaEntity106Update) -> Optional[ResearchModelEntity106]:
        db_obj = self.get_entity_106_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_106(self, entity_id: int) -> bool:
        db_obj = self.get_entity_106_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_107_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity107]:
        return self.db.query(ResearchModelEntity107).offset(skip).limit(limit).all()

    def get_entity_107_by_id(self, entity_id: int) -> Optional[ResearchModelEntity107]:
        return self.db.query(ResearchModelEntity107).filter(ResearchModelEntity107.id == entity_id).first()

    def create_entity_107(self, payload: ResearchSchemaEntity107Create) -> ResearchModelEntity107:
        db_obj = ResearchModelEntity107(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_107(self, entity_id: int, payload: ResearchSchemaEntity107Update) -> Optional[ResearchModelEntity107]:
        db_obj = self.get_entity_107_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_107(self, entity_id: int) -> bool:
        db_obj = self.get_entity_107_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_108_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity108]:
        return self.db.query(ResearchModelEntity108).offset(skip).limit(limit).all()

    def get_entity_108_by_id(self, entity_id: int) -> Optional[ResearchModelEntity108]:
        return self.db.query(ResearchModelEntity108).filter(ResearchModelEntity108.id == entity_id).first()

    def create_entity_108(self, payload: ResearchSchemaEntity108Create) -> ResearchModelEntity108:
        db_obj = ResearchModelEntity108(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_108(self, entity_id: int, payload: ResearchSchemaEntity108Update) -> Optional[ResearchModelEntity108]:
        db_obj = self.get_entity_108_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_108(self, entity_id: int) -> bool:
        db_obj = self.get_entity_108_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_109_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity109]:
        return self.db.query(ResearchModelEntity109).offset(skip).limit(limit).all()

    def get_entity_109_by_id(self, entity_id: int) -> Optional[ResearchModelEntity109]:
        return self.db.query(ResearchModelEntity109).filter(ResearchModelEntity109.id == entity_id).first()

    def create_entity_109(self, payload: ResearchSchemaEntity109Create) -> ResearchModelEntity109:
        db_obj = ResearchModelEntity109(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_109(self, entity_id: int, payload: ResearchSchemaEntity109Update) -> Optional[ResearchModelEntity109]:
        db_obj = self.get_entity_109_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_109(self, entity_id: int) -> bool:
        db_obj = self.get_entity_109_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_110_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity110]:
        return self.db.query(ResearchModelEntity110).offset(skip).limit(limit).all()

    def get_entity_110_by_id(self, entity_id: int) -> Optional[ResearchModelEntity110]:
        return self.db.query(ResearchModelEntity110).filter(ResearchModelEntity110.id == entity_id).first()

    def create_entity_110(self, payload: ResearchSchemaEntity110Create) -> ResearchModelEntity110:
        db_obj = ResearchModelEntity110(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_110(self, entity_id: int, payload: ResearchSchemaEntity110Update) -> Optional[ResearchModelEntity110]:
        db_obj = self.get_entity_110_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_110(self, entity_id: int) -> bool:
        db_obj = self.get_entity_110_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_111_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity111]:
        return self.db.query(ResearchModelEntity111).offset(skip).limit(limit).all()

    def get_entity_111_by_id(self, entity_id: int) -> Optional[ResearchModelEntity111]:
        return self.db.query(ResearchModelEntity111).filter(ResearchModelEntity111.id == entity_id).first()

    def create_entity_111(self, payload: ResearchSchemaEntity111Create) -> ResearchModelEntity111:
        db_obj = ResearchModelEntity111(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_111(self, entity_id: int, payload: ResearchSchemaEntity111Update) -> Optional[ResearchModelEntity111]:
        db_obj = self.get_entity_111_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_111(self, entity_id: int) -> bool:
        db_obj = self.get_entity_111_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_112_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity112]:
        return self.db.query(ResearchModelEntity112).offset(skip).limit(limit).all()

    def get_entity_112_by_id(self, entity_id: int) -> Optional[ResearchModelEntity112]:
        return self.db.query(ResearchModelEntity112).filter(ResearchModelEntity112.id == entity_id).first()

    def create_entity_112(self, payload: ResearchSchemaEntity112Create) -> ResearchModelEntity112:
        db_obj = ResearchModelEntity112(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_112(self, entity_id: int, payload: ResearchSchemaEntity112Update) -> Optional[ResearchModelEntity112]:
        db_obj = self.get_entity_112_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_112(self, entity_id: int) -> bool:
        db_obj = self.get_entity_112_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_113_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity113]:
        return self.db.query(ResearchModelEntity113).offset(skip).limit(limit).all()

    def get_entity_113_by_id(self, entity_id: int) -> Optional[ResearchModelEntity113]:
        return self.db.query(ResearchModelEntity113).filter(ResearchModelEntity113.id == entity_id).first()

    def create_entity_113(self, payload: ResearchSchemaEntity113Create) -> ResearchModelEntity113:
        db_obj = ResearchModelEntity113(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_113(self, entity_id: int, payload: ResearchSchemaEntity113Update) -> Optional[ResearchModelEntity113]:
        db_obj = self.get_entity_113_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_113(self, entity_id: int) -> bool:
        db_obj = self.get_entity_113_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_114_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity114]:
        return self.db.query(ResearchModelEntity114).offset(skip).limit(limit).all()

    def get_entity_114_by_id(self, entity_id: int) -> Optional[ResearchModelEntity114]:
        return self.db.query(ResearchModelEntity114).filter(ResearchModelEntity114.id == entity_id).first()

    def create_entity_114(self, payload: ResearchSchemaEntity114Create) -> ResearchModelEntity114:
        db_obj = ResearchModelEntity114(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_114(self, entity_id: int, payload: ResearchSchemaEntity114Update) -> Optional[ResearchModelEntity114]:
        db_obj = self.get_entity_114_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_114(self, entity_id: int) -> bool:
        db_obj = self.get_entity_114_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_115_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity115]:
        return self.db.query(ResearchModelEntity115).offset(skip).limit(limit).all()

    def get_entity_115_by_id(self, entity_id: int) -> Optional[ResearchModelEntity115]:
        return self.db.query(ResearchModelEntity115).filter(ResearchModelEntity115.id == entity_id).first()

    def create_entity_115(self, payload: ResearchSchemaEntity115Create) -> ResearchModelEntity115:
        db_obj = ResearchModelEntity115(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_115(self, entity_id: int, payload: ResearchSchemaEntity115Update) -> Optional[ResearchModelEntity115]:
        db_obj = self.get_entity_115_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_115(self, entity_id: int) -> bool:
        db_obj = self.get_entity_115_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_116_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity116]:
        return self.db.query(ResearchModelEntity116).offset(skip).limit(limit).all()

    def get_entity_116_by_id(self, entity_id: int) -> Optional[ResearchModelEntity116]:
        return self.db.query(ResearchModelEntity116).filter(ResearchModelEntity116.id == entity_id).first()

    def create_entity_116(self, payload: ResearchSchemaEntity116Create) -> ResearchModelEntity116:
        db_obj = ResearchModelEntity116(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_116(self, entity_id: int, payload: ResearchSchemaEntity116Update) -> Optional[ResearchModelEntity116]:
        db_obj = self.get_entity_116_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_116(self, entity_id: int) -> bool:
        db_obj = self.get_entity_116_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_117_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity117]:
        return self.db.query(ResearchModelEntity117).offset(skip).limit(limit).all()

    def get_entity_117_by_id(self, entity_id: int) -> Optional[ResearchModelEntity117]:
        return self.db.query(ResearchModelEntity117).filter(ResearchModelEntity117.id == entity_id).first()

    def create_entity_117(self, payload: ResearchSchemaEntity117Create) -> ResearchModelEntity117:
        db_obj = ResearchModelEntity117(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_117(self, entity_id: int, payload: ResearchSchemaEntity117Update) -> Optional[ResearchModelEntity117]:
        db_obj = self.get_entity_117_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_117(self, entity_id: int) -> bool:
        db_obj = self.get_entity_117_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_118_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity118]:
        return self.db.query(ResearchModelEntity118).offset(skip).limit(limit).all()

    def get_entity_118_by_id(self, entity_id: int) -> Optional[ResearchModelEntity118]:
        return self.db.query(ResearchModelEntity118).filter(ResearchModelEntity118.id == entity_id).first()

    def create_entity_118(self, payload: ResearchSchemaEntity118Create) -> ResearchModelEntity118:
        db_obj = ResearchModelEntity118(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_118(self, entity_id: int, payload: ResearchSchemaEntity118Update) -> Optional[ResearchModelEntity118]:
        db_obj = self.get_entity_118_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_118(self, entity_id: int) -> bool:
        db_obj = self.get_entity_118_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_119_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity119]:
        return self.db.query(ResearchModelEntity119).offset(skip).limit(limit).all()

    def get_entity_119_by_id(self, entity_id: int) -> Optional[ResearchModelEntity119]:
        return self.db.query(ResearchModelEntity119).filter(ResearchModelEntity119.id == entity_id).first()

    def create_entity_119(self, payload: ResearchSchemaEntity119Create) -> ResearchModelEntity119:
        db_obj = ResearchModelEntity119(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_119(self, entity_id: int, payload: ResearchSchemaEntity119Update) -> Optional[ResearchModelEntity119]:
        db_obj = self.get_entity_119_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_119(self, entity_id: int) -> bool:
        db_obj = self.get_entity_119_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_120_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity120]:
        return self.db.query(ResearchModelEntity120).offset(skip).limit(limit).all()

    def get_entity_120_by_id(self, entity_id: int) -> Optional[ResearchModelEntity120]:
        return self.db.query(ResearchModelEntity120).filter(ResearchModelEntity120.id == entity_id).first()

    def create_entity_120(self, payload: ResearchSchemaEntity120Create) -> ResearchModelEntity120:
        db_obj = ResearchModelEntity120(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_120(self, entity_id: int, payload: ResearchSchemaEntity120Update) -> Optional[ResearchModelEntity120]:
        db_obj = self.get_entity_120_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_120(self, entity_id: int) -> bool:
        db_obj = self.get_entity_120_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_121_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity121]:
        return self.db.query(ResearchModelEntity121).offset(skip).limit(limit).all()

    def get_entity_121_by_id(self, entity_id: int) -> Optional[ResearchModelEntity121]:
        return self.db.query(ResearchModelEntity121).filter(ResearchModelEntity121.id == entity_id).first()

    def create_entity_121(self, payload: ResearchSchemaEntity121Create) -> ResearchModelEntity121:
        db_obj = ResearchModelEntity121(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_121(self, entity_id: int, payload: ResearchSchemaEntity121Update) -> Optional[ResearchModelEntity121]:
        db_obj = self.get_entity_121_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_121(self, entity_id: int) -> bool:
        db_obj = self.get_entity_121_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_122_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity122]:
        return self.db.query(ResearchModelEntity122).offset(skip).limit(limit).all()

    def get_entity_122_by_id(self, entity_id: int) -> Optional[ResearchModelEntity122]:
        return self.db.query(ResearchModelEntity122).filter(ResearchModelEntity122.id == entity_id).first()

    def create_entity_122(self, payload: ResearchSchemaEntity122Create) -> ResearchModelEntity122:
        db_obj = ResearchModelEntity122(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_122(self, entity_id: int, payload: ResearchSchemaEntity122Update) -> Optional[ResearchModelEntity122]:
        db_obj = self.get_entity_122_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_122(self, entity_id: int) -> bool:
        db_obj = self.get_entity_122_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_123_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity123]:
        return self.db.query(ResearchModelEntity123).offset(skip).limit(limit).all()

    def get_entity_123_by_id(self, entity_id: int) -> Optional[ResearchModelEntity123]:
        return self.db.query(ResearchModelEntity123).filter(ResearchModelEntity123.id == entity_id).first()

    def create_entity_123(self, payload: ResearchSchemaEntity123Create) -> ResearchModelEntity123:
        db_obj = ResearchModelEntity123(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_123(self, entity_id: int, payload: ResearchSchemaEntity123Update) -> Optional[ResearchModelEntity123]:
        db_obj = self.get_entity_123_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_123(self, entity_id: int) -> bool:
        db_obj = self.get_entity_123_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_124_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity124]:
        return self.db.query(ResearchModelEntity124).offset(skip).limit(limit).all()

    def get_entity_124_by_id(self, entity_id: int) -> Optional[ResearchModelEntity124]:
        return self.db.query(ResearchModelEntity124).filter(ResearchModelEntity124.id == entity_id).first()

    def create_entity_124(self, payload: ResearchSchemaEntity124Create) -> ResearchModelEntity124:
        db_obj = ResearchModelEntity124(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_124(self, entity_id: int, payload: ResearchSchemaEntity124Update) -> Optional[ResearchModelEntity124]:
        db_obj = self.get_entity_124_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_124(self, entity_id: int) -> bool:
        db_obj = self.get_entity_124_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_125_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity125]:
        return self.db.query(ResearchModelEntity125).offset(skip).limit(limit).all()

    def get_entity_125_by_id(self, entity_id: int) -> Optional[ResearchModelEntity125]:
        return self.db.query(ResearchModelEntity125).filter(ResearchModelEntity125.id == entity_id).first()

    def create_entity_125(self, payload: ResearchSchemaEntity125Create) -> ResearchModelEntity125:
        db_obj = ResearchModelEntity125(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_125(self, entity_id: int, payload: ResearchSchemaEntity125Update) -> Optional[ResearchModelEntity125]:
        db_obj = self.get_entity_125_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_125(self, entity_id: int) -> bool:
        db_obj = self.get_entity_125_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_126_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity126]:
        return self.db.query(ResearchModelEntity126).offset(skip).limit(limit).all()

    def get_entity_126_by_id(self, entity_id: int) -> Optional[ResearchModelEntity126]:
        return self.db.query(ResearchModelEntity126).filter(ResearchModelEntity126.id == entity_id).first()

    def create_entity_126(self, payload: ResearchSchemaEntity126Create) -> ResearchModelEntity126:
        db_obj = ResearchModelEntity126(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_126(self, entity_id: int, payload: ResearchSchemaEntity126Update) -> Optional[ResearchModelEntity126]:
        db_obj = self.get_entity_126_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_126(self, entity_id: int) -> bool:
        db_obj = self.get_entity_126_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_127_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity127]:
        return self.db.query(ResearchModelEntity127).offset(skip).limit(limit).all()

    def get_entity_127_by_id(self, entity_id: int) -> Optional[ResearchModelEntity127]:
        return self.db.query(ResearchModelEntity127).filter(ResearchModelEntity127.id == entity_id).first()

    def create_entity_127(self, payload: ResearchSchemaEntity127Create) -> ResearchModelEntity127:
        db_obj = ResearchModelEntity127(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_127(self, entity_id: int, payload: ResearchSchemaEntity127Update) -> Optional[ResearchModelEntity127]:
        db_obj = self.get_entity_127_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_127(self, entity_id: int) -> bool:
        db_obj = self.get_entity_127_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_128_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity128]:
        return self.db.query(ResearchModelEntity128).offset(skip).limit(limit).all()

    def get_entity_128_by_id(self, entity_id: int) -> Optional[ResearchModelEntity128]:
        return self.db.query(ResearchModelEntity128).filter(ResearchModelEntity128.id == entity_id).first()

    def create_entity_128(self, payload: ResearchSchemaEntity128Create) -> ResearchModelEntity128:
        db_obj = ResearchModelEntity128(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_128(self, entity_id: int, payload: ResearchSchemaEntity128Update) -> Optional[ResearchModelEntity128]:
        db_obj = self.get_entity_128_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_128(self, entity_id: int) -> bool:
        db_obj = self.get_entity_128_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_129_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity129]:
        return self.db.query(ResearchModelEntity129).offset(skip).limit(limit).all()

    def get_entity_129_by_id(self, entity_id: int) -> Optional[ResearchModelEntity129]:
        return self.db.query(ResearchModelEntity129).filter(ResearchModelEntity129.id == entity_id).first()

    def create_entity_129(self, payload: ResearchSchemaEntity129Create) -> ResearchModelEntity129:
        db_obj = ResearchModelEntity129(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_129(self, entity_id: int, payload: ResearchSchemaEntity129Update) -> Optional[ResearchModelEntity129]:
        db_obj = self.get_entity_129_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_129(self, entity_id: int) -> bool:
        db_obj = self.get_entity_129_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_130_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity130]:
        return self.db.query(ResearchModelEntity130).offset(skip).limit(limit).all()

    def get_entity_130_by_id(self, entity_id: int) -> Optional[ResearchModelEntity130]:
        return self.db.query(ResearchModelEntity130).filter(ResearchModelEntity130.id == entity_id).first()

    def create_entity_130(self, payload: ResearchSchemaEntity130Create) -> ResearchModelEntity130:
        db_obj = ResearchModelEntity130(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_130(self, entity_id: int, payload: ResearchSchemaEntity130Update) -> Optional[ResearchModelEntity130]:
        db_obj = self.get_entity_130_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_130(self, entity_id: int) -> bool:
        db_obj = self.get_entity_130_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_131_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity131]:
        return self.db.query(ResearchModelEntity131).offset(skip).limit(limit).all()

    def get_entity_131_by_id(self, entity_id: int) -> Optional[ResearchModelEntity131]:
        return self.db.query(ResearchModelEntity131).filter(ResearchModelEntity131.id == entity_id).first()

    def create_entity_131(self, payload: ResearchSchemaEntity131Create) -> ResearchModelEntity131:
        db_obj = ResearchModelEntity131(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_131(self, entity_id: int, payload: ResearchSchemaEntity131Update) -> Optional[ResearchModelEntity131]:
        db_obj = self.get_entity_131_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_131(self, entity_id: int) -> bool:
        db_obj = self.get_entity_131_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_132_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity132]:
        return self.db.query(ResearchModelEntity132).offset(skip).limit(limit).all()

    def get_entity_132_by_id(self, entity_id: int) -> Optional[ResearchModelEntity132]:
        return self.db.query(ResearchModelEntity132).filter(ResearchModelEntity132.id == entity_id).first()

    def create_entity_132(self, payload: ResearchSchemaEntity132Create) -> ResearchModelEntity132:
        db_obj = ResearchModelEntity132(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_132(self, entity_id: int, payload: ResearchSchemaEntity132Update) -> Optional[ResearchModelEntity132]:
        db_obj = self.get_entity_132_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_132(self, entity_id: int) -> bool:
        db_obj = self.get_entity_132_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_133_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity133]:
        return self.db.query(ResearchModelEntity133).offset(skip).limit(limit).all()

    def get_entity_133_by_id(self, entity_id: int) -> Optional[ResearchModelEntity133]:
        return self.db.query(ResearchModelEntity133).filter(ResearchModelEntity133.id == entity_id).first()

    def create_entity_133(self, payload: ResearchSchemaEntity133Create) -> ResearchModelEntity133:
        db_obj = ResearchModelEntity133(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_133(self, entity_id: int, payload: ResearchSchemaEntity133Update) -> Optional[ResearchModelEntity133]:
        db_obj = self.get_entity_133_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_133(self, entity_id: int) -> bool:
        db_obj = self.get_entity_133_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_134_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity134]:
        return self.db.query(ResearchModelEntity134).offset(skip).limit(limit).all()

    def get_entity_134_by_id(self, entity_id: int) -> Optional[ResearchModelEntity134]:
        return self.db.query(ResearchModelEntity134).filter(ResearchModelEntity134.id == entity_id).first()

    def create_entity_134(self, payload: ResearchSchemaEntity134Create) -> ResearchModelEntity134:
        db_obj = ResearchModelEntity134(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_134(self, entity_id: int, payload: ResearchSchemaEntity134Update) -> Optional[ResearchModelEntity134]:
        db_obj = self.get_entity_134_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_134(self, entity_id: int) -> bool:
        db_obj = self.get_entity_134_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_135_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity135]:
        return self.db.query(ResearchModelEntity135).offset(skip).limit(limit).all()

    def get_entity_135_by_id(self, entity_id: int) -> Optional[ResearchModelEntity135]:
        return self.db.query(ResearchModelEntity135).filter(ResearchModelEntity135.id == entity_id).first()

    def create_entity_135(self, payload: ResearchSchemaEntity135Create) -> ResearchModelEntity135:
        db_obj = ResearchModelEntity135(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_135(self, entity_id: int, payload: ResearchSchemaEntity135Update) -> Optional[ResearchModelEntity135]:
        db_obj = self.get_entity_135_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_135(self, entity_id: int) -> bool:
        db_obj = self.get_entity_135_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_136_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity136]:
        return self.db.query(ResearchModelEntity136).offset(skip).limit(limit).all()

    def get_entity_136_by_id(self, entity_id: int) -> Optional[ResearchModelEntity136]:
        return self.db.query(ResearchModelEntity136).filter(ResearchModelEntity136.id == entity_id).first()

    def create_entity_136(self, payload: ResearchSchemaEntity136Create) -> ResearchModelEntity136:
        db_obj = ResearchModelEntity136(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_136(self, entity_id: int, payload: ResearchSchemaEntity136Update) -> Optional[ResearchModelEntity136]:
        db_obj = self.get_entity_136_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_136(self, entity_id: int) -> bool:
        db_obj = self.get_entity_136_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_137_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity137]:
        return self.db.query(ResearchModelEntity137).offset(skip).limit(limit).all()

    def get_entity_137_by_id(self, entity_id: int) -> Optional[ResearchModelEntity137]:
        return self.db.query(ResearchModelEntity137).filter(ResearchModelEntity137.id == entity_id).first()

    def create_entity_137(self, payload: ResearchSchemaEntity137Create) -> ResearchModelEntity137:
        db_obj = ResearchModelEntity137(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_137(self, entity_id: int, payload: ResearchSchemaEntity137Update) -> Optional[ResearchModelEntity137]:
        db_obj = self.get_entity_137_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_137(self, entity_id: int) -> bool:
        db_obj = self.get_entity_137_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_138_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity138]:
        return self.db.query(ResearchModelEntity138).offset(skip).limit(limit).all()

    def get_entity_138_by_id(self, entity_id: int) -> Optional[ResearchModelEntity138]:
        return self.db.query(ResearchModelEntity138).filter(ResearchModelEntity138.id == entity_id).first()

    def create_entity_138(self, payload: ResearchSchemaEntity138Create) -> ResearchModelEntity138:
        db_obj = ResearchModelEntity138(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_138(self, entity_id: int, payload: ResearchSchemaEntity138Update) -> Optional[ResearchModelEntity138]:
        db_obj = self.get_entity_138_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_138(self, entity_id: int) -> bool:
        db_obj = self.get_entity_138_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_139_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity139]:
        return self.db.query(ResearchModelEntity139).offset(skip).limit(limit).all()

    def get_entity_139_by_id(self, entity_id: int) -> Optional[ResearchModelEntity139]:
        return self.db.query(ResearchModelEntity139).filter(ResearchModelEntity139.id == entity_id).first()

    def create_entity_139(self, payload: ResearchSchemaEntity139Create) -> ResearchModelEntity139:
        db_obj = ResearchModelEntity139(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_139(self, entity_id: int, payload: ResearchSchemaEntity139Update) -> Optional[ResearchModelEntity139]:
        db_obj = self.get_entity_139_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_139(self, entity_id: int) -> bool:
        db_obj = self.get_entity_139_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_140_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity140]:
        return self.db.query(ResearchModelEntity140).offset(skip).limit(limit).all()

    def get_entity_140_by_id(self, entity_id: int) -> Optional[ResearchModelEntity140]:
        return self.db.query(ResearchModelEntity140).filter(ResearchModelEntity140.id == entity_id).first()

    def create_entity_140(self, payload: ResearchSchemaEntity140Create) -> ResearchModelEntity140:
        db_obj = ResearchModelEntity140(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_140(self, entity_id: int, payload: ResearchSchemaEntity140Update) -> Optional[ResearchModelEntity140]:
        db_obj = self.get_entity_140_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_140(self, entity_id: int) -> bool:
        db_obj = self.get_entity_140_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_141_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity141]:
        return self.db.query(ResearchModelEntity141).offset(skip).limit(limit).all()

    def get_entity_141_by_id(self, entity_id: int) -> Optional[ResearchModelEntity141]:
        return self.db.query(ResearchModelEntity141).filter(ResearchModelEntity141.id == entity_id).first()

    def create_entity_141(self, payload: ResearchSchemaEntity141Create) -> ResearchModelEntity141:
        db_obj = ResearchModelEntity141(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_141(self, entity_id: int, payload: ResearchSchemaEntity141Update) -> Optional[ResearchModelEntity141]:
        db_obj = self.get_entity_141_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_141(self, entity_id: int) -> bool:
        db_obj = self.get_entity_141_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_142_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity142]:
        return self.db.query(ResearchModelEntity142).offset(skip).limit(limit).all()

    def get_entity_142_by_id(self, entity_id: int) -> Optional[ResearchModelEntity142]:
        return self.db.query(ResearchModelEntity142).filter(ResearchModelEntity142.id == entity_id).first()

    def create_entity_142(self, payload: ResearchSchemaEntity142Create) -> ResearchModelEntity142:
        db_obj = ResearchModelEntity142(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_142(self, entity_id: int, payload: ResearchSchemaEntity142Update) -> Optional[ResearchModelEntity142]:
        db_obj = self.get_entity_142_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_142(self, entity_id: int) -> bool:
        db_obj = self.get_entity_142_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_143_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity143]:
        return self.db.query(ResearchModelEntity143).offset(skip).limit(limit).all()

    def get_entity_143_by_id(self, entity_id: int) -> Optional[ResearchModelEntity143]:
        return self.db.query(ResearchModelEntity143).filter(ResearchModelEntity143.id == entity_id).first()

    def create_entity_143(self, payload: ResearchSchemaEntity143Create) -> ResearchModelEntity143:
        db_obj = ResearchModelEntity143(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_143(self, entity_id: int, payload: ResearchSchemaEntity143Update) -> Optional[ResearchModelEntity143]:
        db_obj = self.get_entity_143_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_143(self, entity_id: int) -> bool:
        db_obj = self.get_entity_143_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_144_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity144]:
        return self.db.query(ResearchModelEntity144).offset(skip).limit(limit).all()

    def get_entity_144_by_id(self, entity_id: int) -> Optional[ResearchModelEntity144]:
        return self.db.query(ResearchModelEntity144).filter(ResearchModelEntity144.id == entity_id).first()

    def create_entity_144(self, payload: ResearchSchemaEntity144Create) -> ResearchModelEntity144:
        db_obj = ResearchModelEntity144(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_144(self, entity_id: int, payload: ResearchSchemaEntity144Update) -> Optional[ResearchModelEntity144]:
        db_obj = self.get_entity_144_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_144(self, entity_id: int) -> bool:
        db_obj = self.get_entity_144_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_145_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity145]:
        return self.db.query(ResearchModelEntity145).offset(skip).limit(limit).all()

    def get_entity_145_by_id(self, entity_id: int) -> Optional[ResearchModelEntity145]:
        return self.db.query(ResearchModelEntity145).filter(ResearchModelEntity145.id == entity_id).first()

    def create_entity_145(self, payload: ResearchSchemaEntity145Create) -> ResearchModelEntity145:
        db_obj = ResearchModelEntity145(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_145(self, entity_id: int, payload: ResearchSchemaEntity145Update) -> Optional[ResearchModelEntity145]:
        db_obj = self.get_entity_145_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_145(self, entity_id: int) -> bool:
        db_obj = self.get_entity_145_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_146_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity146]:
        return self.db.query(ResearchModelEntity146).offset(skip).limit(limit).all()

    def get_entity_146_by_id(self, entity_id: int) -> Optional[ResearchModelEntity146]:
        return self.db.query(ResearchModelEntity146).filter(ResearchModelEntity146.id == entity_id).first()

    def create_entity_146(self, payload: ResearchSchemaEntity146Create) -> ResearchModelEntity146:
        db_obj = ResearchModelEntity146(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_146(self, entity_id: int, payload: ResearchSchemaEntity146Update) -> Optional[ResearchModelEntity146]:
        db_obj = self.get_entity_146_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_146(self, entity_id: int) -> bool:
        db_obj = self.get_entity_146_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_147_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity147]:
        return self.db.query(ResearchModelEntity147).offset(skip).limit(limit).all()

    def get_entity_147_by_id(self, entity_id: int) -> Optional[ResearchModelEntity147]:
        return self.db.query(ResearchModelEntity147).filter(ResearchModelEntity147.id == entity_id).first()

    def create_entity_147(self, payload: ResearchSchemaEntity147Create) -> ResearchModelEntity147:
        db_obj = ResearchModelEntity147(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_147(self, entity_id: int, payload: ResearchSchemaEntity147Update) -> Optional[ResearchModelEntity147]:
        db_obj = self.get_entity_147_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_147(self, entity_id: int) -> bool:
        db_obj = self.get_entity_147_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_148_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity148]:
        return self.db.query(ResearchModelEntity148).offset(skip).limit(limit).all()

    def get_entity_148_by_id(self, entity_id: int) -> Optional[ResearchModelEntity148]:
        return self.db.query(ResearchModelEntity148).filter(ResearchModelEntity148.id == entity_id).first()

    def create_entity_148(self, payload: ResearchSchemaEntity148Create) -> ResearchModelEntity148:
        db_obj = ResearchModelEntity148(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_148(self, entity_id: int, payload: ResearchSchemaEntity148Update) -> Optional[ResearchModelEntity148]:
        db_obj = self.get_entity_148_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_148(self, entity_id: int) -> bool:
        db_obj = self.get_entity_148_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_149_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity149]:
        return self.db.query(ResearchModelEntity149).offset(skip).limit(limit).all()

    def get_entity_149_by_id(self, entity_id: int) -> Optional[ResearchModelEntity149]:
        return self.db.query(ResearchModelEntity149).filter(ResearchModelEntity149.id == entity_id).first()

    def create_entity_149(self, payload: ResearchSchemaEntity149Create) -> ResearchModelEntity149:
        db_obj = ResearchModelEntity149(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_149(self, entity_id: int, payload: ResearchSchemaEntity149Update) -> Optional[ResearchModelEntity149]:
        db_obj = self.get_entity_149_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_149(self, entity_id: int) -> bool:
        db_obj = self.get_entity_149_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_150_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity150]:
        return self.db.query(ResearchModelEntity150).offset(skip).limit(limit).all()

    def get_entity_150_by_id(self, entity_id: int) -> Optional[ResearchModelEntity150]:
        return self.db.query(ResearchModelEntity150).filter(ResearchModelEntity150.id == entity_id).first()

    def create_entity_150(self, payload: ResearchSchemaEntity150Create) -> ResearchModelEntity150:
        db_obj = ResearchModelEntity150(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_150(self, entity_id: int, payload: ResearchSchemaEntity150Update) -> Optional[ResearchModelEntity150]:
        db_obj = self.get_entity_150_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_150(self, entity_id: int) -> bool:
        db_obj = self.get_entity_150_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_151_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity151]:
        return self.db.query(ResearchModelEntity151).offset(skip).limit(limit).all()

    def get_entity_151_by_id(self, entity_id: int) -> Optional[ResearchModelEntity151]:
        return self.db.query(ResearchModelEntity151).filter(ResearchModelEntity151.id == entity_id).first()

    def create_entity_151(self, payload: ResearchSchemaEntity151Create) -> ResearchModelEntity151:
        db_obj = ResearchModelEntity151(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_151(self, entity_id: int, payload: ResearchSchemaEntity151Update) -> Optional[ResearchModelEntity151]:
        db_obj = self.get_entity_151_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_151(self, entity_id: int) -> bool:
        db_obj = self.get_entity_151_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_152_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity152]:
        return self.db.query(ResearchModelEntity152).offset(skip).limit(limit).all()

    def get_entity_152_by_id(self, entity_id: int) -> Optional[ResearchModelEntity152]:
        return self.db.query(ResearchModelEntity152).filter(ResearchModelEntity152.id == entity_id).first()

    def create_entity_152(self, payload: ResearchSchemaEntity152Create) -> ResearchModelEntity152:
        db_obj = ResearchModelEntity152(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_152(self, entity_id: int, payload: ResearchSchemaEntity152Update) -> Optional[ResearchModelEntity152]:
        db_obj = self.get_entity_152_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_152(self, entity_id: int) -> bool:
        db_obj = self.get_entity_152_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_153_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity153]:
        return self.db.query(ResearchModelEntity153).offset(skip).limit(limit).all()

    def get_entity_153_by_id(self, entity_id: int) -> Optional[ResearchModelEntity153]:
        return self.db.query(ResearchModelEntity153).filter(ResearchModelEntity153.id == entity_id).first()

    def create_entity_153(self, payload: ResearchSchemaEntity153Create) -> ResearchModelEntity153:
        db_obj = ResearchModelEntity153(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_153(self, entity_id: int, payload: ResearchSchemaEntity153Update) -> Optional[ResearchModelEntity153]:
        db_obj = self.get_entity_153_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_153(self, entity_id: int) -> bool:
        db_obj = self.get_entity_153_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_154_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity154]:
        return self.db.query(ResearchModelEntity154).offset(skip).limit(limit).all()

    def get_entity_154_by_id(self, entity_id: int) -> Optional[ResearchModelEntity154]:
        return self.db.query(ResearchModelEntity154).filter(ResearchModelEntity154.id == entity_id).first()

    def create_entity_154(self, payload: ResearchSchemaEntity154Create) -> ResearchModelEntity154:
        db_obj = ResearchModelEntity154(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_154(self, entity_id: int, payload: ResearchSchemaEntity154Update) -> Optional[ResearchModelEntity154]:
        db_obj = self.get_entity_154_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_154(self, entity_id: int) -> bool:
        db_obj = self.get_entity_154_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_155_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity155]:
        return self.db.query(ResearchModelEntity155).offset(skip).limit(limit).all()

    def get_entity_155_by_id(self, entity_id: int) -> Optional[ResearchModelEntity155]:
        return self.db.query(ResearchModelEntity155).filter(ResearchModelEntity155.id == entity_id).first()

    def create_entity_155(self, payload: ResearchSchemaEntity155Create) -> ResearchModelEntity155:
        db_obj = ResearchModelEntity155(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_155(self, entity_id: int, payload: ResearchSchemaEntity155Update) -> Optional[ResearchModelEntity155]:
        db_obj = self.get_entity_155_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_155(self, entity_id: int) -> bool:
        db_obj = self.get_entity_155_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_156_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity156]:
        return self.db.query(ResearchModelEntity156).offset(skip).limit(limit).all()

    def get_entity_156_by_id(self, entity_id: int) -> Optional[ResearchModelEntity156]:
        return self.db.query(ResearchModelEntity156).filter(ResearchModelEntity156.id == entity_id).first()

    def create_entity_156(self, payload: ResearchSchemaEntity156Create) -> ResearchModelEntity156:
        db_obj = ResearchModelEntity156(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_156(self, entity_id: int, payload: ResearchSchemaEntity156Update) -> Optional[ResearchModelEntity156]:
        db_obj = self.get_entity_156_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_156(self, entity_id: int) -> bool:
        db_obj = self.get_entity_156_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_157_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity157]:
        return self.db.query(ResearchModelEntity157).offset(skip).limit(limit).all()

    def get_entity_157_by_id(self, entity_id: int) -> Optional[ResearchModelEntity157]:
        return self.db.query(ResearchModelEntity157).filter(ResearchModelEntity157.id == entity_id).first()

    def create_entity_157(self, payload: ResearchSchemaEntity157Create) -> ResearchModelEntity157:
        db_obj = ResearchModelEntity157(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_157(self, entity_id: int, payload: ResearchSchemaEntity157Update) -> Optional[ResearchModelEntity157]:
        db_obj = self.get_entity_157_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_157(self, entity_id: int) -> bool:
        db_obj = self.get_entity_157_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_158_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity158]:
        return self.db.query(ResearchModelEntity158).offset(skip).limit(limit).all()

    def get_entity_158_by_id(self, entity_id: int) -> Optional[ResearchModelEntity158]:
        return self.db.query(ResearchModelEntity158).filter(ResearchModelEntity158.id == entity_id).first()

    def create_entity_158(self, payload: ResearchSchemaEntity158Create) -> ResearchModelEntity158:
        db_obj = ResearchModelEntity158(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_158(self, entity_id: int, payload: ResearchSchemaEntity158Update) -> Optional[ResearchModelEntity158]:
        db_obj = self.get_entity_158_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_158(self, entity_id: int) -> bool:
        db_obj = self.get_entity_158_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_159_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity159]:
        return self.db.query(ResearchModelEntity159).offset(skip).limit(limit).all()

    def get_entity_159_by_id(self, entity_id: int) -> Optional[ResearchModelEntity159]:
        return self.db.query(ResearchModelEntity159).filter(ResearchModelEntity159.id == entity_id).first()

    def create_entity_159(self, payload: ResearchSchemaEntity159Create) -> ResearchModelEntity159:
        db_obj = ResearchModelEntity159(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_159(self, entity_id: int, payload: ResearchSchemaEntity159Update) -> Optional[ResearchModelEntity159]:
        db_obj = self.get_entity_159_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_159(self, entity_id: int) -> bool:
        db_obj = self.get_entity_159_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_160_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity160]:
        return self.db.query(ResearchModelEntity160).offset(skip).limit(limit).all()

    def get_entity_160_by_id(self, entity_id: int) -> Optional[ResearchModelEntity160]:
        return self.db.query(ResearchModelEntity160).filter(ResearchModelEntity160.id == entity_id).first()

    def create_entity_160(self, payload: ResearchSchemaEntity160Create) -> ResearchModelEntity160:
        db_obj = ResearchModelEntity160(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_160(self, entity_id: int, payload: ResearchSchemaEntity160Update) -> Optional[ResearchModelEntity160]:
        db_obj = self.get_entity_160_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_160(self, entity_id: int) -> bool:
        db_obj = self.get_entity_160_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_161_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity161]:
        return self.db.query(ResearchModelEntity161).offset(skip).limit(limit).all()

    def get_entity_161_by_id(self, entity_id: int) -> Optional[ResearchModelEntity161]:
        return self.db.query(ResearchModelEntity161).filter(ResearchModelEntity161.id == entity_id).first()

    def create_entity_161(self, payload: ResearchSchemaEntity161Create) -> ResearchModelEntity161:
        db_obj = ResearchModelEntity161(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_161(self, entity_id: int, payload: ResearchSchemaEntity161Update) -> Optional[ResearchModelEntity161]:
        db_obj = self.get_entity_161_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_161(self, entity_id: int) -> bool:
        db_obj = self.get_entity_161_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_162_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity162]:
        return self.db.query(ResearchModelEntity162).offset(skip).limit(limit).all()

    def get_entity_162_by_id(self, entity_id: int) -> Optional[ResearchModelEntity162]:
        return self.db.query(ResearchModelEntity162).filter(ResearchModelEntity162.id == entity_id).first()

    def create_entity_162(self, payload: ResearchSchemaEntity162Create) -> ResearchModelEntity162:
        db_obj = ResearchModelEntity162(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_162(self, entity_id: int, payload: ResearchSchemaEntity162Update) -> Optional[ResearchModelEntity162]:
        db_obj = self.get_entity_162_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_162(self, entity_id: int) -> bool:
        db_obj = self.get_entity_162_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_163_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity163]:
        return self.db.query(ResearchModelEntity163).offset(skip).limit(limit).all()

    def get_entity_163_by_id(self, entity_id: int) -> Optional[ResearchModelEntity163]:
        return self.db.query(ResearchModelEntity163).filter(ResearchModelEntity163.id == entity_id).first()

    def create_entity_163(self, payload: ResearchSchemaEntity163Create) -> ResearchModelEntity163:
        db_obj = ResearchModelEntity163(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_163(self, entity_id: int, payload: ResearchSchemaEntity163Update) -> Optional[ResearchModelEntity163]:
        db_obj = self.get_entity_163_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_163(self, entity_id: int) -> bool:
        db_obj = self.get_entity_163_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_164_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity164]:
        return self.db.query(ResearchModelEntity164).offset(skip).limit(limit).all()

    def get_entity_164_by_id(self, entity_id: int) -> Optional[ResearchModelEntity164]:
        return self.db.query(ResearchModelEntity164).filter(ResearchModelEntity164.id == entity_id).first()

    def create_entity_164(self, payload: ResearchSchemaEntity164Create) -> ResearchModelEntity164:
        db_obj = ResearchModelEntity164(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_164(self, entity_id: int, payload: ResearchSchemaEntity164Update) -> Optional[ResearchModelEntity164]:
        db_obj = self.get_entity_164_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_164(self, entity_id: int) -> bool:
        db_obj = self.get_entity_164_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_165_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity165]:
        return self.db.query(ResearchModelEntity165).offset(skip).limit(limit).all()

    def get_entity_165_by_id(self, entity_id: int) -> Optional[ResearchModelEntity165]:
        return self.db.query(ResearchModelEntity165).filter(ResearchModelEntity165.id == entity_id).first()

    def create_entity_165(self, payload: ResearchSchemaEntity165Create) -> ResearchModelEntity165:
        db_obj = ResearchModelEntity165(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_165(self, entity_id: int, payload: ResearchSchemaEntity165Update) -> Optional[ResearchModelEntity165]:
        db_obj = self.get_entity_165_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_165(self, entity_id: int) -> bool:
        db_obj = self.get_entity_165_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_166_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity166]:
        return self.db.query(ResearchModelEntity166).offset(skip).limit(limit).all()

    def get_entity_166_by_id(self, entity_id: int) -> Optional[ResearchModelEntity166]:
        return self.db.query(ResearchModelEntity166).filter(ResearchModelEntity166.id == entity_id).first()

    def create_entity_166(self, payload: ResearchSchemaEntity166Create) -> ResearchModelEntity166:
        db_obj = ResearchModelEntity166(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_166(self, entity_id: int, payload: ResearchSchemaEntity166Update) -> Optional[ResearchModelEntity166]:
        db_obj = self.get_entity_166_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_166(self, entity_id: int) -> bool:
        db_obj = self.get_entity_166_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_167_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity167]:
        return self.db.query(ResearchModelEntity167).offset(skip).limit(limit).all()

    def get_entity_167_by_id(self, entity_id: int) -> Optional[ResearchModelEntity167]:
        return self.db.query(ResearchModelEntity167).filter(ResearchModelEntity167.id == entity_id).first()

    def create_entity_167(self, payload: ResearchSchemaEntity167Create) -> ResearchModelEntity167:
        db_obj = ResearchModelEntity167(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_167(self, entity_id: int, payload: ResearchSchemaEntity167Update) -> Optional[ResearchModelEntity167]:
        db_obj = self.get_entity_167_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_167(self, entity_id: int) -> bool:
        db_obj = self.get_entity_167_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_168_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity168]:
        return self.db.query(ResearchModelEntity168).offset(skip).limit(limit).all()

    def get_entity_168_by_id(self, entity_id: int) -> Optional[ResearchModelEntity168]:
        return self.db.query(ResearchModelEntity168).filter(ResearchModelEntity168.id == entity_id).first()

    def create_entity_168(self, payload: ResearchSchemaEntity168Create) -> ResearchModelEntity168:
        db_obj = ResearchModelEntity168(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_168(self, entity_id: int, payload: ResearchSchemaEntity168Update) -> Optional[ResearchModelEntity168]:
        db_obj = self.get_entity_168_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_168(self, entity_id: int) -> bool:
        db_obj = self.get_entity_168_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_169_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity169]:
        return self.db.query(ResearchModelEntity169).offset(skip).limit(limit).all()

    def get_entity_169_by_id(self, entity_id: int) -> Optional[ResearchModelEntity169]:
        return self.db.query(ResearchModelEntity169).filter(ResearchModelEntity169.id == entity_id).first()

    def create_entity_169(self, payload: ResearchSchemaEntity169Create) -> ResearchModelEntity169:
        db_obj = ResearchModelEntity169(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_169(self, entity_id: int, payload: ResearchSchemaEntity169Update) -> Optional[ResearchModelEntity169]:
        db_obj = self.get_entity_169_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_169(self, entity_id: int) -> bool:
        db_obj = self.get_entity_169_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_170_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity170]:
        return self.db.query(ResearchModelEntity170).offset(skip).limit(limit).all()

    def get_entity_170_by_id(self, entity_id: int) -> Optional[ResearchModelEntity170]:
        return self.db.query(ResearchModelEntity170).filter(ResearchModelEntity170.id == entity_id).first()

    def create_entity_170(self, payload: ResearchSchemaEntity170Create) -> ResearchModelEntity170:
        db_obj = ResearchModelEntity170(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_170(self, entity_id: int, payload: ResearchSchemaEntity170Update) -> Optional[ResearchModelEntity170]:
        db_obj = self.get_entity_170_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_170(self, entity_id: int) -> bool:
        db_obj = self.get_entity_170_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_171_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity171]:
        return self.db.query(ResearchModelEntity171).offset(skip).limit(limit).all()

    def get_entity_171_by_id(self, entity_id: int) -> Optional[ResearchModelEntity171]:
        return self.db.query(ResearchModelEntity171).filter(ResearchModelEntity171.id == entity_id).first()

    def create_entity_171(self, payload: ResearchSchemaEntity171Create) -> ResearchModelEntity171:
        db_obj = ResearchModelEntity171(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_171(self, entity_id: int, payload: ResearchSchemaEntity171Update) -> Optional[ResearchModelEntity171]:
        db_obj = self.get_entity_171_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_171(self, entity_id: int) -> bool:
        db_obj = self.get_entity_171_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_172_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity172]:
        return self.db.query(ResearchModelEntity172).offset(skip).limit(limit).all()

    def get_entity_172_by_id(self, entity_id: int) -> Optional[ResearchModelEntity172]:
        return self.db.query(ResearchModelEntity172).filter(ResearchModelEntity172.id == entity_id).first()

    def create_entity_172(self, payload: ResearchSchemaEntity172Create) -> ResearchModelEntity172:
        db_obj = ResearchModelEntity172(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_172(self, entity_id: int, payload: ResearchSchemaEntity172Update) -> Optional[ResearchModelEntity172]:
        db_obj = self.get_entity_172_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_172(self, entity_id: int) -> bool:
        db_obj = self.get_entity_172_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_173_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity173]:
        return self.db.query(ResearchModelEntity173).offset(skip).limit(limit).all()

    def get_entity_173_by_id(self, entity_id: int) -> Optional[ResearchModelEntity173]:
        return self.db.query(ResearchModelEntity173).filter(ResearchModelEntity173.id == entity_id).first()

    def create_entity_173(self, payload: ResearchSchemaEntity173Create) -> ResearchModelEntity173:
        db_obj = ResearchModelEntity173(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_173(self, entity_id: int, payload: ResearchSchemaEntity173Update) -> Optional[ResearchModelEntity173]:
        db_obj = self.get_entity_173_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_173(self, entity_id: int) -> bool:
        db_obj = self.get_entity_173_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_174_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity174]:
        return self.db.query(ResearchModelEntity174).offset(skip).limit(limit).all()

    def get_entity_174_by_id(self, entity_id: int) -> Optional[ResearchModelEntity174]:
        return self.db.query(ResearchModelEntity174).filter(ResearchModelEntity174.id == entity_id).first()

    def create_entity_174(self, payload: ResearchSchemaEntity174Create) -> ResearchModelEntity174:
        db_obj = ResearchModelEntity174(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_174(self, entity_id: int, payload: ResearchSchemaEntity174Update) -> Optional[ResearchModelEntity174]:
        db_obj = self.get_entity_174_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_174(self, entity_id: int) -> bool:
        db_obj = self.get_entity_174_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_175_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity175]:
        return self.db.query(ResearchModelEntity175).offset(skip).limit(limit).all()

    def get_entity_175_by_id(self, entity_id: int) -> Optional[ResearchModelEntity175]:
        return self.db.query(ResearchModelEntity175).filter(ResearchModelEntity175.id == entity_id).first()

    def create_entity_175(self, payload: ResearchSchemaEntity175Create) -> ResearchModelEntity175:
        db_obj = ResearchModelEntity175(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_175(self, entity_id: int, payload: ResearchSchemaEntity175Update) -> Optional[ResearchModelEntity175]:
        db_obj = self.get_entity_175_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_175(self, entity_id: int) -> bool:
        db_obj = self.get_entity_175_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_176_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity176]:
        return self.db.query(ResearchModelEntity176).offset(skip).limit(limit).all()

    def get_entity_176_by_id(self, entity_id: int) -> Optional[ResearchModelEntity176]:
        return self.db.query(ResearchModelEntity176).filter(ResearchModelEntity176.id == entity_id).first()

    def create_entity_176(self, payload: ResearchSchemaEntity176Create) -> ResearchModelEntity176:
        db_obj = ResearchModelEntity176(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_176(self, entity_id: int, payload: ResearchSchemaEntity176Update) -> Optional[ResearchModelEntity176]:
        db_obj = self.get_entity_176_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_176(self, entity_id: int) -> bool:
        db_obj = self.get_entity_176_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_177_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity177]:
        return self.db.query(ResearchModelEntity177).offset(skip).limit(limit).all()

    def get_entity_177_by_id(self, entity_id: int) -> Optional[ResearchModelEntity177]:
        return self.db.query(ResearchModelEntity177).filter(ResearchModelEntity177.id == entity_id).first()

    def create_entity_177(self, payload: ResearchSchemaEntity177Create) -> ResearchModelEntity177:
        db_obj = ResearchModelEntity177(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_177(self, entity_id: int, payload: ResearchSchemaEntity177Update) -> Optional[ResearchModelEntity177]:
        db_obj = self.get_entity_177_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_177(self, entity_id: int) -> bool:
        db_obj = self.get_entity_177_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_178_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity178]:
        return self.db.query(ResearchModelEntity178).offset(skip).limit(limit).all()

    def get_entity_178_by_id(self, entity_id: int) -> Optional[ResearchModelEntity178]:
        return self.db.query(ResearchModelEntity178).filter(ResearchModelEntity178.id == entity_id).first()

    def create_entity_178(self, payload: ResearchSchemaEntity178Create) -> ResearchModelEntity178:
        db_obj = ResearchModelEntity178(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_178(self, entity_id: int, payload: ResearchSchemaEntity178Update) -> Optional[ResearchModelEntity178]:
        db_obj = self.get_entity_178_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_178(self, entity_id: int) -> bool:
        db_obj = self.get_entity_178_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_179_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity179]:
        return self.db.query(ResearchModelEntity179).offset(skip).limit(limit).all()

    def get_entity_179_by_id(self, entity_id: int) -> Optional[ResearchModelEntity179]:
        return self.db.query(ResearchModelEntity179).filter(ResearchModelEntity179.id == entity_id).first()

    def create_entity_179(self, payload: ResearchSchemaEntity179Create) -> ResearchModelEntity179:
        db_obj = ResearchModelEntity179(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_179(self, entity_id: int, payload: ResearchSchemaEntity179Update) -> Optional[ResearchModelEntity179]:
        db_obj = self.get_entity_179_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_179(self, entity_id: int) -> bool:
        db_obj = self.get_entity_179_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_180_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity180]:
        return self.db.query(ResearchModelEntity180).offset(skip).limit(limit).all()

    def get_entity_180_by_id(self, entity_id: int) -> Optional[ResearchModelEntity180]:
        return self.db.query(ResearchModelEntity180).filter(ResearchModelEntity180.id == entity_id).first()

    def create_entity_180(self, payload: ResearchSchemaEntity180Create) -> ResearchModelEntity180:
        db_obj = ResearchModelEntity180(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_180(self, entity_id: int, payload: ResearchSchemaEntity180Update) -> Optional[ResearchModelEntity180]:
        db_obj = self.get_entity_180_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_180(self, entity_id: int) -> bool:
        db_obj = self.get_entity_180_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_181_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity181]:
        return self.db.query(ResearchModelEntity181).offset(skip).limit(limit).all()

    def get_entity_181_by_id(self, entity_id: int) -> Optional[ResearchModelEntity181]:
        return self.db.query(ResearchModelEntity181).filter(ResearchModelEntity181.id == entity_id).first()

    def create_entity_181(self, payload: ResearchSchemaEntity181Create) -> ResearchModelEntity181:
        db_obj = ResearchModelEntity181(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_181(self, entity_id: int, payload: ResearchSchemaEntity181Update) -> Optional[ResearchModelEntity181]:
        db_obj = self.get_entity_181_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_181(self, entity_id: int) -> bool:
        db_obj = self.get_entity_181_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_182_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity182]:
        return self.db.query(ResearchModelEntity182).offset(skip).limit(limit).all()

    def get_entity_182_by_id(self, entity_id: int) -> Optional[ResearchModelEntity182]:
        return self.db.query(ResearchModelEntity182).filter(ResearchModelEntity182.id == entity_id).first()

    def create_entity_182(self, payload: ResearchSchemaEntity182Create) -> ResearchModelEntity182:
        db_obj = ResearchModelEntity182(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_182(self, entity_id: int, payload: ResearchSchemaEntity182Update) -> Optional[ResearchModelEntity182]:
        db_obj = self.get_entity_182_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_182(self, entity_id: int) -> bool:
        db_obj = self.get_entity_182_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_183_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity183]:
        return self.db.query(ResearchModelEntity183).offset(skip).limit(limit).all()

    def get_entity_183_by_id(self, entity_id: int) -> Optional[ResearchModelEntity183]:
        return self.db.query(ResearchModelEntity183).filter(ResearchModelEntity183.id == entity_id).first()

    def create_entity_183(self, payload: ResearchSchemaEntity183Create) -> ResearchModelEntity183:
        db_obj = ResearchModelEntity183(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_183(self, entity_id: int, payload: ResearchSchemaEntity183Update) -> Optional[ResearchModelEntity183]:
        db_obj = self.get_entity_183_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_183(self, entity_id: int) -> bool:
        db_obj = self.get_entity_183_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_184_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity184]:
        return self.db.query(ResearchModelEntity184).offset(skip).limit(limit).all()

    def get_entity_184_by_id(self, entity_id: int) -> Optional[ResearchModelEntity184]:
        return self.db.query(ResearchModelEntity184).filter(ResearchModelEntity184.id == entity_id).first()

    def create_entity_184(self, payload: ResearchSchemaEntity184Create) -> ResearchModelEntity184:
        db_obj = ResearchModelEntity184(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_184(self, entity_id: int, payload: ResearchSchemaEntity184Update) -> Optional[ResearchModelEntity184]:
        db_obj = self.get_entity_184_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_184(self, entity_id: int) -> bool:
        db_obj = self.get_entity_184_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_185_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity185]:
        return self.db.query(ResearchModelEntity185).offset(skip).limit(limit).all()

    def get_entity_185_by_id(self, entity_id: int) -> Optional[ResearchModelEntity185]:
        return self.db.query(ResearchModelEntity185).filter(ResearchModelEntity185.id == entity_id).first()

    def create_entity_185(self, payload: ResearchSchemaEntity185Create) -> ResearchModelEntity185:
        db_obj = ResearchModelEntity185(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_185(self, entity_id: int, payload: ResearchSchemaEntity185Update) -> Optional[ResearchModelEntity185]:
        db_obj = self.get_entity_185_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_185(self, entity_id: int) -> bool:
        db_obj = self.get_entity_185_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_186_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity186]:
        return self.db.query(ResearchModelEntity186).offset(skip).limit(limit).all()

    def get_entity_186_by_id(self, entity_id: int) -> Optional[ResearchModelEntity186]:
        return self.db.query(ResearchModelEntity186).filter(ResearchModelEntity186.id == entity_id).first()

    def create_entity_186(self, payload: ResearchSchemaEntity186Create) -> ResearchModelEntity186:
        db_obj = ResearchModelEntity186(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_186(self, entity_id: int, payload: ResearchSchemaEntity186Update) -> Optional[ResearchModelEntity186]:
        db_obj = self.get_entity_186_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_186(self, entity_id: int) -> bool:
        db_obj = self.get_entity_186_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_187_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity187]:
        return self.db.query(ResearchModelEntity187).offset(skip).limit(limit).all()

    def get_entity_187_by_id(self, entity_id: int) -> Optional[ResearchModelEntity187]:
        return self.db.query(ResearchModelEntity187).filter(ResearchModelEntity187.id == entity_id).first()

    def create_entity_187(self, payload: ResearchSchemaEntity187Create) -> ResearchModelEntity187:
        db_obj = ResearchModelEntity187(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_187(self, entity_id: int, payload: ResearchSchemaEntity187Update) -> Optional[ResearchModelEntity187]:
        db_obj = self.get_entity_187_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_187(self, entity_id: int) -> bool:
        db_obj = self.get_entity_187_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_188_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity188]:
        return self.db.query(ResearchModelEntity188).offset(skip).limit(limit).all()

    def get_entity_188_by_id(self, entity_id: int) -> Optional[ResearchModelEntity188]:
        return self.db.query(ResearchModelEntity188).filter(ResearchModelEntity188.id == entity_id).first()

    def create_entity_188(self, payload: ResearchSchemaEntity188Create) -> ResearchModelEntity188:
        db_obj = ResearchModelEntity188(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_188(self, entity_id: int, payload: ResearchSchemaEntity188Update) -> Optional[ResearchModelEntity188]:
        db_obj = self.get_entity_188_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_188(self, entity_id: int) -> bool:
        db_obj = self.get_entity_188_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_189_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity189]:
        return self.db.query(ResearchModelEntity189).offset(skip).limit(limit).all()

    def get_entity_189_by_id(self, entity_id: int) -> Optional[ResearchModelEntity189]:
        return self.db.query(ResearchModelEntity189).filter(ResearchModelEntity189.id == entity_id).first()

    def create_entity_189(self, payload: ResearchSchemaEntity189Create) -> ResearchModelEntity189:
        db_obj = ResearchModelEntity189(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_189(self, entity_id: int, payload: ResearchSchemaEntity189Update) -> Optional[ResearchModelEntity189]:
        db_obj = self.get_entity_189_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_189(self, entity_id: int) -> bool:
        db_obj = self.get_entity_189_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_190_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity190]:
        return self.db.query(ResearchModelEntity190).offset(skip).limit(limit).all()

    def get_entity_190_by_id(self, entity_id: int) -> Optional[ResearchModelEntity190]:
        return self.db.query(ResearchModelEntity190).filter(ResearchModelEntity190.id == entity_id).first()

    def create_entity_190(self, payload: ResearchSchemaEntity190Create) -> ResearchModelEntity190:
        db_obj = ResearchModelEntity190(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_190(self, entity_id: int, payload: ResearchSchemaEntity190Update) -> Optional[ResearchModelEntity190]:
        db_obj = self.get_entity_190_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_190(self, entity_id: int) -> bool:
        db_obj = self.get_entity_190_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_191_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity191]:
        return self.db.query(ResearchModelEntity191).offset(skip).limit(limit).all()

    def get_entity_191_by_id(self, entity_id: int) -> Optional[ResearchModelEntity191]:
        return self.db.query(ResearchModelEntity191).filter(ResearchModelEntity191.id == entity_id).first()

    def create_entity_191(self, payload: ResearchSchemaEntity191Create) -> ResearchModelEntity191:
        db_obj = ResearchModelEntity191(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_191(self, entity_id: int, payload: ResearchSchemaEntity191Update) -> Optional[ResearchModelEntity191]:
        db_obj = self.get_entity_191_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_191(self, entity_id: int) -> bool:
        db_obj = self.get_entity_191_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_192_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity192]:
        return self.db.query(ResearchModelEntity192).offset(skip).limit(limit).all()

    def get_entity_192_by_id(self, entity_id: int) -> Optional[ResearchModelEntity192]:
        return self.db.query(ResearchModelEntity192).filter(ResearchModelEntity192.id == entity_id).first()

    def create_entity_192(self, payload: ResearchSchemaEntity192Create) -> ResearchModelEntity192:
        db_obj = ResearchModelEntity192(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_192(self, entity_id: int, payload: ResearchSchemaEntity192Update) -> Optional[ResearchModelEntity192]:
        db_obj = self.get_entity_192_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_192(self, entity_id: int) -> bool:
        db_obj = self.get_entity_192_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_193_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity193]:
        return self.db.query(ResearchModelEntity193).offset(skip).limit(limit).all()

    def get_entity_193_by_id(self, entity_id: int) -> Optional[ResearchModelEntity193]:
        return self.db.query(ResearchModelEntity193).filter(ResearchModelEntity193.id == entity_id).first()

    def create_entity_193(self, payload: ResearchSchemaEntity193Create) -> ResearchModelEntity193:
        db_obj = ResearchModelEntity193(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_193(self, entity_id: int, payload: ResearchSchemaEntity193Update) -> Optional[ResearchModelEntity193]:
        db_obj = self.get_entity_193_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_193(self, entity_id: int) -> bool:
        db_obj = self.get_entity_193_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_194_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity194]:
        return self.db.query(ResearchModelEntity194).offset(skip).limit(limit).all()

    def get_entity_194_by_id(self, entity_id: int) -> Optional[ResearchModelEntity194]:
        return self.db.query(ResearchModelEntity194).filter(ResearchModelEntity194.id == entity_id).first()

    def create_entity_194(self, payload: ResearchSchemaEntity194Create) -> ResearchModelEntity194:
        db_obj = ResearchModelEntity194(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_194(self, entity_id: int, payload: ResearchSchemaEntity194Update) -> Optional[ResearchModelEntity194]:
        db_obj = self.get_entity_194_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_194(self, entity_id: int) -> bool:
        db_obj = self.get_entity_194_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_195_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity195]:
        return self.db.query(ResearchModelEntity195).offset(skip).limit(limit).all()

    def get_entity_195_by_id(self, entity_id: int) -> Optional[ResearchModelEntity195]:
        return self.db.query(ResearchModelEntity195).filter(ResearchModelEntity195.id == entity_id).first()

    def create_entity_195(self, payload: ResearchSchemaEntity195Create) -> ResearchModelEntity195:
        db_obj = ResearchModelEntity195(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_195(self, entity_id: int, payload: ResearchSchemaEntity195Update) -> Optional[ResearchModelEntity195]:
        db_obj = self.get_entity_195_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_195(self, entity_id: int) -> bool:
        db_obj = self.get_entity_195_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_196_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity196]:
        return self.db.query(ResearchModelEntity196).offset(skip).limit(limit).all()

    def get_entity_196_by_id(self, entity_id: int) -> Optional[ResearchModelEntity196]:
        return self.db.query(ResearchModelEntity196).filter(ResearchModelEntity196.id == entity_id).first()

    def create_entity_196(self, payload: ResearchSchemaEntity196Create) -> ResearchModelEntity196:
        db_obj = ResearchModelEntity196(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_196(self, entity_id: int, payload: ResearchSchemaEntity196Update) -> Optional[ResearchModelEntity196]:
        db_obj = self.get_entity_196_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_196(self, entity_id: int) -> bool:
        db_obj = self.get_entity_196_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_197_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity197]:
        return self.db.query(ResearchModelEntity197).offset(skip).limit(limit).all()

    def get_entity_197_by_id(self, entity_id: int) -> Optional[ResearchModelEntity197]:
        return self.db.query(ResearchModelEntity197).filter(ResearchModelEntity197.id == entity_id).first()

    def create_entity_197(self, payload: ResearchSchemaEntity197Create) -> ResearchModelEntity197:
        db_obj = ResearchModelEntity197(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_197(self, entity_id: int, payload: ResearchSchemaEntity197Update) -> Optional[ResearchModelEntity197]:
        db_obj = self.get_entity_197_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_197(self, entity_id: int) -> bool:
        db_obj = self.get_entity_197_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_198_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity198]:
        return self.db.query(ResearchModelEntity198).offset(skip).limit(limit).all()

    def get_entity_198_by_id(self, entity_id: int) -> Optional[ResearchModelEntity198]:
        return self.db.query(ResearchModelEntity198).filter(ResearchModelEntity198.id == entity_id).first()

    def create_entity_198(self, payload: ResearchSchemaEntity198Create) -> ResearchModelEntity198:
        db_obj = ResearchModelEntity198(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_198(self, entity_id: int, payload: ResearchSchemaEntity198Update) -> Optional[ResearchModelEntity198]:
        db_obj = self.get_entity_198_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_198(self, entity_id: int) -> bool:
        db_obj = self.get_entity_198_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_199_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity199]:
        return self.db.query(ResearchModelEntity199).offset(skip).limit(limit).all()

    def get_entity_199_by_id(self, entity_id: int) -> Optional[ResearchModelEntity199]:
        return self.db.query(ResearchModelEntity199).filter(ResearchModelEntity199.id == entity_id).first()

    def create_entity_199(self, payload: ResearchSchemaEntity199Create) -> ResearchModelEntity199:
        db_obj = ResearchModelEntity199(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_199(self, entity_id: int, payload: ResearchSchemaEntity199Update) -> Optional[ResearchModelEntity199]:
        db_obj = self.get_entity_199_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_199(self, entity_id: int) -> bool:
        db_obj = self.get_entity_199_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_200_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity200]:
        return self.db.query(ResearchModelEntity200).offset(skip).limit(limit).all()

    def get_entity_200_by_id(self, entity_id: int) -> Optional[ResearchModelEntity200]:
        return self.db.query(ResearchModelEntity200).filter(ResearchModelEntity200.id == entity_id).first()

    def create_entity_200(self, payload: ResearchSchemaEntity200Create) -> ResearchModelEntity200:
        db_obj = ResearchModelEntity200(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_200(self, entity_id: int, payload: ResearchSchemaEntity200Update) -> Optional[ResearchModelEntity200]:
        db_obj = self.get_entity_200_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_200(self, entity_id: int) -> bool:
        db_obj = self.get_entity_200_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_201_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity201]:
        return self.db.query(ResearchModelEntity201).offset(skip).limit(limit).all()

    def get_entity_201_by_id(self, entity_id: int) -> Optional[ResearchModelEntity201]:
        return self.db.query(ResearchModelEntity201).filter(ResearchModelEntity201.id == entity_id).first()

    def create_entity_201(self, payload: ResearchSchemaEntity201Create) -> ResearchModelEntity201:
        db_obj = ResearchModelEntity201(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_201(self, entity_id: int, payload: ResearchSchemaEntity201Update) -> Optional[ResearchModelEntity201]:
        db_obj = self.get_entity_201_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_201(self, entity_id: int) -> bool:
        db_obj = self.get_entity_201_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_202_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity202]:
        return self.db.query(ResearchModelEntity202).offset(skip).limit(limit).all()

    def get_entity_202_by_id(self, entity_id: int) -> Optional[ResearchModelEntity202]:
        return self.db.query(ResearchModelEntity202).filter(ResearchModelEntity202.id == entity_id).first()

    def create_entity_202(self, payload: ResearchSchemaEntity202Create) -> ResearchModelEntity202:
        db_obj = ResearchModelEntity202(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_202(self, entity_id: int, payload: ResearchSchemaEntity202Update) -> Optional[ResearchModelEntity202]:
        db_obj = self.get_entity_202_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_202(self, entity_id: int) -> bool:
        db_obj = self.get_entity_202_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_203_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity203]:
        return self.db.query(ResearchModelEntity203).offset(skip).limit(limit).all()

    def get_entity_203_by_id(self, entity_id: int) -> Optional[ResearchModelEntity203]:
        return self.db.query(ResearchModelEntity203).filter(ResearchModelEntity203.id == entity_id).first()

    def create_entity_203(self, payload: ResearchSchemaEntity203Create) -> ResearchModelEntity203:
        db_obj = ResearchModelEntity203(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_203(self, entity_id: int, payload: ResearchSchemaEntity203Update) -> Optional[ResearchModelEntity203]:
        db_obj = self.get_entity_203_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_203(self, entity_id: int) -> bool:
        db_obj = self.get_entity_203_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_204_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity204]:
        return self.db.query(ResearchModelEntity204).offset(skip).limit(limit).all()

    def get_entity_204_by_id(self, entity_id: int) -> Optional[ResearchModelEntity204]:
        return self.db.query(ResearchModelEntity204).filter(ResearchModelEntity204.id == entity_id).first()

    def create_entity_204(self, payload: ResearchSchemaEntity204Create) -> ResearchModelEntity204:
        db_obj = ResearchModelEntity204(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_204(self, entity_id: int, payload: ResearchSchemaEntity204Update) -> Optional[ResearchModelEntity204]:
        db_obj = self.get_entity_204_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_204(self, entity_id: int) -> bool:
        db_obj = self.get_entity_204_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_205_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity205]:
        return self.db.query(ResearchModelEntity205).offset(skip).limit(limit).all()

    def get_entity_205_by_id(self, entity_id: int) -> Optional[ResearchModelEntity205]:
        return self.db.query(ResearchModelEntity205).filter(ResearchModelEntity205.id == entity_id).first()

    def create_entity_205(self, payload: ResearchSchemaEntity205Create) -> ResearchModelEntity205:
        db_obj = ResearchModelEntity205(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_205(self, entity_id: int, payload: ResearchSchemaEntity205Update) -> Optional[ResearchModelEntity205]:
        db_obj = self.get_entity_205_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_205(self, entity_id: int) -> bool:
        db_obj = self.get_entity_205_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_206_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity206]:
        return self.db.query(ResearchModelEntity206).offset(skip).limit(limit).all()

    def get_entity_206_by_id(self, entity_id: int) -> Optional[ResearchModelEntity206]:
        return self.db.query(ResearchModelEntity206).filter(ResearchModelEntity206.id == entity_id).first()

    def create_entity_206(self, payload: ResearchSchemaEntity206Create) -> ResearchModelEntity206:
        db_obj = ResearchModelEntity206(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_206(self, entity_id: int, payload: ResearchSchemaEntity206Update) -> Optional[ResearchModelEntity206]:
        db_obj = self.get_entity_206_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_206(self, entity_id: int) -> bool:
        db_obj = self.get_entity_206_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_207_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity207]:
        return self.db.query(ResearchModelEntity207).offset(skip).limit(limit).all()

    def get_entity_207_by_id(self, entity_id: int) -> Optional[ResearchModelEntity207]:
        return self.db.query(ResearchModelEntity207).filter(ResearchModelEntity207.id == entity_id).first()

    def create_entity_207(self, payload: ResearchSchemaEntity207Create) -> ResearchModelEntity207:
        db_obj = ResearchModelEntity207(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_207(self, entity_id: int, payload: ResearchSchemaEntity207Update) -> Optional[ResearchModelEntity207]:
        db_obj = self.get_entity_207_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_207(self, entity_id: int) -> bool:
        db_obj = self.get_entity_207_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_208_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity208]:
        return self.db.query(ResearchModelEntity208).offset(skip).limit(limit).all()

    def get_entity_208_by_id(self, entity_id: int) -> Optional[ResearchModelEntity208]:
        return self.db.query(ResearchModelEntity208).filter(ResearchModelEntity208.id == entity_id).first()

    def create_entity_208(self, payload: ResearchSchemaEntity208Create) -> ResearchModelEntity208:
        db_obj = ResearchModelEntity208(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_208(self, entity_id: int, payload: ResearchSchemaEntity208Update) -> Optional[ResearchModelEntity208]:
        db_obj = self.get_entity_208_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_208(self, entity_id: int) -> bool:
        db_obj = self.get_entity_208_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_209_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity209]:
        return self.db.query(ResearchModelEntity209).offset(skip).limit(limit).all()

    def get_entity_209_by_id(self, entity_id: int) -> Optional[ResearchModelEntity209]:
        return self.db.query(ResearchModelEntity209).filter(ResearchModelEntity209.id == entity_id).first()

    def create_entity_209(self, payload: ResearchSchemaEntity209Create) -> ResearchModelEntity209:
        db_obj = ResearchModelEntity209(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_209(self, entity_id: int, payload: ResearchSchemaEntity209Update) -> Optional[ResearchModelEntity209]:
        db_obj = self.get_entity_209_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_209(self, entity_id: int) -> bool:
        db_obj = self.get_entity_209_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_210_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity210]:
        return self.db.query(ResearchModelEntity210).offset(skip).limit(limit).all()

    def get_entity_210_by_id(self, entity_id: int) -> Optional[ResearchModelEntity210]:
        return self.db.query(ResearchModelEntity210).filter(ResearchModelEntity210.id == entity_id).first()

    def create_entity_210(self, payload: ResearchSchemaEntity210Create) -> ResearchModelEntity210:
        db_obj = ResearchModelEntity210(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_210(self, entity_id: int, payload: ResearchSchemaEntity210Update) -> Optional[ResearchModelEntity210]:
        db_obj = self.get_entity_210_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_210(self, entity_id: int) -> bool:
        db_obj = self.get_entity_210_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_211_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity211]:
        return self.db.query(ResearchModelEntity211).offset(skip).limit(limit).all()

    def get_entity_211_by_id(self, entity_id: int) -> Optional[ResearchModelEntity211]:
        return self.db.query(ResearchModelEntity211).filter(ResearchModelEntity211.id == entity_id).first()

    def create_entity_211(self, payload: ResearchSchemaEntity211Create) -> ResearchModelEntity211:
        db_obj = ResearchModelEntity211(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_211(self, entity_id: int, payload: ResearchSchemaEntity211Update) -> Optional[ResearchModelEntity211]:
        db_obj = self.get_entity_211_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_211(self, entity_id: int) -> bool:
        db_obj = self.get_entity_211_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_212_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity212]:
        return self.db.query(ResearchModelEntity212).offset(skip).limit(limit).all()

    def get_entity_212_by_id(self, entity_id: int) -> Optional[ResearchModelEntity212]:
        return self.db.query(ResearchModelEntity212).filter(ResearchModelEntity212.id == entity_id).first()

    def create_entity_212(self, payload: ResearchSchemaEntity212Create) -> ResearchModelEntity212:
        db_obj = ResearchModelEntity212(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_212(self, entity_id: int, payload: ResearchSchemaEntity212Update) -> Optional[ResearchModelEntity212]:
        db_obj = self.get_entity_212_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_212(self, entity_id: int) -> bool:
        db_obj = self.get_entity_212_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_213_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity213]:
        return self.db.query(ResearchModelEntity213).offset(skip).limit(limit).all()

    def get_entity_213_by_id(self, entity_id: int) -> Optional[ResearchModelEntity213]:
        return self.db.query(ResearchModelEntity213).filter(ResearchModelEntity213.id == entity_id).first()

    def create_entity_213(self, payload: ResearchSchemaEntity213Create) -> ResearchModelEntity213:
        db_obj = ResearchModelEntity213(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_213(self, entity_id: int, payload: ResearchSchemaEntity213Update) -> Optional[ResearchModelEntity213]:
        db_obj = self.get_entity_213_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_213(self, entity_id: int) -> bool:
        db_obj = self.get_entity_213_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_214_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity214]:
        return self.db.query(ResearchModelEntity214).offset(skip).limit(limit).all()

    def get_entity_214_by_id(self, entity_id: int) -> Optional[ResearchModelEntity214]:
        return self.db.query(ResearchModelEntity214).filter(ResearchModelEntity214.id == entity_id).first()

    def create_entity_214(self, payload: ResearchSchemaEntity214Create) -> ResearchModelEntity214:
        db_obj = ResearchModelEntity214(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_214(self, entity_id: int, payload: ResearchSchemaEntity214Update) -> Optional[ResearchModelEntity214]:
        db_obj = self.get_entity_214_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_214(self, entity_id: int) -> bool:
        db_obj = self.get_entity_214_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_215_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity215]:
        return self.db.query(ResearchModelEntity215).offset(skip).limit(limit).all()

    def get_entity_215_by_id(self, entity_id: int) -> Optional[ResearchModelEntity215]:
        return self.db.query(ResearchModelEntity215).filter(ResearchModelEntity215.id == entity_id).first()

    def create_entity_215(self, payload: ResearchSchemaEntity215Create) -> ResearchModelEntity215:
        db_obj = ResearchModelEntity215(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_215(self, entity_id: int, payload: ResearchSchemaEntity215Update) -> Optional[ResearchModelEntity215]:
        db_obj = self.get_entity_215_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_215(self, entity_id: int) -> bool:
        db_obj = self.get_entity_215_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_216_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity216]:
        return self.db.query(ResearchModelEntity216).offset(skip).limit(limit).all()

    def get_entity_216_by_id(self, entity_id: int) -> Optional[ResearchModelEntity216]:
        return self.db.query(ResearchModelEntity216).filter(ResearchModelEntity216.id == entity_id).first()

    def create_entity_216(self, payload: ResearchSchemaEntity216Create) -> ResearchModelEntity216:
        db_obj = ResearchModelEntity216(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_216(self, entity_id: int, payload: ResearchSchemaEntity216Update) -> Optional[ResearchModelEntity216]:
        db_obj = self.get_entity_216_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_216(self, entity_id: int) -> bool:
        db_obj = self.get_entity_216_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_217_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity217]:
        return self.db.query(ResearchModelEntity217).offset(skip).limit(limit).all()

    def get_entity_217_by_id(self, entity_id: int) -> Optional[ResearchModelEntity217]:
        return self.db.query(ResearchModelEntity217).filter(ResearchModelEntity217.id == entity_id).first()

    def create_entity_217(self, payload: ResearchSchemaEntity217Create) -> ResearchModelEntity217:
        db_obj = ResearchModelEntity217(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_217(self, entity_id: int, payload: ResearchSchemaEntity217Update) -> Optional[ResearchModelEntity217]:
        db_obj = self.get_entity_217_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_217(self, entity_id: int) -> bool:
        db_obj = self.get_entity_217_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_218_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity218]:
        return self.db.query(ResearchModelEntity218).offset(skip).limit(limit).all()

    def get_entity_218_by_id(self, entity_id: int) -> Optional[ResearchModelEntity218]:
        return self.db.query(ResearchModelEntity218).filter(ResearchModelEntity218.id == entity_id).first()

    def create_entity_218(self, payload: ResearchSchemaEntity218Create) -> ResearchModelEntity218:
        db_obj = ResearchModelEntity218(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_218(self, entity_id: int, payload: ResearchSchemaEntity218Update) -> Optional[ResearchModelEntity218]:
        db_obj = self.get_entity_218_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_218(self, entity_id: int) -> bool:
        db_obj = self.get_entity_218_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_219_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity219]:
        return self.db.query(ResearchModelEntity219).offset(skip).limit(limit).all()

    def get_entity_219_by_id(self, entity_id: int) -> Optional[ResearchModelEntity219]:
        return self.db.query(ResearchModelEntity219).filter(ResearchModelEntity219.id == entity_id).first()

    def create_entity_219(self, payload: ResearchSchemaEntity219Create) -> ResearchModelEntity219:
        db_obj = ResearchModelEntity219(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_219(self, entity_id: int, payload: ResearchSchemaEntity219Update) -> Optional[ResearchModelEntity219]:
        db_obj = self.get_entity_219_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_219(self, entity_id: int) -> bool:
        db_obj = self.get_entity_219_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_220_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity220]:
        return self.db.query(ResearchModelEntity220).offset(skip).limit(limit).all()

    def get_entity_220_by_id(self, entity_id: int) -> Optional[ResearchModelEntity220]:
        return self.db.query(ResearchModelEntity220).filter(ResearchModelEntity220.id == entity_id).first()

    def create_entity_220(self, payload: ResearchSchemaEntity220Create) -> ResearchModelEntity220:
        db_obj = ResearchModelEntity220(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_220(self, entity_id: int, payload: ResearchSchemaEntity220Update) -> Optional[ResearchModelEntity220]:
        db_obj = self.get_entity_220_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_220(self, entity_id: int) -> bool:
        db_obj = self.get_entity_220_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_221_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity221]:
        return self.db.query(ResearchModelEntity221).offset(skip).limit(limit).all()

    def get_entity_221_by_id(self, entity_id: int) -> Optional[ResearchModelEntity221]:
        return self.db.query(ResearchModelEntity221).filter(ResearchModelEntity221.id == entity_id).first()

    def create_entity_221(self, payload: ResearchSchemaEntity221Create) -> ResearchModelEntity221:
        db_obj = ResearchModelEntity221(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_221(self, entity_id: int, payload: ResearchSchemaEntity221Update) -> Optional[ResearchModelEntity221]:
        db_obj = self.get_entity_221_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_221(self, entity_id: int) -> bool:
        db_obj = self.get_entity_221_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_222_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity222]:
        return self.db.query(ResearchModelEntity222).offset(skip).limit(limit).all()

    def get_entity_222_by_id(self, entity_id: int) -> Optional[ResearchModelEntity222]:
        return self.db.query(ResearchModelEntity222).filter(ResearchModelEntity222.id == entity_id).first()

    def create_entity_222(self, payload: ResearchSchemaEntity222Create) -> ResearchModelEntity222:
        db_obj = ResearchModelEntity222(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_222(self, entity_id: int, payload: ResearchSchemaEntity222Update) -> Optional[ResearchModelEntity222]:
        db_obj = self.get_entity_222_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_222(self, entity_id: int) -> bool:
        db_obj = self.get_entity_222_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_223_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity223]:
        return self.db.query(ResearchModelEntity223).offset(skip).limit(limit).all()

    def get_entity_223_by_id(self, entity_id: int) -> Optional[ResearchModelEntity223]:
        return self.db.query(ResearchModelEntity223).filter(ResearchModelEntity223.id == entity_id).first()

    def create_entity_223(self, payload: ResearchSchemaEntity223Create) -> ResearchModelEntity223:
        db_obj = ResearchModelEntity223(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_223(self, entity_id: int, payload: ResearchSchemaEntity223Update) -> Optional[ResearchModelEntity223]:
        db_obj = self.get_entity_223_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_223(self, entity_id: int) -> bool:
        db_obj = self.get_entity_223_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_224_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity224]:
        return self.db.query(ResearchModelEntity224).offset(skip).limit(limit).all()

    def get_entity_224_by_id(self, entity_id: int) -> Optional[ResearchModelEntity224]:
        return self.db.query(ResearchModelEntity224).filter(ResearchModelEntity224.id == entity_id).first()

    def create_entity_224(self, payload: ResearchSchemaEntity224Create) -> ResearchModelEntity224:
        db_obj = ResearchModelEntity224(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_224(self, entity_id: int, payload: ResearchSchemaEntity224Update) -> Optional[ResearchModelEntity224]:
        db_obj = self.get_entity_224_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_224(self, entity_id: int) -> bool:
        db_obj = self.get_entity_224_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_225_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity225]:
        return self.db.query(ResearchModelEntity225).offset(skip).limit(limit).all()

    def get_entity_225_by_id(self, entity_id: int) -> Optional[ResearchModelEntity225]:
        return self.db.query(ResearchModelEntity225).filter(ResearchModelEntity225.id == entity_id).first()

    def create_entity_225(self, payload: ResearchSchemaEntity225Create) -> ResearchModelEntity225:
        db_obj = ResearchModelEntity225(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_225(self, entity_id: int, payload: ResearchSchemaEntity225Update) -> Optional[ResearchModelEntity225]:
        db_obj = self.get_entity_225_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_225(self, entity_id: int) -> bool:
        db_obj = self.get_entity_225_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_226_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity226]:
        return self.db.query(ResearchModelEntity226).offset(skip).limit(limit).all()

    def get_entity_226_by_id(self, entity_id: int) -> Optional[ResearchModelEntity226]:
        return self.db.query(ResearchModelEntity226).filter(ResearchModelEntity226.id == entity_id).first()

    def create_entity_226(self, payload: ResearchSchemaEntity226Create) -> ResearchModelEntity226:
        db_obj = ResearchModelEntity226(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_226(self, entity_id: int, payload: ResearchSchemaEntity226Update) -> Optional[ResearchModelEntity226]:
        db_obj = self.get_entity_226_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_226(self, entity_id: int) -> bool:
        db_obj = self.get_entity_226_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_227_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity227]:
        return self.db.query(ResearchModelEntity227).offset(skip).limit(limit).all()

    def get_entity_227_by_id(self, entity_id: int) -> Optional[ResearchModelEntity227]:
        return self.db.query(ResearchModelEntity227).filter(ResearchModelEntity227.id == entity_id).first()

    def create_entity_227(self, payload: ResearchSchemaEntity227Create) -> ResearchModelEntity227:
        db_obj = ResearchModelEntity227(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_227(self, entity_id: int, payload: ResearchSchemaEntity227Update) -> Optional[ResearchModelEntity227]:
        db_obj = self.get_entity_227_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_227(self, entity_id: int) -> bool:
        db_obj = self.get_entity_227_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_228_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity228]:
        return self.db.query(ResearchModelEntity228).offset(skip).limit(limit).all()

    def get_entity_228_by_id(self, entity_id: int) -> Optional[ResearchModelEntity228]:
        return self.db.query(ResearchModelEntity228).filter(ResearchModelEntity228.id == entity_id).first()

    def create_entity_228(self, payload: ResearchSchemaEntity228Create) -> ResearchModelEntity228:
        db_obj = ResearchModelEntity228(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_228(self, entity_id: int, payload: ResearchSchemaEntity228Update) -> Optional[ResearchModelEntity228]:
        db_obj = self.get_entity_228_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_228(self, entity_id: int) -> bool:
        db_obj = self.get_entity_228_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_229_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity229]:
        return self.db.query(ResearchModelEntity229).offset(skip).limit(limit).all()

    def get_entity_229_by_id(self, entity_id: int) -> Optional[ResearchModelEntity229]:
        return self.db.query(ResearchModelEntity229).filter(ResearchModelEntity229.id == entity_id).first()

    def create_entity_229(self, payload: ResearchSchemaEntity229Create) -> ResearchModelEntity229:
        db_obj = ResearchModelEntity229(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_229(self, entity_id: int, payload: ResearchSchemaEntity229Update) -> Optional[ResearchModelEntity229]:
        db_obj = self.get_entity_229_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_229(self, entity_id: int) -> bool:
        db_obj = self.get_entity_229_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_230_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity230]:
        return self.db.query(ResearchModelEntity230).offset(skip).limit(limit).all()

    def get_entity_230_by_id(self, entity_id: int) -> Optional[ResearchModelEntity230]:
        return self.db.query(ResearchModelEntity230).filter(ResearchModelEntity230.id == entity_id).first()

    def create_entity_230(self, payload: ResearchSchemaEntity230Create) -> ResearchModelEntity230:
        db_obj = ResearchModelEntity230(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_230(self, entity_id: int, payload: ResearchSchemaEntity230Update) -> Optional[ResearchModelEntity230]:
        db_obj = self.get_entity_230_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_230(self, entity_id: int) -> bool:
        db_obj = self.get_entity_230_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_231_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity231]:
        return self.db.query(ResearchModelEntity231).offset(skip).limit(limit).all()

    def get_entity_231_by_id(self, entity_id: int) -> Optional[ResearchModelEntity231]:
        return self.db.query(ResearchModelEntity231).filter(ResearchModelEntity231.id == entity_id).first()

    def create_entity_231(self, payload: ResearchSchemaEntity231Create) -> ResearchModelEntity231:
        db_obj = ResearchModelEntity231(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_231(self, entity_id: int, payload: ResearchSchemaEntity231Update) -> Optional[ResearchModelEntity231]:
        db_obj = self.get_entity_231_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_231(self, entity_id: int) -> bool:
        db_obj = self.get_entity_231_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_232_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity232]:
        return self.db.query(ResearchModelEntity232).offset(skip).limit(limit).all()

    def get_entity_232_by_id(self, entity_id: int) -> Optional[ResearchModelEntity232]:
        return self.db.query(ResearchModelEntity232).filter(ResearchModelEntity232.id == entity_id).first()

    def create_entity_232(self, payload: ResearchSchemaEntity232Create) -> ResearchModelEntity232:
        db_obj = ResearchModelEntity232(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_232(self, entity_id: int, payload: ResearchSchemaEntity232Update) -> Optional[ResearchModelEntity232]:
        db_obj = self.get_entity_232_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_232(self, entity_id: int) -> bool:
        db_obj = self.get_entity_232_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_233_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity233]:
        return self.db.query(ResearchModelEntity233).offset(skip).limit(limit).all()

    def get_entity_233_by_id(self, entity_id: int) -> Optional[ResearchModelEntity233]:
        return self.db.query(ResearchModelEntity233).filter(ResearchModelEntity233.id == entity_id).first()

    def create_entity_233(self, payload: ResearchSchemaEntity233Create) -> ResearchModelEntity233:
        db_obj = ResearchModelEntity233(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_233(self, entity_id: int, payload: ResearchSchemaEntity233Update) -> Optional[ResearchModelEntity233]:
        db_obj = self.get_entity_233_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_233(self, entity_id: int) -> bool:
        db_obj = self.get_entity_233_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_234_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity234]:
        return self.db.query(ResearchModelEntity234).offset(skip).limit(limit).all()

    def get_entity_234_by_id(self, entity_id: int) -> Optional[ResearchModelEntity234]:
        return self.db.query(ResearchModelEntity234).filter(ResearchModelEntity234.id == entity_id).first()

    def create_entity_234(self, payload: ResearchSchemaEntity234Create) -> ResearchModelEntity234:
        db_obj = ResearchModelEntity234(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_234(self, entity_id: int, payload: ResearchSchemaEntity234Update) -> Optional[ResearchModelEntity234]:
        db_obj = self.get_entity_234_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_234(self, entity_id: int) -> bool:
        db_obj = self.get_entity_234_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_235_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity235]:
        return self.db.query(ResearchModelEntity235).offset(skip).limit(limit).all()

    def get_entity_235_by_id(self, entity_id: int) -> Optional[ResearchModelEntity235]:
        return self.db.query(ResearchModelEntity235).filter(ResearchModelEntity235.id == entity_id).first()

    def create_entity_235(self, payload: ResearchSchemaEntity235Create) -> ResearchModelEntity235:
        db_obj = ResearchModelEntity235(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_235(self, entity_id: int, payload: ResearchSchemaEntity235Update) -> Optional[ResearchModelEntity235]:
        db_obj = self.get_entity_235_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_235(self, entity_id: int) -> bool:
        db_obj = self.get_entity_235_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_236_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity236]:
        return self.db.query(ResearchModelEntity236).offset(skip).limit(limit).all()

    def get_entity_236_by_id(self, entity_id: int) -> Optional[ResearchModelEntity236]:
        return self.db.query(ResearchModelEntity236).filter(ResearchModelEntity236.id == entity_id).first()

    def create_entity_236(self, payload: ResearchSchemaEntity236Create) -> ResearchModelEntity236:
        db_obj = ResearchModelEntity236(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_236(self, entity_id: int, payload: ResearchSchemaEntity236Update) -> Optional[ResearchModelEntity236]:
        db_obj = self.get_entity_236_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_236(self, entity_id: int) -> bool:
        db_obj = self.get_entity_236_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_237_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity237]:
        return self.db.query(ResearchModelEntity237).offset(skip).limit(limit).all()

    def get_entity_237_by_id(self, entity_id: int) -> Optional[ResearchModelEntity237]:
        return self.db.query(ResearchModelEntity237).filter(ResearchModelEntity237.id == entity_id).first()

    def create_entity_237(self, payload: ResearchSchemaEntity237Create) -> ResearchModelEntity237:
        db_obj = ResearchModelEntity237(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_237(self, entity_id: int, payload: ResearchSchemaEntity237Update) -> Optional[ResearchModelEntity237]:
        db_obj = self.get_entity_237_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_237(self, entity_id: int) -> bool:
        db_obj = self.get_entity_237_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_238_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity238]:
        return self.db.query(ResearchModelEntity238).offset(skip).limit(limit).all()

    def get_entity_238_by_id(self, entity_id: int) -> Optional[ResearchModelEntity238]:
        return self.db.query(ResearchModelEntity238).filter(ResearchModelEntity238.id == entity_id).first()

    def create_entity_238(self, payload: ResearchSchemaEntity238Create) -> ResearchModelEntity238:
        db_obj = ResearchModelEntity238(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_238(self, entity_id: int, payload: ResearchSchemaEntity238Update) -> Optional[ResearchModelEntity238]:
        db_obj = self.get_entity_238_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_238(self, entity_id: int) -> bool:
        db_obj = self.get_entity_238_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_239_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity239]:
        return self.db.query(ResearchModelEntity239).offset(skip).limit(limit).all()

    def get_entity_239_by_id(self, entity_id: int) -> Optional[ResearchModelEntity239]:
        return self.db.query(ResearchModelEntity239).filter(ResearchModelEntity239.id == entity_id).first()

    def create_entity_239(self, payload: ResearchSchemaEntity239Create) -> ResearchModelEntity239:
        db_obj = ResearchModelEntity239(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_239(self, entity_id: int, payload: ResearchSchemaEntity239Update) -> Optional[ResearchModelEntity239]:
        db_obj = self.get_entity_239_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_239(self, entity_id: int) -> bool:
        db_obj = self.get_entity_239_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_240_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity240]:
        return self.db.query(ResearchModelEntity240).offset(skip).limit(limit).all()

    def get_entity_240_by_id(self, entity_id: int) -> Optional[ResearchModelEntity240]:
        return self.db.query(ResearchModelEntity240).filter(ResearchModelEntity240.id == entity_id).first()

    def create_entity_240(self, payload: ResearchSchemaEntity240Create) -> ResearchModelEntity240:
        db_obj = ResearchModelEntity240(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_240(self, entity_id: int, payload: ResearchSchemaEntity240Update) -> Optional[ResearchModelEntity240]:
        db_obj = self.get_entity_240_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_240(self, entity_id: int) -> bool:
        db_obj = self.get_entity_240_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_241_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity241]:
        return self.db.query(ResearchModelEntity241).offset(skip).limit(limit).all()

    def get_entity_241_by_id(self, entity_id: int) -> Optional[ResearchModelEntity241]:
        return self.db.query(ResearchModelEntity241).filter(ResearchModelEntity241.id == entity_id).first()

    def create_entity_241(self, payload: ResearchSchemaEntity241Create) -> ResearchModelEntity241:
        db_obj = ResearchModelEntity241(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_241(self, entity_id: int, payload: ResearchSchemaEntity241Update) -> Optional[ResearchModelEntity241]:
        db_obj = self.get_entity_241_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_241(self, entity_id: int) -> bool:
        db_obj = self.get_entity_241_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_242_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity242]:
        return self.db.query(ResearchModelEntity242).offset(skip).limit(limit).all()

    def get_entity_242_by_id(self, entity_id: int) -> Optional[ResearchModelEntity242]:
        return self.db.query(ResearchModelEntity242).filter(ResearchModelEntity242.id == entity_id).first()

    def create_entity_242(self, payload: ResearchSchemaEntity242Create) -> ResearchModelEntity242:
        db_obj = ResearchModelEntity242(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_242(self, entity_id: int, payload: ResearchSchemaEntity242Update) -> Optional[ResearchModelEntity242]:
        db_obj = self.get_entity_242_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_242(self, entity_id: int) -> bool:
        db_obj = self.get_entity_242_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_243_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity243]:
        return self.db.query(ResearchModelEntity243).offset(skip).limit(limit).all()

    def get_entity_243_by_id(self, entity_id: int) -> Optional[ResearchModelEntity243]:
        return self.db.query(ResearchModelEntity243).filter(ResearchModelEntity243.id == entity_id).first()

    def create_entity_243(self, payload: ResearchSchemaEntity243Create) -> ResearchModelEntity243:
        db_obj = ResearchModelEntity243(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_243(self, entity_id: int, payload: ResearchSchemaEntity243Update) -> Optional[ResearchModelEntity243]:
        db_obj = self.get_entity_243_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_243(self, entity_id: int) -> bool:
        db_obj = self.get_entity_243_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_244_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity244]:
        return self.db.query(ResearchModelEntity244).offset(skip).limit(limit).all()

    def get_entity_244_by_id(self, entity_id: int) -> Optional[ResearchModelEntity244]:
        return self.db.query(ResearchModelEntity244).filter(ResearchModelEntity244.id == entity_id).first()

    def create_entity_244(self, payload: ResearchSchemaEntity244Create) -> ResearchModelEntity244:
        db_obj = ResearchModelEntity244(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_244(self, entity_id: int, payload: ResearchSchemaEntity244Update) -> Optional[ResearchModelEntity244]:
        db_obj = self.get_entity_244_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_244(self, entity_id: int) -> bool:
        db_obj = self.get_entity_244_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_245_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity245]:
        return self.db.query(ResearchModelEntity245).offset(skip).limit(limit).all()

    def get_entity_245_by_id(self, entity_id: int) -> Optional[ResearchModelEntity245]:
        return self.db.query(ResearchModelEntity245).filter(ResearchModelEntity245.id == entity_id).first()

    def create_entity_245(self, payload: ResearchSchemaEntity245Create) -> ResearchModelEntity245:
        db_obj = ResearchModelEntity245(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_245(self, entity_id: int, payload: ResearchSchemaEntity245Update) -> Optional[ResearchModelEntity245]:
        db_obj = self.get_entity_245_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_245(self, entity_id: int) -> bool:
        db_obj = self.get_entity_245_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_246_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity246]:
        return self.db.query(ResearchModelEntity246).offset(skip).limit(limit).all()

    def get_entity_246_by_id(self, entity_id: int) -> Optional[ResearchModelEntity246]:
        return self.db.query(ResearchModelEntity246).filter(ResearchModelEntity246.id == entity_id).first()

    def create_entity_246(self, payload: ResearchSchemaEntity246Create) -> ResearchModelEntity246:
        db_obj = ResearchModelEntity246(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_246(self, entity_id: int, payload: ResearchSchemaEntity246Update) -> Optional[ResearchModelEntity246]:
        db_obj = self.get_entity_246_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_246(self, entity_id: int) -> bool:
        db_obj = self.get_entity_246_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_247_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity247]:
        return self.db.query(ResearchModelEntity247).offset(skip).limit(limit).all()

    def get_entity_247_by_id(self, entity_id: int) -> Optional[ResearchModelEntity247]:
        return self.db.query(ResearchModelEntity247).filter(ResearchModelEntity247.id == entity_id).first()

    def create_entity_247(self, payload: ResearchSchemaEntity247Create) -> ResearchModelEntity247:
        db_obj = ResearchModelEntity247(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_247(self, entity_id: int, payload: ResearchSchemaEntity247Update) -> Optional[ResearchModelEntity247]:
        db_obj = self.get_entity_247_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_247(self, entity_id: int) -> bool:
        db_obj = self.get_entity_247_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_248_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity248]:
        return self.db.query(ResearchModelEntity248).offset(skip).limit(limit).all()

    def get_entity_248_by_id(self, entity_id: int) -> Optional[ResearchModelEntity248]:
        return self.db.query(ResearchModelEntity248).filter(ResearchModelEntity248.id == entity_id).first()

    def create_entity_248(self, payload: ResearchSchemaEntity248Create) -> ResearchModelEntity248:
        db_obj = ResearchModelEntity248(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_248(self, entity_id: int, payload: ResearchSchemaEntity248Update) -> Optional[ResearchModelEntity248]:
        db_obj = self.get_entity_248_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_248(self, entity_id: int) -> bool:
        db_obj = self.get_entity_248_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_249_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity249]:
        return self.db.query(ResearchModelEntity249).offset(skip).limit(limit).all()

    def get_entity_249_by_id(self, entity_id: int) -> Optional[ResearchModelEntity249]:
        return self.db.query(ResearchModelEntity249).filter(ResearchModelEntity249.id == entity_id).first()

    def create_entity_249(self, payload: ResearchSchemaEntity249Create) -> ResearchModelEntity249:
        db_obj = ResearchModelEntity249(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_249(self, entity_id: int, payload: ResearchSchemaEntity249Update) -> Optional[ResearchModelEntity249]:
        db_obj = self.get_entity_249_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_249(self, entity_id: int) -> bool:
        db_obj = self.get_entity_249_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def get_entity_250_list(self, skip: int = 0, limit: int = 100) -> List[ResearchModelEntity250]:
        return self.db.query(ResearchModelEntity250).offset(skip).limit(limit).all()

    def get_entity_250_by_id(self, entity_id: int) -> Optional[ResearchModelEntity250]:
        return self.db.query(ResearchModelEntity250).filter(ResearchModelEntity250.id == entity_id).first()

    def create_entity_250(self, payload: ResearchSchemaEntity250Create) -> ResearchModelEntity250:
        db_obj = ResearchModelEntity250(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_250(self, entity_id: int, payload: ResearchSchemaEntity250Update) -> Optional[ResearchModelEntity250]:
        db_obj = self.get_entity_250_by_id(entity_id)
        if not db_obj:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete_entity_250(self, entity_id: int) -> bool:
        db_obj = self.get_entity_250_by_id(entity_id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

