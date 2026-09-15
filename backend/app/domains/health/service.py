"""
Campus Health & Clinic Management - Service Business Logic Layer
Module: app.domains.health.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.health.models import *
from app.domains.health.schemas import *

class HealthDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity1]:
        return self.db.query(HealthModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[HealthModelEntity1]:
        return self.db.query(HealthModelEntity1).filter(HealthModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: HealthSchemaEntity1Create) -> HealthModelEntity1:
        db_obj = HealthModelEntity1(
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

    def update_entity_1(self, entity_id: int, payload: HealthSchemaEntity1Update) -> Optional[HealthModelEntity1]:
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

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity2]:
        return self.db.query(HealthModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[HealthModelEntity2]:
        return self.db.query(HealthModelEntity2).filter(HealthModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: HealthSchemaEntity2Create) -> HealthModelEntity2:
        db_obj = HealthModelEntity2(
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

    def update_entity_2(self, entity_id: int, payload: HealthSchemaEntity2Update) -> Optional[HealthModelEntity2]:
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

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity3]:
        return self.db.query(HealthModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[HealthModelEntity3]:
        return self.db.query(HealthModelEntity3).filter(HealthModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: HealthSchemaEntity3Create) -> HealthModelEntity3:
        db_obj = HealthModelEntity3(
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

    def update_entity_3(self, entity_id: int, payload: HealthSchemaEntity3Update) -> Optional[HealthModelEntity3]:
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

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity4]:
        return self.db.query(HealthModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[HealthModelEntity4]:
        return self.db.query(HealthModelEntity4).filter(HealthModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: HealthSchemaEntity4Create) -> HealthModelEntity4:
        db_obj = HealthModelEntity4(
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

    def update_entity_4(self, entity_id: int, payload: HealthSchemaEntity4Update) -> Optional[HealthModelEntity4]:
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

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity5]:
        return self.db.query(HealthModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[HealthModelEntity5]:
        return self.db.query(HealthModelEntity5).filter(HealthModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: HealthSchemaEntity5Create) -> HealthModelEntity5:
        db_obj = HealthModelEntity5(
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

    def update_entity_5(self, entity_id: int, payload: HealthSchemaEntity5Update) -> Optional[HealthModelEntity5]:
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

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity6]:
        return self.db.query(HealthModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[HealthModelEntity6]:
        return self.db.query(HealthModelEntity6).filter(HealthModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: HealthSchemaEntity6Create) -> HealthModelEntity6:
        db_obj = HealthModelEntity6(
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

    def update_entity_6(self, entity_id: int, payload: HealthSchemaEntity6Update) -> Optional[HealthModelEntity6]:
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

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity7]:
        return self.db.query(HealthModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[HealthModelEntity7]:
        return self.db.query(HealthModelEntity7).filter(HealthModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: HealthSchemaEntity7Create) -> HealthModelEntity7:
        db_obj = HealthModelEntity7(
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

    def update_entity_7(self, entity_id: int, payload: HealthSchemaEntity7Update) -> Optional[HealthModelEntity7]:
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

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity8]:
        return self.db.query(HealthModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[HealthModelEntity8]:
        return self.db.query(HealthModelEntity8).filter(HealthModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: HealthSchemaEntity8Create) -> HealthModelEntity8:
        db_obj = HealthModelEntity8(
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

    def update_entity_8(self, entity_id: int, payload: HealthSchemaEntity8Update) -> Optional[HealthModelEntity8]:
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

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity9]:
        return self.db.query(HealthModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[HealthModelEntity9]:
        return self.db.query(HealthModelEntity9).filter(HealthModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: HealthSchemaEntity9Create) -> HealthModelEntity9:
        db_obj = HealthModelEntity9(
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

    def update_entity_9(self, entity_id: int, payload: HealthSchemaEntity9Update) -> Optional[HealthModelEntity9]:
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

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity10]:
        return self.db.query(HealthModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[HealthModelEntity10]:
        return self.db.query(HealthModelEntity10).filter(HealthModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: HealthSchemaEntity10Create) -> HealthModelEntity10:
        db_obj = HealthModelEntity10(
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

    def update_entity_10(self, entity_id: int, payload: HealthSchemaEntity10Update) -> Optional[HealthModelEntity10]:
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

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity11]:
        return self.db.query(HealthModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[HealthModelEntity11]:
        return self.db.query(HealthModelEntity11).filter(HealthModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: HealthSchemaEntity11Create) -> HealthModelEntity11:
        db_obj = HealthModelEntity11(
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

    def update_entity_11(self, entity_id: int, payload: HealthSchemaEntity11Update) -> Optional[HealthModelEntity11]:
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

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity12]:
        return self.db.query(HealthModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[HealthModelEntity12]:
        return self.db.query(HealthModelEntity12).filter(HealthModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: HealthSchemaEntity12Create) -> HealthModelEntity12:
        db_obj = HealthModelEntity12(
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

    def update_entity_12(self, entity_id: int, payload: HealthSchemaEntity12Update) -> Optional[HealthModelEntity12]:
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

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity13]:
        return self.db.query(HealthModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[HealthModelEntity13]:
        return self.db.query(HealthModelEntity13).filter(HealthModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: HealthSchemaEntity13Create) -> HealthModelEntity13:
        db_obj = HealthModelEntity13(
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

    def update_entity_13(self, entity_id: int, payload: HealthSchemaEntity13Update) -> Optional[HealthModelEntity13]:
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

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity14]:
        return self.db.query(HealthModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[HealthModelEntity14]:
        return self.db.query(HealthModelEntity14).filter(HealthModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: HealthSchemaEntity14Create) -> HealthModelEntity14:
        db_obj = HealthModelEntity14(
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

    def update_entity_14(self, entity_id: int, payload: HealthSchemaEntity14Update) -> Optional[HealthModelEntity14]:
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

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity15]:
        return self.db.query(HealthModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[HealthModelEntity15]:
        return self.db.query(HealthModelEntity15).filter(HealthModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: HealthSchemaEntity15Create) -> HealthModelEntity15:
        db_obj = HealthModelEntity15(
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

    def update_entity_15(self, entity_id: int, payload: HealthSchemaEntity15Update) -> Optional[HealthModelEntity15]:
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

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity16]:
        return self.db.query(HealthModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[HealthModelEntity16]:
        return self.db.query(HealthModelEntity16).filter(HealthModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: HealthSchemaEntity16Create) -> HealthModelEntity16:
        db_obj = HealthModelEntity16(
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

    def update_entity_16(self, entity_id: int, payload: HealthSchemaEntity16Update) -> Optional[HealthModelEntity16]:
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

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity17]:
        return self.db.query(HealthModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[HealthModelEntity17]:
        return self.db.query(HealthModelEntity17).filter(HealthModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: HealthSchemaEntity17Create) -> HealthModelEntity17:
        db_obj = HealthModelEntity17(
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

    def update_entity_17(self, entity_id: int, payload: HealthSchemaEntity17Update) -> Optional[HealthModelEntity17]:
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

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity18]:
        return self.db.query(HealthModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[HealthModelEntity18]:
        return self.db.query(HealthModelEntity18).filter(HealthModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: HealthSchemaEntity18Create) -> HealthModelEntity18:
        db_obj = HealthModelEntity18(
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

    def update_entity_18(self, entity_id: int, payload: HealthSchemaEntity18Update) -> Optional[HealthModelEntity18]:
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

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity19]:
        return self.db.query(HealthModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[HealthModelEntity19]:
        return self.db.query(HealthModelEntity19).filter(HealthModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: HealthSchemaEntity19Create) -> HealthModelEntity19:
        db_obj = HealthModelEntity19(
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

    def update_entity_19(self, entity_id: int, payload: HealthSchemaEntity19Update) -> Optional[HealthModelEntity19]:
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

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity20]:
        return self.db.query(HealthModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[HealthModelEntity20]:
        return self.db.query(HealthModelEntity20).filter(HealthModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: HealthSchemaEntity20Create) -> HealthModelEntity20:
        db_obj = HealthModelEntity20(
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

    def update_entity_20(self, entity_id: int, payload: HealthSchemaEntity20Update) -> Optional[HealthModelEntity20]:
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

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity21]:
        return self.db.query(HealthModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[HealthModelEntity21]:
        return self.db.query(HealthModelEntity21).filter(HealthModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: HealthSchemaEntity21Create) -> HealthModelEntity21:
        db_obj = HealthModelEntity21(
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

    def update_entity_21(self, entity_id: int, payload: HealthSchemaEntity21Update) -> Optional[HealthModelEntity21]:
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

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity22]:
        return self.db.query(HealthModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[HealthModelEntity22]:
        return self.db.query(HealthModelEntity22).filter(HealthModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: HealthSchemaEntity22Create) -> HealthModelEntity22:
        db_obj = HealthModelEntity22(
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

    def update_entity_22(self, entity_id: int, payload: HealthSchemaEntity22Update) -> Optional[HealthModelEntity22]:
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

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity23]:
        return self.db.query(HealthModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[HealthModelEntity23]:
        return self.db.query(HealthModelEntity23).filter(HealthModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: HealthSchemaEntity23Create) -> HealthModelEntity23:
        db_obj = HealthModelEntity23(
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

    def update_entity_23(self, entity_id: int, payload: HealthSchemaEntity23Update) -> Optional[HealthModelEntity23]:
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

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity24]:
        return self.db.query(HealthModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[HealthModelEntity24]:
        return self.db.query(HealthModelEntity24).filter(HealthModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: HealthSchemaEntity24Create) -> HealthModelEntity24:
        db_obj = HealthModelEntity24(
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

    def update_entity_24(self, entity_id: int, payload: HealthSchemaEntity24Update) -> Optional[HealthModelEntity24]:
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

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity25]:
        return self.db.query(HealthModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[HealthModelEntity25]:
        return self.db.query(HealthModelEntity25).filter(HealthModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: HealthSchemaEntity25Create) -> HealthModelEntity25:
        db_obj = HealthModelEntity25(
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

    def update_entity_25(self, entity_id: int, payload: HealthSchemaEntity25Update) -> Optional[HealthModelEntity25]:
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

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity26]:
        return self.db.query(HealthModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[HealthModelEntity26]:
        return self.db.query(HealthModelEntity26).filter(HealthModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: HealthSchemaEntity26Create) -> HealthModelEntity26:
        db_obj = HealthModelEntity26(
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

    def update_entity_26(self, entity_id: int, payload: HealthSchemaEntity26Update) -> Optional[HealthModelEntity26]:
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

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity27]:
        return self.db.query(HealthModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[HealthModelEntity27]:
        return self.db.query(HealthModelEntity27).filter(HealthModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: HealthSchemaEntity27Create) -> HealthModelEntity27:
        db_obj = HealthModelEntity27(
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

    def update_entity_27(self, entity_id: int, payload: HealthSchemaEntity27Update) -> Optional[HealthModelEntity27]:
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

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity28]:
        return self.db.query(HealthModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[HealthModelEntity28]:
        return self.db.query(HealthModelEntity28).filter(HealthModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: HealthSchemaEntity28Create) -> HealthModelEntity28:
        db_obj = HealthModelEntity28(
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

    def update_entity_28(self, entity_id: int, payload: HealthSchemaEntity28Update) -> Optional[HealthModelEntity28]:
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

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity29]:
        return self.db.query(HealthModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[HealthModelEntity29]:
        return self.db.query(HealthModelEntity29).filter(HealthModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: HealthSchemaEntity29Create) -> HealthModelEntity29:
        db_obj = HealthModelEntity29(
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

    def update_entity_29(self, entity_id: int, payload: HealthSchemaEntity29Update) -> Optional[HealthModelEntity29]:
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

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity30]:
        return self.db.query(HealthModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[HealthModelEntity30]:
        return self.db.query(HealthModelEntity30).filter(HealthModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: HealthSchemaEntity30Create) -> HealthModelEntity30:
        db_obj = HealthModelEntity30(
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

    def update_entity_30(self, entity_id: int, payload: HealthSchemaEntity30Update) -> Optional[HealthModelEntity30]:
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

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity31]:
        return self.db.query(HealthModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[HealthModelEntity31]:
        return self.db.query(HealthModelEntity31).filter(HealthModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: HealthSchemaEntity31Create) -> HealthModelEntity31:
        db_obj = HealthModelEntity31(
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

    def update_entity_31(self, entity_id: int, payload: HealthSchemaEntity31Update) -> Optional[HealthModelEntity31]:
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

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity32]:
        return self.db.query(HealthModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[HealthModelEntity32]:
        return self.db.query(HealthModelEntity32).filter(HealthModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: HealthSchemaEntity32Create) -> HealthModelEntity32:
        db_obj = HealthModelEntity32(
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

    def update_entity_32(self, entity_id: int, payload: HealthSchemaEntity32Update) -> Optional[HealthModelEntity32]:
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

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity33]:
        return self.db.query(HealthModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[HealthModelEntity33]:
        return self.db.query(HealthModelEntity33).filter(HealthModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: HealthSchemaEntity33Create) -> HealthModelEntity33:
        db_obj = HealthModelEntity33(
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

    def update_entity_33(self, entity_id: int, payload: HealthSchemaEntity33Update) -> Optional[HealthModelEntity33]:
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

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity34]:
        return self.db.query(HealthModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[HealthModelEntity34]:
        return self.db.query(HealthModelEntity34).filter(HealthModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: HealthSchemaEntity34Create) -> HealthModelEntity34:
        db_obj = HealthModelEntity34(
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

    def update_entity_34(self, entity_id: int, payload: HealthSchemaEntity34Update) -> Optional[HealthModelEntity34]:
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

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity35]:
        return self.db.query(HealthModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[HealthModelEntity35]:
        return self.db.query(HealthModelEntity35).filter(HealthModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: HealthSchemaEntity35Create) -> HealthModelEntity35:
        db_obj = HealthModelEntity35(
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

    def update_entity_35(self, entity_id: int, payload: HealthSchemaEntity35Update) -> Optional[HealthModelEntity35]:
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

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity36]:
        return self.db.query(HealthModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[HealthModelEntity36]:
        return self.db.query(HealthModelEntity36).filter(HealthModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: HealthSchemaEntity36Create) -> HealthModelEntity36:
        db_obj = HealthModelEntity36(
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

    def update_entity_36(self, entity_id: int, payload: HealthSchemaEntity36Update) -> Optional[HealthModelEntity36]:
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

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity37]:
        return self.db.query(HealthModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[HealthModelEntity37]:
        return self.db.query(HealthModelEntity37).filter(HealthModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: HealthSchemaEntity37Create) -> HealthModelEntity37:
        db_obj = HealthModelEntity37(
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

    def update_entity_37(self, entity_id: int, payload: HealthSchemaEntity37Update) -> Optional[HealthModelEntity37]:
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

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity38]:
        return self.db.query(HealthModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[HealthModelEntity38]:
        return self.db.query(HealthModelEntity38).filter(HealthModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: HealthSchemaEntity38Create) -> HealthModelEntity38:
        db_obj = HealthModelEntity38(
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

    def update_entity_38(self, entity_id: int, payload: HealthSchemaEntity38Update) -> Optional[HealthModelEntity38]:
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

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity39]:
        return self.db.query(HealthModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[HealthModelEntity39]:
        return self.db.query(HealthModelEntity39).filter(HealthModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: HealthSchemaEntity39Create) -> HealthModelEntity39:
        db_obj = HealthModelEntity39(
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

    def update_entity_39(self, entity_id: int, payload: HealthSchemaEntity39Update) -> Optional[HealthModelEntity39]:
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

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity40]:
        return self.db.query(HealthModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[HealthModelEntity40]:
        return self.db.query(HealthModelEntity40).filter(HealthModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: HealthSchemaEntity40Create) -> HealthModelEntity40:
        db_obj = HealthModelEntity40(
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

    def update_entity_40(self, entity_id: int, payload: HealthSchemaEntity40Update) -> Optional[HealthModelEntity40]:
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

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity41]:
        return self.db.query(HealthModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[HealthModelEntity41]:
        return self.db.query(HealthModelEntity41).filter(HealthModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: HealthSchemaEntity41Create) -> HealthModelEntity41:
        db_obj = HealthModelEntity41(
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

    def update_entity_41(self, entity_id: int, payload: HealthSchemaEntity41Update) -> Optional[HealthModelEntity41]:
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

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity42]:
        return self.db.query(HealthModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[HealthModelEntity42]:
        return self.db.query(HealthModelEntity42).filter(HealthModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: HealthSchemaEntity42Create) -> HealthModelEntity42:
        db_obj = HealthModelEntity42(
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

    def update_entity_42(self, entity_id: int, payload: HealthSchemaEntity42Update) -> Optional[HealthModelEntity42]:
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

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity43]:
        return self.db.query(HealthModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[HealthModelEntity43]:
        return self.db.query(HealthModelEntity43).filter(HealthModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: HealthSchemaEntity43Create) -> HealthModelEntity43:
        db_obj = HealthModelEntity43(
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

    def update_entity_43(self, entity_id: int, payload: HealthSchemaEntity43Update) -> Optional[HealthModelEntity43]:
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

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity44]:
        return self.db.query(HealthModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[HealthModelEntity44]:
        return self.db.query(HealthModelEntity44).filter(HealthModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: HealthSchemaEntity44Create) -> HealthModelEntity44:
        db_obj = HealthModelEntity44(
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

    def update_entity_44(self, entity_id: int, payload: HealthSchemaEntity44Update) -> Optional[HealthModelEntity44]:
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

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity45]:
        return self.db.query(HealthModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[HealthModelEntity45]:
        return self.db.query(HealthModelEntity45).filter(HealthModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: HealthSchemaEntity45Create) -> HealthModelEntity45:
        db_obj = HealthModelEntity45(
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

    def update_entity_45(self, entity_id: int, payload: HealthSchemaEntity45Update) -> Optional[HealthModelEntity45]:
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

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity46]:
        return self.db.query(HealthModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[HealthModelEntity46]:
        return self.db.query(HealthModelEntity46).filter(HealthModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: HealthSchemaEntity46Create) -> HealthModelEntity46:
        db_obj = HealthModelEntity46(
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

    def update_entity_46(self, entity_id: int, payload: HealthSchemaEntity46Update) -> Optional[HealthModelEntity46]:
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

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity47]:
        return self.db.query(HealthModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[HealthModelEntity47]:
        return self.db.query(HealthModelEntity47).filter(HealthModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: HealthSchemaEntity47Create) -> HealthModelEntity47:
        db_obj = HealthModelEntity47(
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

    def update_entity_47(self, entity_id: int, payload: HealthSchemaEntity47Update) -> Optional[HealthModelEntity47]:
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

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity48]:
        return self.db.query(HealthModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[HealthModelEntity48]:
        return self.db.query(HealthModelEntity48).filter(HealthModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: HealthSchemaEntity48Create) -> HealthModelEntity48:
        db_obj = HealthModelEntity48(
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

    def update_entity_48(self, entity_id: int, payload: HealthSchemaEntity48Update) -> Optional[HealthModelEntity48]:
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

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity49]:
        return self.db.query(HealthModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[HealthModelEntity49]:
        return self.db.query(HealthModelEntity49).filter(HealthModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: HealthSchemaEntity49Create) -> HealthModelEntity49:
        db_obj = HealthModelEntity49(
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

    def update_entity_49(self, entity_id: int, payload: HealthSchemaEntity49Update) -> Optional[HealthModelEntity49]:
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

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity50]:
        return self.db.query(HealthModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[HealthModelEntity50]:
        return self.db.query(HealthModelEntity50).filter(HealthModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: HealthSchemaEntity50Create) -> HealthModelEntity50:
        db_obj = HealthModelEntity50(
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

    def update_entity_50(self, entity_id: int, payload: HealthSchemaEntity50Update) -> Optional[HealthModelEntity50]:
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

    def get_entity_51_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity51]:
        return self.db.query(HealthModelEntity51).offset(skip).limit(limit).all()

    def get_entity_51_by_id(self, entity_id: int) -> Optional[HealthModelEntity51]:
        return self.db.query(HealthModelEntity51).filter(HealthModelEntity51.id == entity_id).first()

    def create_entity_51(self, payload: HealthSchemaEntity51Create) -> HealthModelEntity51:
        db_obj = HealthModelEntity51(
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

    def update_entity_51(self, entity_id: int, payload: HealthSchemaEntity51Update) -> Optional[HealthModelEntity51]:
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

    def get_entity_52_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity52]:
        return self.db.query(HealthModelEntity52).offset(skip).limit(limit).all()

    def get_entity_52_by_id(self, entity_id: int) -> Optional[HealthModelEntity52]:
        return self.db.query(HealthModelEntity52).filter(HealthModelEntity52.id == entity_id).first()

    def create_entity_52(self, payload: HealthSchemaEntity52Create) -> HealthModelEntity52:
        db_obj = HealthModelEntity52(
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

    def update_entity_52(self, entity_id: int, payload: HealthSchemaEntity52Update) -> Optional[HealthModelEntity52]:
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

    def get_entity_53_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity53]:
        return self.db.query(HealthModelEntity53).offset(skip).limit(limit).all()

    def get_entity_53_by_id(self, entity_id: int) -> Optional[HealthModelEntity53]:
        return self.db.query(HealthModelEntity53).filter(HealthModelEntity53.id == entity_id).first()

    def create_entity_53(self, payload: HealthSchemaEntity53Create) -> HealthModelEntity53:
        db_obj = HealthModelEntity53(
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

    def update_entity_53(self, entity_id: int, payload: HealthSchemaEntity53Update) -> Optional[HealthModelEntity53]:
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

    def get_entity_54_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity54]:
        return self.db.query(HealthModelEntity54).offset(skip).limit(limit).all()

    def get_entity_54_by_id(self, entity_id: int) -> Optional[HealthModelEntity54]:
        return self.db.query(HealthModelEntity54).filter(HealthModelEntity54.id == entity_id).first()

    def create_entity_54(self, payload: HealthSchemaEntity54Create) -> HealthModelEntity54:
        db_obj = HealthModelEntity54(
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

    def update_entity_54(self, entity_id: int, payload: HealthSchemaEntity54Update) -> Optional[HealthModelEntity54]:
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

    def get_entity_55_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity55]:
        return self.db.query(HealthModelEntity55).offset(skip).limit(limit).all()

    def get_entity_55_by_id(self, entity_id: int) -> Optional[HealthModelEntity55]:
        return self.db.query(HealthModelEntity55).filter(HealthModelEntity55.id == entity_id).first()

    def create_entity_55(self, payload: HealthSchemaEntity55Create) -> HealthModelEntity55:
        db_obj = HealthModelEntity55(
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

    def update_entity_55(self, entity_id: int, payload: HealthSchemaEntity55Update) -> Optional[HealthModelEntity55]:
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

    def get_entity_56_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity56]:
        return self.db.query(HealthModelEntity56).offset(skip).limit(limit).all()

    def get_entity_56_by_id(self, entity_id: int) -> Optional[HealthModelEntity56]:
        return self.db.query(HealthModelEntity56).filter(HealthModelEntity56.id == entity_id).first()

    def create_entity_56(self, payload: HealthSchemaEntity56Create) -> HealthModelEntity56:
        db_obj = HealthModelEntity56(
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

    def update_entity_56(self, entity_id: int, payload: HealthSchemaEntity56Update) -> Optional[HealthModelEntity56]:
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

    def get_entity_57_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity57]:
        return self.db.query(HealthModelEntity57).offset(skip).limit(limit).all()

    def get_entity_57_by_id(self, entity_id: int) -> Optional[HealthModelEntity57]:
        return self.db.query(HealthModelEntity57).filter(HealthModelEntity57.id == entity_id).first()

    def create_entity_57(self, payload: HealthSchemaEntity57Create) -> HealthModelEntity57:
        db_obj = HealthModelEntity57(
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

    def update_entity_57(self, entity_id: int, payload: HealthSchemaEntity57Update) -> Optional[HealthModelEntity57]:
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

    def get_entity_58_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity58]:
        return self.db.query(HealthModelEntity58).offset(skip).limit(limit).all()

    def get_entity_58_by_id(self, entity_id: int) -> Optional[HealthModelEntity58]:
        return self.db.query(HealthModelEntity58).filter(HealthModelEntity58.id == entity_id).first()

    def create_entity_58(self, payload: HealthSchemaEntity58Create) -> HealthModelEntity58:
        db_obj = HealthModelEntity58(
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

    def update_entity_58(self, entity_id: int, payload: HealthSchemaEntity58Update) -> Optional[HealthModelEntity58]:
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

    def get_entity_59_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity59]:
        return self.db.query(HealthModelEntity59).offset(skip).limit(limit).all()

    def get_entity_59_by_id(self, entity_id: int) -> Optional[HealthModelEntity59]:
        return self.db.query(HealthModelEntity59).filter(HealthModelEntity59.id == entity_id).first()

    def create_entity_59(self, payload: HealthSchemaEntity59Create) -> HealthModelEntity59:
        db_obj = HealthModelEntity59(
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

    def update_entity_59(self, entity_id: int, payload: HealthSchemaEntity59Update) -> Optional[HealthModelEntity59]:
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

    def get_entity_60_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity60]:
        return self.db.query(HealthModelEntity60).offset(skip).limit(limit).all()

    def get_entity_60_by_id(self, entity_id: int) -> Optional[HealthModelEntity60]:
        return self.db.query(HealthModelEntity60).filter(HealthModelEntity60.id == entity_id).first()

    def create_entity_60(self, payload: HealthSchemaEntity60Create) -> HealthModelEntity60:
        db_obj = HealthModelEntity60(
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

    def update_entity_60(self, entity_id: int, payload: HealthSchemaEntity60Update) -> Optional[HealthModelEntity60]:
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

    def get_entity_61_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity61]:
        return self.db.query(HealthModelEntity61).offset(skip).limit(limit).all()

    def get_entity_61_by_id(self, entity_id: int) -> Optional[HealthModelEntity61]:
        return self.db.query(HealthModelEntity61).filter(HealthModelEntity61.id == entity_id).first()

    def create_entity_61(self, payload: HealthSchemaEntity61Create) -> HealthModelEntity61:
        db_obj = HealthModelEntity61(
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

    def update_entity_61(self, entity_id: int, payload: HealthSchemaEntity61Update) -> Optional[HealthModelEntity61]:
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

    def get_entity_62_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity62]:
        return self.db.query(HealthModelEntity62).offset(skip).limit(limit).all()

    def get_entity_62_by_id(self, entity_id: int) -> Optional[HealthModelEntity62]:
        return self.db.query(HealthModelEntity62).filter(HealthModelEntity62.id == entity_id).first()

    def create_entity_62(self, payload: HealthSchemaEntity62Create) -> HealthModelEntity62:
        db_obj = HealthModelEntity62(
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

    def update_entity_62(self, entity_id: int, payload: HealthSchemaEntity62Update) -> Optional[HealthModelEntity62]:
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

    def get_entity_63_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity63]:
        return self.db.query(HealthModelEntity63).offset(skip).limit(limit).all()

    def get_entity_63_by_id(self, entity_id: int) -> Optional[HealthModelEntity63]:
        return self.db.query(HealthModelEntity63).filter(HealthModelEntity63.id == entity_id).first()

    def create_entity_63(self, payload: HealthSchemaEntity63Create) -> HealthModelEntity63:
        db_obj = HealthModelEntity63(
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

    def update_entity_63(self, entity_id: int, payload: HealthSchemaEntity63Update) -> Optional[HealthModelEntity63]:
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

    def get_entity_64_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity64]:
        return self.db.query(HealthModelEntity64).offset(skip).limit(limit).all()

    def get_entity_64_by_id(self, entity_id: int) -> Optional[HealthModelEntity64]:
        return self.db.query(HealthModelEntity64).filter(HealthModelEntity64.id == entity_id).first()

    def create_entity_64(self, payload: HealthSchemaEntity64Create) -> HealthModelEntity64:
        db_obj = HealthModelEntity64(
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

    def update_entity_64(self, entity_id: int, payload: HealthSchemaEntity64Update) -> Optional[HealthModelEntity64]:
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

    def get_entity_65_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity65]:
        return self.db.query(HealthModelEntity65).offset(skip).limit(limit).all()

    def get_entity_65_by_id(self, entity_id: int) -> Optional[HealthModelEntity65]:
        return self.db.query(HealthModelEntity65).filter(HealthModelEntity65.id == entity_id).first()

    def create_entity_65(self, payload: HealthSchemaEntity65Create) -> HealthModelEntity65:
        db_obj = HealthModelEntity65(
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

    def update_entity_65(self, entity_id: int, payload: HealthSchemaEntity65Update) -> Optional[HealthModelEntity65]:
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

    def get_entity_66_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity66]:
        return self.db.query(HealthModelEntity66).offset(skip).limit(limit).all()

    def get_entity_66_by_id(self, entity_id: int) -> Optional[HealthModelEntity66]:
        return self.db.query(HealthModelEntity66).filter(HealthModelEntity66.id == entity_id).first()

    def create_entity_66(self, payload: HealthSchemaEntity66Create) -> HealthModelEntity66:
        db_obj = HealthModelEntity66(
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

    def update_entity_66(self, entity_id: int, payload: HealthSchemaEntity66Update) -> Optional[HealthModelEntity66]:
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

    def get_entity_67_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity67]:
        return self.db.query(HealthModelEntity67).offset(skip).limit(limit).all()

    def get_entity_67_by_id(self, entity_id: int) -> Optional[HealthModelEntity67]:
        return self.db.query(HealthModelEntity67).filter(HealthModelEntity67.id == entity_id).first()

    def create_entity_67(self, payload: HealthSchemaEntity67Create) -> HealthModelEntity67:
        db_obj = HealthModelEntity67(
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

    def update_entity_67(self, entity_id: int, payload: HealthSchemaEntity67Update) -> Optional[HealthModelEntity67]:
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

    def get_entity_68_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity68]:
        return self.db.query(HealthModelEntity68).offset(skip).limit(limit).all()

    def get_entity_68_by_id(self, entity_id: int) -> Optional[HealthModelEntity68]:
        return self.db.query(HealthModelEntity68).filter(HealthModelEntity68.id == entity_id).first()

    def create_entity_68(self, payload: HealthSchemaEntity68Create) -> HealthModelEntity68:
        db_obj = HealthModelEntity68(
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

    def update_entity_68(self, entity_id: int, payload: HealthSchemaEntity68Update) -> Optional[HealthModelEntity68]:
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

    def get_entity_69_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity69]:
        return self.db.query(HealthModelEntity69).offset(skip).limit(limit).all()

    def get_entity_69_by_id(self, entity_id: int) -> Optional[HealthModelEntity69]:
        return self.db.query(HealthModelEntity69).filter(HealthModelEntity69.id == entity_id).first()

    def create_entity_69(self, payload: HealthSchemaEntity69Create) -> HealthModelEntity69:
        db_obj = HealthModelEntity69(
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

    def update_entity_69(self, entity_id: int, payload: HealthSchemaEntity69Update) -> Optional[HealthModelEntity69]:
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

    def get_entity_70_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity70]:
        return self.db.query(HealthModelEntity70).offset(skip).limit(limit).all()

    def get_entity_70_by_id(self, entity_id: int) -> Optional[HealthModelEntity70]:
        return self.db.query(HealthModelEntity70).filter(HealthModelEntity70.id == entity_id).first()

    def create_entity_70(self, payload: HealthSchemaEntity70Create) -> HealthModelEntity70:
        db_obj = HealthModelEntity70(
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

    def update_entity_70(self, entity_id: int, payload: HealthSchemaEntity70Update) -> Optional[HealthModelEntity70]:
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

    def get_entity_71_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity71]:
        return self.db.query(HealthModelEntity71).offset(skip).limit(limit).all()

    def get_entity_71_by_id(self, entity_id: int) -> Optional[HealthModelEntity71]:
        return self.db.query(HealthModelEntity71).filter(HealthModelEntity71.id == entity_id).first()

    def create_entity_71(self, payload: HealthSchemaEntity71Create) -> HealthModelEntity71:
        db_obj = HealthModelEntity71(
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

    def update_entity_71(self, entity_id: int, payload: HealthSchemaEntity71Update) -> Optional[HealthModelEntity71]:
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

    def get_entity_72_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity72]:
        return self.db.query(HealthModelEntity72).offset(skip).limit(limit).all()

    def get_entity_72_by_id(self, entity_id: int) -> Optional[HealthModelEntity72]:
        return self.db.query(HealthModelEntity72).filter(HealthModelEntity72.id == entity_id).first()

    def create_entity_72(self, payload: HealthSchemaEntity72Create) -> HealthModelEntity72:
        db_obj = HealthModelEntity72(
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

    def update_entity_72(self, entity_id: int, payload: HealthSchemaEntity72Update) -> Optional[HealthModelEntity72]:
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

    def get_entity_73_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity73]:
        return self.db.query(HealthModelEntity73).offset(skip).limit(limit).all()

    def get_entity_73_by_id(self, entity_id: int) -> Optional[HealthModelEntity73]:
        return self.db.query(HealthModelEntity73).filter(HealthModelEntity73.id == entity_id).first()

    def create_entity_73(self, payload: HealthSchemaEntity73Create) -> HealthModelEntity73:
        db_obj = HealthModelEntity73(
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

    def update_entity_73(self, entity_id: int, payload: HealthSchemaEntity73Update) -> Optional[HealthModelEntity73]:
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

    def get_entity_74_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity74]:
        return self.db.query(HealthModelEntity74).offset(skip).limit(limit).all()

    def get_entity_74_by_id(self, entity_id: int) -> Optional[HealthModelEntity74]:
        return self.db.query(HealthModelEntity74).filter(HealthModelEntity74.id == entity_id).first()

    def create_entity_74(self, payload: HealthSchemaEntity74Create) -> HealthModelEntity74:
        db_obj = HealthModelEntity74(
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

    def update_entity_74(self, entity_id: int, payload: HealthSchemaEntity74Update) -> Optional[HealthModelEntity74]:
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

    def get_entity_75_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity75]:
        return self.db.query(HealthModelEntity75).offset(skip).limit(limit).all()

    def get_entity_75_by_id(self, entity_id: int) -> Optional[HealthModelEntity75]:
        return self.db.query(HealthModelEntity75).filter(HealthModelEntity75.id == entity_id).first()

    def create_entity_75(self, payload: HealthSchemaEntity75Create) -> HealthModelEntity75:
        db_obj = HealthModelEntity75(
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

    def update_entity_75(self, entity_id: int, payload: HealthSchemaEntity75Update) -> Optional[HealthModelEntity75]:
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

    def get_entity_76_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity76]:
        return self.db.query(HealthModelEntity76).offset(skip).limit(limit).all()

    def get_entity_76_by_id(self, entity_id: int) -> Optional[HealthModelEntity76]:
        return self.db.query(HealthModelEntity76).filter(HealthModelEntity76.id == entity_id).first()

    def create_entity_76(self, payload: HealthSchemaEntity76Create) -> HealthModelEntity76:
        db_obj = HealthModelEntity76(
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

    def update_entity_76(self, entity_id: int, payload: HealthSchemaEntity76Update) -> Optional[HealthModelEntity76]:
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

    def get_entity_77_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity77]:
        return self.db.query(HealthModelEntity77).offset(skip).limit(limit).all()

    def get_entity_77_by_id(self, entity_id: int) -> Optional[HealthModelEntity77]:
        return self.db.query(HealthModelEntity77).filter(HealthModelEntity77.id == entity_id).first()

    def create_entity_77(self, payload: HealthSchemaEntity77Create) -> HealthModelEntity77:
        db_obj = HealthModelEntity77(
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

    def update_entity_77(self, entity_id: int, payload: HealthSchemaEntity77Update) -> Optional[HealthModelEntity77]:
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

    def get_entity_78_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity78]:
        return self.db.query(HealthModelEntity78).offset(skip).limit(limit).all()

    def get_entity_78_by_id(self, entity_id: int) -> Optional[HealthModelEntity78]:
        return self.db.query(HealthModelEntity78).filter(HealthModelEntity78.id == entity_id).first()

    def create_entity_78(self, payload: HealthSchemaEntity78Create) -> HealthModelEntity78:
        db_obj = HealthModelEntity78(
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

    def update_entity_78(self, entity_id: int, payload: HealthSchemaEntity78Update) -> Optional[HealthModelEntity78]:
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

    def get_entity_79_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity79]:
        return self.db.query(HealthModelEntity79).offset(skip).limit(limit).all()

    def get_entity_79_by_id(self, entity_id: int) -> Optional[HealthModelEntity79]:
        return self.db.query(HealthModelEntity79).filter(HealthModelEntity79.id == entity_id).first()

    def create_entity_79(self, payload: HealthSchemaEntity79Create) -> HealthModelEntity79:
        db_obj = HealthModelEntity79(
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

    def update_entity_79(self, entity_id: int, payload: HealthSchemaEntity79Update) -> Optional[HealthModelEntity79]:
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

    def get_entity_80_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity80]:
        return self.db.query(HealthModelEntity80).offset(skip).limit(limit).all()

    def get_entity_80_by_id(self, entity_id: int) -> Optional[HealthModelEntity80]:
        return self.db.query(HealthModelEntity80).filter(HealthModelEntity80.id == entity_id).first()

    def create_entity_80(self, payload: HealthSchemaEntity80Create) -> HealthModelEntity80:
        db_obj = HealthModelEntity80(
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

    def update_entity_80(self, entity_id: int, payload: HealthSchemaEntity80Update) -> Optional[HealthModelEntity80]:
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

    def get_entity_81_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity81]:
        return self.db.query(HealthModelEntity81).offset(skip).limit(limit).all()

    def get_entity_81_by_id(self, entity_id: int) -> Optional[HealthModelEntity81]:
        return self.db.query(HealthModelEntity81).filter(HealthModelEntity81.id == entity_id).first()

    def create_entity_81(self, payload: HealthSchemaEntity81Create) -> HealthModelEntity81:
        db_obj = HealthModelEntity81(
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

    def update_entity_81(self, entity_id: int, payload: HealthSchemaEntity81Update) -> Optional[HealthModelEntity81]:
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

    def get_entity_82_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity82]:
        return self.db.query(HealthModelEntity82).offset(skip).limit(limit).all()

    def get_entity_82_by_id(self, entity_id: int) -> Optional[HealthModelEntity82]:
        return self.db.query(HealthModelEntity82).filter(HealthModelEntity82.id == entity_id).first()

    def create_entity_82(self, payload: HealthSchemaEntity82Create) -> HealthModelEntity82:
        db_obj = HealthModelEntity82(
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

    def update_entity_82(self, entity_id: int, payload: HealthSchemaEntity82Update) -> Optional[HealthModelEntity82]:
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

    def get_entity_83_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity83]:
        return self.db.query(HealthModelEntity83).offset(skip).limit(limit).all()

    def get_entity_83_by_id(self, entity_id: int) -> Optional[HealthModelEntity83]:
        return self.db.query(HealthModelEntity83).filter(HealthModelEntity83.id == entity_id).first()

    def create_entity_83(self, payload: HealthSchemaEntity83Create) -> HealthModelEntity83:
        db_obj = HealthModelEntity83(
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

    def update_entity_83(self, entity_id: int, payload: HealthSchemaEntity83Update) -> Optional[HealthModelEntity83]:
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

    def get_entity_84_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity84]:
        return self.db.query(HealthModelEntity84).offset(skip).limit(limit).all()

    def get_entity_84_by_id(self, entity_id: int) -> Optional[HealthModelEntity84]:
        return self.db.query(HealthModelEntity84).filter(HealthModelEntity84.id == entity_id).first()

    def create_entity_84(self, payload: HealthSchemaEntity84Create) -> HealthModelEntity84:
        db_obj = HealthModelEntity84(
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

    def update_entity_84(self, entity_id: int, payload: HealthSchemaEntity84Update) -> Optional[HealthModelEntity84]:
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

    def get_entity_85_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity85]:
        return self.db.query(HealthModelEntity85).offset(skip).limit(limit).all()

    def get_entity_85_by_id(self, entity_id: int) -> Optional[HealthModelEntity85]:
        return self.db.query(HealthModelEntity85).filter(HealthModelEntity85.id == entity_id).first()

    def create_entity_85(self, payload: HealthSchemaEntity85Create) -> HealthModelEntity85:
        db_obj = HealthModelEntity85(
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

    def update_entity_85(self, entity_id: int, payload: HealthSchemaEntity85Update) -> Optional[HealthModelEntity85]:
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

    def get_entity_86_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity86]:
        return self.db.query(HealthModelEntity86).offset(skip).limit(limit).all()

    def get_entity_86_by_id(self, entity_id: int) -> Optional[HealthModelEntity86]:
        return self.db.query(HealthModelEntity86).filter(HealthModelEntity86.id == entity_id).first()

    def create_entity_86(self, payload: HealthSchemaEntity86Create) -> HealthModelEntity86:
        db_obj = HealthModelEntity86(
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

    def update_entity_86(self, entity_id: int, payload: HealthSchemaEntity86Update) -> Optional[HealthModelEntity86]:
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

    def get_entity_87_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity87]:
        return self.db.query(HealthModelEntity87).offset(skip).limit(limit).all()

    def get_entity_87_by_id(self, entity_id: int) -> Optional[HealthModelEntity87]:
        return self.db.query(HealthModelEntity87).filter(HealthModelEntity87.id == entity_id).first()

    def create_entity_87(self, payload: HealthSchemaEntity87Create) -> HealthModelEntity87:
        db_obj = HealthModelEntity87(
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

    def update_entity_87(self, entity_id: int, payload: HealthSchemaEntity87Update) -> Optional[HealthModelEntity87]:
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

    def get_entity_88_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity88]:
        return self.db.query(HealthModelEntity88).offset(skip).limit(limit).all()

    def get_entity_88_by_id(self, entity_id: int) -> Optional[HealthModelEntity88]:
        return self.db.query(HealthModelEntity88).filter(HealthModelEntity88.id == entity_id).first()

    def create_entity_88(self, payload: HealthSchemaEntity88Create) -> HealthModelEntity88:
        db_obj = HealthModelEntity88(
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

    def update_entity_88(self, entity_id: int, payload: HealthSchemaEntity88Update) -> Optional[HealthModelEntity88]:
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

    def get_entity_89_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity89]:
        return self.db.query(HealthModelEntity89).offset(skip).limit(limit).all()

    def get_entity_89_by_id(self, entity_id: int) -> Optional[HealthModelEntity89]:
        return self.db.query(HealthModelEntity89).filter(HealthModelEntity89.id == entity_id).first()

    def create_entity_89(self, payload: HealthSchemaEntity89Create) -> HealthModelEntity89:
        db_obj = HealthModelEntity89(
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

    def update_entity_89(self, entity_id: int, payload: HealthSchemaEntity89Update) -> Optional[HealthModelEntity89]:
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

    def get_entity_90_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity90]:
        return self.db.query(HealthModelEntity90).offset(skip).limit(limit).all()

    def get_entity_90_by_id(self, entity_id: int) -> Optional[HealthModelEntity90]:
        return self.db.query(HealthModelEntity90).filter(HealthModelEntity90.id == entity_id).first()

    def create_entity_90(self, payload: HealthSchemaEntity90Create) -> HealthModelEntity90:
        db_obj = HealthModelEntity90(
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

    def update_entity_90(self, entity_id: int, payload: HealthSchemaEntity90Update) -> Optional[HealthModelEntity90]:
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

    def get_entity_91_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity91]:
        return self.db.query(HealthModelEntity91).offset(skip).limit(limit).all()

    def get_entity_91_by_id(self, entity_id: int) -> Optional[HealthModelEntity91]:
        return self.db.query(HealthModelEntity91).filter(HealthModelEntity91.id == entity_id).first()

    def create_entity_91(self, payload: HealthSchemaEntity91Create) -> HealthModelEntity91:
        db_obj = HealthModelEntity91(
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

    def update_entity_91(self, entity_id: int, payload: HealthSchemaEntity91Update) -> Optional[HealthModelEntity91]:
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

    def get_entity_92_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity92]:
        return self.db.query(HealthModelEntity92).offset(skip).limit(limit).all()

    def get_entity_92_by_id(self, entity_id: int) -> Optional[HealthModelEntity92]:
        return self.db.query(HealthModelEntity92).filter(HealthModelEntity92.id == entity_id).first()

    def create_entity_92(self, payload: HealthSchemaEntity92Create) -> HealthModelEntity92:
        db_obj = HealthModelEntity92(
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

    def update_entity_92(self, entity_id: int, payload: HealthSchemaEntity92Update) -> Optional[HealthModelEntity92]:
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

    def get_entity_93_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity93]:
        return self.db.query(HealthModelEntity93).offset(skip).limit(limit).all()

    def get_entity_93_by_id(self, entity_id: int) -> Optional[HealthModelEntity93]:
        return self.db.query(HealthModelEntity93).filter(HealthModelEntity93.id == entity_id).first()

    def create_entity_93(self, payload: HealthSchemaEntity93Create) -> HealthModelEntity93:
        db_obj = HealthModelEntity93(
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

    def update_entity_93(self, entity_id: int, payload: HealthSchemaEntity93Update) -> Optional[HealthModelEntity93]:
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

    def get_entity_94_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity94]:
        return self.db.query(HealthModelEntity94).offset(skip).limit(limit).all()

    def get_entity_94_by_id(self, entity_id: int) -> Optional[HealthModelEntity94]:
        return self.db.query(HealthModelEntity94).filter(HealthModelEntity94.id == entity_id).first()

    def create_entity_94(self, payload: HealthSchemaEntity94Create) -> HealthModelEntity94:
        db_obj = HealthModelEntity94(
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

    def update_entity_94(self, entity_id: int, payload: HealthSchemaEntity94Update) -> Optional[HealthModelEntity94]:
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

    def get_entity_95_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity95]:
        return self.db.query(HealthModelEntity95).offset(skip).limit(limit).all()

    def get_entity_95_by_id(self, entity_id: int) -> Optional[HealthModelEntity95]:
        return self.db.query(HealthModelEntity95).filter(HealthModelEntity95.id == entity_id).first()

    def create_entity_95(self, payload: HealthSchemaEntity95Create) -> HealthModelEntity95:
        db_obj = HealthModelEntity95(
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

    def update_entity_95(self, entity_id: int, payload: HealthSchemaEntity95Update) -> Optional[HealthModelEntity95]:
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

    def get_entity_96_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity96]:
        return self.db.query(HealthModelEntity96).offset(skip).limit(limit).all()

    def get_entity_96_by_id(self, entity_id: int) -> Optional[HealthModelEntity96]:
        return self.db.query(HealthModelEntity96).filter(HealthModelEntity96.id == entity_id).first()

    def create_entity_96(self, payload: HealthSchemaEntity96Create) -> HealthModelEntity96:
        db_obj = HealthModelEntity96(
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

    def update_entity_96(self, entity_id: int, payload: HealthSchemaEntity96Update) -> Optional[HealthModelEntity96]:
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

    def get_entity_97_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity97]:
        return self.db.query(HealthModelEntity97).offset(skip).limit(limit).all()

    def get_entity_97_by_id(self, entity_id: int) -> Optional[HealthModelEntity97]:
        return self.db.query(HealthModelEntity97).filter(HealthModelEntity97.id == entity_id).first()

    def create_entity_97(self, payload: HealthSchemaEntity97Create) -> HealthModelEntity97:
        db_obj = HealthModelEntity97(
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

    def update_entity_97(self, entity_id: int, payload: HealthSchemaEntity97Update) -> Optional[HealthModelEntity97]:
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

    def get_entity_98_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity98]:
        return self.db.query(HealthModelEntity98).offset(skip).limit(limit).all()

    def get_entity_98_by_id(self, entity_id: int) -> Optional[HealthModelEntity98]:
        return self.db.query(HealthModelEntity98).filter(HealthModelEntity98.id == entity_id).first()

    def create_entity_98(self, payload: HealthSchemaEntity98Create) -> HealthModelEntity98:
        db_obj = HealthModelEntity98(
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

    def update_entity_98(self, entity_id: int, payload: HealthSchemaEntity98Update) -> Optional[HealthModelEntity98]:
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

    def get_entity_99_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity99]:
        return self.db.query(HealthModelEntity99).offset(skip).limit(limit).all()

    def get_entity_99_by_id(self, entity_id: int) -> Optional[HealthModelEntity99]:
        return self.db.query(HealthModelEntity99).filter(HealthModelEntity99.id == entity_id).first()

    def create_entity_99(self, payload: HealthSchemaEntity99Create) -> HealthModelEntity99:
        db_obj = HealthModelEntity99(
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

    def update_entity_99(self, entity_id: int, payload: HealthSchemaEntity99Update) -> Optional[HealthModelEntity99]:
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

    def get_entity_100_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity100]:
        return self.db.query(HealthModelEntity100).offset(skip).limit(limit).all()

    def get_entity_100_by_id(self, entity_id: int) -> Optional[HealthModelEntity100]:
        return self.db.query(HealthModelEntity100).filter(HealthModelEntity100.id == entity_id).first()

    def create_entity_100(self, payload: HealthSchemaEntity100Create) -> HealthModelEntity100:
        db_obj = HealthModelEntity100(
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

    def update_entity_100(self, entity_id: int, payload: HealthSchemaEntity100Update) -> Optional[HealthModelEntity100]:
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

    def get_entity_101_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity101]:
        return self.db.query(HealthModelEntity101).offset(skip).limit(limit).all()

    def get_entity_101_by_id(self, entity_id: int) -> Optional[HealthModelEntity101]:
        return self.db.query(HealthModelEntity101).filter(HealthModelEntity101.id == entity_id).first()

    def create_entity_101(self, payload: HealthSchemaEntity101Create) -> HealthModelEntity101:
        db_obj = HealthModelEntity101(
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

    def update_entity_101(self, entity_id: int, payload: HealthSchemaEntity101Update) -> Optional[HealthModelEntity101]:
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

    def get_entity_102_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity102]:
        return self.db.query(HealthModelEntity102).offset(skip).limit(limit).all()

    def get_entity_102_by_id(self, entity_id: int) -> Optional[HealthModelEntity102]:
        return self.db.query(HealthModelEntity102).filter(HealthModelEntity102.id == entity_id).first()

    def create_entity_102(self, payload: HealthSchemaEntity102Create) -> HealthModelEntity102:
        db_obj = HealthModelEntity102(
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

    def update_entity_102(self, entity_id: int, payload: HealthSchemaEntity102Update) -> Optional[HealthModelEntity102]:
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

    def get_entity_103_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity103]:
        return self.db.query(HealthModelEntity103).offset(skip).limit(limit).all()

    def get_entity_103_by_id(self, entity_id: int) -> Optional[HealthModelEntity103]:
        return self.db.query(HealthModelEntity103).filter(HealthModelEntity103.id == entity_id).first()

    def create_entity_103(self, payload: HealthSchemaEntity103Create) -> HealthModelEntity103:
        db_obj = HealthModelEntity103(
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

    def update_entity_103(self, entity_id: int, payload: HealthSchemaEntity103Update) -> Optional[HealthModelEntity103]:
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

    def get_entity_104_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity104]:
        return self.db.query(HealthModelEntity104).offset(skip).limit(limit).all()

    def get_entity_104_by_id(self, entity_id: int) -> Optional[HealthModelEntity104]:
        return self.db.query(HealthModelEntity104).filter(HealthModelEntity104.id == entity_id).first()

    def create_entity_104(self, payload: HealthSchemaEntity104Create) -> HealthModelEntity104:
        db_obj = HealthModelEntity104(
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

    def update_entity_104(self, entity_id: int, payload: HealthSchemaEntity104Update) -> Optional[HealthModelEntity104]:
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

    def get_entity_105_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity105]:
        return self.db.query(HealthModelEntity105).offset(skip).limit(limit).all()

    def get_entity_105_by_id(self, entity_id: int) -> Optional[HealthModelEntity105]:
        return self.db.query(HealthModelEntity105).filter(HealthModelEntity105.id == entity_id).first()

    def create_entity_105(self, payload: HealthSchemaEntity105Create) -> HealthModelEntity105:
        db_obj = HealthModelEntity105(
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

    def update_entity_105(self, entity_id: int, payload: HealthSchemaEntity105Update) -> Optional[HealthModelEntity105]:
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

    def get_entity_106_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity106]:
        return self.db.query(HealthModelEntity106).offset(skip).limit(limit).all()

    def get_entity_106_by_id(self, entity_id: int) -> Optional[HealthModelEntity106]:
        return self.db.query(HealthModelEntity106).filter(HealthModelEntity106.id == entity_id).first()

    def create_entity_106(self, payload: HealthSchemaEntity106Create) -> HealthModelEntity106:
        db_obj = HealthModelEntity106(
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

    def update_entity_106(self, entity_id: int, payload: HealthSchemaEntity106Update) -> Optional[HealthModelEntity106]:
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

    def get_entity_107_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity107]:
        return self.db.query(HealthModelEntity107).offset(skip).limit(limit).all()

    def get_entity_107_by_id(self, entity_id: int) -> Optional[HealthModelEntity107]:
        return self.db.query(HealthModelEntity107).filter(HealthModelEntity107.id == entity_id).first()

    def create_entity_107(self, payload: HealthSchemaEntity107Create) -> HealthModelEntity107:
        db_obj = HealthModelEntity107(
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

    def update_entity_107(self, entity_id: int, payload: HealthSchemaEntity107Update) -> Optional[HealthModelEntity107]:
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

    def get_entity_108_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity108]:
        return self.db.query(HealthModelEntity108).offset(skip).limit(limit).all()

    def get_entity_108_by_id(self, entity_id: int) -> Optional[HealthModelEntity108]:
        return self.db.query(HealthModelEntity108).filter(HealthModelEntity108.id == entity_id).first()

    def create_entity_108(self, payload: HealthSchemaEntity108Create) -> HealthModelEntity108:
        db_obj = HealthModelEntity108(
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

    def update_entity_108(self, entity_id: int, payload: HealthSchemaEntity108Update) -> Optional[HealthModelEntity108]:
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

    def get_entity_109_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity109]:
        return self.db.query(HealthModelEntity109).offset(skip).limit(limit).all()

    def get_entity_109_by_id(self, entity_id: int) -> Optional[HealthModelEntity109]:
        return self.db.query(HealthModelEntity109).filter(HealthModelEntity109.id == entity_id).first()

    def create_entity_109(self, payload: HealthSchemaEntity109Create) -> HealthModelEntity109:
        db_obj = HealthModelEntity109(
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

    def update_entity_109(self, entity_id: int, payload: HealthSchemaEntity109Update) -> Optional[HealthModelEntity109]:
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

    def get_entity_110_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity110]:
        return self.db.query(HealthModelEntity110).offset(skip).limit(limit).all()

    def get_entity_110_by_id(self, entity_id: int) -> Optional[HealthModelEntity110]:
        return self.db.query(HealthModelEntity110).filter(HealthModelEntity110.id == entity_id).first()

    def create_entity_110(self, payload: HealthSchemaEntity110Create) -> HealthModelEntity110:
        db_obj = HealthModelEntity110(
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

    def update_entity_110(self, entity_id: int, payload: HealthSchemaEntity110Update) -> Optional[HealthModelEntity110]:
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

    def get_entity_111_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity111]:
        return self.db.query(HealthModelEntity111).offset(skip).limit(limit).all()

    def get_entity_111_by_id(self, entity_id: int) -> Optional[HealthModelEntity111]:
        return self.db.query(HealthModelEntity111).filter(HealthModelEntity111.id == entity_id).first()

    def create_entity_111(self, payload: HealthSchemaEntity111Create) -> HealthModelEntity111:
        db_obj = HealthModelEntity111(
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

    def update_entity_111(self, entity_id: int, payload: HealthSchemaEntity111Update) -> Optional[HealthModelEntity111]:
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

    def get_entity_112_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity112]:
        return self.db.query(HealthModelEntity112).offset(skip).limit(limit).all()

    def get_entity_112_by_id(self, entity_id: int) -> Optional[HealthModelEntity112]:
        return self.db.query(HealthModelEntity112).filter(HealthModelEntity112.id == entity_id).first()

    def create_entity_112(self, payload: HealthSchemaEntity112Create) -> HealthModelEntity112:
        db_obj = HealthModelEntity112(
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

    def update_entity_112(self, entity_id: int, payload: HealthSchemaEntity112Update) -> Optional[HealthModelEntity112]:
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

    def get_entity_113_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity113]:
        return self.db.query(HealthModelEntity113).offset(skip).limit(limit).all()

    def get_entity_113_by_id(self, entity_id: int) -> Optional[HealthModelEntity113]:
        return self.db.query(HealthModelEntity113).filter(HealthModelEntity113.id == entity_id).first()

    def create_entity_113(self, payload: HealthSchemaEntity113Create) -> HealthModelEntity113:
        db_obj = HealthModelEntity113(
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

    def update_entity_113(self, entity_id: int, payload: HealthSchemaEntity113Update) -> Optional[HealthModelEntity113]:
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

    def get_entity_114_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity114]:
        return self.db.query(HealthModelEntity114).offset(skip).limit(limit).all()

    def get_entity_114_by_id(self, entity_id: int) -> Optional[HealthModelEntity114]:
        return self.db.query(HealthModelEntity114).filter(HealthModelEntity114.id == entity_id).first()

    def create_entity_114(self, payload: HealthSchemaEntity114Create) -> HealthModelEntity114:
        db_obj = HealthModelEntity114(
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

    def update_entity_114(self, entity_id: int, payload: HealthSchemaEntity114Update) -> Optional[HealthModelEntity114]:
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

    def get_entity_115_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity115]:
        return self.db.query(HealthModelEntity115).offset(skip).limit(limit).all()

    def get_entity_115_by_id(self, entity_id: int) -> Optional[HealthModelEntity115]:
        return self.db.query(HealthModelEntity115).filter(HealthModelEntity115.id == entity_id).first()

    def create_entity_115(self, payload: HealthSchemaEntity115Create) -> HealthModelEntity115:
        db_obj = HealthModelEntity115(
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

    def update_entity_115(self, entity_id: int, payload: HealthSchemaEntity115Update) -> Optional[HealthModelEntity115]:
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

    def get_entity_116_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity116]:
        return self.db.query(HealthModelEntity116).offset(skip).limit(limit).all()

    def get_entity_116_by_id(self, entity_id: int) -> Optional[HealthModelEntity116]:
        return self.db.query(HealthModelEntity116).filter(HealthModelEntity116.id == entity_id).first()

    def create_entity_116(self, payload: HealthSchemaEntity116Create) -> HealthModelEntity116:
        db_obj = HealthModelEntity116(
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

    def update_entity_116(self, entity_id: int, payload: HealthSchemaEntity116Update) -> Optional[HealthModelEntity116]:
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

    def get_entity_117_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity117]:
        return self.db.query(HealthModelEntity117).offset(skip).limit(limit).all()

    def get_entity_117_by_id(self, entity_id: int) -> Optional[HealthModelEntity117]:
        return self.db.query(HealthModelEntity117).filter(HealthModelEntity117.id == entity_id).first()

    def create_entity_117(self, payload: HealthSchemaEntity117Create) -> HealthModelEntity117:
        db_obj = HealthModelEntity117(
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

    def update_entity_117(self, entity_id: int, payload: HealthSchemaEntity117Update) -> Optional[HealthModelEntity117]:
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

    def get_entity_118_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity118]:
        return self.db.query(HealthModelEntity118).offset(skip).limit(limit).all()

    def get_entity_118_by_id(self, entity_id: int) -> Optional[HealthModelEntity118]:
        return self.db.query(HealthModelEntity118).filter(HealthModelEntity118.id == entity_id).first()

    def create_entity_118(self, payload: HealthSchemaEntity118Create) -> HealthModelEntity118:
        db_obj = HealthModelEntity118(
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

    def update_entity_118(self, entity_id: int, payload: HealthSchemaEntity118Update) -> Optional[HealthModelEntity118]:
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

    def get_entity_119_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity119]:
        return self.db.query(HealthModelEntity119).offset(skip).limit(limit).all()

    def get_entity_119_by_id(self, entity_id: int) -> Optional[HealthModelEntity119]:
        return self.db.query(HealthModelEntity119).filter(HealthModelEntity119.id == entity_id).first()

    def create_entity_119(self, payload: HealthSchemaEntity119Create) -> HealthModelEntity119:
        db_obj = HealthModelEntity119(
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

    def update_entity_119(self, entity_id: int, payload: HealthSchemaEntity119Update) -> Optional[HealthModelEntity119]:
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

    def get_entity_120_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity120]:
        return self.db.query(HealthModelEntity120).offset(skip).limit(limit).all()

    def get_entity_120_by_id(self, entity_id: int) -> Optional[HealthModelEntity120]:
        return self.db.query(HealthModelEntity120).filter(HealthModelEntity120.id == entity_id).first()

    def create_entity_120(self, payload: HealthSchemaEntity120Create) -> HealthModelEntity120:
        db_obj = HealthModelEntity120(
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

    def update_entity_120(self, entity_id: int, payload: HealthSchemaEntity120Update) -> Optional[HealthModelEntity120]:
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

    def get_entity_121_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity121]:
        return self.db.query(HealthModelEntity121).offset(skip).limit(limit).all()

    def get_entity_121_by_id(self, entity_id: int) -> Optional[HealthModelEntity121]:
        return self.db.query(HealthModelEntity121).filter(HealthModelEntity121.id == entity_id).first()

    def create_entity_121(self, payload: HealthSchemaEntity121Create) -> HealthModelEntity121:
        db_obj = HealthModelEntity121(
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

    def update_entity_121(self, entity_id: int, payload: HealthSchemaEntity121Update) -> Optional[HealthModelEntity121]:
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

    def get_entity_122_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity122]:
        return self.db.query(HealthModelEntity122).offset(skip).limit(limit).all()

    def get_entity_122_by_id(self, entity_id: int) -> Optional[HealthModelEntity122]:
        return self.db.query(HealthModelEntity122).filter(HealthModelEntity122.id == entity_id).first()

    def create_entity_122(self, payload: HealthSchemaEntity122Create) -> HealthModelEntity122:
        db_obj = HealthModelEntity122(
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

    def update_entity_122(self, entity_id: int, payload: HealthSchemaEntity122Update) -> Optional[HealthModelEntity122]:
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

    def get_entity_123_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity123]:
        return self.db.query(HealthModelEntity123).offset(skip).limit(limit).all()

    def get_entity_123_by_id(self, entity_id: int) -> Optional[HealthModelEntity123]:
        return self.db.query(HealthModelEntity123).filter(HealthModelEntity123.id == entity_id).first()

    def create_entity_123(self, payload: HealthSchemaEntity123Create) -> HealthModelEntity123:
        db_obj = HealthModelEntity123(
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

    def update_entity_123(self, entity_id: int, payload: HealthSchemaEntity123Update) -> Optional[HealthModelEntity123]:
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

    def get_entity_124_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity124]:
        return self.db.query(HealthModelEntity124).offset(skip).limit(limit).all()

    def get_entity_124_by_id(self, entity_id: int) -> Optional[HealthModelEntity124]:
        return self.db.query(HealthModelEntity124).filter(HealthModelEntity124.id == entity_id).first()

    def create_entity_124(self, payload: HealthSchemaEntity124Create) -> HealthModelEntity124:
        db_obj = HealthModelEntity124(
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

    def update_entity_124(self, entity_id: int, payload: HealthSchemaEntity124Update) -> Optional[HealthModelEntity124]:
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

    def get_entity_125_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity125]:
        return self.db.query(HealthModelEntity125).offset(skip).limit(limit).all()

    def get_entity_125_by_id(self, entity_id: int) -> Optional[HealthModelEntity125]:
        return self.db.query(HealthModelEntity125).filter(HealthModelEntity125.id == entity_id).first()

    def create_entity_125(self, payload: HealthSchemaEntity125Create) -> HealthModelEntity125:
        db_obj = HealthModelEntity125(
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

    def update_entity_125(self, entity_id: int, payload: HealthSchemaEntity125Update) -> Optional[HealthModelEntity125]:
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

    def get_entity_126_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity126]:
        return self.db.query(HealthModelEntity126).offset(skip).limit(limit).all()

    def get_entity_126_by_id(self, entity_id: int) -> Optional[HealthModelEntity126]:
        return self.db.query(HealthModelEntity126).filter(HealthModelEntity126.id == entity_id).first()

    def create_entity_126(self, payload: HealthSchemaEntity126Create) -> HealthModelEntity126:
        db_obj = HealthModelEntity126(
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

    def update_entity_126(self, entity_id: int, payload: HealthSchemaEntity126Update) -> Optional[HealthModelEntity126]:
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

    def get_entity_127_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity127]:
        return self.db.query(HealthModelEntity127).offset(skip).limit(limit).all()

    def get_entity_127_by_id(self, entity_id: int) -> Optional[HealthModelEntity127]:
        return self.db.query(HealthModelEntity127).filter(HealthModelEntity127.id == entity_id).first()

    def create_entity_127(self, payload: HealthSchemaEntity127Create) -> HealthModelEntity127:
        db_obj = HealthModelEntity127(
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

    def update_entity_127(self, entity_id: int, payload: HealthSchemaEntity127Update) -> Optional[HealthModelEntity127]:
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

    def get_entity_128_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity128]:
        return self.db.query(HealthModelEntity128).offset(skip).limit(limit).all()

    def get_entity_128_by_id(self, entity_id: int) -> Optional[HealthModelEntity128]:
        return self.db.query(HealthModelEntity128).filter(HealthModelEntity128.id == entity_id).first()

    def create_entity_128(self, payload: HealthSchemaEntity128Create) -> HealthModelEntity128:
        db_obj = HealthModelEntity128(
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

    def update_entity_128(self, entity_id: int, payload: HealthSchemaEntity128Update) -> Optional[HealthModelEntity128]:
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

    def get_entity_129_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity129]:
        return self.db.query(HealthModelEntity129).offset(skip).limit(limit).all()

    def get_entity_129_by_id(self, entity_id: int) -> Optional[HealthModelEntity129]:
        return self.db.query(HealthModelEntity129).filter(HealthModelEntity129.id == entity_id).first()

    def create_entity_129(self, payload: HealthSchemaEntity129Create) -> HealthModelEntity129:
        db_obj = HealthModelEntity129(
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

    def update_entity_129(self, entity_id: int, payload: HealthSchemaEntity129Update) -> Optional[HealthModelEntity129]:
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

    def get_entity_130_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity130]:
        return self.db.query(HealthModelEntity130).offset(skip).limit(limit).all()

    def get_entity_130_by_id(self, entity_id: int) -> Optional[HealthModelEntity130]:
        return self.db.query(HealthModelEntity130).filter(HealthModelEntity130.id == entity_id).first()

    def create_entity_130(self, payload: HealthSchemaEntity130Create) -> HealthModelEntity130:
        db_obj = HealthModelEntity130(
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

    def update_entity_130(self, entity_id: int, payload: HealthSchemaEntity130Update) -> Optional[HealthModelEntity130]:
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

    def get_entity_131_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity131]:
        return self.db.query(HealthModelEntity131).offset(skip).limit(limit).all()

    def get_entity_131_by_id(self, entity_id: int) -> Optional[HealthModelEntity131]:
        return self.db.query(HealthModelEntity131).filter(HealthModelEntity131.id == entity_id).first()

    def create_entity_131(self, payload: HealthSchemaEntity131Create) -> HealthModelEntity131:
        db_obj = HealthModelEntity131(
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

    def update_entity_131(self, entity_id: int, payload: HealthSchemaEntity131Update) -> Optional[HealthModelEntity131]:
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

    def get_entity_132_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity132]:
        return self.db.query(HealthModelEntity132).offset(skip).limit(limit).all()

    def get_entity_132_by_id(self, entity_id: int) -> Optional[HealthModelEntity132]:
        return self.db.query(HealthModelEntity132).filter(HealthModelEntity132.id == entity_id).first()

    def create_entity_132(self, payload: HealthSchemaEntity132Create) -> HealthModelEntity132:
        db_obj = HealthModelEntity132(
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

    def update_entity_132(self, entity_id: int, payload: HealthSchemaEntity132Update) -> Optional[HealthModelEntity132]:
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

    def get_entity_133_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity133]:
        return self.db.query(HealthModelEntity133).offset(skip).limit(limit).all()

    def get_entity_133_by_id(self, entity_id: int) -> Optional[HealthModelEntity133]:
        return self.db.query(HealthModelEntity133).filter(HealthModelEntity133.id == entity_id).first()

    def create_entity_133(self, payload: HealthSchemaEntity133Create) -> HealthModelEntity133:
        db_obj = HealthModelEntity133(
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

    def update_entity_133(self, entity_id: int, payload: HealthSchemaEntity133Update) -> Optional[HealthModelEntity133]:
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

    def get_entity_134_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity134]:
        return self.db.query(HealthModelEntity134).offset(skip).limit(limit).all()

    def get_entity_134_by_id(self, entity_id: int) -> Optional[HealthModelEntity134]:
        return self.db.query(HealthModelEntity134).filter(HealthModelEntity134.id == entity_id).first()

    def create_entity_134(self, payload: HealthSchemaEntity134Create) -> HealthModelEntity134:
        db_obj = HealthModelEntity134(
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

    def update_entity_134(self, entity_id: int, payload: HealthSchemaEntity134Update) -> Optional[HealthModelEntity134]:
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

    def get_entity_135_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity135]:
        return self.db.query(HealthModelEntity135).offset(skip).limit(limit).all()

    def get_entity_135_by_id(self, entity_id: int) -> Optional[HealthModelEntity135]:
        return self.db.query(HealthModelEntity135).filter(HealthModelEntity135.id == entity_id).first()

    def create_entity_135(self, payload: HealthSchemaEntity135Create) -> HealthModelEntity135:
        db_obj = HealthModelEntity135(
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

    def update_entity_135(self, entity_id: int, payload: HealthSchemaEntity135Update) -> Optional[HealthModelEntity135]:
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

    def get_entity_136_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity136]:
        return self.db.query(HealthModelEntity136).offset(skip).limit(limit).all()

    def get_entity_136_by_id(self, entity_id: int) -> Optional[HealthModelEntity136]:
        return self.db.query(HealthModelEntity136).filter(HealthModelEntity136.id == entity_id).first()

    def create_entity_136(self, payload: HealthSchemaEntity136Create) -> HealthModelEntity136:
        db_obj = HealthModelEntity136(
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

    def update_entity_136(self, entity_id: int, payload: HealthSchemaEntity136Update) -> Optional[HealthModelEntity136]:
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

    def get_entity_137_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity137]:
        return self.db.query(HealthModelEntity137).offset(skip).limit(limit).all()

    def get_entity_137_by_id(self, entity_id: int) -> Optional[HealthModelEntity137]:
        return self.db.query(HealthModelEntity137).filter(HealthModelEntity137.id == entity_id).first()

    def create_entity_137(self, payload: HealthSchemaEntity137Create) -> HealthModelEntity137:
        db_obj = HealthModelEntity137(
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

    def update_entity_137(self, entity_id: int, payload: HealthSchemaEntity137Update) -> Optional[HealthModelEntity137]:
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

    def get_entity_138_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity138]:
        return self.db.query(HealthModelEntity138).offset(skip).limit(limit).all()

    def get_entity_138_by_id(self, entity_id: int) -> Optional[HealthModelEntity138]:
        return self.db.query(HealthModelEntity138).filter(HealthModelEntity138.id == entity_id).first()

    def create_entity_138(self, payload: HealthSchemaEntity138Create) -> HealthModelEntity138:
        db_obj = HealthModelEntity138(
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

    def update_entity_138(self, entity_id: int, payload: HealthSchemaEntity138Update) -> Optional[HealthModelEntity138]:
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

    def get_entity_139_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity139]:
        return self.db.query(HealthModelEntity139).offset(skip).limit(limit).all()

    def get_entity_139_by_id(self, entity_id: int) -> Optional[HealthModelEntity139]:
        return self.db.query(HealthModelEntity139).filter(HealthModelEntity139.id == entity_id).first()

    def create_entity_139(self, payload: HealthSchemaEntity139Create) -> HealthModelEntity139:
        db_obj = HealthModelEntity139(
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

    def update_entity_139(self, entity_id: int, payload: HealthSchemaEntity139Update) -> Optional[HealthModelEntity139]:
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

    def get_entity_140_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity140]:
        return self.db.query(HealthModelEntity140).offset(skip).limit(limit).all()

    def get_entity_140_by_id(self, entity_id: int) -> Optional[HealthModelEntity140]:
        return self.db.query(HealthModelEntity140).filter(HealthModelEntity140.id == entity_id).first()

    def create_entity_140(self, payload: HealthSchemaEntity140Create) -> HealthModelEntity140:
        db_obj = HealthModelEntity140(
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

    def update_entity_140(self, entity_id: int, payload: HealthSchemaEntity140Update) -> Optional[HealthModelEntity140]:
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

    def get_entity_141_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity141]:
        return self.db.query(HealthModelEntity141).offset(skip).limit(limit).all()

    def get_entity_141_by_id(self, entity_id: int) -> Optional[HealthModelEntity141]:
        return self.db.query(HealthModelEntity141).filter(HealthModelEntity141.id == entity_id).first()

    def create_entity_141(self, payload: HealthSchemaEntity141Create) -> HealthModelEntity141:
        db_obj = HealthModelEntity141(
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

    def update_entity_141(self, entity_id: int, payload: HealthSchemaEntity141Update) -> Optional[HealthModelEntity141]:
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

    def get_entity_142_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity142]:
        return self.db.query(HealthModelEntity142).offset(skip).limit(limit).all()

    def get_entity_142_by_id(self, entity_id: int) -> Optional[HealthModelEntity142]:
        return self.db.query(HealthModelEntity142).filter(HealthModelEntity142.id == entity_id).first()

    def create_entity_142(self, payload: HealthSchemaEntity142Create) -> HealthModelEntity142:
        db_obj = HealthModelEntity142(
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

    def update_entity_142(self, entity_id: int, payload: HealthSchemaEntity142Update) -> Optional[HealthModelEntity142]:
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

    def get_entity_143_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity143]:
        return self.db.query(HealthModelEntity143).offset(skip).limit(limit).all()

    def get_entity_143_by_id(self, entity_id: int) -> Optional[HealthModelEntity143]:
        return self.db.query(HealthModelEntity143).filter(HealthModelEntity143.id == entity_id).first()

    def create_entity_143(self, payload: HealthSchemaEntity143Create) -> HealthModelEntity143:
        db_obj = HealthModelEntity143(
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

    def update_entity_143(self, entity_id: int, payload: HealthSchemaEntity143Update) -> Optional[HealthModelEntity143]:
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

    def get_entity_144_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity144]:
        return self.db.query(HealthModelEntity144).offset(skip).limit(limit).all()

    def get_entity_144_by_id(self, entity_id: int) -> Optional[HealthModelEntity144]:
        return self.db.query(HealthModelEntity144).filter(HealthModelEntity144.id == entity_id).first()

    def create_entity_144(self, payload: HealthSchemaEntity144Create) -> HealthModelEntity144:
        db_obj = HealthModelEntity144(
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

    def update_entity_144(self, entity_id: int, payload: HealthSchemaEntity144Update) -> Optional[HealthModelEntity144]:
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

    def get_entity_145_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity145]:
        return self.db.query(HealthModelEntity145).offset(skip).limit(limit).all()

    def get_entity_145_by_id(self, entity_id: int) -> Optional[HealthModelEntity145]:
        return self.db.query(HealthModelEntity145).filter(HealthModelEntity145.id == entity_id).first()

    def create_entity_145(self, payload: HealthSchemaEntity145Create) -> HealthModelEntity145:
        db_obj = HealthModelEntity145(
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

    def update_entity_145(self, entity_id: int, payload: HealthSchemaEntity145Update) -> Optional[HealthModelEntity145]:
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

    def get_entity_146_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity146]:
        return self.db.query(HealthModelEntity146).offset(skip).limit(limit).all()

    def get_entity_146_by_id(self, entity_id: int) -> Optional[HealthModelEntity146]:
        return self.db.query(HealthModelEntity146).filter(HealthModelEntity146.id == entity_id).first()

    def create_entity_146(self, payload: HealthSchemaEntity146Create) -> HealthModelEntity146:
        db_obj = HealthModelEntity146(
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

    def update_entity_146(self, entity_id: int, payload: HealthSchemaEntity146Update) -> Optional[HealthModelEntity146]:
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

    def get_entity_147_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity147]:
        return self.db.query(HealthModelEntity147).offset(skip).limit(limit).all()

    def get_entity_147_by_id(self, entity_id: int) -> Optional[HealthModelEntity147]:
        return self.db.query(HealthModelEntity147).filter(HealthModelEntity147.id == entity_id).first()

    def create_entity_147(self, payload: HealthSchemaEntity147Create) -> HealthModelEntity147:
        db_obj = HealthModelEntity147(
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

    def update_entity_147(self, entity_id: int, payload: HealthSchemaEntity147Update) -> Optional[HealthModelEntity147]:
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

    def get_entity_148_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity148]:
        return self.db.query(HealthModelEntity148).offset(skip).limit(limit).all()

    def get_entity_148_by_id(self, entity_id: int) -> Optional[HealthModelEntity148]:
        return self.db.query(HealthModelEntity148).filter(HealthModelEntity148.id == entity_id).first()

    def create_entity_148(self, payload: HealthSchemaEntity148Create) -> HealthModelEntity148:
        db_obj = HealthModelEntity148(
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

    def update_entity_148(self, entity_id: int, payload: HealthSchemaEntity148Update) -> Optional[HealthModelEntity148]:
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

    def get_entity_149_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity149]:
        return self.db.query(HealthModelEntity149).offset(skip).limit(limit).all()

    def get_entity_149_by_id(self, entity_id: int) -> Optional[HealthModelEntity149]:
        return self.db.query(HealthModelEntity149).filter(HealthModelEntity149.id == entity_id).first()

    def create_entity_149(self, payload: HealthSchemaEntity149Create) -> HealthModelEntity149:
        db_obj = HealthModelEntity149(
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

    def update_entity_149(self, entity_id: int, payload: HealthSchemaEntity149Update) -> Optional[HealthModelEntity149]:
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

    def get_entity_150_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity150]:
        return self.db.query(HealthModelEntity150).offset(skip).limit(limit).all()

    def get_entity_150_by_id(self, entity_id: int) -> Optional[HealthModelEntity150]:
        return self.db.query(HealthModelEntity150).filter(HealthModelEntity150.id == entity_id).first()

    def create_entity_150(self, payload: HealthSchemaEntity150Create) -> HealthModelEntity150:
        db_obj = HealthModelEntity150(
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

    def update_entity_150(self, entity_id: int, payload: HealthSchemaEntity150Update) -> Optional[HealthModelEntity150]:
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

    def get_entity_151_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity151]:
        return self.db.query(HealthModelEntity151).offset(skip).limit(limit).all()

    def get_entity_151_by_id(self, entity_id: int) -> Optional[HealthModelEntity151]:
        return self.db.query(HealthModelEntity151).filter(HealthModelEntity151.id == entity_id).first()

    def create_entity_151(self, payload: HealthSchemaEntity151Create) -> HealthModelEntity151:
        db_obj = HealthModelEntity151(
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

    def update_entity_151(self, entity_id: int, payload: HealthSchemaEntity151Update) -> Optional[HealthModelEntity151]:
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

    def get_entity_152_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity152]:
        return self.db.query(HealthModelEntity152).offset(skip).limit(limit).all()

    def get_entity_152_by_id(self, entity_id: int) -> Optional[HealthModelEntity152]:
        return self.db.query(HealthModelEntity152).filter(HealthModelEntity152.id == entity_id).first()

    def create_entity_152(self, payload: HealthSchemaEntity152Create) -> HealthModelEntity152:
        db_obj = HealthModelEntity152(
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

    def update_entity_152(self, entity_id: int, payload: HealthSchemaEntity152Update) -> Optional[HealthModelEntity152]:
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

    def get_entity_153_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity153]:
        return self.db.query(HealthModelEntity153).offset(skip).limit(limit).all()

    def get_entity_153_by_id(self, entity_id: int) -> Optional[HealthModelEntity153]:
        return self.db.query(HealthModelEntity153).filter(HealthModelEntity153.id == entity_id).first()

    def create_entity_153(self, payload: HealthSchemaEntity153Create) -> HealthModelEntity153:
        db_obj = HealthModelEntity153(
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

    def update_entity_153(self, entity_id: int, payload: HealthSchemaEntity153Update) -> Optional[HealthModelEntity153]:
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

    def get_entity_154_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity154]:
        return self.db.query(HealthModelEntity154).offset(skip).limit(limit).all()

    def get_entity_154_by_id(self, entity_id: int) -> Optional[HealthModelEntity154]:
        return self.db.query(HealthModelEntity154).filter(HealthModelEntity154.id == entity_id).first()

    def create_entity_154(self, payload: HealthSchemaEntity154Create) -> HealthModelEntity154:
        db_obj = HealthModelEntity154(
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

    def update_entity_154(self, entity_id: int, payload: HealthSchemaEntity154Update) -> Optional[HealthModelEntity154]:
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

    def get_entity_155_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity155]:
        return self.db.query(HealthModelEntity155).offset(skip).limit(limit).all()

    def get_entity_155_by_id(self, entity_id: int) -> Optional[HealthModelEntity155]:
        return self.db.query(HealthModelEntity155).filter(HealthModelEntity155.id == entity_id).first()

    def create_entity_155(self, payload: HealthSchemaEntity155Create) -> HealthModelEntity155:
        db_obj = HealthModelEntity155(
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

    def update_entity_155(self, entity_id: int, payload: HealthSchemaEntity155Update) -> Optional[HealthModelEntity155]:
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

    def get_entity_156_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity156]:
        return self.db.query(HealthModelEntity156).offset(skip).limit(limit).all()

    def get_entity_156_by_id(self, entity_id: int) -> Optional[HealthModelEntity156]:
        return self.db.query(HealthModelEntity156).filter(HealthModelEntity156.id == entity_id).first()

    def create_entity_156(self, payload: HealthSchemaEntity156Create) -> HealthModelEntity156:
        db_obj = HealthModelEntity156(
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

    def update_entity_156(self, entity_id: int, payload: HealthSchemaEntity156Update) -> Optional[HealthModelEntity156]:
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

    def get_entity_157_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity157]:
        return self.db.query(HealthModelEntity157).offset(skip).limit(limit).all()

    def get_entity_157_by_id(self, entity_id: int) -> Optional[HealthModelEntity157]:
        return self.db.query(HealthModelEntity157).filter(HealthModelEntity157.id == entity_id).first()

    def create_entity_157(self, payload: HealthSchemaEntity157Create) -> HealthModelEntity157:
        db_obj = HealthModelEntity157(
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

    def update_entity_157(self, entity_id: int, payload: HealthSchemaEntity157Update) -> Optional[HealthModelEntity157]:
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

    def get_entity_158_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity158]:
        return self.db.query(HealthModelEntity158).offset(skip).limit(limit).all()

    def get_entity_158_by_id(self, entity_id: int) -> Optional[HealthModelEntity158]:
        return self.db.query(HealthModelEntity158).filter(HealthModelEntity158.id == entity_id).first()

    def create_entity_158(self, payload: HealthSchemaEntity158Create) -> HealthModelEntity158:
        db_obj = HealthModelEntity158(
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

    def update_entity_158(self, entity_id: int, payload: HealthSchemaEntity158Update) -> Optional[HealthModelEntity158]:
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

    def get_entity_159_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity159]:
        return self.db.query(HealthModelEntity159).offset(skip).limit(limit).all()

    def get_entity_159_by_id(self, entity_id: int) -> Optional[HealthModelEntity159]:
        return self.db.query(HealthModelEntity159).filter(HealthModelEntity159.id == entity_id).first()

    def create_entity_159(self, payload: HealthSchemaEntity159Create) -> HealthModelEntity159:
        db_obj = HealthModelEntity159(
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

    def update_entity_159(self, entity_id: int, payload: HealthSchemaEntity159Update) -> Optional[HealthModelEntity159]:
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

    def get_entity_160_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity160]:
        return self.db.query(HealthModelEntity160).offset(skip).limit(limit).all()

    def get_entity_160_by_id(self, entity_id: int) -> Optional[HealthModelEntity160]:
        return self.db.query(HealthModelEntity160).filter(HealthModelEntity160.id == entity_id).first()

    def create_entity_160(self, payload: HealthSchemaEntity160Create) -> HealthModelEntity160:
        db_obj = HealthModelEntity160(
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

    def update_entity_160(self, entity_id: int, payload: HealthSchemaEntity160Update) -> Optional[HealthModelEntity160]:
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

    def get_entity_161_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity161]:
        return self.db.query(HealthModelEntity161).offset(skip).limit(limit).all()

    def get_entity_161_by_id(self, entity_id: int) -> Optional[HealthModelEntity161]:
        return self.db.query(HealthModelEntity161).filter(HealthModelEntity161.id == entity_id).first()

    def create_entity_161(self, payload: HealthSchemaEntity161Create) -> HealthModelEntity161:
        db_obj = HealthModelEntity161(
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

    def update_entity_161(self, entity_id: int, payload: HealthSchemaEntity161Update) -> Optional[HealthModelEntity161]:
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

    def get_entity_162_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity162]:
        return self.db.query(HealthModelEntity162).offset(skip).limit(limit).all()

    def get_entity_162_by_id(self, entity_id: int) -> Optional[HealthModelEntity162]:
        return self.db.query(HealthModelEntity162).filter(HealthModelEntity162.id == entity_id).first()

    def create_entity_162(self, payload: HealthSchemaEntity162Create) -> HealthModelEntity162:
        db_obj = HealthModelEntity162(
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

    def update_entity_162(self, entity_id: int, payload: HealthSchemaEntity162Update) -> Optional[HealthModelEntity162]:
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

    def get_entity_163_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity163]:
        return self.db.query(HealthModelEntity163).offset(skip).limit(limit).all()

    def get_entity_163_by_id(self, entity_id: int) -> Optional[HealthModelEntity163]:
        return self.db.query(HealthModelEntity163).filter(HealthModelEntity163.id == entity_id).first()

    def create_entity_163(self, payload: HealthSchemaEntity163Create) -> HealthModelEntity163:
        db_obj = HealthModelEntity163(
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

    def update_entity_163(self, entity_id: int, payload: HealthSchemaEntity163Update) -> Optional[HealthModelEntity163]:
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

    def get_entity_164_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity164]:
        return self.db.query(HealthModelEntity164).offset(skip).limit(limit).all()

    def get_entity_164_by_id(self, entity_id: int) -> Optional[HealthModelEntity164]:
        return self.db.query(HealthModelEntity164).filter(HealthModelEntity164.id == entity_id).first()

    def create_entity_164(self, payload: HealthSchemaEntity164Create) -> HealthModelEntity164:
        db_obj = HealthModelEntity164(
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

    def update_entity_164(self, entity_id: int, payload: HealthSchemaEntity164Update) -> Optional[HealthModelEntity164]:
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

    def get_entity_165_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity165]:
        return self.db.query(HealthModelEntity165).offset(skip).limit(limit).all()

    def get_entity_165_by_id(self, entity_id: int) -> Optional[HealthModelEntity165]:
        return self.db.query(HealthModelEntity165).filter(HealthModelEntity165.id == entity_id).first()

    def create_entity_165(self, payload: HealthSchemaEntity165Create) -> HealthModelEntity165:
        db_obj = HealthModelEntity165(
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

    def update_entity_165(self, entity_id: int, payload: HealthSchemaEntity165Update) -> Optional[HealthModelEntity165]:
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

    def get_entity_166_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity166]:
        return self.db.query(HealthModelEntity166).offset(skip).limit(limit).all()

    def get_entity_166_by_id(self, entity_id: int) -> Optional[HealthModelEntity166]:
        return self.db.query(HealthModelEntity166).filter(HealthModelEntity166.id == entity_id).first()

    def create_entity_166(self, payload: HealthSchemaEntity166Create) -> HealthModelEntity166:
        db_obj = HealthModelEntity166(
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

    def update_entity_166(self, entity_id: int, payload: HealthSchemaEntity166Update) -> Optional[HealthModelEntity166]:
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

    def get_entity_167_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity167]:
        return self.db.query(HealthModelEntity167).offset(skip).limit(limit).all()

    def get_entity_167_by_id(self, entity_id: int) -> Optional[HealthModelEntity167]:
        return self.db.query(HealthModelEntity167).filter(HealthModelEntity167.id == entity_id).first()

    def create_entity_167(self, payload: HealthSchemaEntity167Create) -> HealthModelEntity167:
        db_obj = HealthModelEntity167(
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

    def update_entity_167(self, entity_id: int, payload: HealthSchemaEntity167Update) -> Optional[HealthModelEntity167]:
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

    def get_entity_168_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity168]:
        return self.db.query(HealthModelEntity168).offset(skip).limit(limit).all()

    def get_entity_168_by_id(self, entity_id: int) -> Optional[HealthModelEntity168]:
        return self.db.query(HealthModelEntity168).filter(HealthModelEntity168.id == entity_id).first()

    def create_entity_168(self, payload: HealthSchemaEntity168Create) -> HealthModelEntity168:
        db_obj = HealthModelEntity168(
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

    def update_entity_168(self, entity_id: int, payload: HealthSchemaEntity168Update) -> Optional[HealthModelEntity168]:
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

    def get_entity_169_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity169]:
        return self.db.query(HealthModelEntity169).offset(skip).limit(limit).all()

    def get_entity_169_by_id(self, entity_id: int) -> Optional[HealthModelEntity169]:
        return self.db.query(HealthModelEntity169).filter(HealthModelEntity169.id == entity_id).first()

    def create_entity_169(self, payload: HealthSchemaEntity169Create) -> HealthModelEntity169:
        db_obj = HealthModelEntity169(
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

    def update_entity_169(self, entity_id: int, payload: HealthSchemaEntity169Update) -> Optional[HealthModelEntity169]:
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

    def get_entity_170_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity170]:
        return self.db.query(HealthModelEntity170).offset(skip).limit(limit).all()

    def get_entity_170_by_id(self, entity_id: int) -> Optional[HealthModelEntity170]:
        return self.db.query(HealthModelEntity170).filter(HealthModelEntity170.id == entity_id).first()

    def create_entity_170(self, payload: HealthSchemaEntity170Create) -> HealthModelEntity170:
        db_obj = HealthModelEntity170(
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

    def update_entity_170(self, entity_id: int, payload: HealthSchemaEntity170Update) -> Optional[HealthModelEntity170]:
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

    def get_entity_171_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity171]:
        return self.db.query(HealthModelEntity171).offset(skip).limit(limit).all()

    def get_entity_171_by_id(self, entity_id: int) -> Optional[HealthModelEntity171]:
        return self.db.query(HealthModelEntity171).filter(HealthModelEntity171.id == entity_id).first()

    def create_entity_171(self, payload: HealthSchemaEntity171Create) -> HealthModelEntity171:
        db_obj = HealthModelEntity171(
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

    def update_entity_171(self, entity_id: int, payload: HealthSchemaEntity171Update) -> Optional[HealthModelEntity171]:
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

    def get_entity_172_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity172]:
        return self.db.query(HealthModelEntity172).offset(skip).limit(limit).all()

    def get_entity_172_by_id(self, entity_id: int) -> Optional[HealthModelEntity172]:
        return self.db.query(HealthModelEntity172).filter(HealthModelEntity172.id == entity_id).first()

    def create_entity_172(self, payload: HealthSchemaEntity172Create) -> HealthModelEntity172:
        db_obj = HealthModelEntity172(
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

    def update_entity_172(self, entity_id: int, payload: HealthSchemaEntity172Update) -> Optional[HealthModelEntity172]:
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

    def get_entity_173_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity173]:
        return self.db.query(HealthModelEntity173).offset(skip).limit(limit).all()

    def get_entity_173_by_id(self, entity_id: int) -> Optional[HealthModelEntity173]:
        return self.db.query(HealthModelEntity173).filter(HealthModelEntity173.id == entity_id).first()

    def create_entity_173(self, payload: HealthSchemaEntity173Create) -> HealthModelEntity173:
        db_obj = HealthModelEntity173(
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

    def update_entity_173(self, entity_id: int, payload: HealthSchemaEntity173Update) -> Optional[HealthModelEntity173]:
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

    def get_entity_174_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity174]:
        return self.db.query(HealthModelEntity174).offset(skip).limit(limit).all()

    def get_entity_174_by_id(self, entity_id: int) -> Optional[HealthModelEntity174]:
        return self.db.query(HealthModelEntity174).filter(HealthModelEntity174.id == entity_id).first()

    def create_entity_174(self, payload: HealthSchemaEntity174Create) -> HealthModelEntity174:
        db_obj = HealthModelEntity174(
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

    def update_entity_174(self, entity_id: int, payload: HealthSchemaEntity174Update) -> Optional[HealthModelEntity174]:
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

    def get_entity_175_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity175]:
        return self.db.query(HealthModelEntity175).offset(skip).limit(limit).all()

    def get_entity_175_by_id(self, entity_id: int) -> Optional[HealthModelEntity175]:
        return self.db.query(HealthModelEntity175).filter(HealthModelEntity175.id == entity_id).first()

    def create_entity_175(self, payload: HealthSchemaEntity175Create) -> HealthModelEntity175:
        db_obj = HealthModelEntity175(
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

    def update_entity_175(self, entity_id: int, payload: HealthSchemaEntity175Update) -> Optional[HealthModelEntity175]:
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

    def get_entity_176_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity176]:
        return self.db.query(HealthModelEntity176).offset(skip).limit(limit).all()

    def get_entity_176_by_id(self, entity_id: int) -> Optional[HealthModelEntity176]:
        return self.db.query(HealthModelEntity176).filter(HealthModelEntity176.id == entity_id).first()

    def create_entity_176(self, payload: HealthSchemaEntity176Create) -> HealthModelEntity176:
        db_obj = HealthModelEntity176(
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

    def update_entity_176(self, entity_id: int, payload: HealthSchemaEntity176Update) -> Optional[HealthModelEntity176]:
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

    def get_entity_177_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity177]:
        return self.db.query(HealthModelEntity177).offset(skip).limit(limit).all()

    def get_entity_177_by_id(self, entity_id: int) -> Optional[HealthModelEntity177]:
        return self.db.query(HealthModelEntity177).filter(HealthModelEntity177.id == entity_id).first()

    def create_entity_177(self, payload: HealthSchemaEntity177Create) -> HealthModelEntity177:
        db_obj = HealthModelEntity177(
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

    def update_entity_177(self, entity_id: int, payload: HealthSchemaEntity177Update) -> Optional[HealthModelEntity177]:
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

    def get_entity_178_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity178]:
        return self.db.query(HealthModelEntity178).offset(skip).limit(limit).all()

    def get_entity_178_by_id(self, entity_id: int) -> Optional[HealthModelEntity178]:
        return self.db.query(HealthModelEntity178).filter(HealthModelEntity178.id == entity_id).first()

    def create_entity_178(self, payload: HealthSchemaEntity178Create) -> HealthModelEntity178:
        db_obj = HealthModelEntity178(
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

    def update_entity_178(self, entity_id: int, payload: HealthSchemaEntity178Update) -> Optional[HealthModelEntity178]:
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

    def get_entity_179_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity179]:
        return self.db.query(HealthModelEntity179).offset(skip).limit(limit).all()

    def get_entity_179_by_id(self, entity_id: int) -> Optional[HealthModelEntity179]:
        return self.db.query(HealthModelEntity179).filter(HealthModelEntity179.id == entity_id).first()

    def create_entity_179(self, payload: HealthSchemaEntity179Create) -> HealthModelEntity179:
        db_obj = HealthModelEntity179(
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

    def update_entity_179(self, entity_id: int, payload: HealthSchemaEntity179Update) -> Optional[HealthModelEntity179]:
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

    def get_entity_180_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity180]:
        return self.db.query(HealthModelEntity180).offset(skip).limit(limit).all()

    def get_entity_180_by_id(self, entity_id: int) -> Optional[HealthModelEntity180]:
        return self.db.query(HealthModelEntity180).filter(HealthModelEntity180.id == entity_id).first()

    def create_entity_180(self, payload: HealthSchemaEntity180Create) -> HealthModelEntity180:
        db_obj = HealthModelEntity180(
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

    def update_entity_180(self, entity_id: int, payload: HealthSchemaEntity180Update) -> Optional[HealthModelEntity180]:
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

    def get_entity_181_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity181]:
        return self.db.query(HealthModelEntity181).offset(skip).limit(limit).all()

    def get_entity_181_by_id(self, entity_id: int) -> Optional[HealthModelEntity181]:
        return self.db.query(HealthModelEntity181).filter(HealthModelEntity181.id == entity_id).first()

    def create_entity_181(self, payload: HealthSchemaEntity181Create) -> HealthModelEntity181:
        db_obj = HealthModelEntity181(
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

    def update_entity_181(self, entity_id: int, payload: HealthSchemaEntity181Update) -> Optional[HealthModelEntity181]:
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

    def get_entity_182_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity182]:
        return self.db.query(HealthModelEntity182).offset(skip).limit(limit).all()

    def get_entity_182_by_id(self, entity_id: int) -> Optional[HealthModelEntity182]:
        return self.db.query(HealthModelEntity182).filter(HealthModelEntity182.id == entity_id).first()

    def create_entity_182(self, payload: HealthSchemaEntity182Create) -> HealthModelEntity182:
        db_obj = HealthModelEntity182(
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

    def update_entity_182(self, entity_id: int, payload: HealthSchemaEntity182Update) -> Optional[HealthModelEntity182]:
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

    def get_entity_183_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity183]:
        return self.db.query(HealthModelEntity183).offset(skip).limit(limit).all()

    def get_entity_183_by_id(self, entity_id: int) -> Optional[HealthModelEntity183]:
        return self.db.query(HealthModelEntity183).filter(HealthModelEntity183.id == entity_id).first()

    def create_entity_183(self, payload: HealthSchemaEntity183Create) -> HealthModelEntity183:
        db_obj = HealthModelEntity183(
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

    def update_entity_183(self, entity_id: int, payload: HealthSchemaEntity183Update) -> Optional[HealthModelEntity183]:
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

    def get_entity_184_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity184]:
        return self.db.query(HealthModelEntity184).offset(skip).limit(limit).all()

    def get_entity_184_by_id(self, entity_id: int) -> Optional[HealthModelEntity184]:
        return self.db.query(HealthModelEntity184).filter(HealthModelEntity184.id == entity_id).first()

    def create_entity_184(self, payload: HealthSchemaEntity184Create) -> HealthModelEntity184:
        db_obj = HealthModelEntity184(
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

    def update_entity_184(self, entity_id: int, payload: HealthSchemaEntity184Update) -> Optional[HealthModelEntity184]:
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

    def get_entity_185_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity185]:
        return self.db.query(HealthModelEntity185).offset(skip).limit(limit).all()

    def get_entity_185_by_id(self, entity_id: int) -> Optional[HealthModelEntity185]:
        return self.db.query(HealthModelEntity185).filter(HealthModelEntity185.id == entity_id).first()

    def create_entity_185(self, payload: HealthSchemaEntity185Create) -> HealthModelEntity185:
        db_obj = HealthModelEntity185(
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

    def update_entity_185(self, entity_id: int, payload: HealthSchemaEntity185Update) -> Optional[HealthModelEntity185]:
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

    def get_entity_186_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity186]:
        return self.db.query(HealthModelEntity186).offset(skip).limit(limit).all()

    def get_entity_186_by_id(self, entity_id: int) -> Optional[HealthModelEntity186]:
        return self.db.query(HealthModelEntity186).filter(HealthModelEntity186.id == entity_id).first()

    def create_entity_186(self, payload: HealthSchemaEntity186Create) -> HealthModelEntity186:
        db_obj = HealthModelEntity186(
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

    def update_entity_186(self, entity_id: int, payload: HealthSchemaEntity186Update) -> Optional[HealthModelEntity186]:
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

    def get_entity_187_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity187]:
        return self.db.query(HealthModelEntity187).offset(skip).limit(limit).all()

    def get_entity_187_by_id(self, entity_id: int) -> Optional[HealthModelEntity187]:
        return self.db.query(HealthModelEntity187).filter(HealthModelEntity187.id == entity_id).first()

    def create_entity_187(self, payload: HealthSchemaEntity187Create) -> HealthModelEntity187:
        db_obj = HealthModelEntity187(
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

    def update_entity_187(self, entity_id: int, payload: HealthSchemaEntity187Update) -> Optional[HealthModelEntity187]:
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

    def get_entity_188_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity188]:
        return self.db.query(HealthModelEntity188).offset(skip).limit(limit).all()

    def get_entity_188_by_id(self, entity_id: int) -> Optional[HealthModelEntity188]:
        return self.db.query(HealthModelEntity188).filter(HealthModelEntity188.id == entity_id).first()

    def create_entity_188(self, payload: HealthSchemaEntity188Create) -> HealthModelEntity188:
        db_obj = HealthModelEntity188(
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

    def update_entity_188(self, entity_id: int, payload: HealthSchemaEntity188Update) -> Optional[HealthModelEntity188]:
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

    def get_entity_189_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity189]:
        return self.db.query(HealthModelEntity189).offset(skip).limit(limit).all()

    def get_entity_189_by_id(self, entity_id: int) -> Optional[HealthModelEntity189]:
        return self.db.query(HealthModelEntity189).filter(HealthModelEntity189.id == entity_id).first()

    def create_entity_189(self, payload: HealthSchemaEntity189Create) -> HealthModelEntity189:
        db_obj = HealthModelEntity189(
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

    def update_entity_189(self, entity_id: int, payload: HealthSchemaEntity189Update) -> Optional[HealthModelEntity189]:
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

    def get_entity_190_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity190]:
        return self.db.query(HealthModelEntity190).offset(skip).limit(limit).all()

    def get_entity_190_by_id(self, entity_id: int) -> Optional[HealthModelEntity190]:
        return self.db.query(HealthModelEntity190).filter(HealthModelEntity190.id == entity_id).first()

    def create_entity_190(self, payload: HealthSchemaEntity190Create) -> HealthModelEntity190:
        db_obj = HealthModelEntity190(
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

    def update_entity_190(self, entity_id: int, payload: HealthSchemaEntity190Update) -> Optional[HealthModelEntity190]:
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

    def get_entity_191_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity191]:
        return self.db.query(HealthModelEntity191).offset(skip).limit(limit).all()

    def get_entity_191_by_id(self, entity_id: int) -> Optional[HealthModelEntity191]:
        return self.db.query(HealthModelEntity191).filter(HealthModelEntity191.id == entity_id).first()

    def create_entity_191(self, payload: HealthSchemaEntity191Create) -> HealthModelEntity191:
        db_obj = HealthModelEntity191(
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

    def update_entity_191(self, entity_id: int, payload: HealthSchemaEntity191Update) -> Optional[HealthModelEntity191]:
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

    def get_entity_192_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity192]:
        return self.db.query(HealthModelEntity192).offset(skip).limit(limit).all()

    def get_entity_192_by_id(self, entity_id: int) -> Optional[HealthModelEntity192]:
        return self.db.query(HealthModelEntity192).filter(HealthModelEntity192.id == entity_id).first()

    def create_entity_192(self, payload: HealthSchemaEntity192Create) -> HealthModelEntity192:
        db_obj = HealthModelEntity192(
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

    def update_entity_192(self, entity_id: int, payload: HealthSchemaEntity192Update) -> Optional[HealthModelEntity192]:
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

    def get_entity_193_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity193]:
        return self.db.query(HealthModelEntity193).offset(skip).limit(limit).all()

    def get_entity_193_by_id(self, entity_id: int) -> Optional[HealthModelEntity193]:
        return self.db.query(HealthModelEntity193).filter(HealthModelEntity193.id == entity_id).first()

    def create_entity_193(self, payload: HealthSchemaEntity193Create) -> HealthModelEntity193:
        db_obj = HealthModelEntity193(
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

    def update_entity_193(self, entity_id: int, payload: HealthSchemaEntity193Update) -> Optional[HealthModelEntity193]:
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

    def get_entity_194_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity194]:
        return self.db.query(HealthModelEntity194).offset(skip).limit(limit).all()

    def get_entity_194_by_id(self, entity_id: int) -> Optional[HealthModelEntity194]:
        return self.db.query(HealthModelEntity194).filter(HealthModelEntity194.id == entity_id).first()

    def create_entity_194(self, payload: HealthSchemaEntity194Create) -> HealthModelEntity194:
        db_obj = HealthModelEntity194(
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

    def update_entity_194(self, entity_id: int, payload: HealthSchemaEntity194Update) -> Optional[HealthModelEntity194]:
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

    def get_entity_195_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity195]:
        return self.db.query(HealthModelEntity195).offset(skip).limit(limit).all()

    def get_entity_195_by_id(self, entity_id: int) -> Optional[HealthModelEntity195]:
        return self.db.query(HealthModelEntity195).filter(HealthModelEntity195.id == entity_id).first()

    def create_entity_195(self, payload: HealthSchemaEntity195Create) -> HealthModelEntity195:
        db_obj = HealthModelEntity195(
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

    def update_entity_195(self, entity_id: int, payload: HealthSchemaEntity195Update) -> Optional[HealthModelEntity195]:
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

    def get_entity_196_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity196]:
        return self.db.query(HealthModelEntity196).offset(skip).limit(limit).all()

    def get_entity_196_by_id(self, entity_id: int) -> Optional[HealthModelEntity196]:
        return self.db.query(HealthModelEntity196).filter(HealthModelEntity196.id == entity_id).first()

    def create_entity_196(self, payload: HealthSchemaEntity196Create) -> HealthModelEntity196:
        db_obj = HealthModelEntity196(
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

    def update_entity_196(self, entity_id: int, payload: HealthSchemaEntity196Update) -> Optional[HealthModelEntity196]:
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

    def get_entity_197_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity197]:
        return self.db.query(HealthModelEntity197).offset(skip).limit(limit).all()

    def get_entity_197_by_id(self, entity_id: int) -> Optional[HealthModelEntity197]:
        return self.db.query(HealthModelEntity197).filter(HealthModelEntity197.id == entity_id).first()

    def create_entity_197(self, payload: HealthSchemaEntity197Create) -> HealthModelEntity197:
        db_obj = HealthModelEntity197(
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

    def update_entity_197(self, entity_id: int, payload: HealthSchemaEntity197Update) -> Optional[HealthModelEntity197]:
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

    def get_entity_198_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity198]:
        return self.db.query(HealthModelEntity198).offset(skip).limit(limit).all()

    def get_entity_198_by_id(self, entity_id: int) -> Optional[HealthModelEntity198]:
        return self.db.query(HealthModelEntity198).filter(HealthModelEntity198.id == entity_id).first()

    def create_entity_198(self, payload: HealthSchemaEntity198Create) -> HealthModelEntity198:
        db_obj = HealthModelEntity198(
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

    def update_entity_198(self, entity_id: int, payload: HealthSchemaEntity198Update) -> Optional[HealthModelEntity198]:
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

    def get_entity_199_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity199]:
        return self.db.query(HealthModelEntity199).offset(skip).limit(limit).all()

    def get_entity_199_by_id(self, entity_id: int) -> Optional[HealthModelEntity199]:
        return self.db.query(HealthModelEntity199).filter(HealthModelEntity199.id == entity_id).first()

    def create_entity_199(self, payload: HealthSchemaEntity199Create) -> HealthModelEntity199:
        db_obj = HealthModelEntity199(
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

    def update_entity_199(self, entity_id: int, payload: HealthSchemaEntity199Update) -> Optional[HealthModelEntity199]:
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

    def get_entity_200_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity200]:
        return self.db.query(HealthModelEntity200).offset(skip).limit(limit).all()

    def get_entity_200_by_id(self, entity_id: int) -> Optional[HealthModelEntity200]:
        return self.db.query(HealthModelEntity200).filter(HealthModelEntity200.id == entity_id).first()

    def create_entity_200(self, payload: HealthSchemaEntity200Create) -> HealthModelEntity200:
        db_obj = HealthModelEntity200(
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

    def update_entity_200(self, entity_id: int, payload: HealthSchemaEntity200Update) -> Optional[HealthModelEntity200]:
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

    def get_entity_201_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity201]:
        return self.db.query(HealthModelEntity201).offset(skip).limit(limit).all()

    def get_entity_201_by_id(self, entity_id: int) -> Optional[HealthModelEntity201]:
        return self.db.query(HealthModelEntity201).filter(HealthModelEntity201.id == entity_id).first()

    def create_entity_201(self, payload: HealthSchemaEntity201Create) -> HealthModelEntity201:
        db_obj = HealthModelEntity201(
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

    def update_entity_201(self, entity_id: int, payload: HealthSchemaEntity201Update) -> Optional[HealthModelEntity201]:
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

    def get_entity_202_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity202]:
        return self.db.query(HealthModelEntity202).offset(skip).limit(limit).all()

    def get_entity_202_by_id(self, entity_id: int) -> Optional[HealthModelEntity202]:
        return self.db.query(HealthModelEntity202).filter(HealthModelEntity202.id == entity_id).first()

    def create_entity_202(self, payload: HealthSchemaEntity202Create) -> HealthModelEntity202:
        db_obj = HealthModelEntity202(
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

    def update_entity_202(self, entity_id: int, payload: HealthSchemaEntity202Update) -> Optional[HealthModelEntity202]:
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

    def get_entity_203_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity203]:
        return self.db.query(HealthModelEntity203).offset(skip).limit(limit).all()

    def get_entity_203_by_id(self, entity_id: int) -> Optional[HealthModelEntity203]:
        return self.db.query(HealthModelEntity203).filter(HealthModelEntity203.id == entity_id).first()

    def create_entity_203(self, payload: HealthSchemaEntity203Create) -> HealthModelEntity203:
        db_obj = HealthModelEntity203(
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

    def update_entity_203(self, entity_id: int, payload: HealthSchemaEntity203Update) -> Optional[HealthModelEntity203]:
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

    def get_entity_204_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity204]:
        return self.db.query(HealthModelEntity204).offset(skip).limit(limit).all()

    def get_entity_204_by_id(self, entity_id: int) -> Optional[HealthModelEntity204]:
        return self.db.query(HealthModelEntity204).filter(HealthModelEntity204.id == entity_id).first()

    def create_entity_204(self, payload: HealthSchemaEntity204Create) -> HealthModelEntity204:
        db_obj = HealthModelEntity204(
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

    def update_entity_204(self, entity_id: int, payload: HealthSchemaEntity204Update) -> Optional[HealthModelEntity204]:
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

    def get_entity_205_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity205]:
        return self.db.query(HealthModelEntity205).offset(skip).limit(limit).all()

    def get_entity_205_by_id(self, entity_id: int) -> Optional[HealthModelEntity205]:
        return self.db.query(HealthModelEntity205).filter(HealthModelEntity205.id == entity_id).first()

    def create_entity_205(self, payload: HealthSchemaEntity205Create) -> HealthModelEntity205:
        db_obj = HealthModelEntity205(
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

    def update_entity_205(self, entity_id: int, payload: HealthSchemaEntity205Update) -> Optional[HealthModelEntity205]:
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

    def get_entity_206_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity206]:
        return self.db.query(HealthModelEntity206).offset(skip).limit(limit).all()

    def get_entity_206_by_id(self, entity_id: int) -> Optional[HealthModelEntity206]:
        return self.db.query(HealthModelEntity206).filter(HealthModelEntity206.id == entity_id).first()

    def create_entity_206(self, payload: HealthSchemaEntity206Create) -> HealthModelEntity206:
        db_obj = HealthModelEntity206(
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

    def update_entity_206(self, entity_id: int, payload: HealthSchemaEntity206Update) -> Optional[HealthModelEntity206]:
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

    def get_entity_207_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity207]:
        return self.db.query(HealthModelEntity207).offset(skip).limit(limit).all()

    def get_entity_207_by_id(self, entity_id: int) -> Optional[HealthModelEntity207]:
        return self.db.query(HealthModelEntity207).filter(HealthModelEntity207.id == entity_id).first()

    def create_entity_207(self, payload: HealthSchemaEntity207Create) -> HealthModelEntity207:
        db_obj = HealthModelEntity207(
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

    def update_entity_207(self, entity_id: int, payload: HealthSchemaEntity207Update) -> Optional[HealthModelEntity207]:
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

    def get_entity_208_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity208]:
        return self.db.query(HealthModelEntity208).offset(skip).limit(limit).all()

    def get_entity_208_by_id(self, entity_id: int) -> Optional[HealthModelEntity208]:
        return self.db.query(HealthModelEntity208).filter(HealthModelEntity208.id == entity_id).first()

    def create_entity_208(self, payload: HealthSchemaEntity208Create) -> HealthModelEntity208:
        db_obj = HealthModelEntity208(
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

    def update_entity_208(self, entity_id: int, payload: HealthSchemaEntity208Update) -> Optional[HealthModelEntity208]:
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

    def get_entity_209_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity209]:
        return self.db.query(HealthModelEntity209).offset(skip).limit(limit).all()

    def get_entity_209_by_id(self, entity_id: int) -> Optional[HealthModelEntity209]:
        return self.db.query(HealthModelEntity209).filter(HealthModelEntity209.id == entity_id).first()

    def create_entity_209(self, payload: HealthSchemaEntity209Create) -> HealthModelEntity209:
        db_obj = HealthModelEntity209(
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

    def update_entity_209(self, entity_id: int, payload: HealthSchemaEntity209Update) -> Optional[HealthModelEntity209]:
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

    def get_entity_210_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity210]:
        return self.db.query(HealthModelEntity210).offset(skip).limit(limit).all()

    def get_entity_210_by_id(self, entity_id: int) -> Optional[HealthModelEntity210]:
        return self.db.query(HealthModelEntity210).filter(HealthModelEntity210.id == entity_id).first()

    def create_entity_210(self, payload: HealthSchemaEntity210Create) -> HealthModelEntity210:
        db_obj = HealthModelEntity210(
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

    def update_entity_210(self, entity_id: int, payload: HealthSchemaEntity210Update) -> Optional[HealthModelEntity210]:
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

    def get_entity_211_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity211]:
        return self.db.query(HealthModelEntity211).offset(skip).limit(limit).all()

    def get_entity_211_by_id(self, entity_id: int) -> Optional[HealthModelEntity211]:
        return self.db.query(HealthModelEntity211).filter(HealthModelEntity211.id == entity_id).first()

    def create_entity_211(self, payload: HealthSchemaEntity211Create) -> HealthModelEntity211:
        db_obj = HealthModelEntity211(
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

    def update_entity_211(self, entity_id: int, payload: HealthSchemaEntity211Update) -> Optional[HealthModelEntity211]:
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

    def get_entity_212_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity212]:
        return self.db.query(HealthModelEntity212).offset(skip).limit(limit).all()

    def get_entity_212_by_id(self, entity_id: int) -> Optional[HealthModelEntity212]:
        return self.db.query(HealthModelEntity212).filter(HealthModelEntity212.id == entity_id).first()

    def create_entity_212(self, payload: HealthSchemaEntity212Create) -> HealthModelEntity212:
        db_obj = HealthModelEntity212(
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

    def update_entity_212(self, entity_id: int, payload: HealthSchemaEntity212Update) -> Optional[HealthModelEntity212]:
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

    def get_entity_213_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity213]:
        return self.db.query(HealthModelEntity213).offset(skip).limit(limit).all()

    def get_entity_213_by_id(self, entity_id: int) -> Optional[HealthModelEntity213]:
        return self.db.query(HealthModelEntity213).filter(HealthModelEntity213.id == entity_id).first()

    def create_entity_213(self, payload: HealthSchemaEntity213Create) -> HealthModelEntity213:
        db_obj = HealthModelEntity213(
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

    def update_entity_213(self, entity_id: int, payload: HealthSchemaEntity213Update) -> Optional[HealthModelEntity213]:
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

    def get_entity_214_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity214]:
        return self.db.query(HealthModelEntity214).offset(skip).limit(limit).all()

    def get_entity_214_by_id(self, entity_id: int) -> Optional[HealthModelEntity214]:
        return self.db.query(HealthModelEntity214).filter(HealthModelEntity214.id == entity_id).first()

    def create_entity_214(self, payload: HealthSchemaEntity214Create) -> HealthModelEntity214:
        db_obj = HealthModelEntity214(
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

    def update_entity_214(self, entity_id: int, payload: HealthSchemaEntity214Update) -> Optional[HealthModelEntity214]:
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

    def get_entity_215_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity215]:
        return self.db.query(HealthModelEntity215).offset(skip).limit(limit).all()

    def get_entity_215_by_id(self, entity_id: int) -> Optional[HealthModelEntity215]:
        return self.db.query(HealthModelEntity215).filter(HealthModelEntity215.id == entity_id).first()

    def create_entity_215(self, payload: HealthSchemaEntity215Create) -> HealthModelEntity215:
        db_obj = HealthModelEntity215(
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

    def update_entity_215(self, entity_id: int, payload: HealthSchemaEntity215Update) -> Optional[HealthModelEntity215]:
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

    def get_entity_216_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity216]:
        return self.db.query(HealthModelEntity216).offset(skip).limit(limit).all()

    def get_entity_216_by_id(self, entity_id: int) -> Optional[HealthModelEntity216]:
        return self.db.query(HealthModelEntity216).filter(HealthModelEntity216.id == entity_id).first()

    def create_entity_216(self, payload: HealthSchemaEntity216Create) -> HealthModelEntity216:
        db_obj = HealthModelEntity216(
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

    def update_entity_216(self, entity_id: int, payload: HealthSchemaEntity216Update) -> Optional[HealthModelEntity216]:
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

    def get_entity_217_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity217]:
        return self.db.query(HealthModelEntity217).offset(skip).limit(limit).all()

    def get_entity_217_by_id(self, entity_id: int) -> Optional[HealthModelEntity217]:
        return self.db.query(HealthModelEntity217).filter(HealthModelEntity217.id == entity_id).first()

    def create_entity_217(self, payload: HealthSchemaEntity217Create) -> HealthModelEntity217:
        db_obj = HealthModelEntity217(
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

    def update_entity_217(self, entity_id: int, payload: HealthSchemaEntity217Update) -> Optional[HealthModelEntity217]:
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

    def get_entity_218_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity218]:
        return self.db.query(HealthModelEntity218).offset(skip).limit(limit).all()

    def get_entity_218_by_id(self, entity_id: int) -> Optional[HealthModelEntity218]:
        return self.db.query(HealthModelEntity218).filter(HealthModelEntity218.id == entity_id).first()

    def create_entity_218(self, payload: HealthSchemaEntity218Create) -> HealthModelEntity218:
        db_obj = HealthModelEntity218(
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

    def update_entity_218(self, entity_id: int, payload: HealthSchemaEntity218Update) -> Optional[HealthModelEntity218]:
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

    def get_entity_219_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity219]:
        return self.db.query(HealthModelEntity219).offset(skip).limit(limit).all()

    def get_entity_219_by_id(self, entity_id: int) -> Optional[HealthModelEntity219]:
        return self.db.query(HealthModelEntity219).filter(HealthModelEntity219.id == entity_id).first()

    def create_entity_219(self, payload: HealthSchemaEntity219Create) -> HealthModelEntity219:
        db_obj = HealthModelEntity219(
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

    def update_entity_219(self, entity_id: int, payload: HealthSchemaEntity219Update) -> Optional[HealthModelEntity219]:
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

    def get_entity_220_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity220]:
        return self.db.query(HealthModelEntity220).offset(skip).limit(limit).all()

    def get_entity_220_by_id(self, entity_id: int) -> Optional[HealthModelEntity220]:
        return self.db.query(HealthModelEntity220).filter(HealthModelEntity220.id == entity_id).first()

    def create_entity_220(self, payload: HealthSchemaEntity220Create) -> HealthModelEntity220:
        db_obj = HealthModelEntity220(
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

    def update_entity_220(self, entity_id: int, payload: HealthSchemaEntity220Update) -> Optional[HealthModelEntity220]:
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

    def get_entity_221_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity221]:
        return self.db.query(HealthModelEntity221).offset(skip).limit(limit).all()

    def get_entity_221_by_id(self, entity_id: int) -> Optional[HealthModelEntity221]:
        return self.db.query(HealthModelEntity221).filter(HealthModelEntity221.id == entity_id).first()

    def create_entity_221(self, payload: HealthSchemaEntity221Create) -> HealthModelEntity221:
        db_obj = HealthModelEntity221(
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

    def update_entity_221(self, entity_id: int, payload: HealthSchemaEntity221Update) -> Optional[HealthModelEntity221]:
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

    def get_entity_222_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity222]:
        return self.db.query(HealthModelEntity222).offset(skip).limit(limit).all()

    def get_entity_222_by_id(self, entity_id: int) -> Optional[HealthModelEntity222]:
        return self.db.query(HealthModelEntity222).filter(HealthModelEntity222.id == entity_id).first()

    def create_entity_222(self, payload: HealthSchemaEntity222Create) -> HealthModelEntity222:
        db_obj = HealthModelEntity222(
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

    def update_entity_222(self, entity_id: int, payload: HealthSchemaEntity222Update) -> Optional[HealthModelEntity222]:
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

    def get_entity_223_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity223]:
        return self.db.query(HealthModelEntity223).offset(skip).limit(limit).all()

    def get_entity_223_by_id(self, entity_id: int) -> Optional[HealthModelEntity223]:
        return self.db.query(HealthModelEntity223).filter(HealthModelEntity223.id == entity_id).first()

    def create_entity_223(self, payload: HealthSchemaEntity223Create) -> HealthModelEntity223:
        db_obj = HealthModelEntity223(
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

    def update_entity_223(self, entity_id: int, payload: HealthSchemaEntity223Update) -> Optional[HealthModelEntity223]:
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

    def get_entity_224_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity224]:
        return self.db.query(HealthModelEntity224).offset(skip).limit(limit).all()

    def get_entity_224_by_id(self, entity_id: int) -> Optional[HealthModelEntity224]:
        return self.db.query(HealthModelEntity224).filter(HealthModelEntity224.id == entity_id).first()

    def create_entity_224(self, payload: HealthSchemaEntity224Create) -> HealthModelEntity224:
        db_obj = HealthModelEntity224(
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

    def update_entity_224(self, entity_id: int, payload: HealthSchemaEntity224Update) -> Optional[HealthModelEntity224]:
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

    def get_entity_225_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity225]:
        return self.db.query(HealthModelEntity225).offset(skip).limit(limit).all()

    def get_entity_225_by_id(self, entity_id: int) -> Optional[HealthModelEntity225]:
        return self.db.query(HealthModelEntity225).filter(HealthModelEntity225.id == entity_id).first()

    def create_entity_225(self, payload: HealthSchemaEntity225Create) -> HealthModelEntity225:
        db_obj = HealthModelEntity225(
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

    def update_entity_225(self, entity_id: int, payload: HealthSchemaEntity225Update) -> Optional[HealthModelEntity225]:
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

    def get_entity_226_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity226]:
        return self.db.query(HealthModelEntity226).offset(skip).limit(limit).all()

    def get_entity_226_by_id(self, entity_id: int) -> Optional[HealthModelEntity226]:
        return self.db.query(HealthModelEntity226).filter(HealthModelEntity226.id == entity_id).first()

    def create_entity_226(self, payload: HealthSchemaEntity226Create) -> HealthModelEntity226:
        db_obj = HealthModelEntity226(
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

    def update_entity_226(self, entity_id: int, payload: HealthSchemaEntity226Update) -> Optional[HealthModelEntity226]:
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

    def get_entity_227_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity227]:
        return self.db.query(HealthModelEntity227).offset(skip).limit(limit).all()

    def get_entity_227_by_id(self, entity_id: int) -> Optional[HealthModelEntity227]:
        return self.db.query(HealthModelEntity227).filter(HealthModelEntity227.id == entity_id).first()

    def create_entity_227(self, payload: HealthSchemaEntity227Create) -> HealthModelEntity227:
        db_obj = HealthModelEntity227(
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

    def update_entity_227(self, entity_id: int, payload: HealthSchemaEntity227Update) -> Optional[HealthModelEntity227]:
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

    def get_entity_228_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity228]:
        return self.db.query(HealthModelEntity228).offset(skip).limit(limit).all()

    def get_entity_228_by_id(self, entity_id: int) -> Optional[HealthModelEntity228]:
        return self.db.query(HealthModelEntity228).filter(HealthModelEntity228.id == entity_id).first()

    def create_entity_228(self, payload: HealthSchemaEntity228Create) -> HealthModelEntity228:
        db_obj = HealthModelEntity228(
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

    def update_entity_228(self, entity_id: int, payload: HealthSchemaEntity228Update) -> Optional[HealthModelEntity228]:
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

    def get_entity_229_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity229]:
        return self.db.query(HealthModelEntity229).offset(skip).limit(limit).all()

    def get_entity_229_by_id(self, entity_id: int) -> Optional[HealthModelEntity229]:
        return self.db.query(HealthModelEntity229).filter(HealthModelEntity229.id == entity_id).first()

    def create_entity_229(self, payload: HealthSchemaEntity229Create) -> HealthModelEntity229:
        db_obj = HealthModelEntity229(
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

    def update_entity_229(self, entity_id: int, payload: HealthSchemaEntity229Update) -> Optional[HealthModelEntity229]:
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

    def get_entity_230_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity230]:
        return self.db.query(HealthModelEntity230).offset(skip).limit(limit).all()

    def get_entity_230_by_id(self, entity_id: int) -> Optional[HealthModelEntity230]:
        return self.db.query(HealthModelEntity230).filter(HealthModelEntity230.id == entity_id).first()

    def create_entity_230(self, payload: HealthSchemaEntity230Create) -> HealthModelEntity230:
        db_obj = HealthModelEntity230(
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

    def update_entity_230(self, entity_id: int, payload: HealthSchemaEntity230Update) -> Optional[HealthModelEntity230]:
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

    def get_entity_231_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity231]:
        return self.db.query(HealthModelEntity231).offset(skip).limit(limit).all()

    def get_entity_231_by_id(self, entity_id: int) -> Optional[HealthModelEntity231]:
        return self.db.query(HealthModelEntity231).filter(HealthModelEntity231.id == entity_id).first()

    def create_entity_231(self, payload: HealthSchemaEntity231Create) -> HealthModelEntity231:
        db_obj = HealthModelEntity231(
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

    def update_entity_231(self, entity_id: int, payload: HealthSchemaEntity231Update) -> Optional[HealthModelEntity231]:
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

    def get_entity_232_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity232]:
        return self.db.query(HealthModelEntity232).offset(skip).limit(limit).all()

    def get_entity_232_by_id(self, entity_id: int) -> Optional[HealthModelEntity232]:
        return self.db.query(HealthModelEntity232).filter(HealthModelEntity232.id == entity_id).first()

    def create_entity_232(self, payload: HealthSchemaEntity232Create) -> HealthModelEntity232:
        db_obj = HealthModelEntity232(
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

    def update_entity_232(self, entity_id: int, payload: HealthSchemaEntity232Update) -> Optional[HealthModelEntity232]:
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

    def get_entity_233_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity233]:
        return self.db.query(HealthModelEntity233).offset(skip).limit(limit).all()

    def get_entity_233_by_id(self, entity_id: int) -> Optional[HealthModelEntity233]:
        return self.db.query(HealthModelEntity233).filter(HealthModelEntity233.id == entity_id).first()

    def create_entity_233(self, payload: HealthSchemaEntity233Create) -> HealthModelEntity233:
        db_obj = HealthModelEntity233(
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

    def update_entity_233(self, entity_id: int, payload: HealthSchemaEntity233Update) -> Optional[HealthModelEntity233]:
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

    def get_entity_234_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity234]:
        return self.db.query(HealthModelEntity234).offset(skip).limit(limit).all()

    def get_entity_234_by_id(self, entity_id: int) -> Optional[HealthModelEntity234]:
        return self.db.query(HealthModelEntity234).filter(HealthModelEntity234.id == entity_id).first()

    def create_entity_234(self, payload: HealthSchemaEntity234Create) -> HealthModelEntity234:
        db_obj = HealthModelEntity234(
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

    def update_entity_234(self, entity_id: int, payload: HealthSchemaEntity234Update) -> Optional[HealthModelEntity234]:
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

    def get_entity_235_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity235]:
        return self.db.query(HealthModelEntity235).offset(skip).limit(limit).all()

    def get_entity_235_by_id(self, entity_id: int) -> Optional[HealthModelEntity235]:
        return self.db.query(HealthModelEntity235).filter(HealthModelEntity235.id == entity_id).first()

    def create_entity_235(self, payload: HealthSchemaEntity235Create) -> HealthModelEntity235:
        db_obj = HealthModelEntity235(
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

    def update_entity_235(self, entity_id: int, payload: HealthSchemaEntity235Update) -> Optional[HealthModelEntity235]:
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

    def get_entity_236_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity236]:
        return self.db.query(HealthModelEntity236).offset(skip).limit(limit).all()

    def get_entity_236_by_id(self, entity_id: int) -> Optional[HealthModelEntity236]:
        return self.db.query(HealthModelEntity236).filter(HealthModelEntity236.id == entity_id).first()

    def create_entity_236(self, payload: HealthSchemaEntity236Create) -> HealthModelEntity236:
        db_obj = HealthModelEntity236(
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

    def update_entity_236(self, entity_id: int, payload: HealthSchemaEntity236Update) -> Optional[HealthModelEntity236]:
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

    def get_entity_237_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity237]:
        return self.db.query(HealthModelEntity237).offset(skip).limit(limit).all()

    def get_entity_237_by_id(self, entity_id: int) -> Optional[HealthModelEntity237]:
        return self.db.query(HealthModelEntity237).filter(HealthModelEntity237.id == entity_id).first()

    def create_entity_237(self, payload: HealthSchemaEntity237Create) -> HealthModelEntity237:
        db_obj = HealthModelEntity237(
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

    def update_entity_237(self, entity_id: int, payload: HealthSchemaEntity237Update) -> Optional[HealthModelEntity237]:
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

    def get_entity_238_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity238]:
        return self.db.query(HealthModelEntity238).offset(skip).limit(limit).all()

    def get_entity_238_by_id(self, entity_id: int) -> Optional[HealthModelEntity238]:
        return self.db.query(HealthModelEntity238).filter(HealthModelEntity238.id == entity_id).first()

    def create_entity_238(self, payload: HealthSchemaEntity238Create) -> HealthModelEntity238:
        db_obj = HealthModelEntity238(
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

    def update_entity_238(self, entity_id: int, payload: HealthSchemaEntity238Update) -> Optional[HealthModelEntity238]:
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

    def get_entity_239_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity239]:
        return self.db.query(HealthModelEntity239).offset(skip).limit(limit).all()

    def get_entity_239_by_id(self, entity_id: int) -> Optional[HealthModelEntity239]:
        return self.db.query(HealthModelEntity239).filter(HealthModelEntity239.id == entity_id).first()

    def create_entity_239(self, payload: HealthSchemaEntity239Create) -> HealthModelEntity239:
        db_obj = HealthModelEntity239(
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

    def update_entity_239(self, entity_id: int, payload: HealthSchemaEntity239Update) -> Optional[HealthModelEntity239]:
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

    def get_entity_240_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity240]:
        return self.db.query(HealthModelEntity240).offset(skip).limit(limit).all()

    def get_entity_240_by_id(self, entity_id: int) -> Optional[HealthModelEntity240]:
        return self.db.query(HealthModelEntity240).filter(HealthModelEntity240.id == entity_id).first()

    def create_entity_240(self, payload: HealthSchemaEntity240Create) -> HealthModelEntity240:
        db_obj = HealthModelEntity240(
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

    def update_entity_240(self, entity_id: int, payload: HealthSchemaEntity240Update) -> Optional[HealthModelEntity240]:
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

    def get_entity_241_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity241]:
        return self.db.query(HealthModelEntity241).offset(skip).limit(limit).all()

    def get_entity_241_by_id(self, entity_id: int) -> Optional[HealthModelEntity241]:
        return self.db.query(HealthModelEntity241).filter(HealthModelEntity241.id == entity_id).first()

    def create_entity_241(self, payload: HealthSchemaEntity241Create) -> HealthModelEntity241:
        db_obj = HealthModelEntity241(
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

    def update_entity_241(self, entity_id: int, payload: HealthSchemaEntity241Update) -> Optional[HealthModelEntity241]:
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

    def get_entity_242_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity242]:
        return self.db.query(HealthModelEntity242).offset(skip).limit(limit).all()

    def get_entity_242_by_id(self, entity_id: int) -> Optional[HealthModelEntity242]:
        return self.db.query(HealthModelEntity242).filter(HealthModelEntity242.id == entity_id).first()

    def create_entity_242(self, payload: HealthSchemaEntity242Create) -> HealthModelEntity242:
        db_obj = HealthModelEntity242(
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

    def update_entity_242(self, entity_id: int, payload: HealthSchemaEntity242Update) -> Optional[HealthModelEntity242]:
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

    def get_entity_243_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity243]:
        return self.db.query(HealthModelEntity243).offset(skip).limit(limit).all()

    def get_entity_243_by_id(self, entity_id: int) -> Optional[HealthModelEntity243]:
        return self.db.query(HealthModelEntity243).filter(HealthModelEntity243.id == entity_id).first()

    def create_entity_243(self, payload: HealthSchemaEntity243Create) -> HealthModelEntity243:
        db_obj = HealthModelEntity243(
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

    def update_entity_243(self, entity_id: int, payload: HealthSchemaEntity243Update) -> Optional[HealthModelEntity243]:
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

    def get_entity_244_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity244]:
        return self.db.query(HealthModelEntity244).offset(skip).limit(limit).all()

    def get_entity_244_by_id(self, entity_id: int) -> Optional[HealthModelEntity244]:
        return self.db.query(HealthModelEntity244).filter(HealthModelEntity244.id == entity_id).first()

    def create_entity_244(self, payload: HealthSchemaEntity244Create) -> HealthModelEntity244:
        db_obj = HealthModelEntity244(
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

    def update_entity_244(self, entity_id: int, payload: HealthSchemaEntity244Update) -> Optional[HealthModelEntity244]:
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

    def get_entity_245_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity245]:
        return self.db.query(HealthModelEntity245).offset(skip).limit(limit).all()

    def get_entity_245_by_id(self, entity_id: int) -> Optional[HealthModelEntity245]:
        return self.db.query(HealthModelEntity245).filter(HealthModelEntity245.id == entity_id).first()

    def create_entity_245(self, payload: HealthSchemaEntity245Create) -> HealthModelEntity245:
        db_obj = HealthModelEntity245(
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

    def update_entity_245(self, entity_id: int, payload: HealthSchemaEntity245Update) -> Optional[HealthModelEntity245]:
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

    def get_entity_246_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity246]:
        return self.db.query(HealthModelEntity246).offset(skip).limit(limit).all()

    def get_entity_246_by_id(self, entity_id: int) -> Optional[HealthModelEntity246]:
        return self.db.query(HealthModelEntity246).filter(HealthModelEntity246.id == entity_id).first()

    def create_entity_246(self, payload: HealthSchemaEntity246Create) -> HealthModelEntity246:
        db_obj = HealthModelEntity246(
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

    def update_entity_246(self, entity_id: int, payload: HealthSchemaEntity246Update) -> Optional[HealthModelEntity246]:
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

    def get_entity_247_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity247]:
        return self.db.query(HealthModelEntity247).offset(skip).limit(limit).all()

    def get_entity_247_by_id(self, entity_id: int) -> Optional[HealthModelEntity247]:
        return self.db.query(HealthModelEntity247).filter(HealthModelEntity247.id == entity_id).first()

    def create_entity_247(self, payload: HealthSchemaEntity247Create) -> HealthModelEntity247:
        db_obj = HealthModelEntity247(
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

    def update_entity_247(self, entity_id: int, payload: HealthSchemaEntity247Update) -> Optional[HealthModelEntity247]:
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

    def get_entity_248_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity248]:
        return self.db.query(HealthModelEntity248).offset(skip).limit(limit).all()

    def get_entity_248_by_id(self, entity_id: int) -> Optional[HealthModelEntity248]:
        return self.db.query(HealthModelEntity248).filter(HealthModelEntity248.id == entity_id).first()

    def create_entity_248(self, payload: HealthSchemaEntity248Create) -> HealthModelEntity248:
        db_obj = HealthModelEntity248(
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

    def update_entity_248(self, entity_id: int, payload: HealthSchemaEntity248Update) -> Optional[HealthModelEntity248]:
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

    def get_entity_249_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity249]:
        return self.db.query(HealthModelEntity249).offset(skip).limit(limit).all()

    def get_entity_249_by_id(self, entity_id: int) -> Optional[HealthModelEntity249]:
        return self.db.query(HealthModelEntity249).filter(HealthModelEntity249.id == entity_id).first()

    def create_entity_249(self, payload: HealthSchemaEntity249Create) -> HealthModelEntity249:
        db_obj = HealthModelEntity249(
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

    def update_entity_249(self, entity_id: int, payload: HealthSchemaEntity249Update) -> Optional[HealthModelEntity249]:
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

    def get_entity_250_list(self, skip: int = 0, limit: int = 100) -> List[HealthModelEntity250]:
        return self.db.query(HealthModelEntity250).offset(skip).limit(limit).all()

    def get_entity_250_by_id(self, entity_id: int) -> Optional[HealthModelEntity250]:
        return self.db.query(HealthModelEntity250).filter(HealthModelEntity250.id == entity_id).first()

    def create_entity_250(self, payload: HealthSchemaEntity250Create) -> HealthModelEntity250:
        db_obj = HealthModelEntity250(
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

    def update_entity_250(self, entity_id: int, payload: HealthSchemaEntity250Update) -> Optional[HealthModelEntity250]:
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

