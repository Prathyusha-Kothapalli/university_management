"""
Student Life & Hostel Operations - Service Business Logic Layer
Module: app.domains.hostels.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.hostels.models import *
from app.domains.hostels.schemas import *

class HostelsDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity1]:
        return self.db.query(HostelsModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[HostelsModelEntity1]:
        return self.db.query(HostelsModelEntity1).filter(HostelsModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: HostelsSchemaEntity1Create) -> HostelsModelEntity1:
        db_obj = HostelsModelEntity1(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_1(self, entity_id: int, payload: HostelsSchemaEntity1Update) -> Optional[HostelsModelEntity1]:
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

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity2]:
        return self.db.query(HostelsModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[HostelsModelEntity2]:
        return self.db.query(HostelsModelEntity2).filter(HostelsModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: HostelsSchemaEntity2Create) -> HostelsModelEntity2:
        db_obj = HostelsModelEntity2(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_2(self, entity_id: int, payload: HostelsSchemaEntity2Update) -> Optional[HostelsModelEntity2]:
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

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity3]:
        return self.db.query(HostelsModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[HostelsModelEntity3]:
        return self.db.query(HostelsModelEntity3).filter(HostelsModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: HostelsSchemaEntity3Create) -> HostelsModelEntity3:
        db_obj = HostelsModelEntity3(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_3(self, entity_id: int, payload: HostelsSchemaEntity3Update) -> Optional[HostelsModelEntity3]:
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

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity4]:
        return self.db.query(HostelsModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[HostelsModelEntity4]:
        return self.db.query(HostelsModelEntity4).filter(HostelsModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: HostelsSchemaEntity4Create) -> HostelsModelEntity4:
        db_obj = HostelsModelEntity4(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_4(self, entity_id: int, payload: HostelsSchemaEntity4Update) -> Optional[HostelsModelEntity4]:
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

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity5]:
        return self.db.query(HostelsModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[HostelsModelEntity5]:
        return self.db.query(HostelsModelEntity5).filter(HostelsModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: HostelsSchemaEntity5Create) -> HostelsModelEntity5:
        db_obj = HostelsModelEntity5(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_5(self, entity_id: int, payload: HostelsSchemaEntity5Update) -> Optional[HostelsModelEntity5]:
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

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity6]:
        return self.db.query(HostelsModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[HostelsModelEntity6]:
        return self.db.query(HostelsModelEntity6).filter(HostelsModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: HostelsSchemaEntity6Create) -> HostelsModelEntity6:
        db_obj = HostelsModelEntity6(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_6(self, entity_id: int, payload: HostelsSchemaEntity6Update) -> Optional[HostelsModelEntity6]:
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

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity7]:
        return self.db.query(HostelsModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[HostelsModelEntity7]:
        return self.db.query(HostelsModelEntity7).filter(HostelsModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: HostelsSchemaEntity7Create) -> HostelsModelEntity7:
        db_obj = HostelsModelEntity7(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_7(self, entity_id: int, payload: HostelsSchemaEntity7Update) -> Optional[HostelsModelEntity7]:
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

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity8]:
        return self.db.query(HostelsModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[HostelsModelEntity8]:
        return self.db.query(HostelsModelEntity8).filter(HostelsModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: HostelsSchemaEntity8Create) -> HostelsModelEntity8:
        db_obj = HostelsModelEntity8(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_8(self, entity_id: int, payload: HostelsSchemaEntity8Update) -> Optional[HostelsModelEntity8]:
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

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity9]:
        return self.db.query(HostelsModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[HostelsModelEntity9]:
        return self.db.query(HostelsModelEntity9).filter(HostelsModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: HostelsSchemaEntity9Create) -> HostelsModelEntity9:
        db_obj = HostelsModelEntity9(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_9(self, entity_id: int, payload: HostelsSchemaEntity9Update) -> Optional[HostelsModelEntity9]:
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

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity10]:
        return self.db.query(HostelsModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[HostelsModelEntity10]:
        return self.db.query(HostelsModelEntity10).filter(HostelsModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: HostelsSchemaEntity10Create) -> HostelsModelEntity10:
        db_obj = HostelsModelEntity10(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_10(self, entity_id: int, payload: HostelsSchemaEntity10Update) -> Optional[HostelsModelEntity10]:
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

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity11]:
        return self.db.query(HostelsModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[HostelsModelEntity11]:
        return self.db.query(HostelsModelEntity11).filter(HostelsModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: HostelsSchemaEntity11Create) -> HostelsModelEntity11:
        db_obj = HostelsModelEntity11(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_11(self, entity_id: int, payload: HostelsSchemaEntity11Update) -> Optional[HostelsModelEntity11]:
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

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity12]:
        return self.db.query(HostelsModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[HostelsModelEntity12]:
        return self.db.query(HostelsModelEntity12).filter(HostelsModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: HostelsSchemaEntity12Create) -> HostelsModelEntity12:
        db_obj = HostelsModelEntity12(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_12(self, entity_id: int, payload: HostelsSchemaEntity12Update) -> Optional[HostelsModelEntity12]:
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

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity13]:
        return self.db.query(HostelsModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[HostelsModelEntity13]:
        return self.db.query(HostelsModelEntity13).filter(HostelsModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: HostelsSchemaEntity13Create) -> HostelsModelEntity13:
        db_obj = HostelsModelEntity13(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_13(self, entity_id: int, payload: HostelsSchemaEntity13Update) -> Optional[HostelsModelEntity13]:
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

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity14]:
        return self.db.query(HostelsModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[HostelsModelEntity14]:
        return self.db.query(HostelsModelEntity14).filter(HostelsModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: HostelsSchemaEntity14Create) -> HostelsModelEntity14:
        db_obj = HostelsModelEntity14(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_14(self, entity_id: int, payload: HostelsSchemaEntity14Update) -> Optional[HostelsModelEntity14]:
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

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity15]:
        return self.db.query(HostelsModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[HostelsModelEntity15]:
        return self.db.query(HostelsModelEntity15).filter(HostelsModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: HostelsSchemaEntity15Create) -> HostelsModelEntity15:
        db_obj = HostelsModelEntity15(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_15(self, entity_id: int, payload: HostelsSchemaEntity15Update) -> Optional[HostelsModelEntity15]:
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

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity16]:
        return self.db.query(HostelsModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[HostelsModelEntity16]:
        return self.db.query(HostelsModelEntity16).filter(HostelsModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: HostelsSchemaEntity16Create) -> HostelsModelEntity16:
        db_obj = HostelsModelEntity16(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_16(self, entity_id: int, payload: HostelsSchemaEntity16Update) -> Optional[HostelsModelEntity16]:
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

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity17]:
        return self.db.query(HostelsModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[HostelsModelEntity17]:
        return self.db.query(HostelsModelEntity17).filter(HostelsModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: HostelsSchemaEntity17Create) -> HostelsModelEntity17:
        db_obj = HostelsModelEntity17(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_17(self, entity_id: int, payload: HostelsSchemaEntity17Update) -> Optional[HostelsModelEntity17]:
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

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity18]:
        return self.db.query(HostelsModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[HostelsModelEntity18]:
        return self.db.query(HostelsModelEntity18).filter(HostelsModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: HostelsSchemaEntity18Create) -> HostelsModelEntity18:
        db_obj = HostelsModelEntity18(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_18(self, entity_id: int, payload: HostelsSchemaEntity18Update) -> Optional[HostelsModelEntity18]:
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

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity19]:
        return self.db.query(HostelsModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[HostelsModelEntity19]:
        return self.db.query(HostelsModelEntity19).filter(HostelsModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: HostelsSchemaEntity19Create) -> HostelsModelEntity19:
        db_obj = HostelsModelEntity19(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_19(self, entity_id: int, payload: HostelsSchemaEntity19Update) -> Optional[HostelsModelEntity19]:
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

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity20]:
        return self.db.query(HostelsModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[HostelsModelEntity20]:
        return self.db.query(HostelsModelEntity20).filter(HostelsModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: HostelsSchemaEntity20Create) -> HostelsModelEntity20:
        db_obj = HostelsModelEntity20(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_20(self, entity_id: int, payload: HostelsSchemaEntity20Update) -> Optional[HostelsModelEntity20]:
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

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity21]:
        return self.db.query(HostelsModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[HostelsModelEntity21]:
        return self.db.query(HostelsModelEntity21).filter(HostelsModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: HostelsSchemaEntity21Create) -> HostelsModelEntity21:
        db_obj = HostelsModelEntity21(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_21(self, entity_id: int, payload: HostelsSchemaEntity21Update) -> Optional[HostelsModelEntity21]:
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

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity22]:
        return self.db.query(HostelsModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[HostelsModelEntity22]:
        return self.db.query(HostelsModelEntity22).filter(HostelsModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: HostelsSchemaEntity22Create) -> HostelsModelEntity22:
        db_obj = HostelsModelEntity22(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_22(self, entity_id: int, payload: HostelsSchemaEntity22Update) -> Optional[HostelsModelEntity22]:
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

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity23]:
        return self.db.query(HostelsModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[HostelsModelEntity23]:
        return self.db.query(HostelsModelEntity23).filter(HostelsModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: HostelsSchemaEntity23Create) -> HostelsModelEntity23:
        db_obj = HostelsModelEntity23(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_23(self, entity_id: int, payload: HostelsSchemaEntity23Update) -> Optional[HostelsModelEntity23]:
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

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity24]:
        return self.db.query(HostelsModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[HostelsModelEntity24]:
        return self.db.query(HostelsModelEntity24).filter(HostelsModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: HostelsSchemaEntity24Create) -> HostelsModelEntity24:
        db_obj = HostelsModelEntity24(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_24(self, entity_id: int, payload: HostelsSchemaEntity24Update) -> Optional[HostelsModelEntity24]:
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

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity25]:
        return self.db.query(HostelsModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[HostelsModelEntity25]:
        return self.db.query(HostelsModelEntity25).filter(HostelsModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: HostelsSchemaEntity25Create) -> HostelsModelEntity25:
        db_obj = HostelsModelEntity25(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_25(self, entity_id: int, payload: HostelsSchemaEntity25Update) -> Optional[HostelsModelEntity25]:
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

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity26]:
        return self.db.query(HostelsModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[HostelsModelEntity26]:
        return self.db.query(HostelsModelEntity26).filter(HostelsModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: HostelsSchemaEntity26Create) -> HostelsModelEntity26:
        db_obj = HostelsModelEntity26(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_26(self, entity_id: int, payload: HostelsSchemaEntity26Update) -> Optional[HostelsModelEntity26]:
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

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity27]:
        return self.db.query(HostelsModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[HostelsModelEntity27]:
        return self.db.query(HostelsModelEntity27).filter(HostelsModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: HostelsSchemaEntity27Create) -> HostelsModelEntity27:
        db_obj = HostelsModelEntity27(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_27(self, entity_id: int, payload: HostelsSchemaEntity27Update) -> Optional[HostelsModelEntity27]:
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

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity28]:
        return self.db.query(HostelsModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[HostelsModelEntity28]:
        return self.db.query(HostelsModelEntity28).filter(HostelsModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: HostelsSchemaEntity28Create) -> HostelsModelEntity28:
        db_obj = HostelsModelEntity28(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_28(self, entity_id: int, payload: HostelsSchemaEntity28Update) -> Optional[HostelsModelEntity28]:
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

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity29]:
        return self.db.query(HostelsModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[HostelsModelEntity29]:
        return self.db.query(HostelsModelEntity29).filter(HostelsModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: HostelsSchemaEntity29Create) -> HostelsModelEntity29:
        db_obj = HostelsModelEntity29(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_29(self, entity_id: int, payload: HostelsSchemaEntity29Update) -> Optional[HostelsModelEntity29]:
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

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity30]:
        return self.db.query(HostelsModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[HostelsModelEntity30]:
        return self.db.query(HostelsModelEntity30).filter(HostelsModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: HostelsSchemaEntity30Create) -> HostelsModelEntity30:
        db_obj = HostelsModelEntity30(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_30(self, entity_id: int, payload: HostelsSchemaEntity30Update) -> Optional[HostelsModelEntity30]:
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

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity31]:
        return self.db.query(HostelsModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[HostelsModelEntity31]:
        return self.db.query(HostelsModelEntity31).filter(HostelsModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: HostelsSchemaEntity31Create) -> HostelsModelEntity31:
        db_obj = HostelsModelEntity31(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_31(self, entity_id: int, payload: HostelsSchemaEntity31Update) -> Optional[HostelsModelEntity31]:
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

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity32]:
        return self.db.query(HostelsModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[HostelsModelEntity32]:
        return self.db.query(HostelsModelEntity32).filter(HostelsModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: HostelsSchemaEntity32Create) -> HostelsModelEntity32:
        db_obj = HostelsModelEntity32(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_32(self, entity_id: int, payload: HostelsSchemaEntity32Update) -> Optional[HostelsModelEntity32]:
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

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity33]:
        return self.db.query(HostelsModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[HostelsModelEntity33]:
        return self.db.query(HostelsModelEntity33).filter(HostelsModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: HostelsSchemaEntity33Create) -> HostelsModelEntity33:
        db_obj = HostelsModelEntity33(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_33(self, entity_id: int, payload: HostelsSchemaEntity33Update) -> Optional[HostelsModelEntity33]:
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

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity34]:
        return self.db.query(HostelsModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[HostelsModelEntity34]:
        return self.db.query(HostelsModelEntity34).filter(HostelsModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: HostelsSchemaEntity34Create) -> HostelsModelEntity34:
        db_obj = HostelsModelEntity34(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_34(self, entity_id: int, payload: HostelsSchemaEntity34Update) -> Optional[HostelsModelEntity34]:
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

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity35]:
        return self.db.query(HostelsModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[HostelsModelEntity35]:
        return self.db.query(HostelsModelEntity35).filter(HostelsModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: HostelsSchemaEntity35Create) -> HostelsModelEntity35:
        db_obj = HostelsModelEntity35(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_35(self, entity_id: int, payload: HostelsSchemaEntity35Update) -> Optional[HostelsModelEntity35]:
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

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity36]:
        return self.db.query(HostelsModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[HostelsModelEntity36]:
        return self.db.query(HostelsModelEntity36).filter(HostelsModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: HostelsSchemaEntity36Create) -> HostelsModelEntity36:
        db_obj = HostelsModelEntity36(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_36(self, entity_id: int, payload: HostelsSchemaEntity36Update) -> Optional[HostelsModelEntity36]:
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

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity37]:
        return self.db.query(HostelsModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[HostelsModelEntity37]:
        return self.db.query(HostelsModelEntity37).filter(HostelsModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: HostelsSchemaEntity37Create) -> HostelsModelEntity37:
        db_obj = HostelsModelEntity37(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_37(self, entity_id: int, payload: HostelsSchemaEntity37Update) -> Optional[HostelsModelEntity37]:
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

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity38]:
        return self.db.query(HostelsModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[HostelsModelEntity38]:
        return self.db.query(HostelsModelEntity38).filter(HostelsModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: HostelsSchemaEntity38Create) -> HostelsModelEntity38:
        db_obj = HostelsModelEntity38(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_38(self, entity_id: int, payload: HostelsSchemaEntity38Update) -> Optional[HostelsModelEntity38]:
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

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity39]:
        return self.db.query(HostelsModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[HostelsModelEntity39]:
        return self.db.query(HostelsModelEntity39).filter(HostelsModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: HostelsSchemaEntity39Create) -> HostelsModelEntity39:
        db_obj = HostelsModelEntity39(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_39(self, entity_id: int, payload: HostelsSchemaEntity39Update) -> Optional[HostelsModelEntity39]:
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

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity40]:
        return self.db.query(HostelsModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[HostelsModelEntity40]:
        return self.db.query(HostelsModelEntity40).filter(HostelsModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: HostelsSchemaEntity40Create) -> HostelsModelEntity40:
        db_obj = HostelsModelEntity40(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_40(self, entity_id: int, payload: HostelsSchemaEntity40Update) -> Optional[HostelsModelEntity40]:
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

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity41]:
        return self.db.query(HostelsModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[HostelsModelEntity41]:
        return self.db.query(HostelsModelEntity41).filter(HostelsModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: HostelsSchemaEntity41Create) -> HostelsModelEntity41:
        db_obj = HostelsModelEntity41(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_41(self, entity_id: int, payload: HostelsSchemaEntity41Update) -> Optional[HostelsModelEntity41]:
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

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity42]:
        return self.db.query(HostelsModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[HostelsModelEntity42]:
        return self.db.query(HostelsModelEntity42).filter(HostelsModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: HostelsSchemaEntity42Create) -> HostelsModelEntity42:
        db_obj = HostelsModelEntity42(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_42(self, entity_id: int, payload: HostelsSchemaEntity42Update) -> Optional[HostelsModelEntity42]:
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

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity43]:
        return self.db.query(HostelsModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[HostelsModelEntity43]:
        return self.db.query(HostelsModelEntity43).filter(HostelsModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: HostelsSchemaEntity43Create) -> HostelsModelEntity43:
        db_obj = HostelsModelEntity43(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_43(self, entity_id: int, payload: HostelsSchemaEntity43Update) -> Optional[HostelsModelEntity43]:
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

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity44]:
        return self.db.query(HostelsModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[HostelsModelEntity44]:
        return self.db.query(HostelsModelEntity44).filter(HostelsModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: HostelsSchemaEntity44Create) -> HostelsModelEntity44:
        db_obj = HostelsModelEntity44(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_44(self, entity_id: int, payload: HostelsSchemaEntity44Update) -> Optional[HostelsModelEntity44]:
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

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity45]:
        return self.db.query(HostelsModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[HostelsModelEntity45]:
        return self.db.query(HostelsModelEntity45).filter(HostelsModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: HostelsSchemaEntity45Create) -> HostelsModelEntity45:
        db_obj = HostelsModelEntity45(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_45(self, entity_id: int, payload: HostelsSchemaEntity45Update) -> Optional[HostelsModelEntity45]:
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

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity46]:
        return self.db.query(HostelsModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[HostelsModelEntity46]:
        return self.db.query(HostelsModelEntity46).filter(HostelsModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: HostelsSchemaEntity46Create) -> HostelsModelEntity46:
        db_obj = HostelsModelEntity46(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_46(self, entity_id: int, payload: HostelsSchemaEntity46Update) -> Optional[HostelsModelEntity46]:
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

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity47]:
        return self.db.query(HostelsModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[HostelsModelEntity47]:
        return self.db.query(HostelsModelEntity47).filter(HostelsModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: HostelsSchemaEntity47Create) -> HostelsModelEntity47:
        db_obj = HostelsModelEntity47(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_47(self, entity_id: int, payload: HostelsSchemaEntity47Update) -> Optional[HostelsModelEntity47]:
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

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity48]:
        return self.db.query(HostelsModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[HostelsModelEntity48]:
        return self.db.query(HostelsModelEntity48).filter(HostelsModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: HostelsSchemaEntity48Create) -> HostelsModelEntity48:
        db_obj = HostelsModelEntity48(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_48(self, entity_id: int, payload: HostelsSchemaEntity48Update) -> Optional[HostelsModelEntity48]:
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

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity49]:
        return self.db.query(HostelsModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[HostelsModelEntity49]:
        return self.db.query(HostelsModelEntity49).filter(HostelsModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: HostelsSchemaEntity49Create) -> HostelsModelEntity49:
        db_obj = HostelsModelEntity49(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_49(self, entity_id: int, payload: HostelsSchemaEntity49Update) -> Optional[HostelsModelEntity49]:
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

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity50]:
        return self.db.query(HostelsModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[HostelsModelEntity50]:
        return self.db.query(HostelsModelEntity50).filter(HostelsModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: HostelsSchemaEntity50Create) -> HostelsModelEntity50:
        db_obj = HostelsModelEntity50(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_50(self, entity_id: int, payload: HostelsSchemaEntity50Update) -> Optional[HostelsModelEntity50]:
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

    def get_entity_51_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity51]:
        return self.db.query(HostelsModelEntity51).offset(skip).limit(limit).all()

    def get_entity_51_by_id(self, entity_id: int) -> Optional[HostelsModelEntity51]:
        return self.db.query(HostelsModelEntity51).filter(HostelsModelEntity51.id == entity_id).first()

    def create_entity_51(self, payload: HostelsSchemaEntity51Create) -> HostelsModelEntity51:
        db_obj = HostelsModelEntity51(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_51(self, entity_id: int, payload: HostelsSchemaEntity51Update) -> Optional[HostelsModelEntity51]:
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

    def get_entity_52_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity52]:
        return self.db.query(HostelsModelEntity52).offset(skip).limit(limit).all()

    def get_entity_52_by_id(self, entity_id: int) -> Optional[HostelsModelEntity52]:
        return self.db.query(HostelsModelEntity52).filter(HostelsModelEntity52.id == entity_id).first()

    def create_entity_52(self, payload: HostelsSchemaEntity52Create) -> HostelsModelEntity52:
        db_obj = HostelsModelEntity52(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_52(self, entity_id: int, payload: HostelsSchemaEntity52Update) -> Optional[HostelsModelEntity52]:
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

    def get_entity_53_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity53]:
        return self.db.query(HostelsModelEntity53).offset(skip).limit(limit).all()

    def get_entity_53_by_id(self, entity_id: int) -> Optional[HostelsModelEntity53]:
        return self.db.query(HostelsModelEntity53).filter(HostelsModelEntity53.id == entity_id).first()

    def create_entity_53(self, payload: HostelsSchemaEntity53Create) -> HostelsModelEntity53:
        db_obj = HostelsModelEntity53(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_53(self, entity_id: int, payload: HostelsSchemaEntity53Update) -> Optional[HostelsModelEntity53]:
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

    def get_entity_54_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity54]:
        return self.db.query(HostelsModelEntity54).offset(skip).limit(limit).all()

    def get_entity_54_by_id(self, entity_id: int) -> Optional[HostelsModelEntity54]:
        return self.db.query(HostelsModelEntity54).filter(HostelsModelEntity54.id == entity_id).first()

    def create_entity_54(self, payload: HostelsSchemaEntity54Create) -> HostelsModelEntity54:
        db_obj = HostelsModelEntity54(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_54(self, entity_id: int, payload: HostelsSchemaEntity54Update) -> Optional[HostelsModelEntity54]:
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

    def get_entity_55_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity55]:
        return self.db.query(HostelsModelEntity55).offset(skip).limit(limit).all()

    def get_entity_55_by_id(self, entity_id: int) -> Optional[HostelsModelEntity55]:
        return self.db.query(HostelsModelEntity55).filter(HostelsModelEntity55.id == entity_id).first()

    def create_entity_55(self, payload: HostelsSchemaEntity55Create) -> HostelsModelEntity55:
        db_obj = HostelsModelEntity55(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_55(self, entity_id: int, payload: HostelsSchemaEntity55Update) -> Optional[HostelsModelEntity55]:
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

    def get_entity_56_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity56]:
        return self.db.query(HostelsModelEntity56).offset(skip).limit(limit).all()

    def get_entity_56_by_id(self, entity_id: int) -> Optional[HostelsModelEntity56]:
        return self.db.query(HostelsModelEntity56).filter(HostelsModelEntity56.id == entity_id).first()

    def create_entity_56(self, payload: HostelsSchemaEntity56Create) -> HostelsModelEntity56:
        db_obj = HostelsModelEntity56(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_56(self, entity_id: int, payload: HostelsSchemaEntity56Update) -> Optional[HostelsModelEntity56]:
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

    def get_entity_57_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity57]:
        return self.db.query(HostelsModelEntity57).offset(skip).limit(limit).all()

    def get_entity_57_by_id(self, entity_id: int) -> Optional[HostelsModelEntity57]:
        return self.db.query(HostelsModelEntity57).filter(HostelsModelEntity57.id == entity_id).first()

    def create_entity_57(self, payload: HostelsSchemaEntity57Create) -> HostelsModelEntity57:
        db_obj = HostelsModelEntity57(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_57(self, entity_id: int, payload: HostelsSchemaEntity57Update) -> Optional[HostelsModelEntity57]:
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

    def get_entity_58_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity58]:
        return self.db.query(HostelsModelEntity58).offset(skip).limit(limit).all()

    def get_entity_58_by_id(self, entity_id: int) -> Optional[HostelsModelEntity58]:
        return self.db.query(HostelsModelEntity58).filter(HostelsModelEntity58.id == entity_id).first()

    def create_entity_58(self, payload: HostelsSchemaEntity58Create) -> HostelsModelEntity58:
        db_obj = HostelsModelEntity58(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_58(self, entity_id: int, payload: HostelsSchemaEntity58Update) -> Optional[HostelsModelEntity58]:
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

    def get_entity_59_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity59]:
        return self.db.query(HostelsModelEntity59).offset(skip).limit(limit).all()

    def get_entity_59_by_id(self, entity_id: int) -> Optional[HostelsModelEntity59]:
        return self.db.query(HostelsModelEntity59).filter(HostelsModelEntity59.id == entity_id).first()

    def create_entity_59(self, payload: HostelsSchemaEntity59Create) -> HostelsModelEntity59:
        db_obj = HostelsModelEntity59(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_59(self, entity_id: int, payload: HostelsSchemaEntity59Update) -> Optional[HostelsModelEntity59]:
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

    def get_entity_60_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity60]:
        return self.db.query(HostelsModelEntity60).offset(skip).limit(limit).all()

    def get_entity_60_by_id(self, entity_id: int) -> Optional[HostelsModelEntity60]:
        return self.db.query(HostelsModelEntity60).filter(HostelsModelEntity60.id == entity_id).first()

    def create_entity_60(self, payload: HostelsSchemaEntity60Create) -> HostelsModelEntity60:
        db_obj = HostelsModelEntity60(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_60(self, entity_id: int, payload: HostelsSchemaEntity60Update) -> Optional[HostelsModelEntity60]:
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

    def get_entity_61_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity61]:
        return self.db.query(HostelsModelEntity61).offset(skip).limit(limit).all()

    def get_entity_61_by_id(self, entity_id: int) -> Optional[HostelsModelEntity61]:
        return self.db.query(HostelsModelEntity61).filter(HostelsModelEntity61.id == entity_id).first()

    def create_entity_61(self, payload: HostelsSchemaEntity61Create) -> HostelsModelEntity61:
        db_obj = HostelsModelEntity61(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_61(self, entity_id: int, payload: HostelsSchemaEntity61Update) -> Optional[HostelsModelEntity61]:
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

    def get_entity_62_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity62]:
        return self.db.query(HostelsModelEntity62).offset(skip).limit(limit).all()

    def get_entity_62_by_id(self, entity_id: int) -> Optional[HostelsModelEntity62]:
        return self.db.query(HostelsModelEntity62).filter(HostelsModelEntity62.id == entity_id).first()

    def create_entity_62(self, payload: HostelsSchemaEntity62Create) -> HostelsModelEntity62:
        db_obj = HostelsModelEntity62(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_62(self, entity_id: int, payload: HostelsSchemaEntity62Update) -> Optional[HostelsModelEntity62]:
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

    def get_entity_63_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity63]:
        return self.db.query(HostelsModelEntity63).offset(skip).limit(limit).all()

    def get_entity_63_by_id(self, entity_id: int) -> Optional[HostelsModelEntity63]:
        return self.db.query(HostelsModelEntity63).filter(HostelsModelEntity63.id == entity_id).first()

    def create_entity_63(self, payload: HostelsSchemaEntity63Create) -> HostelsModelEntity63:
        db_obj = HostelsModelEntity63(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_63(self, entity_id: int, payload: HostelsSchemaEntity63Update) -> Optional[HostelsModelEntity63]:
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

    def get_entity_64_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity64]:
        return self.db.query(HostelsModelEntity64).offset(skip).limit(limit).all()

    def get_entity_64_by_id(self, entity_id: int) -> Optional[HostelsModelEntity64]:
        return self.db.query(HostelsModelEntity64).filter(HostelsModelEntity64.id == entity_id).first()

    def create_entity_64(self, payload: HostelsSchemaEntity64Create) -> HostelsModelEntity64:
        db_obj = HostelsModelEntity64(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_64(self, entity_id: int, payload: HostelsSchemaEntity64Update) -> Optional[HostelsModelEntity64]:
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

    def get_entity_65_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity65]:
        return self.db.query(HostelsModelEntity65).offset(skip).limit(limit).all()

    def get_entity_65_by_id(self, entity_id: int) -> Optional[HostelsModelEntity65]:
        return self.db.query(HostelsModelEntity65).filter(HostelsModelEntity65.id == entity_id).first()

    def create_entity_65(self, payload: HostelsSchemaEntity65Create) -> HostelsModelEntity65:
        db_obj = HostelsModelEntity65(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_65(self, entity_id: int, payload: HostelsSchemaEntity65Update) -> Optional[HostelsModelEntity65]:
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

    def get_entity_66_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity66]:
        return self.db.query(HostelsModelEntity66).offset(skip).limit(limit).all()

    def get_entity_66_by_id(self, entity_id: int) -> Optional[HostelsModelEntity66]:
        return self.db.query(HostelsModelEntity66).filter(HostelsModelEntity66.id == entity_id).first()

    def create_entity_66(self, payload: HostelsSchemaEntity66Create) -> HostelsModelEntity66:
        db_obj = HostelsModelEntity66(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_66(self, entity_id: int, payload: HostelsSchemaEntity66Update) -> Optional[HostelsModelEntity66]:
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

    def get_entity_67_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity67]:
        return self.db.query(HostelsModelEntity67).offset(skip).limit(limit).all()

    def get_entity_67_by_id(self, entity_id: int) -> Optional[HostelsModelEntity67]:
        return self.db.query(HostelsModelEntity67).filter(HostelsModelEntity67.id == entity_id).first()

    def create_entity_67(self, payload: HostelsSchemaEntity67Create) -> HostelsModelEntity67:
        db_obj = HostelsModelEntity67(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_67(self, entity_id: int, payload: HostelsSchemaEntity67Update) -> Optional[HostelsModelEntity67]:
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

    def get_entity_68_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity68]:
        return self.db.query(HostelsModelEntity68).offset(skip).limit(limit).all()

    def get_entity_68_by_id(self, entity_id: int) -> Optional[HostelsModelEntity68]:
        return self.db.query(HostelsModelEntity68).filter(HostelsModelEntity68.id == entity_id).first()

    def create_entity_68(self, payload: HostelsSchemaEntity68Create) -> HostelsModelEntity68:
        db_obj = HostelsModelEntity68(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_68(self, entity_id: int, payload: HostelsSchemaEntity68Update) -> Optional[HostelsModelEntity68]:
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

    def get_entity_69_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity69]:
        return self.db.query(HostelsModelEntity69).offset(skip).limit(limit).all()

    def get_entity_69_by_id(self, entity_id: int) -> Optional[HostelsModelEntity69]:
        return self.db.query(HostelsModelEntity69).filter(HostelsModelEntity69.id == entity_id).first()

    def create_entity_69(self, payload: HostelsSchemaEntity69Create) -> HostelsModelEntity69:
        db_obj = HostelsModelEntity69(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_69(self, entity_id: int, payload: HostelsSchemaEntity69Update) -> Optional[HostelsModelEntity69]:
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

    def get_entity_70_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity70]:
        return self.db.query(HostelsModelEntity70).offset(skip).limit(limit).all()

    def get_entity_70_by_id(self, entity_id: int) -> Optional[HostelsModelEntity70]:
        return self.db.query(HostelsModelEntity70).filter(HostelsModelEntity70.id == entity_id).first()

    def create_entity_70(self, payload: HostelsSchemaEntity70Create) -> HostelsModelEntity70:
        db_obj = HostelsModelEntity70(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_70(self, entity_id: int, payload: HostelsSchemaEntity70Update) -> Optional[HostelsModelEntity70]:
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

    def get_entity_71_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity71]:
        return self.db.query(HostelsModelEntity71).offset(skip).limit(limit).all()

    def get_entity_71_by_id(self, entity_id: int) -> Optional[HostelsModelEntity71]:
        return self.db.query(HostelsModelEntity71).filter(HostelsModelEntity71.id == entity_id).first()

    def create_entity_71(self, payload: HostelsSchemaEntity71Create) -> HostelsModelEntity71:
        db_obj = HostelsModelEntity71(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_71(self, entity_id: int, payload: HostelsSchemaEntity71Update) -> Optional[HostelsModelEntity71]:
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

    def get_entity_72_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity72]:
        return self.db.query(HostelsModelEntity72).offset(skip).limit(limit).all()

    def get_entity_72_by_id(self, entity_id: int) -> Optional[HostelsModelEntity72]:
        return self.db.query(HostelsModelEntity72).filter(HostelsModelEntity72.id == entity_id).first()

    def create_entity_72(self, payload: HostelsSchemaEntity72Create) -> HostelsModelEntity72:
        db_obj = HostelsModelEntity72(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_72(self, entity_id: int, payload: HostelsSchemaEntity72Update) -> Optional[HostelsModelEntity72]:
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

    def get_entity_73_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity73]:
        return self.db.query(HostelsModelEntity73).offset(skip).limit(limit).all()

    def get_entity_73_by_id(self, entity_id: int) -> Optional[HostelsModelEntity73]:
        return self.db.query(HostelsModelEntity73).filter(HostelsModelEntity73.id == entity_id).first()

    def create_entity_73(self, payload: HostelsSchemaEntity73Create) -> HostelsModelEntity73:
        db_obj = HostelsModelEntity73(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_73(self, entity_id: int, payload: HostelsSchemaEntity73Update) -> Optional[HostelsModelEntity73]:
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

    def get_entity_74_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity74]:
        return self.db.query(HostelsModelEntity74).offset(skip).limit(limit).all()

    def get_entity_74_by_id(self, entity_id: int) -> Optional[HostelsModelEntity74]:
        return self.db.query(HostelsModelEntity74).filter(HostelsModelEntity74.id == entity_id).first()

    def create_entity_74(self, payload: HostelsSchemaEntity74Create) -> HostelsModelEntity74:
        db_obj = HostelsModelEntity74(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_74(self, entity_id: int, payload: HostelsSchemaEntity74Update) -> Optional[HostelsModelEntity74]:
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

    def get_entity_75_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity75]:
        return self.db.query(HostelsModelEntity75).offset(skip).limit(limit).all()

    def get_entity_75_by_id(self, entity_id: int) -> Optional[HostelsModelEntity75]:
        return self.db.query(HostelsModelEntity75).filter(HostelsModelEntity75.id == entity_id).first()

    def create_entity_75(self, payload: HostelsSchemaEntity75Create) -> HostelsModelEntity75:
        db_obj = HostelsModelEntity75(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_75(self, entity_id: int, payload: HostelsSchemaEntity75Update) -> Optional[HostelsModelEntity75]:
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

    def get_entity_76_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity76]:
        return self.db.query(HostelsModelEntity76).offset(skip).limit(limit).all()

    def get_entity_76_by_id(self, entity_id: int) -> Optional[HostelsModelEntity76]:
        return self.db.query(HostelsModelEntity76).filter(HostelsModelEntity76.id == entity_id).first()

    def create_entity_76(self, payload: HostelsSchemaEntity76Create) -> HostelsModelEntity76:
        db_obj = HostelsModelEntity76(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_76(self, entity_id: int, payload: HostelsSchemaEntity76Update) -> Optional[HostelsModelEntity76]:
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

    def get_entity_77_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity77]:
        return self.db.query(HostelsModelEntity77).offset(skip).limit(limit).all()

    def get_entity_77_by_id(self, entity_id: int) -> Optional[HostelsModelEntity77]:
        return self.db.query(HostelsModelEntity77).filter(HostelsModelEntity77.id == entity_id).first()

    def create_entity_77(self, payload: HostelsSchemaEntity77Create) -> HostelsModelEntity77:
        db_obj = HostelsModelEntity77(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_77(self, entity_id: int, payload: HostelsSchemaEntity77Update) -> Optional[HostelsModelEntity77]:
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

    def get_entity_78_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity78]:
        return self.db.query(HostelsModelEntity78).offset(skip).limit(limit).all()

    def get_entity_78_by_id(self, entity_id: int) -> Optional[HostelsModelEntity78]:
        return self.db.query(HostelsModelEntity78).filter(HostelsModelEntity78.id == entity_id).first()

    def create_entity_78(self, payload: HostelsSchemaEntity78Create) -> HostelsModelEntity78:
        db_obj = HostelsModelEntity78(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_78(self, entity_id: int, payload: HostelsSchemaEntity78Update) -> Optional[HostelsModelEntity78]:
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

    def get_entity_79_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity79]:
        return self.db.query(HostelsModelEntity79).offset(skip).limit(limit).all()

    def get_entity_79_by_id(self, entity_id: int) -> Optional[HostelsModelEntity79]:
        return self.db.query(HostelsModelEntity79).filter(HostelsModelEntity79.id == entity_id).first()

    def create_entity_79(self, payload: HostelsSchemaEntity79Create) -> HostelsModelEntity79:
        db_obj = HostelsModelEntity79(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_79(self, entity_id: int, payload: HostelsSchemaEntity79Update) -> Optional[HostelsModelEntity79]:
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

    def get_entity_80_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity80]:
        return self.db.query(HostelsModelEntity80).offset(skip).limit(limit).all()

    def get_entity_80_by_id(self, entity_id: int) -> Optional[HostelsModelEntity80]:
        return self.db.query(HostelsModelEntity80).filter(HostelsModelEntity80.id == entity_id).first()

    def create_entity_80(self, payload: HostelsSchemaEntity80Create) -> HostelsModelEntity80:
        db_obj = HostelsModelEntity80(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_80(self, entity_id: int, payload: HostelsSchemaEntity80Update) -> Optional[HostelsModelEntity80]:
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

    def get_entity_81_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity81]:
        return self.db.query(HostelsModelEntity81).offset(skip).limit(limit).all()

    def get_entity_81_by_id(self, entity_id: int) -> Optional[HostelsModelEntity81]:
        return self.db.query(HostelsModelEntity81).filter(HostelsModelEntity81.id == entity_id).first()

    def create_entity_81(self, payload: HostelsSchemaEntity81Create) -> HostelsModelEntity81:
        db_obj = HostelsModelEntity81(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_81(self, entity_id: int, payload: HostelsSchemaEntity81Update) -> Optional[HostelsModelEntity81]:
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

    def get_entity_82_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity82]:
        return self.db.query(HostelsModelEntity82).offset(skip).limit(limit).all()

    def get_entity_82_by_id(self, entity_id: int) -> Optional[HostelsModelEntity82]:
        return self.db.query(HostelsModelEntity82).filter(HostelsModelEntity82.id == entity_id).first()

    def create_entity_82(self, payload: HostelsSchemaEntity82Create) -> HostelsModelEntity82:
        db_obj = HostelsModelEntity82(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_82(self, entity_id: int, payload: HostelsSchemaEntity82Update) -> Optional[HostelsModelEntity82]:
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

    def get_entity_83_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity83]:
        return self.db.query(HostelsModelEntity83).offset(skip).limit(limit).all()

    def get_entity_83_by_id(self, entity_id: int) -> Optional[HostelsModelEntity83]:
        return self.db.query(HostelsModelEntity83).filter(HostelsModelEntity83.id == entity_id).first()

    def create_entity_83(self, payload: HostelsSchemaEntity83Create) -> HostelsModelEntity83:
        db_obj = HostelsModelEntity83(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_83(self, entity_id: int, payload: HostelsSchemaEntity83Update) -> Optional[HostelsModelEntity83]:
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

    def get_entity_84_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity84]:
        return self.db.query(HostelsModelEntity84).offset(skip).limit(limit).all()

    def get_entity_84_by_id(self, entity_id: int) -> Optional[HostelsModelEntity84]:
        return self.db.query(HostelsModelEntity84).filter(HostelsModelEntity84.id == entity_id).first()

    def create_entity_84(self, payload: HostelsSchemaEntity84Create) -> HostelsModelEntity84:
        db_obj = HostelsModelEntity84(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_84(self, entity_id: int, payload: HostelsSchemaEntity84Update) -> Optional[HostelsModelEntity84]:
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

    def get_entity_85_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity85]:
        return self.db.query(HostelsModelEntity85).offset(skip).limit(limit).all()

    def get_entity_85_by_id(self, entity_id: int) -> Optional[HostelsModelEntity85]:
        return self.db.query(HostelsModelEntity85).filter(HostelsModelEntity85.id == entity_id).first()

    def create_entity_85(self, payload: HostelsSchemaEntity85Create) -> HostelsModelEntity85:
        db_obj = HostelsModelEntity85(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_85(self, entity_id: int, payload: HostelsSchemaEntity85Update) -> Optional[HostelsModelEntity85]:
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

    def get_entity_86_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity86]:
        return self.db.query(HostelsModelEntity86).offset(skip).limit(limit).all()

    def get_entity_86_by_id(self, entity_id: int) -> Optional[HostelsModelEntity86]:
        return self.db.query(HostelsModelEntity86).filter(HostelsModelEntity86.id == entity_id).first()

    def create_entity_86(self, payload: HostelsSchemaEntity86Create) -> HostelsModelEntity86:
        db_obj = HostelsModelEntity86(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_86(self, entity_id: int, payload: HostelsSchemaEntity86Update) -> Optional[HostelsModelEntity86]:
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

    def get_entity_87_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity87]:
        return self.db.query(HostelsModelEntity87).offset(skip).limit(limit).all()

    def get_entity_87_by_id(self, entity_id: int) -> Optional[HostelsModelEntity87]:
        return self.db.query(HostelsModelEntity87).filter(HostelsModelEntity87.id == entity_id).first()

    def create_entity_87(self, payload: HostelsSchemaEntity87Create) -> HostelsModelEntity87:
        db_obj = HostelsModelEntity87(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_87(self, entity_id: int, payload: HostelsSchemaEntity87Update) -> Optional[HostelsModelEntity87]:
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

    def get_entity_88_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity88]:
        return self.db.query(HostelsModelEntity88).offset(skip).limit(limit).all()

    def get_entity_88_by_id(self, entity_id: int) -> Optional[HostelsModelEntity88]:
        return self.db.query(HostelsModelEntity88).filter(HostelsModelEntity88.id == entity_id).first()

    def create_entity_88(self, payload: HostelsSchemaEntity88Create) -> HostelsModelEntity88:
        db_obj = HostelsModelEntity88(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_88(self, entity_id: int, payload: HostelsSchemaEntity88Update) -> Optional[HostelsModelEntity88]:
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

    def get_entity_89_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity89]:
        return self.db.query(HostelsModelEntity89).offset(skip).limit(limit).all()

    def get_entity_89_by_id(self, entity_id: int) -> Optional[HostelsModelEntity89]:
        return self.db.query(HostelsModelEntity89).filter(HostelsModelEntity89.id == entity_id).first()

    def create_entity_89(self, payload: HostelsSchemaEntity89Create) -> HostelsModelEntity89:
        db_obj = HostelsModelEntity89(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_89(self, entity_id: int, payload: HostelsSchemaEntity89Update) -> Optional[HostelsModelEntity89]:
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

    def get_entity_90_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity90]:
        return self.db.query(HostelsModelEntity90).offset(skip).limit(limit).all()

    def get_entity_90_by_id(self, entity_id: int) -> Optional[HostelsModelEntity90]:
        return self.db.query(HostelsModelEntity90).filter(HostelsModelEntity90.id == entity_id).first()

    def create_entity_90(self, payload: HostelsSchemaEntity90Create) -> HostelsModelEntity90:
        db_obj = HostelsModelEntity90(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_90(self, entity_id: int, payload: HostelsSchemaEntity90Update) -> Optional[HostelsModelEntity90]:
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

    def get_entity_91_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity91]:
        return self.db.query(HostelsModelEntity91).offset(skip).limit(limit).all()

    def get_entity_91_by_id(self, entity_id: int) -> Optional[HostelsModelEntity91]:
        return self.db.query(HostelsModelEntity91).filter(HostelsModelEntity91.id == entity_id).first()

    def create_entity_91(self, payload: HostelsSchemaEntity91Create) -> HostelsModelEntity91:
        db_obj = HostelsModelEntity91(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_91(self, entity_id: int, payload: HostelsSchemaEntity91Update) -> Optional[HostelsModelEntity91]:
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

    def get_entity_92_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity92]:
        return self.db.query(HostelsModelEntity92).offset(skip).limit(limit).all()

    def get_entity_92_by_id(self, entity_id: int) -> Optional[HostelsModelEntity92]:
        return self.db.query(HostelsModelEntity92).filter(HostelsModelEntity92.id == entity_id).first()

    def create_entity_92(self, payload: HostelsSchemaEntity92Create) -> HostelsModelEntity92:
        db_obj = HostelsModelEntity92(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_92(self, entity_id: int, payload: HostelsSchemaEntity92Update) -> Optional[HostelsModelEntity92]:
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

    def get_entity_93_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity93]:
        return self.db.query(HostelsModelEntity93).offset(skip).limit(limit).all()

    def get_entity_93_by_id(self, entity_id: int) -> Optional[HostelsModelEntity93]:
        return self.db.query(HostelsModelEntity93).filter(HostelsModelEntity93.id == entity_id).first()

    def create_entity_93(self, payload: HostelsSchemaEntity93Create) -> HostelsModelEntity93:
        db_obj = HostelsModelEntity93(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_93(self, entity_id: int, payload: HostelsSchemaEntity93Update) -> Optional[HostelsModelEntity93]:
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

    def get_entity_94_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity94]:
        return self.db.query(HostelsModelEntity94).offset(skip).limit(limit).all()

    def get_entity_94_by_id(self, entity_id: int) -> Optional[HostelsModelEntity94]:
        return self.db.query(HostelsModelEntity94).filter(HostelsModelEntity94.id == entity_id).first()

    def create_entity_94(self, payload: HostelsSchemaEntity94Create) -> HostelsModelEntity94:
        db_obj = HostelsModelEntity94(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_94(self, entity_id: int, payload: HostelsSchemaEntity94Update) -> Optional[HostelsModelEntity94]:
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

    def get_entity_95_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity95]:
        return self.db.query(HostelsModelEntity95).offset(skip).limit(limit).all()

    def get_entity_95_by_id(self, entity_id: int) -> Optional[HostelsModelEntity95]:
        return self.db.query(HostelsModelEntity95).filter(HostelsModelEntity95.id == entity_id).first()

    def create_entity_95(self, payload: HostelsSchemaEntity95Create) -> HostelsModelEntity95:
        db_obj = HostelsModelEntity95(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_95(self, entity_id: int, payload: HostelsSchemaEntity95Update) -> Optional[HostelsModelEntity95]:
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

    def get_entity_96_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity96]:
        return self.db.query(HostelsModelEntity96).offset(skip).limit(limit).all()

    def get_entity_96_by_id(self, entity_id: int) -> Optional[HostelsModelEntity96]:
        return self.db.query(HostelsModelEntity96).filter(HostelsModelEntity96.id == entity_id).first()

    def create_entity_96(self, payload: HostelsSchemaEntity96Create) -> HostelsModelEntity96:
        db_obj = HostelsModelEntity96(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_96(self, entity_id: int, payload: HostelsSchemaEntity96Update) -> Optional[HostelsModelEntity96]:
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

    def get_entity_97_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity97]:
        return self.db.query(HostelsModelEntity97).offset(skip).limit(limit).all()

    def get_entity_97_by_id(self, entity_id: int) -> Optional[HostelsModelEntity97]:
        return self.db.query(HostelsModelEntity97).filter(HostelsModelEntity97.id == entity_id).first()

    def create_entity_97(self, payload: HostelsSchemaEntity97Create) -> HostelsModelEntity97:
        db_obj = HostelsModelEntity97(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_97(self, entity_id: int, payload: HostelsSchemaEntity97Update) -> Optional[HostelsModelEntity97]:
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

    def get_entity_98_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity98]:
        return self.db.query(HostelsModelEntity98).offset(skip).limit(limit).all()

    def get_entity_98_by_id(self, entity_id: int) -> Optional[HostelsModelEntity98]:
        return self.db.query(HostelsModelEntity98).filter(HostelsModelEntity98.id == entity_id).first()

    def create_entity_98(self, payload: HostelsSchemaEntity98Create) -> HostelsModelEntity98:
        db_obj = HostelsModelEntity98(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_98(self, entity_id: int, payload: HostelsSchemaEntity98Update) -> Optional[HostelsModelEntity98]:
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

    def get_entity_99_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity99]:
        return self.db.query(HostelsModelEntity99).offset(skip).limit(limit).all()

    def get_entity_99_by_id(self, entity_id: int) -> Optional[HostelsModelEntity99]:
        return self.db.query(HostelsModelEntity99).filter(HostelsModelEntity99.id == entity_id).first()

    def create_entity_99(self, payload: HostelsSchemaEntity99Create) -> HostelsModelEntity99:
        db_obj = HostelsModelEntity99(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_99(self, entity_id: int, payload: HostelsSchemaEntity99Update) -> Optional[HostelsModelEntity99]:
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

    def get_entity_100_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity100]:
        return self.db.query(HostelsModelEntity100).offset(skip).limit(limit).all()

    def get_entity_100_by_id(self, entity_id: int) -> Optional[HostelsModelEntity100]:
        return self.db.query(HostelsModelEntity100).filter(HostelsModelEntity100.id == entity_id).first()

    def create_entity_100(self, payload: HostelsSchemaEntity100Create) -> HostelsModelEntity100:
        db_obj = HostelsModelEntity100(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_100(self, entity_id: int, payload: HostelsSchemaEntity100Update) -> Optional[HostelsModelEntity100]:
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

    def get_entity_101_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity101]:
        return self.db.query(HostelsModelEntity101).offset(skip).limit(limit).all()

    def get_entity_101_by_id(self, entity_id: int) -> Optional[HostelsModelEntity101]:
        return self.db.query(HostelsModelEntity101).filter(HostelsModelEntity101.id == entity_id).first()

    def create_entity_101(self, payload: HostelsSchemaEntity101Create) -> HostelsModelEntity101:
        db_obj = HostelsModelEntity101(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_101(self, entity_id: int, payload: HostelsSchemaEntity101Update) -> Optional[HostelsModelEntity101]:
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

    def get_entity_102_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity102]:
        return self.db.query(HostelsModelEntity102).offset(skip).limit(limit).all()

    def get_entity_102_by_id(self, entity_id: int) -> Optional[HostelsModelEntity102]:
        return self.db.query(HostelsModelEntity102).filter(HostelsModelEntity102.id == entity_id).first()

    def create_entity_102(self, payload: HostelsSchemaEntity102Create) -> HostelsModelEntity102:
        db_obj = HostelsModelEntity102(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_102(self, entity_id: int, payload: HostelsSchemaEntity102Update) -> Optional[HostelsModelEntity102]:
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

    def get_entity_103_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity103]:
        return self.db.query(HostelsModelEntity103).offset(skip).limit(limit).all()

    def get_entity_103_by_id(self, entity_id: int) -> Optional[HostelsModelEntity103]:
        return self.db.query(HostelsModelEntity103).filter(HostelsModelEntity103.id == entity_id).first()

    def create_entity_103(self, payload: HostelsSchemaEntity103Create) -> HostelsModelEntity103:
        db_obj = HostelsModelEntity103(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_103(self, entity_id: int, payload: HostelsSchemaEntity103Update) -> Optional[HostelsModelEntity103]:
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

    def get_entity_104_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity104]:
        return self.db.query(HostelsModelEntity104).offset(skip).limit(limit).all()

    def get_entity_104_by_id(self, entity_id: int) -> Optional[HostelsModelEntity104]:
        return self.db.query(HostelsModelEntity104).filter(HostelsModelEntity104.id == entity_id).first()

    def create_entity_104(self, payload: HostelsSchemaEntity104Create) -> HostelsModelEntity104:
        db_obj = HostelsModelEntity104(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_104(self, entity_id: int, payload: HostelsSchemaEntity104Update) -> Optional[HostelsModelEntity104]:
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

    def get_entity_105_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity105]:
        return self.db.query(HostelsModelEntity105).offset(skip).limit(limit).all()

    def get_entity_105_by_id(self, entity_id: int) -> Optional[HostelsModelEntity105]:
        return self.db.query(HostelsModelEntity105).filter(HostelsModelEntity105.id == entity_id).first()

    def create_entity_105(self, payload: HostelsSchemaEntity105Create) -> HostelsModelEntity105:
        db_obj = HostelsModelEntity105(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_105(self, entity_id: int, payload: HostelsSchemaEntity105Update) -> Optional[HostelsModelEntity105]:
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

    def get_entity_106_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity106]:
        return self.db.query(HostelsModelEntity106).offset(skip).limit(limit).all()

    def get_entity_106_by_id(self, entity_id: int) -> Optional[HostelsModelEntity106]:
        return self.db.query(HostelsModelEntity106).filter(HostelsModelEntity106.id == entity_id).first()

    def create_entity_106(self, payload: HostelsSchemaEntity106Create) -> HostelsModelEntity106:
        db_obj = HostelsModelEntity106(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_106(self, entity_id: int, payload: HostelsSchemaEntity106Update) -> Optional[HostelsModelEntity106]:
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

    def get_entity_107_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity107]:
        return self.db.query(HostelsModelEntity107).offset(skip).limit(limit).all()

    def get_entity_107_by_id(self, entity_id: int) -> Optional[HostelsModelEntity107]:
        return self.db.query(HostelsModelEntity107).filter(HostelsModelEntity107.id == entity_id).first()

    def create_entity_107(self, payload: HostelsSchemaEntity107Create) -> HostelsModelEntity107:
        db_obj = HostelsModelEntity107(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_107(self, entity_id: int, payload: HostelsSchemaEntity107Update) -> Optional[HostelsModelEntity107]:
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

    def get_entity_108_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity108]:
        return self.db.query(HostelsModelEntity108).offset(skip).limit(limit).all()

    def get_entity_108_by_id(self, entity_id: int) -> Optional[HostelsModelEntity108]:
        return self.db.query(HostelsModelEntity108).filter(HostelsModelEntity108.id == entity_id).first()

    def create_entity_108(self, payload: HostelsSchemaEntity108Create) -> HostelsModelEntity108:
        db_obj = HostelsModelEntity108(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_108(self, entity_id: int, payload: HostelsSchemaEntity108Update) -> Optional[HostelsModelEntity108]:
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

    def get_entity_109_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity109]:
        return self.db.query(HostelsModelEntity109).offset(skip).limit(limit).all()

    def get_entity_109_by_id(self, entity_id: int) -> Optional[HostelsModelEntity109]:
        return self.db.query(HostelsModelEntity109).filter(HostelsModelEntity109.id == entity_id).first()

    def create_entity_109(self, payload: HostelsSchemaEntity109Create) -> HostelsModelEntity109:
        db_obj = HostelsModelEntity109(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_109(self, entity_id: int, payload: HostelsSchemaEntity109Update) -> Optional[HostelsModelEntity109]:
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

    def get_entity_110_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity110]:
        return self.db.query(HostelsModelEntity110).offset(skip).limit(limit).all()

    def get_entity_110_by_id(self, entity_id: int) -> Optional[HostelsModelEntity110]:
        return self.db.query(HostelsModelEntity110).filter(HostelsModelEntity110.id == entity_id).first()

    def create_entity_110(self, payload: HostelsSchemaEntity110Create) -> HostelsModelEntity110:
        db_obj = HostelsModelEntity110(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_110(self, entity_id: int, payload: HostelsSchemaEntity110Update) -> Optional[HostelsModelEntity110]:
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

    def get_entity_111_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity111]:
        return self.db.query(HostelsModelEntity111).offset(skip).limit(limit).all()

    def get_entity_111_by_id(self, entity_id: int) -> Optional[HostelsModelEntity111]:
        return self.db.query(HostelsModelEntity111).filter(HostelsModelEntity111.id == entity_id).first()

    def create_entity_111(self, payload: HostelsSchemaEntity111Create) -> HostelsModelEntity111:
        db_obj = HostelsModelEntity111(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_111(self, entity_id: int, payload: HostelsSchemaEntity111Update) -> Optional[HostelsModelEntity111]:
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

    def get_entity_112_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity112]:
        return self.db.query(HostelsModelEntity112).offset(skip).limit(limit).all()

    def get_entity_112_by_id(self, entity_id: int) -> Optional[HostelsModelEntity112]:
        return self.db.query(HostelsModelEntity112).filter(HostelsModelEntity112.id == entity_id).first()

    def create_entity_112(self, payload: HostelsSchemaEntity112Create) -> HostelsModelEntity112:
        db_obj = HostelsModelEntity112(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_112(self, entity_id: int, payload: HostelsSchemaEntity112Update) -> Optional[HostelsModelEntity112]:
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

    def get_entity_113_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity113]:
        return self.db.query(HostelsModelEntity113).offset(skip).limit(limit).all()

    def get_entity_113_by_id(self, entity_id: int) -> Optional[HostelsModelEntity113]:
        return self.db.query(HostelsModelEntity113).filter(HostelsModelEntity113.id == entity_id).first()

    def create_entity_113(self, payload: HostelsSchemaEntity113Create) -> HostelsModelEntity113:
        db_obj = HostelsModelEntity113(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_113(self, entity_id: int, payload: HostelsSchemaEntity113Update) -> Optional[HostelsModelEntity113]:
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

    def get_entity_114_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity114]:
        return self.db.query(HostelsModelEntity114).offset(skip).limit(limit).all()

    def get_entity_114_by_id(self, entity_id: int) -> Optional[HostelsModelEntity114]:
        return self.db.query(HostelsModelEntity114).filter(HostelsModelEntity114.id == entity_id).first()

    def create_entity_114(self, payload: HostelsSchemaEntity114Create) -> HostelsModelEntity114:
        db_obj = HostelsModelEntity114(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_114(self, entity_id: int, payload: HostelsSchemaEntity114Update) -> Optional[HostelsModelEntity114]:
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

    def get_entity_115_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity115]:
        return self.db.query(HostelsModelEntity115).offset(skip).limit(limit).all()

    def get_entity_115_by_id(self, entity_id: int) -> Optional[HostelsModelEntity115]:
        return self.db.query(HostelsModelEntity115).filter(HostelsModelEntity115.id == entity_id).first()

    def create_entity_115(self, payload: HostelsSchemaEntity115Create) -> HostelsModelEntity115:
        db_obj = HostelsModelEntity115(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_115(self, entity_id: int, payload: HostelsSchemaEntity115Update) -> Optional[HostelsModelEntity115]:
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

    def get_entity_116_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity116]:
        return self.db.query(HostelsModelEntity116).offset(skip).limit(limit).all()

    def get_entity_116_by_id(self, entity_id: int) -> Optional[HostelsModelEntity116]:
        return self.db.query(HostelsModelEntity116).filter(HostelsModelEntity116.id == entity_id).first()

    def create_entity_116(self, payload: HostelsSchemaEntity116Create) -> HostelsModelEntity116:
        db_obj = HostelsModelEntity116(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_116(self, entity_id: int, payload: HostelsSchemaEntity116Update) -> Optional[HostelsModelEntity116]:
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

    def get_entity_117_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity117]:
        return self.db.query(HostelsModelEntity117).offset(skip).limit(limit).all()

    def get_entity_117_by_id(self, entity_id: int) -> Optional[HostelsModelEntity117]:
        return self.db.query(HostelsModelEntity117).filter(HostelsModelEntity117.id == entity_id).first()

    def create_entity_117(self, payload: HostelsSchemaEntity117Create) -> HostelsModelEntity117:
        db_obj = HostelsModelEntity117(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_117(self, entity_id: int, payload: HostelsSchemaEntity117Update) -> Optional[HostelsModelEntity117]:
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

    def get_entity_118_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity118]:
        return self.db.query(HostelsModelEntity118).offset(skip).limit(limit).all()

    def get_entity_118_by_id(self, entity_id: int) -> Optional[HostelsModelEntity118]:
        return self.db.query(HostelsModelEntity118).filter(HostelsModelEntity118.id == entity_id).first()

    def create_entity_118(self, payload: HostelsSchemaEntity118Create) -> HostelsModelEntity118:
        db_obj = HostelsModelEntity118(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_118(self, entity_id: int, payload: HostelsSchemaEntity118Update) -> Optional[HostelsModelEntity118]:
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

    def get_entity_119_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity119]:
        return self.db.query(HostelsModelEntity119).offset(skip).limit(limit).all()

    def get_entity_119_by_id(self, entity_id: int) -> Optional[HostelsModelEntity119]:
        return self.db.query(HostelsModelEntity119).filter(HostelsModelEntity119.id == entity_id).first()

    def create_entity_119(self, payload: HostelsSchemaEntity119Create) -> HostelsModelEntity119:
        db_obj = HostelsModelEntity119(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_119(self, entity_id: int, payload: HostelsSchemaEntity119Update) -> Optional[HostelsModelEntity119]:
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

    def get_entity_120_list(self, skip: int = 0, limit: int = 100) -> List[HostelsModelEntity120]:
        return self.db.query(HostelsModelEntity120).offset(skip).limit(limit).all()

    def get_entity_120_by_id(self, entity_id: int) -> Optional[HostelsModelEntity120]:
        return self.db.query(HostelsModelEntity120).filter(HostelsModelEntity120.id == entity_id).first()

    def create_entity_120(self, payload: HostelsSchemaEntity120Create) -> HostelsModelEntity120:
        db_obj = HostelsModelEntity120(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_120(self, entity_id: int, payload: HostelsSchemaEntity120Update) -> Optional[HostelsModelEntity120]:
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

