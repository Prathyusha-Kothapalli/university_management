"""
Human Resources & Faculty Management - Service Business Logic Layer
Module: app.domains.hr.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.hr.models import *
from app.domains.hr.schemas import *

class HrDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity1]:
        return self.db.query(HrModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[HrModelEntity1]:
        return self.db.query(HrModelEntity1).filter(HrModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: HrSchemaEntity1Create) -> HrModelEntity1:
        db_obj = HrModelEntity1(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_1(self, entity_id: int, payload: HrSchemaEntity1Update) -> Optional[HrModelEntity1]:
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

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity2]:
        return self.db.query(HrModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[HrModelEntity2]:
        return self.db.query(HrModelEntity2).filter(HrModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: HrSchemaEntity2Create) -> HrModelEntity2:
        db_obj = HrModelEntity2(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_2(self, entity_id: int, payload: HrSchemaEntity2Update) -> Optional[HrModelEntity2]:
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

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity3]:
        return self.db.query(HrModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[HrModelEntity3]:
        return self.db.query(HrModelEntity3).filter(HrModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: HrSchemaEntity3Create) -> HrModelEntity3:
        db_obj = HrModelEntity3(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_3(self, entity_id: int, payload: HrSchemaEntity3Update) -> Optional[HrModelEntity3]:
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

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity4]:
        return self.db.query(HrModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[HrModelEntity4]:
        return self.db.query(HrModelEntity4).filter(HrModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: HrSchemaEntity4Create) -> HrModelEntity4:
        db_obj = HrModelEntity4(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_4(self, entity_id: int, payload: HrSchemaEntity4Update) -> Optional[HrModelEntity4]:
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

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity5]:
        return self.db.query(HrModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[HrModelEntity5]:
        return self.db.query(HrModelEntity5).filter(HrModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: HrSchemaEntity5Create) -> HrModelEntity5:
        db_obj = HrModelEntity5(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_5(self, entity_id: int, payload: HrSchemaEntity5Update) -> Optional[HrModelEntity5]:
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

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity6]:
        return self.db.query(HrModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[HrModelEntity6]:
        return self.db.query(HrModelEntity6).filter(HrModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: HrSchemaEntity6Create) -> HrModelEntity6:
        db_obj = HrModelEntity6(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_6(self, entity_id: int, payload: HrSchemaEntity6Update) -> Optional[HrModelEntity6]:
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

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity7]:
        return self.db.query(HrModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[HrModelEntity7]:
        return self.db.query(HrModelEntity7).filter(HrModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: HrSchemaEntity7Create) -> HrModelEntity7:
        db_obj = HrModelEntity7(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_7(self, entity_id: int, payload: HrSchemaEntity7Update) -> Optional[HrModelEntity7]:
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

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity8]:
        return self.db.query(HrModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[HrModelEntity8]:
        return self.db.query(HrModelEntity8).filter(HrModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: HrSchemaEntity8Create) -> HrModelEntity8:
        db_obj = HrModelEntity8(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_8(self, entity_id: int, payload: HrSchemaEntity8Update) -> Optional[HrModelEntity8]:
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

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity9]:
        return self.db.query(HrModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[HrModelEntity9]:
        return self.db.query(HrModelEntity9).filter(HrModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: HrSchemaEntity9Create) -> HrModelEntity9:
        db_obj = HrModelEntity9(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_9(self, entity_id: int, payload: HrSchemaEntity9Update) -> Optional[HrModelEntity9]:
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

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity10]:
        return self.db.query(HrModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[HrModelEntity10]:
        return self.db.query(HrModelEntity10).filter(HrModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: HrSchemaEntity10Create) -> HrModelEntity10:
        db_obj = HrModelEntity10(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_10(self, entity_id: int, payload: HrSchemaEntity10Update) -> Optional[HrModelEntity10]:
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

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity11]:
        return self.db.query(HrModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[HrModelEntity11]:
        return self.db.query(HrModelEntity11).filter(HrModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: HrSchemaEntity11Create) -> HrModelEntity11:
        db_obj = HrModelEntity11(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_11(self, entity_id: int, payload: HrSchemaEntity11Update) -> Optional[HrModelEntity11]:
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

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity12]:
        return self.db.query(HrModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[HrModelEntity12]:
        return self.db.query(HrModelEntity12).filter(HrModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: HrSchemaEntity12Create) -> HrModelEntity12:
        db_obj = HrModelEntity12(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_12(self, entity_id: int, payload: HrSchemaEntity12Update) -> Optional[HrModelEntity12]:
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

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity13]:
        return self.db.query(HrModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[HrModelEntity13]:
        return self.db.query(HrModelEntity13).filter(HrModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: HrSchemaEntity13Create) -> HrModelEntity13:
        db_obj = HrModelEntity13(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_13(self, entity_id: int, payload: HrSchemaEntity13Update) -> Optional[HrModelEntity13]:
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

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity14]:
        return self.db.query(HrModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[HrModelEntity14]:
        return self.db.query(HrModelEntity14).filter(HrModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: HrSchemaEntity14Create) -> HrModelEntity14:
        db_obj = HrModelEntity14(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_14(self, entity_id: int, payload: HrSchemaEntity14Update) -> Optional[HrModelEntity14]:
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

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity15]:
        return self.db.query(HrModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[HrModelEntity15]:
        return self.db.query(HrModelEntity15).filter(HrModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: HrSchemaEntity15Create) -> HrModelEntity15:
        db_obj = HrModelEntity15(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_15(self, entity_id: int, payload: HrSchemaEntity15Update) -> Optional[HrModelEntity15]:
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

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity16]:
        return self.db.query(HrModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[HrModelEntity16]:
        return self.db.query(HrModelEntity16).filter(HrModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: HrSchemaEntity16Create) -> HrModelEntity16:
        db_obj = HrModelEntity16(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_16(self, entity_id: int, payload: HrSchemaEntity16Update) -> Optional[HrModelEntity16]:
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

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity17]:
        return self.db.query(HrModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[HrModelEntity17]:
        return self.db.query(HrModelEntity17).filter(HrModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: HrSchemaEntity17Create) -> HrModelEntity17:
        db_obj = HrModelEntity17(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_17(self, entity_id: int, payload: HrSchemaEntity17Update) -> Optional[HrModelEntity17]:
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

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity18]:
        return self.db.query(HrModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[HrModelEntity18]:
        return self.db.query(HrModelEntity18).filter(HrModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: HrSchemaEntity18Create) -> HrModelEntity18:
        db_obj = HrModelEntity18(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_18(self, entity_id: int, payload: HrSchemaEntity18Update) -> Optional[HrModelEntity18]:
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

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity19]:
        return self.db.query(HrModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[HrModelEntity19]:
        return self.db.query(HrModelEntity19).filter(HrModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: HrSchemaEntity19Create) -> HrModelEntity19:
        db_obj = HrModelEntity19(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_19(self, entity_id: int, payload: HrSchemaEntity19Update) -> Optional[HrModelEntity19]:
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

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity20]:
        return self.db.query(HrModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[HrModelEntity20]:
        return self.db.query(HrModelEntity20).filter(HrModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: HrSchemaEntity20Create) -> HrModelEntity20:
        db_obj = HrModelEntity20(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_20(self, entity_id: int, payload: HrSchemaEntity20Update) -> Optional[HrModelEntity20]:
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

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity21]:
        return self.db.query(HrModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[HrModelEntity21]:
        return self.db.query(HrModelEntity21).filter(HrModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: HrSchemaEntity21Create) -> HrModelEntity21:
        db_obj = HrModelEntity21(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_21(self, entity_id: int, payload: HrSchemaEntity21Update) -> Optional[HrModelEntity21]:
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

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity22]:
        return self.db.query(HrModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[HrModelEntity22]:
        return self.db.query(HrModelEntity22).filter(HrModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: HrSchemaEntity22Create) -> HrModelEntity22:
        db_obj = HrModelEntity22(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_22(self, entity_id: int, payload: HrSchemaEntity22Update) -> Optional[HrModelEntity22]:
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

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity23]:
        return self.db.query(HrModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[HrModelEntity23]:
        return self.db.query(HrModelEntity23).filter(HrModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: HrSchemaEntity23Create) -> HrModelEntity23:
        db_obj = HrModelEntity23(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_23(self, entity_id: int, payload: HrSchemaEntity23Update) -> Optional[HrModelEntity23]:
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

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity24]:
        return self.db.query(HrModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[HrModelEntity24]:
        return self.db.query(HrModelEntity24).filter(HrModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: HrSchemaEntity24Create) -> HrModelEntity24:
        db_obj = HrModelEntity24(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_24(self, entity_id: int, payload: HrSchemaEntity24Update) -> Optional[HrModelEntity24]:
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

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity25]:
        return self.db.query(HrModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[HrModelEntity25]:
        return self.db.query(HrModelEntity25).filter(HrModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: HrSchemaEntity25Create) -> HrModelEntity25:
        db_obj = HrModelEntity25(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_25(self, entity_id: int, payload: HrSchemaEntity25Update) -> Optional[HrModelEntity25]:
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

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity26]:
        return self.db.query(HrModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[HrModelEntity26]:
        return self.db.query(HrModelEntity26).filter(HrModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: HrSchemaEntity26Create) -> HrModelEntity26:
        db_obj = HrModelEntity26(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_26(self, entity_id: int, payload: HrSchemaEntity26Update) -> Optional[HrModelEntity26]:
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

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity27]:
        return self.db.query(HrModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[HrModelEntity27]:
        return self.db.query(HrModelEntity27).filter(HrModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: HrSchemaEntity27Create) -> HrModelEntity27:
        db_obj = HrModelEntity27(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_27(self, entity_id: int, payload: HrSchemaEntity27Update) -> Optional[HrModelEntity27]:
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

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity28]:
        return self.db.query(HrModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[HrModelEntity28]:
        return self.db.query(HrModelEntity28).filter(HrModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: HrSchemaEntity28Create) -> HrModelEntity28:
        db_obj = HrModelEntity28(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_28(self, entity_id: int, payload: HrSchemaEntity28Update) -> Optional[HrModelEntity28]:
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

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity29]:
        return self.db.query(HrModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[HrModelEntity29]:
        return self.db.query(HrModelEntity29).filter(HrModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: HrSchemaEntity29Create) -> HrModelEntity29:
        db_obj = HrModelEntity29(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_29(self, entity_id: int, payload: HrSchemaEntity29Update) -> Optional[HrModelEntity29]:
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

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity30]:
        return self.db.query(HrModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[HrModelEntity30]:
        return self.db.query(HrModelEntity30).filter(HrModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: HrSchemaEntity30Create) -> HrModelEntity30:
        db_obj = HrModelEntity30(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_30(self, entity_id: int, payload: HrSchemaEntity30Update) -> Optional[HrModelEntity30]:
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

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity31]:
        return self.db.query(HrModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[HrModelEntity31]:
        return self.db.query(HrModelEntity31).filter(HrModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: HrSchemaEntity31Create) -> HrModelEntity31:
        db_obj = HrModelEntity31(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_31(self, entity_id: int, payload: HrSchemaEntity31Update) -> Optional[HrModelEntity31]:
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

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity32]:
        return self.db.query(HrModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[HrModelEntity32]:
        return self.db.query(HrModelEntity32).filter(HrModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: HrSchemaEntity32Create) -> HrModelEntity32:
        db_obj = HrModelEntity32(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_32(self, entity_id: int, payload: HrSchemaEntity32Update) -> Optional[HrModelEntity32]:
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

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity33]:
        return self.db.query(HrModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[HrModelEntity33]:
        return self.db.query(HrModelEntity33).filter(HrModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: HrSchemaEntity33Create) -> HrModelEntity33:
        db_obj = HrModelEntity33(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_33(self, entity_id: int, payload: HrSchemaEntity33Update) -> Optional[HrModelEntity33]:
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

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity34]:
        return self.db.query(HrModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[HrModelEntity34]:
        return self.db.query(HrModelEntity34).filter(HrModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: HrSchemaEntity34Create) -> HrModelEntity34:
        db_obj = HrModelEntity34(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_34(self, entity_id: int, payload: HrSchemaEntity34Update) -> Optional[HrModelEntity34]:
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

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity35]:
        return self.db.query(HrModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[HrModelEntity35]:
        return self.db.query(HrModelEntity35).filter(HrModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: HrSchemaEntity35Create) -> HrModelEntity35:
        db_obj = HrModelEntity35(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_35(self, entity_id: int, payload: HrSchemaEntity35Update) -> Optional[HrModelEntity35]:
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

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity36]:
        return self.db.query(HrModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[HrModelEntity36]:
        return self.db.query(HrModelEntity36).filter(HrModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: HrSchemaEntity36Create) -> HrModelEntity36:
        db_obj = HrModelEntity36(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_36(self, entity_id: int, payload: HrSchemaEntity36Update) -> Optional[HrModelEntity36]:
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

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity37]:
        return self.db.query(HrModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[HrModelEntity37]:
        return self.db.query(HrModelEntity37).filter(HrModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: HrSchemaEntity37Create) -> HrModelEntity37:
        db_obj = HrModelEntity37(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_37(self, entity_id: int, payload: HrSchemaEntity37Update) -> Optional[HrModelEntity37]:
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

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity38]:
        return self.db.query(HrModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[HrModelEntity38]:
        return self.db.query(HrModelEntity38).filter(HrModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: HrSchemaEntity38Create) -> HrModelEntity38:
        db_obj = HrModelEntity38(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_38(self, entity_id: int, payload: HrSchemaEntity38Update) -> Optional[HrModelEntity38]:
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

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity39]:
        return self.db.query(HrModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[HrModelEntity39]:
        return self.db.query(HrModelEntity39).filter(HrModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: HrSchemaEntity39Create) -> HrModelEntity39:
        db_obj = HrModelEntity39(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_39(self, entity_id: int, payload: HrSchemaEntity39Update) -> Optional[HrModelEntity39]:
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

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity40]:
        return self.db.query(HrModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[HrModelEntity40]:
        return self.db.query(HrModelEntity40).filter(HrModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: HrSchemaEntity40Create) -> HrModelEntity40:
        db_obj = HrModelEntity40(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_40(self, entity_id: int, payload: HrSchemaEntity40Update) -> Optional[HrModelEntity40]:
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

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity41]:
        return self.db.query(HrModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[HrModelEntity41]:
        return self.db.query(HrModelEntity41).filter(HrModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: HrSchemaEntity41Create) -> HrModelEntity41:
        db_obj = HrModelEntity41(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_41(self, entity_id: int, payload: HrSchemaEntity41Update) -> Optional[HrModelEntity41]:
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

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity42]:
        return self.db.query(HrModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[HrModelEntity42]:
        return self.db.query(HrModelEntity42).filter(HrModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: HrSchemaEntity42Create) -> HrModelEntity42:
        db_obj = HrModelEntity42(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_42(self, entity_id: int, payload: HrSchemaEntity42Update) -> Optional[HrModelEntity42]:
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

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity43]:
        return self.db.query(HrModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[HrModelEntity43]:
        return self.db.query(HrModelEntity43).filter(HrModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: HrSchemaEntity43Create) -> HrModelEntity43:
        db_obj = HrModelEntity43(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_43(self, entity_id: int, payload: HrSchemaEntity43Update) -> Optional[HrModelEntity43]:
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

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity44]:
        return self.db.query(HrModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[HrModelEntity44]:
        return self.db.query(HrModelEntity44).filter(HrModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: HrSchemaEntity44Create) -> HrModelEntity44:
        db_obj = HrModelEntity44(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_44(self, entity_id: int, payload: HrSchemaEntity44Update) -> Optional[HrModelEntity44]:
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

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity45]:
        return self.db.query(HrModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[HrModelEntity45]:
        return self.db.query(HrModelEntity45).filter(HrModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: HrSchemaEntity45Create) -> HrModelEntity45:
        db_obj = HrModelEntity45(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_45(self, entity_id: int, payload: HrSchemaEntity45Update) -> Optional[HrModelEntity45]:
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

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity46]:
        return self.db.query(HrModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[HrModelEntity46]:
        return self.db.query(HrModelEntity46).filter(HrModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: HrSchemaEntity46Create) -> HrModelEntity46:
        db_obj = HrModelEntity46(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_46(self, entity_id: int, payload: HrSchemaEntity46Update) -> Optional[HrModelEntity46]:
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

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity47]:
        return self.db.query(HrModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[HrModelEntity47]:
        return self.db.query(HrModelEntity47).filter(HrModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: HrSchemaEntity47Create) -> HrModelEntity47:
        db_obj = HrModelEntity47(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_47(self, entity_id: int, payload: HrSchemaEntity47Update) -> Optional[HrModelEntity47]:
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

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity48]:
        return self.db.query(HrModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[HrModelEntity48]:
        return self.db.query(HrModelEntity48).filter(HrModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: HrSchemaEntity48Create) -> HrModelEntity48:
        db_obj = HrModelEntity48(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_48(self, entity_id: int, payload: HrSchemaEntity48Update) -> Optional[HrModelEntity48]:
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

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity49]:
        return self.db.query(HrModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[HrModelEntity49]:
        return self.db.query(HrModelEntity49).filter(HrModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: HrSchemaEntity49Create) -> HrModelEntity49:
        db_obj = HrModelEntity49(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_49(self, entity_id: int, payload: HrSchemaEntity49Update) -> Optional[HrModelEntity49]:
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

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity50]:
        return self.db.query(HrModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[HrModelEntity50]:
        return self.db.query(HrModelEntity50).filter(HrModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: HrSchemaEntity50Create) -> HrModelEntity50:
        db_obj = HrModelEntity50(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_50(self, entity_id: int, payload: HrSchemaEntity50Update) -> Optional[HrModelEntity50]:
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

    def get_entity_51_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity51]:
        return self.db.query(HrModelEntity51).offset(skip).limit(limit).all()

    def get_entity_51_by_id(self, entity_id: int) -> Optional[HrModelEntity51]:
        return self.db.query(HrModelEntity51).filter(HrModelEntity51.id == entity_id).first()

    def create_entity_51(self, payload: HrSchemaEntity51Create) -> HrModelEntity51:
        db_obj = HrModelEntity51(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_51(self, entity_id: int, payload: HrSchemaEntity51Update) -> Optional[HrModelEntity51]:
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

    def get_entity_52_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity52]:
        return self.db.query(HrModelEntity52).offset(skip).limit(limit).all()

    def get_entity_52_by_id(self, entity_id: int) -> Optional[HrModelEntity52]:
        return self.db.query(HrModelEntity52).filter(HrModelEntity52.id == entity_id).first()

    def create_entity_52(self, payload: HrSchemaEntity52Create) -> HrModelEntity52:
        db_obj = HrModelEntity52(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_52(self, entity_id: int, payload: HrSchemaEntity52Update) -> Optional[HrModelEntity52]:
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

    def get_entity_53_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity53]:
        return self.db.query(HrModelEntity53).offset(skip).limit(limit).all()

    def get_entity_53_by_id(self, entity_id: int) -> Optional[HrModelEntity53]:
        return self.db.query(HrModelEntity53).filter(HrModelEntity53.id == entity_id).first()

    def create_entity_53(self, payload: HrSchemaEntity53Create) -> HrModelEntity53:
        db_obj = HrModelEntity53(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_53(self, entity_id: int, payload: HrSchemaEntity53Update) -> Optional[HrModelEntity53]:
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

    def get_entity_54_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity54]:
        return self.db.query(HrModelEntity54).offset(skip).limit(limit).all()

    def get_entity_54_by_id(self, entity_id: int) -> Optional[HrModelEntity54]:
        return self.db.query(HrModelEntity54).filter(HrModelEntity54.id == entity_id).first()

    def create_entity_54(self, payload: HrSchemaEntity54Create) -> HrModelEntity54:
        db_obj = HrModelEntity54(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_54(self, entity_id: int, payload: HrSchemaEntity54Update) -> Optional[HrModelEntity54]:
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

    def get_entity_55_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity55]:
        return self.db.query(HrModelEntity55).offset(skip).limit(limit).all()

    def get_entity_55_by_id(self, entity_id: int) -> Optional[HrModelEntity55]:
        return self.db.query(HrModelEntity55).filter(HrModelEntity55.id == entity_id).first()

    def create_entity_55(self, payload: HrSchemaEntity55Create) -> HrModelEntity55:
        db_obj = HrModelEntity55(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_55(self, entity_id: int, payload: HrSchemaEntity55Update) -> Optional[HrModelEntity55]:
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

    def get_entity_56_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity56]:
        return self.db.query(HrModelEntity56).offset(skip).limit(limit).all()

    def get_entity_56_by_id(self, entity_id: int) -> Optional[HrModelEntity56]:
        return self.db.query(HrModelEntity56).filter(HrModelEntity56.id == entity_id).first()

    def create_entity_56(self, payload: HrSchemaEntity56Create) -> HrModelEntity56:
        db_obj = HrModelEntity56(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_56(self, entity_id: int, payload: HrSchemaEntity56Update) -> Optional[HrModelEntity56]:
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

    def get_entity_57_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity57]:
        return self.db.query(HrModelEntity57).offset(skip).limit(limit).all()

    def get_entity_57_by_id(self, entity_id: int) -> Optional[HrModelEntity57]:
        return self.db.query(HrModelEntity57).filter(HrModelEntity57.id == entity_id).first()

    def create_entity_57(self, payload: HrSchemaEntity57Create) -> HrModelEntity57:
        db_obj = HrModelEntity57(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_57(self, entity_id: int, payload: HrSchemaEntity57Update) -> Optional[HrModelEntity57]:
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

    def get_entity_58_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity58]:
        return self.db.query(HrModelEntity58).offset(skip).limit(limit).all()

    def get_entity_58_by_id(self, entity_id: int) -> Optional[HrModelEntity58]:
        return self.db.query(HrModelEntity58).filter(HrModelEntity58.id == entity_id).first()

    def create_entity_58(self, payload: HrSchemaEntity58Create) -> HrModelEntity58:
        db_obj = HrModelEntity58(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_58(self, entity_id: int, payload: HrSchemaEntity58Update) -> Optional[HrModelEntity58]:
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

    def get_entity_59_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity59]:
        return self.db.query(HrModelEntity59).offset(skip).limit(limit).all()

    def get_entity_59_by_id(self, entity_id: int) -> Optional[HrModelEntity59]:
        return self.db.query(HrModelEntity59).filter(HrModelEntity59.id == entity_id).first()

    def create_entity_59(self, payload: HrSchemaEntity59Create) -> HrModelEntity59:
        db_obj = HrModelEntity59(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_59(self, entity_id: int, payload: HrSchemaEntity59Update) -> Optional[HrModelEntity59]:
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

    def get_entity_60_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity60]:
        return self.db.query(HrModelEntity60).offset(skip).limit(limit).all()

    def get_entity_60_by_id(self, entity_id: int) -> Optional[HrModelEntity60]:
        return self.db.query(HrModelEntity60).filter(HrModelEntity60.id == entity_id).first()

    def create_entity_60(self, payload: HrSchemaEntity60Create) -> HrModelEntity60:
        db_obj = HrModelEntity60(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_60(self, entity_id: int, payload: HrSchemaEntity60Update) -> Optional[HrModelEntity60]:
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

    def get_entity_61_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity61]:
        return self.db.query(HrModelEntity61).offset(skip).limit(limit).all()

    def get_entity_61_by_id(self, entity_id: int) -> Optional[HrModelEntity61]:
        return self.db.query(HrModelEntity61).filter(HrModelEntity61.id == entity_id).first()

    def create_entity_61(self, payload: HrSchemaEntity61Create) -> HrModelEntity61:
        db_obj = HrModelEntity61(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_61(self, entity_id: int, payload: HrSchemaEntity61Update) -> Optional[HrModelEntity61]:
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

    def get_entity_62_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity62]:
        return self.db.query(HrModelEntity62).offset(skip).limit(limit).all()

    def get_entity_62_by_id(self, entity_id: int) -> Optional[HrModelEntity62]:
        return self.db.query(HrModelEntity62).filter(HrModelEntity62.id == entity_id).first()

    def create_entity_62(self, payload: HrSchemaEntity62Create) -> HrModelEntity62:
        db_obj = HrModelEntity62(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_62(self, entity_id: int, payload: HrSchemaEntity62Update) -> Optional[HrModelEntity62]:
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

    def get_entity_63_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity63]:
        return self.db.query(HrModelEntity63).offset(skip).limit(limit).all()

    def get_entity_63_by_id(self, entity_id: int) -> Optional[HrModelEntity63]:
        return self.db.query(HrModelEntity63).filter(HrModelEntity63.id == entity_id).first()

    def create_entity_63(self, payload: HrSchemaEntity63Create) -> HrModelEntity63:
        db_obj = HrModelEntity63(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_63(self, entity_id: int, payload: HrSchemaEntity63Update) -> Optional[HrModelEntity63]:
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

    def get_entity_64_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity64]:
        return self.db.query(HrModelEntity64).offset(skip).limit(limit).all()

    def get_entity_64_by_id(self, entity_id: int) -> Optional[HrModelEntity64]:
        return self.db.query(HrModelEntity64).filter(HrModelEntity64.id == entity_id).first()

    def create_entity_64(self, payload: HrSchemaEntity64Create) -> HrModelEntity64:
        db_obj = HrModelEntity64(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_64(self, entity_id: int, payload: HrSchemaEntity64Update) -> Optional[HrModelEntity64]:
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

    def get_entity_65_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity65]:
        return self.db.query(HrModelEntity65).offset(skip).limit(limit).all()

    def get_entity_65_by_id(self, entity_id: int) -> Optional[HrModelEntity65]:
        return self.db.query(HrModelEntity65).filter(HrModelEntity65.id == entity_id).first()

    def create_entity_65(self, payload: HrSchemaEntity65Create) -> HrModelEntity65:
        db_obj = HrModelEntity65(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_65(self, entity_id: int, payload: HrSchemaEntity65Update) -> Optional[HrModelEntity65]:
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

    def get_entity_66_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity66]:
        return self.db.query(HrModelEntity66).offset(skip).limit(limit).all()

    def get_entity_66_by_id(self, entity_id: int) -> Optional[HrModelEntity66]:
        return self.db.query(HrModelEntity66).filter(HrModelEntity66.id == entity_id).first()

    def create_entity_66(self, payload: HrSchemaEntity66Create) -> HrModelEntity66:
        db_obj = HrModelEntity66(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_66(self, entity_id: int, payload: HrSchemaEntity66Update) -> Optional[HrModelEntity66]:
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

    def get_entity_67_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity67]:
        return self.db.query(HrModelEntity67).offset(skip).limit(limit).all()

    def get_entity_67_by_id(self, entity_id: int) -> Optional[HrModelEntity67]:
        return self.db.query(HrModelEntity67).filter(HrModelEntity67.id == entity_id).first()

    def create_entity_67(self, payload: HrSchemaEntity67Create) -> HrModelEntity67:
        db_obj = HrModelEntity67(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_67(self, entity_id: int, payload: HrSchemaEntity67Update) -> Optional[HrModelEntity67]:
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

    def get_entity_68_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity68]:
        return self.db.query(HrModelEntity68).offset(skip).limit(limit).all()

    def get_entity_68_by_id(self, entity_id: int) -> Optional[HrModelEntity68]:
        return self.db.query(HrModelEntity68).filter(HrModelEntity68.id == entity_id).first()

    def create_entity_68(self, payload: HrSchemaEntity68Create) -> HrModelEntity68:
        db_obj = HrModelEntity68(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_68(self, entity_id: int, payload: HrSchemaEntity68Update) -> Optional[HrModelEntity68]:
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

    def get_entity_69_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity69]:
        return self.db.query(HrModelEntity69).offset(skip).limit(limit).all()

    def get_entity_69_by_id(self, entity_id: int) -> Optional[HrModelEntity69]:
        return self.db.query(HrModelEntity69).filter(HrModelEntity69.id == entity_id).first()

    def create_entity_69(self, payload: HrSchemaEntity69Create) -> HrModelEntity69:
        db_obj = HrModelEntity69(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_69(self, entity_id: int, payload: HrSchemaEntity69Update) -> Optional[HrModelEntity69]:
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

    def get_entity_70_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity70]:
        return self.db.query(HrModelEntity70).offset(skip).limit(limit).all()

    def get_entity_70_by_id(self, entity_id: int) -> Optional[HrModelEntity70]:
        return self.db.query(HrModelEntity70).filter(HrModelEntity70.id == entity_id).first()

    def create_entity_70(self, payload: HrSchemaEntity70Create) -> HrModelEntity70:
        db_obj = HrModelEntity70(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_70(self, entity_id: int, payload: HrSchemaEntity70Update) -> Optional[HrModelEntity70]:
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

    def get_entity_71_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity71]:
        return self.db.query(HrModelEntity71).offset(skip).limit(limit).all()

    def get_entity_71_by_id(self, entity_id: int) -> Optional[HrModelEntity71]:
        return self.db.query(HrModelEntity71).filter(HrModelEntity71.id == entity_id).first()

    def create_entity_71(self, payload: HrSchemaEntity71Create) -> HrModelEntity71:
        db_obj = HrModelEntity71(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_71(self, entity_id: int, payload: HrSchemaEntity71Update) -> Optional[HrModelEntity71]:
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

    def get_entity_72_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity72]:
        return self.db.query(HrModelEntity72).offset(skip).limit(limit).all()

    def get_entity_72_by_id(self, entity_id: int) -> Optional[HrModelEntity72]:
        return self.db.query(HrModelEntity72).filter(HrModelEntity72.id == entity_id).first()

    def create_entity_72(self, payload: HrSchemaEntity72Create) -> HrModelEntity72:
        db_obj = HrModelEntity72(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_72(self, entity_id: int, payload: HrSchemaEntity72Update) -> Optional[HrModelEntity72]:
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

    def get_entity_73_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity73]:
        return self.db.query(HrModelEntity73).offset(skip).limit(limit).all()

    def get_entity_73_by_id(self, entity_id: int) -> Optional[HrModelEntity73]:
        return self.db.query(HrModelEntity73).filter(HrModelEntity73.id == entity_id).first()

    def create_entity_73(self, payload: HrSchemaEntity73Create) -> HrModelEntity73:
        db_obj = HrModelEntity73(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_73(self, entity_id: int, payload: HrSchemaEntity73Update) -> Optional[HrModelEntity73]:
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

    def get_entity_74_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity74]:
        return self.db.query(HrModelEntity74).offset(skip).limit(limit).all()

    def get_entity_74_by_id(self, entity_id: int) -> Optional[HrModelEntity74]:
        return self.db.query(HrModelEntity74).filter(HrModelEntity74.id == entity_id).first()

    def create_entity_74(self, payload: HrSchemaEntity74Create) -> HrModelEntity74:
        db_obj = HrModelEntity74(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_74(self, entity_id: int, payload: HrSchemaEntity74Update) -> Optional[HrModelEntity74]:
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

    def get_entity_75_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity75]:
        return self.db.query(HrModelEntity75).offset(skip).limit(limit).all()

    def get_entity_75_by_id(self, entity_id: int) -> Optional[HrModelEntity75]:
        return self.db.query(HrModelEntity75).filter(HrModelEntity75.id == entity_id).first()

    def create_entity_75(self, payload: HrSchemaEntity75Create) -> HrModelEntity75:
        db_obj = HrModelEntity75(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_75(self, entity_id: int, payload: HrSchemaEntity75Update) -> Optional[HrModelEntity75]:
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

    def get_entity_76_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity76]:
        return self.db.query(HrModelEntity76).offset(skip).limit(limit).all()

    def get_entity_76_by_id(self, entity_id: int) -> Optional[HrModelEntity76]:
        return self.db.query(HrModelEntity76).filter(HrModelEntity76.id == entity_id).first()

    def create_entity_76(self, payload: HrSchemaEntity76Create) -> HrModelEntity76:
        db_obj = HrModelEntity76(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_76(self, entity_id: int, payload: HrSchemaEntity76Update) -> Optional[HrModelEntity76]:
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

    def get_entity_77_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity77]:
        return self.db.query(HrModelEntity77).offset(skip).limit(limit).all()

    def get_entity_77_by_id(self, entity_id: int) -> Optional[HrModelEntity77]:
        return self.db.query(HrModelEntity77).filter(HrModelEntity77.id == entity_id).first()

    def create_entity_77(self, payload: HrSchemaEntity77Create) -> HrModelEntity77:
        db_obj = HrModelEntity77(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_77(self, entity_id: int, payload: HrSchemaEntity77Update) -> Optional[HrModelEntity77]:
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

    def get_entity_78_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity78]:
        return self.db.query(HrModelEntity78).offset(skip).limit(limit).all()

    def get_entity_78_by_id(self, entity_id: int) -> Optional[HrModelEntity78]:
        return self.db.query(HrModelEntity78).filter(HrModelEntity78.id == entity_id).first()

    def create_entity_78(self, payload: HrSchemaEntity78Create) -> HrModelEntity78:
        db_obj = HrModelEntity78(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_78(self, entity_id: int, payload: HrSchemaEntity78Update) -> Optional[HrModelEntity78]:
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

    def get_entity_79_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity79]:
        return self.db.query(HrModelEntity79).offset(skip).limit(limit).all()

    def get_entity_79_by_id(self, entity_id: int) -> Optional[HrModelEntity79]:
        return self.db.query(HrModelEntity79).filter(HrModelEntity79.id == entity_id).first()

    def create_entity_79(self, payload: HrSchemaEntity79Create) -> HrModelEntity79:
        db_obj = HrModelEntity79(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_79(self, entity_id: int, payload: HrSchemaEntity79Update) -> Optional[HrModelEntity79]:
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

    def get_entity_80_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity80]:
        return self.db.query(HrModelEntity80).offset(skip).limit(limit).all()

    def get_entity_80_by_id(self, entity_id: int) -> Optional[HrModelEntity80]:
        return self.db.query(HrModelEntity80).filter(HrModelEntity80.id == entity_id).first()

    def create_entity_80(self, payload: HrSchemaEntity80Create) -> HrModelEntity80:
        db_obj = HrModelEntity80(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_80(self, entity_id: int, payload: HrSchemaEntity80Update) -> Optional[HrModelEntity80]:
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

    def get_entity_81_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity81]:
        return self.db.query(HrModelEntity81).offset(skip).limit(limit).all()

    def get_entity_81_by_id(self, entity_id: int) -> Optional[HrModelEntity81]:
        return self.db.query(HrModelEntity81).filter(HrModelEntity81.id == entity_id).first()

    def create_entity_81(self, payload: HrSchemaEntity81Create) -> HrModelEntity81:
        db_obj = HrModelEntity81(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_81(self, entity_id: int, payload: HrSchemaEntity81Update) -> Optional[HrModelEntity81]:
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

    def get_entity_82_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity82]:
        return self.db.query(HrModelEntity82).offset(skip).limit(limit).all()

    def get_entity_82_by_id(self, entity_id: int) -> Optional[HrModelEntity82]:
        return self.db.query(HrModelEntity82).filter(HrModelEntity82.id == entity_id).first()

    def create_entity_82(self, payload: HrSchemaEntity82Create) -> HrModelEntity82:
        db_obj = HrModelEntity82(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_82(self, entity_id: int, payload: HrSchemaEntity82Update) -> Optional[HrModelEntity82]:
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

    def get_entity_83_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity83]:
        return self.db.query(HrModelEntity83).offset(skip).limit(limit).all()

    def get_entity_83_by_id(self, entity_id: int) -> Optional[HrModelEntity83]:
        return self.db.query(HrModelEntity83).filter(HrModelEntity83.id == entity_id).first()

    def create_entity_83(self, payload: HrSchemaEntity83Create) -> HrModelEntity83:
        db_obj = HrModelEntity83(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_83(self, entity_id: int, payload: HrSchemaEntity83Update) -> Optional[HrModelEntity83]:
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

    def get_entity_84_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity84]:
        return self.db.query(HrModelEntity84).offset(skip).limit(limit).all()

    def get_entity_84_by_id(self, entity_id: int) -> Optional[HrModelEntity84]:
        return self.db.query(HrModelEntity84).filter(HrModelEntity84.id == entity_id).first()

    def create_entity_84(self, payload: HrSchemaEntity84Create) -> HrModelEntity84:
        db_obj = HrModelEntity84(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_84(self, entity_id: int, payload: HrSchemaEntity84Update) -> Optional[HrModelEntity84]:
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

    def get_entity_85_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity85]:
        return self.db.query(HrModelEntity85).offset(skip).limit(limit).all()

    def get_entity_85_by_id(self, entity_id: int) -> Optional[HrModelEntity85]:
        return self.db.query(HrModelEntity85).filter(HrModelEntity85.id == entity_id).first()

    def create_entity_85(self, payload: HrSchemaEntity85Create) -> HrModelEntity85:
        db_obj = HrModelEntity85(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_85(self, entity_id: int, payload: HrSchemaEntity85Update) -> Optional[HrModelEntity85]:
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

    def get_entity_86_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity86]:
        return self.db.query(HrModelEntity86).offset(skip).limit(limit).all()

    def get_entity_86_by_id(self, entity_id: int) -> Optional[HrModelEntity86]:
        return self.db.query(HrModelEntity86).filter(HrModelEntity86.id == entity_id).first()

    def create_entity_86(self, payload: HrSchemaEntity86Create) -> HrModelEntity86:
        db_obj = HrModelEntity86(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_86(self, entity_id: int, payload: HrSchemaEntity86Update) -> Optional[HrModelEntity86]:
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

    def get_entity_87_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity87]:
        return self.db.query(HrModelEntity87).offset(skip).limit(limit).all()

    def get_entity_87_by_id(self, entity_id: int) -> Optional[HrModelEntity87]:
        return self.db.query(HrModelEntity87).filter(HrModelEntity87.id == entity_id).first()

    def create_entity_87(self, payload: HrSchemaEntity87Create) -> HrModelEntity87:
        db_obj = HrModelEntity87(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_87(self, entity_id: int, payload: HrSchemaEntity87Update) -> Optional[HrModelEntity87]:
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

    def get_entity_88_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity88]:
        return self.db.query(HrModelEntity88).offset(skip).limit(limit).all()

    def get_entity_88_by_id(self, entity_id: int) -> Optional[HrModelEntity88]:
        return self.db.query(HrModelEntity88).filter(HrModelEntity88.id == entity_id).first()

    def create_entity_88(self, payload: HrSchemaEntity88Create) -> HrModelEntity88:
        db_obj = HrModelEntity88(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_88(self, entity_id: int, payload: HrSchemaEntity88Update) -> Optional[HrModelEntity88]:
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

    def get_entity_89_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity89]:
        return self.db.query(HrModelEntity89).offset(skip).limit(limit).all()

    def get_entity_89_by_id(self, entity_id: int) -> Optional[HrModelEntity89]:
        return self.db.query(HrModelEntity89).filter(HrModelEntity89.id == entity_id).first()

    def create_entity_89(self, payload: HrSchemaEntity89Create) -> HrModelEntity89:
        db_obj = HrModelEntity89(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_89(self, entity_id: int, payload: HrSchemaEntity89Update) -> Optional[HrModelEntity89]:
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

    def get_entity_90_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity90]:
        return self.db.query(HrModelEntity90).offset(skip).limit(limit).all()

    def get_entity_90_by_id(self, entity_id: int) -> Optional[HrModelEntity90]:
        return self.db.query(HrModelEntity90).filter(HrModelEntity90.id == entity_id).first()

    def create_entity_90(self, payload: HrSchemaEntity90Create) -> HrModelEntity90:
        db_obj = HrModelEntity90(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_90(self, entity_id: int, payload: HrSchemaEntity90Update) -> Optional[HrModelEntity90]:
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

    def get_entity_91_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity91]:
        return self.db.query(HrModelEntity91).offset(skip).limit(limit).all()

    def get_entity_91_by_id(self, entity_id: int) -> Optional[HrModelEntity91]:
        return self.db.query(HrModelEntity91).filter(HrModelEntity91.id == entity_id).first()

    def create_entity_91(self, payload: HrSchemaEntity91Create) -> HrModelEntity91:
        db_obj = HrModelEntity91(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_91(self, entity_id: int, payload: HrSchemaEntity91Update) -> Optional[HrModelEntity91]:
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

    def get_entity_92_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity92]:
        return self.db.query(HrModelEntity92).offset(skip).limit(limit).all()

    def get_entity_92_by_id(self, entity_id: int) -> Optional[HrModelEntity92]:
        return self.db.query(HrModelEntity92).filter(HrModelEntity92.id == entity_id).first()

    def create_entity_92(self, payload: HrSchemaEntity92Create) -> HrModelEntity92:
        db_obj = HrModelEntity92(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_92(self, entity_id: int, payload: HrSchemaEntity92Update) -> Optional[HrModelEntity92]:
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

    def get_entity_93_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity93]:
        return self.db.query(HrModelEntity93).offset(skip).limit(limit).all()

    def get_entity_93_by_id(self, entity_id: int) -> Optional[HrModelEntity93]:
        return self.db.query(HrModelEntity93).filter(HrModelEntity93.id == entity_id).first()

    def create_entity_93(self, payload: HrSchemaEntity93Create) -> HrModelEntity93:
        db_obj = HrModelEntity93(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_93(self, entity_id: int, payload: HrSchemaEntity93Update) -> Optional[HrModelEntity93]:
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

    def get_entity_94_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity94]:
        return self.db.query(HrModelEntity94).offset(skip).limit(limit).all()

    def get_entity_94_by_id(self, entity_id: int) -> Optional[HrModelEntity94]:
        return self.db.query(HrModelEntity94).filter(HrModelEntity94.id == entity_id).first()

    def create_entity_94(self, payload: HrSchemaEntity94Create) -> HrModelEntity94:
        db_obj = HrModelEntity94(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_94(self, entity_id: int, payload: HrSchemaEntity94Update) -> Optional[HrModelEntity94]:
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

    def get_entity_95_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity95]:
        return self.db.query(HrModelEntity95).offset(skip).limit(limit).all()

    def get_entity_95_by_id(self, entity_id: int) -> Optional[HrModelEntity95]:
        return self.db.query(HrModelEntity95).filter(HrModelEntity95.id == entity_id).first()

    def create_entity_95(self, payload: HrSchemaEntity95Create) -> HrModelEntity95:
        db_obj = HrModelEntity95(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_95(self, entity_id: int, payload: HrSchemaEntity95Update) -> Optional[HrModelEntity95]:
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

    def get_entity_96_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity96]:
        return self.db.query(HrModelEntity96).offset(skip).limit(limit).all()

    def get_entity_96_by_id(self, entity_id: int) -> Optional[HrModelEntity96]:
        return self.db.query(HrModelEntity96).filter(HrModelEntity96.id == entity_id).first()

    def create_entity_96(self, payload: HrSchemaEntity96Create) -> HrModelEntity96:
        db_obj = HrModelEntity96(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_96(self, entity_id: int, payload: HrSchemaEntity96Update) -> Optional[HrModelEntity96]:
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

    def get_entity_97_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity97]:
        return self.db.query(HrModelEntity97).offset(skip).limit(limit).all()

    def get_entity_97_by_id(self, entity_id: int) -> Optional[HrModelEntity97]:
        return self.db.query(HrModelEntity97).filter(HrModelEntity97.id == entity_id).first()

    def create_entity_97(self, payload: HrSchemaEntity97Create) -> HrModelEntity97:
        db_obj = HrModelEntity97(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_97(self, entity_id: int, payload: HrSchemaEntity97Update) -> Optional[HrModelEntity97]:
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

    def get_entity_98_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity98]:
        return self.db.query(HrModelEntity98).offset(skip).limit(limit).all()

    def get_entity_98_by_id(self, entity_id: int) -> Optional[HrModelEntity98]:
        return self.db.query(HrModelEntity98).filter(HrModelEntity98.id == entity_id).first()

    def create_entity_98(self, payload: HrSchemaEntity98Create) -> HrModelEntity98:
        db_obj = HrModelEntity98(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_98(self, entity_id: int, payload: HrSchemaEntity98Update) -> Optional[HrModelEntity98]:
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

    def get_entity_99_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity99]:
        return self.db.query(HrModelEntity99).offset(skip).limit(limit).all()

    def get_entity_99_by_id(self, entity_id: int) -> Optional[HrModelEntity99]:
        return self.db.query(HrModelEntity99).filter(HrModelEntity99.id == entity_id).first()

    def create_entity_99(self, payload: HrSchemaEntity99Create) -> HrModelEntity99:
        db_obj = HrModelEntity99(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_99(self, entity_id: int, payload: HrSchemaEntity99Update) -> Optional[HrModelEntity99]:
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

    def get_entity_100_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity100]:
        return self.db.query(HrModelEntity100).offset(skip).limit(limit).all()

    def get_entity_100_by_id(self, entity_id: int) -> Optional[HrModelEntity100]:
        return self.db.query(HrModelEntity100).filter(HrModelEntity100.id == entity_id).first()

    def create_entity_100(self, payload: HrSchemaEntity100Create) -> HrModelEntity100:
        db_obj = HrModelEntity100(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_100(self, entity_id: int, payload: HrSchemaEntity100Update) -> Optional[HrModelEntity100]:
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

    def get_entity_101_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity101]:
        return self.db.query(HrModelEntity101).offset(skip).limit(limit).all()

    def get_entity_101_by_id(self, entity_id: int) -> Optional[HrModelEntity101]:
        return self.db.query(HrModelEntity101).filter(HrModelEntity101.id == entity_id).first()

    def create_entity_101(self, payload: HrSchemaEntity101Create) -> HrModelEntity101:
        db_obj = HrModelEntity101(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_101(self, entity_id: int, payload: HrSchemaEntity101Update) -> Optional[HrModelEntity101]:
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

    def get_entity_102_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity102]:
        return self.db.query(HrModelEntity102).offset(skip).limit(limit).all()

    def get_entity_102_by_id(self, entity_id: int) -> Optional[HrModelEntity102]:
        return self.db.query(HrModelEntity102).filter(HrModelEntity102.id == entity_id).first()

    def create_entity_102(self, payload: HrSchemaEntity102Create) -> HrModelEntity102:
        db_obj = HrModelEntity102(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_102(self, entity_id: int, payload: HrSchemaEntity102Update) -> Optional[HrModelEntity102]:
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

    def get_entity_103_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity103]:
        return self.db.query(HrModelEntity103).offset(skip).limit(limit).all()

    def get_entity_103_by_id(self, entity_id: int) -> Optional[HrModelEntity103]:
        return self.db.query(HrModelEntity103).filter(HrModelEntity103.id == entity_id).first()

    def create_entity_103(self, payload: HrSchemaEntity103Create) -> HrModelEntity103:
        db_obj = HrModelEntity103(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_103(self, entity_id: int, payload: HrSchemaEntity103Update) -> Optional[HrModelEntity103]:
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

    def get_entity_104_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity104]:
        return self.db.query(HrModelEntity104).offset(skip).limit(limit).all()

    def get_entity_104_by_id(self, entity_id: int) -> Optional[HrModelEntity104]:
        return self.db.query(HrModelEntity104).filter(HrModelEntity104.id == entity_id).first()

    def create_entity_104(self, payload: HrSchemaEntity104Create) -> HrModelEntity104:
        db_obj = HrModelEntity104(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_104(self, entity_id: int, payload: HrSchemaEntity104Update) -> Optional[HrModelEntity104]:
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

    def get_entity_105_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity105]:
        return self.db.query(HrModelEntity105).offset(skip).limit(limit).all()

    def get_entity_105_by_id(self, entity_id: int) -> Optional[HrModelEntity105]:
        return self.db.query(HrModelEntity105).filter(HrModelEntity105.id == entity_id).first()

    def create_entity_105(self, payload: HrSchemaEntity105Create) -> HrModelEntity105:
        db_obj = HrModelEntity105(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_105(self, entity_id: int, payload: HrSchemaEntity105Update) -> Optional[HrModelEntity105]:
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

    def get_entity_106_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity106]:
        return self.db.query(HrModelEntity106).offset(skip).limit(limit).all()

    def get_entity_106_by_id(self, entity_id: int) -> Optional[HrModelEntity106]:
        return self.db.query(HrModelEntity106).filter(HrModelEntity106.id == entity_id).first()

    def create_entity_106(self, payload: HrSchemaEntity106Create) -> HrModelEntity106:
        db_obj = HrModelEntity106(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_106(self, entity_id: int, payload: HrSchemaEntity106Update) -> Optional[HrModelEntity106]:
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

    def get_entity_107_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity107]:
        return self.db.query(HrModelEntity107).offset(skip).limit(limit).all()

    def get_entity_107_by_id(self, entity_id: int) -> Optional[HrModelEntity107]:
        return self.db.query(HrModelEntity107).filter(HrModelEntity107.id == entity_id).first()

    def create_entity_107(self, payload: HrSchemaEntity107Create) -> HrModelEntity107:
        db_obj = HrModelEntity107(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_107(self, entity_id: int, payload: HrSchemaEntity107Update) -> Optional[HrModelEntity107]:
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

    def get_entity_108_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity108]:
        return self.db.query(HrModelEntity108).offset(skip).limit(limit).all()

    def get_entity_108_by_id(self, entity_id: int) -> Optional[HrModelEntity108]:
        return self.db.query(HrModelEntity108).filter(HrModelEntity108.id == entity_id).first()

    def create_entity_108(self, payload: HrSchemaEntity108Create) -> HrModelEntity108:
        db_obj = HrModelEntity108(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_108(self, entity_id: int, payload: HrSchemaEntity108Update) -> Optional[HrModelEntity108]:
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

    def get_entity_109_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity109]:
        return self.db.query(HrModelEntity109).offset(skip).limit(limit).all()

    def get_entity_109_by_id(self, entity_id: int) -> Optional[HrModelEntity109]:
        return self.db.query(HrModelEntity109).filter(HrModelEntity109.id == entity_id).first()

    def create_entity_109(self, payload: HrSchemaEntity109Create) -> HrModelEntity109:
        db_obj = HrModelEntity109(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_109(self, entity_id: int, payload: HrSchemaEntity109Update) -> Optional[HrModelEntity109]:
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

    def get_entity_110_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity110]:
        return self.db.query(HrModelEntity110).offset(skip).limit(limit).all()

    def get_entity_110_by_id(self, entity_id: int) -> Optional[HrModelEntity110]:
        return self.db.query(HrModelEntity110).filter(HrModelEntity110.id == entity_id).first()

    def create_entity_110(self, payload: HrSchemaEntity110Create) -> HrModelEntity110:
        db_obj = HrModelEntity110(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_110(self, entity_id: int, payload: HrSchemaEntity110Update) -> Optional[HrModelEntity110]:
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

    def get_entity_111_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity111]:
        return self.db.query(HrModelEntity111).offset(skip).limit(limit).all()

    def get_entity_111_by_id(self, entity_id: int) -> Optional[HrModelEntity111]:
        return self.db.query(HrModelEntity111).filter(HrModelEntity111.id == entity_id).first()

    def create_entity_111(self, payload: HrSchemaEntity111Create) -> HrModelEntity111:
        db_obj = HrModelEntity111(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_111(self, entity_id: int, payload: HrSchemaEntity111Update) -> Optional[HrModelEntity111]:
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

    def get_entity_112_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity112]:
        return self.db.query(HrModelEntity112).offset(skip).limit(limit).all()

    def get_entity_112_by_id(self, entity_id: int) -> Optional[HrModelEntity112]:
        return self.db.query(HrModelEntity112).filter(HrModelEntity112.id == entity_id).first()

    def create_entity_112(self, payload: HrSchemaEntity112Create) -> HrModelEntity112:
        db_obj = HrModelEntity112(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_112(self, entity_id: int, payload: HrSchemaEntity112Update) -> Optional[HrModelEntity112]:
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

    def get_entity_113_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity113]:
        return self.db.query(HrModelEntity113).offset(skip).limit(limit).all()

    def get_entity_113_by_id(self, entity_id: int) -> Optional[HrModelEntity113]:
        return self.db.query(HrModelEntity113).filter(HrModelEntity113.id == entity_id).first()

    def create_entity_113(self, payload: HrSchemaEntity113Create) -> HrModelEntity113:
        db_obj = HrModelEntity113(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_113(self, entity_id: int, payload: HrSchemaEntity113Update) -> Optional[HrModelEntity113]:
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

    def get_entity_114_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity114]:
        return self.db.query(HrModelEntity114).offset(skip).limit(limit).all()

    def get_entity_114_by_id(self, entity_id: int) -> Optional[HrModelEntity114]:
        return self.db.query(HrModelEntity114).filter(HrModelEntity114.id == entity_id).first()

    def create_entity_114(self, payload: HrSchemaEntity114Create) -> HrModelEntity114:
        db_obj = HrModelEntity114(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_114(self, entity_id: int, payload: HrSchemaEntity114Update) -> Optional[HrModelEntity114]:
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

    def get_entity_115_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity115]:
        return self.db.query(HrModelEntity115).offset(skip).limit(limit).all()

    def get_entity_115_by_id(self, entity_id: int) -> Optional[HrModelEntity115]:
        return self.db.query(HrModelEntity115).filter(HrModelEntity115.id == entity_id).first()

    def create_entity_115(self, payload: HrSchemaEntity115Create) -> HrModelEntity115:
        db_obj = HrModelEntity115(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_115(self, entity_id: int, payload: HrSchemaEntity115Update) -> Optional[HrModelEntity115]:
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

    def get_entity_116_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity116]:
        return self.db.query(HrModelEntity116).offset(skip).limit(limit).all()

    def get_entity_116_by_id(self, entity_id: int) -> Optional[HrModelEntity116]:
        return self.db.query(HrModelEntity116).filter(HrModelEntity116.id == entity_id).first()

    def create_entity_116(self, payload: HrSchemaEntity116Create) -> HrModelEntity116:
        db_obj = HrModelEntity116(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_116(self, entity_id: int, payload: HrSchemaEntity116Update) -> Optional[HrModelEntity116]:
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

    def get_entity_117_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity117]:
        return self.db.query(HrModelEntity117).offset(skip).limit(limit).all()

    def get_entity_117_by_id(self, entity_id: int) -> Optional[HrModelEntity117]:
        return self.db.query(HrModelEntity117).filter(HrModelEntity117.id == entity_id).first()

    def create_entity_117(self, payload: HrSchemaEntity117Create) -> HrModelEntity117:
        db_obj = HrModelEntity117(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_117(self, entity_id: int, payload: HrSchemaEntity117Update) -> Optional[HrModelEntity117]:
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

    def get_entity_118_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity118]:
        return self.db.query(HrModelEntity118).offset(skip).limit(limit).all()

    def get_entity_118_by_id(self, entity_id: int) -> Optional[HrModelEntity118]:
        return self.db.query(HrModelEntity118).filter(HrModelEntity118.id == entity_id).first()

    def create_entity_118(self, payload: HrSchemaEntity118Create) -> HrModelEntity118:
        db_obj = HrModelEntity118(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_118(self, entity_id: int, payload: HrSchemaEntity118Update) -> Optional[HrModelEntity118]:
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

    def get_entity_119_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity119]:
        return self.db.query(HrModelEntity119).offset(skip).limit(limit).all()

    def get_entity_119_by_id(self, entity_id: int) -> Optional[HrModelEntity119]:
        return self.db.query(HrModelEntity119).filter(HrModelEntity119.id == entity_id).first()

    def create_entity_119(self, payload: HrSchemaEntity119Create) -> HrModelEntity119:
        db_obj = HrModelEntity119(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_119(self, entity_id: int, payload: HrSchemaEntity119Update) -> Optional[HrModelEntity119]:
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

    def get_entity_120_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity120]:
        return self.db.query(HrModelEntity120).offset(skip).limit(limit).all()

    def get_entity_120_by_id(self, entity_id: int) -> Optional[HrModelEntity120]:
        return self.db.query(HrModelEntity120).filter(HrModelEntity120.id == entity_id).first()

    def create_entity_120(self, payload: HrSchemaEntity120Create) -> HrModelEntity120:
        db_obj = HrModelEntity120(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_120(self, entity_id: int, payload: HrSchemaEntity120Update) -> Optional[HrModelEntity120]:
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

    def get_entity_121_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity121]:
        return self.db.query(HrModelEntity121).offset(skip).limit(limit).all()

    def get_entity_121_by_id(self, entity_id: int) -> Optional[HrModelEntity121]:
        return self.db.query(HrModelEntity121).filter(HrModelEntity121.id == entity_id).first()

    def create_entity_121(self, payload: HrSchemaEntity121Create) -> HrModelEntity121:
        db_obj = HrModelEntity121(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_121(self, entity_id: int, payload: HrSchemaEntity121Update) -> Optional[HrModelEntity121]:
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

    def get_entity_122_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity122]:
        return self.db.query(HrModelEntity122).offset(skip).limit(limit).all()

    def get_entity_122_by_id(self, entity_id: int) -> Optional[HrModelEntity122]:
        return self.db.query(HrModelEntity122).filter(HrModelEntity122.id == entity_id).first()

    def create_entity_122(self, payload: HrSchemaEntity122Create) -> HrModelEntity122:
        db_obj = HrModelEntity122(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_122(self, entity_id: int, payload: HrSchemaEntity122Update) -> Optional[HrModelEntity122]:
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

    def get_entity_123_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity123]:
        return self.db.query(HrModelEntity123).offset(skip).limit(limit).all()

    def get_entity_123_by_id(self, entity_id: int) -> Optional[HrModelEntity123]:
        return self.db.query(HrModelEntity123).filter(HrModelEntity123.id == entity_id).first()

    def create_entity_123(self, payload: HrSchemaEntity123Create) -> HrModelEntity123:
        db_obj = HrModelEntity123(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_123(self, entity_id: int, payload: HrSchemaEntity123Update) -> Optional[HrModelEntity123]:
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

    def get_entity_124_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity124]:
        return self.db.query(HrModelEntity124).offset(skip).limit(limit).all()

    def get_entity_124_by_id(self, entity_id: int) -> Optional[HrModelEntity124]:
        return self.db.query(HrModelEntity124).filter(HrModelEntity124.id == entity_id).first()

    def create_entity_124(self, payload: HrSchemaEntity124Create) -> HrModelEntity124:
        db_obj = HrModelEntity124(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_124(self, entity_id: int, payload: HrSchemaEntity124Update) -> Optional[HrModelEntity124]:
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

    def get_entity_125_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity125]:
        return self.db.query(HrModelEntity125).offset(skip).limit(limit).all()

    def get_entity_125_by_id(self, entity_id: int) -> Optional[HrModelEntity125]:
        return self.db.query(HrModelEntity125).filter(HrModelEntity125.id == entity_id).first()

    def create_entity_125(self, payload: HrSchemaEntity125Create) -> HrModelEntity125:
        db_obj = HrModelEntity125(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_125(self, entity_id: int, payload: HrSchemaEntity125Update) -> Optional[HrModelEntity125]:
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

    def get_entity_126_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity126]:
        return self.db.query(HrModelEntity126).offset(skip).limit(limit).all()

    def get_entity_126_by_id(self, entity_id: int) -> Optional[HrModelEntity126]:
        return self.db.query(HrModelEntity126).filter(HrModelEntity126.id == entity_id).first()

    def create_entity_126(self, payload: HrSchemaEntity126Create) -> HrModelEntity126:
        db_obj = HrModelEntity126(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_126(self, entity_id: int, payload: HrSchemaEntity126Update) -> Optional[HrModelEntity126]:
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

    def get_entity_127_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity127]:
        return self.db.query(HrModelEntity127).offset(skip).limit(limit).all()

    def get_entity_127_by_id(self, entity_id: int) -> Optional[HrModelEntity127]:
        return self.db.query(HrModelEntity127).filter(HrModelEntity127.id == entity_id).first()

    def create_entity_127(self, payload: HrSchemaEntity127Create) -> HrModelEntity127:
        db_obj = HrModelEntity127(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_127(self, entity_id: int, payload: HrSchemaEntity127Update) -> Optional[HrModelEntity127]:
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

    def get_entity_128_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity128]:
        return self.db.query(HrModelEntity128).offset(skip).limit(limit).all()

    def get_entity_128_by_id(self, entity_id: int) -> Optional[HrModelEntity128]:
        return self.db.query(HrModelEntity128).filter(HrModelEntity128.id == entity_id).first()

    def create_entity_128(self, payload: HrSchemaEntity128Create) -> HrModelEntity128:
        db_obj = HrModelEntity128(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_128(self, entity_id: int, payload: HrSchemaEntity128Update) -> Optional[HrModelEntity128]:
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

    def get_entity_129_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity129]:
        return self.db.query(HrModelEntity129).offset(skip).limit(limit).all()

    def get_entity_129_by_id(self, entity_id: int) -> Optional[HrModelEntity129]:
        return self.db.query(HrModelEntity129).filter(HrModelEntity129.id == entity_id).first()

    def create_entity_129(self, payload: HrSchemaEntity129Create) -> HrModelEntity129:
        db_obj = HrModelEntity129(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_129(self, entity_id: int, payload: HrSchemaEntity129Update) -> Optional[HrModelEntity129]:
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

    def get_entity_130_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity130]:
        return self.db.query(HrModelEntity130).offset(skip).limit(limit).all()

    def get_entity_130_by_id(self, entity_id: int) -> Optional[HrModelEntity130]:
        return self.db.query(HrModelEntity130).filter(HrModelEntity130.id == entity_id).first()

    def create_entity_130(self, payload: HrSchemaEntity130Create) -> HrModelEntity130:
        db_obj = HrModelEntity130(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_130(self, entity_id: int, payload: HrSchemaEntity130Update) -> Optional[HrModelEntity130]:
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

    def get_entity_131_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity131]:
        return self.db.query(HrModelEntity131).offset(skip).limit(limit).all()

    def get_entity_131_by_id(self, entity_id: int) -> Optional[HrModelEntity131]:
        return self.db.query(HrModelEntity131).filter(HrModelEntity131.id == entity_id).first()

    def create_entity_131(self, payload: HrSchemaEntity131Create) -> HrModelEntity131:
        db_obj = HrModelEntity131(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_131(self, entity_id: int, payload: HrSchemaEntity131Update) -> Optional[HrModelEntity131]:
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

    def get_entity_132_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity132]:
        return self.db.query(HrModelEntity132).offset(skip).limit(limit).all()

    def get_entity_132_by_id(self, entity_id: int) -> Optional[HrModelEntity132]:
        return self.db.query(HrModelEntity132).filter(HrModelEntity132.id == entity_id).first()

    def create_entity_132(self, payload: HrSchemaEntity132Create) -> HrModelEntity132:
        db_obj = HrModelEntity132(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_132(self, entity_id: int, payload: HrSchemaEntity132Update) -> Optional[HrModelEntity132]:
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

    def get_entity_133_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity133]:
        return self.db.query(HrModelEntity133).offset(skip).limit(limit).all()

    def get_entity_133_by_id(self, entity_id: int) -> Optional[HrModelEntity133]:
        return self.db.query(HrModelEntity133).filter(HrModelEntity133.id == entity_id).first()

    def create_entity_133(self, payload: HrSchemaEntity133Create) -> HrModelEntity133:
        db_obj = HrModelEntity133(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_133(self, entity_id: int, payload: HrSchemaEntity133Update) -> Optional[HrModelEntity133]:
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

    def get_entity_134_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity134]:
        return self.db.query(HrModelEntity134).offset(skip).limit(limit).all()

    def get_entity_134_by_id(self, entity_id: int) -> Optional[HrModelEntity134]:
        return self.db.query(HrModelEntity134).filter(HrModelEntity134.id == entity_id).first()

    def create_entity_134(self, payload: HrSchemaEntity134Create) -> HrModelEntity134:
        db_obj = HrModelEntity134(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_134(self, entity_id: int, payload: HrSchemaEntity134Update) -> Optional[HrModelEntity134]:
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

    def get_entity_135_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity135]:
        return self.db.query(HrModelEntity135).offset(skip).limit(limit).all()

    def get_entity_135_by_id(self, entity_id: int) -> Optional[HrModelEntity135]:
        return self.db.query(HrModelEntity135).filter(HrModelEntity135.id == entity_id).first()

    def create_entity_135(self, payload: HrSchemaEntity135Create) -> HrModelEntity135:
        db_obj = HrModelEntity135(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_135(self, entity_id: int, payload: HrSchemaEntity135Update) -> Optional[HrModelEntity135]:
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

    def get_entity_136_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity136]:
        return self.db.query(HrModelEntity136).offset(skip).limit(limit).all()

    def get_entity_136_by_id(self, entity_id: int) -> Optional[HrModelEntity136]:
        return self.db.query(HrModelEntity136).filter(HrModelEntity136.id == entity_id).first()

    def create_entity_136(self, payload: HrSchemaEntity136Create) -> HrModelEntity136:
        db_obj = HrModelEntity136(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_136(self, entity_id: int, payload: HrSchemaEntity136Update) -> Optional[HrModelEntity136]:
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

    def get_entity_137_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity137]:
        return self.db.query(HrModelEntity137).offset(skip).limit(limit).all()

    def get_entity_137_by_id(self, entity_id: int) -> Optional[HrModelEntity137]:
        return self.db.query(HrModelEntity137).filter(HrModelEntity137.id == entity_id).first()

    def create_entity_137(self, payload: HrSchemaEntity137Create) -> HrModelEntity137:
        db_obj = HrModelEntity137(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_137(self, entity_id: int, payload: HrSchemaEntity137Update) -> Optional[HrModelEntity137]:
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

    def get_entity_138_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity138]:
        return self.db.query(HrModelEntity138).offset(skip).limit(limit).all()

    def get_entity_138_by_id(self, entity_id: int) -> Optional[HrModelEntity138]:
        return self.db.query(HrModelEntity138).filter(HrModelEntity138.id == entity_id).first()

    def create_entity_138(self, payload: HrSchemaEntity138Create) -> HrModelEntity138:
        db_obj = HrModelEntity138(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_138(self, entity_id: int, payload: HrSchemaEntity138Update) -> Optional[HrModelEntity138]:
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

    def get_entity_139_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity139]:
        return self.db.query(HrModelEntity139).offset(skip).limit(limit).all()

    def get_entity_139_by_id(self, entity_id: int) -> Optional[HrModelEntity139]:
        return self.db.query(HrModelEntity139).filter(HrModelEntity139.id == entity_id).first()

    def create_entity_139(self, payload: HrSchemaEntity139Create) -> HrModelEntity139:
        db_obj = HrModelEntity139(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_139(self, entity_id: int, payload: HrSchemaEntity139Update) -> Optional[HrModelEntity139]:
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

    def get_entity_140_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity140]:
        return self.db.query(HrModelEntity140).offset(skip).limit(limit).all()

    def get_entity_140_by_id(self, entity_id: int) -> Optional[HrModelEntity140]:
        return self.db.query(HrModelEntity140).filter(HrModelEntity140.id == entity_id).first()

    def create_entity_140(self, payload: HrSchemaEntity140Create) -> HrModelEntity140:
        db_obj = HrModelEntity140(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_140(self, entity_id: int, payload: HrSchemaEntity140Update) -> Optional[HrModelEntity140]:
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

    def get_entity_141_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity141]:
        return self.db.query(HrModelEntity141).offset(skip).limit(limit).all()

    def get_entity_141_by_id(self, entity_id: int) -> Optional[HrModelEntity141]:
        return self.db.query(HrModelEntity141).filter(HrModelEntity141.id == entity_id).first()

    def create_entity_141(self, payload: HrSchemaEntity141Create) -> HrModelEntity141:
        db_obj = HrModelEntity141(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_141(self, entity_id: int, payload: HrSchemaEntity141Update) -> Optional[HrModelEntity141]:
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

    def get_entity_142_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity142]:
        return self.db.query(HrModelEntity142).offset(skip).limit(limit).all()

    def get_entity_142_by_id(self, entity_id: int) -> Optional[HrModelEntity142]:
        return self.db.query(HrModelEntity142).filter(HrModelEntity142.id == entity_id).first()

    def create_entity_142(self, payload: HrSchemaEntity142Create) -> HrModelEntity142:
        db_obj = HrModelEntity142(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_142(self, entity_id: int, payload: HrSchemaEntity142Update) -> Optional[HrModelEntity142]:
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

    def get_entity_143_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity143]:
        return self.db.query(HrModelEntity143).offset(skip).limit(limit).all()

    def get_entity_143_by_id(self, entity_id: int) -> Optional[HrModelEntity143]:
        return self.db.query(HrModelEntity143).filter(HrModelEntity143.id == entity_id).first()

    def create_entity_143(self, payload: HrSchemaEntity143Create) -> HrModelEntity143:
        db_obj = HrModelEntity143(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_143(self, entity_id: int, payload: HrSchemaEntity143Update) -> Optional[HrModelEntity143]:
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

    def get_entity_144_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity144]:
        return self.db.query(HrModelEntity144).offset(skip).limit(limit).all()

    def get_entity_144_by_id(self, entity_id: int) -> Optional[HrModelEntity144]:
        return self.db.query(HrModelEntity144).filter(HrModelEntity144.id == entity_id).first()

    def create_entity_144(self, payload: HrSchemaEntity144Create) -> HrModelEntity144:
        db_obj = HrModelEntity144(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_144(self, entity_id: int, payload: HrSchemaEntity144Update) -> Optional[HrModelEntity144]:
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

    def get_entity_145_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity145]:
        return self.db.query(HrModelEntity145).offset(skip).limit(limit).all()

    def get_entity_145_by_id(self, entity_id: int) -> Optional[HrModelEntity145]:
        return self.db.query(HrModelEntity145).filter(HrModelEntity145.id == entity_id).first()

    def create_entity_145(self, payload: HrSchemaEntity145Create) -> HrModelEntity145:
        db_obj = HrModelEntity145(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_145(self, entity_id: int, payload: HrSchemaEntity145Update) -> Optional[HrModelEntity145]:
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

    def get_entity_146_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity146]:
        return self.db.query(HrModelEntity146).offset(skip).limit(limit).all()

    def get_entity_146_by_id(self, entity_id: int) -> Optional[HrModelEntity146]:
        return self.db.query(HrModelEntity146).filter(HrModelEntity146.id == entity_id).first()

    def create_entity_146(self, payload: HrSchemaEntity146Create) -> HrModelEntity146:
        db_obj = HrModelEntity146(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_146(self, entity_id: int, payload: HrSchemaEntity146Update) -> Optional[HrModelEntity146]:
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

    def get_entity_147_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity147]:
        return self.db.query(HrModelEntity147).offset(skip).limit(limit).all()

    def get_entity_147_by_id(self, entity_id: int) -> Optional[HrModelEntity147]:
        return self.db.query(HrModelEntity147).filter(HrModelEntity147.id == entity_id).first()

    def create_entity_147(self, payload: HrSchemaEntity147Create) -> HrModelEntity147:
        db_obj = HrModelEntity147(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_147(self, entity_id: int, payload: HrSchemaEntity147Update) -> Optional[HrModelEntity147]:
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

    def get_entity_148_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity148]:
        return self.db.query(HrModelEntity148).offset(skip).limit(limit).all()

    def get_entity_148_by_id(self, entity_id: int) -> Optional[HrModelEntity148]:
        return self.db.query(HrModelEntity148).filter(HrModelEntity148.id == entity_id).first()

    def create_entity_148(self, payload: HrSchemaEntity148Create) -> HrModelEntity148:
        db_obj = HrModelEntity148(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_148(self, entity_id: int, payload: HrSchemaEntity148Update) -> Optional[HrModelEntity148]:
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

    def get_entity_149_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity149]:
        return self.db.query(HrModelEntity149).offset(skip).limit(limit).all()

    def get_entity_149_by_id(self, entity_id: int) -> Optional[HrModelEntity149]:
        return self.db.query(HrModelEntity149).filter(HrModelEntity149.id == entity_id).first()

    def create_entity_149(self, payload: HrSchemaEntity149Create) -> HrModelEntity149:
        db_obj = HrModelEntity149(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_149(self, entity_id: int, payload: HrSchemaEntity149Update) -> Optional[HrModelEntity149]:
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

    def get_entity_150_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity150]:
        return self.db.query(HrModelEntity150).offset(skip).limit(limit).all()

    def get_entity_150_by_id(self, entity_id: int) -> Optional[HrModelEntity150]:
        return self.db.query(HrModelEntity150).filter(HrModelEntity150.id == entity_id).first()

    def create_entity_150(self, payload: HrSchemaEntity150Create) -> HrModelEntity150:
        db_obj = HrModelEntity150(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_150(self, entity_id: int, payload: HrSchemaEntity150Update) -> Optional[HrModelEntity150]:
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

    def get_entity_151_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity151]:
        return self.db.query(HrModelEntity151).offset(skip).limit(limit).all()

    def get_entity_151_by_id(self, entity_id: int) -> Optional[HrModelEntity151]:
        return self.db.query(HrModelEntity151).filter(HrModelEntity151.id == entity_id).first()

    def create_entity_151(self, payload: HrSchemaEntity151Create) -> HrModelEntity151:
        db_obj = HrModelEntity151(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_151(self, entity_id: int, payload: HrSchemaEntity151Update) -> Optional[HrModelEntity151]:
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

    def get_entity_152_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity152]:
        return self.db.query(HrModelEntity152).offset(skip).limit(limit).all()

    def get_entity_152_by_id(self, entity_id: int) -> Optional[HrModelEntity152]:
        return self.db.query(HrModelEntity152).filter(HrModelEntity152.id == entity_id).first()

    def create_entity_152(self, payload: HrSchemaEntity152Create) -> HrModelEntity152:
        db_obj = HrModelEntity152(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_152(self, entity_id: int, payload: HrSchemaEntity152Update) -> Optional[HrModelEntity152]:
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

    def get_entity_153_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity153]:
        return self.db.query(HrModelEntity153).offset(skip).limit(limit).all()

    def get_entity_153_by_id(self, entity_id: int) -> Optional[HrModelEntity153]:
        return self.db.query(HrModelEntity153).filter(HrModelEntity153.id == entity_id).first()

    def create_entity_153(self, payload: HrSchemaEntity153Create) -> HrModelEntity153:
        db_obj = HrModelEntity153(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_153(self, entity_id: int, payload: HrSchemaEntity153Update) -> Optional[HrModelEntity153]:
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

    def get_entity_154_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity154]:
        return self.db.query(HrModelEntity154).offset(skip).limit(limit).all()

    def get_entity_154_by_id(self, entity_id: int) -> Optional[HrModelEntity154]:
        return self.db.query(HrModelEntity154).filter(HrModelEntity154.id == entity_id).first()

    def create_entity_154(self, payload: HrSchemaEntity154Create) -> HrModelEntity154:
        db_obj = HrModelEntity154(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_154(self, entity_id: int, payload: HrSchemaEntity154Update) -> Optional[HrModelEntity154]:
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

    def get_entity_155_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity155]:
        return self.db.query(HrModelEntity155).offset(skip).limit(limit).all()

    def get_entity_155_by_id(self, entity_id: int) -> Optional[HrModelEntity155]:
        return self.db.query(HrModelEntity155).filter(HrModelEntity155.id == entity_id).first()

    def create_entity_155(self, payload: HrSchemaEntity155Create) -> HrModelEntity155:
        db_obj = HrModelEntity155(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_155(self, entity_id: int, payload: HrSchemaEntity155Update) -> Optional[HrModelEntity155]:
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

    def get_entity_156_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity156]:
        return self.db.query(HrModelEntity156).offset(skip).limit(limit).all()

    def get_entity_156_by_id(self, entity_id: int) -> Optional[HrModelEntity156]:
        return self.db.query(HrModelEntity156).filter(HrModelEntity156.id == entity_id).first()

    def create_entity_156(self, payload: HrSchemaEntity156Create) -> HrModelEntity156:
        db_obj = HrModelEntity156(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_156(self, entity_id: int, payload: HrSchemaEntity156Update) -> Optional[HrModelEntity156]:
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

    def get_entity_157_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity157]:
        return self.db.query(HrModelEntity157).offset(skip).limit(limit).all()

    def get_entity_157_by_id(self, entity_id: int) -> Optional[HrModelEntity157]:
        return self.db.query(HrModelEntity157).filter(HrModelEntity157.id == entity_id).first()

    def create_entity_157(self, payload: HrSchemaEntity157Create) -> HrModelEntity157:
        db_obj = HrModelEntity157(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_157(self, entity_id: int, payload: HrSchemaEntity157Update) -> Optional[HrModelEntity157]:
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

    def get_entity_158_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity158]:
        return self.db.query(HrModelEntity158).offset(skip).limit(limit).all()

    def get_entity_158_by_id(self, entity_id: int) -> Optional[HrModelEntity158]:
        return self.db.query(HrModelEntity158).filter(HrModelEntity158.id == entity_id).first()

    def create_entity_158(self, payload: HrSchemaEntity158Create) -> HrModelEntity158:
        db_obj = HrModelEntity158(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_158(self, entity_id: int, payload: HrSchemaEntity158Update) -> Optional[HrModelEntity158]:
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

    def get_entity_159_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity159]:
        return self.db.query(HrModelEntity159).offset(skip).limit(limit).all()

    def get_entity_159_by_id(self, entity_id: int) -> Optional[HrModelEntity159]:
        return self.db.query(HrModelEntity159).filter(HrModelEntity159.id == entity_id).first()

    def create_entity_159(self, payload: HrSchemaEntity159Create) -> HrModelEntity159:
        db_obj = HrModelEntity159(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_159(self, entity_id: int, payload: HrSchemaEntity159Update) -> Optional[HrModelEntity159]:
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

    def get_entity_160_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity160]:
        return self.db.query(HrModelEntity160).offset(skip).limit(limit).all()

    def get_entity_160_by_id(self, entity_id: int) -> Optional[HrModelEntity160]:
        return self.db.query(HrModelEntity160).filter(HrModelEntity160.id == entity_id).first()

    def create_entity_160(self, payload: HrSchemaEntity160Create) -> HrModelEntity160:
        db_obj = HrModelEntity160(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_160(self, entity_id: int, payload: HrSchemaEntity160Update) -> Optional[HrModelEntity160]:
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

    def get_entity_161_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity161]:
        return self.db.query(HrModelEntity161).offset(skip).limit(limit).all()

    def get_entity_161_by_id(self, entity_id: int) -> Optional[HrModelEntity161]:
        return self.db.query(HrModelEntity161).filter(HrModelEntity161.id == entity_id).first()

    def create_entity_161(self, payload: HrSchemaEntity161Create) -> HrModelEntity161:
        db_obj = HrModelEntity161(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_161(self, entity_id: int, payload: HrSchemaEntity161Update) -> Optional[HrModelEntity161]:
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

    def get_entity_162_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity162]:
        return self.db.query(HrModelEntity162).offset(skip).limit(limit).all()

    def get_entity_162_by_id(self, entity_id: int) -> Optional[HrModelEntity162]:
        return self.db.query(HrModelEntity162).filter(HrModelEntity162.id == entity_id).first()

    def create_entity_162(self, payload: HrSchemaEntity162Create) -> HrModelEntity162:
        db_obj = HrModelEntity162(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_162(self, entity_id: int, payload: HrSchemaEntity162Update) -> Optional[HrModelEntity162]:
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

    def get_entity_163_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity163]:
        return self.db.query(HrModelEntity163).offset(skip).limit(limit).all()

    def get_entity_163_by_id(self, entity_id: int) -> Optional[HrModelEntity163]:
        return self.db.query(HrModelEntity163).filter(HrModelEntity163.id == entity_id).first()

    def create_entity_163(self, payload: HrSchemaEntity163Create) -> HrModelEntity163:
        db_obj = HrModelEntity163(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_163(self, entity_id: int, payload: HrSchemaEntity163Update) -> Optional[HrModelEntity163]:
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

    def get_entity_164_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity164]:
        return self.db.query(HrModelEntity164).offset(skip).limit(limit).all()

    def get_entity_164_by_id(self, entity_id: int) -> Optional[HrModelEntity164]:
        return self.db.query(HrModelEntity164).filter(HrModelEntity164.id == entity_id).first()

    def create_entity_164(self, payload: HrSchemaEntity164Create) -> HrModelEntity164:
        db_obj = HrModelEntity164(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_164(self, entity_id: int, payload: HrSchemaEntity164Update) -> Optional[HrModelEntity164]:
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

    def get_entity_165_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity165]:
        return self.db.query(HrModelEntity165).offset(skip).limit(limit).all()

    def get_entity_165_by_id(self, entity_id: int) -> Optional[HrModelEntity165]:
        return self.db.query(HrModelEntity165).filter(HrModelEntity165.id == entity_id).first()

    def create_entity_165(self, payload: HrSchemaEntity165Create) -> HrModelEntity165:
        db_obj = HrModelEntity165(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_165(self, entity_id: int, payload: HrSchemaEntity165Update) -> Optional[HrModelEntity165]:
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

    def get_entity_166_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity166]:
        return self.db.query(HrModelEntity166).offset(skip).limit(limit).all()

    def get_entity_166_by_id(self, entity_id: int) -> Optional[HrModelEntity166]:
        return self.db.query(HrModelEntity166).filter(HrModelEntity166.id == entity_id).first()

    def create_entity_166(self, payload: HrSchemaEntity166Create) -> HrModelEntity166:
        db_obj = HrModelEntity166(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_166(self, entity_id: int, payload: HrSchemaEntity166Update) -> Optional[HrModelEntity166]:
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

    def get_entity_167_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity167]:
        return self.db.query(HrModelEntity167).offset(skip).limit(limit).all()

    def get_entity_167_by_id(self, entity_id: int) -> Optional[HrModelEntity167]:
        return self.db.query(HrModelEntity167).filter(HrModelEntity167.id == entity_id).first()

    def create_entity_167(self, payload: HrSchemaEntity167Create) -> HrModelEntity167:
        db_obj = HrModelEntity167(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_167(self, entity_id: int, payload: HrSchemaEntity167Update) -> Optional[HrModelEntity167]:
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

    def get_entity_168_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity168]:
        return self.db.query(HrModelEntity168).offset(skip).limit(limit).all()

    def get_entity_168_by_id(self, entity_id: int) -> Optional[HrModelEntity168]:
        return self.db.query(HrModelEntity168).filter(HrModelEntity168.id == entity_id).first()

    def create_entity_168(self, payload: HrSchemaEntity168Create) -> HrModelEntity168:
        db_obj = HrModelEntity168(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_168(self, entity_id: int, payload: HrSchemaEntity168Update) -> Optional[HrModelEntity168]:
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

    def get_entity_169_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity169]:
        return self.db.query(HrModelEntity169).offset(skip).limit(limit).all()

    def get_entity_169_by_id(self, entity_id: int) -> Optional[HrModelEntity169]:
        return self.db.query(HrModelEntity169).filter(HrModelEntity169.id == entity_id).first()

    def create_entity_169(self, payload: HrSchemaEntity169Create) -> HrModelEntity169:
        db_obj = HrModelEntity169(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_169(self, entity_id: int, payload: HrSchemaEntity169Update) -> Optional[HrModelEntity169]:
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

    def get_entity_170_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity170]:
        return self.db.query(HrModelEntity170).offset(skip).limit(limit).all()

    def get_entity_170_by_id(self, entity_id: int) -> Optional[HrModelEntity170]:
        return self.db.query(HrModelEntity170).filter(HrModelEntity170.id == entity_id).first()

    def create_entity_170(self, payload: HrSchemaEntity170Create) -> HrModelEntity170:
        db_obj = HrModelEntity170(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_170(self, entity_id: int, payload: HrSchemaEntity170Update) -> Optional[HrModelEntity170]:
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

    def get_entity_171_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity171]:
        return self.db.query(HrModelEntity171).offset(skip).limit(limit).all()

    def get_entity_171_by_id(self, entity_id: int) -> Optional[HrModelEntity171]:
        return self.db.query(HrModelEntity171).filter(HrModelEntity171.id == entity_id).first()

    def create_entity_171(self, payload: HrSchemaEntity171Create) -> HrModelEntity171:
        db_obj = HrModelEntity171(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_171(self, entity_id: int, payload: HrSchemaEntity171Update) -> Optional[HrModelEntity171]:
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

    def get_entity_172_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity172]:
        return self.db.query(HrModelEntity172).offset(skip).limit(limit).all()

    def get_entity_172_by_id(self, entity_id: int) -> Optional[HrModelEntity172]:
        return self.db.query(HrModelEntity172).filter(HrModelEntity172.id == entity_id).first()

    def create_entity_172(self, payload: HrSchemaEntity172Create) -> HrModelEntity172:
        db_obj = HrModelEntity172(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_172(self, entity_id: int, payload: HrSchemaEntity172Update) -> Optional[HrModelEntity172]:
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

    def get_entity_173_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity173]:
        return self.db.query(HrModelEntity173).offset(skip).limit(limit).all()

    def get_entity_173_by_id(self, entity_id: int) -> Optional[HrModelEntity173]:
        return self.db.query(HrModelEntity173).filter(HrModelEntity173.id == entity_id).first()

    def create_entity_173(self, payload: HrSchemaEntity173Create) -> HrModelEntity173:
        db_obj = HrModelEntity173(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_173(self, entity_id: int, payload: HrSchemaEntity173Update) -> Optional[HrModelEntity173]:
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

    def get_entity_174_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity174]:
        return self.db.query(HrModelEntity174).offset(skip).limit(limit).all()

    def get_entity_174_by_id(self, entity_id: int) -> Optional[HrModelEntity174]:
        return self.db.query(HrModelEntity174).filter(HrModelEntity174.id == entity_id).first()

    def create_entity_174(self, payload: HrSchemaEntity174Create) -> HrModelEntity174:
        db_obj = HrModelEntity174(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_174(self, entity_id: int, payload: HrSchemaEntity174Update) -> Optional[HrModelEntity174]:
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

    def get_entity_175_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity175]:
        return self.db.query(HrModelEntity175).offset(skip).limit(limit).all()

    def get_entity_175_by_id(self, entity_id: int) -> Optional[HrModelEntity175]:
        return self.db.query(HrModelEntity175).filter(HrModelEntity175.id == entity_id).first()

    def create_entity_175(self, payload: HrSchemaEntity175Create) -> HrModelEntity175:
        db_obj = HrModelEntity175(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_175(self, entity_id: int, payload: HrSchemaEntity175Update) -> Optional[HrModelEntity175]:
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

    def get_entity_176_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity176]:
        return self.db.query(HrModelEntity176).offset(skip).limit(limit).all()

    def get_entity_176_by_id(self, entity_id: int) -> Optional[HrModelEntity176]:
        return self.db.query(HrModelEntity176).filter(HrModelEntity176.id == entity_id).first()

    def create_entity_176(self, payload: HrSchemaEntity176Create) -> HrModelEntity176:
        db_obj = HrModelEntity176(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_176(self, entity_id: int, payload: HrSchemaEntity176Update) -> Optional[HrModelEntity176]:
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

    def get_entity_177_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity177]:
        return self.db.query(HrModelEntity177).offset(skip).limit(limit).all()

    def get_entity_177_by_id(self, entity_id: int) -> Optional[HrModelEntity177]:
        return self.db.query(HrModelEntity177).filter(HrModelEntity177.id == entity_id).first()

    def create_entity_177(self, payload: HrSchemaEntity177Create) -> HrModelEntity177:
        db_obj = HrModelEntity177(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_177(self, entity_id: int, payload: HrSchemaEntity177Update) -> Optional[HrModelEntity177]:
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

    def get_entity_178_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity178]:
        return self.db.query(HrModelEntity178).offset(skip).limit(limit).all()

    def get_entity_178_by_id(self, entity_id: int) -> Optional[HrModelEntity178]:
        return self.db.query(HrModelEntity178).filter(HrModelEntity178.id == entity_id).first()

    def create_entity_178(self, payload: HrSchemaEntity178Create) -> HrModelEntity178:
        db_obj = HrModelEntity178(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_178(self, entity_id: int, payload: HrSchemaEntity178Update) -> Optional[HrModelEntity178]:
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

    def get_entity_179_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity179]:
        return self.db.query(HrModelEntity179).offset(skip).limit(limit).all()

    def get_entity_179_by_id(self, entity_id: int) -> Optional[HrModelEntity179]:
        return self.db.query(HrModelEntity179).filter(HrModelEntity179.id == entity_id).first()

    def create_entity_179(self, payload: HrSchemaEntity179Create) -> HrModelEntity179:
        db_obj = HrModelEntity179(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_179(self, entity_id: int, payload: HrSchemaEntity179Update) -> Optional[HrModelEntity179]:
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

    def get_entity_180_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity180]:
        return self.db.query(HrModelEntity180).offset(skip).limit(limit).all()

    def get_entity_180_by_id(self, entity_id: int) -> Optional[HrModelEntity180]:
        return self.db.query(HrModelEntity180).filter(HrModelEntity180.id == entity_id).first()

    def create_entity_180(self, payload: HrSchemaEntity180Create) -> HrModelEntity180:
        db_obj = HrModelEntity180(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_180(self, entity_id: int, payload: HrSchemaEntity180Update) -> Optional[HrModelEntity180]:
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

    def get_entity_181_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity181]:
        return self.db.query(HrModelEntity181).offset(skip).limit(limit).all()

    def get_entity_181_by_id(self, entity_id: int) -> Optional[HrModelEntity181]:
        return self.db.query(HrModelEntity181).filter(HrModelEntity181.id == entity_id).first()

    def create_entity_181(self, payload: HrSchemaEntity181Create) -> HrModelEntity181:
        db_obj = HrModelEntity181(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_181(self, entity_id: int, payload: HrSchemaEntity181Update) -> Optional[HrModelEntity181]:
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

    def get_entity_182_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity182]:
        return self.db.query(HrModelEntity182).offset(skip).limit(limit).all()

    def get_entity_182_by_id(self, entity_id: int) -> Optional[HrModelEntity182]:
        return self.db.query(HrModelEntity182).filter(HrModelEntity182.id == entity_id).first()

    def create_entity_182(self, payload: HrSchemaEntity182Create) -> HrModelEntity182:
        db_obj = HrModelEntity182(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_182(self, entity_id: int, payload: HrSchemaEntity182Update) -> Optional[HrModelEntity182]:
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

    def get_entity_183_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity183]:
        return self.db.query(HrModelEntity183).offset(skip).limit(limit).all()

    def get_entity_183_by_id(self, entity_id: int) -> Optional[HrModelEntity183]:
        return self.db.query(HrModelEntity183).filter(HrModelEntity183.id == entity_id).first()

    def create_entity_183(self, payload: HrSchemaEntity183Create) -> HrModelEntity183:
        db_obj = HrModelEntity183(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_183(self, entity_id: int, payload: HrSchemaEntity183Update) -> Optional[HrModelEntity183]:
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

    def get_entity_184_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity184]:
        return self.db.query(HrModelEntity184).offset(skip).limit(limit).all()

    def get_entity_184_by_id(self, entity_id: int) -> Optional[HrModelEntity184]:
        return self.db.query(HrModelEntity184).filter(HrModelEntity184.id == entity_id).first()

    def create_entity_184(self, payload: HrSchemaEntity184Create) -> HrModelEntity184:
        db_obj = HrModelEntity184(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_184(self, entity_id: int, payload: HrSchemaEntity184Update) -> Optional[HrModelEntity184]:
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

    def get_entity_185_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity185]:
        return self.db.query(HrModelEntity185).offset(skip).limit(limit).all()

    def get_entity_185_by_id(self, entity_id: int) -> Optional[HrModelEntity185]:
        return self.db.query(HrModelEntity185).filter(HrModelEntity185.id == entity_id).first()

    def create_entity_185(self, payload: HrSchemaEntity185Create) -> HrModelEntity185:
        db_obj = HrModelEntity185(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_185(self, entity_id: int, payload: HrSchemaEntity185Update) -> Optional[HrModelEntity185]:
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

    def get_entity_186_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity186]:
        return self.db.query(HrModelEntity186).offset(skip).limit(limit).all()

    def get_entity_186_by_id(self, entity_id: int) -> Optional[HrModelEntity186]:
        return self.db.query(HrModelEntity186).filter(HrModelEntity186.id == entity_id).first()

    def create_entity_186(self, payload: HrSchemaEntity186Create) -> HrModelEntity186:
        db_obj = HrModelEntity186(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_186(self, entity_id: int, payload: HrSchemaEntity186Update) -> Optional[HrModelEntity186]:
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

    def get_entity_187_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity187]:
        return self.db.query(HrModelEntity187).offset(skip).limit(limit).all()

    def get_entity_187_by_id(self, entity_id: int) -> Optional[HrModelEntity187]:
        return self.db.query(HrModelEntity187).filter(HrModelEntity187.id == entity_id).first()

    def create_entity_187(self, payload: HrSchemaEntity187Create) -> HrModelEntity187:
        db_obj = HrModelEntity187(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_187(self, entity_id: int, payload: HrSchemaEntity187Update) -> Optional[HrModelEntity187]:
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

    def get_entity_188_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity188]:
        return self.db.query(HrModelEntity188).offset(skip).limit(limit).all()

    def get_entity_188_by_id(self, entity_id: int) -> Optional[HrModelEntity188]:
        return self.db.query(HrModelEntity188).filter(HrModelEntity188.id == entity_id).first()

    def create_entity_188(self, payload: HrSchemaEntity188Create) -> HrModelEntity188:
        db_obj = HrModelEntity188(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_188(self, entity_id: int, payload: HrSchemaEntity188Update) -> Optional[HrModelEntity188]:
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

    def get_entity_189_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity189]:
        return self.db.query(HrModelEntity189).offset(skip).limit(limit).all()

    def get_entity_189_by_id(self, entity_id: int) -> Optional[HrModelEntity189]:
        return self.db.query(HrModelEntity189).filter(HrModelEntity189.id == entity_id).first()

    def create_entity_189(self, payload: HrSchemaEntity189Create) -> HrModelEntity189:
        db_obj = HrModelEntity189(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_189(self, entity_id: int, payload: HrSchemaEntity189Update) -> Optional[HrModelEntity189]:
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

    def get_entity_190_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity190]:
        return self.db.query(HrModelEntity190).offset(skip).limit(limit).all()

    def get_entity_190_by_id(self, entity_id: int) -> Optional[HrModelEntity190]:
        return self.db.query(HrModelEntity190).filter(HrModelEntity190.id == entity_id).first()

    def create_entity_190(self, payload: HrSchemaEntity190Create) -> HrModelEntity190:
        db_obj = HrModelEntity190(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_190(self, entity_id: int, payload: HrSchemaEntity190Update) -> Optional[HrModelEntity190]:
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

    def get_entity_191_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity191]:
        return self.db.query(HrModelEntity191).offset(skip).limit(limit).all()

    def get_entity_191_by_id(self, entity_id: int) -> Optional[HrModelEntity191]:
        return self.db.query(HrModelEntity191).filter(HrModelEntity191.id == entity_id).first()

    def create_entity_191(self, payload: HrSchemaEntity191Create) -> HrModelEntity191:
        db_obj = HrModelEntity191(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_191(self, entity_id: int, payload: HrSchemaEntity191Update) -> Optional[HrModelEntity191]:
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

    def get_entity_192_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity192]:
        return self.db.query(HrModelEntity192).offset(skip).limit(limit).all()

    def get_entity_192_by_id(self, entity_id: int) -> Optional[HrModelEntity192]:
        return self.db.query(HrModelEntity192).filter(HrModelEntity192.id == entity_id).first()

    def create_entity_192(self, payload: HrSchemaEntity192Create) -> HrModelEntity192:
        db_obj = HrModelEntity192(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_192(self, entity_id: int, payload: HrSchemaEntity192Update) -> Optional[HrModelEntity192]:
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

    def get_entity_193_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity193]:
        return self.db.query(HrModelEntity193).offset(skip).limit(limit).all()

    def get_entity_193_by_id(self, entity_id: int) -> Optional[HrModelEntity193]:
        return self.db.query(HrModelEntity193).filter(HrModelEntity193.id == entity_id).first()

    def create_entity_193(self, payload: HrSchemaEntity193Create) -> HrModelEntity193:
        db_obj = HrModelEntity193(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_193(self, entity_id: int, payload: HrSchemaEntity193Update) -> Optional[HrModelEntity193]:
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

    def get_entity_194_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity194]:
        return self.db.query(HrModelEntity194).offset(skip).limit(limit).all()

    def get_entity_194_by_id(self, entity_id: int) -> Optional[HrModelEntity194]:
        return self.db.query(HrModelEntity194).filter(HrModelEntity194.id == entity_id).first()

    def create_entity_194(self, payload: HrSchemaEntity194Create) -> HrModelEntity194:
        db_obj = HrModelEntity194(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_194(self, entity_id: int, payload: HrSchemaEntity194Update) -> Optional[HrModelEntity194]:
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

    def get_entity_195_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity195]:
        return self.db.query(HrModelEntity195).offset(skip).limit(limit).all()

    def get_entity_195_by_id(self, entity_id: int) -> Optional[HrModelEntity195]:
        return self.db.query(HrModelEntity195).filter(HrModelEntity195.id == entity_id).first()

    def create_entity_195(self, payload: HrSchemaEntity195Create) -> HrModelEntity195:
        db_obj = HrModelEntity195(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_195(self, entity_id: int, payload: HrSchemaEntity195Update) -> Optional[HrModelEntity195]:
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

    def get_entity_196_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity196]:
        return self.db.query(HrModelEntity196).offset(skip).limit(limit).all()

    def get_entity_196_by_id(self, entity_id: int) -> Optional[HrModelEntity196]:
        return self.db.query(HrModelEntity196).filter(HrModelEntity196.id == entity_id).first()

    def create_entity_196(self, payload: HrSchemaEntity196Create) -> HrModelEntity196:
        db_obj = HrModelEntity196(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_196(self, entity_id: int, payload: HrSchemaEntity196Update) -> Optional[HrModelEntity196]:
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

    def get_entity_197_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity197]:
        return self.db.query(HrModelEntity197).offset(skip).limit(limit).all()

    def get_entity_197_by_id(self, entity_id: int) -> Optional[HrModelEntity197]:
        return self.db.query(HrModelEntity197).filter(HrModelEntity197.id == entity_id).first()

    def create_entity_197(self, payload: HrSchemaEntity197Create) -> HrModelEntity197:
        db_obj = HrModelEntity197(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_197(self, entity_id: int, payload: HrSchemaEntity197Update) -> Optional[HrModelEntity197]:
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

    def get_entity_198_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity198]:
        return self.db.query(HrModelEntity198).offset(skip).limit(limit).all()

    def get_entity_198_by_id(self, entity_id: int) -> Optional[HrModelEntity198]:
        return self.db.query(HrModelEntity198).filter(HrModelEntity198.id == entity_id).first()

    def create_entity_198(self, payload: HrSchemaEntity198Create) -> HrModelEntity198:
        db_obj = HrModelEntity198(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_198(self, entity_id: int, payload: HrSchemaEntity198Update) -> Optional[HrModelEntity198]:
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

    def get_entity_199_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity199]:
        return self.db.query(HrModelEntity199).offset(skip).limit(limit).all()

    def get_entity_199_by_id(self, entity_id: int) -> Optional[HrModelEntity199]:
        return self.db.query(HrModelEntity199).filter(HrModelEntity199.id == entity_id).first()

    def create_entity_199(self, payload: HrSchemaEntity199Create) -> HrModelEntity199:
        db_obj = HrModelEntity199(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_199(self, entity_id: int, payload: HrSchemaEntity199Update) -> Optional[HrModelEntity199]:
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

    def get_entity_200_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity200]:
        return self.db.query(HrModelEntity200).offset(skip).limit(limit).all()

    def get_entity_200_by_id(self, entity_id: int) -> Optional[HrModelEntity200]:
        return self.db.query(HrModelEntity200).filter(HrModelEntity200.id == entity_id).first()

    def create_entity_200(self, payload: HrSchemaEntity200Create) -> HrModelEntity200:
        db_obj = HrModelEntity200(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_200(self, entity_id: int, payload: HrSchemaEntity200Update) -> Optional[HrModelEntity200]:
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

    def get_entity_201_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity201]:
        return self.db.query(HrModelEntity201).offset(skip).limit(limit).all()

    def get_entity_201_by_id(self, entity_id: int) -> Optional[HrModelEntity201]:
        return self.db.query(HrModelEntity201).filter(HrModelEntity201.id == entity_id).first()

    def create_entity_201(self, payload: HrSchemaEntity201Create) -> HrModelEntity201:
        db_obj = HrModelEntity201(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_201(self, entity_id: int, payload: HrSchemaEntity201Update) -> Optional[HrModelEntity201]:
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

    def get_entity_202_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity202]:
        return self.db.query(HrModelEntity202).offset(skip).limit(limit).all()

    def get_entity_202_by_id(self, entity_id: int) -> Optional[HrModelEntity202]:
        return self.db.query(HrModelEntity202).filter(HrModelEntity202.id == entity_id).first()

    def create_entity_202(self, payload: HrSchemaEntity202Create) -> HrModelEntity202:
        db_obj = HrModelEntity202(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_202(self, entity_id: int, payload: HrSchemaEntity202Update) -> Optional[HrModelEntity202]:
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

    def get_entity_203_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity203]:
        return self.db.query(HrModelEntity203).offset(skip).limit(limit).all()

    def get_entity_203_by_id(self, entity_id: int) -> Optional[HrModelEntity203]:
        return self.db.query(HrModelEntity203).filter(HrModelEntity203.id == entity_id).first()

    def create_entity_203(self, payload: HrSchemaEntity203Create) -> HrModelEntity203:
        db_obj = HrModelEntity203(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_203(self, entity_id: int, payload: HrSchemaEntity203Update) -> Optional[HrModelEntity203]:
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

    def get_entity_204_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity204]:
        return self.db.query(HrModelEntity204).offset(skip).limit(limit).all()

    def get_entity_204_by_id(self, entity_id: int) -> Optional[HrModelEntity204]:
        return self.db.query(HrModelEntity204).filter(HrModelEntity204.id == entity_id).first()

    def create_entity_204(self, payload: HrSchemaEntity204Create) -> HrModelEntity204:
        db_obj = HrModelEntity204(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_204(self, entity_id: int, payload: HrSchemaEntity204Update) -> Optional[HrModelEntity204]:
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

    def get_entity_205_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity205]:
        return self.db.query(HrModelEntity205).offset(skip).limit(limit).all()

    def get_entity_205_by_id(self, entity_id: int) -> Optional[HrModelEntity205]:
        return self.db.query(HrModelEntity205).filter(HrModelEntity205.id == entity_id).first()

    def create_entity_205(self, payload: HrSchemaEntity205Create) -> HrModelEntity205:
        db_obj = HrModelEntity205(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_205(self, entity_id: int, payload: HrSchemaEntity205Update) -> Optional[HrModelEntity205]:
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

    def get_entity_206_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity206]:
        return self.db.query(HrModelEntity206).offset(skip).limit(limit).all()

    def get_entity_206_by_id(self, entity_id: int) -> Optional[HrModelEntity206]:
        return self.db.query(HrModelEntity206).filter(HrModelEntity206.id == entity_id).first()

    def create_entity_206(self, payload: HrSchemaEntity206Create) -> HrModelEntity206:
        db_obj = HrModelEntity206(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_206(self, entity_id: int, payload: HrSchemaEntity206Update) -> Optional[HrModelEntity206]:
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

    def get_entity_207_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity207]:
        return self.db.query(HrModelEntity207).offset(skip).limit(limit).all()

    def get_entity_207_by_id(self, entity_id: int) -> Optional[HrModelEntity207]:
        return self.db.query(HrModelEntity207).filter(HrModelEntity207.id == entity_id).first()

    def create_entity_207(self, payload: HrSchemaEntity207Create) -> HrModelEntity207:
        db_obj = HrModelEntity207(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_207(self, entity_id: int, payload: HrSchemaEntity207Update) -> Optional[HrModelEntity207]:
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

    def get_entity_208_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity208]:
        return self.db.query(HrModelEntity208).offset(skip).limit(limit).all()

    def get_entity_208_by_id(self, entity_id: int) -> Optional[HrModelEntity208]:
        return self.db.query(HrModelEntity208).filter(HrModelEntity208.id == entity_id).first()

    def create_entity_208(self, payload: HrSchemaEntity208Create) -> HrModelEntity208:
        db_obj = HrModelEntity208(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_208(self, entity_id: int, payload: HrSchemaEntity208Update) -> Optional[HrModelEntity208]:
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

    def get_entity_209_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity209]:
        return self.db.query(HrModelEntity209).offset(skip).limit(limit).all()

    def get_entity_209_by_id(self, entity_id: int) -> Optional[HrModelEntity209]:
        return self.db.query(HrModelEntity209).filter(HrModelEntity209.id == entity_id).first()

    def create_entity_209(self, payload: HrSchemaEntity209Create) -> HrModelEntity209:
        db_obj = HrModelEntity209(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_209(self, entity_id: int, payload: HrSchemaEntity209Update) -> Optional[HrModelEntity209]:
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

    def get_entity_210_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity210]:
        return self.db.query(HrModelEntity210).offset(skip).limit(limit).all()

    def get_entity_210_by_id(self, entity_id: int) -> Optional[HrModelEntity210]:
        return self.db.query(HrModelEntity210).filter(HrModelEntity210.id == entity_id).first()

    def create_entity_210(self, payload: HrSchemaEntity210Create) -> HrModelEntity210:
        db_obj = HrModelEntity210(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_210(self, entity_id: int, payload: HrSchemaEntity210Update) -> Optional[HrModelEntity210]:
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

    def get_entity_211_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity211]:
        return self.db.query(HrModelEntity211).offset(skip).limit(limit).all()

    def get_entity_211_by_id(self, entity_id: int) -> Optional[HrModelEntity211]:
        return self.db.query(HrModelEntity211).filter(HrModelEntity211.id == entity_id).first()

    def create_entity_211(self, payload: HrSchemaEntity211Create) -> HrModelEntity211:
        db_obj = HrModelEntity211(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_211(self, entity_id: int, payload: HrSchemaEntity211Update) -> Optional[HrModelEntity211]:
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

    def get_entity_212_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity212]:
        return self.db.query(HrModelEntity212).offset(skip).limit(limit).all()

    def get_entity_212_by_id(self, entity_id: int) -> Optional[HrModelEntity212]:
        return self.db.query(HrModelEntity212).filter(HrModelEntity212.id == entity_id).first()

    def create_entity_212(self, payload: HrSchemaEntity212Create) -> HrModelEntity212:
        db_obj = HrModelEntity212(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_212(self, entity_id: int, payload: HrSchemaEntity212Update) -> Optional[HrModelEntity212]:
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

    def get_entity_213_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity213]:
        return self.db.query(HrModelEntity213).offset(skip).limit(limit).all()

    def get_entity_213_by_id(self, entity_id: int) -> Optional[HrModelEntity213]:
        return self.db.query(HrModelEntity213).filter(HrModelEntity213.id == entity_id).first()

    def create_entity_213(self, payload: HrSchemaEntity213Create) -> HrModelEntity213:
        db_obj = HrModelEntity213(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_213(self, entity_id: int, payload: HrSchemaEntity213Update) -> Optional[HrModelEntity213]:
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

    def get_entity_214_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity214]:
        return self.db.query(HrModelEntity214).offset(skip).limit(limit).all()

    def get_entity_214_by_id(self, entity_id: int) -> Optional[HrModelEntity214]:
        return self.db.query(HrModelEntity214).filter(HrModelEntity214.id == entity_id).first()

    def create_entity_214(self, payload: HrSchemaEntity214Create) -> HrModelEntity214:
        db_obj = HrModelEntity214(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_214(self, entity_id: int, payload: HrSchemaEntity214Update) -> Optional[HrModelEntity214]:
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

    def get_entity_215_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity215]:
        return self.db.query(HrModelEntity215).offset(skip).limit(limit).all()

    def get_entity_215_by_id(self, entity_id: int) -> Optional[HrModelEntity215]:
        return self.db.query(HrModelEntity215).filter(HrModelEntity215.id == entity_id).first()

    def create_entity_215(self, payload: HrSchemaEntity215Create) -> HrModelEntity215:
        db_obj = HrModelEntity215(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_215(self, entity_id: int, payload: HrSchemaEntity215Update) -> Optional[HrModelEntity215]:
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

    def get_entity_216_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity216]:
        return self.db.query(HrModelEntity216).offset(skip).limit(limit).all()

    def get_entity_216_by_id(self, entity_id: int) -> Optional[HrModelEntity216]:
        return self.db.query(HrModelEntity216).filter(HrModelEntity216.id == entity_id).first()

    def create_entity_216(self, payload: HrSchemaEntity216Create) -> HrModelEntity216:
        db_obj = HrModelEntity216(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_216(self, entity_id: int, payload: HrSchemaEntity216Update) -> Optional[HrModelEntity216]:
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

    def get_entity_217_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity217]:
        return self.db.query(HrModelEntity217).offset(skip).limit(limit).all()

    def get_entity_217_by_id(self, entity_id: int) -> Optional[HrModelEntity217]:
        return self.db.query(HrModelEntity217).filter(HrModelEntity217.id == entity_id).first()

    def create_entity_217(self, payload: HrSchemaEntity217Create) -> HrModelEntity217:
        db_obj = HrModelEntity217(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_217(self, entity_id: int, payload: HrSchemaEntity217Update) -> Optional[HrModelEntity217]:
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

    def get_entity_218_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity218]:
        return self.db.query(HrModelEntity218).offset(skip).limit(limit).all()

    def get_entity_218_by_id(self, entity_id: int) -> Optional[HrModelEntity218]:
        return self.db.query(HrModelEntity218).filter(HrModelEntity218.id == entity_id).first()

    def create_entity_218(self, payload: HrSchemaEntity218Create) -> HrModelEntity218:
        db_obj = HrModelEntity218(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_218(self, entity_id: int, payload: HrSchemaEntity218Update) -> Optional[HrModelEntity218]:
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

    def get_entity_219_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity219]:
        return self.db.query(HrModelEntity219).offset(skip).limit(limit).all()

    def get_entity_219_by_id(self, entity_id: int) -> Optional[HrModelEntity219]:
        return self.db.query(HrModelEntity219).filter(HrModelEntity219.id == entity_id).first()

    def create_entity_219(self, payload: HrSchemaEntity219Create) -> HrModelEntity219:
        db_obj = HrModelEntity219(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_219(self, entity_id: int, payload: HrSchemaEntity219Update) -> Optional[HrModelEntity219]:
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

    def get_entity_220_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity220]:
        return self.db.query(HrModelEntity220).offset(skip).limit(limit).all()

    def get_entity_220_by_id(self, entity_id: int) -> Optional[HrModelEntity220]:
        return self.db.query(HrModelEntity220).filter(HrModelEntity220.id == entity_id).first()

    def create_entity_220(self, payload: HrSchemaEntity220Create) -> HrModelEntity220:
        db_obj = HrModelEntity220(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_220(self, entity_id: int, payload: HrSchemaEntity220Update) -> Optional[HrModelEntity220]:
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

    def get_entity_221_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity221]:
        return self.db.query(HrModelEntity221).offset(skip).limit(limit).all()

    def get_entity_221_by_id(self, entity_id: int) -> Optional[HrModelEntity221]:
        return self.db.query(HrModelEntity221).filter(HrModelEntity221.id == entity_id).first()

    def create_entity_221(self, payload: HrSchemaEntity221Create) -> HrModelEntity221:
        db_obj = HrModelEntity221(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_221(self, entity_id: int, payload: HrSchemaEntity221Update) -> Optional[HrModelEntity221]:
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

    def get_entity_222_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity222]:
        return self.db.query(HrModelEntity222).offset(skip).limit(limit).all()

    def get_entity_222_by_id(self, entity_id: int) -> Optional[HrModelEntity222]:
        return self.db.query(HrModelEntity222).filter(HrModelEntity222.id == entity_id).first()

    def create_entity_222(self, payload: HrSchemaEntity222Create) -> HrModelEntity222:
        db_obj = HrModelEntity222(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_222(self, entity_id: int, payload: HrSchemaEntity222Update) -> Optional[HrModelEntity222]:
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

    def get_entity_223_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity223]:
        return self.db.query(HrModelEntity223).offset(skip).limit(limit).all()

    def get_entity_223_by_id(self, entity_id: int) -> Optional[HrModelEntity223]:
        return self.db.query(HrModelEntity223).filter(HrModelEntity223.id == entity_id).first()

    def create_entity_223(self, payload: HrSchemaEntity223Create) -> HrModelEntity223:
        db_obj = HrModelEntity223(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_223(self, entity_id: int, payload: HrSchemaEntity223Update) -> Optional[HrModelEntity223]:
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

    def get_entity_224_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity224]:
        return self.db.query(HrModelEntity224).offset(skip).limit(limit).all()

    def get_entity_224_by_id(self, entity_id: int) -> Optional[HrModelEntity224]:
        return self.db.query(HrModelEntity224).filter(HrModelEntity224.id == entity_id).first()

    def create_entity_224(self, payload: HrSchemaEntity224Create) -> HrModelEntity224:
        db_obj = HrModelEntity224(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_224(self, entity_id: int, payload: HrSchemaEntity224Update) -> Optional[HrModelEntity224]:
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

    def get_entity_225_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity225]:
        return self.db.query(HrModelEntity225).offset(skip).limit(limit).all()

    def get_entity_225_by_id(self, entity_id: int) -> Optional[HrModelEntity225]:
        return self.db.query(HrModelEntity225).filter(HrModelEntity225.id == entity_id).first()

    def create_entity_225(self, payload: HrSchemaEntity225Create) -> HrModelEntity225:
        db_obj = HrModelEntity225(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_225(self, entity_id: int, payload: HrSchemaEntity225Update) -> Optional[HrModelEntity225]:
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

    def get_entity_226_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity226]:
        return self.db.query(HrModelEntity226).offset(skip).limit(limit).all()

    def get_entity_226_by_id(self, entity_id: int) -> Optional[HrModelEntity226]:
        return self.db.query(HrModelEntity226).filter(HrModelEntity226.id == entity_id).first()

    def create_entity_226(self, payload: HrSchemaEntity226Create) -> HrModelEntity226:
        db_obj = HrModelEntity226(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_226(self, entity_id: int, payload: HrSchemaEntity226Update) -> Optional[HrModelEntity226]:
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

    def get_entity_227_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity227]:
        return self.db.query(HrModelEntity227).offset(skip).limit(limit).all()

    def get_entity_227_by_id(self, entity_id: int) -> Optional[HrModelEntity227]:
        return self.db.query(HrModelEntity227).filter(HrModelEntity227.id == entity_id).first()

    def create_entity_227(self, payload: HrSchemaEntity227Create) -> HrModelEntity227:
        db_obj = HrModelEntity227(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_227(self, entity_id: int, payload: HrSchemaEntity227Update) -> Optional[HrModelEntity227]:
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

    def get_entity_228_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity228]:
        return self.db.query(HrModelEntity228).offset(skip).limit(limit).all()

    def get_entity_228_by_id(self, entity_id: int) -> Optional[HrModelEntity228]:
        return self.db.query(HrModelEntity228).filter(HrModelEntity228.id == entity_id).first()

    def create_entity_228(self, payload: HrSchemaEntity228Create) -> HrModelEntity228:
        db_obj = HrModelEntity228(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_228(self, entity_id: int, payload: HrSchemaEntity228Update) -> Optional[HrModelEntity228]:
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

    def get_entity_229_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity229]:
        return self.db.query(HrModelEntity229).offset(skip).limit(limit).all()

    def get_entity_229_by_id(self, entity_id: int) -> Optional[HrModelEntity229]:
        return self.db.query(HrModelEntity229).filter(HrModelEntity229.id == entity_id).first()

    def create_entity_229(self, payload: HrSchemaEntity229Create) -> HrModelEntity229:
        db_obj = HrModelEntity229(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_229(self, entity_id: int, payload: HrSchemaEntity229Update) -> Optional[HrModelEntity229]:
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

    def get_entity_230_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity230]:
        return self.db.query(HrModelEntity230).offset(skip).limit(limit).all()

    def get_entity_230_by_id(self, entity_id: int) -> Optional[HrModelEntity230]:
        return self.db.query(HrModelEntity230).filter(HrModelEntity230.id == entity_id).first()

    def create_entity_230(self, payload: HrSchemaEntity230Create) -> HrModelEntity230:
        db_obj = HrModelEntity230(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_230(self, entity_id: int, payload: HrSchemaEntity230Update) -> Optional[HrModelEntity230]:
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

    def get_entity_231_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity231]:
        return self.db.query(HrModelEntity231).offset(skip).limit(limit).all()

    def get_entity_231_by_id(self, entity_id: int) -> Optional[HrModelEntity231]:
        return self.db.query(HrModelEntity231).filter(HrModelEntity231.id == entity_id).first()

    def create_entity_231(self, payload: HrSchemaEntity231Create) -> HrModelEntity231:
        db_obj = HrModelEntity231(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_231(self, entity_id: int, payload: HrSchemaEntity231Update) -> Optional[HrModelEntity231]:
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

    def get_entity_232_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity232]:
        return self.db.query(HrModelEntity232).offset(skip).limit(limit).all()

    def get_entity_232_by_id(self, entity_id: int) -> Optional[HrModelEntity232]:
        return self.db.query(HrModelEntity232).filter(HrModelEntity232.id == entity_id).first()

    def create_entity_232(self, payload: HrSchemaEntity232Create) -> HrModelEntity232:
        db_obj = HrModelEntity232(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_232(self, entity_id: int, payload: HrSchemaEntity232Update) -> Optional[HrModelEntity232]:
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

    def get_entity_233_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity233]:
        return self.db.query(HrModelEntity233).offset(skip).limit(limit).all()

    def get_entity_233_by_id(self, entity_id: int) -> Optional[HrModelEntity233]:
        return self.db.query(HrModelEntity233).filter(HrModelEntity233.id == entity_id).first()

    def create_entity_233(self, payload: HrSchemaEntity233Create) -> HrModelEntity233:
        db_obj = HrModelEntity233(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_233(self, entity_id: int, payload: HrSchemaEntity233Update) -> Optional[HrModelEntity233]:
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

    def get_entity_234_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity234]:
        return self.db.query(HrModelEntity234).offset(skip).limit(limit).all()

    def get_entity_234_by_id(self, entity_id: int) -> Optional[HrModelEntity234]:
        return self.db.query(HrModelEntity234).filter(HrModelEntity234.id == entity_id).first()

    def create_entity_234(self, payload: HrSchemaEntity234Create) -> HrModelEntity234:
        db_obj = HrModelEntity234(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_234(self, entity_id: int, payload: HrSchemaEntity234Update) -> Optional[HrModelEntity234]:
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

    def get_entity_235_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity235]:
        return self.db.query(HrModelEntity235).offset(skip).limit(limit).all()

    def get_entity_235_by_id(self, entity_id: int) -> Optional[HrModelEntity235]:
        return self.db.query(HrModelEntity235).filter(HrModelEntity235.id == entity_id).first()

    def create_entity_235(self, payload: HrSchemaEntity235Create) -> HrModelEntity235:
        db_obj = HrModelEntity235(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_235(self, entity_id: int, payload: HrSchemaEntity235Update) -> Optional[HrModelEntity235]:
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

    def get_entity_236_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity236]:
        return self.db.query(HrModelEntity236).offset(skip).limit(limit).all()

    def get_entity_236_by_id(self, entity_id: int) -> Optional[HrModelEntity236]:
        return self.db.query(HrModelEntity236).filter(HrModelEntity236.id == entity_id).first()

    def create_entity_236(self, payload: HrSchemaEntity236Create) -> HrModelEntity236:
        db_obj = HrModelEntity236(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_236(self, entity_id: int, payload: HrSchemaEntity236Update) -> Optional[HrModelEntity236]:
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

    def get_entity_237_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity237]:
        return self.db.query(HrModelEntity237).offset(skip).limit(limit).all()

    def get_entity_237_by_id(self, entity_id: int) -> Optional[HrModelEntity237]:
        return self.db.query(HrModelEntity237).filter(HrModelEntity237.id == entity_id).first()

    def create_entity_237(self, payload: HrSchemaEntity237Create) -> HrModelEntity237:
        db_obj = HrModelEntity237(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_237(self, entity_id: int, payload: HrSchemaEntity237Update) -> Optional[HrModelEntity237]:
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

    def get_entity_238_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity238]:
        return self.db.query(HrModelEntity238).offset(skip).limit(limit).all()

    def get_entity_238_by_id(self, entity_id: int) -> Optional[HrModelEntity238]:
        return self.db.query(HrModelEntity238).filter(HrModelEntity238.id == entity_id).first()

    def create_entity_238(self, payload: HrSchemaEntity238Create) -> HrModelEntity238:
        db_obj = HrModelEntity238(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_238(self, entity_id: int, payload: HrSchemaEntity238Update) -> Optional[HrModelEntity238]:
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

    def get_entity_239_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity239]:
        return self.db.query(HrModelEntity239).offset(skip).limit(limit).all()

    def get_entity_239_by_id(self, entity_id: int) -> Optional[HrModelEntity239]:
        return self.db.query(HrModelEntity239).filter(HrModelEntity239.id == entity_id).first()

    def create_entity_239(self, payload: HrSchemaEntity239Create) -> HrModelEntity239:
        db_obj = HrModelEntity239(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_239(self, entity_id: int, payload: HrSchemaEntity239Update) -> Optional[HrModelEntity239]:
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

    def get_entity_240_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity240]:
        return self.db.query(HrModelEntity240).offset(skip).limit(limit).all()

    def get_entity_240_by_id(self, entity_id: int) -> Optional[HrModelEntity240]:
        return self.db.query(HrModelEntity240).filter(HrModelEntity240.id == entity_id).first()

    def create_entity_240(self, payload: HrSchemaEntity240Create) -> HrModelEntity240:
        db_obj = HrModelEntity240(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_240(self, entity_id: int, payload: HrSchemaEntity240Update) -> Optional[HrModelEntity240]:
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

    def get_entity_241_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity241]:
        return self.db.query(HrModelEntity241).offset(skip).limit(limit).all()

    def get_entity_241_by_id(self, entity_id: int) -> Optional[HrModelEntity241]:
        return self.db.query(HrModelEntity241).filter(HrModelEntity241.id == entity_id).first()

    def create_entity_241(self, payload: HrSchemaEntity241Create) -> HrModelEntity241:
        db_obj = HrModelEntity241(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_241(self, entity_id: int, payload: HrSchemaEntity241Update) -> Optional[HrModelEntity241]:
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

    def get_entity_242_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity242]:
        return self.db.query(HrModelEntity242).offset(skip).limit(limit).all()

    def get_entity_242_by_id(self, entity_id: int) -> Optional[HrModelEntity242]:
        return self.db.query(HrModelEntity242).filter(HrModelEntity242.id == entity_id).first()

    def create_entity_242(self, payload: HrSchemaEntity242Create) -> HrModelEntity242:
        db_obj = HrModelEntity242(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_242(self, entity_id: int, payload: HrSchemaEntity242Update) -> Optional[HrModelEntity242]:
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

    def get_entity_243_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity243]:
        return self.db.query(HrModelEntity243).offset(skip).limit(limit).all()

    def get_entity_243_by_id(self, entity_id: int) -> Optional[HrModelEntity243]:
        return self.db.query(HrModelEntity243).filter(HrModelEntity243.id == entity_id).first()

    def create_entity_243(self, payload: HrSchemaEntity243Create) -> HrModelEntity243:
        db_obj = HrModelEntity243(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_243(self, entity_id: int, payload: HrSchemaEntity243Update) -> Optional[HrModelEntity243]:
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

    def get_entity_244_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity244]:
        return self.db.query(HrModelEntity244).offset(skip).limit(limit).all()

    def get_entity_244_by_id(self, entity_id: int) -> Optional[HrModelEntity244]:
        return self.db.query(HrModelEntity244).filter(HrModelEntity244.id == entity_id).first()

    def create_entity_244(self, payload: HrSchemaEntity244Create) -> HrModelEntity244:
        db_obj = HrModelEntity244(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_244(self, entity_id: int, payload: HrSchemaEntity244Update) -> Optional[HrModelEntity244]:
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

    def get_entity_245_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity245]:
        return self.db.query(HrModelEntity245).offset(skip).limit(limit).all()

    def get_entity_245_by_id(self, entity_id: int) -> Optional[HrModelEntity245]:
        return self.db.query(HrModelEntity245).filter(HrModelEntity245.id == entity_id).first()

    def create_entity_245(self, payload: HrSchemaEntity245Create) -> HrModelEntity245:
        db_obj = HrModelEntity245(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_245(self, entity_id: int, payload: HrSchemaEntity245Update) -> Optional[HrModelEntity245]:
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

    def get_entity_246_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity246]:
        return self.db.query(HrModelEntity246).offset(skip).limit(limit).all()

    def get_entity_246_by_id(self, entity_id: int) -> Optional[HrModelEntity246]:
        return self.db.query(HrModelEntity246).filter(HrModelEntity246.id == entity_id).first()

    def create_entity_246(self, payload: HrSchemaEntity246Create) -> HrModelEntity246:
        db_obj = HrModelEntity246(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_246(self, entity_id: int, payload: HrSchemaEntity246Update) -> Optional[HrModelEntity246]:
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

    def get_entity_247_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity247]:
        return self.db.query(HrModelEntity247).offset(skip).limit(limit).all()

    def get_entity_247_by_id(self, entity_id: int) -> Optional[HrModelEntity247]:
        return self.db.query(HrModelEntity247).filter(HrModelEntity247.id == entity_id).first()

    def create_entity_247(self, payload: HrSchemaEntity247Create) -> HrModelEntity247:
        db_obj = HrModelEntity247(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_247(self, entity_id: int, payload: HrSchemaEntity247Update) -> Optional[HrModelEntity247]:
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

    def get_entity_248_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity248]:
        return self.db.query(HrModelEntity248).offset(skip).limit(limit).all()

    def get_entity_248_by_id(self, entity_id: int) -> Optional[HrModelEntity248]:
        return self.db.query(HrModelEntity248).filter(HrModelEntity248.id == entity_id).first()

    def create_entity_248(self, payload: HrSchemaEntity248Create) -> HrModelEntity248:
        db_obj = HrModelEntity248(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_248(self, entity_id: int, payload: HrSchemaEntity248Update) -> Optional[HrModelEntity248]:
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

    def get_entity_249_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity249]:
        return self.db.query(HrModelEntity249).offset(skip).limit(limit).all()

    def get_entity_249_by_id(self, entity_id: int) -> Optional[HrModelEntity249]:
        return self.db.query(HrModelEntity249).filter(HrModelEntity249.id == entity_id).first()

    def create_entity_249(self, payload: HrSchemaEntity249Create) -> HrModelEntity249:
        db_obj = HrModelEntity249(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_249(self, entity_id: int, payload: HrSchemaEntity249Update) -> Optional[HrModelEntity249]:
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

    def get_entity_250_list(self, skip: int = 0, limit: int = 100) -> List[HrModelEntity250]:
        return self.db.query(HrModelEntity250).offset(skip).limit(limit).all()

    def get_entity_250_by_id(self, entity_id: int) -> Optional[HrModelEntity250]:
        return self.db.query(HrModelEntity250).filter(HrModelEntity250.id == entity_id).first()

    def create_entity_250(self, payload: HrSchemaEntity250Create) -> HrModelEntity250:
        db_obj = HrModelEntity250(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_250(self, entity_id: int, payload: HrSchemaEntity250Update) -> Optional[HrModelEntity250]:
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

