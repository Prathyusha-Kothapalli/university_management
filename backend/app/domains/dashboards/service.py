"""
Executive & Departmental Dashboards - Service Business Logic Layer
Module: app.domains.dashboards.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.dashboards.models import *
from app.domains.dashboards.schemas import *

class DashboardsDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity1]:
        return self.db.query(DashboardsModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity1]:
        return self.db.query(DashboardsModelEntity1).filter(DashboardsModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: DashboardsSchemaEntity1Create) -> DashboardsModelEntity1:
        db_obj = DashboardsModelEntity1(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_1(self, entity_id: int, payload: DashboardsSchemaEntity1Update) -> Optional[DashboardsModelEntity1]:
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

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity2]:
        return self.db.query(DashboardsModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity2]:
        return self.db.query(DashboardsModelEntity2).filter(DashboardsModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: DashboardsSchemaEntity2Create) -> DashboardsModelEntity2:
        db_obj = DashboardsModelEntity2(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_2(self, entity_id: int, payload: DashboardsSchemaEntity2Update) -> Optional[DashboardsModelEntity2]:
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

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity3]:
        return self.db.query(DashboardsModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity3]:
        return self.db.query(DashboardsModelEntity3).filter(DashboardsModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: DashboardsSchemaEntity3Create) -> DashboardsModelEntity3:
        db_obj = DashboardsModelEntity3(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_3(self, entity_id: int, payload: DashboardsSchemaEntity3Update) -> Optional[DashboardsModelEntity3]:
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

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity4]:
        return self.db.query(DashboardsModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity4]:
        return self.db.query(DashboardsModelEntity4).filter(DashboardsModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: DashboardsSchemaEntity4Create) -> DashboardsModelEntity4:
        db_obj = DashboardsModelEntity4(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_4(self, entity_id: int, payload: DashboardsSchemaEntity4Update) -> Optional[DashboardsModelEntity4]:
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

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity5]:
        return self.db.query(DashboardsModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity5]:
        return self.db.query(DashboardsModelEntity5).filter(DashboardsModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: DashboardsSchemaEntity5Create) -> DashboardsModelEntity5:
        db_obj = DashboardsModelEntity5(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_5(self, entity_id: int, payload: DashboardsSchemaEntity5Update) -> Optional[DashboardsModelEntity5]:
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

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity6]:
        return self.db.query(DashboardsModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity6]:
        return self.db.query(DashboardsModelEntity6).filter(DashboardsModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: DashboardsSchemaEntity6Create) -> DashboardsModelEntity6:
        db_obj = DashboardsModelEntity6(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_6(self, entity_id: int, payload: DashboardsSchemaEntity6Update) -> Optional[DashboardsModelEntity6]:
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

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity7]:
        return self.db.query(DashboardsModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity7]:
        return self.db.query(DashboardsModelEntity7).filter(DashboardsModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: DashboardsSchemaEntity7Create) -> DashboardsModelEntity7:
        db_obj = DashboardsModelEntity7(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_7(self, entity_id: int, payload: DashboardsSchemaEntity7Update) -> Optional[DashboardsModelEntity7]:
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

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity8]:
        return self.db.query(DashboardsModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity8]:
        return self.db.query(DashboardsModelEntity8).filter(DashboardsModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: DashboardsSchemaEntity8Create) -> DashboardsModelEntity8:
        db_obj = DashboardsModelEntity8(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_8(self, entity_id: int, payload: DashboardsSchemaEntity8Update) -> Optional[DashboardsModelEntity8]:
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

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity9]:
        return self.db.query(DashboardsModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity9]:
        return self.db.query(DashboardsModelEntity9).filter(DashboardsModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: DashboardsSchemaEntity9Create) -> DashboardsModelEntity9:
        db_obj = DashboardsModelEntity9(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_9(self, entity_id: int, payload: DashboardsSchemaEntity9Update) -> Optional[DashboardsModelEntity9]:
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

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity10]:
        return self.db.query(DashboardsModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity10]:
        return self.db.query(DashboardsModelEntity10).filter(DashboardsModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: DashboardsSchemaEntity10Create) -> DashboardsModelEntity10:
        db_obj = DashboardsModelEntity10(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_10(self, entity_id: int, payload: DashboardsSchemaEntity10Update) -> Optional[DashboardsModelEntity10]:
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

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity11]:
        return self.db.query(DashboardsModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity11]:
        return self.db.query(DashboardsModelEntity11).filter(DashboardsModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: DashboardsSchemaEntity11Create) -> DashboardsModelEntity11:
        db_obj = DashboardsModelEntity11(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_11(self, entity_id: int, payload: DashboardsSchemaEntity11Update) -> Optional[DashboardsModelEntity11]:
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

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity12]:
        return self.db.query(DashboardsModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity12]:
        return self.db.query(DashboardsModelEntity12).filter(DashboardsModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: DashboardsSchemaEntity12Create) -> DashboardsModelEntity12:
        db_obj = DashboardsModelEntity12(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_12(self, entity_id: int, payload: DashboardsSchemaEntity12Update) -> Optional[DashboardsModelEntity12]:
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

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity13]:
        return self.db.query(DashboardsModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity13]:
        return self.db.query(DashboardsModelEntity13).filter(DashboardsModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: DashboardsSchemaEntity13Create) -> DashboardsModelEntity13:
        db_obj = DashboardsModelEntity13(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_13(self, entity_id: int, payload: DashboardsSchemaEntity13Update) -> Optional[DashboardsModelEntity13]:
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

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity14]:
        return self.db.query(DashboardsModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity14]:
        return self.db.query(DashboardsModelEntity14).filter(DashboardsModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: DashboardsSchemaEntity14Create) -> DashboardsModelEntity14:
        db_obj = DashboardsModelEntity14(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_14(self, entity_id: int, payload: DashboardsSchemaEntity14Update) -> Optional[DashboardsModelEntity14]:
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

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity15]:
        return self.db.query(DashboardsModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity15]:
        return self.db.query(DashboardsModelEntity15).filter(DashboardsModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: DashboardsSchemaEntity15Create) -> DashboardsModelEntity15:
        db_obj = DashboardsModelEntity15(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_15(self, entity_id: int, payload: DashboardsSchemaEntity15Update) -> Optional[DashboardsModelEntity15]:
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

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity16]:
        return self.db.query(DashboardsModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity16]:
        return self.db.query(DashboardsModelEntity16).filter(DashboardsModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: DashboardsSchemaEntity16Create) -> DashboardsModelEntity16:
        db_obj = DashboardsModelEntity16(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_16(self, entity_id: int, payload: DashboardsSchemaEntity16Update) -> Optional[DashboardsModelEntity16]:
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

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity17]:
        return self.db.query(DashboardsModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity17]:
        return self.db.query(DashboardsModelEntity17).filter(DashboardsModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: DashboardsSchemaEntity17Create) -> DashboardsModelEntity17:
        db_obj = DashboardsModelEntity17(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_17(self, entity_id: int, payload: DashboardsSchemaEntity17Update) -> Optional[DashboardsModelEntity17]:
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

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity18]:
        return self.db.query(DashboardsModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity18]:
        return self.db.query(DashboardsModelEntity18).filter(DashboardsModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: DashboardsSchemaEntity18Create) -> DashboardsModelEntity18:
        db_obj = DashboardsModelEntity18(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_18(self, entity_id: int, payload: DashboardsSchemaEntity18Update) -> Optional[DashboardsModelEntity18]:
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

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity19]:
        return self.db.query(DashboardsModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity19]:
        return self.db.query(DashboardsModelEntity19).filter(DashboardsModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: DashboardsSchemaEntity19Create) -> DashboardsModelEntity19:
        db_obj = DashboardsModelEntity19(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_19(self, entity_id: int, payload: DashboardsSchemaEntity19Update) -> Optional[DashboardsModelEntity19]:
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

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity20]:
        return self.db.query(DashboardsModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity20]:
        return self.db.query(DashboardsModelEntity20).filter(DashboardsModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: DashboardsSchemaEntity20Create) -> DashboardsModelEntity20:
        db_obj = DashboardsModelEntity20(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_20(self, entity_id: int, payload: DashboardsSchemaEntity20Update) -> Optional[DashboardsModelEntity20]:
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

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity21]:
        return self.db.query(DashboardsModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity21]:
        return self.db.query(DashboardsModelEntity21).filter(DashboardsModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: DashboardsSchemaEntity21Create) -> DashboardsModelEntity21:
        db_obj = DashboardsModelEntity21(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_21(self, entity_id: int, payload: DashboardsSchemaEntity21Update) -> Optional[DashboardsModelEntity21]:
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

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity22]:
        return self.db.query(DashboardsModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity22]:
        return self.db.query(DashboardsModelEntity22).filter(DashboardsModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: DashboardsSchemaEntity22Create) -> DashboardsModelEntity22:
        db_obj = DashboardsModelEntity22(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_22(self, entity_id: int, payload: DashboardsSchemaEntity22Update) -> Optional[DashboardsModelEntity22]:
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

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity23]:
        return self.db.query(DashboardsModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity23]:
        return self.db.query(DashboardsModelEntity23).filter(DashboardsModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: DashboardsSchemaEntity23Create) -> DashboardsModelEntity23:
        db_obj = DashboardsModelEntity23(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_23(self, entity_id: int, payload: DashboardsSchemaEntity23Update) -> Optional[DashboardsModelEntity23]:
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

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity24]:
        return self.db.query(DashboardsModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity24]:
        return self.db.query(DashboardsModelEntity24).filter(DashboardsModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: DashboardsSchemaEntity24Create) -> DashboardsModelEntity24:
        db_obj = DashboardsModelEntity24(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_24(self, entity_id: int, payload: DashboardsSchemaEntity24Update) -> Optional[DashboardsModelEntity24]:
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

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity25]:
        return self.db.query(DashboardsModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity25]:
        return self.db.query(DashboardsModelEntity25).filter(DashboardsModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: DashboardsSchemaEntity25Create) -> DashboardsModelEntity25:
        db_obj = DashboardsModelEntity25(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_25(self, entity_id: int, payload: DashboardsSchemaEntity25Update) -> Optional[DashboardsModelEntity25]:
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

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity26]:
        return self.db.query(DashboardsModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity26]:
        return self.db.query(DashboardsModelEntity26).filter(DashboardsModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: DashboardsSchemaEntity26Create) -> DashboardsModelEntity26:
        db_obj = DashboardsModelEntity26(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_26(self, entity_id: int, payload: DashboardsSchemaEntity26Update) -> Optional[DashboardsModelEntity26]:
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

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity27]:
        return self.db.query(DashboardsModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity27]:
        return self.db.query(DashboardsModelEntity27).filter(DashboardsModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: DashboardsSchemaEntity27Create) -> DashboardsModelEntity27:
        db_obj = DashboardsModelEntity27(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_27(self, entity_id: int, payload: DashboardsSchemaEntity27Update) -> Optional[DashboardsModelEntity27]:
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

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity28]:
        return self.db.query(DashboardsModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity28]:
        return self.db.query(DashboardsModelEntity28).filter(DashboardsModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: DashboardsSchemaEntity28Create) -> DashboardsModelEntity28:
        db_obj = DashboardsModelEntity28(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_28(self, entity_id: int, payload: DashboardsSchemaEntity28Update) -> Optional[DashboardsModelEntity28]:
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

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity29]:
        return self.db.query(DashboardsModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity29]:
        return self.db.query(DashboardsModelEntity29).filter(DashboardsModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: DashboardsSchemaEntity29Create) -> DashboardsModelEntity29:
        db_obj = DashboardsModelEntity29(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_29(self, entity_id: int, payload: DashboardsSchemaEntity29Update) -> Optional[DashboardsModelEntity29]:
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

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity30]:
        return self.db.query(DashboardsModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity30]:
        return self.db.query(DashboardsModelEntity30).filter(DashboardsModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: DashboardsSchemaEntity30Create) -> DashboardsModelEntity30:
        db_obj = DashboardsModelEntity30(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_30(self, entity_id: int, payload: DashboardsSchemaEntity30Update) -> Optional[DashboardsModelEntity30]:
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

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity31]:
        return self.db.query(DashboardsModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity31]:
        return self.db.query(DashboardsModelEntity31).filter(DashboardsModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: DashboardsSchemaEntity31Create) -> DashboardsModelEntity31:
        db_obj = DashboardsModelEntity31(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_31(self, entity_id: int, payload: DashboardsSchemaEntity31Update) -> Optional[DashboardsModelEntity31]:
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

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity32]:
        return self.db.query(DashboardsModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity32]:
        return self.db.query(DashboardsModelEntity32).filter(DashboardsModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: DashboardsSchemaEntity32Create) -> DashboardsModelEntity32:
        db_obj = DashboardsModelEntity32(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_32(self, entity_id: int, payload: DashboardsSchemaEntity32Update) -> Optional[DashboardsModelEntity32]:
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

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity33]:
        return self.db.query(DashboardsModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity33]:
        return self.db.query(DashboardsModelEntity33).filter(DashboardsModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: DashboardsSchemaEntity33Create) -> DashboardsModelEntity33:
        db_obj = DashboardsModelEntity33(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_33(self, entity_id: int, payload: DashboardsSchemaEntity33Update) -> Optional[DashboardsModelEntity33]:
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

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity34]:
        return self.db.query(DashboardsModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity34]:
        return self.db.query(DashboardsModelEntity34).filter(DashboardsModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: DashboardsSchemaEntity34Create) -> DashboardsModelEntity34:
        db_obj = DashboardsModelEntity34(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_34(self, entity_id: int, payload: DashboardsSchemaEntity34Update) -> Optional[DashboardsModelEntity34]:
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

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity35]:
        return self.db.query(DashboardsModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity35]:
        return self.db.query(DashboardsModelEntity35).filter(DashboardsModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: DashboardsSchemaEntity35Create) -> DashboardsModelEntity35:
        db_obj = DashboardsModelEntity35(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_35(self, entity_id: int, payload: DashboardsSchemaEntity35Update) -> Optional[DashboardsModelEntity35]:
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

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity36]:
        return self.db.query(DashboardsModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity36]:
        return self.db.query(DashboardsModelEntity36).filter(DashboardsModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: DashboardsSchemaEntity36Create) -> DashboardsModelEntity36:
        db_obj = DashboardsModelEntity36(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_36(self, entity_id: int, payload: DashboardsSchemaEntity36Update) -> Optional[DashboardsModelEntity36]:
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

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity37]:
        return self.db.query(DashboardsModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity37]:
        return self.db.query(DashboardsModelEntity37).filter(DashboardsModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: DashboardsSchemaEntity37Create) -> DashboardsModelEntity37:
        db_obj = DashboardsModelEntity37(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_37(self, entity_id: int, payload: DashboardsSchemaEntity37Update) -> Optional[DashboardsModelEntity37]:
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

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity38]:
        return self.db.query(DashboardsModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity38]:
        return self.db.query(DashboardsModelEntity38).filter(DashboardsModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: DashboardsSchemaEntity38Create) -> DashboardsModelEntity38:
        db_obj = DashboardsModelEntity38(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_38(self, entity_id: int, payload: DashboardsSchemaEntity38Update) -> Optional[DashboardsModelEntity38]:
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

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity39]:
        return self.db.query(DashboardsModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity39]:
        return self.db.query(DashboardsModelEntity39).filter(DashboardsModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: DashboardsSchemaEntity39Create) -> DashboardsModelEntity39:
        db_obj = DashboardsModelEntity39(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_39(self, entity_id: int, payload: DashboardsSchemaEntity39Update) -> Optional[DashboardsModelEntity39]:
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

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity40]:
        return self.db.query(DashboardsModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity40]:
        return self.db.query(DashboardsModelEntity40).filter(DashboardsModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: DashboardsSchemaEntity40Create) -> DashboardsModelEntity40:
        db_obj = DashboardsModelEntity40(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_40(self, entity_id: int, payload: DashboardsSchemaEntity40Update) -> Optional[DashboardsModelEntity40]:
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

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity41]:
        return self.db.query(DashboardsModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity41]:
        return self.db.query(DashboardsModelEntity41).filter(DashboardsModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: DashboardsSchemaEntity41Create) -> DashboardsModelEntity41:
        db_obj = DashboardsModelEntity41(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_41(self, entity_id: int, payload: DashboardsSchemaEntity41Update) -> Optional[DashboardsModelEntity41]:
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

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity42]:
        return self.db.query(DashboardsModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity42]:
        return self.db.query(DashboardsModelEntity42).filter(DashboardsModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: DashboardsSchemaEntity42Create) -> DashboardsModelEntity42:
        db_obj = DashboardsModelEntity42(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_42(self, entity_id: int, payload: DashboardsSchemaEntity42Update) -> Optional[DashboardsModelEntity42]:
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

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity43]:
        return self.db.query(DashboardsModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity43]:
        return self.db.query(DashboardsModelEntity43).filter(DashboardsModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: DashboardsSchemaEntity43Create) -> DashboardsModelEntity43:
        db_obj = DashboardsModelEntity43(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_43(self, entity_id: int, payload: DashboardsSchemaEntity43Update) -> Optional[DashboardsModelEntity43]:
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

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity44]:
        return self.db.query(DashboardsModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity44]:
        return self.db.query(DashboardsModelEntity44).filter(DashboardsModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: DashboardsSchemaEntity44Create) -> DashboardsModelEntity44:
        db_obj = DashboardsModelEntity44(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_44(self, entity_id: int, payload: DashboardsSchemaEntity44Update) -> Optional[DashboardsModelEntity44]:
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

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity45]:
        return self.db.query(DashboardsModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity45]:
        return self.db.query(DashboardsModelEntity45).filter(DashboardsModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: DashboardsSchemaEntity45Create) -> DashboardsModelEntity45:
        db_obj = DashboardsModelEntity45(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_45(self, entity_id: int, payload: DashboardsSchemaEntity45Update) -> Optional[DashboardsModelEntity45]:
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

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity46]:
        return self.db.query(DashboardsModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity46]:
        return self.db.query(DashboardsModelEntity46).filter(DashboardsModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: DashboardsSchemaEntity46Create) -> DashboardsModelEntity46:
        db_obj = DashboardsModelEntity46(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_46(self, entity_id: int, payload: DashboardsSchemaEntity46Update) -> Optional[DashboardsModelEntity46]:
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

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity47]:
        return self.db.query(DashboardsModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity47]:
        return self.db.query(DashboardsModelEntity47).filter(DashboardsModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: DashboardsSchemaEntity47Create) -> DashboardsModelEntity47:
        db_obj = DashboardsModelEntity47(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_47(self, entity_id: int, payload: DashboardsSchemaEntity47Update) -> Optional[DashboardsModelEntity47]:
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

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity48]:
        return self.db.query(DashboardsModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity48]:
        return self.db.query(DashboardsModelEntity48).filter(DashboardsModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: DashboardsSchemaEntity48Create) -> DashboardsModelEntity48:
        db_obj = DashboardsModelEntity48(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_48(self, entity_id: int, payload: DashboardsSchemaEntity48Update) -> Optional[DashboardsModelEntity48]:
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

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity49]:
        return self.db.query(DashboardsModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity49]:
        return self.db.query(DashboardsModelEntity49).filter(DashboardsModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: DashboardsSchemaEntity49Create) -> DashboardsModelEntity49:
        db_obj = DashboardsModelEntity49(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_49(self, entity_id: int, payload: DashboardsSchemaEntity49Update) -> Optional[DashboardsModelEntity49]:
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

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[DashboardsModelEntity50]:
        return self.db.query(DashboardsModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[DashboardsModelEntity50]:
        return self.db.query(DashboardsModelEntity50).filter(DashboardsModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: DashboardsSchemaEntity50Create) -> DashboardsModelEntity50:
        db_obj = DashboardsModelEntity50(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_50(self, entity_id: int, payload: DashboardsSchemaEntity50Update) -> Optional[DashboardsModelEntity50]:
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

