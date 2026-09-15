"""
Finance, Billing & Payroll - Service Business Logic Layer
Module: app.domains.finance.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.finance.models import *
from app.domains.finance.schemas import *

class FinanceDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity1]:
        return self.db.query(FinanceModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[FinanceModelEntity1]:
        return self.db.query(FinanceModelEntity1).filter(FinanceModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: FinanceSchemaEntity1Create) -> FinanceModelEntity1:
        db_obj = FinanceModelEntity1(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_1(self, entity_id: int, payload: FinanceSchemaEntity1Update) -> Optional[FinanceModelEntity1]:
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

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity2]:
        return self.db.query(FinanceModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[FinanceModelEntity2]:
        return self.db.query(FinanceModelEntity2).filter(FinanceModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: FinanceSchemaEntity2Create) -> FinanceModelEntity2:
        db_obj = FinanceModelEntity2(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_2(self, entity_id: int, payload: FinanceSchemaEntity2Update) -> Optional[FinanceModelEntity2]:
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

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity3]:
        return self.db.query(FinanceModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[FinanceModelEntity3]:
        return self.db.query(FinanceModelEntity3).filter(FinanceModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: FinanceSchemaEntity3Create) -> FinanceModelEntity3:
        db_obj = FinanceModelEntity3(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_3(self, entity_id: int, payload: FinanceSchemaEntity3Update) -> Optional[FinanceModelEntity3]:
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

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity4]:
        return self.db.query(FinanceModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[FinanceModelEntity4]:
        return self.db.query(FinanceModelEntity4).filter(FinanceModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: FinanceSchemaEntity4Create) -> FinanceModelEntity4:
        db_obj = FinanceModelEntity4(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_4(self, entity_id: int, payload: FinanceSchemaEntity4Update) -> Optional[FinanceModelEntity4]:
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

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity5]:
        return self.db.query(FinanceModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[FinanceModelEntity5]:
        return self.db.query(FinanceModelEntity5).filter(FinanceModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: FinanceSchemaEntity5Create) -> FinanceModelEntity5:
        db_obj = FinanceModelEntity5(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_5(self, entity_id: int, payload: FinanceSchemaEntity5Update) -> Optional[FinanceModelEntity5]:
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

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity6]:
        return self.db.query(FinanceModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[FinanceModelEntity6]:
        return self.db.query(FinanceModelEntity6).filter(FinanceModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: FinanceSchemaEntity6Create) -> FinanceModelEntity6:
        db_obj = FinanceModelEntity6(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_6(self, entity_id: int, payload: FinanceSchemaEntity6Update) -> Optional[FinanceModelEntity6]:
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

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity7]:
        return self.db.query(FinanceModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[FinanceModelEntity7]:
        return self.db.query(FinanceModelEntity7).filter(FinanceModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: FinanceSchemaEntity7Create) -> FinanceModelEntity7:
        db_obj = FinanceModelEntity7(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_7(self, entity_id: int, payload: FinanceSchemaEntity7Update) -> Optional[FinanceModelEntity7]:
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

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity8]:
        return self.db.query(FinanceModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[FinanceModelEntity8]:
        return self.db.query(FinanceModelEntity8).filter(FinanceModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: FinanceSchemaEntity8Create) -> FinanceModelEntity8:
        db_obj = FinanceModelEntity8(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_8(self, entity_id: int, payload: FinanceSchemaEntity8Update) -> Optional[FinanceModelEntity8]:
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

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity9]:
        return self.db.query(FinanceModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[FinanceModelEntity9]:
        return self.db.query(FinanceModelEntity9).filter(FinanceModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: FinanceSchemaEntity9Create) -> FinanceModelEntity9:
        db_obj = FinanceModelEntity9(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_9(self, entity_id: int, payload: FinanceSchemaEntity9Update) -> Optional[FinanceModelEntity9]:
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

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity10]:
        return self.db.query(FinanceModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[FinanceModelEntity10]:
        return self.db.query(FinanceModelEntity10).filter(FinanceModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: FinanceSchemaEntity10Create) -> FinanceModelEntity10:
        db_obj = FinanceModelEntity10(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_10(self, entity_id: int, payload: FinanceSchemaEntity10Update) -> Optional[FinanceModelEntity10]:
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

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity11]:
        return self.db.query(FinanceModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[FinanceModelEntity11]:
        return self.db.query(FinanceModelEntity11).filter(FinanceModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: FinanceSchemaEntity11Create) -> FinanceModelEntity11:
        db_obj = FinanceModelEntity11(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_11(self, entity_id: int, payload: FinanceSchemaEntity11Update) -> Optional[FinanceModelEntity11]:
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

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity12]:
        return self.db.query(FinanceModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[FinanceModelEntity12]:
        return self.db.query(FinanceModelEntity12).filter(FinanceModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: FinanceSchemaEntity12Create) -> FinanceModelEntity12:
        db_obj = FinanceModelEntity12(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_12(self, entity_id: int, payload: FinanceSchemaEntity12Update) -> Optional[FinanceModelEntity12]:
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

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity13]:
        return self.db.query(FinanceModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[FinanceModelEntity13]:
        return self.db.query(FinanceModelEntity13).filter(FinanceModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: FinanceSchemaEntity13Create) -> FinanceModelEntity13:
        db_obj = FinanceModelEntity13(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_13(self, entity_id: int, payload: FinanceSchemaEntity13Update) -> Optional[FinanceModelEntity13]:
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

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity14]:
        return self.db.query(FinanceModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[FinanceModelEntity14]:
        return self.db.query(FinanceModelEntity14).filter(FinanceModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: FinanceSchemaEntity14Create) -> FinanceModelEntity14:
        db_obj = FinanceModelEntity14(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_14(self, entity_id: int, payload: FinanceSchemaEntity14Update) -> Optional[FinanceModelEntity14]:
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

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity15]:
        return self.db.query(FinanceModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[FinanceModelEntity15]:
        return self.db.query(FinanceModelEntity15).filter(FinanceModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: FinanceSchemaEntity15Create) -> FinanceModelEntity15:
        db_obj = FinanceModelEntity15(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_15(self, entity_id: int, payload: FinanceSchemaEntity15Update) -> Optional[FinanceModelEntity15]:
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

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity16]:
        return self.db.query(FinanceModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[FinanceModelEntity16]:
        return self.db.query(FinanceModelEntity16).filter(FinanceModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: FinanceSchemaEntity16Create) -> FinanceModelEntity16:
        db_obj = FinanceModelEntity16(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_16(self, entity_id: int, payload: FinanceSchemaEntity16Update) -> Optional[FinanceModelEntity16]:
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

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity17]:
        return self.db.query(FinanceModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[FinanceModelEntity17]:
        return self.db.query(FinanceModelEntity17).filter(FinanceModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: FinanceSchemaEntity17Create) -> FinanceModelEntity17:
        db_obj = FinanceModelEntity17(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_17(self, entity_id: int, payload: FinanceSchemaEntity17Update) -> Optional[FinanceModelEntity17]:
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

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity18]:
        return self.db.query(FinanceModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[FinanceModelEntity18]:
        return self.db.query(FinanceModelEntity18).filter(FinanceModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: FinanceSchemaEntity18Create) -> FinanceModelEntity18:
        db_obj = FinanceModelEntity18(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_18(self, entity_id: int, payload: FinanceSchemaEntity18Update) -> Optional[FinanceModelEntity18]:
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

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity19]:
        return self.db.query(FinanceModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[FinanceModelEntity19]:
        return self.db.query(FinanceModelEntity19).filter(FinanceModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: FinanceSchemaEntity19Create) -> FinanceModelEntity19:
        db_obj = FinanceModelEntity19(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_19(self, entity_id: int, payload: FinanceSchemaEntity19Update) -> Optional[FinanceModelEntity19]:
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

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity20]:
        return self.db.query(FinanceModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[FinanceModelEntity20]:
        return self.db.query(FinanceModelEntity20).filter(FinanceModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: FinanceSchemaEntity20Create) -> FinanceModelEntity20:
        db_obj = FinanceModelEntity20(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_20(self, entity_id: int, payload: FinanceSchemaEntity20Update) -> Optional[FinanceModelEntity20]:
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

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity21]:
        return self.db.query(FinanceModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[FinanceModelEntity21]:
        return self.db.query(FinanceModelEntity21).filter(FinanceModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: FinanceSchemaEntity21Create) -> FinanceModelEntity21:
        db_obj = FinanceModelEntity21(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_21(self, entity_id: int, payload: FinanceSchemaEntity21Update) -> Optional[FinanceModelEntity21]:
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

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity22]:
        return self.db.query(FinanceModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[FinanceModelEntity22]:
        return self.db.query(FinanceModelEntity22).filter(FinanceModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: FinanceSchemaEntity22Create) -> FinanceModelEntity22:
        db_obj = FinanceModelEntity22(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_22(self, entity_id: int, payload: FinanceSchemaEntity22Update) -> Optional[FinanceModelEntity22]:
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

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity23]:
        return self.db.query(FinanceModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[FinanceModelEntity23]:
        return self.db.query(FinanceModelEntity23).filter(FinanceModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: FinanceSchemaEntity23Create) -> FinanceModelEntity23:
        db_obj = FinanceModelEntity23(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_23(self, entity_id: int, payload: FinanceSchemaEntity23Update) -> Optional[FinanceModelEntity23]:
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

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity24]:
        return self.db.query(FinanceModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[FinanceModelEntity24]:
        return self.db.query(FinanceModelEntity24).filter(FinanceModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: FinanceSchemaEntity24Create) -> FinanceModelEntity24:
        db_obj = FinanceModelEntity24(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_24(self, entity_id: int, payload: FinanceSchemaEntity24Update) -> Optional[FinanceModelEntity24]:
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

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity25]:
        return self.db.query(FinanceModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[FinanceModelEntity25]:
        return self.db.query(FinanceModelEntity25).filter(FinanceModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: FinanceSchemaEntity25Create) -> FinanceModelEntity25:
        db_obj = FinanceModelEntity25(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_25(self, entity_id: int, payload: FinanceSchemaEntity25Update) -> Optional[FinanceModelEntity25]:
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

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity26]:
        return self.db.query(FinanceModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[FinanceModelEntity26]:
        return self.db.query(FinanceModelEntity26).filter(FinanceModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: FinanceSchemaEntity26Create) -> FinanceModelEntity26:
        db_obj = FinanceModelEntity26(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_26(self, entity_id: int, payload: FinanceSchemaEntity26Update) -> Optional[FinanceModelEntity26]:
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

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity27]:
        return self.db.query(FinanceModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[FinanceModelEntity27]:
        return self.db.query(FinanceModelEntity27).filter(FinanceModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: FinanceSchemaEntity27Create) -> FinanceModelEntity27:
        db_obj = FinanceModelEntity27(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_27(self, entity_id: int, payload: FinanceSchemaEntity27Update) -> Optional[FinanceModelEntity27]:
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

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity28]:
        return self.db.query(FinanceModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[FinanceModelEntity28]:
        return self.db.query(FinanceModelEntity28).filter(FinanceModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: FinanceSchemaEntity28Create) -> FinanceModelEntity28:
        db_obj = FinanceModelEntity28(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_28(self, entity_id: int, payload: FinanceSchemaEntity28Update) -> Optional[FinanceModelEntity28]:
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

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity29]:
        return self.db.query(FinanceModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[FinanceModelEntity29]:
        return self.db.query(FinanceModelEntity29).filter(FinanceModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: FinanceSchemaEntity29Create) -> FinanceModelEntity29:
        db_obj = FinanceModelEntity29(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_29(self, entity_id: int, payload: FinanceSchemaEntity29Update) -> Optional[FinanceModelEntity29]:
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

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity30]:
        return self.db.query(FinanceModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[FinanceModelEntity30]:
        return self.db.query(FinanceModelEntity30).filter(FinanceModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: FinanceSchemaEntity30Create) -> FinanceModelEntity30:
        db_obj = FinanceModelEntity30(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_30(self, entity_id: int, payload: FinanceSchemaEntity30Update) -> Optional[FinanceModelEntity30]:
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

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity31]:
        return self.db.query(FinanceModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[FinanceModelEntity31]:
        return self.db.query(FinanceModelEntity31).filter(FinanceModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: FinanceSchemaEntity31Create) -> FinanceModelEntity31:
        db_obj = FinanceModelEntity31(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_31(self, entity_id: int, payload: FinanceSchemaEntity31Update) -> Optional[FinanceModelEntity31]:
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

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity32]:
        return self.db.query(FinanceModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[FinanceModelEntity32]:
        return self.db.query(FinanceModelEntity32).filter(FinanceModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: FinanceSchemaEntity32Create) -> FinanceModelEntity32:
        db_obj = FinanceModelEntity32(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_32(self, entity_id: int, payload: FinanceSchemaEntity32Update) -> Optional[FinanceModelEntity32]:
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

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity33]:
        return self.db.query(FinanceModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[FinanceModelEntity33]:
        return self.db.query(FinanceModelEntity33).filter(FinanceModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: FinanceSchemaEntity33Create) -> FinanceModelEntity33:
        db_obj = FinanceModelEntity33(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_33(self, entity_id: int, payload: FinanceSchemaEntity33Update) -> Optional[FinanceModelEntity33]:
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

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity34]:
        return self.db.query(FinanceModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[FinanceModelEntity34]:
        return self.db.query(FinanceModelEntity34).filter(FinanceModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: FinanceSchemaEntity34Create) -> FinanceModelEntity34:
        db_obj = FinanceModelEntity34(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_34(self, entity_id: int, payload: FinanceSchemaEntity34Update) -> Optional[FinanceModelEntity34]:
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

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity35]:
        return self.db.query(FinanceModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[FinanceModelEntity35]:
        return self.db.query(FinanceModelEntity35).filter(FinanceModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: FinanceSchemaEntity35Create) -> FinanceModelEntity35:
        db_obj = FinanceModelEntity35(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_35(self, entity_id: int, payload: FinanceSchemaEntity35Update) -> Optional[FinanceModelEntity35]:
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

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity36]:
        return self.db.query(FinanceModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[FinanceModelEntity36]:
        return self.db.query(FinanceModelEntity36).filter(FinanceModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: FinanceSchemaEntity36Create) -> FinanceModelEntity36:
        db_obj = FinanceModelEntity36(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_36(self, entity_id: int, payload: FinanceSchemaEntity36Update) -> Optional[FinanceModelEntity36]:
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

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity37]:
        return self.db.query(FinanceModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[FinanceModelEntity37]:
        return self.db.query(FinanceModelEntity37).filter(FinanceModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: FinanceSchemaEntity37Create) -> FinanceModelEntity37:
        db_obj = FinanceModelEntity37(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_37(self, entity_id: int, payload: FinanceSchemaEntity37Update) -> Optional[FinanceModelEntity37]:
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

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity38]:
        return self.db.query(FinanceModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[FinanceModelEntity38]:
        return self.db.query(FinanceModelEntity38).filter(FinanceModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: FinanceSchemaEntity38Create) -> FinanceModelEntity38:
        db_obj = FinanceModelEntity38(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_38(self, entity_id: int, payload: FinanceSchemaEntity38Update) -> Optional[FinanceModelEntity38]:
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

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity39]:
        return self.db.query(FinanceModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[FinanceModelEntity39]:
        return self.db.query(FinanceModelEntity39).filter(FinanceModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: FinanceSchemaEntity39Create) -> FinanceModelEntity39:
        db_obj = FinanceModelEntity39(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_39(self, entity_id: int, payload: FinanceSchemaEntity39Update) -> Optional[FinanceModelEntity39]:
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

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity40]:
        return self.db.query(FinanceModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[FinanceModelEntity40]:
        return self.db.query(FinanceModelEntity40).filter(FinanceModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: FinanceSchemaEntity40Create) -> FinanceModelEntity40:
        db_obj = FinanceModelEntity40(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_40(self, entity_id: int, payload: FinanceSchemaEntity40Update) -> Optional[FinanceModelEntity40]:
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

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity41]:
        return self.db.query(FinanceModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[FinanceModelEntity41]:
        return self.db.query(FinanceModelEntity41).filter(FinanceModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: FinanceSchemaEntity41Create) -> FinanceModelEntity41:
        db_obj = FinanceModelEntity41(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_41(self, entity_id: int, payload: FinanceSchemaEntity41Update) -> Optional[FinanceModelEntity41]:
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

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity42]:
        return self.db.query(FinanceModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[FinanceModelEntity42]:
        return self.db.query(FinanceModelEntity42).filter(FinanceModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: FinanceSchemaEntity42Create) -> FinanceModelEntity42:
        db_obj = FinanceModelEntity42(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_42(self, entity_id: int, payload: FinanceSchemaEntity42Update) -> Optional[FinanceModelEntity42]:
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

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity43]:
        return self.db.query(FinanceModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[FinanceModelEntity43]:
        return self.db.query(FinanceModelEntity43).filter(FinanceModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: FinanceSchemaEntity43Create) -> FinanceModelEntity43:
        db_obj = FinanceModelEntity43(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_43(self, entity_id: int, payload: FinanceSchemaEntity43Update) -> Optional[FinanceModelEntity43]:
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

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity44]:
        return self.db.query(FinanceModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[FinanceModelEntity44]:
        return self.db.query(FinanceModelEntity44).filter(FinanceModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: FinanceSchemaEntity44Create) -> FinanceModelEntity44:
        db_obj = FinanceModelEntity44(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_44(self, entity_id: int, payload: FinanceSchemaEntity44Update) -> Optional[FinanceModelEntity44]:
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

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity45]:
        return self.db.query(FinanceModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[FinanceModelEntity45]:
        return self.db.query(FinanceModelEntity45).filter(FinanceModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: FinanceSchemaEntity45Create) -> FinanceModelEntity45:
        db_obj = FinanceModelEntity45(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_45(self, entity_id: int, payload: FinanceSchemaEntity45Update) -> Optional[FinanceModelEntity45]:
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

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity46]:
        return self.db.query(FinanceModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[FinanceModelEntity46]:
        return self.db.query(FinanceModelEntity46).filter(FinanceModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: FinanceSchemaEntity46Create) -> FinanceModelEntity46:
        db_obj = FinanceModelEntity46(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_46(self, entity_id: int, payload: FinanceSchemaEntity46Update) -> Optional[FinanceModelEntity46]:
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

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity47]:
        return self.db.query(FinanceModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[FinanceModelEntity47]:
        return self.db.query(FinanceModelEntity47).filter(FinanceModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: FinanceSchemaEntity47Create) -> FinanceModelEntity47:
        db_obj = FinanceModelEntity47(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_47(self, entity_id: int, payload: FinanceSchemaEntity47Update) -> Optional[FinanceModelEntity47]:
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

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity48]:
        return self.db.query(FinanceModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[FinanceModelEntity48]:
        return self.db.query(FinanceModelEntity48).filter(FinanceModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: FinanceSchemaEntity48Create) -> FinanceModelEntity48:
        db_obj = FinanceModelEntity48(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_48(self, entity_id: int, payload: FinanceSchemaEntity48Update) -> Optional[FinanceModelEntity48]:
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

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity49]:
        return self.db.query(FinanceModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[FinanceModelEntity49]:
        return self.db.query(FinanceModelEntity49).filter(FinanceModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: FinanceSchemaEntity49Create) -> FinanceModelEntity49:
        db_obj = FinanceModelEntity49(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_49(self, entity_id: int, payload: FinanceSchemaEntity49Update) -> Optional[FinanceModelEntity49]:
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

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity50]:
        return self.db.query(FinanceModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[FinanceModelEntity50]:
        return self.db.query(FinanceModelEntity50).filter(FinanceModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: FinanceSchemaEntity50Create) -> FinanceModelEntity50:
        db_obj = FinanceModelEntity50(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_50(self, entity_id: int, payload: FinanceSchemaEntity50Update) -> Optional[FinanceModelEntity50]:
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

    def get_entity_51_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity51]:
        return self.db.query(FinanceModelEntity51).offset(skip).limit(limit).all()

    def get_entity_51_by_id(self, entity_id: int) -> Optional[FinanceModelEntity51]:
        return self.db.query(FinanceModelEntity51).filter(FinanceModelEntity51.id == entity_id).first()

    def create_entity_51(self, payload: FinanceSchemaEntity51Create) -> FinanceModelEntity51:
        db_obj = FinanceModelEntity51(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_51(self, entity_id: int, payload: FinanceSchemaEntity51Update) -> Optional[FinanceModelEntity51]:
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

    def get_entity_52_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity52]:
        return self.db.query(FinanceModelEntity52).offset(skip).limit(limit).all()

    def get_entity_52_by_id(self, entity_id: int) -> Optional[FinanceModelEntity52]:
        return self.db.query(FinanceModelEntity52).filter(FinanceModelEntity52.id == entity_id).first()

    def create_entity_52(self, payload: FinanceSchemaEntity52Create) -> FinanceModelEntity52:
        db_obj = FinanceModelEntity52(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_52(self, entity_id: int, payload: FinanceSchemaEntity52Update) -> Optional[FinanceModelEntity52]:
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

    def get_entity_53_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity53]:
        return self.db.query(FinanceModelEntity53).offset(skip).limit(limit).all()

    def get_entity_53_by_id(self, entity_id: int) -> Optional[FinanceModelEntity53]:
        return self.db.query(FinanceModelEntity53).filter(FinanceModelEntity53.id == entity_id).first()

    def create_entity_53(self, payload: FinanceSchemaEntity53Create) -> FinanceModelEntity53:
        db_obj = FinanceModelEntity53(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_53(self, entity_id: int, payload: FinanceSchemaEntity53Update) -> Optional[FinanceModelEntity53]:
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

    def get_entity_54_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity54]:
        return self.db.query(FinanceModelEntity54).offset(skip).limit(limit).all()

    def get_entity_54_by_id(self, entity_id: int) -> Optional[FinanceModelEntity54]:
        return self.db.query(FinanceModelEntity54).filter(FinanceModelEntity54.id == entity_id).first()

    def create_entity_54(self, payload: FinanceSchemaEntity54Create) -> FinanceModelEntity54:
        db_obj = FinanceModelEntity54(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_54(self, entity_id: int, payload: FinanceSchemaEntity54Update) -> Optional[FinanceModelEntity54]:
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

    def get_entity_55_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity55]:
        return self.db.query(FinanceModelEntity55).offset(skip).limit(limit).all()

    def get_entity_55_by_id(self, entity_id: int) -> Optional[FinanceModelEntity55]:
        return self.db.query(FinanceModelEntity55).filter(FinanceModelEntity55.id == entity_id).first()

    def create_entity_55(self, payload: FinanceSchemaEntity55Create) -> FinanceModelEntity55:
        db_obj = FinanceModelEntity55(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_55(self, entity_id: int, payload: FinanceSchemaEntity55Update) -> Optional[FinanceModelEntity55]:
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

    def get_entity_56_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity56]:
        return self.db.query(FinanceModelEntity56).offset(skip).limit(limit).all()

    def get_entity_56_by_id(self, entity_id: int) -> Optional[FinanceModelEntity56]:
        return self.db.query(FinanceModelEntity56).filter(FinanceModelEntity56.id == entity_id).first()

    def create_entity_56(self, payload: FinanceSchemaEntity56Create) -> FinanceModelEntity56:
        db_obj = FinanceModelEntity56(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_56(self, entity_id: int, payload: FinanceSchemaEntity56Update) -> Optional[FinanceModelEntity56]:
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

    def get_entity_57_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity57]:
        return self.db.query(FinanceModelEntity57).offset(skip).limit(limit).all()

    def get_entity_57_by_id(self, entity_id: int) -> Optional[FinanceModelEntity57]:
        return self.db.query(FinanceModelEntity57).filter(FinanceModelEntity57.id == entity_id).first()

    def create_entity_57(self, payload: FinanceSchemaEntity57Create) -> FinanceModelEntity57:
        db_obj = FinanceModelEntity57(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_57(self, entity_id: int, payload: FinanceSchemaEntity57Update) -> Optional[FinanceModelEntity57]:
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

    def get_entity_58_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity58]:
        return self.db.query(FinanceModelEntity58).offset(skip).limit(limit).all()

    def get_entity_58_by_id(self, entity_id: int) -> Optional[FinanceModelEntity58]:
        return self.db.query(FinanceModelEntity58).filter(FinanceModelEntity58.id == entity_id).first()

    def create_entity_58(self, payload: FinanceSchemaEntity58Create) -> FinanceModelEntity58:
        db_obj = FinanceModelEntity58(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_58(self, entity_id: int, payload: FinanceSchemaEntity58Update) -> Optional[FinanceModelEntity58]:
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

    def get_entity_59_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity59]:
        return self.db.query(FinanceModelEntity59).offset(skip).limit(limit).all()

    def get_entity_59_by_id(self, entity_id: int) -> Optional[FinanceModelEntity59]:
        return self.db.query(FinanceModelEntity59).filter(FinanceModelEntity59.id == entity_id).first()

    def create_entity_59(self, payload: FinanceSchemaEntity59Create) -> FinanceModelEntity59:
        db_obj = FinanceModelEntity59(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_59(self, entity_id: int, payload: FinanceSchemaEntity59Update) -> Optional[FinanceModelEntity59]:
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

    def get_entity_60_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity60]:
        return self.db.query(FinanceModelEntity60).offset(skip).limit(limit).all()

    def get_entity_60_by_id(self, entity_id: int) -> Optional[FinanceModelEntity60]:
        return self.db.query(FinanceModelEntity60).filter(FinanceModelEntity60.id == entity_id).first()

    def create_entity_60(self, payload: FinanceSchemaEntity60Create) -> FinanceModelEntity60:
        db_obj = FinanceModelEntity60(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_60(self, entity_id: int, payload: FinanceSchemaEntity60Update) -> Optional[FinanceModelEntity60]:
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

    def get_entity_61_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity61]:
        return self.db.query(FinanceModelEntity61).offset(skip).limit(limit).all()

    def get_entity_61_by_id(self, entity_id: int) -> Optional[FinanceModelEntity61]:
        return self.db.query(FinanceModelEntity61).filter(FinanceModelEntity61.id == entity_id).first()

    def create_entity_61(self, payload: FinanceSchemaEntity61Create) -> FinanceModelEntity61:
        db_obj = FinanceModelEntity61(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_61(self, entity_id: int, payload: FinanceSchemaEntity61Update) -> Optional[FinanceModelEntity61]:
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

    def get_entity_62_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity62]:
        return self.db.query(FinanceModelEntity62).offset(skip).limit(limit).all()

    def get_entity_62_by_id(self, entity_id: int) -> Optional[FinanceModelEntity62]:
        return self.db.query(FinanceModelEntity62).filter(FinanceModelEntity62.id == entity_id).first()

    def create_entity_62(self, payload: FinanceSchemaEntity62Create) -> FinanceModelEntity62:
        db_obj = FinanceModelEntity62(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_62(self, entity_id: int, payload: FinanceSchemaEntity62Update) -> Optional[FinanceModelEntity62]:
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

    def get_entity_63_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity63]:
        return self.db.query(FinanceModelEntity63).offset(skip).limit(limit).all()

    def get_entity_63_by_id(self, entity_id: int) -> Optional[FinanceModelEntity63]:
        return self.db.query(FinanceModelEntity63).filter(FinanceModelEntity63.id == entity_id).first()

    def create_entity_63(self, payload: FinanceSchemaEntity63Create) -> FinanceModelEntity63:
        db_obj = FinanceModelEntity63(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_63(self, entity_id: int, payload: FinanceSchemaEntity63Update) -> Optional[FinanceModelEntity63]:
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

    def get_entity_64_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity64]:
        return self.db.query(FinanceModelEntity64).offset(skip).limit(limit).all()

    def get_entity_64_by_id(self, entity_id: int) -> Optional[FinanceModelEntity64]:
        return self.db.query(FinanceModelEntity64).filter(FinanceModelEntity64.id == entity_id).first()

    def create_entity_64(self, payload: FinanceSchemaEntity64Create) -> FinanceModelEntity64:
        db_obj = FinanceModelEntity64(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_64(self, entity_id: int, payload: FinanceSchemaEntity64Update) -> Optional[FinanceModelEntity64]:
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

    def get_entity_65_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity65]:
        return self.db.query(FinanceModelEntity65).offset(skip).limit(limit).all()

    def get_entity_65_by_id(self, entity_id: int) -> Optional[FinanceModelEntity65]:
        return self.db.query(FinanceModelEntity65).filter(FinanceModelEntity65.id == entity_id).first()

    def create_entity_65(self, payload: FinanceSchemaEntity65Create) -> FinanceModelEntity65:
        db_obj = FinanceModelEntity65(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_65(self, entity_id: int, payload: FinanceSchemaEntity65Update) -> Optional[FinanceModelEntity65]:
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

    def get_entity_66_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity66]:
        return self.db.query(FinanceModelEntity66).offset(skip).limit(limit).all()

    def get_entity_66_by_id(self, entity_id: int) -> Optional[FinanceModelEntity66]:
        return self.db.query(FinanceModelEntity66).filter(FinanceModelEntity66.id == entity_id).first()

    def create_entity_66(self, payload: FinanceSchemaEntity66Create) -> FinanceModelEntity66:
        db_obj = FinanceModelEntity66(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_66(self, entity_id: int, payload: FinanceSchemaEntity66Update) -> Optional[FinanceModelEntity66]:
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

    def get_entity_67_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity67]:
        return self.db.query(FinanceModelEntity67).offset(skip).limit(limit).all()

    def get_entity_67_by_id(self, entity_id: int) -> Optional[FinanceModelEntity67]:
        return self.db.query(FinanceModelEntity67).filter(FinanceModelEntity67.id == entity_id).first()

    def create_entity_67(self, payload: FinanceSchemaEntity67Create) -> FinanceModelEntity67:
        db_obj = FinanceModelEntity67(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_67(self, entity_id: int, payload: FinanceSchemaEntity67Update) -> Optional[FinanceModelEntity67]:
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

    def get_entity_68_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity68]:
        return self.db.query(FinanceModelEntity68).offset(skip).limit(limit).all()

    def get_entity_68_by_id(self, entity_id: int) -> Optional[FinanceModelEntity68]:
        return self.db.query(FinanceModelEntity68).filter(FinanceModelEntity68.id == entity_id).first()

    def create_entity_68(self, payload: FinanceSchemaEntity68Create) -> FinanceModelEntity68:
        db_obj = FinanceModelEntity68(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_68(self, entity_id: int, payload: FinanceSchemaEntity68Update) -> Optional[FinanceModelEntity68]:
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

    def get_entity_69_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity69]:
        return self.db.query(FinanceModelEntity69).offset(skip).limit(limit).all()

    def get_entity_69_by_id(self, entity_id: int) -> Optional[FinanceModelEntity69]:
        return self.db.query(FinanceModelEntity69).filter(FinanceModelEntity69.id == entity_id).first()

    def create_entity_69(self, payload: FinanceSchemaEntity69Create) -> FinanceModelEntity69:
        db_obj = FinanceModelEntity69(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_69(self, entity_id: int, payload: FinanceSchemaEntity69Update) -> Optional[FinanceModelEntity69]:
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

    def get_entity_70_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity70]:
        return self.db.query(FinanceModelEntity70).offset(skip).limit(limit).all()

    def get_entity_70_by_id(self, entity_id: int) -> Optional[FinanceModelEntity70]:
        return self.db.query(FinanceModelEntity70).filter(FinanceModelEntity70.id == entity_id).first()

    def create_entity_70(self, payload: FinanceSchemaEntity70Create) -> FinanceModelEntity70:
        db_obj = FinanceModelEntity70(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_70(self, entity_id: int, payload: FinanceSchemaEntity70Update) -> Optional[FinanceModelEntity70]:
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

    def get_entity_71_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity71]:
        return self.db.query(FinanceModelEntity71).offset(skip).limit(limit).all()

    def get_entity_71_by_id(self, entity_id: int) -> Optional[FinanceModelEntity71]:
        return self.db.query(FinanceModelEntity71).filter(FinanceModelEntity71.id == entity_id).first()

    def create_entity_71(self, payload: FinanceSchemaEntity71Create) -> FinanceModelEntity71:
        db_obj = FinanceModelEntity71(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_71(self, entity_id: int, payload: FinanceSchemaEntity71Update) -> Optional[FinanceModelEntity71]:
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

    def get_entity_72_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity72]:
        return self.db.query(FinanceModelEntity72).offset(skip).limit(limit).all()

    def get_entity_72_by_id(self, entity_id: int) -> Optional[FinanceModelEntity72]:
        return self.db.query(FinanceModelEntity72).filter(FinanceModelEntity72.id == entity_id).first()

    def create_entity_72(self, payload: FinanceSchemaEntity72Create) -> FinanceModelEntity72:
        db_obj = FinanceModelEntity72(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_72(self, entity_id: int, payload: FinanceSchemaEntity72Update) -> Optional[FinanceModelEntity72]:
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

    def get_entity_73_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity73]:
        return self.db.query(FinanceModelEntity73).offset(skip).limit(limit).all()

    def get_entity_73_by_id(self, entity_id: int) -> Optional[FinanceModelEntity73]:
        return self.db.query(FinanceModelEntity73).filter(FinanceModelEntity73.id == entity_id).first()

    def create_entity_73(self, payload: FinanceSchemaEntity73Create) -> FinanceModelEntity73:
        db_obj = FinanceModelEntity73(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_73(self, entity_id: int, payload: FinanceSchemaEntity73Update) -> Optional[FinanceModelEntity73]:
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

    def get_entity_74_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity74]:
        return self.db.query(FinanceModelEntity74).offset(skip).limit(limit).all()

    def get_entity_74_by_id(self, entity_id: int) -> Optional[FinanceModelEntity74]:
        return self.db.query(FinanceModelEntity74).filter(FinanceModelEntity74.id == entity_id).first()

    def create_entity_74(self, payload: FinanceSchemaEntity74Create) -> FinanceModelEntity74:
        db_obj = FinanceModelEntity74(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_74(self, entity_id: int, payload: FinanceSchemaEntity74Update) -> Optional[FinanceModelEntity74]:
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

    def get_entity_75_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity75]:
        return self.db.query(FinanceModelEntity75).offset(skip).limit(limit).all()

    def get_entity_75_by_id(self, entity_id: int) -> Optional[FinanceModelEntity75]:
        return self.db.query(FinanceModelEntity75).filter(FinanceModelEntity75.id == entity_id).first()

    def create_entity_75(self, payload: FinanceSchemaEntity75Create) -> FinanceModelEntity75:
        db_obj = FinanceModelEntity75(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_75(self, entity_id: int, payload: FinanceSchemaEntity75Update) -> Optional[FinanceModelEntity75]:
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

    def get_entity_76_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity76]:
        return self.db.query(FinanceModelEntity76).offset(skip).limit(limit).all()

    def get_entity_76_by_id(self, entity_id: int) -> Optional[FinanceModelEntity76]:
        return self.db.query(FinanceModelEntity76).filter(FinanceModelEntity76.id == entity_id).first()

    def create_entity_76(self, payload: FinanceSchemaEntity76Create) -> FinanceModelEntity76:
        db_obj = FinanceModelEntity76(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_76(self, entity_id: int, payload: FinanceSchemaEntity76Update) -> Optional[FinanceModelEntity76]:
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

    def get_entity_77_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity77]:
        return self.db.query(FinanceModelEntity77).offset(skip).limit(limit).all()

    def get_entity_77_by_id(self, entity_id: int) -> Optional[FinanceModelEntity77]:
        return self.db.query(FinanceModelEntity77).filter(FinanceModelEntity77.id == entity_id).first()

    def create_entity_77(self, payload: FinanceSchemaEntity77Create) -> FinanceModelEntity77:
        db_obj = FinanceModelEntity77(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_77(self, entity_id: int, payload: FinanceSchemaEntity77Update) -> Optional[FinanceModelEntity77]:
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

    def get_entity_78_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity78]:
        return self.db.query(FinanceModelEntity78).offset(skip).limit(limit).all()

    def get_entity_78_by_id(self, entity_id: int) -> Optional[FinanceModelEntity78]:
        return self.db.query(FinanceModelEntity78).filter(FinanceModelEntity78.id == entity_id).first()

    def create_entity_78(self, payload: FinanceSchemaEntity78Create) -> FinanceModelEntity78:
        db_obj = FinanceModelEntity78(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_78(self, entity_id: int, payload: FinanceSchemaEntity78Update) -> Optional[FinanceModelEntity78]:
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

    def get_entity_79_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity79]:
        return self.db.query(FinanceModelEntity79).offset(skip).limit(limit).all()

    def get_entity_79_by_id(self, entity_id: int) -> Optional[FinanceModelEntity79]:
        return self.db.query(FinanceModelEntity79).filter(FinanceModelEntity79.id == entity_id).first()

    def create_entity_79(self, payload: FinanceSchemaEntity79Create) -> FinanceModelEntity79:
        db_obj = FinanceModelEntity79(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_79(self, entity_id: int, payload: FinanceSchemaEntity79Update) -> Optional[FinanceModelEntity79]:
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

    def get_entity_80_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity80]:
        return self.db.query(FinanceModelEntity80).offset(skip).limit(limit).all()

    def get_entity_80_by_id(self, entity_id: int) -> Optional[FinanceModelEntity80]:
        return self.db.query(FinanceModelEntity80).filter(FinanceModelEntity80.id == entity_id).first()

    def create_entity_80(self, payload: FinanceSchemaEntity80Create) -> FinanceModelEntity80:
        db_obj = FinanceModelEntity80(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_80(self, entity_id: int, payload: FinanceSchemaEntity80Update) -> Optional[FinanceModelEntity80]:
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

    def get_entity_81_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity81]:
        return self.db.query(FinanceModelEntity81).offset(skip).limit(limit).all()

    def get_entity_81_by_id(self, entity_id: int) -> Optional[FinanceModelEntity81]:
        return self.db.query(FinanceModelEntity81).filter(FinanceModelEntity81.id == entity_id).first()

    def create_entity_81(self, payload: FinanceSchemaEntity81Create) -> FinanceModelEntity81:
        db_obj = FinanceModelEntity81(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_81(self, entity_id: int, payload: FinanceSchemaEntity81Update) -> Optional[FinanceModelEntity81]:
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

    def get_entity_82_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity82]:
        return self.db.query(FinanceModelEntity82).offset(skip).limit(limit).all()

    def get_entity_82_by_id(self, entity_id: int) -> Optional[FinanceModelEntity82]:
        return self.db.query(FinanceModelEntity82).filter(FinanceModelEntity82.id == entity_id).first()

    def create_entity_82(self, payload: FinanceSchemaEntity82Create) -> FinanceModelEntity82:
        db_obj = FinanceModelEntity82(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_82(self, entity_id: int, payload: FinanceSchemaEntity82Update) -> Optional[FinanceModelEntity82]:
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

    def get_entity_83_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity83]:
        return self.db.query(FinanceModelEntity83).offset(skip).limit(limit).all()

    def get_entity_83_by_id(self, entity_id: int) -> Optional[FinanceModelEntity83]:
        return self.db.query(FinanceModelEntity83).filter(FinanceModelEntity83.id == entity_id).first()

    def create_entity_83(self, payload: FinanceSchemaEntity83Create) -> FinanceModelEntity83:
        db_obj = FinanceModelEntity83(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_83(self, entity_id: int, payload: FinanceSchemaEntity83Update) -> Optional[FinanceModelEntity83]:
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

    def get_entity_84_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity84]:
        return self.db.query(FinanceModelEntity84).offset(skip).limit(limit).all()

    def get_entity_84_by_id(self, entity_id: int) -> Optional[FinanceModelEntity84]:
        return self.db.query(FinanceModelEntity84).filter(FinanceModelEntity84.id == entity_id).first()

    def create_entity_84(self, payload: FinanceSchemaEntity84Create) -> FinanceModelEntity84:
        db_obj = FinanceModelEntity84(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_84(self, entity_id: int, payload: FinanceSchemaEntity84Update) -> Optional[FinanceModelEntity84]:
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

    def get_entity_85_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity85]:
        return self.db.query(FinanceModelEntity85).offset(skip).limit(limit).all()

    def get_entity_85_by_id(self, entity_id: int) -> Optional[FinanceModelEntity85]:
        return self.db.query(FinanceModelEntity85).filter(FinanceModelEntity85.id == entity_id).first()

    def create_entity_85(self, payload: FinanceSchemaEntity85Create) -> FinanceModelEntity85:
        db_obj = FinanceModelEntity85(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_85(self, entity_id: int, payload: FinanceSchemaEntity85Update) -> Optional[FinanceModelEntity85]:
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

    def get_entity_86_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity86]:
        return self.db.query(FinanceModelEntity86).offset(skip).limit(limit).all()

    def get_entity_86_by_id(self, entity_id: int) -> Optional[FinanceModelEntity86]:
        return self.db.query(FinanceModelEntity86).filter(FinanceModelEntity86.id == entity_id).first()

    def create_entity_86(self, payload: FinanceSchemaEntity86Create) -> FinanceModelEntity86:
        db_obj = FinanceModelEntity86(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_86(self, entity_id: int, payload: FinanceSchemaEntity86Update) -> Optional[FinanceModelEntity86]:
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

    def get_entity_87_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity87]:
        return self.db.query(FinanceModelEntity87).offset(skip).limit(limit).all()

    def get_entity_87_by_id(self, entity_id: int) -> Optional[FinanceModelEntity87]:
        return self.db.query(FinanceModelEntity87).filter(FinanceModelEntity87.id == entity_id).first()

    def create_entity_87(self, payload: FinanceSchemaEntity87Create) -> FinanceModelEntity87:
        db_obj = FinanceModelEntity87(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_87(self, entity_id: int, payload: FinanceSchemaEntity87Update) -> Optional[FinanceModelEntity87]:
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

    def get_entity_88_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity88]:
        return self.db.query(FinanceModelEntity88).offset(skip).limit(limit).all()

    def get_entity_88_by_id(self, entity_id: int) -> Optional[FinanceModelEntity88]:
        return self.db.query(FinanceModelEntity88).filter(FinanceModelEntity88.id == entity_id).first()

    def create_entity_88(self, payload: FinanceSchemaEntity88Create) -> FinanceModelEntity88:
        db_obj = FinanceModelEntity88(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_88(self, entity_id: int, payload: FinanceSchemaEntity88Update) -> Optional[FinanceModelEntity88]:
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

    def get_entity_89_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity89]:
        return self.db.query(FinanceModelEntity89).offset(skip).limit(limit).all()

    def get_entity_89_by_id(self, entity_id: int) -> Optional[FinanceModelEntity89]:
        return self.db.query(FinanceModelEntity89).filter(FinanceModelEntity89.id == entity_id).first()

    def create_entity_89(self, payload: FinanceSchemaEntity89Create) -> FinanceModelEntity89:
        db_obj = FinanceModelEntity89(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_89(self, entity_id: int, payload: FinanceSchemaEntity89Update) -> Optional[FinanceModelEntity89]:
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

    def get_entity_90_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity90]:
        return self.db.query(FinanceModelEntity90).offset(skip).limit(limit).all()

    def get_entity_90_by_id(self, entity_id: int) -> Optional[FinanceModelEntity90]:
        return self.db.query(FinanceModelEntity90).filter(FinanceModelEntity90.id == entity_id).first()

    def create_entity_90(self, payload: FinanceSchemaEntity90Create) -> FinanceModelEntity90:
        db_obj = FinanceModelEntity90(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_90(self, entity_id: int, payload: FinanceSchemaEntity90Update) -> Optional[FinanceModelEntity90]:
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

    def get_entity_91_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity91]:
        return self.db.query(FinanceModelEntity91).offset(skip).limit(limit).all()

    def get_entity_91_by_id(self, entity_id: int) -> Optional[FinanceModelEntity91]:
        return self.db.query(FinanceModelEntity91).filter(FinanceModelEntity91.id == entity_id).first()

    def create_entity_91(self, payload: FinanceSchemaEntity91Create) -> FinanceModelEntity91:
        db_obj = FinanceModelEntity91(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_91(self, entity_id: int, payload: FinanceSchemaEntity91Update) -> Optional[FinanceModelEntity91]:
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

    def get_entity_92_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity92]:
        return self.db.query(FinanceModelEntity92).offset(skip).limit(limit).all()

    def get_entity_92_by_id(self, entity_id: int) -> Optional[FinanceModelEntity92]:
        return self.db.query(FinanceModelEntity92).filter(FinanceModelEntity92.id == entity_id).first()

    def create_entity_92(self, payload: FinanceSchemaEntity92Create) -> FinanceModelEntity92:
        db_obj = FinanceModelEntity92(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_92(self, entity_id: int, payload: FinanceSchemaEntity92Update) -> Optional[FinanceModelEntity92]:
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

    def get_entity_93_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity93]:
        return self.db.query(FinanceModelEntity93).offset(skip).limit(limit).all()

    def get_entity_93_by_id(self, entity_id: int) -> Optional[FinanceModelEntity93]:
        return self.db.query(FinanceModelEntity93).filter(FinanceModelEntity93.id == entity_id).first()

    def create_entity_93(self, payload: FinanceSchemaEntity93Create) -> FinanceModelEntity93:
        db_obj = FinanceModelEntity93(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_93(self, entity_id: int, payload: FinanceSchemaEntity93Update) -> Optional[FinanceModelEntity93]:
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

    def get_entity_94_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity94]:
        return self.db.query(FinanceModelEntity94).offset(skip).limit(limit).all()

    def get_entity_94_by_id(self, entity_id: int) -> Optional[FinanceModelEntity94]:
        return self.db.query(FinanceModelEntity94).filter(FinanceModelEntity94.id == entity_id).first()

    def create_entity_94(self, payload: FinanceSchemaEntity94Create) -> FinanceModelEntity94:
        db_obj = FinanceModelEntity94(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_94(self, entity_id: int, payload: FinanceSchemaEntity94Update) -> Optional[FinanceModelEntity94]:
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

    def get_entity_95_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity95]:
        return self.db.query(FinanceModelEntity95).offset(skip).limit(limit).all()

    def get_entity_95_by_id(self, entity_id: int) -> Optional[FinanceModelEntity95]:
        return self.db.query(FinanceModelEntity95).filter(FinanceModelEntity95.id == entity_id).first()

    def create_entity_95(self, payload: FinanceSchemaEntity95Create) -> FinanceModelEntity95:
        db_obj = FinanceModelEntity95(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_95(self, entity_id: int, payload: FinanceSchemaEntity95Update) -> Optional[FinanceModelEntity95]:
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

    def get_entity_96_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity96]:
        return self.db.query(FinanceModelEntity96).offset(skip).limit(limit).all()

    def get_entity_96_by_id(self, entity_id: int) -> Optional[FinanceModelEntity96]:
        return self.db.query(FinanceModelEntity96).filter(FinanceModelEntity96.id == entity_id).first()

    def create_entity_96(self, payload: FinanceSchemaEntity96Create) -> FinanceModelEntity96:
        db_obj = FinanceModelEntity96(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_96(self, entity_id: int, payload: FinanceSchemaEntity96Update) -> Optional[FinanceModelEntity96]:
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

    def get_entity_97_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity97]:
        return self.db.query(FinanceModelEntity97).offset(skip).limit(limit).all()

    def get_entity_97_by_id(self, entity_id: int) -> Optional[FinanceModelEntity97]:
        return self.db.query(FinanceModelEntity97).filter(FinanceModelEntity97.id == entity_id).first()

    def create_entity_97(self, payload: FinanceSchemaEntity97Create) -> FinanceModelEntity97:
        db_obj = FinanceModelEntity97(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_97(self, entity_id: int, payload: FinanceSchemaEntity97Update) -> Optional[FinanceModelEntity97]:
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

    def get_entity_98_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity98]:
        return self.db.query(FinanceModelEntity98).offset(skip).limit(limit).all()

    def get_entity_98_by_id(self, entity_id: int) -> Optional[FinanceModelEntity98]:
        return self.db.query(FinanceModelEntity98).filter(FinanceModelEntity98.id == entity_id).first()

    def create_entity_98(self, payload: FinanceSchemaEntity98Create) -> FinanceModelEntity98:
        db_obj = FinanceModelEntity98(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_98(self, entity_id: int, payload: FinanceSchemaEntity98Update) -> Optional[FinanceModelEntity98]:
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

    def get_entity_99_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity99]:
        return self.db.query(FinanceModelEntity99).offset(skip).limit(limit).all()

    def get_entity_99_by_id(self, entity_id: int) -> Optional[FinanceModelEntity99]:
        return self.db.query(FinanceModelEntity99).filter(FinanceModelEntity99.id == entity_id).first()

    def create_entity_99(self, payload: FinanceSchemaEntity99Create) -> FinanceModelEntity99:
        db_obj = FinanceModelEntity99(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_99(self, entity_id: int, payload: FinanceSchemaEntity99Update) -> Optional[FinanceModelEntity99]:
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

    def get_entity_100_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity100]:
        return self.db.query(FinanceModelEntity100).offset(skip).limit(limit).all()

    def get_entity_100_by_id(self, entity_id: int) -> Optional[FinanceModelEntity100]:
        return self.db.query(FinanceModelEntity100).filter(FinanceModelEntity100.id == entity_id).first()

    def create_entity_100(self, payload: FinanceSchemaEntity100Create) -> FinanceModelEntity100:
        db_obj = FinanceModelEntity100(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_100(self, entity_id: int, payload: FinanceSchemaEntity100Update) -> Optional[FinanceModelEntity100]:
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

    def get_entity_101_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity101]:
        return self.db.query(FinanceModelEntity101).offset(skip).limit(limit).all()

    def get_entity_101_by_id(self, entity_id: int) -> Optional[FinanceModelEntity101]:
        return self.db.query(FinanceModelEntity101).filter(FinanceModelEntity101.id == entity_id).first()

    def create_entity_101(self, payload: FinanceSchemaEntity101Create) -> FinanceModelEntity101:
        db_obj = FinanceModelEntity101(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_101(self, entity_id: int, payload: FinanceSchemaEntity101Update) -> Optional[FinanceModelEntity101]:
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

    def get_entity_102_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity102]:
        return self.db.query(FinanceModelEntity102).offset(skip).limit(limit).all()

    def get_entity_102_by_id(self, entity_id: int) -> Optional[FinanceModelEntity102]:
        return self.db.query(FinanceModelEntity102).filter(FinanceModelEntity102.id == entity_id).first()

    def create_entity_102(self, payload: FinanceSchemaEntity102Create) -> FinanceModelEntity102:
        db_obj = FinanceModelEntity102(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_102(self, entity_id: int, payload: FinanceSchemaEntity102Update) -> Optional[FinanceModelEntity102]:
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

    def get_entity_103_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity103]:
        return self.db.query(FinanceModelEntity103).offset(skip).limit(limit).all()

    def get_entity_103_by_id(self, entity_id: int) -> Optional[FinanceModelEntity103]:
        return self.db.query(FinanceModelEntity103).filter(FinanceModelEntity103.id == entity_id).first()

    def create_entity_103(self, payload: FinanceSchemaEntity103Create) -> FinanceModelEntity103:
        db_obj = FinanceModelEntity103(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_103(self, entity_id: int, payload: FinanceSchemaEntity103Update) -> Optional[FinanceModelEntity103]:
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

    def get_entity_104_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity104]:
        return self.db.query(FinanceModelEntity104).offset(skip).limit(limit).all()

    def get_entity_104_by_id(self, entity_id: int) -> Optional[FinanceModelEntity104]:
        return self.db.query(FinanceModelEntity104).filter(FinanceModelEntity104.id == entity_id).first()

    def create_entity_104(self, payload: FinanceSchemaEntity104Create) -> FinanceModelEntity104:
        db_obj = FinanceModelEntity104(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_104(self, entity_id: int, payload: FinanceSchemaEntity104Update) -> Optional[FinanceModelEntity104]:
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

    def get_entity_105_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity105]:
        return self.db.query(FinanceModelEntity105).offset(skip).limit(limit).all()

    def get_entity_105_by_id(self, entity_id: int) -> Optional[FinanceModelEntity105]:
        return self.db.query(FinanceModelEntity105).filter(FinanceModelEntity105.id == entity_id).first()

    def create_entity_105(self, payload: FinanceSchemaEntity105Create) -> FinanceModelEntity105:
        db_obj = FinanceModelEntity105(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_105(self, entity_id: int, payload: FinanceSchemaEntity105Update) -> Optional[FinanceModelEntity105]:
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

    def get_entity_106_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity106]:
        return self.db.query(FinanceModelEntity106).offset(skip).limit(limit).all()

    def get_entity_106_by_id(self, entity_id: int) -> Optional[FinanceModelEntity106]:
        return self.db.query(FinanceModelEntity106).filter(FinanceModelEntity106.id == entity_id).first()

    def create_entity_106(self, payload: FinanceSchemaEntity106Create) -> FinanceModelEntity106:
        db_obj = FinanceModelEntity106(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_106(self, entity_id: int, payload: FinanceSchemaEntity106Update) -> Optional[FinanceModelEntity106]:
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

    def get_entity_107_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity107]:
        return self.db.query(FinanceModelEntity107).offset(skip).limit(limit).all()

    def get_entity_107_by_id(self, entity_id: int) -> Optional[FinanceModelEntity107]:
        return self.db.query(FinanceModelEntity107).filter(FinanceModelEntity107.id == entity_id).first()

    def create_entity_107(self, payload: FinanceSchemaEntity107Create) -> FinanceModelEntity107:
        db_obj = FinanceModelEntity107(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_107(self, entity_id: int, payload: FinanceSchemaEntity107Update) -> Optional[FinanceModelEntity107]:
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

    def get_entity_108_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity108]:
        return self.db.query(FinanceModelEntity108).offset(skip).limit(limit).all()

    def get_entity_108_by_id(self, entity_id: int) -> Optional[FinanceModelEntity108]:
        return self.db.query(FinanceModelEntity108).filter(FinanceModelEntity108.id == entity_id).first()

    def create_entity_108(self, payload: FinanceSchemaEntity108Create) -> FinanceModelEntity108:
        db_obj = FinanceModelEntity108(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_108(self, entity_id: int, payload: FinanceSchemaEntity108Update) -> Optional[FinanceModelEntity108]:
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

    def get_entity_109_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity109]:
        return self.db.query(FinanceModelEntity109).offset(skip).limit(limit).all()

    def get_entity_109_by_id(self, entity_id: int) -> Optional[FinanceModelEntity109]:
        return self.db.query(FinanceModelEntity109).filter(FinanceModelEntity109.id == entity_id).first()

    def create_entity_109(self, payload: FinanceSchemaEntity109Create) -> FinanceModelEntity109:
        db_obj = FinanceModelEntity109(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_109(self, entity_id: int, payload: FinanceSchemaEntity109Update) -> Optional[FinanceModelEntity109]:
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

    def get_entity_110_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity110]:
        return self.db.query(FinanceModelEntity110).offset(skip).limit(limit).all()

    def get_entity_110_by_id(self, entity_id: int) -> Optional[FinanceModelEntity110]:
        return self.db.query(FinanceModelEntity110).filter(FinanceModelEntity110.id == entity_id).first()

    def create_entity_110(self, payload: FinanceSchemaEntity110Create) -> FinanceModelEntity110:
        db_obj = FinanceModelEntity110(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_110(self, entity_id: int, payload: FinanceSchemaEntity110Update) -> Optional[FinanceModelEntity110]:
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

    def get_entity_111_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity111]:
        return self.db.query(FinanceModelEntity111).offset(skip).limit(limit).all()

    def get_entity_111_by_id(self, entity_id: int) -> Optional[FinanceModelEntity111]:
        return self.db.query(FinanceModelEntity111).filter(FinanceModelEntity111.id == entity_id).first()

    def create_entity_111(self, payload: FinanceSchemaEntity111Create) -> FinanceModelEntity111:
        db_obj = FinanceModelEntity111(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_111(self, entity_id: int, payload: FinanceSchemaEntity111Update) -> Optional[FinanceModelEntity111]:
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

    def get_entity_112_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity112]:
        return self.db.query(FinanceModelEntity112).offset(skip).limit(limit).all()

    def get_entity_112_by_id(self, entity_id: int) -> Optional[FinanceModelEntity112]:
        return self.db.query(FinanceModelEntity112).filter(FinanceModelEntity112.id == entity_id).first()

    def create_entity_112(self, payload: FinanceSchemaEntity112Create) -> FinanceModelEntity112:
        db_obj = FinanceModelEntity112(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_112(self, entity_id: int, payload: FinanceSchemaEntity112Update) -> Optional[FinanceModelEntity112]:
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

    def get_entity_113_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity113]:
        return self.db.query(FinanceModelEntity113).offset(skip).limit(limit).all()

    def get_entity_113_by_id(self, entity_id: int) -> Optional[FinanceModelEntity113]:
        return self.db.query(FinanceModelEntity113).filter(FinanceModelEntity113.id == entity_id).first()

    def create_entity_113(self, payload: FinanceSchemaEntity113Create) -> FinanceModelEntity113:
        db_obj = FinanceModelEntity113(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_113(self, entity_id: int, payload: FinanceSchemaEntity113Update) -> Optional[FinanceModelEntity113]:
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

    def get_entity_114_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity114]:
        return self.db.query(FinanceModelEntity114).offset(skip).limit(limit).all()

    def get_entity_114_by_id(self, entity_id: int) -> Optional[FinanceModelEntity114]:
        return self.db.query(FinanceModelEntity114).filter(FinanceModelEntity114.id == entity_id).first()

    def create_entity_114(self, payload: FinanceSchemaEntity114Create) -> FinanceModelEntity114:
        db_obj = FinanceModelEntity114(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_114(self, entity_id: int, payload: FinanceSchemaEntity114Update) -> Optional[FinanceModelEntity114]:
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

    def get_entity_115_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity115]:
        return self.db.query(FinanceModelEntity115).offset(skip).limit(limit).all()

    def get_entity_115_by_id(self, entity_id: int) -> Optional[FinanceModelEntity115]:
        return self.db.query(FinanceModelEntity115).filter(FinanceModelEntity115.id == entity_id).first()

    def create_entity_115(self, payload: FinanceSchemaEntity115Create) -> FinanceModelEntity115:
        db_obj = FinanceModelEntity115(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_115(self, entity_id: int, payload: FinanceSchemaEntity115Update) -> Optional[FinanceModelEntity115]:
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

    def get_entity_116_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity116]:
        return self.db.query(FinanceModelEntity116).offset(skip).limit(limit).all()

    def get_entity_116_by_id(self, entity_id: int) -> Optional[FinanceModelEntity116]:
        return self.db.query(FinanceModelEntity116).filter(FinanceModelEntity116.id == entity_id).first()

    def create_entity_116(self, payload: FinanceSchemaEntity116Create) -> FinanceModelEntity116:
        db_obj = FinanceModelEntity116(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_116(self, entity_id: int, payload: FinanceSchemaEntity116Update) -> Optional[FinanceModelEntity116]:
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

    def get_entity_117_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity117]:
        return self.db.query(FinanceModelEntity117).offset(skip).limit(limit).all()

    def get_entity_117_by_id(self, entity_id: int) -> Optional[FinanceModelEntity117]:
        return self.db.query(FinanceModelEntity117).filter(FinanceModelEntity117.id == entity_id).first()

    def create_entity_117(self, payload: FinanceSchemaEntity117Create) -> FinanceModelEntity117:
        db_obj = FinanceModelEntity117(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_117(self, entity_id: int, payload: FinanceSchemaEntity117Update) -> Optional[FinanceModelEntity117]:
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

    def get_entity_118_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity118]:
        return self.db.query(FinanceModelEntity118).offset(skip).limit(limit).all()

    def get_entity_118_by_id(self, entity_id: int) -> Optional[FinanceModelEntity118]:
        return self.db.query(FinanceModelEntity118).filter(FinanceModelEntity118.id == entity_id).first()

    def create_entity_118(self, payload: FinanceSchemaEntity118Create) -> FinanceModelEntity118:
        db_obj = FinanceModelEntity118(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_118(self, entity_id: int, payload: FinanceSchemaEntity118Update) -> Optional[FinanceModelEntity118]:
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

    def get_entity_119_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity119]:
        return self.db.query(FinanceModelEntity119).offset(skip).limit(limit).all()

    def get_entity_119_by_id(self, entity_id: int) -> Optional[FinanceModelEntity119]:
        return self.db.query(FinanceModelEntity119).filter(FinanceModelEntity119.id == entity_id).first()

    def create_entity_119(self, payload: FinanceSchemaEntity119Create) -> FinanceModelEntity119:
        db_obj = FinanceModelEntity119(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_119(self, entity_id: int, payload: FinanceSchemaEntity119Update) -> Optional[FinanceModelEntity119]:
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

    def get_entity_120_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity120]:
        return self.db.query(FinanceModelEntity120).offset(skip).limit(limit).all()

    def get_entity_120_by_id(self, entity_id: int) -> Optional[FinanceModelEntity120]:
        return self.db.query(FinanceModelEntity120).filter(FinanceModelEntity120.id == entity_id).first()

    def create_entity_120(self, payload: FinanceSchemaEntity120Create) -> FinanceModelEntity120:
        db_obj = FinanceModelEntity120(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_120(self, entity_id: int, payload: FinanceSchemaEntity120Update) -> Optional[FinanceModelEntity120]:
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

    def get_entity_121_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity121]:
        return self.db.query(FinanceModelEntity121).offset(skip).limit(limit).all()

    def get_entity_121_by_id(self, entity_id: int) -> Optional[FinanceModelEntity121]:
        return self.db.query(FinanceModelEntity121).filter(FinanceModelEntity121.id == entity_id).first()

    def create_entity_121(self, payload: FinanceSchemaEntity121Create) -> FinanceModelEntity121:
        db_obj = FinanceModelEntity121(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_121(self, entity_id: int, payload: FinanceSchemaEntity121Update) -> Optional[FinanceModelEntity121]:
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

    def get_entity_122_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity122]:
        return self.db.query(FinanceModelEntity122).offset(skip).limit(limit).all()

    def get_entity_122_by_id(self, entity_id: int) -> Optional[FinanceModelEntity122]:
        return self.db.query(FinanceModelEntity122).filter(FinanceModelEntity122.id == entity_id).first()

    def create_entity_122(self, payload: FinanceSchemaEntity122Create) -> FinanceModelEntity122:
        db_obj = FinanceModelEntity122(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_122(self, entity_id: int, payload: FinanceSchemaEntity122Update) -> Optional[FinanceModelEntity122]:
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

    def get_entity_123_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity123]:
        return self.db.query(FinanceModelEntity123).offset(skip).limit(limit).all()

    def get_entity_123_by_id(self, entity_id: int) -> Optional[FinanceModelEntity123]:
        return self.db.query(FinanceModelEntity123).filter(FinanceModelEntity123.id == entity_id).first()

    def create_entity_123(self, payload: FinanceSchemaEntity123Create) -> FinanceModelEntity123:
        db_obj = FinanceModelEntity123(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_123(self, entity_id: int, payload: FinanceSchemaEntity123Update) -> Optional[FinanceModelEntity123]:
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

    def get_entity_124_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity124]:
        return self.db.query(FinanceModelEntity124).offset(skip).limit(limit).all()

    def get_entity_124_by_id(self, entity_id: int) -> Optional[FinanceModelEntity124]:
        return self.db.query(FinanceModelEntity124).filter(FinanceModelEntity124.id == entity_id).first()

    def create_entity_124(self, payload: FinanceSchemaEntity124Create) -> FinanceModelEntity124:
        db_obj = FinanceModelEntity124(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_124(self, entity_id: int, payload: FinanceSchemaEntity124Update) -> Optional[FinanceModelEntity124]:
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

    def get_entity_125_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity125]:
        return self.db.query(FinanceModelEntity125).offset(skip).limit(limit).all()

    def get_entity_125_by_id(self, entity_id: int) -> Optional[FinanceModelEntity125]:
        return self.db.query(FinanceModelEntity125).filter(FinanceModelEntity125.id == entity_id).first()

    def create_entity_125(self, payload: FinanceSchemaEntity125Create) -> FinanceModelEntity125:
        db_obj = FinanceModelEntity125(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_125(self, entity_id: int, payload: FinanceSchemaEntity125Update) -> Optional[FinanceModelEntity125]:
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

    def get_entity_126_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity126]:
        return self.db.query(FinanceModelEntity126).offset(skip).limit(limit).all()

    def get_entity_126_by_id(self, entity_id: int) -> Optional[FinanceModelEntity126]:
        return self.db.query(FinanceModelEntity126).filter(FinanceModelEntity126.id == entity_id).first()

    def create_entity_126(self, payload: FinanceSchemaEntity126Create) -> FinanceModelEntity126:
        db_obj = FinanceModelEntity126(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_126(self, entity_id: int, payload: FinanceSchemaEntity126Update) -> Optional[FinanceModelEntity126]:
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

    def get_entity_127_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity127]:
        return self.db.query(FinanceModelEntity127).offset(skip).limit(limit).all()

    def get_entity_127_by_id(self, entity_id: int) -> Optional[FinanceModelEntity127]:
        return self.db.query(FinanceModelEntity127).filter(FinanceModelEntity127.id == entity_id).first()

    def create_entity_127(self, payload: FinanceSchemaEntity127Create) -> FinanceModelEntity127:
        db_obj = FinanceModelEntity127(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_127(self, entity_id: int, payload: FinanceSchemaEntity127Update) -> Optional[FinanceModelEntity127]:
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

    def get_entity_128_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity128]:
        return self.db.query(FinanceModelEntity128).offset(skip).limit(limit).all()

    def get_entity_128_by_id(self, entity_id: int) -> Optional[FinanceModelEntity128]:
        return self.db.query(FinanceModelEntity128).filter(FinanceModelEntity128.id == entity_id).first()

    def create_entity_128(self, payload: FinanceSchemaEntity128Create) -> FinanceModelEntity128:
        db_obj = FinanceModelEntity128(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_128(self, entity_id: int, payload: FinanceSchemaEntity128Update) -> Optional[FinanceModelEntity128]:
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

    def get_entity_129_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity129]:
        return self.db.query(FinanceModelEntity129).offset(skip).limit(limit).all()

    def get_entity_129_by_id(self, entity_id: int) -> Optional[FinanceModelEntity129]:
        return self.db.query(FinanceModelEntity129).filter(FinanceModelEntity129.id == entity_id).first()

    def create_entity_129(self, payload: FinanceSchemaEntity129Create) -> FinanceModelEntity129:
        db_obj = FinanceModelEntity129(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_129(self, entity_id: int, payload: FinanceSchemaEntity129Update) -> Optional[FinanceModelEntity129]:
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

    def get_entity_130_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity130]:
        return self.db.query(FinanceModelEntity130).offset(skip).limit(limit).all()

    def get_entity_130_by_id(self, entity_id: int) -> Optional[FinanceModelEntity130]:
        return self.db.query(FinanceModelEntity130).filter(FinanceModelEntity130.id == entity_id).first()

    def create_entity_130(self, payload: FinanceSchemaEntity130Create) -> FinanceModelEntity130:
        db_obj = FinanceModelEntity130(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_130(self, entity_id: int, payload: FinanceSchemaEntity130Update) -> Optional[FinanceModelEntity130]:
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

    def get_entity_131_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity131]:
        return self.db.query(FinanceModelEntity131).offset(skip).limit(limit).all()

    def get_entity_131_by_id(self, entity_id: int) -> Optional[FinanceModelEntity131]:
        return self.db.query(FinanceModelEntity131).filter(FinanceModelEntity131.id == entity_id).first()

    def create_entity_131(self, payload: FinanceSchemaEntity131Create) -> FinanceModelEntity131:
        db_obj = FinanceModelEntity131(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_131(self, entity_id: int, payload: FinanceSchemaEntity131Update) -> Optional[FinanceModelEntity131]:
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

    def get_entity_132_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity132]:
        return self.db.query(FinanceModelEntity132).offset(skip).limit(limit).all()

    def get_entity_132_by_id(self, entity_id: int) -> Optional[FinanceModelEntity132]:
        return self.db.query(FinanceModelEntity132).filter(FinanceModelEntity132.id == entity_id).first()

    def create_entity_132(self, payload: FinanceSchemaEntity132Create) -> FinanceModelEntity132:
        db_obj = FinanceModelEntity132(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_132(self, entity_id: int, payload: FinanceSchemaEntity132Update) -> Optional[FinanceModelEntity132]:
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

    def get_entity_133_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity133]:
        return self.db.query(FinanceModelEntity133).offset(skip).limit(limit).all()

    def get_entity_133_by_id(self, entity_id: int) -> Optional[FinanceModelEntity133]:
        return self.db.query(FinanceModelEntity133).filter(FinanceModelEntity133.id == entity_id).first()

    def create_entity_133(self, payload: FinanceSchemaEntity133Create) -> FinanceModelEntity133:
        db_obj = FinanceModelEntity133(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_133(self, entity_id: int, payload: FinanceSchemaEntity133Update) -> Optional[FinanceModelEntity133]:
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

    def get_entity_134_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity134]:
        return self.db.query(FinanceModelEntity134).offset(skip).limit(limit).all()

    def get_entity_134_by_id(self, entity_id: int) -> Optional[FinanceModelEntity134]:
        return self.db.query(FinanceModelEntity134).filter(FinanceModelEntity134.id == entity_id).first()

    def create_entity_134(self, payload: FinanceSchemaEntity134Create) -> FinanceModelEntity134:
        db_obj = FinanceModelEntity134(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_134(self, entity_id: int, payload: FinanceSchemaEntity134Update) -> Optional[FinanceModelEntity134]:
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

    def get_entity_135_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity135]:
        return self.db.query(FinanceModelEntity135).offset(skip).limit(limit).all()

    def get_entity_135_by_id(self, entity_id: int) -> Optional[FinanceModelEntity135]:
        return self.db.query(FinanceModelEntity135).filter(FinanceModelEntity135.id == entity_id).first()

    def create_entity_135(self, payload: FinanceSchemaEntity135Create) -> FinanceModelEntity135:
        db_obj = FinanceModelEntity135(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_135(self, entity_id: int, payload: FinanceSchemaEntity135Update) -> Optional[FinanceModelEntity135]:
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

    def get_entity_136_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity136]:
        return self.db.query(FinanceModelEntity136).offset(skip).limit(limit).all()

    def get_entity_136_by_id(self, entity_id: int) -> Optional[FinanceModelEntity136]:
        return self.db.query(FinanceModelEntity136).filter(FinanceModelEntity136.id == entity_id).first()

    def create_entity_136(self, payload: FinanceSchemaEntity136Create) -> FinanceModelEntity136:
        db_obj = FinanceModelEntity136(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_136(self, entity_id: int, payload: FinanceSchemaEntity136Update) -> Optional[FinanceModelEntity136]:
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

    def get_entity_137_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity137]:
        return self.db.query(FinanceModelEntity137).offset(skip).limit(limit).all()

    def get_entity_137_by_id(self, entity_id: int) -> Optional[FinanceModelEntity137]:
        return self.db.query(FinanceModelEntity137).filter(FinanceModelEntity137.id == entity_id).first()

    def create_entity_137(self, payload: FinanceSchemaEntity137Create) -> FinanceModelEntity137:
        db_obj = FinanceModelEntity137(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_137(self, entity_id: int, payload: FinanceSchemaEntity137Update) -> Optional[FinanceModelEntity137]:
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

    def get_entity_138_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity138]:
        return self.db.query(FinanceModelEntity138).offset(skip).limit(limit).all()

    def get_entity_138_by_id(self, entity_id: int) -> Optional[FinanceModelEntity138]:
        return self.db.query(FinanceModelEntity138).filter(FinanceModelEntity138.id == entity_id).first()

    def create_entity_138(self, payload: FinanceSchemaEntity138Create) -> FinanceModelEntity138:
        db_obj = FinanceModelEntity138(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_138(self, entity_id: int, payload: FinanceSchemaEntity138Update) -> Optional[FinanceModelEntity138]:
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

    def get_entity_139_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity139]:
        return self.db.query(FinanceModelEntity139).offset(skip).limit(limit).all()

    def get_entity_139_by_id(self, entity_id: int) -> Optional[FinanceModelEntity139]:
        return self.db.query(FinanceModelEntity139).filter(FinanceModelEntity139.id == entity_id).first()

    def create_entity_139(self, payload: FinanceSchemaEntity139Create) -> FinanceModelEntity139:
        db_obj = FinanceModelEntity139(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_139(self, entity_id: int, payload: FinanceSchemaEntity139Update) -> Optional[FinanceModelEntity139]:
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

    def get_entity_140_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity140]:
        return self.db.query(FinanceModelEntity140).offset(skip).limit(limit).all()

    def get_entity_140_by_id(self, entity_id: int) -> Optional[FinanceModelEntity140]:
        return self.db.query(FinanceModelEntity140).filter(FinanceModelEntity140.id == entity_id).first()

    def create_entity_140(self, payload: FinanceSchemaEntity140Create) -> FinanceModelEntity140:
        db_obj = FinanceModelEntity140(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_140(self, entity_id: int, payload: FinanceSchemaEntity140Update) -> Optional[FinanceModelEntity140]:
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

    def get_entity_141_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity141]:
        return self.db.query(FinanceModelEntity141).offset(skip).limit(limit).all()

    def get_entity_141_by_id(self, entity_id: int) -> Optional[FinanceModelEntity141]:
        return self.db.query(FinanceModelEntity141).filter(FinanceModelEntity141.id == entity_id).first()

    def create_entity_141(self, payload: FinanceSchemaEntity141Create) -> FinanceModelEntity141:
        db_obj = FinanceModelEntity141(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_141(self, entity_id: int, payload: FinanceSchemaEntity141Update) -> Optional[FinanceModelEntity141]:
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

    def get_entity_142_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity142]:
        return self.db.query(FinanceModelEntity142).offset(skip).limit(limit).all()

    def get_entity_142_by_id(self, entity_id: int) -> Optional[FinanceModelEntity142]:
        return self.db.query(FinanceModelEntity142).filter(FinanceModelEntity142.id == entity_id).first()

    def create_entity_142(self, payload: FinanceSchemaEntity142Create) -> FinanceModelEntity142:
        db_obj = FinanceModelEntity142(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_142(self, entity_id: int, payload: FinanceSchemaEntity142Update) -> Optional[FinanceModelEntity142]:
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

    def get_entity_143_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity143]:
        return self.db.query(FinanceModelEntity143).offset(skip).limit(limit).all()

    def get_entity_143_by_id(self, entity_id: int) -> Optional[FinanceModelEntity143]:
        return self.db.query(FinanceModelEntity143).filter(FinanceModelEntity143.id == entity_id).first()

    def create_entity_143(self, payload: FinanceSchemaEntity143Create) -> FinanceModelEntity143:
        db_obj = FinanceModelEntity143(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_143(self, entity_id: int, payload: FinanceSchemaEntity143Update) -> Optional[FinanceModelEntity143]:
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

    def get_entity_144_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity144]:
        return self.db.query(FinanceModelEntity144).offset(skip).limit(limit).all()

    def get_entity_144_by_id(self, entity_id: int) -> Optional[FinanceModelEntity144]:
        return self.db.query(FinanceModelEntity144).filter(FinanceModelEntity144.id == entity_id).first()

    def create_entity_144(self, payload: FinanceSchemaEntity144Create) -> FinanceModelEntity144:
        db_obj = FinanceModelEntity144(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_144(self, entity_id: int, payload: FinanceSchemaEntity144Update) -> Optional[FinanceModelEntity144]:
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

    def get_entity_145_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity145]:
        return self.db.query(FinanceModelEntity145).offset(skip).limit(limit).all()

    def get_entity_145_by_id(self, entity_id: int) -> Optional[FinanceModelEntity145]:
        return self.db.query(FinanceModelEntity145).filter(FinanceModelEntity145.id == entity_id).first()

    def create_entity_145(self, payload: FinanceSchemaEntity145Create) -> FinanceModelEntity145:
        db_obj = FinanceModelEntity145(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_145(self, entity_id: int, payload: FinanceSchemaEntity145Update) -> Optional[FinanceModelEntity145]:
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

    def get_entity_146_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity146]:
        return self.db.query(FinanceModelEntity146).offset(skip).limit(limit).all()

    def get_entity_146_by_id(self, entity_id: int) -> Optional[FinanceModelEntity146]:
        return self.db.query(FinanceModelEntity146).filter(FinanceModelEntity146.id == entity_id).first()

    def create_entity_146(self, payload: FinanceSchemaEntity146Create) -> FinanceModelEntity146:
        db_obj = FinanceModelEntity146(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_146(self, entity_id: int, payload: FinanceSchemaEntity146Update) -> Optional[FinanceModelEntity146]:
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

    def get_entity_147_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity147]:
        return self.db.query(FinanceModelEntity147).offset(skip).limit(limit).all()

    def get_entity_147_by_id(self, entity_id: int) -> Optional[FinanceModelEntity147]:
        return self.db.query(FinanceModelEntity147).filter(FinanceModelEntity147.id == entity_id).first()

    def create_entity_147(self, payload: FinanceSchemaEntity147Create) -> FinanceModelEntity147:
        db_obj = FinanceModelEntity147(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_147(self, entity_id: int, payload: FinanceSchemaEntity147Update) -> Optional[FinanceModelEntity147]:
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

    def get_entity_148_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity148]:
        return self.db.query(FinanceModelEntity148).offset(skip).limit(limit).all()

    def get_entity_148_by_id(self, entity_id: int) -> Optional[FinanceModelEntity148]:
        return self.db.query(FinanceModelEntity148).filter(FinanceModelEntity148.id == entity_id).first()

    def create_entity_148(self, payload: FinanceSchemaEntity148Create) -> FinanceModelEntity148:
        db_obj = FinanceModelEntity148(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_148(self, entity_id: int, payload: FinanceSchemaEntity148Update) -> Optional[FinanceModelEntity148]:
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

    def get_entity_149_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity149]:
        return self.db.query(FinanceModelEntity149).offset(skip).limit(limit).all()

    def get_entity_149_by_id(self, entity_id: int) -> Optional[FinanceModelEntity149]:
        return self.db.query(FinanceModelEntity149).filter(FinanceModelEntity149.id == entity_id).first()

    def create_entity_149(self, payload: FinanceSchemaEntity149Create) -> FinanceModelEntity149:
        db_obj = FinanceModelEntity149(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_149(self, entity_id: int, payload: FinanceSchemaEntity149Update) -> Optional[FinanceModelEntity149]:
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

    def get_entity_150_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity150]:
        return self.db.query(FinanceModelEntity150).offset(skip).limit(limit).all()

    def get_entity_150_by_id(self, entity_id: int) -> Optional[FinanceModelEntity150]:
        return self.db.query(FinanceModelEntity150).filter(FinanceModelEntity150.id == entity_id).first()

    def create_entity_150(self, payload: FinanceSchemaEntity150Create) -> FinanceModelEntity150:
        db_obj = FinanceModelEntity150(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_150(self, entity_id: int, payload: FinanceSchemaEntity150Update) -> Optional[FinanceModelEntity150]:
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

    def get_entity_151_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity151]:
        return self.db.query(FinanceModelEntity151).offset(skip).limit(limit).all()

    def get_entity_151_by_id(self, entity_id: int) -> Optional[FinanceModelEntity151]:
        return self.db.query(FinanceModelEntity151).filter(FinanceModelEntity151.id == entity_id).first()

    def create_entity_151(self, payload: FinanceSchemaEntity151Create) -> FinanceModelEntity151:
        db_obj = FinanceModelEntity151(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_151(self, entity_id: int, payload: FinanceSchemaEntity151Update) -> Optional[FinanceModelEntity151]:
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

    def get_entity_152_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity152]:
        return self.db.query(FinanceModelEntity152).offset(skip).limit(limit).all()

    def get_entity_152_by_id(self, entity_id: int) -> Optional[FinanceModelEntity152]:
        return self.db.query(FinanceModelEntity152).filter(FinanceModelEntity152.id == entity_id).first()

    def create_entity_152(self, payload: FinanceSchemaEntity152Create) -> FinanceModelEntity152:
        db_obj = FinanceModelEntity152(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_152(self, entity_id: int, payload: FinanceSchemaEntity152Update) -> Optional[FinanceModelEntity152]:
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

    def get_entity_153_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity153]:
        return self.db.query(FinanceModelEntity153).offset(skip).limit(limit).all()

    def get_entity_153_by_id(self, entity_id: int) -> Optional[FinanceModelEntity153]:
        return self.db.query(FinanceModelEntity153).filter(FinanceModelEntity153.id == entity_id).first()

    def create_entity_153(self, payload: FinanceSchemaEntity153Create) -> FinanceModelEntity153:
        db_obj = FinanceModelEntity153(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_153(self, entity_id: int, payload: FinanceSchemaEntity153Update) -> Optional[FinanceModelEntity153]:
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

    def get_entity_154_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity154]:
        return self.db.query(FinanceModelEntity154).offset(skip).limit(limit).all()

    def get_entity_154_by_id(self, entity_id: int) -> Optional[FinanceModelEntity154]:
        return self.db.query(FinanceModelEntity154).filter(FinanceModelEntity154.id == entity_id).first()

    def create_entity_154(self, payload: FinanceSchemaEntity154Create) -> FinanceModelEntity154:
        db_obj = FinanceModelEntity154(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_154(self, entity_id: int, payload: FinanceSchemaEntity154Update) -> Optional[FinanceModelEntity154]:
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

    def get_entity_155_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity155]:
        return self.db.query(FinanceModelEntity155).offset(skip).limit(limit).all()

    def get_entity_155_by_id(self, entity_id: int) -> Optional[FinanceModelEntity155]:
        return self.db.query(FinanceModelEntity155).filter(FinanceModelEntity155.id == entity_id).first()

    def create_entity_155(self, payload: FinanceSchemaEntity155Create) -> FinanceModelEntity155:
        db_obj = FinanceModelEntity155(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_155(self, entity_id: int, payload: FinanceSchemaEntity155Update) -> Optional[FinanceModelEntity155]:
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

    def get_entity_156_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity156]:
        return self.db.query(FinanceModelEntity156).offset(skip).limit(limit).all()

    def get_entity_156_by_id(self, entity_id: int) -> Optional[FinanceModelEntity156]:
        return self.db.query(FinanceModelEntity156).filter(FinanceModelEntity156.id == entity_id).first()

    def create_entity_156(self, payload: FinanceSchemaEntity156Create) -> FinanceModelEntity156:
        db_obj = FinanceModelEntity156(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_156(self, entity_id: int, payload: FinanceSchemaEntity156Update) -> Optional[FinanceModelEntity156]:
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

    def get_entity_157_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity157]:
        return self.db.query(FinanceModelEntity157).offset(skip).limit(limit).all()

    def get_entity_157_by_id(self, entity_id: int) -> Optional[FinanceModelEntity157]:
        return self.db.query(FinanceModelEntity157).filter(FinanceModelEntity157.id == entity_id).first()

    def create_entity_157(self, payload: FinanceSchemaEntity157Create) -> FinanceModelEntity157:
        db_obj = FinanceModelEntity157(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_157(self, entity_id: int, payload: FinanceSchemaEntity157Update) -> Optional[FinanceModelEntity157]:
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

    def get_entity_158_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity158]:
        return self.db.query(FinanceModelEntity158).offset(skip).limit(limit).all()

    def get_entity_158_by_id(self, entity_id: int) -> Optional[FinanceModelEntity158]:
        return self.db.query(FinanceModelEntity158).filter(FinanceModelEntity158.id == entity_id).first()

    def create_entity_158(self, payload: FinanceSchemaEntity158Create) -> FinanceModelEntity158:
        db_obj = FinanceModelEntity158(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_158(self, entity_id: int, payload: FinanceSchemaEntity158Update) -> Optional[FinanceModelEntity158]:
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

    def get_entity_159_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity159]:
        return self.db.query(FinanceModelEntity159).offset(skip).limit(limit).all()

    def get_entity_159_by_id(self, entity_id: int) -> Optional[FinanceModelEntity159]:
        return self.db.query(FinanceModelEntity159).filter(FinanceModelEntity159.id == entity_id).first()

    def create_entity_159(self, payload: FinanceSchemaEntity159Create) -> FinanceModelEntity159:
        db_obj = FinanceModelEntity159(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_159(self, entity_id: int, payload: FinanceSchemaEntity159Update) -> Optional[FinanceModelEntity159]:
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

    def get_entity_160_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity160]:
        return self.db.query(FinanceModelEntity160).offset(skip).limit(limit).all()

    def get_entity_160_by_id(self, entity_id: int) -> Optional[FinanceModelEntity160]:
        return self.db.query(FinanceModelEntity160).filter(FinanceModelEntity160.id == entity_id).first()

    def create_entity_160(self, payload: FinanceSchemaEntity160Create) -> FinanceModelEntity160:
        db_obj = FinanceModelEntity160(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_160(self, entity_id: int, payload: FinanceSchemaEntity160Update) -> Optional[FinanceModelEntity160]:
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

    def get_entity_161_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity161]:
        return self.db.query(FinanceModelEntity161).offset(skip).limit(limit).all()

    def get_entity_161_by_id(self, entity_id: int) -> Optional[FinanceModelEntity161]:
        return self.db.query(FinanceModelEntity161).filter(FinanceModelEntity161.id == entity_id).first()

    def create_entity_161(self, payload: FinanceSchemaEntity161Create) -> FinanceModelEntity161:
        db_obj = FinanceModelEntity161(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_161(self, entity_id: int, payload: FinanceSchemaEntity161Update) -> Optional[FinanceModelEntity161]:
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

    def get_entity_162_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity162]:
        return self.db.query(FinanceModelEntity162).offset(skip).limit(limit).all()

    def get_entity_162_by_id(self, entity_id: int) -> Optional[FinanceModelEntity162]:
        return self.db.query(FinanceModelEntity162).filter(FinanceModelEntity162.id == entity_id).first()

    def create_entity_162(self, payload: FinanceSchemaEntity162Create) -> FinanceModelEntity162:
        db_obj = FinanceModelEntity162(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_162(self, entity_id: int, payload: FinanceSchemaEntity162Update) -> Optional[FinanceModelEntity162]:
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

    def get_entity_163_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity163]:
        return self.db.query(FinanceModelEntity163).offset(skip).limit(limit).all()

    def get_entity_163_by_id(self, entity_id: int) -> Optional[FinanceModelEntity163]:
        return self.db.query(FinanceModelEntity163).filter(FinanceModelEntity163.id == entity_id).first()

    def create_entity_163(self, payload: FinanceSchemaEntity163Create) -> FinanceModelEntity163:
        db_obj = FinanceModelEntity163(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_163(self, entity_id: int, payload: FinanceSchemaEntity163Update) -> Optional[FinanceModelEntity163]:
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

    def get_entity_164_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity164]:
        return self.db.query(FinanceModelEntity164).offset(skip).limit(limit).all()

    def get_entity_164_by_id(self, entity_id: int) -> Optional[FinanceModelEntity164]:
        return self.db.query(FinanceModelEntity164).filter(FinanceModelEntity164.id == entity_id).first()

    def create_entity_164(self, payload: FinanceSchemaEntity164Create) -> FinanceModelEntity164:
        db_obj = FinanceModelEntity164(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_164(self, entity_id: int, payload: FinanceSchemaEntity164Update) -> Optional[FinanceModelEntity164]:
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

    def get_entity_165_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity165]:
        return self.db.query(FinanceModelEntity165).offset(skip).limit(limit).all()

    def get_entity_165_by_id(self, entity_id: int) -> Optional[FinanceModelEntity165]:
        return self.db.query(FinanceModelEntity165).filter(FinanceModelEntity165.id == entity_id).first()

    def create_entity_165(self, payload: FinanceSchemaEntity165Create) -> FinanceModelEntity165:
        db_obj = FinanceModelEntity165(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_165(self, entity_id: int, payload: FinanceSchemaEntity165Update) -> Optional[FinanceModelEntity165]:
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

    def get_entity_166_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity166]:
        return self.db.query(FinanceModelEntity166).offset(skip).limit(limit).all()

    def get_entity_166_by_id(self, entity_id: int) -> Optional[FinanceModelEntity166]:
        return self.db.query(FinanceModelEntity166).filter(FinanceModelEntity166.id == entity_id).first()

    def create_entity_166(self, payload: FinanceSchemaEntity166Create) -> FinanceModelEntity166:
        db_obj = FinanceModelEntity166(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_166(self, entity_id: int, payload: FinanceSchemaEntity166Update) -> Optional[FinanceModelEntity166]:
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

    def get_entity_167_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity167]:
        return self.db.query(FinanceModelEntity167).offset(skip).limit(limit).all()

    def get_entity_167_by_id(self, entity_id: int) -> Optional[FinanceModelEntity167]:
        return self.db.query(FinanceModelEntity167).filter(FinanceModelEntity167.id == entity_id).first()

    def create_entity_167(self, payload: FinanceSchemaEntity167Create) -> FinanceModelEntity167:
        db_obj = FinanceModelEntity167(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_167(self, entity_id: int, payload: FinanceSchemaEntity167Update) -> Optional[FinanceModelEntity167]:
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

    def get_entity_168_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity168]:
        return self.db.query(FinanceModelEntity168).offset(skip).limit(limit).all()

    def get_entity_168_by_id(self, entity_id: int) -> Optional[FinanceModelEntity168]:
        return self.db.query(FinanceModelEntity168).filter(FinanceModelEntity168.id == entity_id).first()

    def create_entity_168(self, payload: FinanceSchemaEntity168Create) -> FinanceModelEntity168:
        db_obj = FinanceModelEntity168(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_168(self, entity_id: int, payload: FinanceSchemaEntity168Update) -> Optional[FinanceModelEntity168]:
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

    def get_entity_169_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity169]:
        return self.db.query(FinanceModelEntity169).offset(skip).limit(limit).all()

    def get_entity_169_by_id(self, entity_id: int) -> Optional[FinanceModelEntity169]:
        return self.db.query(FinanceModelEntity169).filter(FinanceModelEntity169.id == entity_id).first()

    def create_entity_169(self, payload: FinanceSchemaEntity169Create) -> FinanceModelEntity169:
        db_obj = FinanceModelEntity169(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_169(self, entity_id: int, payload: FinanceSchemaEntity169Update) -> Optional[FinanceModelEntity169]:
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

    def get_entity_170_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity170]:
        return self.db.query(FinanceModelEntity170).offset(skip).limit(limit).all()

    def get_entity_170_by_id(self, entity_id: int) -> Optional[FinanceModelEntity170]:
        return self.db.query(FinanceModelEntity170).filter(FinanceModelEntity170.id == entity_id).first()

    def create_entity_170(self, payload: FinanceSchemaEntity170Create) -> FinanceModelEntity170:
        db_obj = FinanceModelEntity170(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_170(self, entity_id: int, payload: FinanceSchemaEntity170Update) -> Optional[FinanceModelEntity170]:
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

    def get_entity_171_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity171]:
        return self.db.query(FinanceModelEntity171).offset(skip).limit(limit).all()

    def get_entity_171_by_id(self, entity_id: int) -> Optional[FinanceModelEntity171]:
        return self.db.query(FinanceModelEntity171).filter(FinanceModelEntity171.id == entity_id).first()

    def create_entity_171(self, payload: FinanceSchemaEntity171Create) -> FinanceModelEntity171:
        db_obj = FinanceModelEntity171(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_171(self, entity_id: int, payload: FinanceSchemaEntity171Update) -> Optional[FinanceModelEntity171]:
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

    def get_entity_172_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity172]:
        return self.db.query(FinanceModelEntity172).offset(skip).limit(limit).all()

    def get_entity_172_by_id(self, entity_id: int) -> Optional[FinanceModelEntity172]:
        return self.db.query(FinanceModelEntity172).filter(FinanceModelEntity172.id == entity_id).first()

    def create_entity_172(self, payload: FinanceSchemaEntity172Create) -> FinanceModelEntity172:
        db_obj = FinanceModelEntity172(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_172(self, entity_id: int, payload: FinanceSchemaEntity172Update) -> Optional[FinanceModelEntity172]:
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

    def get_entity_173_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity173]:
        return self.db.query(FinanceModelEntity173).offset(skip).limit(limit).all()

    def get_entity_173_by_id(self, entity_id: int) -> Optional[FinanceModelEntity173]:
        return self.db.query(FinanceModelEntity173).filter(FinanceModelEntity173.id == entity_id).first()

    def create_entity_173(self, payload: FinanceSchemaEntity173Create) -> FinanceModelEntity173:
        db_obj = FinanceModelEntity173(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_173(self, entity_id: int, payload: FinanceSchemaEntity173Update) -> Optional[FinanceModelEntity173]:
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

    def get_entity_174_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity174]:
        return self.db.query(FinanceModelEntity174).offset(skip).limit(limit).all()

    def get_entity_174_by_id(self, entity_id: int) -> Optional[FinanceModelEntity174]:
        return self.db.query(FinanceModelEntity174).filter(FinanceModelEntity174.id == entity_id).first()

    def create_entity_174(self, payload: FinanceSchemaEntity174Create) -> FinanceModelEntity174:
        db_obj = FinanceModelEntity174(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_174(self, entity_id: int, payload: FinanceSchemaEntity174Update) -> Optional[FinanceModelEntity174]:
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

    def get_entity_175_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity175]:
        return self.db.query(FinanceModelEntity175).offset(skip).limit(limit).all()

    def get_entity_175_by_id(self, entity_id: int) -> Optional[FinanceModelEntity175]:
        return self.db.query(FinanceModelEntity175).filter(FinanceModelEntity175.id == entity_id).first()

    def create_entity_175(self, payload: FinanceSchemaEntity175Create) -> FinanceModelEntity175:
        db_obj = FinanceModelEntity175(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_175(self, entity_id: int, payload: FinanceSchemaEntity175Update) -> Optional[FinanceModelEntity175]:
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

    def get_entity_176_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity176]:
        return self.db.query(FinanceModelEntity176).offset(skip).limit(limit).all()

    def get_entity_176_by_id(self, entity_id: int) -> Optional[FinanceModelEntity176]:
        return self.db.query(FinanceModelEntity176).filter(FinanceModelEntity176.id == entity_id).first()

    def create_entity_176(self, payload: FinanceSchemaEntity176Create) -> FinanceModelEntity176:
        db_obj = FinanceModelEntity176(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_176(self, entity_id: int, payload: FinanceSchemaEntity176Update) -> Optional[FinanceModelEntity176]:
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

    def get_entity_177_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity177]:
        return self.db.query(FinanceModelEntity177).offset(skip).limit(limit).all()

    def get_entity_177_by_id(self, entity_id: int) -> Optional[FinanceModelEntity177]:
        return self.db.query(FinanceModelEntity177).filter(FinanceModelEntity177.id == entity_id).first()

    def create_entity_177(self, payload: FinanceSchemaEntity177Create) -> FinanceModelEntity177:
        db_obj = FinanceModelEntity177(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_177(self, entity_id: int, payload: FinanceSchemaEntity177Update) -> Optional[FinanceModelEntity177]:
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

    def get_entity_178_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity178]:
        return self.db.query(FinanceModelEntity178).offset(skip).limit(limit).all()

    def get_entity_178_by_id(self, entity_id: int) -> Optional[FinanceModelEntity178]:
        return self.db.query(FinanceModelEntity178).filter(FinanceModelEntity178.id == entity_id).first()

    def create_entity_178(self, payload: FinanceSchemaEntity178Create) -> FinanceModelEntity178:
        db_obj = FinanceModelEntity178(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_178(self, entity_id: int, payload: FinanceSchemaEntity178Update) -> Optional[FinanceModelEntity178]:
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

    def get_entity_179_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity179]:
        return self.db.query(FinanceModelEntity179).offset(skip).limit(limit).all()

    def get_entity_179_by_id(self, entity_id: int) -> Optional[FinanceModelEntity179]:
        return self.db.query(FinanceModelEntity179).filter(FinanceModelEntity179.id == entity_id).first()

    def create_entity_179(self, payload: FinanceSchemaEntity179Create) -> FinanceModelEntity179:
        db_obj = FinanceModelEntity179(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_179(self, entity_id: int, payload: FinanceSchemaEntity179Update) -> Optional[FinanceModelEntity179]:
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

    def get_entity_180_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity180]:
        return self.db.query(FinanceModelEntity180).offset(skip).limit(limit).all()

    def get_entity_180_by_id(self, entity_id: int) -> Optional[FinanceModelEntity180]:
        return self.db.query(FinanceModelEntity180).filter(FinanceModelEntity180.id == entity_id).first()

    def create_entity_180(self, payload: FinanceSchemaEntity180Create) -> FinanceModelEntity180:
        db_obj = FinanceModelEntity180(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_180(self, entity_id: int, payload: FinanceSchemaEntity180Update) -> Optional[FinanceModelEntity180]:
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

    def get_entity_181_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity181]:
        return self.db.query(FinanceModelEntity181).offset(skip).limit(limit).all()

    def get_entity_181_by_id(self, entity_id: int) -> Optional[FinanceModelEntity181]:
        return self.db.query(FinanceModelEntity181).filter(FinanceModelEntity181.id == entity_id).first()

    def create_entity_181(self, payload: FinanceSchemaEntity181Create) -> FinanceModelEntity181:
        db_obj = FinanceModelEntity181(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_181(self, entity_id: int, payload: FinanceSchemaEntity181Update) -> Optional[FinanceModelEntity181]:
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

    def get_entity_182_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity182]:
        return self.db.query(FinanceModelEntity182).offset(skip).limit(limit).all()

    def get_entity_182_by_id(self, entity_id: int) -> Optional[FinanceModelEntity182]:
        return self.db.query(FinanceModelEntity182).filter(FinanceModelEntity182.id == entity_id).first()

    def create_entity_182(self, payload: FinanceSchemaEntity182Create) -> FinanceModelEntity182:
        db_obj = FinanceModelEntity182(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_182(self, entity_id: int, payload: FinanceSchemaEntity182Update) -> Optional[FinanceModelEntity182]:
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

    def get_entity_183_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity183]:
        return self.db.query(FinanceModelEntity183).offset(skip).limit(limit).all()

    def get_entity_183_by_id(self, entity_id: int) -> Optional[FinanceModelEntity183]:
        return self.db.query(FinanceModelEntity183).filter(FinanceModelEntity183.id == entity_id).first()

    def create_entity_183(self, payload: FinanceSchemaEntity183Create) -> FinanceModelEntity183:
        db_obj = FinanceModelEntity183(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_183(self, entity_id: int, payload: FinanceSchemaEntity183Update) -> Optional[FinanceModelEntity183]:
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

    def get_entity_184_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity184]:
        return self.db.query(FinanceModelEntity184).offset(skip).limit(limit).all()

    def get_entity_184_by_id(self, entity_id: int) -> Optional[FinanceModelEntity184]:
        return self.db.query(FinanceModelEntity184).filter(FinanceModelEntity184.id == entity_id).first()

    def create_entity_184(self, payload: FinanceSchemaEntity184Create) -> FinanceModelEntity184:
        db_obj = FinanceModelEntity184(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_184(self, entity_id: int, payload: FinanceSchemaEntity184Update) -> Optional[FinanceModelEntity184]:
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

    def get_entity_185_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity185]:
        return self.db.query(FinanceModelEntity185).offset(skip).limit(limit).all()

    def get_entity_185_by_id(self, entity_id: int) -> Optional[FinanceModelEntity185]:
        return self.db.query(FinanceModelEntity185).filter(FinanceModelEntity185.id == entity_id).first()

    def create_entity_185(self, payload: FinanceSchemaEntity185Create) -> FinanceModelEntity185:
        db_obj = FinanceModelEntity185(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_185(self, entity_id: int, payload: FinanceSchemaEntity185Update) -> Optional[FinanceModelEntity185]:
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

    def get_entity_186_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity186]:
        return self.db.query(FinanceModelEntity186).offset(skip).limit(limit).all()

    def get_entity_186_by_id(self, entity_id: int) -> Optional[FinanceModelEntity186]:
        return self.db.query(FinanceModelEntity186).filter(FinanceModelEntity186.id == entity_id).first()

    def create_entity_186(self, payload: FinanceSchemaEntity186Create) -> FinanceModelEntity186:
        db_obj = FinanceModelEntity186(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_186(self, entity_id: int, payload: FinanceSchemaEntity186Update) -> Optional[FinanceModelEntity186]:
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

    def get_entity_187_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity187]:
        return self.db.query(FinanceModelEntity187).offset(skip).limit(limit).all()

    def get_entity_187_by_id(self, entity_id: int) -> Optional[FinanceModelEntity187]:
        return self.db.query(FinanceModelEntity187).filter(FinanceModelEntity187.id == entity_id).first()

    def create_entity_187(self, payload: FinanceSchemaEntity187Create) -> FinanceModelEntity187:
        db_obj = FinanceModelEntity187(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_187(self, entity_id: int, payload: FinanceSchemaEntity187Update) -> Optional[FinanceModelEntity187]:
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

    def get_entity_188_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity188]:
        return self.db.query(FinanceModelEntity188).offset(skip).limit(limit).all()

    def get_entity_188_by_id(self, entity_id: int) -> Optional[FinanceModelEntity188]:
        return self.db.query(FinanceModelEntity188).filter(FinanceModelEntity188.id == entity_id).first()

    def create_entity_188(self, payload: FinanceSchemaEntity188Create) -> FinanceModelEntity188:
        db_obj = FinanceModelEntity188(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_188(self, entity_id: int, payload: FinanceSchemaEntity188Update) -> Optional[FinanceModelEntity188]:
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

    def get_entity_189_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity189]:
        return self.db.query(FinanceModelEntity189).offset(skip).limit(limit).all()

    def get_entity_189_by_id(self, entity_id: int) -> Optional[FinanceModelEntity189]:
        return self.db.query(FinanceModelEntity189).filter(FinanceModelEntity189.id == entity_id).first()

    def create_entity_189(self, payload: FinanceSchemaEntity189Create) -> FinanceModelEntity189:
        db_obj = FinanceModelEntity189(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_189(self, entity_id: int, payload: FinanceSchemaEntity189Update) -> Optional[FinanceModelEntity189]:
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

    def get_entity_190_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity190]:
        return self.db.query(FinanceModelEntity190).offset(skip).limit(limit).all()

    def get_entity_190_by_id(self, entity_id: int) -> Optional[FinanceModelEntity190]:
        return self.db.query(FinanceModelEntity190).filter(FinanceModelEntity190.id == entity_id).first()

    def create_entity_190(self, payload: FinanceSchemaEntity190Create) -> FinanceModelEntity190:
        db_obj = FinanceModelEntity190(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_190(self, entity_id: int, payload: FinanceSchemaEntity190Update) -> Optional[FinanceModelEntity190]:
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

    def get_entity_191_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity191]:
        return self.db.query(FinanceModelEntity191).offset(skip).limit(limit).all()

    def get_entity_191_by_id(self, entity_id: int) -> Optional[FinanceModelEntity191]:
        return self.db.query(FinanceModelEntity191).filter(FinanceModelEntity191.id == entity_id).first()

    def create_entity_191(self, payload: FinanceSchemaEntity191Create) -> FinanceModelEntity191:
        db_obj = FinanceModelEntity191(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_191(self, entity_id: int, payload: FinanceSchemaEntity191Update) -> Optional[FinanceModelEntity191]:
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

    def get_entity_192_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity192]:
        return self.db.query(FinanceModelEntity192).offset(skip).limit(limit).all()

    def get_entity_192_by_id(self, entity_id: int) -> Optional[FinanceModelEntity192]:
        return self.db.query(FinanceModelEntity192).filter(FinanceModelEntity192.id == entity_id).first()

    def create_entity_192(self, payload: FinanceSchemaEntity192Create) -> FinanceModelEntity192:
        db_obj = FinanceModelEntity192(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_192(self, entity_id: int, payload: FinanceSchemaEntity192Update) -> Optional[FinanceModelEntity192]:
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

    def get_entity_193_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity193]:
        return self.db.query(FinanceModelEntity193).offset(skip).limit(limit).all()

    def get_entity_193_by_id(self, entity_id: int) -> Optional[FinanceModelEntity193]:
        return self.db.query(FinanceModelEntity193).filter(FinanceModelEntity193.id == entity_id).first()

    def create_entity_193(self, payload: FinanceSchemaEntity193Create) -> FinanceModelEntity193:
        db_obj = FinanceModelEntity193(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_193(self, entity_id: int, payload: FinanceSchemaEntity193Update) -> Optional[FinanceModelEntity193]:
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

    def get_entity_194_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity194]:
        return self.db.query(FinanceModelEntity194).offset(skip).limit(limit).all()

    def get_entity_194_by_id(self, entity_id: int) -> Optional[FinanceModelEntity194]:
        return self.db.query(FinanceModelEntity194).filter(FinanceModelEntity194.id == entity_id).first()

    def create_entity_194(self, payload: FinanceSchemaEntity194Create) -> FinanceModelEntity194:
        db_obj = FinanceModelEntity194(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_194(self, entity_id: int, payload: FinanceSchemaEntity194Update) -> Optional[FinanceModelEntity194]:
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

    def get_entity_195_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity195]:
        return self.db.query(FinanceModelEntity195).offset(skip).limit(limit).all()

    def get_entity_195_by_id(self, entity_id: int) -> Optional[FinanceModelEntity195]:
        return self.db.query(FinanceModelEntity195).filter(FinanceModelEntity195.id == entity_id).first()

    def create_entity_195(self, payload: FinanceSchemaEntity195Create) -> FinanceModelEntity195:
        db_obj = FinanceModelEntity195(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_195(self, entity_id: int, payload: FinanceSchemaEntity195Update) -> Optional[FinanceModelEntity195]:
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

    def get_entity_196_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity196]:
        return self.db.query(FinanceModelEntity196).offset(skip).limit(limit).all()

    def get_entity_196_by_id(self, entity_id: int) -> Optional[FinanceModelEntity196]:
        return self.db.query(FinanceModelEntity196).filter(FinanceModelEntity196.id == entity_id).first()

    def create_entity_196(self, payload: FinanceSchemaEntity196Create) -> FinanceModelEntity196:
        db_obj = FinanceModelEntity196(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_196(self, entity_id: int, payload: FinanceSchemaEntity196Update) -> Optional[FinanceModelEntity196]:
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

    def get_entity_197_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity197]:
        return self.db.query(FinanceModelEntity197).offset(skip).limit(limit).all()

    def get_entity_197_by_id(self, entity_id: int) -> Optional[FinanceModelEntity197]:
        return self.db.query(FinanceModelEntity197).filter(FinanceModelEntity197.id == entity_id).first()

    def create_entity_197(self, payload: FinanceSchemaEntity197Create) -> FinanceModelEntity197:
        db_obj = FinanceModelEntity197(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_197(self, entity_id: int, payload: FinanceSchemaEntity197Update) -> Optional[FinanceModelEntity197]:
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

    def get_entity_198_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity198]:
        return self.db.query(FinanceModelEntity198).offset(skip).limit(limit).all()

    def get_entity_198_by_id(self, entity_id: int) -> Optional[FinanceModelEntity198]:
        return self.db.query(FinanceModelEntity198).filter(FinanceModelEntity198.id == entity_id).first()

    def create_entity_198(self, payload: FinanceSchemaEntity198Create) -> FinanceModelEntity198:
        db_obj = FinanceModelEntity198(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_198(self, entity_id: int, payload: FinanceSchemaEntity198Update) -> Optional[FinanceModelEntity198]:
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

    def get_entity_199_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity199]:
        return self.db.query(FinanceModelEntity199).offset(skip).limit(limit).all()

    def get_entity_199_by_id(self, entity_id: int) -> Optional[FinanceModelEntity199]:
        return self.db.query(FinanceModelEntity199).filter(FinanceModelEntity199.id == entity_id).first()

    def create_entity_199(self, payload: FinanceSchemaEntity199Create) -> FinanceModelEntity199:
        db_obj = FinanceModelEntity199(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_199(self, entity_id: int, payload: FinanceSchemaEntity199Update) -> Optional[FinanceModelEntity199]:
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

    def get_entity_200_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity200]:
        return self.db.query(FinanceModelEntity200).offset(skip).limit(limit).all()

    def get_entity_200_by_id(self, entity_id: int) -> Optional[FinanceModelEntity200]:
        return self.db.query(FinanceModelEntity200).filter(FinanceModelEntity200.id == entity_id).first()

    def create_entity_200(self, payload: FinanceSchemaEntity200Create) -> FinanceModelEntity200:
        db_obj = FinanceModelEntity200(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_200(self, entity_id: int, payload: FinanceSchemaEntity200Update) -> Optional[FinanceModelEntity200]:
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

    def get_entity_201_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity201]:
        return self.db.query(FinanceModelEntity201).offset(skip).limit(limit).all()

    def get_entity_201_by_id(self, entity_id: int) -> Optional[FinanceModelEntity201]:
        return self.db.query(FinanceModelEntity201).filter(FinanceModelEntity201.id == entity_id).first()

    def create_entity_201(self, payload: FinanceSchemaEntity201Create) -> FinanceModelEntity201:
        db_obj = FinanceModelEntity201(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_201(self, entity_id: int, payload: FinanceSchemaEntity201Update) -> Optional[FinanceModelEntity201]:
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

    def get_entity_202_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity202]:
        return self.db.query(FinanceModelEntity202).offset(skip).limit(limit).all()

    def get_entity_202_by_id(self, entity_id: int) -> Optional[FinanceModelEntity202]:
        return self.db.query(FinanceModelEntity202).filter(FinanceModelEntity202.id == entity_id).first()

    def create_entity_202(self, payload: FinanceSchemaEntity202Create) -> FinanceModelEntity202:
        db_obj = FinanceModelEntity202(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_202(self, entity_id: int, payload: FinanceSchemaEntity202Update) -> Optional[FinanceModelEntity202]:
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

    def get_entity_203_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity203]:
        return self.db.query(FinanceModelEntity203).offset(skip).limit(limit).all()

    def get_entity_203_by_id(self, entity_id: int) -> Optional[FinanceModelEntity203]:
        return self.db.query(FinanceModelEntity203).filter(FinanceModelEntity203.id == entity_id).first()

    def create_entity_203(self, payload: FinanceSchemaEntity203Create) -> FinanceModelEntity203:
        db_obj = FinanceModelEntity203(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_203(self, entity_id: int, payload: FinanceSchemaEntity203Update) -> Optional[FinanceModelEntity203]:
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

    def get_entity_204_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity204]:
        return self.db.query(FinanceModelEntity204).offset(skip).limit(limit).all()

    def get_entity_204_by_id(self, entity_id: int) -> Optional[FinanceModelEntity204]:
        return self.db.query(FinanceModelEntity204).filter(FinanceModelEntity204.id == entity_id).first()

    def create_entity_204(self, payload: FinanceSchemaEntity204Create) -> FinanceModelEntity204:
        db_obj = FinanceModelEntity204(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_204(self, entity_id: int, payload: FinanceSchemaEntity204Update) -> Optional[FinanceModelEntity204]:
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

    def get_entity_205_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity205]:
        return self.db.query(FinanceModelEntity205).offset(skip).limit(limit).all()

    def get_entity_205_by_id(self, entity_id: int) -> Optional[FinanceModelEntity205]:
        return self.db.query(FinanceModelEntity205).filter(FinanceModelEntity205.id == entity_id).first()

    def create_entity_205(self, payload: FinanceSchemaEntity205Create) -> FinanceModelEntity205:
        db_obj = FinanceModelEntity205(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_205(self, entity_id: int, payload: FinanceSchemaEntity205Update) -> Optional[FinanceModelEntity205]:
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

    def get_entity_206_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity206]:
        return self.db.query(FinanceModelEntity206).offset(skip).limit(limit).all()

    def get_entity_206_by_id(self, entity_id: int) -> Optional[FinanceModelEntity206]:
        return self.db.query(FinanceModelEntity206).filter(FinanceModelEntity206.id == entity_id).first()

    def create_entity_206(self, payload: FinanceSchemaEntity206Create) -> FinanceModelEntity206:
        db_obj = FinanceModelEntity206(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_206(self, entity_id: int, payload: FinanceSchemaEntity206Update) -> Optional[FinanceModelEntity206]:
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

    def get_entity_207_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity207]:
        return self.db.query(FinanceModelEntity207).offset(skip).limit(limit).all()

    def get_entity_207_by_id(self, entity_id: int) -> Optional[FinanceModelEntity207]:
        return self.db.query(FinanceModelEntity207).filter(FinanceModelEntity207.id == entity_id).first()

    def create_entity_207(self, payload: FinanceSchemaEntity207Create) -> FinanceModelEntity207:
        db_obj = FinanceModelEntity207(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_207(self, entity_id: int, payload: FinanceSchemaEntity207Update) -> Optional[FinanceModelEntity207]:
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

    def get_entity_208_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity208]:
        return self.db.query(FinanceModelEntity208).offset(skip).limit(limit).all()

    def get_entity_208_by_id(self, entity_id: int) -> Optional[FinanceModelEntity208]:
        return self.db.query(FinanceModelEntity208).filter(FinanceModelEntity208.id == entity_id).first()

    def create_entity_208(self, payload: FinanceSchemaEntity208Create) -> FinanceModelEntity208:
        db_obj = FinanceModelEntity208(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_208(self, entity_id: int, payload: FinanceSchemaEntity208Update) -> Optional[FinanceModelEntity208]:
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

    def get_entity_209_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity209]:
        return self.db.query(FinanceModelEntity209).offset(skip).limit(limit).all()

    def get_entity_209_by_id(self, entity_id: int) -> Optional[FinanceModelEntity209]:
        return self.db.query(FinanceModelEntity209).filter(FinanceModelEntity209.id == entity_id).first()

    def create_entity_209(self, payload: FinanceSchemaEntity209Create) -> FinanceModelEntity209:
        db_obj = FinanceModelEntity209(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_209(self, entity_id: int, payload: FinanceSchemaEntity209Update) -> Optional[FinanceModelEntity209]:
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

    def get_entity_210_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity210]:
        return self.db.query(FinanceModelEntity210).offset(skip).limit(limit).all()

    def get_entity_210_by_id(self, entity_id: int) -> Optional[FinanceModelEntity210]:
        return self.db.query(FinanceModelEntity210).filter(FinanceModelEntity210.id == entity_id).first()

    def create_entity_210(self, payload: FinanceSchemaEntity210Create) -> FinanceModelEntity210:
        db_obj = FinanceModelEntity210(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_210(self, entity_id: int, payload: FinanceSchemaEntity210Update) -> Optional[FinanceModelEntity210]:
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

    def get_entity_211_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity211]:
        return self.db.query(FinanceModelEntity211).offset(skip).limit(limit).all()

    def get_entity_211_by_id(self, entity_id: int) -> Optional[FinanceModelEntity211]:
        return self.db.query(FinanceModelEntity211).filter(FinanceModelEntity211.id == entity_id).first()

    def create_entity_211(self, payload: FinanceSchemaEntity211Create) -> FinanceModelEntity211:
        db_obj = FinanceModelEntity211(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_211(self, entity_id: int, payload: FinanceSchemaEntity211Update) -> Optional[FinanceModelEntity211]:
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

    def get_entity_212_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity212]:
        return self.db.query(FinanceModelEntity212).offset(skip).limit(limit).all()

    def get_entity_212_by_id(self, entity_id: int) -> Optional[FinanceModelEntity212]:
        return self.db.query(FinanceModelEntity212).filter(FinanceModelEntity212.id == entity_id).first()

    def create_entity_212(self, payload: FinanceSchemaEntity212Create) -> FinanceModelEntity212:
        db_obj = FinanceModelEntity212(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_212(self, entity_id: int, payload: FinanceSchemaEntity212Update) -> Optional[FinanceModelEntity212]:
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

    def get_entity_213_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity213]:
        return self.db.query(FinanceModelEntity213).offset(skip).limit(limit).all()

    def get_entity_213_by_id(self, entity_id: int) -> Optional[FinanceModelEntity213]:
        return self.db.query(FinanceModelEntity213).filter(FinanceModelEntity213.id == entity_id).first()

    def create_entity_213(self, payload: FinanceSchemaEntity213Create) -> FinanceModelEntity213:
        db_obj = FinanceModelEntity213(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_213(self, entity_id: int, payload: FinanceSchemaEntity213Update) -> Optional[FinanceModelEntity213]:
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

    def get_entity_214_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity214]:
        return self.db.query(FinanceModelEntity214).offset(skip).limit(limit).all()

    def get_entity_214_by_id(self, entity_id: int) -> Optional[FinanceModelEntity214]:
        return self.db.query(FinanceModelEntity214).filter(FinanceModelEntity214.id == entity_id).first()

    def create_entity_214(self, payload: FinanceSchemaEntity214Create) -> FinanceModelEntity214:
        db_obj = FinanceModelEntity214(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_214(self, entity_id: int, payload: FinanceSchemaEntity214Update) -> Optional[FinanceModelEntity214]:
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

    def get_entity_215_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity215]:
        return self.db.query(FinanceModelEntity215).offset(skip).limit(limit).all()

    def get_entity_215_by_id(self, entity_id: int) -> Optional[FinanceModelEntity215]:
        return self.db.query(FinanceModelEntity215).filter(FinanceModelEntity215.id == entity_id).first()

    def create_entity_215(self, payload: FinanceSchemaEntity215Create) -> FinanceModelEntity215:
        db_obj = FinanceModelEntity215(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_215(self, entity_id: int, payload: FinanceSchemaEntity215Update) -> Optional[FinanceModelEntity215]:
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

    def get_entity_216_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity216]:
        return self.db.query(FinanceModelEntity216).offset(skip).limit(limit).all()

    def get_entity_216_by_id(self, entity_id: int) -> Optional[FinanceModelEntity216]:
        return self.db.query(FinanceModelEntity216).filter(FinanceModelEntity216.id == entity_id).first()

    def create_entity_216(self, payload: FinanceSchemaEntity216Create) -> FinanceModelEntity216:
        db_obj = FinanceModelEntity216(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_216(self, entity_id: int, payload: FinanceSchemaEntity216Update) -> Optional[FinanceModelEntity216]:
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

    def get_entity_217_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity217]:
        return self.db.query(FinanceModelEntity217).offset(skip).limit(limit).all()

    def get_entity_217_by_id(self, entity_id: int) -> Optional[FinanceModelEntity217]:
        return self.db.query(FinanceModelEntity217).filter(FinanceModelEntity217.id == entity_id).first()

    def create_entity_217(self, payload: FinanceSchemaEntity217Create) -> FinanceModelEntity217:
        db_obj = FinanceModelEntity217(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_217(self, entity_id: int, payload: FinanceSchemaEntity217Update) -> Optional[FinanceModelEntity217]:
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

    def get_entity_218_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity218]:
        return self.db.query(FinanceModelEntity218).offset(skip).limit(limit).all()

    def get_entity_218_by_id(self, entity_id: int) -> Optional[FinanceModelEntity218]:
        return self.db.query(FinanceModelEntity218).filter(FinanceModelEntity218.id == entity_id).first()

    def create_entity_218(self, payload: FinanceSchemaEntity218Create) -> FinanceModelEntity218:
        db_obj = FinanceModelEntity218(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_218(self, entity_id: int, payload: FinanceSchemaEntity218Update) -> Optional[FinanceModelEntity218]:
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

    def get_entity_219_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity219]:
        return self.db.query(FinanceModelEntity219).offset(skip).limit(limit).all()

    def get_entity_219_by_id(self, entity_id: int) -> Optional[FinanceModelEntity219]:
        return self.db.query(FinanceModelEntity219).filter(FinanceModelEntity219.id == entity_id).first()

    def create_entity_219(self, payload: FinanceSchemaEntity219Create) -> FinanceModelEntity219:
        db_obj = FinanceModelEntity219(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_219(self, entity_id: int, payload: FinanceSchemaEntity219Update) -> Optional[FinanceModelEntity219]:
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

    def get_entity_220_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity220]:
        return self.db.query(FinanceModelEntity220).offset(skip).limit(limit).all()

    def get_entity_220_by_id(self, entity_id: int) -> Optional[FinanceModelEntity220]:
        return self.db.query(FinanceModelEntity220).filter(FinanceModelEntity220.id == entity_id).first()

    def create_entity_220(self, payload: FinanceSchemaEntity220Create) -> FinanceModelEntity220:
        db_obj = FinanceModelEntity220(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_220(self, entity_id: int, payload: FinanceSchemaEntity220Update) -> Optional[FinanceModelEntity220]:
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

    def get_entity_221_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity221]:
        return self.db.query(FinanceModelEntity221).offset(skip).limit(limit).all()

    def get_entity_221_by_id(self, entity_id: int) -> Optional[FinanceModelEntity221]:
        return self.db.query(FinanceModelEntity221).filter(FinanceModelEntity221.id == entity_id).first()

    def create_entity_221(self, payload: FinanceSchemaEntity221Create) -> FinanceModelEntity221:
        db_obj = FinanceModelEntity221(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_221(self, entity_id: int, payload: FinanceSchemaEntity221Update) -> Optional[FinanceModelEntity221]:
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

    def get_entity_222_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity222]:
        return self.db.query(FinanceModelEntity222).offset(skip).limit(limit).all()

    def get_entity_222_by_id(self, entity_id: int) -> Optional[FinanceModelEntity222]:
        return self.db.query(FinanceModelEntity222).filter(FinanceModelEntity222.id == entity_id).first()

    def create_entity_222(self, payload: FinanceSchemaEntity222Create) -> FinanceModelEntity222:
        db_obj = FinanceModelEntity222(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_222(self, entity_id: int, payload: FinanceSchemaEntity222Update) -> Optional[FinanceModelEntity222]:
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

    def get_entity_223_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity223]:
        return self.db.query(FinanceModelEntity223).offset(skip).limit(limit).all()

    def get_entity_223_by_id(self, entity_id: int) -> Optional[FinanceModelEntity223]:
        return self.db.query(FinanceModelEntity223).filter(FinanceModelEntity223.id == entity_id).first()

    def create_entity_223(self, payload: FinanceSchemaEntity223Create) -> FinanceModelEntity223:
        db_obj = FinanceModelEntity223(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_223(self, entity_id: int, payload: FinanceSchemaEntity223Update) -> Optional[FinanceModelEntity223]:
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

    def get_entity_224_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity224]:
        return self.db.query(FinanceModelEntity224).offset(skip).limit(limit).all()

    def get_entity_224_by_id(self, entity_id: int) -> Optional[FinanceModelEntity224]:
        return self.db.query(FinanceModelEntity224).filter(FinanceModelEntity224.id == entity_id).first()

    def create_entity_224(self, payload: FinanceSchemaEntity224Create) -> FinanceModelEntity224:
        db_obj = FinanceModelEntity224(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_224(self, entity_id: int, payload: FinanceSchemaEntity224Update) -> Optional[FinanceModelEntity224]:
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

    def get_entity_225_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity225]:
        return self.db.query(FinanceModelEntity225).offset(skip).limit(limit).all()

    def get_entity_225_by_id(self, entity_id: int) -> Optional[FinanceModelEntity225]:
        return self.db.query(FinanceModelEntity225).filter(FinanceModelEntity225.id == entity_id).first()

    def create_entity_225(self, payload: FinanceSchemaEntity225Create) -> FinanceModelEntity225:
        db_obj = FinanceModelEntity225(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_225(self, entity_id: int, payload: FinanceSchemaEntity225Update) -> Optional[FinanceModelEntity225]:
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

    def get_entity_226_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity226]:
        return self.db.query(FinanceModelEntity226).offset(skip).limit(limit).all()

    def get_entity_226_by_id(self, entity_id: int) -> Optional[FinanceModelEntity226]:
        return self.db.query(FinanceModelEntity226).filter(FinanceModelEntity226.id == entity_id).first()

    def create_entity_226(self, payload: FinanceSchemaEntity226Create) -> FinanceModelEntity226:
        db_obj = FinanceModelEntity226(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_226(self, entity_id: int, payload: FinanceSchemaEntity226Update) -> Optional[FinanceModelEntity226]:
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

    def get_entity_227_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity227]:
        return self.db.query(FinanceModelEntity227).offset(skip).limit(limit).all()

    def get_entity_227_by_id(self, entity_id: int) -> Optional[FinanceModelEntity227]:
        return self.db.query(FinanceModelEntity227).filter(FinanceModelEntity227.id == entity_id).first()

    def create_entity_227(self, payload: FinanceSchemaEntity227Create) -> FinanceModelEntity227:
        db_obj = FinanceModelEntity227(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_227(self, entity_id: int, payload: FinanceSchemaEntity227Update) -> Optional[FinanceModelEntity227]:
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

    def get_entity_228_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity228]:
        return self.db.query(FinanceModelEntity228).offset(skip).limit(limit).all()

    def get_entity_228_by_id(self, entity_id: int) -> Optional[FinanceModelEntity228]:
        return self.db.query(FinanceModelEntity228).filter(FinanceModelEntity228.id == entity_id).first()

    def create_entity_228(self, payload: FinanceSchemaEntity228Create) -> FinanceModelEntity228:
        db_obj = FinanceModelEntity228(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_228(self, entity_id: int, payload: FinanceSchemaEntity228Update) -> Optional[FinanceModelEntity228]:
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

    def get_entity_229_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity229]:
        return self.db.query(FinanceModelEntity229).offset(skip).limit(limit).all()

    def get_entity_229_by_id(self, entity_id: int) -> Optional[FinanceModelEntity229]:
        return self.db.query(FinanceModelEntity229).filter(FinanceModelEntity229.id == entity_id).first()

    def create_entity_229(self, payload: FinanceSchemaEntity229Create) -> FinanceModelEntity229:
        db_obj = FinanceModelEntity229(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_229(self, entity_id: int, payload: FinanceSchemaEntity229Update) -> Optional[FinanceModelEntity229]:
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

    def get_entity_230_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity230]:
        return self.db.query(FinanceModelEntity230).offset(skip).limit(limit).all()

    def get_entity_230_by_id(self, entity_id: int) -> Optional[FinanceModelEntity230]:
        return self.db.query(FinanceModelEntity230).filter(FinanceModelEntity230.id == entity_id).first()

    def create_entity_230(self, payload: FinanceSchemaEntity230Create) -> FinanceModelEntity230:
        db_obj = FinanceModelEntity230(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_230(self, entity_id: int, payload: FinanceSchemaEntity230Update) -> Optional[FinanceModelEntity230]:
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

    def get_entity_231_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity231]:
        return self.db.query(FinanceModelEntity231).offset(skip).limit(limit).all()

    def get_entity_231_by_id(self, entity_id: int) -> Optional[FinanceModelEntity231]:
        return self.db.query(FinanceModelEntity231).filter(FinanceModelEntity231.id == entity_id).first()

    def create_entity_231(self, payload: FinanceSchemaEntity231Create) -> FinanceModelEntity231:
        db_obj = FinanceModelEntity231(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_231(self, entity_id: int, payload: FinanceSchemaEntity231Update) -> Optional[FinanceModelEntity231]:
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

    def get_entity_232_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity232]:
        return self.db.query(FinanceModelEntity232).offset(skip).limit(limit).all()

    def get_entity_232_by_id(self, entity_id: int) -> Optional[FinanceModelEntity232]:
        return self.db.query(FinanceModelEntity232).filter(FinanceModelEntity232.id == entity_id).first()

    def create_entity_232(self, payload: FinanceSchemaEntity232Create) -> FinanceModelEntity232:
        db_obj = FinanceModelEntity232(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_232(self, entity_id: int, payload: FinanceSchemaEntity232Update) -> Optional[FinanceModelEntity232]:
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

    def get_entity_233_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity233]:
        return self.db.query(FinanceModelEntity233).offset(skip).limit(limit).all()

    def get_entity_233_by_id(self, entity_id: int) -> Optional[FinanceModelEntity233]:
        return self.db.query(FinanceModelEntity233).filter(FinanceModelEntity233.id == entity_id).first()

    def create_entity_233(self, payload: FinanceSchemaEntity233Create) -> FinanceModelEntity233:
        db_obj = FinanceModelEntity233(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_233(self, entity_id: int, payload: FinanceSchemaEntity233Update) -> Optional[FinanceModelEntity233]:
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

    def get_entity_234_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity234]:
        return self.db.query(FinanceModelEntity234).offset(skip).limit(limit).all()

    def get_entity_234_by_id(self, entity_id: int) -> Optional[FinanceModelEntity234]:
        return self.db.query(FinanceModelEntity234).filter(FinanceModelEntity234.id == entity_id).first()

    def create_entity_234(self, payload: FinanceSchemaEntity234Create) -> FinanceModelEntity234:
        db_obj = FinanceModelEntity234(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_234(self, entity_id: int, payload: FinanceSchemaEntity234Update) -> Optional[FinanceModelEntity234]:
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

    def get_entity_235_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity235]:
        return self.db.query(FinanceModelEntity235).offset(skip).limit(limit).all()

    def get_entity_235_by_id(self, entity_id: int) -> Optional[FinanceModelEntity235]:
        return self.db.query(FinanceModelEntity235).filter(FinanceModelEntity235.id == entity_id).first()

    def create_entity_235(self, payload: FinanceSchemaEntity235Create) -> FinanceModelEntity235:
        db_obj = FinanceModelEntity235(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_235(self, entity_id: int, payload: FinanceSchemaEntity235Update) -> Optional[FinanceModelEntity235]:
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

    def get_entity_236_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity236]:
        return self.db.query(FinanceModelEntity236).offset(skip).limit(limit).all()

    def get_entity_236_by_id(self, entity_id: int) -> Optional[FinanceModelEntity236]:
        return self.db.query(FinanceModelEntity236).filter(FinanceModelEntity236.id == entity_id).first()

    def create_entity_236(self, payload: FinanceSchemaEntity236Create) -> FinanceModelEntity236:
        db_obj = FinanceModelEntity236(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_236(self, entity_id: int, payload: FinanceSchemaEntity236Update) -> Optional[FinanceModelEntity236]:
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

    def get_entity_237_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity237]:
        return self.db.query(FinanceModelEntity237).offset(skip).limit(limit).all()

    def get_entity_237_by_id(self, entity_id: int) -> Optional[FinanceModelEntity237]:
        return self.db.query(FinanceModelEntity237).filter(FinanceModelEntity237.id == entity_id).first()

    def create_entity_237(self, payload: FinanceSchemaEntity237Create) -> FinanceModelEntity237:
        db_obj = FinanceModelEntity237(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_237(self, entity_id: int, payload: FinanceSchemaEntity237Update) -> Optional[FinanceModelEntity237]:
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

    def get_entity_238_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity238]:
        return self.db.query(FinanceModelEntity238).offset(skip).limit(limit).all()

    def get_entity_238_by_id(self, entity_id: int) -> Optional[FinanceModelEntity238]:
        return self.db.query(FinanceModelEntity238).filter(FinanceModelEntity238.id == entity_id).first()

    def create_entity_238(self, payload: FinanceSchemaEntity238Create) -> FinanceModelEntity238:
        db_obj = FinanceModelEntity238(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_238(self, entity_id: int, payload: FinanceSchemaEntity238Update) -> Optional[FinanceModelEntity238]:
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

    def get_entity_239_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity239]:
        return self.db.query(FinanceModelEntity239).offset(skip).limit(limit).all()

    def get_entity_239_by_id(self, entity_id: int) -> Optional[FinanceModelEntity239]:
        return self.db.query(FinanceModelEntity239).filter(FinanceModelEntity239.id == entity_id).first()

    def create_entity_239(self, payload: FinanceSchemaEntity239Create) -> FinanceModelEntity239:
        db_obj = FinanceModelEntity239(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_239(self, entity_id: int, payload: FinanceSchemaEntity239Update) -> Optional[FinanceModelEntity239]:
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

    def get_entity_240_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity240]:
        return self.db.query(FinanceModelEntity240).offset(skip).limit(limit).all()

    def get_entity_240_by_id(self, entity_id: int) -> Optional[FinanceModelEntity240]:
        return self.db.query(FinanceModelEntity240).filter(FinanceModelEntity240.id == entity_id).first()

    def create_entity_240(self, payload: FinanceSchemaEntity240Create) -> FinanceModelEntity240:
        db_obj = FinanceModelEntity240(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_240(self, entity_id: int, payload: FinanceSchemaEntity240Update) -> Optional[FinanceModelEntity240]:
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

    def get_entity_241_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity241]:
        return self.db.query(FinanceModelEntity241).offset(skip).limit(limit).all()

    def get_entity_241_by_id(self, entity_id: int) -> Optional[FinanceModelEntity241]:
        return self.db.query(FinanceModelEntity241).filter(FinanceModelEntity241.id == entity_id).first()

    def create_entity_241(self, payload: FinanceSchemaEntity241Create) -> FinanceModelEntity241:
        db_obj = FinanceModelEntity241(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_241(self, entity_id: int, payload: FinanceSchemaEntity241Update) -> Optional[FinanceModelEntity241]:
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

    def get_entity_242_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity242]:
        return self.db.query(FinanceModelEntity242).offset(skip).limit(limit).all()

    def get_entity_242_by_id(self, entity_id: int) -> Optional[FinanceModelEntity242]:
        return self.db.query(FinanceModelEntity242).filter(FinanceModelEntity242.id == entity_id).first()

    def create_entity_242(self, payload: FinanceSchemaEntity242Create) -> FinanceModelEntity242:
        db_obj = FinanceModelEntity242(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_242(self, entity_id: int, payload: FinanceSchemaEntity242Update) -> Optional[FinanceModelEntity242]:
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

    def get_entity_243_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity243]:
        return self.db.query(FinanceModelEntity243).offset(skip).limit(limit).all()

    def get_entity_243_by_id(self, entity_id: int) -> Optional[FinanceModelEntity243]:
        return self.db.query(FinanceModelEntity243).filter(FinanceModelEntity243.id == entity_id).first()

    def create_entity_243(self, payload: FinanceSchemaEntity243Create) -> FinanceModelEntity243:
        db_obj = FinanceModelEntity243(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_243(self, entity_id: int, payload: FinanceSchemaEntity243Update) -> Optional[FinanceModelEntity243]:
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

    def get_entity_244_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity244]:
        return self.db.query(FinanceModelEntity244).offset(skip).limit(limit).all()

    def get_entity_244_by_id(self, entity_id: int) -> Optional[FinanceModelEntity244]:
        return self.db.query(FinanceModelEntity244).filter(FinanceModelEntity244.id == entity_id).first()

    def create_entity_244(self, payload: FinanceSchemaEntity244Create) -> FinanceModelEntity244:
        db_obj = FinanceModelEntity244(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_244(self, entity_id: int, payload: FinanceSchemaEntity244Update) -> Optional[FinanceModelEntity244]:
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

    def get_entity_245_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity245]:
        return self.db.query(FinanceModelEntity245).offset(skip).limit(limit).all()

    def get_entity_245_by_id(self, entity_id: int) -> Optional[FinanceModelEntity245]:
        return self.db.query(FinanceModelEntity245).filter(FinanceModelEntity245.id == entity_id).first()

    def create_entity_245(self, payload: FinanceSchemaEntity245Create) -> FinanceModelEntity245:
        db_obj = FinanceModelEntity245(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_245(self, entity_id: int, payload: FinanceSchemaEntity245Update) -> Optional[FinanceModelEntity245]:
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

    def get_entity_246_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity246]:
        return self.db.query(FinanceModelEntity246).offset(skip).limit(limit).all()

    def get_entity_246_by_id(self, entity_id: int) -> Optional[FinanceModelEntity246]:
        return self.db.query(FinanceModelEntity246).filter(FinanceModelEntity246.id == entity_id).first()

    def create_entity_246(self, payload: FinanceSchemaEntity246Create) -> FinanceModelEntity246:
        db_obj = FinanceModelEntity246(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_246(self, entity_id: int, payload: FinanceSchemaEntity246Update) -> Optional[FinanceModelEntity246]:
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

    def get_entity_247_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity247]:
        return self.db.query(FinanceModelEntity247).offset(skip).limit(limit).all()

    def get_entity_247_by_id(self, entity_id: int) -> Optional[FinanceModelEntity247]:
        return self.db.query(FinanceModelEntity247).filter(FinanceModelEntity247.id == entity_id).first()

    def create_entity_247(self, payload: FinanceSchemaEntity247Create) -> FinanceModelEntity247:
        db_obj = FinanceModelEntity247(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_247(self, entity_id: int, payload: FinanceSchemaEntity247Update) -> Optional[FinanceModelEntity247]:
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

    def get_entity_248_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity248]:
        return self.db.query(FinanceModelEntity248).offset(skip).limit(limit).all()

    def get_entity_248_by_id(self, entity_id: int) -> Optional[FinanceModelEntity248]:
        return self.db.query(FinanceModelEntity248).filter(FinanceModelEntity248.id == entity_id).first()

    def create_entity_248(self, payload: FinanceSchemaEntity248Create) -> FinanceModelEntity248:
        db_obj = FinanceModelEntity248(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_248(self, entity_id: int, payload: FinanceSchemaEntity248Update) -> Optional[FinanceModelEntity248]:
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

    def get_entity_249_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity249]:
        return self.db.query(FinanceModelEntity249).offset(skip).limit(limit).all()

    def get_entity_249_by_id(self, entity_id: int) -> Optional[FinanceModelEntity249]:
        return self.db.query(FinanceModelEntity249).filter(FinanceModelEntity249.id == entity_id).first()

    def create_entity_249(self, payload: FinanceSchemaEntity249Create) -> FinanceModelEntity249:
        db_obj = FinanceModelEntity249(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_249(self, entity_id: int, payload: FinanceSchemaEntity249Update) -> Optional[FinanceModelEntity249]:
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

    def get_entity_250_list(self, skip: int = 0, limit: int = 100) -> List[FinanceModelEntity250]:
        return self.db.query(FinanceModelEntity250).offset(skip).limit(limit).all()

    def get_entity_250_by_id(self, entity_id: int) -> Optional[FinanceModelEntity250]:
        return self.db.query(FinanceModelEntity250).filter(FinanceModelEntity250.id == entity_id).first()

    def create_entity_250(self, payload: FinanceSchemaEntity250Create) -> FinanceModelEntity250:
        db_obj = FinanceModelEntity250(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_250(self, entity_id: int, payload: FinanceSchemaEntity250Update) -> Optional[FinanceModelEntity250]:
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

