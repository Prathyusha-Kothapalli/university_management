"""
Library & Digital Repositories - Service Business Logic Layer
Module: app.domains.library.service
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.domains.library.models import *
from app.domains.library.schemas import *

class LibraryDomainService:
    def __init__(self, db: Session):
        self.db = db

    def get_entity_1_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity1]:
        return self.db.query(LibraryModelEntity1).offset(skip).limit(limit).all()

    def get_entity_1_by_id(self, entity_id: int) -> Optional[LibraryModelEntity1]:
        return self.db.query(LibraryModelEntity1).filter(LibraryModelEntity1.id == entity_id).first()

    def create_entity_1(self, payload: LibrarySchemaEntity1Create) -> LibraryModelEntity1:
        db_obj = LibraryModelEntity1(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_1(self, entity_id: int, payload: LibrarySchemaEntity1Update) -> Optional[LibraryModelEntity1]:
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

    def get_entity_2_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity2]:
        return self.db.query(LibraryModelEntity2).offset(skip).limit(limit).all()

    def get_entity_2_by_id(self, entity_id: int) -> Optional[LibraryModelEntity2]:
        return self.db.query(LibraryModelEntity2).filter(LibraryModelEntity2.id == entity_id).first()

    def create_entity_2(self, payload: LibrarySchemaEntity2Create) -> LibraryModelEntity2:
        db_obj = LibraryModelEntity2(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_2(self, entity_id: int, payload: LibrarySchemaEntity2Update) -> Optional[LibraryModelEntity2]:
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

    def get_entity_3_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity3]:
        return self.db.query(LibraryModelEntity3).offset(skip).limit(limit).all()

    def get_entity_3_by_id(self, entity_id: int) -> Optional[LibraryModelEntity3]:
        return self.db.query(LibraryModelEntity3).filter(LibraryModelEntity3.id == entity_id).first()

    def create_entity_3(self, payload: LibrarySchemaEntity3Create) -> LibraryModelEntity3:
        db_obj = LibraryModelEntity3(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_3(self, entity_id: int, payload: LibrarySchemaEntity3Update) -> Optional[LibraryModelEntity3]:
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

    def get_entity_4_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity4]:
        return self.db.query(LibraryModelEntity4).offset(skip).limit(limit).all()

    def get_entity_4_by_id(self, entity_id: int) -> Optional[LibraryModelEntity4]:
        return self.db.query(LibraryModelEntity4).filter(LibraryModelEntity4.id == entity_id).first()

    def create_entity_4(self, payload: LibrarySchemaEntity4Create) -> LibraryModelEntity4:
        db_obj = LibraryModelEntity4(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_4(self, entity_id: int, payload: LibrarySchemaEntity4Update) -> Optional[LibraryModelEntity4]:
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

    def get_entity_5_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity5]:
        return self.db.query(LibraryModelEntity5).offset(skip).limit(limit).all()

    def get_entity_5_by_id(self, entity_id: int) -> Optional[LibraryModelEntity5]:
        return self.db.query(LibraryModelEntity5).filter(LibraryModelEntity5.id == entity_id).first()

    def create_entity_5(self, payload: LibrarySchemaEntity5Create) -> LibraryModelEntity5:
        db_obj = LibraryModelEntity5(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_5(self, entity_id: int, payload: LibrarySchemaEntity5Update) -> Optional[LibraryModelEntity5]:
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

    def get_entity_6_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity6]:
        return self.db.query(LibraryModelEntity6).offset(skip).limit(limit).all()

    def get_entity_6_by_id(self, entity_id: int) -> Optional[LibraryModelEntity6]:
        return self.db.query(LibraryModelEntity6).filter(LibraryModelEntity6.id == entity_id).first()

    def create_entity_6(self, payload: LibrarySchemaEntity6Create) -> LibraryModelEntity6:
        db_obj = LibraryModelEntity6(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_6(self, entity_id: int, payload: LibrarySchemaEntity6Update) -> Optional[LibraryModelEntity6]:
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

    def get_entity_7_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity7]:
        return self.db.query(LibraryModelEntity7).offset(skip).limit(limit).all()

    def get_entity_7_by_id(self, entity_id: int) -> Optional[LibraryModelEntity7]:
        return self.db.query(LibraryModelEntity7).filter(LibraryModelEntity7.id == entity_id).first()

    def create_entity_7(self, payload: LibrarySchemaEntity7Create) -> LibraryModelEntity7:
        db_obj = LibraryModelEntity7(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_7(self, entity_id: int, payload: LibrarySchemaEntity7Update) -> Optional[LibraryModelEntity7]:
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

    def get_entity_8_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity8]:
        return self.db.query(LibraryModelEntity8).offset(skip).limit(limit).all()

    def get_entity_8_by_id(self, entity_id: int) -> Optional[LibraryModelEntity8]:
        return self.db.query(LibraryModelEntity8).filter(LibraryModelEntity8.id == entity_id).first()

    def create_entity_8(self, payload: LibrarySchemaEntity8Create) -> LibraryModelEntity8:
        db_obj = LibraryModelEntity8(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_8(self, entity_id: int, payload: LibrarySchemaEntity8Update) -> Optional[LibraryModelEntity8]:
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

    def get_entity_9_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity9]:
        return self.db.query(LibraryModelEntity9).offset(skip).limit(limit).all()

    def get_entity_9_by_id(self, entity_id: int) -> Optional[LibraryModelEntity9]:
        return self.db.query(LibraryModelEntity9).filter(LibraryModelEntity9.id == entity_id).first()

    def create_entity_9(self, payload: LibrarySchemaEntity9Create) -> LibraryModelEntity9:
        db_obj = LibraryModelEntity9(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_9(self, entity_id: int, payload: LibrarySchemaEntity9Update) -> Optional[LibraryModelEntity9]:
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

    def get_entity_10_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity10]:
        return self.db.query(LibraryModelEntity10).offset(skip).limit(limit).all()

    def get_entity_10_by_id(self, entity_id: int) -> Optional[LibraryModelEntity10]:
        return self.db.query(LibraryModelEntity10).filter(LibraryModelEntity10.id == entity_id).first()

    def create_entity_10(self, payload: LibrarySchemaEntity10Create) -> LibraryModelEntity10:
        db_obj = LibraryModelEntity10(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_10(self, entity_id: int, payload: LibrarySchemaEntity10Update) -> Optional[LibraryModelEntity10]:
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

    def get_entity_11_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity11]:
        return self.db.query(LibraryModelEntity11).offset(skip).limit(limit).all()

    def get_entity_11_by_id(self, entity_id: int) -> Optional[LibraryModelEntity11]:
        return self.db.query(LibraryModelEntity11).filter(LibraryModelEntity11.id == entity_id).first()

    def create_entity_11(self, payload: LibrarySchemaEntity11Create) -> LibraryModelEntity11:
        db_obj = LibraryModelEntity11(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_11(self, entity_id: int, payload: LibrarySchemaEntity11Update) -> Optional[LibraryModelEntity11]:
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

    def get_entity_12_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity12]:
        return self.db.query(LibraryModelEntity12).offset(skip).limit(limit).all()

    def get_entity_12_by_id(self, entity_id: int) -> Optional[LibraryModelEntity12]:
        return self.db.query(LibraryModelEntity12).filter(LibraryModelEntity12.id == entity_id).first()

    def create_entity_12(self, payload: LibrarySchemaEntity12Create) -> LibraryModelEntity12:
        db_obj = LibraryModelEntity12(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_12(self, entity_id: int, payload: LibrarySchemaEntity12Update) -> Optional[LibraryModelEntity12]:
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

    def get_entity_13_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity13]:
        return self.db.query(LibraryModelEntity13).offset(skip).limit(limit).all()

    def get_entity_13_by_id(self, entity_id: int) -> Optional[LibraryModelEntity13]:
        return self.db.query(LibraryModelEntity13).filter(LibraryModelEntity13.id == entity_id).first()

    def create_entity_13(self, payload: LibrarySchemaEntity13Create) -> LibraryModelEntity13:
        db_obj = LibraryModelEntity13(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_13(self, entity_id: int, payload: LibrarySchemaEntity13Update) -> Optional[LibraryModelEntity13]:
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

    def get_entity_14_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity14]:
        return self.db.query(LibraryModelEntity14).offset(skip).limit(limit).all()

    def get_entity_14_by_id(self, entity_id: int) -> Optional[LibraryModelEntity14]:
        return self.db.query(LibraryModelEntity14).filter(LibraryModelEntity14.id == entity_id).first()

    def create_entity_14(self, payload: LibrarySchemaEntity14Create) -> LibraryModelEntity14:
        db_obj = LibraryModelEntity14(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_14(self, entity_id: int, payload: LibrarySchemaEntity14Update) -> Optional[LibraryModelEntity14]:
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

    def get_entity_15_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity15]:
        return self.db.query(LibraryModelEntity15).offset(skip).limit(limit).all()

    def get_entity_15_by_id(self, entity_id: int) -> Optional[LibraryModelEntity15]:
        return self.db.query(LibraryModelEntity15).filter(LibraryModelEntity15.id == entity_id).first()

    def create_entity_15(self, payload: LibrarySchemaEntity15Create) -> LibraryModelEntity15:
        db_obj = LibraryModelEntity15(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_15(self, entity_id: int, payload: LibrarySchemaEntity15Update) -> Optional[LibraryModelEntity15]:
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

    def get_entity_16_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity16]:
        return self.db.query(LibraryModelEntity16).offset(skip).limit(limit).all()

    def get_entity_16_by_id(self, entity_id: int) -> Optional[LibraryModelEntity16]:
        return self.db.query(LibraryModelEntity16).filter(LibraryModelEntity16.id == entity_id).first()

    def create_entity_16(self, payload: LibrarySchemaEntity16Create) -> LibraryModelEntity16:
        db_obj = LibraryModelEntity16(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_16(self, entity_id: int, payload: LibrarySchemaEntity16Update) -> Optional[LibraryModelEntity16]:
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

    def get_entity_17_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity17]:
        return self.db.query(LibraryModelEntity17).offset(skip).limit(limit).all()

    def get_entity_17_by_id(self, entity_id: int) -> Optional[LibraryModelEntity17]:
        return self.db.query(LibraryModelEntity17).filter(LibraryModelEntity17.id == entity_id).first()

    def create_entity_17(self, payload: LibrarySchemaEntity17Create) -> LibraryModelEntity17:
        db_obj = LibraryModelEntity17(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_17(self, entity_id: int, payload: LibrarySchemaEntity17Update) -> Optional[LibraryModelEntity17]:
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

    def get_entity_18_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity18]:
        return self.db.query(LibraryModelEntity18).offset(skip).limit(limit).all()

    def get_entity_18_by_id(self, entity_id: int) -> Optional[LibraryModelEntity18]:
        return self.db.query(LibraryModelEntity18).filter(LibraryModelEntity18.id == entity_id).first()

    def create_entity_18(self, payload: LibrarySchemaEntity18Create) -> LibraryModelEntity18:
        db_obj = LibraryModelEntity18(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_18(self, entity_id: int, payload: LibrarySchemaEntity18Update) -> Optional[LibraryModelEntity18]:
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

    def get_entity_19_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity19]:
        return self.db.query(LibraryModelEntity19).offset(skip).limit(limit).all()

    def get_entity_19_by_id(self, entity_id: int) -> Optional[LibraryModelEntity19]:
        return self.db.query(LibraryModelEntity19).filter(LibraryModelEntity19.id == entity_id).first()

    def create_entity_19(self, payload: LibrarySchemaEntity19Create) -> LibraryModelEntity19:
        db_obj = LibraryModelEntity19(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_19(self, entity_id: int, payload: LibrarySchemaEntity19Update) -> Optional[LibraryModelEntity19]:
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

    def get_entity_20_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity20]:
        return self.db.query(LibraryModelEntity20).offset(skip).limit(limit).all()

    def get_entity_20_by_id(self, entity_id: int) -> Optional[LibraryModelEntity20]:
        return self.db.query(LibraryModelEntity20).filter(LibraryModelEntity20.id == entity_id).first()

    def create_entity_20(self, payload: LibrarySchemaEntity20Create) -> LibraryModelEntity20:
        db_obj = LibraryModelEntity20(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_20(self, entity_id: int, payload: LibrarySchemaEntity20Update) -> Optional[LibraryModelEntity20]:
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

    def get_entity_21_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity21]:
        return self.db.query(LibraryModelEntity21).offset(skip).limit(limit).all()

    def get_entity_21_by_id(self, entity_id: int) -> Optional[LibraryModelEntity21]:
        return self.db.query(LibraryModelEntity21).filter(LibraryModelEntity21.id == entity_id).first()

    def create_entity_21(self, payload: LibrarySchemaEntity21Create) -> LibraryModelEntity21:
        db_obj = LibraryModelEntity21(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_21(self, entity_id: int, payload: LibrarySchemaEntity21Update) -> Optional[LibraryModelEntity21]:
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

    def get_entity_22_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity22]:
        return self.db.query(LibraryModelEntity22).offset(skip).limit(limit).all()

    def get_entity_22_by_id(self, entity_id: int) -> Optional[LibraryModelEntity22]:
        return self.db.query(LibraryModelEntity22).filter(LibraryModelEntity22.id == entity_id).first()

    def create_entity_22(self, payload: LibrarySchemaEntity22Create) -> LibraryModelEntity22:
        db_obj = LibraryModelEntity22(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_22(self, entity_id: int, payload: LibrarySchemaEntity22Update) -> Optional[LibraryModelEntity22]:
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

    def get_entity_23_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity23]:
        return self.db.query(LibraryModelEntity23).offset(skip).limit(limit).all()

    def get_entity_23_by_id(self, entity_id: int) -> Optional[LibraryModelEntity23]:
        return self.db.query(LibraryModelEntity23).filter(LibraryModelEntity23.id == entity_id).first()

    def create_entity_23(self, payload: LibrarySchemaEntity23Create) -> LibraryModelEntity23:
        db_obj = LibraryModelEntity23(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_23(self, entity_id: int, payload: LibrarySchemaEntity23Update) -> Optional[LibraryModelEntity23]:
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

    def get_entity_24_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity24]:
        return self.db.query(LibraryModelEntity24).offset(skip).limit(limit).all()

    def get_entity_24_by_id(self, entity_id: int) -> Optional[LibraryModelEntity24]:
        return self.db.query(LibraryModelEntity24).filter(LibraryModelEntity24.id == entity_id).first()

    def create_entity_24(self, payload: LibrarySchemaEntity24Create) -> LibraryModelEntity24:
        db_obj = LibraryModelEntity24(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_24(self, entity_id: int, payload: LibrarySchemaEntity24Update) -> Optional[LibraryModelEntity24]:
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

    def get_entity_25_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity25]:
        return self.db.query(LibraryModelEntity25).offset(skip).limit(limit).all()

    def get_entity_25_by_id(self, entity_id: int) -> Optional[LibraryModelEntity25]:
        return self.db.query(LibraryModelEntity25).filter(LibraryModelEntity25.id == entity_id).first()

    def create_entity_25(self, payload: LibrarySchemaEntity25Create) -> LibraryModelEntity25:
        db_obj = LibraryModelEntity25(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_25(self, entity_id: int, payload: LibrarySchemaEntity25Update) -> Optional[LibraryModelEntity25]:
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

    def get_entity_26_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity26]:
        return self.db.query(LibraryModelEntity26).offset(skip).limit(limit).all()

    def get_entity_26_by_id(self, entity_id: int) -> Optional[LibraryModelEntity26]:
        return self.db.query(LibraryModelEntity26).filter(LibraryModelEntity26.id == entity_id).first()

    def create_entity_26(self, payload: LibrarySchemaEntity26Create) -> LibraryModelEntity26:
        db_obj = LibraryModelEntity26(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_26(self, entity_id: int, payload: LibrarySchemaEntity26Update) -> Optional[LibraryModelEntity26]:
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

    def get_entity_27_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity27]:
        return self.db.query(LibraryModelEntity27).offset(skip).limit(limit).all()

    def get_entity_27_by_id(self, entity_id: int) -> Optional[LibraryModelEntity27]:
        return self.db.query(LibraryModelEntity27).filter(LibraryModelEntity27.id == entity_id).first()

    def create_entity_27(self, payload: LibrarySchemaEntity27Create) -> LibraryModelEntity27:
        db_obj = LibraryModelEntity27(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_27(self, entity_id: int, payload: LibrarySchemaEntity27Update) -> Optional[LibraryModelEntity27]:
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

    def get_entity_28_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity28]:
        return self.db.query(LibraryModelEntity28).offset(skip).limit(limit).all()

    def get_entity_28_by_id(self, entity_id: int) -> Optional[LibraryModelEntity28]:
        return self.db.query(LibraryModelEntity28).filter(LibraryModelEntity28.id == entity_id).first()

    def create_entity_28(self, payload: LibrarySchemaEntity28Create) -> LibraryModelEntity28:
        db_obj = LibraryModelEntity28(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_28(self, entity_id: int, payload: LibrarySchemaEntity28Update) -> Optional[LibraryModelEntity28]:
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

    def get_entity_29_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity29]:
        return self.db.query(LibraryModelEntity29).offset(skip).limit(limit).all()

    def get_entity_29_by_id(self, entity_id: int) -> Optional[LibraryModelEntity29]:
        return self.db.query(LibraryModelEntity29).filter(LibraryModelEntity29.id == entity_id).first()

    def create_entity_29(self, payload: LibrarySchemaEntity29Create) -> LibraryModelEntity29:
        db_obj = LibraryModelEntity29(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_29(self, entity_id: int, payload: LibrarySchemaEntity29Update) -> Optional[LibraryModelEntity29]:
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

    def get_entity_30_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity30]:
        return self.db.query(LibraryModelEntity30).offset(skip).limit(limit).all()

    def get_entity_30_by_id(self, entity_id: int) -> Optional[LibraryModelEntity30]:
        return self.db.query(LibraryModelEntity30).filter(LibraryModelEntity30.id == entity_id).first()

    def create_entity_30(self, payload: LibrarySchemaEntity30Create) -> LibraryModelEntity30:
        db_obj = LibraryModelEntity30(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_30(self, entity_id: int, payload: LibrarySchemaEntity30Update) -> Optional[LibraryModelEntity30]:
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

    def get_entity_31_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity31]:
        return self.db.query(LibraryModelEntity31).offset(skip).limit(limit).all()

    def get_entity_31_by_id(self, entity_id: int) -> Optional[LibraryModelEntity31]:
        return self.db.query(LibraryModelEntity31).filter(LibraryModelEntity31.id == entity_id).first()

    def create_entity_31(self, payload: LibrarySchemaEntity31Create) -> LibraryModelEntity31:
        db_obj = LibraryModelEntity31(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_31(self, entity_id: int, payload: LibrarySchemaEntity31Update) -> Optional[LibraryModelEntity31]:
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

    def get_entity_32_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity32]:
        return self.db.query(LibraryModelEntity32).offset(skip).limit(limit).all()

    def get_entity_32_by_id(self, entity_id: int) -> Optional[LibraryModelEntity32]:
        return self.db.query(LibraryModelEntity32).filter(LibraryModelEntity32.id == entity_id).first()

    def create_entity_32(self, payload: LibrarySchemaEntity32Create) -> LibraryModelEntity32:
        db_obj = LibraryModelEntity32(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_32(self, entity_id: int, payload: LibrarySchemaEntity32Update) -> Optional[LibraryModelEntity32]:
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

    def get_entity_33_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity33]:
        return self.db.query(LibraryModelEntity33).offset(skip).limit(limit).all()

    def get_entity_33_by_id(self, entity_id: int) -> Optional[LibraryModelEntity33]:
        return self.db.query(LibraryModelEntity33).filter(LibraryModelEntity33.id == entity_id).first()

    def create_entity_33(self, payload: LibrarySchemaEntity33Create) -> LibraryModelEntity33:
        db_obj = LibraryModelEntity33(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_33(self, entity_id: int, payload: LibrarySchemaEntity33Update) -> Optional[LibraryModelEntity33]:
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

    def get_entity_34_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity34]:
        return self.db.query(LibraryModelEntity34).offset(skip).limit(limit).all()

    def get_entity_34_by_id(self, entity_id: int) -> Optional[LibraryModelEntity34]:
        return self.db.query(LibraryModelEntity34).filter(LibraryModelEntity34.id == entity_id).first()

    def create_entity_34(self, payload: LibrarySchemaEntity34Create) -> LibraryModelEntity34:
        db_obj = LibraryModelEntity34(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_34(self, entity_id: int, payload: LibrarySchemaEntity34Update) -> Optional[LibraryModelEntity34]:
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

    def get_entity_35_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity35]:
        return self.db.query(LibraryModelEntity35).offset(skip).limit(limit).all()

    def get_entity_35_by_id(self, entity_id: int) -> Optional[LibraryModelEntity35]:
        return self.db.query(LibraryModelEntity35).filter(LibraryModelEntity35.id == entity_id).first()

    def create_entity_35(self, payload: LibrarySchemaEntity35Create) -> LibraryModelEntity35:
        db_obj = LibraryModelEntity35(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_35(self, entity_id: int, payload: LibrarySchemaEntity35Update) -> Optional[LibraryModelEntity35]:
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

    def get_entity_36_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity36]:
        return self.db.query(LibraryModelEntity36).offset(skip).limit(limit).all()

    def get_entity_36_by_id(self, entity_id: int) -> Optional[LibraryModelEntity36]:
        return self.db.query(LibraryModelEntity36).filter(LibraryModelEntity36.id == entity_id).first()

    def create_entity_36(self, payload: LibrarySchemaEntity36Create) -> LibraryModelEntity36:
        db_obj = LibraryModelEntity36(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_36(self, entity_id: int, payload: LibrarySchemaEntity36Update) -> Optional[LibraryModelEntity36]:
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

    def get_entity_37_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity37]:
        return self.db.query(LibraryModelEntity37).offset(skip).limit(limit).all()

    def get_entity_37_by_id(self, entity_id: int) -> Optional[LibraryModelEntity37]:
        return self.db.query(LibraryModelEntity37).filter(LibraryModelEntity37.id == entity_id).first()

    def create_entity_37(self, payload: LibrarySchemaEntity37Create) -> LibraryModelEntity37:
        db_obj = LibraryModelEntity37(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_37(self, entity_id: int, payload: LibrarySchemaEntity37Update) -> Optional[LibraryModelEntity37]:
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

    def get_entity_38_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity38]:
        return self.db.query(LibraryModelEntity38).offset(skip).limit(limit).all()

    def get_entity_38_by_id(self, entity_id: int) -> Optional[LibraryModelEntity38]:
        return self.db.query(LibraryModelEntity38).filter(LibraryModelEntity38.id == entity_id).first()

    def create_entity_38(self, payload: LibrarySchemaEntity38Create) -> LibraryModelEntity38:
        db_obj = LibraryModelEntity38(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_38(self, entity_id: int, payload: LibrarySchemaEntity38Update) -> Optional[LibraryModelEntity38]:
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

    def get_entity_39_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity39]:
        return self.db.query(LibraryModelEntity39).offset(skip).limit(limit).all()

    def get_entity_39_by_id(self, entity_id: int) -> Optional[LibraryModelEntity39]:
        return self.db.query(LibraryModelEntity39).filter(LibraryModelEntity39.id == entity_id).first()

    def create_entity_39(self, payload: LibrarySchemaEntity39Create) -> LibraryModelEntity39:
        db_obj = LibraryModelEntity39(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_39(self, entity_id: int, payload: LibrarySchemaEntity39Update) -> Optional[LibraryModelEntity39]:
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

    def get_entity_40_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity40]:
        return self.db.query(LibraryModelEntity40).offset(skip).limit(limit).all()

    def get_entity_40_by_id(self, entity_id: int) -> Optional[LibraryModelEntity40]:
        return self.db.query(LibraryModelEntity40).filter(LibraryModelEntity40.id == entity_id).first()

    def create_entity_40(self, payload: LibrarySchemaEntity40Create) -> LibraryModelEntity40:
        db_obj = LibraryModelEntity40(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_40(self, entity_id: int, payload: LibrarySchemaEntity40Update) -> Optional[LibraryModelEntity40]:
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

    def get_entity_41_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity41]:
        return self.db.query(LibraryModelEntity41).offset(skip).limit(limit).all()

    def get_entity_41_by_id(self, entity_id: int) -> Optional[LibraryModelEntity41]:
        return self.db.query(LibraryModelEntity41).filter(LibraryModelEntity41.id == entity_id).first()

    def create_entity_41(self, payload: LibrarySchemaEntity41Create) -> LibraryModelEntity41:
        db_obj = LibraryModelEntity41(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_41(self, entity_id: int, payload: LibrarySchemaEntity41Update) -> Optional[LibraryModelEntity41]:
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

    def get_entity_42_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity42]:
        return self.db.query(LibraryModelEntity42).offset(skip).limit(limit).all()

    def get_entity_42_by_id(self, entity_id: int) -> Optional[LibraryModelEntity42]:
        return self.db.query(LibraryModelEntity42).filter(LibraryModelEntity42.id == entity_id).first()

    def create_entity_42(self, payload: LibrarySchemaEntity42Create) -> LibraryModelEntity42:
        db_obj = LibraryModelEntity42(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_42(self, entity_id: int, payload: LibrarySchemaEntity42Update) -> Optional[LibraryModelEntity42]:
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

    def get_entity_43_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity43]:
        return self.db.query(LibraryModelEntity43).offset(skip).limit(limit).all()

    def get_entity_43_by_id(self, entity_id: int) -> Optional[LibraryModelEntity43]:
        return self.db.query(LibraryModelEntity43).filter(LibraryModelEntity43.id == entity_id).first()

    def create_entity_43(self, payload: LibrarySchemaEntity43Create) -> LibraryModelEntity43:
        db_obj = LibraryModelEntity43(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_43(self, entity_id: int, payload: LibrarySchemaEntity43Update) -> Optional[LibraryModelEntity43]:
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

    def get_entity_44_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity44]:
        return self.db.query(LibraryModelEntity44).offset(skip).limit(limit).all()

    def get_entity_44_by_id(self, entity_id: int) -> Optional[LibraryModelEntity44]:
        return self.db.query(LibraryModelEntity44).filter(LibraryModelEntity44.id == entity_id).first()

    def create_entity_44(self, payload: LibrarySchemaEntity44Create) -> LibraryModelEntity44:
        db_obj = LibraryModelEntity44(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_44(self, entity_id: int, payload: LibrarySchemaEntity44Update) -> Optional[LibraryModelEntity44]:
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

    def get_entity_45_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity45]:
        return self.db.query(LibraryModelEntity45).offset(skip).limit(limit).all()

    def get_entity_45_by_id(self, entity_id: int) -> Optional[LibraryModelEntity45]:
        return self.db.query(LibraryModelEntity45).filter(LibraryModelEntity45.id == entity_id).first()

    def create_entity_45(self, payload: LibrarySchemaEntity45Create) -> LibraryModelEntity45:
        db_obj = LibraryModelEntity45(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_45(self, entity_id: int, payload: LibrarySchemaEntity45Update) -> Optional[LibraryModelEntity45]:
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

    def get_entity_46_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity46]:
        return self.db.query(LibraryModelEntity46).offset(skip).limit(limit).all()

    def get_entity_46_by_id(self, entity_id: int) -> Optional[LibraryModelEntity46]:
        return self.db.query(LibraryModelEntity46).filter(LibraryModelEntity46.id == entity_id).first()

    def create_entity_46(self, payload: LibrarySchemaEntity46Create) -> LibraryModelEntity46:
        db_obj = LibraryModelEntity46(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_46(self, entity_id: int, payload: LibrarySchemaEntity46Update) -> Optional[LibraryModelEntity46]:
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

    def get_entity_47_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity47]:
        return self.db.query(LibraryModelEntity47).offset(skip).limit(limit).all()

    def get_entity_47_by_id(self, entity_id: int) -> Optional[LibraryModelEntity47]:
        return self.db.query(LibraryModelEntity47).filter(LibraryModelEntity47.id == entity_id).first()

    def create_entity_47(self, payload: LibrarySchemaEntity47Create) -> LibraryModelEntity47:
        db_obj = LibraryModelEntity47(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_47(self, entity_id: int, payload: LibrarySchemaEntity47Update) -> Optional[LibraryModelEntity47]:
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

    def get_entity_48_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity48]:
        return self.db.query(LibraryModelEntity48).offset(skip).limit(limit).all()

    def get_entity_48_by_id(self, entity_id: int) -> Optional[LibraryModelEntity48]:
        return self.db.query(LibraryModelEntity48).filter(LibraryModelEntity48.id == entity_id).first()

    def create_entity_48(self, payload: LibrarySchemaEntity48Create) -> LibraryModelEntity48:
        db_obj = LibraryModelEntity48(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_48(self, entity_id: int, payload: LibrarySchemaEntity48Update) -> Optional[LibraryModelEntity48]:
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

    def get_entity_49_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity49]:
        return self.db.query(LibraryModelEntity49).offset(skip).limit(limit).all()

    def get_entity_49_by_id(self, entity_id: int) -> Optional[LibraryModelEntity49]:
        return self.db.query(LibraryModelEntity49).filter(LibraryModelEntity49.id == entity_id).first()

    def create_entity_49(self, payload: LibrarySchemaEntity49Create) -> LibraryModelEntity49:
        db_obj = LibraryModelEntity49(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_49(self, entity_id: int, payload: LibrarySchemaEntity49Update) -> Optional[LibraryModelEntity49]:
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

    def get_entity_50_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity50]:
        return self.db.query(LibraryModelEntity50).offset(skip).limit(limit).all()

    def get_entity_50_by_id(self, entity_id: int) -> Optional[LibraryModelEntity50]:
        return self.db.query(LibraryModelEntity50).filter(LibraryModelEntity50.id == entity_id).first()

    def create_entity_50(self, payload: LibrarySchemaEntity50Create) -> LibraryModelEntity50:
        db_obj = LibraryModelEntity50(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_50(self, entity_id: int, payload: LibrarySchemaEntity50Update) -> Optional[LibraryModelEntity50]:
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

    def get_entity_51_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity51]:
        return self.db.query(LibraryModelEntity51).offset(skip).limit(limit).all()

    def get_entity_51_by_id(self, entity_id: int) -> Optional[LibraryModelEntity51]:
        return self.db.query(LibraryModelEntity51).filter(LibraryModelEntity51.id == entity_id).first()

    def create_entity_51(self, payload: LibrarySchemaEntity51Create) -> LibraryModelEntity51:
        db_obj = LibraryModelEntity51(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_51(self, entity_id: int, payload: LibrarySchemaEntity51Update) -> Optional[LibraryModelEntity51]:
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

    def get_entity_52_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity52]:
        return self.db.query(LibraryModelEntity52).offset(skip).limit(limit).all()

    def get_entity_52_by_id(self, entity_id: int) -> Optional[LibraryModelEntity52]:
        return self.db.query(LibraryModelEntity52).filter(LibraryModelEntity52.id == entity_id).first()

    def create_entity_52(self, payload: LibrarySchemaEntity52Create) -> LibraryModelEntity52:
        db_obj = LibraryModelEntity52(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_52(self, entity_id: int, payload: LibrarySchemaEntity52Update) -> Optional[LibraryModelEntity52]:
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

    def get_entity_53_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity53]:
        return self.db.query(LibraryModelEntity53).offset(skip).limit(limit).all()

    def get_entity_53_by_id(self, entity_id: int) -> Optional[LibraryModelEntity53]:
        return self.db.query(LibraryModelEntity53).filter(LibraryModelEntity53.id == entity_id).first()

    def create_entity_53(self, payload: LibrarySchemaEntity53Create) -> LibraryModelEntity53:
        db_obj = LibraryModelEntity53(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_53(self, entity_id: int, payload: LibrarySchemaEntity53Update) -> Optional[LibraryModelEntity53]:
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

    def get_entity_54_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity54]:
        return self.db.query(LibraryModelEntity54).offset(skip).limit(limit).all()

    def get_entity_54_by_id(self, entity_id: int) -> Optional[LibraryModelEntity54]:
        return self.db.query(LibraryModelEntity54).filter(LibraryModelEntity54.id == entity_id).first()

    def create_entity_54(self, payload: LibrarySchemaEntity54Create) -> LibraryModelEntity54:
        db_obj = LibraryModelEntity54(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_54(self, entity_id: int, payload: LibrarySchemaEntity54Update) -> Optional[LibraryModelEntity54]:
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

    def get_entity_55_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity55]:
        return self.db.query(LibraryModelEntity55).offset(skip).limit(limit).all()

    def get_entity_55_by_id(self, entity_id: int) -> Optional[LibraryModelEntity55]:
        return self.db.query(LibraryModelEntity55).filter(LibraryModelEntity55.id == entity_id).first()

    def create_entity_55(self, payload: LibrarySchemaEntity55Create) -> LibraryModelEntity55:
        db_obj = LibraryModelEntity55(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_55(self, entity_id: int, payload: LibrarySchemaEntity55Update) -> Optional[LibraryModelEntity55]:
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

    def get_entity_56_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity56]:
        return self.db.query(LibraryModelEntity56).offset(skip).limit(limit).all()

    def get_entity_56_by_id(self, entity_id: int) -> Optional[LibraryModelEntity56]:
        return self.db.query(LibraryModelEntity56).filter(LibraryModelEntity56.id == entity_id).first()

    def create_entity_56(self, payload: LibrarySchemaEntity56Create) -> LibraryModelEntity56:
        db_obj = LibraryModelEntity56(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_56(self, entity_id: int, payload: LibrarySchemaEntity56Update) -> Optional[LibraryModelEntity56]:
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

    def get_entity_57_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity57]:
        return self.db.query(LibraryModelEntity57).offset(skip).limit(limit).all()

    def get_entity_57_by_id(self, entity_id: int) -> Optional[LibraryModelEntity57]:
        return self.db.query(LibraryModelEntity57).filter(LibraryModelEntity57.id == entity_id).first()

    def create_entity_57(self, payload: LibrarySchemaEntity57Create) -> LibraryModelEntity57:
        db_obj = LibraryModelEntity57(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_57(self, entity_id: int, payload: LibrarySchemaEntity57Update) -> Optional[LibraryModelEntity57]:
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

    def get_entity_58_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity58]:
        return self.db.query(LibraryModelEntity58).offset(skip).limit(limit).all()

    def get_entity_58_by_id(self, entity_id: int) -> Optional[LibraryModelEntity58]:
        return self.db.query(LibraryModelEntity58).filter(LibraryModelEntity58.id == entity_id).first()

    def create_entity_58(self, payload: LibrarySchemaEntity58Create) -> LibraryModelEntity58:
        db_obj = LibraryModelEntity58(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_58(self, entity_id: int, payload: LibrarySchemaEntity58Update) -> Optional[LibraryModelEntity58]:
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

    def get_entity_59_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity59]:
        return self.db.query(LibraryModelEntity59).offset(skip).limit(limit).all()

    def get_entity_59_by_id(self, entity_id: int) -> Optional[LibraryModelEntity59]:
        return self.db.query(LibraryModelEntity59).filter(LibraryModelEntity59.id == entity_id).first()

    def create_entity_59(self, payload: LibrarySchemaEntity59Create) -> LibraryModelEntity59:
        db_obj = LibraryModelEntity59(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_59(self, entity_id: int, payload: LibrarySchemaEntity59Update) -> Optional[LibraryModelEntity59]:
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

    def get_entity_60_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity60]:
        return self.db.query(LibraryModelEntity60).offset(skip).limit(limit).all()

    def get_entity_60_by_id(self, entity_id: int) -> Optional[LibraryModelEntity60]:
        return self.db.query(LibraryModelEntity60).filter(LibraryModelEntity60.id == entity_id).first()

    def create_entity_60(self, payload: LibrarySchemaEntity60Create) -> LibraryModelEntity60:
        db_obj = LibraryModelEntity60(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_60(self, entity_id: int, payload: LibrarySchemaEntity60Update) -> Optional[LibraryModelEntity60]:
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

    def get_entity_61_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity61]:
        return self.db.query(LibraryModelEntity61).offset(skip).limit(limit).all()

    def get_entity_61_by_id(self, entity_id: int) -> Optional[LibraryModelEntity61]:
        return self.db.query(LibraryModelEntity61).filter(LibraryModelEntity61.id == entity_id).first()

    def create_entity_61(self, payload: LibrarySchemaEntity61Create) -> LibraryModelEntity61:
        db_obj = LibraryModelEntity61(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_61(self, entity_id: int, payload: LibrarySchemaEntity61Update) -> Optional[LibraryModelEntity61]:
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

    def get_entity_62_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity62]:
        return self.db.query(LibraryModelEntity62).offset(skip).limit(limit).all()

    def get_entity_62_by_id(self, entity_id: int) -> Optional[LibraryModelEntity62]:
        return self.db.query(LibraryModelEntity62).filter(LibraryModelEntity62.id == entity_id).first()

    def create_entity_62(self, payload: LibrarySchemaEntity62Create) -> LibraryModelEntity62:
        db_obj = LibraryModelEntity62(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_62(self, entity_id: int, payload: LibrarySchemaEntity62Update) -> Optional[LibraryModelEntity62]:
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

    def get_entity_63_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity63]:
        return self.db.query(LibraryModelEntity63).offset(skip).limit(limit).all()

    def get_entity_63_by_id(self, entity_id: int) -> Optional[LibraryModelEntity63]:
        return self.db.query(LibraryModelEntity63).filter(LibraryModelEntity63.id == entity_id).first()

    def create_entity_63(self, payload: LibrarySchemaEntity63Create) -> LibraryModelEntity63:
        db_obj = LibraryModelEntity63(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_63(self, entity_id: int, payload: LibrarySchemaEntity63Update) -> Optional[LibraryModelEntity63]:
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

    def get_entity_64_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity64]:
        return self.db.query(LibraryModelEntity64).offset(skip).limit(limit).all()

    def get_entity_64_by_id(self, entity_id: int) -> Optional[LibraryModelEntity64]:
        return self.db.query(LibraryModelEntity64).filter(LibraryModelEntity64.id == entity_id).first()

    def create_entity_64(self, payload: LibrarySchemaEntity64Create) -> LibraryModelEntity64:
        db_obj = LibraryModelEntity64(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_64(self, entity_id: int, payload: LibrarySchemaEntity64Update) -> Optional[LibraryModelEntity64]:
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

    def get_entity_65_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity65]:
        return self.db.query(LibraryModelEntity65).offset(skip).limit(limit).all()

    def get_entity_65_by_id(self, entity_id: int) -> Optional[LibraryModelEntity65]:
        return self.db.query(LibraryModelEntity65).filter(LibraryModelEntity65.id == entity_id).first()

    def create_entity_65(self, payload: LibrarySchemaEntity65Create) -> LibraryModelEntity65:
        db_obj = LibraryModelEntity65(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_65(self, entity_id: int, payload: LibrarySchemaEntity65Update) -> Optional[LibraryModelEntity65]:
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

    def get_entity_66_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity66]:
        return self.db.query(LibraryModelEntity66).offset(skip).limit(limit).all()

    def get_entity_66_by_id(self, entity_id: int) -> Optional[LibraryModelEntity66]:
        return self.db.query(LibraryModelEntity66).filter(LibraryModelEntity66.id == entity_id).first()

    def create_entity_66(self, payload: LibrarySchemaEntity66Create) -> LibraryModelEntity66:
        db_obj = LibraryModelEntity66(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_66(self, entity_id: int, payload: LibrarySchemaEntity66Update) -> Optional[LibraryModelEntity66]:
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

    def get_entity_67_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity67]:
        return self.db.query(LibraryModelEntity67).offset(skip).limit(limit).all()

    def get_entity_67_by_id(self, entity_id: int) -> Optional[LibraryModelEntity67]:
        return self.db.query(LibraryModelEntity67).filter(LibraryModelEntity67.id == entity_id).first()

    def create_entity_67(self, payload: LibrarySchemaEntity67Create) -> LibraryModelEntity67:
        db_obj = LibraryModelEntity67(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_67(self, entity_id: int, payload: LibrarySchemaEntity67Update) -> Optional[LibraryModelEntity67]:
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

    def get_entity_68_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity68]:
        return self.db.query(LibraryModelEntity68).offset(skip).limit(limit).all()

    def get_entity_68_by_id(self, entity_id: int) -> Optional[LibraryModelEntity68]:
        return self.db.query(LibraryModelEntity68).filter(LibraryModelEntity68.id == entity_id).first()

    def create_entity_68(self, payload: LibrarySchemaEntity68Create) -> LibraryModelEntity68:
        db_obj = LibraryModelEntity68(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_68(self, entity_id: int, payload: LibrarySchemaEntity68Update) -> Optional[LibraryModelEntity68]:
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

    def get_entity_69_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity69]:
        return self.db.query(LibraryModelEntity69).offset(skip).limit(limit).all()

    def get_entity_69_by_id(self, entity_id: int) -> Optional[LibraryModelEntity69]:
        return self.db.query(LibraryModelEntity69).filter(LibraryModelEntity69.id == entity_id).first()

    def create_entity_69(self, payload: LibrarySchemaEntity69Create) -> LibraryModelEntity69:
        db_obj = LibraryModelEntity69(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_69(self, entity_id: int, payload: LibrarySchemaEntity69Update) -> Optional[LibraryModelEntity69]:
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

    def get_entity_70_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity70]:
        return self.db.query(LibraryModelEntity70).offset(skip).limit(limit).all()

    def get_entity_70_by_id(self, entity_id: int) -> Optional[LibraryModelEntity70]:
        return self.db.query(LibraryModelEntity70).filter(LibraryModelEntity70.id == entity_id).first()

    def create_entity_70(self, payload: LibrarySchemaEntity70Create) -> LibraryModelEntity70:
        db_obj = LibraryModelEntity70(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_70(self, entity_id: int, payload: LibrarySchemaEntity70Update) -> Optional[LibraryModelEntity70]:
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

    def get_entity_71_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity71]:
        return self.db.query(LibraryModelEntity71).offset(skip).limit(limit).all()

    def get_entity_71_by_id(self, entity_id: int) -> Optional[LibraryModelEntity71]:
        return self.db.query(LibraryModelEntity71).filter(LibraryModelEntity71.id == entity_id).first()

    def create_entity_71(self, payload: LibrarySchemaEntity71Create) -> LibraryModelEntity71:
        db_obj = LibraryModelEntity71(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_71(self, entity_id: int, payload: LibrarySchemaEntity71Update) -> Optional[LibraryModelEntity71]:
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

    def get_entity_72_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity72]:
        return self.db.query(LibraryModelEntity72).offset(skip).limit(limit).all()

    def get_entity_72_by_id(self, entity_id: int) -> Optional[LibraryModelEntity72]:
        return self.db.query(LibraryModelEntity72).filter(LibraryModelEntity72.id == entity_id).first()

    def create_entity_72(self, payload: LibrarySchemaEntity72Create) -> LibraryModelEntity72:
        db_obj = LibraryModelEntity72(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_72(self, entity_id: int, payload: LibrarySchemaEntity72Update) -> Optional[LibraryModelEntity72]:
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

    def get_entity_73_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity73]:
        return self.db.query(LibraryModelEntity73).offset(skip).limit(limit).all()

    def get_entity_73_by_id(self, entity_id: int) -> Optional[LibraryModelEntity73]:
        return self.db.query(LibraryModelEntity73).filter(LibraryModelEntity73.id == entity_id).first()

    def create_entity_73(self, payload: LibrarySchemaEntity73Create) -> LibraryModelEntity73:
        db_obj = LibraryModelEntity73(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_73(self, entity_id: int, payload: LibrarySchemaEntity73Update) -> Optional[LibraryModelEntity73]:
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

    def get_entity_74_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity74]:
        return self.db.query(LibraryModelEntity74).offset(skip).limit(limit).all()

    def get_entity_74_by_id(self, entity_id: int) -> Optional[LibraryModelEntity74]:
        return self.db.query(LibraryModelEntity74).filter(LibraryModelEntity74.id == entity_id).first()

    def create_entity_74(self, payload: LibrarySchemaEntity74Create) -> LibraryModelEntity74:
        db_obj = LibraryModelEntity74(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_74(self, entity_id: int, payload: LibrarySchemaEntity74Update) -> Optional[LibraryModelEntity74]:
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

    def get_entity_75_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity75]:
        return self.db.query(LibraryModelEntity75).offset(skip).limit(limit).all()

    def get_entity_75_by_id(self, entity_id: int) -> Optional[LibraryModelEntity75]:
        return self.db.query(LibraryModelEntity75).filter(LibraryModelEntity75.id == entity_id).first()

    def create_entity_75(self, payload: LibrarySchemaEntity75Create) -> LibraryModelEntity75:
        db_obj = LibraryModelEntity75(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_75(self, entity_id: int, payload: LibrarySchemaEntity75Update) -> Optional[LibraryModelEntity75]:
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

    def get_entity_76_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity76]:
        return self.db.query(LibraryModelEntity76).offset(skip).limit(limit).all()

    def get_entity_76_by_id(self, entity_id: int) -> Optional[LibraryModelEntity76]:
        return self.db.query(LibraryModelEntity76).filter(LibraryModelEntity76.id == entity_id).first()

    def create_entity_76(self, payload: LibrarySchemaEntity76Create) -> LibraryModelEntity76:
        db_obj = LibraryModelEntity76(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_76(self, entity_id: int, payload: LibrarySchemaEntity76Update) -> Optional[LibraryModelEntity76]:
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

    def get_entity_77_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity77]:
        return self.db.query(LibraryModelEntity77).offset(skip).limit(limit).all()

    def get_entity_77_by_id(self, entity_id: int) -> Optional[LibraryModelEntity77]:
        return self.db.query(LibraryModelEntity77).filter(LibraryModelEntity77.id == entity_id).first()

    def create_entity_77(self, payload: LibrarySchemaEntity77Create) -> LibraryModelEntity77:
        db_obj = LibraryModelEntity77(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_77(self, entity_id: int, payload: LibrarySchemaEntity77Update) -> Optional[LibraryModelEntity77]:
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

    def get_entity_78_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity78]:
        return self.db.query(LibraryModelEntity78).offset(skip).limit(limit).all()

    def get_entity_78_by_id(self, entity_id: int) -> Optional[LibraryModelEntity78]:
        return self.db.query(LibraryModelEntity78).filter(LibraryModelEntity78.id == entity_id).first()

    def create_entity_78(self, payload: LibrarySchemaEntity78Create) -> LibraryModelEntity78:
        db_obj = LibraryModelEntity78(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_78(self, entity_id: int, payload: LibrarySchemaEntity78Update) -> Optional[LibraryModelEntity78]:
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

    def get_entity_79_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity79]:
        return self.db.query(LibraryModelEntity79).offset(skip).limit(limit).all()

    def get_entity_79_by_id(self, entity_id: int) -> Optional[LibraryModelEntity79]:
        return self.db.query(LibraryModelEntity79).filter(LibraryModelEntity79.id == entity_id).first()

    def create_entity_79(self, payload: LibrarySchemaEntity79Create) -> LibraryModelEntity79:
        db_obj = LibraryModelEntity79(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_79(self, entity_id: int, payload: LibrarySchemaEntity79Update) -> Optional[LibraryModelEntity79]:
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

    def get_entity_80_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity80]:
        return self.db.query(LibraryModelEntity80).offset(skip).limit(limit).all()

    def get_entity_80_by_id(self, entity_id: int) -> Optional[LibraryModelEntity80]:
        return self.db.query(LibraryModelEntity80).filter(LibraryModelEntity80.id == entity_id).first()

    def create_entity_80(self, payload: LibrarySchemaEntity80Create) -> LibraryModelEntity80:
        db_obj = LibraryModelEntity80(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_80(self, entity_id: int, payload: LibrarySchemaEntity80Update) -> Optional[LibraryModelEntity80]:
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

    def get_entity_81_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity81]:
        return self.db.query(LibraryModelEntity81).offset(skip).limit(limit).all()

    def get_entity_81_by_id(self, entity_id: int) -> Optional[LibraryModelEntity81]:
        return self.db.query(LibraryModelEntity81).filter(LibraryModelEntity81.id == entity_id).first()

    def create_entity_81(self, payload: LibrarySchemaEntity81Create) -> LibraryModelEntity81:
        db_obj = LibraryModelEntity81(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_81(self, entity_id: int, payload: LibrarySchemaEntity81Update) -> Optional[LibraryModelEntity81]:
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

    def get_entity_82_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity82]:
        return self.db.query(LibraryModelEntity82).offset(skip).limit(limit).all()

    def get_entity_82_by_id(self, entity_id: int) -> Optional[LibraryModelEntity82]:
        return self.db.query(LibraryModelEntity82).filter(LibraryModelEntity82.id == entity_id).first()

    def create_entity_82(self, payload: LibrarySchemaEntity82Create) -> LibraryModelEntity82:
        db_obj = LibraryModelEntity82(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_82(self, entity_id: int, payload: LibrarySchemaEntity82Update) -> Optional[LibraryModelEntity82]:
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

    def get_entity_83_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity83]:
        return self.db.query(LibraryModelEntity83).offset(skip).limit(limit).all()

    def get_entity_83_by_id(self, entity_id: int) -> Optional[LibraryModelEntity83]:
        return self.db.query(LibraryModelEntity83).filter(LibraryModelEntity83.id == entity_id).first()

    def create_entity_83(self, payload: LibrarySchemaEntity83Create) -> LibraryModelEntity83:
        db_obj = LibraryModelEntity83(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_83(self, entity_id: int, payload: LibrarySchemaEntity83Update) -> Optional[LibraryModelEntity83]:
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

    def get_entity_84_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity84]:
        return self.db.query(LibraryModelEntity84).offset(skip).limit(limit).all()

    def get_entity_84_by_id(self, entity_id: int) -> Optional[LibraryModelEntity84]:
        return self.db.query(LibraryModelEntity84).filter(LibraryModelEntity84.id == entity_id).first()

    def create_entity_84(self, payload: LibrarySchemaEntity84Create) -> LibraryModelEntity84:
        db_obj = LibraryModelEntity84(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_84(self, entity_id: int, payload: LibrarySchemaEntity84Update) -> Optional[LibraryModelEntity84]:
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

    def get_entity_85_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity85]:
        return self.db.query(LibraryModelEntity85).offset(skip).limit(limit).all()

    def get_entity_85_by_id(self, entity_id: int) -> Optional[LibraryModelEntity85]:
        return self.db.query(LibraryModelEntity85).filter(LibraryModelEntity85.id == entity_id).first()

    def create_entity_85(self, payload: LibrarySchemaEntity85Create) -> LibraryModelEntity85:
        db_obj = LibraryModelEntity85(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_85(self, entity_id: int, payload: LibrarySchemaEntity85Update) -> Optional[LibraryModelEntity85]:
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

    def get_entity_86_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity86]:
        return self.db.query(LibraryModelEntity86).offset(skip).limit(limit).all()

    def get_entity_86_by_id(self, entity_id: int) -> Optional[LibraryModelEntity86]:
        return self.db.query(LibraryModelEntity86).filter(LibraryModelEntity86.id == entity_id).first()

    def create_entity_86(self, payload: LibrarySchemaEntity86Create) -> LibraryModelEntity86:
        db_obj = LibraryModelEntity86(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_86(self, entity_id: int, payload: LibrarySchemaEntity86Update) -> Optional[LibraryModelEntity86]:
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

    def get_entity_87_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity87]:
        return self.db.query(LibraryModelEntity87).offset(skip).limit(limit).all()

    def get_entity_87_by_id(self, entity_id: int) -> Optional[LibraryModelEntity87]:
        return self.db.query(LibraryModelEntity87).filter(LibraryModelEntity87.id == entity_id).first()

    def create_entity_87(self, payload: LibrarySchemaEntity87Create) -> LibraryModelEntity87:
        db_obj = LibraryModelEntity87(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_87(self, entity_id: int, payload: LibrarySchemaEntity87Update) -> Optional[LibraryModelEntity87]:
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

    def get_entity_88_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity88]:
        return self.db.query(LibraryModelEntity88).offset(skip).limit(limit).all()

    def get_entity_88_by_id(self, entity_id: int) -> Optional[LibraryModelEntity88]:
        return self.db.query(LibraryModelEntity88).filter(LibraryModelEntity88.id == entity_id).first()

    def create_entity_88(self, payload: LibrarySchemaEntity88Create) -> LibraryModelEntity88:
        db_obj = LibraryModelEntity88(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_88(self, entity_id: int, payload: LibrarySchemaEntity88Update) -> Optional[LibraryModelEntity88]:
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

    def get_entity_89_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity89]:
        return self.db.query(LibraryModelEntity89).offset(skip).limit(limit).all()

    def get_entity_89_by_id(self, entity_id: int) -> Optional[LibraryModelEntity89]:
        return self.db.query(LibraryModelEntity89).filter(LibraryModelEntity89.id == entity_id).first()

    def create_entity_89(self, payload: LibrarySchemaEntity89Create) -> LibraryModelEntity89:
        db_obj = LibraryModelEntity89(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_89(self, entity_id: int, payload: LibrarySchemaEntity89Update) -> Optional[LibraryModelEntity89]:
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

    def get_entity_90_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity90]:
        return self.db.query(LibraryModelEntity90).offset(skip).limit(limit).all()

    def get_entity_90_by_id(self, entity_id: int) -> Optional[LibraryModelEntity90]:
        return self.db.query(LibraryModelEntity90).filter(LibraryModelEntity90.id == entity_id).first()

    def create_entity_90(self, payload: LibrarySchemaEntity90Create) -> LibraryModelEntity90:
        db_obj = LibraryModelEntity90(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_90(self, entity_id: int, payload: LibrarySchemaEntity90Update) -> Optional[LibraryModelEntity90]:
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

    def get_entity_91_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity91]:
        return self.db.query(LibraryModelEntity91).offset(skip).limit(limit).all()

    def get_entity_91_by_id(self, entity_id: int) -> Optional[LibraryModelEntity91]:
        return self.db.query(LibraryModelEntity91).filter(LibraryModelEntity91.id == entity_id).first()

    def create_entity_91(self, payload: LibrarySchemaEntity91Create) -> LibraryModelEntity91:
        db_obj = LibraryModelEntity91(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_91(self, entity_id: int, payload: LibrarySchemaEntity91Update) -> Optional[LibraryModelEntity91]:
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

    def get_entity_92_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity92]:
        return self.db.query(LibraryModelEntity92).offset(skip).limit(limit).all()

    def get_entity_92_by_id(self, entity_id: int) -> Optional[LibraryModelEntity92]:
        return self.db.query(LibraryModelEntity92).filter(LibraryModelEntity92.id == entity_id).first()

    def create_entity_92(self, payload: LibrarySchemaEntity92Create) -> LibraryModelEntity92:
        db_obj = LibraryModelEntity92(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_92(self, entity_id: int, payload: LibrarySchemaEntity92Update) -> Optional[LibraryModelEntity92]:
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

    def get_entity_93_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity93]:
        return self.db.query(LibraryModelEntity93).offset(skip).limit(limit).all()

    def get_entity_93_by_id(self, entity_id: int) -> Optional[LibraryModelEntity93]:
        return self.db.query(LibraryModelEntity93).filter(LibraryModelEntity93.id == entity_id).first()

    def create_entity_93(self, payload: LibrarySchemaEntity93Create) -> LibraryModelEntity93:
        db_obj = LibraryModelEntity93(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_93(self, entity_id: int, payload: LibrarySchemaEntity93Update) -> Optional[LibraryModelEntity93]:
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

    def get_entity_94_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity94]:
        return self.db.query(LibraryModelEntity94).offset(skip).limit(limit).all()

    def get_entity_94_by_id(self, entity_id: int) -> Optional[LibraryModelEntity94]:
        return self.db.query(LibraryModelEntity94).filter(LibraryModelEntity94.id == entity_id).first()

    def create_entity_94(self, payload: LibrarySchemaEntity94Create) -> LibraryModelEntity94:
        db_obj = LibraryModelEntity94(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_94(self, entity_id: int, payload: LibrarySchemaEntity94Update) -> Optional[LibraryModelEntity94]:
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

    def get_entity_95_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity95]:
        return self.db.query(LibraryModelEntity95).offset(skip).limit(limit).all()

    def get_entity_95_by_id(self, entity_id: int) -> Optional[LibraryModelEntity95]:
        return self.db.query(LibraryModelEntity95).filter(LibraryModelEntity95.id == entity_id).first()

    def create_entity_95(self, payload: LibrarySchemaEntity95Create) -> LibraryModelEntity95:
        db_obj = LibraryModelEntity95(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_95(self, entity_id: int, payload: LibrarySchemaEntity95Update) -> Optional[LibraryModelEntity95]:
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

    def get_entity_96_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity96]:
        return self.db.query(LibraryModelEntity96).offset(skip).limit(limit).all()

    def get_entity_96_by_id(self, entity_id: int) -> Optional[LibraryModelEntity96]:
        return self.db.query(LibraryModelEntity96).filter(LibraryModelEntity96.id == entity_id).first()

    def create_entity_96(self, payload: LibrarySchemaEntity96Create) -> LibraryModelEntity96:
        db_obj = LibraryModelEntity96(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_96(self, entity_id: int, payload: LibrarySchemaEntity96Update) -> Optional[LibraryModelEntity96]:
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

    def get_entity_97_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity97]:
        return self.db.query(LibraryModelEntity97).offset(skip).limit(limit).all()

    def get_entity_97_by_id(self, entity_id: int) -> Optional[LibraryModelEntity97]:
        return self.db.query(LibraryModelEntity97).filter(LibraryModelEntity97.id == entity_id).first()

    def create_entity_97(self, payload: LibrarySchemaEntity97Create) -> LibraryModelEntity97:
        db_obj = LibraryModelEntity97(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_97(self, entity_id: int, payload: LibrarySchemaEntity97Update) -> Optional[LibraryModelEntity97]:
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

    def get_entity_98_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity98]:
        return self.db.query(LibraryModelEntity98).offset(skip).limit(limit).all()

    def get_entity_98_by_id(self, entity_id: int) -> Optional[LibraryModelEntity98]:
        return self.db.query(LibraryModelEntity98).filter(LibraryModelEntity98.id == entity_id).first()

    def create_entity_98(self, payload: LibrarySchemaEntity98Create) -> LibraryModelEntity98:
        db_obj = LibraryModelEntity98(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_98(self, entity_id: int, payload: LibrarySchemaEntity98Update) -> Optional[LibraryModelEntity98]:
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

    def get_entity_99_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity99]:
        return self.db.query(LibraryModelEntity99).offset(skip).limit(limit).all()

    def get_entity_99_by_id(self, entity_id: int) -> Optional[LibraryModelEntity99]:
        return self.db.query(LibraryModelEntity99).filter(LibraryModelEntity99.id == entity_id).first()

    def create_entity_99(self, payload: LibrarySchemaEntity99Create) -> LibraryModelEntity99:
        db_obj = LibraryModelEntity99(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_99(self, entity_id: int, payload: LibrarySchemaEntity99Update) -> Optional[LibraryModelEntity99]:
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

    def get_entity_100_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity100]:
        return self.db.query(LibraryModelEntity100).offset(skip).limit(limit).all()

    def get_entity_100_by_id(self, entity_id: int) -> Optional[LibraryModelEntity100]:
        return self.db.query(LibraryModelEntity100).filter(LibraryModelEntity100.id == entity_id).first()

    def create_entity_100(self, payload: LibrarySchemaEntity100Create) -> LibraryModelEntity100:
        db_obj = LibraryModelEntity100(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_100(self, entity_id: int, payload: LibrarySchemaEntity100Update) -> Optional[LibraryModelEntity100]:
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

    def get_entity_101_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity101]:
        return self.db.query(LibraryModelEntity101).offset(skip).limit(limit).all()

    def get_entity_101_by_id(self, entity_id: int) -> Optional[LibraryModelEntity101]:
        return self.db.query(LibraryModelEntity101).filter(LibraryModelEntity101.id == entity_id).first()

    def create_entity_101(self, payload: LibrarySchemaEntity101Create) -> LibraryModelEntity101:
        db_obj = LibraryModelEntity101(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_101(self, entity_id: int, payload: LibrarySchemaEntity101Update) -> Optional[LibraryModelEntity101]:
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

    def get_entity_102_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity102]:
        return self.db.query(LibraryModelEntity102).offset(skip).limit(limit).all()

    def get_entity_102_by_id(self, entity_id: int) -> Optional[LibraryModelEntity102]:
        return self.db.query(LibraryModelEntity102).filter(LibraryModelEntity102.id == entity_id).first()

    def create_entity_102(self, payload: LibrarySchemaEntity102Create) -> LibraryModelEntity102:
        db_obj = LibraryModelEntity102(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_102(self, entity_id: int, payload: LibrarySchemaEntity102Update) -> Optional[LibraryModelEntity102]:
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

    def get_entity_103_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity103]:
        return self.db.query(LibraryModelEntity103).offset(skip).limit(limit).all()

    def get_entity_103_by_id(self, entity_id: int) -> Optional[LibraryModelEntity103]:
        return self.db.query(LibraryModelEntity103).filter(LibraryModelEntity103.id == entity_id).first()

    def create_entity_103(self, payload: LibrarySchemaEntity103Create) -> LibraryModelEntity103:
        db_obj = LibraryModelEntity103(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_103(self, entity_id: int, payload: LibrarySchemaEntity103Update) -> Optional[LibraryModelEntity103]:
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

    def get_entity_104_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity104]:
        return self.db.query(LibraryModelEntity104).offset(skip).limit(limit).all()

    def get_entity_104_by_id(self, entity_id: int) -> Optional[LibraryModelEntity104]:
        return self.db.query(LibraryModelEntity104).filter(LibraryModelEntity104.id == entity_id).first()

    def create_entity_104(self, payload: LibrarySchemaEntity104Create) -> LibraryModelEntity104:
        db_obj = LibraryModelEntity104(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_104(self, entity_id: int, payload: LibrarySchemaEntity104Update) -> Optional[LibraryModelEntity104]:
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

    def get_entity_105_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity105]:
        return self.db.query(LibraryModelEntity105).offset(skip).limit(limit).all()

    def get_entity_105_by_id(self, entity_id: int) -> Optional[LibraryModelEntity105]:
        return self.db.query(LibraryModelEntity105).filter(LibraryModelEntity105.id == entity_id).first()

    def create_entity_105(self, payload: LibrarySchemaEntity105Create) -> LibraryModelEntity105:
        db_obj = LibraryModelEntity105(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_105(self, entity_id: int, payload: LibrarySchemaEntity105Update) -> Optional[LibraryModelEntity105]:
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

    def get_entity_106_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity106]:
        return self.db.query(LibraryModelEntity106).offset(skip).limit(limit).all()

    def get_entity_106_by_id(self, entity_id: int) -> Optional[LibraryModelEntity106]:
        return self.db.query(LibraryModelEntity106).filter(LibraryModelEntity106.id == entity_id).first()

    def create_entity_106(self, payload: LibrarySchemaEntity106Create) -> LibraryModelEntity106:
        db_obj = LibraryModelEntity106(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_106(self, entity_id: int, payload: LibrarySchemaEntity106Update) -> Optional[LibraryModelEntity106]:
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

    def get_entity_107_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity107]:
        return self.db.query(LibraryModelEntity107).offset(skip).limit(limit).all()

    def get_entity_107_by_id(self, entity_id: int) -> Optional[LibraryModelEntity107]:
        return self.db.query(LibraryModelEntity107).filter(LibraryModelEntity107.id == entity_id).first()

    def create_entity_107(self, payload: LibrarySchemaEntity107Create) -> LibraryModelEntity107:
        db_obj = LibraryModelEntity107(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_107(self, entity_id: int, payload: LibrarySchemaEntity107Update) -> Optional[LibraryModelEntity107]:
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

    def get_entity_108_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity108]:
        return self.db.query(LibraryModelEntity108).offset(skip).limit(limit).all()

    def get_entity_108_by_id(self, entity_id: int) -> Optional[LibraryModelEntity108]:
        return self.db.query(LibraryModelEntity108).filter(LibraryModelEntity108.id == entity_id).first()

    def create_entity_108(self, payload: LibrarySchemaEntity108Create) -> LibraryModelEntity108:
        db_obj = LibraryModelEntity108(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_108(self, entity_id: int, payload: LibrarySchemaEntity108Update) -> Optional[LibraryModelEntity108]:
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

    def get_entity_109_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity109]:
        return self.db.query(LibraryModelEntity109).offset(skip).limit(limit).all()

    def get_entity_109_by_id(self, entity_id: int) -> Optional[LibraryModelEntity109]:
        return self.db.query(LibraryModelEntity109).filter(LibraryModelEntity109.id == entity_id).first()

    def create_entity_109(self, payload: LibrarySchemaEntity109Create) -> LibraryModelEntity109:
        db_obj = LibraryModelEntity109(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_109(self, entity_id: int, payload: LibrarySchemaEntity109Update) -> Optional[LibraryModelEntity109]:
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

    def get_entity_110_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity110]:
        return self.db.query(LibraryModelEntity110).offset(skip).limit(limit).all()

    def get_entity_110_by_id(self, entity_id: int) -> Optional[LibraryModelEntity110]:
        return self.db.query(LibraryModelEntity110).filter(LibraryModelEntity110.id == entity_id).first()

    def create_entity_110(self, payload: LibrarySchemaEntity110Create) -> LibraryModelEntity110:
        db_obj = LibraryModelEntity110(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_110(self, entity_id: int, payload: LibrarySchemaEntity110Update) -> Optional[LibraryModelEntity110]:
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

    def get_entity_111_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity111]:
        return self.db.query(LibraryModelEntity111).offset(skip).limit(limit).all()

    def get_entity_111_by_id(self, entity_id: int) -> Optional[LibraryModelEntity111]:
        return self.db.query(LibraryModelEntity111).filter(LibraryModelEntity111.id == entity_id).first()

    def create_entity_111(self, payload: LibrarySchemaEntity111Create) -> LibraryModelEntity111:
        db_obj = LibraryModelEntity111(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_111(self, entity_id: int, payload: LibrarySchemaEntity111Update) -> Optional[LibraryModelEntity111]:
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

    def get_entity_112_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity112]:
        return self.db.query(LibraryModelEntity112).offset(skip).limit(limit).all()

    def get_entity_112_by_id(self, entity_id: int) -> Optional[LibraryModelEntity112]:
        return self.db.query(LibraryModelEntity112).filter(LibraryModelEntity112.id == entity_id).first()

    def create_entity_112(self, payload: LibrarySchemaEntity112Create) -> LibraryModelEntity112:
        db_obj = LibraryModelEntity112(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_112(self, entity_id: int, payload: LibrarySchemaEntity112Update) -> Optional[LibraryModelEntity112]:
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

    def get_entity_113_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity113]:
        return self.db.query(LibraryModelEntity113).offset(skip).limit(limit).all()

    def get_entity_113_by_id(self, entity_id: int) -> Optional[LibraryModelEntity113]:
        return self.db.query(LibraryModelEntity113).filter(LibraryModelEntity113.id == entity_id).first()

    def create_entity_113(self, payload: LibrarySchemaEntity113Create) -> LibraryModelEntity113:
        db_obj = LibraryModelEntity113(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_113(self, entity_id: int, payload: LibrarySchemaEntity113Update) -> Optional[LibraryModelEntity113]:
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

    def get_entity_114_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity114]:
        return self.db.query(LibraryModelEntity114).offset(skip).limit(limit).all()

    def get_entity_114_by_id(self, entity_id: int) -> Optional[LibraryModelEntity114]:
        return self.db.query(LibraryModelEntity114).filter(LibraryModelEntity114.id == entity_id).first()

    def create_entity_114(self, payload: LibrarySchemaEntity114Create) -> LibraryModelEntity114:
        db_obj = LibraryModelEntity114(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_114(self, entity_id: int, payload: LibrarySchemaEntity114Update) -> Optional[LibraryModelEntity114]:
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

    def get_entity_115_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity115]:
        return self.db.query(LibraryModelEntity115).offset(skip).limit(limit).all()

    def get_entity_115_by_id(self, entity_id: int) -> Optional[LibraryModelEntity115]:
        return self.db.query(LibraryModelEntity115).filter(LibraryModelEntity115.id == entity_id).first()

    def create_entity_115(self, payload: LibrarySchemaEntity115Create) -> LibraryModelEntity115:
        db_obj = LibraryModelEntity115(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_115(self, entity_id: int, payload: LibrarySchemaEntity115Update) -> Optional[LibraryModelEntity115]:
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

    def get_entity_116_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity116]:
        return self.db.query(LibraryModelEntity116).offset(skip).limit(limit).all()

    def get_entity_116_by_id(self, entity_id: int) -> Optional[LibraryModelEntity116]:
        return self.db.query(LibraryModelEntity116).filter(LibraryModelEntity116.id == entity_id).first()

    def create_entity_116(self, payload: LibrarySchemaEntity116Create) -> LibraryModelEntity116:
        db_obj = LibraryModelEntity116(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_116(self, entity_id: int, payload: LibrarySchemaEntity116Update) -> Optional[LibraryModelEntity116]:
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

    def get_entity_117_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity117]:
        return self.db.query(LibraryModelEntity117).offset(skip).limit(limit).all()

    def get_entity_117_by_id(self, entity_id: int) -> Optional[LibraryModelEntity117]:
        return self.db.query(LibraryModelEntity117).filter(LibraryModelEntity117.id == entity_id).first()

    def create_entity_117(self, payload: LibrarySchemaEntity117Create) -> LibraryModelEntity117:
        db_obj = LibraryModelEntity117(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_117(self, entity_id: int, payload: LibrarySchemaEntity117Update) -> Optional[LibraryModelEntity117]:
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

    def get_entity_118_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity118]:
        return self.db.query(LibraryModelEntity118).offset(skip).limit(limit).all()

    def get_entity_118_by_id(self, entity_id: int) -> Optional[LibraryModelEntity118]:
        return self.db.query(LibraryModelEntity118).filter(LibraryModelEntity118.id == entity_id).first()

    def create_entity_118(self, payload: LibrarySchemaEntity118Create) -> LibraryModelEntity118:
        db_obj = LibraryModelEntity118(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_118(self, entity_id: int, payload: LibrarySchemaEntity118Update) -> Optional[LibraryModelEntity118]:
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

    def get_entity_119_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity119]:
        return self.db.query(LibraryModelEntity119).offset(skip).limit(limit).all()

    def get_entity_119_by_id(self, entity_id: int) -> Optional[LibraryModelEntity119]:
        return self.db.query(LibraryModelEntity119).filter(LibraryModelEntity119.id == entity_id).first()

    def create_entity_119(self, payload: LibrarySchemaEntity119Create) -> LibraryModelEntity119:
        db_obj = LibraryModelEntity119(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_119(self, entity_id: int, payload: LibrarySchemaEntity119Update) -> Optional[LibraryModelEntity119]:
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

    def get_entity_120_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity120]:
        return self.db.query(LibraryModelEntity120).offset(skip).limit(limit).all()

    def get_entity_120_by_id(self, entity_id: int) -> Optional[LibraryModelEntity120]:
        return self.db.query(LibraryModelEntity120).filter(LibraryModelEntity120.id == entity_id).first()

    def create_entity_120(self, payload: LibrarySchemaEntity120Create) -> LibraryModelEntity120:
        db_obj = LibraryModelEntity120(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_120(self, entity_id: int, payload: LibrarySchemaEntity120Update) -> Optional[LibraryModelEntity120]:
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

    def get_entity_121_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity121]:
        return self.db.query(LibraryModelEntity121).offset(skip).limit(limit).all()

    def get_entity_121_by_id(self, entity_id: int) -> Optional[LibraryModelEntity121]:
        return self.db.query(LibraryModelEntity121).filter(LibraryModelEntity121.id == entity_id).first()

    def create_entity_121(self, payload: LibrarySchemaEntity121Create) -> LibraryModelEntity121:
        db_obj = LibraryModelEntity121(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_121(self, entity_id: int, payload: LibrarySchemaEntity121Update) -> Optional[LibraryModelEntity121]:
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

    def get_entity_122_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity122]:
        return self.db.query(LibraryModelEntity122).offset(skip).limit(limit).all()

    def get_entity_122_by_id(self, entity_id: int) -> Optional[LibraryModelEntity122]:
        return self.db.query(LibraryModelEntity122).filter(LibraryModelEntity122.id == entity_id).first()

    def create_entity_122(self, payload: LibrarySchemaEntity122Create) -> LibraryModelEntity122:
        db_obj = LibraryModelEntity122(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_122(self, entity_id: int, payload: LibrarySchemaEntity122Update) -> Optional[LibraryModelEntity122]:
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

    def get_entity_123_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity123]:
        return self.db.query(LibraryModelEntity123).offset(skip).limit(limit).all()

    def get_entity_123_by_id(self, entity_id: int) -> Optional[LibraryModelEntity123]:
        return self.db.query(LibraryModelEntity123).filter(LibraryModelEntity123.id == entity_id).first()

    def create_entity_123(self, payload: LibrarySchemaEntity123Create) -> LibraryModelEntity123:
        db_obj = LibraryModelEntity123(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_123(self, entity_id: int, payload: LibrarySchemaEntity123Update) -> Optional[LibraryModelEntity123]:
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

    def get_entity_124_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity124]:
        return self.db.query(LibraryModelEntity124).offset(skip).limit(limit).all()

    def get_entity_124_by_id(self, entity_id: int) -> Optional[LibraryModelEntity124]:
        return self.db.query(LibraryModelEntity124).filter(LibraryModelEntity124.id == entity_id).first()

    def create_entity_124(self, payload: LibrarySchemaEntity124Create) -> LibraryModelEntity124:
        db_obj = LibraryModelEntity124(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_124(self, entity_id: int, payload: LibrarySchemaEntity124Update) -> Optional[LibraryModelEntity124]:
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

    def get_entity_125_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity125]:
        return self.db.query(LibraryModelEntity125).offset(skip).limit(limit).all()

    def get_entity_125_by_id(self, entity_id: int) -> Optional[LibraryModelEntity125]:
        return self.db.query(LibraryModelEntity125).filter(LibraryModelEntity125.id == entity_id).first()

    def create_entity_125(self, payload: LibrarySchemaEntity125Create) -> LibraryModelEntity125:
        db_obj = LibraryModelEntity125(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_125(self, entity_id: int, payload: LibrarySchemaEntity125Update) -> Optional[LibraryModelEntity125]:
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

    def get_entity_126_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity126]:
        return self.db.query(LibraryModelEntity126).offset(skip).limit(limit).all()

    def get_entity_126_by_id(self, entity_id: int) -> Optional[LibraryModelEntity126]:
        return self.db.query(LibraryModelEntity126).filter(LibraryModelEntity126.id == entity_id).first()

    def create_entity_126(self, payload: LibrarySchemaEntity126Create) -> LibraryModelEntity126:
        db_obj = LibraryModelEntity126(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_126(self, entity_id: int, payload: LibrarySchemaEntity126Update) -> Optional[LibraryModelEntity126]:
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

    def get_entity_127_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity127]:
        return self.db.query(LibraryModelEntity127).offset(skip).limit(limit).all()

    def get_entity_127_by_id(self, entity_id: int) -> Optional[LibraryModelEntity127]:
        return self.db.query(LibraryModelEntity127).filter(LibraryModelEntity127.id == entity_id).first()

    def create_entity_127(self, payload: LibrarySchemaEntity127Create) -> LibraryModelEntity127:
        db_obj = LibraryModelEntity127(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_127(self, entity_id: int, payload: LibrarySchemaEntity127Update) -> Optional[LibraryModelEntity127]:
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

    def get_entity_128_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity128]:
        return self.db.query(LibraryModelEntity128).offset(skip).limit(limit).all()

    def get_entity_128_by_id(self, entity_id: int) -> Optional[LibraryModelEntity128]:
        return self.db.query(LibraryModelEntity128).filter(LibraryModelEntity128.id == entity_id).first()

    def create_entity_128(self, payload: LibrarySchemaEntity128Create) -> LibraryModelEntity128:
        db_obj = LibraryModelEntity128(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_128(self, entity_id: int, payload: LibrarySchemaEntity128Update) -> Optional[LibraryModelEntity128]:
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

    def get_entity_129_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity129]:
        return self.db.query(LibraryModelEntity129).offset(skip).limit(limit).all()

    def get_entity_129_by_id(self, entity_id: int) -> Optional[LibraryModelEntity129]:
        return self.db.query(LibraryModelEntity129).filter(LibraryModelEntity129.id == entity_id).first()

    def create_entity_129(self, payload: LibrarySchemaEntity129Create) -> LibraryModelEntity129:
        db_obj = LibraryModelEntity129(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_129(self, entity_id: int, payload: LibrarySchemaEntity129Update) -> Optional[LibraryModelEntity129]:
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

    def get_entity_130_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity130]:
        return self.db.query(LibraryModelEntity130).offset(skip).limit(limit).all()

    def get_entity_130_by_id(self, entity_id: int) -> Optional[LibraryModelEntity130]:
        return self.db.query(LibraryModelEntity130).filter(LibraryModelEntity130.id == entity_id).first()

    def create_entity_130(self, payload: LibrarySchemaEntity130Create) -> LibraryModelEntity130:
        db_obj = LibraryModelEntity130(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_130(self, entity_id: int, payload: LibrarySchemaEntity130Update) -> Optional[LibraryModelEntity130]:
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

    def get_entity_131_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity131]:
        return self.db.query(LibraryModelEntity131).offset(skip).limit(limit).all()

    def get_entity_131_by_id(self, entity_id: int) -> Optional[LibraryModelEntity131]:
        return self.db.query(LibraryModelEntity131).filter(LibraryModelEntity131.id == entity_id).first()

    def create_entity_131(self, payload: LibrarySchemaEntity131Create) -> LibraryModelEntity131:
        db_obj = LibraryModelEntity131(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_131(self, entity_id: int, payload: LibrarySchemaEntity131Update) -> Optional[LibraryModelEntity131]:
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

    def get_entity_132_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity132]:
        return self.db.query(LibraryModelEntity132).offset(skip).limit(limit).all()

    def get_entity_132_by_id(self, entity_id: int) -> Optional[LibraryModelEntity132]:
        return self.db.query(LibraryModelEntity132).filter(LibraryModelEntity132.id == entity_id).first()

    def create_entity_132(self, payload: LibrarySchemaEntity132Create) -> LibraryModelEntity132:
        db_obj = LibraryModelEntity132(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_132(self, entity_id: int, payload: LibrarySchemaEntity132Update) -> Optional[LibraryModelEntity132]:
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

    def get_entity_133_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity133]:
        return self.db.query(LibraryModelEntity133).offset(skip).limit(limit).all()

    def get_entity_133_by_id(self, entity_id: int) -> Optional[LibraryModelEntity133]:
        return self.db.query(LibraryModelEntity133).filter(LibraryModelEntity133.id == entity_id).first()

    def create_entity_133(self, payload: LibrarySchemaEntity133Create) -> LibraryModelEntity133:
        db_obj = LibraryModelEntity133(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_133(self, entity_id: int, payload: LibrarySchemaEntity133Update) -> Optional[LibraryModelEntity133]:
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

    def get_entity_134_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity134]:
        return self.db.query(LibraryModelEntity134).offset(skip).limit(limit).all()

    def get_entity_134_by_id(self, entity_id: int) -> Optional[LibraryModelEntity134]:
        return self.db.query(LibraryModelEntity134).filter(LibraryModelEntity134.id == entity_id).first()

    def create_entity_134(self, payload: LibrarySchemaEntity134Create) -> LibraryModelEntity134:
        db_obj = LibraryModelEntity134(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_134(self, entity_id: int, payload: LibrarySchemaEntity134Update) -> Optional[LibraryModelEntity134]:
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

    def get_entity_135_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity135]:
        return self.db.query(LibraryModelEntity135).offset(skip).limit(limit).all()

    def get_entity_135_by_id(self, entity_id: int) -> Optional[LibraryModelEntity135]:
        return self.db.query(LibraryModelEntity135).filter(LibraryModelEntity135.id == entity_id).first()

    def create_entity_135(self, payload: LibrarySchemaEntity135Create) -> LibraryModelEntity135:
        db_obj = LibraryModelEntity135(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_135(self, entity_id: int, payload: LibrarySchemaEntity135Update) -> Optional[LibraryModelEntity135]:
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

    def get_entity_136_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity136]:
        return self.db.query(LibraryModelEntity136).offset(skip).limit(limit).all()

    def get_entity_136_by_id(self, entity_id: int) -> Optional[LibraryModelEntity136]:
        return self.db.query(LibraryModelEntity136).filter(LibraryModelEntity136.id == entity_id).first()

    def create_entity_136(self, payload: LibrarySchemaEntity136Create) -> LibraryModelEntity136:
        db_obj = LibraryModelEntity136(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_136(self, entity_id: int, payload: LibrarySchemaEntity136Update) -> Optional[LibraryModelEntity136]:
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

    def get_entity_137_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity137]:
        return self.db.query(LibraryModelEntity137).offset(skip).limit(limit).all()

    def get_entity_137_by_id(self, entity_id: int) -> Optional[LibraryModelEntity137]:
        return self.db.query(LibraryModelEntity137).filter(LibraryModelEntity137.id == entity_id).first()

    def create_entity_137(self, payload: LibrarySchemaEntity137Create) -> LibraryModelEntity137:
        db_obj = LibraryModelEntity137(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_137(self, entity_id: int, payload: LibrarySchemaEntity137Update) -> Optional[LibraryModelEntity137]:
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

    def get_entity_138_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity138]:
        return self.db.query(LibraryModelEntity138).offset(skip).limit(limit).all()

    def get_entity_138_by_id(self, entity_id: int) -> Optional[LibraryModelEntity138]:
        return self.db.query(LibraryModelEntity138).filter(LibraryModelEntity138.id == entity_id).first()

    def create_entity_138(self, payload: LibrarySchemaEntity138Create) -> LibraryModelEntity138:
        db_obj = LibraryModelEntity138(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_138(self, entity_id: int, payload: LibrarySchemaEntity138Update) -> Optional[LibraryModelEntity138]:
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

    def get_entity_139_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity139]:
        return self.db.query(LibraryModelEntity139).offset(skip).limit(limit).all()

    def get_entity_139_by_id(self, entity_id: int) -> Optional[LibraryModelEntity139]:
        return self.db.query(LibraryModelEntity139).filter(LibraryModelEntity139.id == entity_id).first()

    def create_entity_139(self, payload: LibrarySchemaEntity139Create) -> LibraryModelEntity139:
        db_obj = LibraryModelEntity139(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_139(self, entity_id: int, payload: LibrarySchemaEntity139Update) -> Optional[LibraryModelEntity139]:
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

    def get_entity_140_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity140]:
        return self.db.query(LibraryModelEntity140).offset(skip).limit(limit).all()

    def get_entity_140_by_id(self, entity_id: int) -> Optional[LibraryModelEntity140]:
        return self.db.query(LibraryModelEntity140).filter(LibraryModelEntity140.id == entity_id).first()

    def create_entity_140(self, payload: LibrarySchemaEntity140Create) -> LibraryModelEntity140:
        db_obj = LibraryModelEntity140(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_140(self, entity_id: int, payload: LibrarySchemaEntity140Update) -> Optional[LibraryModelEntity140]:
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

    def get_entity_141_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity141]:
        return self.db.query(LibraryModelEntity141).offset(skip).limit(limit).all()

    def get_entity_141_by_id(self, entity_id: int) -> Optional[LibraryModelEntity141]:
        return self.db.query(LibraryModelEntity141).filter(LibraryModelEntity141.id == entity_id).first()

    def create_entity_141(self, payload: LibrarySchemaEntity141Create) -> LibraryModelEntity141:
        db_obj = LibraryModelEntity141(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_141(self, entity_id: int, payload: LibrarySchemaEntity141Update) -> Optional[LibraryModelEntity141]:
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

    def get_entity_142_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity142]:
        return self.db.query(LibraryModelEntity142).offset(skip).limit(limit).all()

    def get_entity_142_by_id(self, entity_id: int) -> Optional[LibraryModelEntity142]:
        return self.db.query(LibraryModelEntity142).filter(LibraryModelEntity142.id == entity_id).first()

    def create_entity_142(self, payload: LibrarySchemaEntity142Create) -> LibraryModelEntity142:
        db_obj = LibraryModelEntity142(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_142(self, entity_id: int, payload: LibrarySchemaEntity142Update) -> Optional[LibraryModelEntity142]:
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

    def get_entity_143_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity143]:
        return self.db.query(LibraryModelEntity143).offset(skip).limit(limit).all()

    def get_entity_143_by_id(self, entity_id: int) -> Optional[LibraryModelEntity143]:
        return self.db.query(LibraryModelEntity143).filter(LibraryModelEntity143.id == entity_id).first()

    def create_entity_143(self, payload: LibrarySchemaEntity143Create) -> LibraryModelEntity143:
        db_obj = LibraryModelEntity143(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_143(self, entity_id: int, payload: LibrarySchemaEntity143Update) -> Optional[LibraryModelEntity143]:
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

    def get_entity_144_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity144]:
        return self.db.query(LibraryModelEntity144).offset(skip).limit(limit).all()

    def get_entity_144_by_id(self, entity_id: int) -> Optional[LibraryModelEntity144]:
        return self.db.query(LibraryModelEntity144).filter(LibraryModelEntity144.id == entity_id).first()

    def create_entity_144(self, payload: LibrarySchemaEntity144Create) -> LibraryModelEntity144:
        db_obj = LibraryModelEntity144(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_144(self, entity_id: int, payload: LibrarySchemaEntity144Update) -> Optional[LibraryModelEntity144]:
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

    def get_entity_145_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity145]:
        return self.db.query(LibraryModelEntity145).offset(skip).limit(limit).all()

    def get_entity_145_by_id(self, entity_id: int) -> Optional[LibraryModelEntity145]:
        return self.db.query(LibraryModelEntity145).filter(LibraryModelEntity145.id == entity_id).first()

    def create_entity_145(self, payload: LibrarySchemaEntity145Create) -> LibraryModelEntity145:
        db_obj = LibraryModelEntity145(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_145(self, entity_id: int, payload: LibrarySchemaEntity145Update) -> Optional[LibraryModelEntity145]:
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

    def get_entity_146_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity146]:
        return self.db.query(LibraryModelEntity146).offset(skip).limit(limit).all()

    def get_entity_146_by_id(self, entity_id: int) -> Optional[LibraryModelEntity146]:
        return self.db.query(LibraryModelEntity146).filter(LibraryModelEntity146.id == entity_id).first()

    def create_entity_146(self, payload: LibrarySchemaEntity146Create) -> LibraryModelEntity146:
        db_obj = LibraryModelEntity146(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_146(self, entity_id: int, payload: LibrarySchemaEntity146Update) -> Optional[LibraryModelEntity146]:
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

    def get_entity_147_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity147]:
        return self.db.query(LibraryModelEntity147).offset(skip).limit(limit).all()

    def get_entity_147_by_id(self, entity_id: int) -> Optional[LibraryModelEntity147]:
        return self.db.query(LibraryModelEntity147).filter(LibraryModelEntity147.id == entity_id).first()

    def create_entity_147(self, payload: LibrarySchemaEntity147Create) -> LibraryModelEntity147:
        db_obj = LibraryModelEntity147(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_147(self, entity_id: int, payload: LibrarySchemaEntity147Update) -> Optional[LibraryModelEntity147]:
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

    def get_entity_148_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity148]:
        return self.db.query(LibraryModelEntity148).offset(skip).limit(limit).all()

    def get_entity_148_by_id(self, entity_id: int) -> Optional[LibraryModelEntity148]:
        return self.db.query(LibraryModelEntity148).filter(LibraryModelEntity148.id == entity_id).first()

    def create_entity_148(self, payload: LibrarySchemaEntity148Create) -> LibraryModelEntity148:
        db_obj = LibraryModelEntity148(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_148(self, entity_id: int, payload: LibrarySchemaEntity148Update) -> Optional[LibraryModelEntity148]:
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

    def get_entity_149_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity149]:
        return self.db.query(LibraryModelEntity149).offset(skip).limit(limit).all()

    def get_entity_149_by_id(self, entity_id: int) -> Optional[LibraryModelEntity149]:
        return self.db.query(LibraryModelEntity149).filter(LibraryModelEntity149.id == entity_id).first()

    def create_entity_149(self, payload: LibrarySchemaEntity149Create) -> LibraryModelEntity149:
        db_obj = LibraryModelEntity149(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_149(self, entity_id: int, payload: LibrarySchemaEntity149Update) -> Optional[LibraryModelEntity149]:
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

    def get_entity_150_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity150]:
        return self.db.query(LibraryModelEntity150).offset(skip).limit(limit).all()

    def get_entity_150_by_id(self, entity_id: int) -> Optional[LibraryModelEntity150]:
        return self.db.query(LibraryModelEntity150).filter(LibraryModelEntity150.id == entity_id).first()

    def create_entity_150(self, payload: LibrarySchemaEntity150Create) -> LibraryModelEntity150:
        db_obj = LibraryModelEntity150(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_150(self, entity_id: int, payload: LibrarySchemaEntity150Update) -> Optional[LibraryModelEntity150]:
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

    def get_entity_151_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity151]:
        return self.db.query(LibraryModelEntity151).offset(skip).limit(limit).all()

    def get_entity_151_by_id(self, entity_id: int) -> Optional[LibraryModelEntity151]:
        return self.db.query(LibraryModelEntity151).filter(LibraryModelEntity151.id == entity_id).first()

    def create_entity_151(self, payload: LibrarySchemaEntity151Create) -> LibraryModelEntity151:
        db_obj = LibraryModelEntity151(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_151(self, entity_id: int, payload: LibrarySchemaEntity151Update) -> Optional[LibraryModelEntity151]:
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

    def get_entity_152_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity152]:
        return self.db.query(LibraryModelEntity152).offset(skip).limit(limit).all()

    def get_entity_152_by_id(self, entity_id: int) -> Optional[LibraryModelEntity152]:
        return self.db.query(LibraryModelEntity152).filter(LibraryModelEntity152.id == entity_id).first()

    def create_entity_152(self, payload: LibrarySchemaEntity152Create) -> LibraryModelEntity152:
        db_obj = LibraryModelEntity152(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_152(self, entity_id: int, payload: LibrarySchemaEntity152Update) -> Optional[LibraryModelEntity152]:
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

    def get_entity_153_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity153]:
        return self.db.query(LibraryModelEntity153).offset(skip).limit(limit).all()

    def get_entity_153_by_id(self, entity_id: int) -> Optional[LibraryModelEntity153]:
        return self.db.query(LibraryModelEntity153).filter(LibraryModelEntity153.id == entity_id).first()

    def create_entity_153(self, payload: LibrarySchemaEntity153Create) -> LibraryModelEntity153:
        db_obj = LibraryModelEntity153(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_153(self, entity_id: int, payload: LibrarySchemaEntity153Update) -> Optional[LibraryModelEntity153]:
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

    def get_entity_154_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity154]:
        return self.db.query(LibraryModelEntity154).offset(skip).limit(limit).all()

    def get_entity_154_by_id(self, entity_id: int) -> Optional[LibraryModelEntity154]:
        return self.db.query(LibraryModelEntity154).filter(LibraryModelEntity154.id == entity_id).first()

    def create_entity_154(self, payload: LibrarySchemaEntity154Create) -> LibraryModelEntity154:
        db_obj = LibraryModelEntity154(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_154(self, entity_id: int, payload: LibrarySchemaEntity154Update) -> Optional[LibraryModelEntity154]:
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

    def get_entity_155_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity155]:
        return self.db.query(LibraryModelEntity155).offset(skip).limit(limit).all()

    def get_entity_155_by_id(self, entity_id: int) -> Optional[LibraryModelEntity155]:
        return self.db.query(LibraryModelEntity155).filter(LibraryModelEntity155.id == entity_id).first()

    def create_entity_155(self, payload: LibrarySchemaEntity155Create) -> LibraryModelEntity155:
        db_obj = LibraryModelEntity155(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_155(self, entity_id: int, payload: LibrarySchemaEntity155Update) -> Optional[LibraryModelEntity155]:
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

    def get_entity_156_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity156]:
        return self.db.query(LibraryModelEntity156).offset(skip).limit(limit).all()

    def get_entity_156_by_id(self, entity_id: int) -> Optional[LibraryModelEntity156]:
        return self.db.query(LibraryModelEntity156).filter(LibraryModelEntity156.id == entity_id).first()

    def create_entity_156(self, payload: LibrarySchemaEntity156Create) -> LibraryModelEntity156:
        db_obj = LibraryModelEntity156(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_156(self, entity_id: int, payload: LibrarySchemaEntity156Update) -> Optional[LibraryModelEntity156]:
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

    def get_entity_157_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity157]:
        return self.db.query(LibraryModelEntity157).offset(skip).limit(limit).all()

    def get_entity_157_by_id(self, entity_id: int) -> Optional[LibraryModelEntity157]:
        return self.db.query(LibraryModelEntity157).filter(LibraryModelEntity157.id == entity_id).first()

    def create_entity_157(self, payload: LibrarySchemaEntity157Create) -> LibraryModelEntity157:
        db_obj = LibraryModelEntity157(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_157(self, entity_id: int, payload: LibrarySchemaEntity157Update) -> Optional[LibraryModelEntity157]:
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

    def get_entity_158_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity158]:
        return self.db.query(LibraryModelEntity158).offset(skip).limit(limit).all()

    def get_entity_158_by_id(self, entity_id: int) -> Optional[LibraryModelEntity158]:
        return self.db.query(LibraryModelEntity158).filter(LibraryModelEntity158.id == entity_id).first()

    def create_entity_158(self, payload: LibrarySchemaEntity158Create) -> LibraryModelEntity158:
        db_obj = LibraryModelEntity158(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_158(self, entity_id: int, payload: LibrarySchemaEntity158Update) -> Optional[LibraryModelEntity158]:
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

    def get_entity_159_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity159]:
        return self.db.query(LibraryModelEntity159).offset(skip).limit(limit).all()

    def get_entity_159_by_id(self, entity_id: int) -> Optional[LibraryModelEntity159]:
        return self.db.query(LibraryModelEntity159).filter(LibraryModelEntity159.id == entity_id).first()

    def create_entity_159(self, payload: LibrarySchemaEntity159Create) -> LibraryModelEntity159:
        db_obj = LibraryModelEntity159(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_159(self, entity_id: int, payload: LibrarySchemaEntity159Update) -> Optional[LibraryModelEntity159]:
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

    def get_entity_160_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity160]:
        return self.db.query(LibraryModelEntity160).offset(skip).limit(limit).all()

    def get_entity_160_by_id(self, entity_id: int) -> Optional[LibraryModelEntity160]:
        return self.db.query(LibraryModelEntity160).filter(LibraryModelEntity160.id == entity_id).first()

    def create_entity_160(self, payload: LibrarySchemaEntity160Create) -> LibraryModelEntity160:
        db_obj = LibraryModelEntity160(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_160(self, entity_id: int, payload: LibrarySchemaEntity160Update) -> Optional[LibraryModelEntity160]:
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

    def get_entity_161_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity161]:
        return self.db.query(LibraryModelEntity161).offset(skip).limit(limit).all()

    def get_entity_161_by_id(self, entity_id: int) -> Optional[LibraryModelEntity161]:
        return self.db.query(LibraryModelEntity161).filter(LibraryModelEntity161.id == entity_id).first()

    def create_entity_161(self, payload: LibrarySchemaEntity161Create) -> LibraryModelEntity161:
        db_obj = LibraryModelEntity161(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_161(self, entity_id: int, payload: LibrarySchemaEntity161Update) -> Optional[LibraryModelEntity161]:
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

    def get_entity_162_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity162]:
        return self.db.query(LibraryModelEntity162).offset(skip).limit(limit).all()

    def get_entity_162_by_id(self, entity_id: int) -> Optional[LibraryModelEntity162]:
        return self.db.query(LibraryModelEntity162).filter(LibraryModelEntity162.id == entity_id).first()

    def create_entity_162(self, payload: LibrarySchemaEntity162Create) -> LibraryModelEntity162:
        db_obj = LibraryModelEntity162(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_162(self, entity_id: int, payload: LibrarySchemaEntity162Update) -> Optional[LibraryModelEntity162]:
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

    def get_entity_163_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity163]:
        return self.db.query(LibraryModelEntity163).offset(skip).limit(limit).all()

    def get_entity_163_by_id(self, entity_id: int) -> Optional[LibraryModelEntity163]:
        return self.db.query(LibraryModelEntity163).filter(LibraryModelEntity163.id == entity_id).first()

    def create_entity_163(self, payload: LibrarySchemaEntity163Create) -> LibraryModelEntity163:
        db_obj = LibraryModelEntity163(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_163(self, entity_id: int, payload: LibrarySchemaEntity163Update) -> Optional[LibraryModelEntity163]:
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

    def get_entity_164_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity164]:
        return self.db.query(LibraryModelEntity164).offset(skip).limit(limit).all()

    def get_entity_164_by_id(self, entity_id: int) -> Optional[LibraryModelEntity164]:
        return self.db.query(LibraryModelEntity164).filter(LibraryModelEntity164.id == entity_id).first()

    def create_entity_164(self, payload: LibrarySchemaEntity164Create) -> LibraryModelEntity164:
        db_obj = LibraryModelEntity164(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_164(self, entity_id: int, payload: LibrarySchemaEntity164Update) -> Optional[LibraryModelEntity164]:
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

    def get_entity_165_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity165]:
        return self.db.query(LibraryModelEntity165).offset(skip).limit(limit).all()

    def get_entity_165_by_id(self, entity_id: int) -> Optional[LibraryModelEntity165]:
        return self.db.query(LibraryModelEntity165).filter(LibraryModelEntity165.id == entity_id).first()

    def create_entity_165(self, payload: LibrarySchemaEntity165Create) -> LibraryModelEntity165:
        db_obj = LibraryModelEntity165(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_165(self, entity_id: int, payload: LibrarySchemaEntity165Update) -> Optional[LibraryModelEntity165]:
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

    def get_entity_166_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity166]:
        return self.db.query(LibraryModelEntity166).offset(skip).limit(limit).all()

    def get_entity_166_by_id(self, entity_id: int) -> Optional[LibraryModelEntity166]:
        return self.db.query(LibraryModelEntity166).filter(LibraryModelEntity166.id == entity_id).first()

    def create_entity_166(self, payload: LibrarySchemaEntity166Create) -> LibraryModelEntity166:
        db_obj = LibraryModelEntity166(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_166(self, entity_id: int, payload: LibrarySchemaEntity166Update) -> Optional[LibraryModelEntity166]:
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

    def get_entity_167_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity167]:
        return self.db.query(LibraryModelEntity167).offset(skip).limit(limit).all()

    def get_entity_167_by_id(self, entity_id: int) -> Optional[LibraryModelEntity167]:
        return self.db.query(LibraryModelEntity167).filter(LibraryModelEntity167.id == entity_id).first()

    def create_entity_167(self, payload: LibrarySchemaEntity167Create) -> LibraryModelEntity167:
        db_obj = LibraryModelEntity167(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_167(self, entity_id: int, payload: LibrarySchemaEntity167Update) -> Optional[LibraryModelEntity167]:
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

    def get_entity_168_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity168]:
        return self.db.query(LibraryModelEntity168).offset(skip).limit(limit).all()

    def get_entity_168_by_id(self, entity_id: int) -> Optional[LibraryModelEntity168]:
        return self.db.query(LibraryModelEntity168).filter(LibraryModelEntity168.id == entity_id).first()

    def create_entity_168(self, payload: LibrarySchemaEntity168Create) -> LibraryModelEntity168:
        db_obj = LibraryModelEntity168(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_168(self, entity_id: int, payload: LibrarySchemaEntity168Update) -> Optional[LibraryModelEntity168]:
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

    def get_entity_169_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity169]:
        return self.db.query(LibraryModelEntity169).offset(skip).limit(limit).all()

    def get_entity_169_by_id(self, entity_id: int) -> Optional[LibraryModelEntity169]:
        return self.db.query(LibraryModelEntity169).filter(LibraryModelEntity169.id == entity_id).first()

    def create_entity_169(self, payload: LibrarySchemaEntity169Create) -> LibraryModelEntity169:
        db_obj = LibraryModelEntity169(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_169(self, entity_id: int, payload: LibrarySchemaEntity169Update) -> Optional[LibraryModelEntity169]:
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

    def get_entity_170_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity170]:
        return self.db.query(LibraryModelEntity170).offset(skip).limit(limit).all()

    def get_entity_170_by_id(self, entity_id: int) -> Optional[LibraryModelEntity170]:
        return self.db.query(LibraryModelEntity170).filter(LibraryModelEntity170.id == entity_id).first()

    def create_entity_170(self, payload: LibrarySchemaEntity170Create) -> LibraryModelEntity170:
        db_obj = LibraryModelEntity170(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_170(self, entity_id: int, payload: LibrarySchemaEntity170Update) -> Optional[LibraryModelEntity170]:
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

    def get_entity_171_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity171]:
        return self.db.query(LibraryModelEntity171).offset(skip).limit(limit).all()

    def get_entity_171_by_id(self, entity_id: int) -> Optional[LibraryModelEntity171]:
        return self.db.query(LibraryModelEntity171).filter(LibraryModelEntity171.id == entity_id).first()

    def create_entity_171(self, payload: LibrarySchemaEntity171Create) -> LibraryModelEntity171:
        db_obj = LibraryModelEntity171(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_171(self, entity_id: int, payload: LibrarySchemaEntity171Update) -> Optional[LibraryModelEntity171]:
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

    def get_entity_172_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity172]:
        return self.db.query(LibraryModelEntity172).offset(skip).limit(limit).all()

    def get_entity_172_by_id(self, entity_id: int) -> Optional[LibraryModelEntity172]:
        return self.db.query(LibraryModelEntity172).filter(LibraryModelEntity172.id == entity_id).first()

    def create_entity_172(self, payload: LibrarySchemaEntity172Create) -> LibraryModelEntity172:
        db_obj = LibraryModelEntity172(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_172(self, entity_id: int, payload: LibrarySchemaEntity172Update) -> Optional[LibraryModelEntity172]:
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

    def get_entity_173_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity173]:
        return self.db.query(LibraryModelEntity173).offset(skip).limit(limit).all()

    def get_entity_173_by_id(self, entity_id: int) -> Optional[LibraryModelEntity173]:
        return self.db.query(LibraryModelEntity173).filter(LibraryModelEntity173.id == entity_id).first()

    def create_entity_173(self, payload: LibrarySchemaEntity173Create) -> LibraryModelEntity173:
        db_obj = LibraryModelEntity173(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_173(self, entity_id: int, payload: LibrarySchemaEntity173Update) -> Optional[LibraryModelEntity173]:
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

    def get_entity_174_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity174]:
        return self.db.query(LibraryModelEntity174).offset(skip).limit(limit).all()

    def get_entity_174_by_id(self, entity_id: int) -> Optional[LibraryModelEntity174]:
        return self.db.query(LibraryModelEntity174).filter(LibraryModelEntity174.id == entity_id).first()

    def create_entity_174(self, payload: LibrarySchemaEntity174Create) -> LibraryModelEntity174:
        db_obj = LibraryModelEntity174(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_174(self, entity_id: int, payload: LibrarySchemaEntity174Update) -> Optional[LibraryModelEntity174]:
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

    def get_entity_175_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity175]:
        return self.db.query(LibraryModelEntity175).offset(skip).limit(limit).all()

    def get_entity_175_by_id(self, entity_id: int) -> Optional[LibraryModelEntity175]:
        return self.db.query(LibraryModelEntity175).filter(LibraryModelEntity175.id == entity_id).first()

    def create_entity_175(self, payload: LibrarySchemaEntity175Create) -> LibraryModelEntity175:
        db_obj = LibraryModelEntity175(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_175(self, entity_id: int, payload: LibrarySchemaEntity175Update) -> Optional[LibraryModelEntity175]:
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

    def get_entity_176_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity176]:
        return self.db.query(LibraryModelEntity176).offset(skip).limit(limit).all()

    def get_entity_176_by_id(self, entity_id: int) -> Optional[LibraryModelEntity176]:
        return self.db.query(LibraryModelEntity176).filter(LibraryModelEntity176.id == entity_id).first()

    def create_entity_176(self, payload: LibrarySchemaEntity176Create) -> LibraryModelEntity176:
        db_obj = LibraryModelEntity176(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_176(self, entity_id: int, payload: LibrarySchemaEntity176Update) -> Optional[LibraryModelEntity176]:
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

    def get_entity_177_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity177]:
        return self.db.query(LibraryModelEntity177).offset(skip).limit(limit).all()

    def get_entity_177_by_id(self, entity_id: int) -> Optional[LibraryModelEntity177]:
        return self.db.query(LibraryModelEntity177).filter(LibraryModelEntity177.id == entity_id).first()

    def create_entity_177(self, payload: LibrarySchemaEntity177Create) -> LibraryModelEntity177:
        db_obj = LibraryModelEntity177(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_177(self, entity_id: int, payload: LibrarySchemaEntity177Update) -> Optional[LibraryModelEntity177]:
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

    def get_entity_178_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity178]:
        return self.db.query(LibraryModelEntity178).offset(skip).limit(limit).all()

    def get_entity_178_by_id(self, entity_id: int) -> Optional[LibraryModelEntity178]:
        return self.db.query(LibraryModelEntity178).filter(LibraryModelEntity178.id == entity_id).first()

    def create_entity_178(self, payload: LibrarySchemaEntity178Create) -> LibraryModelEntity178:
        db_obj = LibraryModelEntity178(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_178(self, entity_id: int, payload: LibrarySchemaEntity178Update) -> Optional[LibraryModelEntity178]:
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

    def get_entity_179_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity179]:
        return self.db.query(LibraryModelEntity179).offset(skip).limit(limit).all()

    def get_entity_179_by_id(self, entity_id: int) -> Optional[LibraryModelEntity179]:
        return self.db.query(LibraryModelEntity179).filter(LibraryModelEntity179.id == entity_id).first()

    def create_entity_179(self, payload: LibrarySchemaEntity179Create) -> LibraryModelEntity179:
        db_obj = LibraryModelEntity179(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_179(self, entity_id: int, payload: LibrarySchemaEntity179Update) -> Optional[LibraryModelEntity179]:
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

    def get_entity_180_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity180]:
        return self.db.query(LibraryModelEntity180).offset(skip).limit(limit).all()

    def get_entity_180_by_id(self, entity_id: int) -> Optional[LibraryModelEntity180]:
        return self.db.query(LibraryModelEntity180).filter(LibraryModelEntity180.id == entity_id).first()

    def create_entity_180(self, payload: LibrarySchemaEntity180Create) -> LibraryModelEntity180:
        db_obj = LibraryModelEntity180(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_180(self, entity_id: int, payload: LibrarySchemaEntity180Update) -> Optional[LibraryModelEntity180]:
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

    def get_entity_181_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity181]:
        return self.db.query(LibraryModelEntity181).offset(skip).limit(limit).all()

    def get_entity_181_by_id(self, entity_id: int) -> Optional[LibraryModelEntity181]:
        return self.db.query(LibraryModelEntity181).filter(LibraryModelEntity181.id == entity_id).first()

    def create_entity_181(self, payload: LibrarySchemaEntity181Create) -> LibraryModelEntity181:
        db_obj = LibraryModelEntity181(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_181(self, entity_id: int, payload: LibrarySchemaEntity181Update) -> Optional[LibraryModelEntity181]:
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

    def get_entity_182_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity182]:
        return self.db.query(LibraryModelEntity182).offset(skip).limit(limit).all()

    def get_entity_182_by_id(self, entity_id: int) -> Optional[LibraryModelEntity182]:
        return self.db.query(LibraryModelEntity182).filter(LibraryModelEntity182.id == entity_id).first()

    def create_entity_182(self, payload: LibrarySchemaEntity182Create) -> LibraryModelEntity182:
        db_obj = LibraryModelEntity182(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_182(self, entity_id: int, payload: LibrarySchemaEntity182Update) -> Optional[LibraryModelEntity182]:
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

    def get_entity_183_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity183]:
        return self.db.query(LibraryModelEntity183).offset(skip).limit(limit).all()

    def get_entity_183_by_id(self, entity_id: int) -> Optional[LibraryModelEntity183]:
        return self.db.query(LibraryModelEntity183).filter(LibraryModelEntity183.id == entity_id).first()

    def create_entity_183(self, payload: LibrarySchemaEntity183Create) -> LibraryModelEntity183:
        db_obj = LibraryModelEntity183(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_183(self, entity_id: int, payload: LibrarySchemaEntity183Update) -> Optional[LibraryModelEntity183]:
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

    def get_entity_184_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity184]:
        return self.db.query(LibraryModelEntity184).offset(skip).limit(limit).all()

    def get_entity_184_by_id(self, entity_id: int) -> Optional[LibraryModelEntity184]:
        return self.db.query(LibraryModelEntity184).filter(LibraryModelEntity184.id == entity_id).first()

    def create_entity_184(self, payload: LibrarySchemaEntity184Create) -> LibraryModelEntity184:
        db_obj = LibraryModelEntity184(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_184(self, entity_id: int, payload: LibrarySchemaEntity184Update) -> Optional[LibraryModelEntity184]:
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

    def get_entity_185_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity185]:
        return self.db.query(LibraryModelEntity185).offset(skip).limit(limit).all()

    def get_entity_185_by_id(self, entity_id: int) -> Optional[LibraryModelEntity185]:
        return self.db.query(LibraryModelEntity185).filter(LibraryModelEntity185.id == entity_id).first()

    def create_entity_185(self, payload: LibrarySchemaEntity185Create) -> LibraryModelEntity185:
        db_obj = LibraryModelEntity185(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_185(self, entity_id: int, payload: LibrarySchemaEntity185Update) -> Optional[LibraryModelEntity185]:
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

    def get_entity_186_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity186]:
        return self.db.query(LibraryModelEntity186).offset(skip).limit(limit).all()

    def get_entity_186_by_id(self, entity_id: int) -> Optional[LibraryModelEntity186]:
        return self.db.query(LibraryModelEntity186).filter(LibraryModelEntity186.id == entity_id).first()

    def create_entity_186(self, payload: LibrarySchemaEntity186Create) -> LibraryModelEntity186:
        db_obj = LibraryModelEntity186(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_186(self, entity_id: int, payload: LibrarySchemaEntity186Update) -> Optional[LibraryModelEntity186]:
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

    def get_entity_187_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity187]:
        return self.db.query(LibraryModelEntity187).offset(skip).limit(limit).all()

    def get_entity_187_by_id(self, entity_id: int) -> Optional[LibraryModelEntity187]:
        return self.db.query(LibraryModelEntity187).filter(LibraryModelEntity187.id == entity_id).first()

    def create_entity_187(self, payload: LibrarySchemaEntity187Create) -> LibraryModelEntity187:
        db_obj = LibraryModelEntity187(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_187(self, entity_id: int, payload: LibrarySchemaEntity187Update) -> Optional[LibraryModelEntity187]:
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

    def get_entity_188_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity188]:
        return self.db.query(LibraryModelEntity188).offset(skip).limit(limit).all()

    def get_entity_188_by_id(self, entity_id: int) -> Optional[LibraryModelEntity188]:
        return self.db.query(LibraryModelEntity188).filter(LibraryModelEntity188.id == entity_id).first()

    def create_entity_188(self, payload: LibrarySchemaEntity188Create) -> LibraryModelEntity188:
        db_obj = LibraryModelEntity188(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_188(self, entity_id: int, payload: LibrarySchemaEntity188Update) -> Optional[LibraryModelEntity188]:
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

    def get_entity_189_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity189]:
        return self.db.query(LibraryModelEntity189).offset(skip).limit(limit).all()

    def get_entity_189_by_id(self, entity_id: int) -> Optional[LibraryModelEntity189]:
        return self.db.query(LibraryModelEntity189).filter(LibraryModelEntity189.id == entity_id).first()

    def create_entity_189(self, payload: LibrarySchemaEntity189Create) -> LibraryModelEntity189:
        db_obj = LibraryModelEntity189(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_189(self, entity_id: int, payload: LibrarySchemaEntity189Update) -> Optional[LibraryModelEntity189]:
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

    def get_entity_190_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity190]:
        return self.db.query(LibraryModelEntity190).offset(skip).limit(limit).all()

    def get_entity_190_by_id(self, entity_id: int) -> Optional[LibraryModelEntity190]:
        return self.db.query(LibraryModelEntity190).filter(LibraryModelEntity190.id == entity_id).first()

    def create_entity_190(self, payload: LibrarySchemaEntity190Create) -> LibraryModelEntity190:
        db_obj = LibraryModelEntity190(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_190(self, entity_id: int, payload: LibrarySchemaEntity190Update) -> Optional[LibraryModelEntity190]:
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

    def get_entity_191_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity191]:
        return self.db.query(LibraryModelEntity191).offset(skip).limit(limit).all()

    def get_entity_191_by_id(self, entity_id: int) -> Optional[LibraryModelEntity191]:
        return self.db.query(LibraryModelEntity191).filter(LibraryModelEntity191.id == entity_id).first()

    def create_entity_191(self, payload: LibrarySchemaEntity191Create) -> LibraryModelEntity191:
        db_obj = LibraryModelEntity191(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_191(self, entity_id: int, payload: LibrarySchemaEntity191Update) -> Optional[LibraryModelEntity191]:
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

    def get_entity_192_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity192]:
        return self.db.query(LibraryModelEntity192).offset(skip).limit(limit).all()

    def get_entity_192_by_id(self, entity_id: int) -> Optional[LibraryModelEntity192]:
        return self.db.query(LibraryModelEntity192).filter(LibraryModelEntity192.id == entity_id).first()

    def create_entity_192(self, payload: LibrarySchemaEntity192Create) -> LibraryModelEntity192:
        db_obj = LibraryModelEntity192(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_192(self, entity_id: int, payload: LibrarySchemaEntity192Update) -> Optional[LibraryModelEntity192]:
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

    def get_entity_193_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity193]:
        return self.db.query(LibraryModelEntity193).offset(skip).limit(limit).all()

    def get_entity_193_by_id(self, entity_id: int) -> Optional[LibraryModelEntity193]:
        return self.db.query(LibraryModelEntity193).filter(LibraryModelEntity193.id == entity_id).first()

    def create_entity_193(self, payload: LibrarySchemaEntity193Create) -> LibraryModelEntity193:
        db_obj = LibraryModelEntity193(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_193(self, entity_id: int, payload: LibrarySchemaEntity193Update) -> Optional[LibraryModelEntity193]:
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

    def get_entity_194_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity194]:
        return self.db.query(LibraryModelEntity194).offset(skip).limit(limit).all()

    def get_entity_194_by_id(self, entity_id: int) -> Optional[LibraryModelEntity194]:
        return self.db.query(LibraryModelEntity194).filter(LibraryModelEntity194.id == entity_id).first()

    def create_entity_194(self, payload: LibrarySchemaEntity194Create) -> LibraryModelEntity194:
        db_obj = LibraryModelEntity194(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_194(self, entity_id: int, payload: LibrarySchemaEntity194Update) -> Optional[LibraryModelEntity194]:
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

    def get_entity_195_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity195]:
        return self.db.query(LibraryModelEntity195).offset(skip).limit(limit).all()

    def get_entity_195_by_id(self, entity_id: int) -> Optional[LibraryModelEntity195]:
        return self.db.query(LibraryModelEntity195).filter(LibraryModelEntity195.id == entity_id).first()

    def create_entity_195(self, payload: LibrarySchemaEntity195Create) -> LibraryModelEntity195:
        db_obj = LibraryModelEntity195(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_195(self, entity_id: int, payload: LibrarySchemaEntity195Update) -> Optional[LibraryModelEntity195]:
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

    def get_entity_196_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity196]:
        return self.db.query(LibraryModelEntity196).offset(skip).limit(limit).all()

    def get_entity_196_by_id(self, entity_id: int) -> Optional[LibraryModelEntity196]:
        return self.db.query(LibraryModelEntity196).filter(LibraryModelEntity196.id == entity_id).first()

    def create_entity_196(self, payload: LibrarySchemaEntity196Create) -> LibraryModelEntity196:
        db_obj = LibraryModelEntity196(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_196(self, entity_id: int, payload: LibrarySchemaEntity196Update) -> Optional[LibraryModelEntity196]:
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

    def get_entity_197_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity197]:
        return self.db.query(LibraryModelEntity197).offset(skip).limit(limit).all()

    def get_entity_197_by_id(self, entity_id: int) -> Optional[LibraryModelEntity197]:
        return self.db.query(LibraryModelEntity197).filter(LibraryModelEntity197.id == entity_id).first()

    def create_entity_197(self, payload: LibrarySchemaEntity197Create) -> LibraryModelEntity197:
        db_obj = LibraryModelEntity197(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_197(self, entity_id: int, payload: LibrarySchemaEntity197Update) -> Optional[LibraryModelEntity197]:
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

    def get_entity_198_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity198]:
        return self.db.query(LibraryModelEntity198).offset(skip).limit(limit).all()

    def get_entity_198_by_id(self, entity_id: int) -> Optional[LibraryModelEntity198]:
        return self.db.query(LibraryModelEntity198).filter(LibraryModelEntity198.id == entity_id).first()

    def create_entity_198(self, payload: LibrarySchemaEntity198Create) -> LibraryModelEntity198:
        db_obj = LibraryModelEntity198(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_198(self, entity_id: int, payload: LibrarySchemaEntity198Update) -> Optional[LibraryModelEntity198]:
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

    def get_entity_199_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity199]:
        return self.db.query(LibraryModelEntity199).offset(skip).limit(limit).all()

    def get_entity_199_by_id(self, entity_id: int) -> Optional[LibraryModelEntity199]:
        return self.db.query(LibraryModelEntity199).filter(LibraryModelEntity199.id == entity_id).first()

    def create_entity_199(self, payload: LibrarySchemaEntity199Create) -> LibraryModelEntity199:
        db_obj = LibraryModelEntity199(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_199(self, entity_id: int, payload: LibrarySchemaEntity199Update) -> Optional[LibraryModelEntity199]:
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

    def get_entity_200_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity200]:
        return self.db.query(LibraryModelEntity200).offset(skip).limit(limit).all()

    def get_entity_200_by_id(self, entity_id: int) -> Optional[LibraryModelEntity200]:
        return self.db.query(LibraryModelEntity200).filter(LibraryModelEntity200.id == entity_id).first()

    def create_entity_200(self, payload: LibrarySchemaEntity200Create) -> LibraryModelEntity200:
        db_obj = LibraryModelEntity200(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_200(self, entity_id: int, payload: LibrarySchemaEntity200Update) -> Optional[LibraryModelEntity200]:
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

    def get_entity_201_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity201]:
        return self.db.query(LibraryModelEntity201).offset(skip).limit(limit).all()

    def get_entity_201_by_id(self, entity_id: int) -> Optional[LibraryModelEntity201]:
        return self.db.query(LibraryModelEntity201).filter(LibraryModelEntity201.id == entity_id).first()

    def create_entity_201(self, payload: LibrarySchemaEntity201Create) -> LibraryModelEntity201:
        db_obj = LibraryModelEntity201(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_201(self, entity_id: int, payload: LibrarySchemaEntity201Update) -> Optional[LibraryModelEntity201]:
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

    def get_entity_202_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity202]:
        return self.db.query(LibraryModelEntity202).offset(skip).limit(limit).all()

    def get_entity_202_by_id(self, entity_id: int) -> Optional[LibraryModelEntity202]:
        return self.db.query(LibraryModelEntity202).filter(LibraryModelEntity202.id == entity_id).first()

    def create_entity_202(self, payload: LibrarySchemaEntity202Create) -> LibraryModelEntity202:
        db_obj = LibraryModelEntity202(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_202(self, entity_id: int, payload: LibrarySchemaEntity202Update) -> Optional[LibraryModelEntity202]:
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

    def get_entity_203_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity203]:
        return self.db.query(LibraryModelEntity203).offset(skip).limit(limit).all()

    def get_entity_203_by_id(self, entity_id: int) -> Optional[LibraryModelEntity203]:
        return self.db.query(LibraryModelEntity203).filter(LibraryModelEntity203.id == entity_id).first()

    def create_entity_203(self, payload: LibrarySchemaEntity203Create) -> LibraryModelEntity203:
        db_obj = LibraryModelEntity203(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_203(self, entity_id: int, payload: LibrarySchemaEntity203Update) -> Optional[LibraryModelEntity203]:
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

    def get_entity_204_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity204]:
        return self.db.query(LibraryModelEntity204).offset(skip).limit(limit).all()

    def get_entity_204_by_id(self, entity_id: int) -> Optional[LibraryModelEntity204]:
        return self.db.query(LibraryModelEntity204).filter(LibraryModelEntity204.id == entity_id).first()

    def create_entity_204(self, payload: LibrarySchemaEntity204Create) -> LibraryModelEntity204:
        db_obj = LibraryModelEntity204(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_204(self, entity_id: int, payload: LibrarySchemaEntity204Update) -> Optional[LibraryModelEntity204]:
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

    def get_entity_205_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity205]:
        return self.db.query(LibraryModelEntity205).offset(skip).limit(limit).all()

    def get_entity_205_by_id(self, entity_id: int) -> Optional[LibraryModelEntity205]:
        return self.db.query(LibraryModelEntity205).filter(LibraryModelEntity205.id == entity_id).first()

    def create_entity_205(self, payload: LibrarySchemaEntity205Create) -> LibraryModelEntity205:
        db_obj = LibraryModelEntity205(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_205(self, entity_id: int, payload: LibrarySchemaEntity205Update) -> Optional[LibraryModelEntity205]:
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

    def get_entity_206_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity206]:
        return self.db.query(LibraryModelEntity206).offset(skip).limit(limit).all()

    def get_entity_206_by_id(self, entity_id: int) -> Optional[LibraryModelEntity206]:
        return self.db.query(LibraryModelEntity206).filter(LibraryModelEntity206.id == entity_id).first()

    def create_entity_206(self, payload: LibrarySchemaEntity206Create) -> LibraryModelEntity206:
        db_obj = LibraryModelEntity206(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_206(self, entity_id: int, payload: LibrarySchemaEntity206Update) -> Optional[LibraryModelEntity206]:
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

    def get_entity_207_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity207]:
        return self.db.query(LibraryModelEntity207).offset(skip).limit(limit).all()

    def get_entity_207_by_id(self, entity_id: int) -> Optional[LibraryModelEntity207]:
        return self.db.query(LibraryModelEntity207).filter(LibraryModelEntity207.id == entity_id).first()

    def create_entity_207(self, payload: LibrarySchemaEntity207Create) -> LibraryModelEntity207:
        db_obj = LibraryModelEntity207(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_207(self, entity_id: int, payload: LibrarySchemaEntity207Update) -> Optional[LibraryModelEntity207]:
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

    def get_entity_208_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity208]:
        return self.db.query(LibraryModelEntity208).offset(skip).limit(limit).all()

    def get_entity_208_by_id(self, entity_id: int) -> Optional[LibraryModelEntity208]:
        return self.db.query(LibraryModelEntity208).filter(LibraryModelEntity208.id == entity_id).first()

    def create_entity_208(self, payload: LibrarySchemaEntity208Create) -> LibraryModelEntity208:
        db_obj = LibraryModelEntity208(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_208(self, entity_id: int, payload: LibrarySchemaEntity208Update) -> Optional[LibraryModelEntity208]:
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

    def get_entity_209_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity209]:
        return self.db.query(LibraryModelEntity209).offset(skip).limit(limit).all()

    def get_entity_209_by_id(self, entity_id: int) -> Optional[LibraryModelEntity209]:
        return self.db.query(LibraryModelEntity209).filter(LibraryModelEntity209.id == entity_id).first()

    def create_entity_209(self, payload: LibrarySchemaEntity209Create) -> LibraryModelEntity209:
        db_obj = LibraryModelEntity209(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_209(self, entity_id: int, payload: LibrarySchemaEntity209Update) -> Optional[LibraryModelEntity209]:
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

    def get_entity_210_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity210]:
        return self.db.query(LibraryModelEntity210).offset(skip).limit(limit).all()

    def get_entity_210_by_id(self, entity_id: int) -> Optional[LibraryModelEntity210]:
        return self.db.query(LibraryModelEntity210).filter(LibraryModelEntity210.id == entity_id).first()

    def create_entity_210(self, payload: LibrarySchemaEntity210Create) -> LibraryModelEntity210:
        db_obj = LibraryModelEntity210(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_210(self, entity_id: int, payload: LibrarySchemaEntity210Update) -> Optional[LibraryModelEntity210]:
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

    def get_entity_211_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity211]:
        return self.db.query(LibraryModelEntity211).offset(skip).limit(limit).all()

    def get_entity_211_by_id(self, entity_id: int) -> Optional[LibraryModelEntity211]:
        return self.db.query(LibraryModelEntity211).filter(LibraryModelEntity211.id == entity_id).first()

    def create_entity_211(self, payload: LibrarySchemaEntity211Create) -> LibraryModelEntity211:
        db_obj = LibraryModelEntity211(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_211(self, entity_id: int, payload: LibrarySchemaEntity211Update) -> Optional[LibraryModelEntity211]:
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

    def get_entity_212_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity212]:
        return self.db.query(LibraryModelEntity212).offset(skip).limit(limit).all()

    def get_entity_212_by_id(self, entity_id: int) -> Optional[LibraryModelEntity212]:
        return self.db.query(LibraryModelEntity212).filter(LibraryModelEntity212.id == entity_id).first()

    def create_entity_212(self, payload: LibrarySchemaEntity212Create) -> LibraryModelEntity212:
        db_obj = LibraryModelEntity212(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_212(self, entity_id: int, payload: LibrarySchemaEntity212Update) -> Optional[LibraryModelEntity212]:
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

    def get_entity_213_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity213]:
        return self.db.query(LibraryModelEntity213).offset(skip).limit(limit).all()

    def get_entity_213_by_id(self, entity_id: int) -> Optional[LibraryModelEntity213]:
        return self.db.query(LibraryModelEntity213).filter(LibraryModelEntity213.id == entity_id).first()

    def create_entity_213(self, payload: LibrarySchemaEntity213Create) -> LibraryModelEntity213:
        db_obj = LibraryModelEntity213(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_213(self, entity_id: int, payload: LibrarySchemaEntity213Update) -> Optional[LibraryModelEntity213]:
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

    def get_entity_214_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity214]:
        return self.db.query(LibraryModelEntity214).offset(skip).limit(limit).all()

    def get_entity_214_by_id(self, entity_id: int) -> Optional[LibraryModelEntity214]:
        return self.db.query(LibraryModelEntity214).filter(LibraryModelEntity214.id == entity_id).first()

    def create_entity_214(self, payload: LibrarySchemaEntity214Create) -> LibraryModelEntity214:
        db_obj = LibraryModelEntity214(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_214(self, entity_id: int, payload: LibrarySchemaEntity214Update) -> Optional[LibraryModelEntity214]:
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

    def get_entity_215_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity215]:
        return self.db.query(LibraryModelEntity215).offset(skip).limit(limit).all()

    def get_entity_215_by_id(self, entity_id: int) -> Optional[LibraryModelEntity215]:
        return self.db.query(LibraryModelEntity215).filter(LibraryModelEntity215.id == entity_id).first()

    def create_entity_215(self, payload: LibrarySchemaEntity215Create) -> LibraryModelEntity215:
        db_obj = LibraryModelEntity215(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_215(self, entity_id: int, payload: LibrarySchemaEntity215Update) -> Optional[LibraryModelEntity215]:
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

    def get_entity_216_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity216]:
        return self.db.query(LibraryModelEntity216).offset(skip).limit(limit).all()

    def get_entity_216_by_id(self, entity_id: int) -> Optional[LibraryModelEntity216]:
        return self.db.query(LibraryModelEntity216).filter(LibraryModelEntity216.id == entity_id).first()

    def create_entity_216(self, payload: LibrarySchemaEntity216Create) -> LibraryModelEntity216:
        db_obj = LibraryModelEntity216(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_216(self, entity_id: int, payload: LibrarySchemaEntity216Update) -> Optional[LibraryModelEntity216]:
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

    def get_entity_217_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity217]:
        return self.db.query(LibraryModelEntity217).offset(skip).limit(limit).all()

    def get_entity_217_by_id(self, entity_id: int) -> Optional[LibraryModelEntity217]:
        return self.db.query(LibraryModelEntity217).filter(LibraryModelEntity217.id == entity_id).first()

    def create_entity_217(self, payload: LibrarySchemaEntity217Create) -> LibraryModelEntity217:
        db_obj = LibraryModelEntity217(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_217(self, entity_id: int, payload: LibrarySchemaEntity217Update) -> Optional[LibraryModelEntity217]:
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

    def get_entity_218_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity218]:
        return self.db.query(LibraryModelEntity218).offset(skip).limit(limit).all()

    def get_entity_218_by_id(self, entity_id: int) -> Optional[LibraryModelEntity218]:
        return self.db.query(LibraryModelEntity218).filter(LibraryModelEntity218.id == entity_id).first()

    def create_entity_218(self, payload: LibrarySchemaEntity218Create) -> LibraryModelEntity218:
        db_obj = LibraryModelEntity218(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_218(self, entity_id: int, payload: LibrarySchemaEntity218Update) -> Optional[LibraryModelEntity218]:
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

    def get_entity_219_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity219]:
        return self.db.query(LibraryModelEntity219).offset(skip).limit(limit).all()

    def get_entity_219_by_id(self, entity_id: int) -> Optional[LibraryModelEntity219]:
        return self.db.query(LibraryModelEntity219).filter(LibraryModelEntity219.id == entity_id).first()

    def create_entity_219(self, payload: LibrarySchemaEntity219Create) -> LibraryModelEntity219:
        db_obj = LibraryModelEntity219(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_219(self, entity_id: int, payload: LibrarySchemaEntity219Update) -> Optional[LibraryModelEntity219]:
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

    def get_entity_220_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity220]:
        return self.db.query(LibraryModelEntity220).offset(skip).limit(limit).all()

    def get_entity_220_by_id(self, entity_id: int) -> Optional[LibraryModelEntity220]:
        return self.db.query(LibraryModelEntity220).filter(LibraryModelEntity220.id == entity_id).first()

    def create_entity_220(self, payload: LibrarySchemaEntity220Create) -> LibraryModelEntity220:
        db_obj = LibraryModelEntity220(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_220(self, entity_id: int, payload: LibrarySchemaEntity220Update) -> Optional[LibraryModelEntity220]:
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

    def get_entity_221_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity221]:
        return self.db.query(LibraryModelEntity221).offset(skip).limit(limit).all()

    def get_entity_221_by_id(self, entity_id: int) -> Optional[LibraryModelEntity221]:
        return self.db.query(LibraryModelEntity221).filter(LibraryModelEntity221.id == entity_id).first()

    def create_entity_221(self, payload: LibrarySchemaEntity221Create) -> LibraryModelEntity221:
        db_obj = LibraryModelEntity221(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_221(self, entity_id: int, payload: LibrarySchemaEntity221Update) -> Optional[LibraryModelEntity221]:
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

    def get_entity_222_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity222]:
        return self.db.query(LibraryModelEntity222).offset(skip).limit(limit).all()

    def get_entity_222_by_id(self, entity_id: int) -> Optional[LibraryModelEntity222]:
        return self.db.query(LibraryModelEntity222).filter(LibraryModelEntity222.id == entity_id).first()

    def create_entity_222(self, payload: LibrarySchemaEntity222Create) -> LibraryModelEntity222:
        db_obj = LibraryModelEntity222(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_222(self, entity_id: int, payload: LibrarySchemaEntity222Update) -> Optional[LibraryModelEntity222]:
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

    def get_entity_223_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity223]:
        return self.db.query(LibraryModelEntity223).offset(skip).limit(limit).all()

    def get_entity_223_by_id(self, entity_id: int) -> Optional[LibraryModelEntity223]:
        return self.db.query(LibraryModelEntity223).filter(LibraryModelEntity223.id == entity_id).first()

    def create_entity_223(self, payload: LibrarySchemaEntity223Create) -> LibraryModelEntity223:
        db_obj = LibraryModelEntity223(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_223(self, entity_id: int, payload: LibrarySchemaEntity223Update) -> Optional[LibraryModelEntity223]:
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

    def get_entity_224_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity224]:
        return self.db.query(LibraryModelEntity224).offset(skip).limit(limit).all()

    def get_entity_224_by_id(self, entity_id: int) -> Optional[LibraryModelEntity224]:
        return self.db.query(LibraryModelEntity224).filter(LibraryModelEntity224.id == entity_id).first()

    def create_entity_224(self, payload: LibrarySchemaEntity224Create) -> LibraryModelEntity224:
        db_obj = LibraryModelEntity224(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_224(self, entity_id: int, payload: LibrarySchemaEntity224Update) -> Optional[LibraryModelEntity224]:
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

    def get_entity_225_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity225]:
        return self.db.query(LibraryModelEntity225).offset(skip).limit(limit).all()

    def get_entity_225_by_id(self, entity_id: int) -> Optional[LibraryModelEntity225]:
        return self.db.query(LibraryModelEntity225).filter(LibraryModelEntity225.id == entity_id).first()

    def create_entity_225(self, payload: LibrarySchemaEntity225Create) -> LibraryModelEntity225:
        db_obj = LibraryModelEntity225(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_225(self, entity_id: int, payload: LibrarySchemaEntity225Update) -> Optional[LibraryModelEntity225]:
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

    def get_entity_226_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity226]:
        return self.db.query(LibraryModelEntity226).offset(skip).limit(limit).all()

    def get_entity_226_by_id(self, entity_id: int) -> Optional[LibraryModelEntity226]:
        return self.db.query(LibraryModelEntity226).filter(LibraryModelEntity226.id == entity_id).first()

    def create_entity_226(self, payload: LibrarySchemaEntity226Create) -> LibraryModelEntity226:
        db_obj = LibraryModelEntity226(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_226(self, entity_id: int, payload: LibrarySchemaEntity226Update) -> Optional[LibraryModelEntity226]:
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

    def get_entity_227_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity227]:
        return self.db.query(LibraryModelEntity227).offset(skip).limit(limit).all()

    def get_entity_227_by_id(self, entity_id: int) -> Optional[LibraryModelEntity227]:
        return self.db.query(LibraryModelEntity227).filter(LibraryModelEntity227.id == entity_id).first()

    def create_entity_227(self, payload: LibrarySchemaEntity227Create) -> LibraryModelEntity227:
        db_obj = LibraryModelEntity227(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_227(self, entity_id: int, payload: LibrarySchemaEntity227Update) -> Optional[LibraryModelEntity227]:
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

    def get_entity_228_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity228]:
        return self.db.query(LibraryModelEntity228).offset(skip).limit(limit).all()

    def get_entity_228_by_id(self, entity_id: int) -> Optional[LibraryModelEntity228]:
        return self.db.query(LibraryModelEntity228).filter(LibraryModelEntity228.id == entity_id).first()

    def create_entity_228(self, payload: LibrarySchemaEntity228Create) -> LibraryModelEntity228:
        db_obj = LibraryModelEntity228(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_228(self, entity_id: int, payload: LibrarySchemaEntity228Update) -> Optional[LibraryModelEntity228]:
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

    def get_entity_229_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity229]:
        return self.db.query(LibraryModelEntity229).offset(skip).limit(limit).all()

    def get_entity_229_by_id(self, entity_id: int) -> Optional[LibraryModelEntity229]:
        return self.db.query(LibraryModelEntity229).filter(LibraryModelEntity229.id == entity_id).first()

    def create_entity_229(self, payload: LibrarySchemaEntity229Create) -> LibraryModelEntity229:
        db_obj = LibraryModelEntity229(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_229(self, entity_id: int, payload: LibrarySchemaEntity229Update) -> Optional[LibraryModelEntity229]:
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

    def get_entity_230_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity230]:
        return self.db.query(LibraryModelEntity230).offset(skip).limit(limit).all()

    def get_entity_230_by_id(self, entity_id: int) -> Optional[LibraryModelEntity230]:
        return self.db.query(LibraryModelEntity230).filter(LibraryModelEntity230.id == entity_id).first()

    def create_entity_230(self, payload: LibrarySchemaEntity230Create) -> LibraryModelEntity230:
        db_obj = LibraryModelEntity230(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_230(self, entity_id: int, payload: LibrarySchemaEntity230Update) -> Optional[LibraryModelEntity230]:
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

    def get_entity_231_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity231]:
        return self.db.query(LibraryModelEntity231).offset(skip).limit(limit).all()

    def get_entity_231_by_id(self, entity_id: int) -> Optional[LibraryModelEntity231]:
        return self.db.query(LibraryModelEntity231).filter(LibraryModelEntity231.id == entity_id).first()

    def create_entity_231(self, payload: LibrarySchemaEntity231Create) -> LibraryModelEntity231:
        db_obj = LibraryModelEntity231(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_231(self, entity_id: int, payload: LibrarySchemaEntity231Update) -> Optional[LibraryModelEntity231]:
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

    def get_entity_232_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity232]:
        return self.db.query(LibraryModelEntity232).offset(skip).limit(limit).all()

    def get_entity_232_by_id(self, entity_id: int) -> Optional[LibraryModelEntity232]:
        return self.db.query(LibraryModelEntity232).filter(LibraryModelEntity232.id == entity_id).first()

    def create_entity_232(self, payload: LibrarySchemaEntity232Create) -> LibraryModelEntity232:
        db_obj = LibraryModelEntity232(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_232(self, entity_id: int, payload: LibrarySchemaEntity232Update) -> Optional[LibraryModelEntity232]:
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

    def get_entity_233_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity233]:
        return self.db.query(LibraryModelEntity233).offset(skip).limit(limit).all()

    def get_entity_233_by_id(self, entity_id: int) -> Optional[LibraryModelEntity233]:
        return self.db.query(LibraryModelEntity233).filter(LibraryModelEntity233.id == entity_id).first()

    def create_entity_233(self, payload: LibrarySchemaEntity233Create) -> LibraryModelEntity233:
        db_obj = LibraryModelEntity233(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_233(self, entity_id: int, payload: LibrarySchemaEntity233Update) -> Optional[LibraryModelEntity233]:
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

    def get_entity_234_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity234]:
        return self.db.query(LibraryModelEntity234).offset(skip).limit(limit).all()

    def get_entity_234_by_id(self, entity_id: int) -> Optional[LibraryModelEntity234]:
        return self.db.query(LibraryModelEntity234).filter(LibraryModelEntity234.id == entity_id).first()

    def create_entity_234(self, payload: LibrarySchemaEntity234Create) -> LibraryModelEntity234:
        db_obj = LibraryModelEntity234(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_234(self, entity_id: int, payload: LibrarySchemaEntity234Update) -> Optional[LibraryModelEntity234]:
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

    def get_entity_235_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity235]:
        return self.db.query(LibraryModelEntity235).offset(skip).limit(limit).all()

    def get_entity_235_by_id(self, entity_id: int) -> Optional[LibraryModelEntity235]:
        return self.db.query(LibraryModelEntity235).filter(LibraryModelEntity235.id == entity_id).first()

    def create_entity_235(self, payload: LibrarySchemaEntity235Create) -> LibraryModelEntity235:
        db_obj = LibraryModelEntity235(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_235(self, entity_id: int, payload: LibrarySchemaEntity235Update) -> Optional[LibraryModelEntity235]:
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

    def get_entity_236_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity236]:
        return self.db.query(LibraryModelEntity236).offset(skip).limit(limit).all()

    def get_entity_236_by_id(self, entity_id: int) -> Optional[LibraryModelEntity236]:
        return self.db.query(LibraryModelEntity236).filter(LibraryModelEntity236.id == entity_id).first()

    def create_entity_236(self, payload: LibrarySchemaEntity236Create) -> LibraryModelEntity236:
        db_obj = LibraryModelEntity236(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_236(self, entity_id: int, payload: LibrarySchemaEntity236Update) -> Optional[LibraryModelEntity236]:
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

    def get_entity_237_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity237]:
        return self.db.query(LibraryModelEntity237).offset(skip).limit(limit).all()

    def get_entity_237_by_id(self, entity_id: int) -> Optional[LibraryModelEntity237]:
        return self.db.query(LibraryModelEntity237).filter(LibraryModelEntity237.id == entity_id).first()

    def create_entity_237(self, payload: LibrarySchemaEntity237Create) -> LibraryModelEntity237:
        db_obj = LibraryModelEntity237(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_237(self, entity_id: int, payload: LibrarySchemaEntity237Update) -> Optional[LibraryModelEntity237]:
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

    def get_entity_238_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity238]:
        return self.db.query(LibraryModelEntity238).offset(skip).limit(limit).all()

    def get_entity_238_by_id(self, entity_id: int) -> Optional[LibraryModelEntity238]:
        return self.db.query(LibraryModelEntity238).filter(LibraryModelEntity238.id == entity_id).first()

    def create_entity_238(self, payload: LibrarySchemaEntity238Create) -> LibraryModelEntity238:
        db_obj = LibraryModelEntity238(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_238(self, entity_id: int, payload: LibrarySchemaEntity238Update) -> Optional[LibraryModelEntity238]:
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

    def get_entity_239_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity239]:
        return self.db.query(LibraryModelEntity239).offset(skip).limit(limit).all()

    def get_entity_239_by_id(self, entity_id: int) -> Optional[LibraryModelEntity239]:
        return self.db.query(LibraryModelEntity239).filter(LibraryModelEntity239.id == entity_id).first()

    def create_entity_239(self, payload: LibrarySchemaEntity239Create) -> LibraryModelEntity239:
        db_obj = LibraryModelEntity239(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_239(self, entity_id: int, payload: LibrarySchemaEntity239Update) -> Optional[LibraryModelEntity239]:
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

    def get_entity_240_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity240]:
        return self.db.query(LibraryModelEntity240).offset(skip).limit(limit).all()

    def get_entity_240_by_id(self, entity_id: int) -> Optional[LibraryModelEntity240]:
        return self.db.query(LibraryModelEntity240).filter(LibraryModelEntity240.id == entity_id).first()

    def create_entity_240(self, payload: LibrarySchemaEntity240Create) -> LibraryModelEntity240:
        db_obj = LibraryModelEntity240(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_240(self, entity_id: int, payload: LibrarySchemaEntity240Update) -> Optional[LibraryModelEntity240]:
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

    def get_entity_241_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity241]:
        return self.db.query(LibraryModelEntity241).offset(skip).limit(limit).all()

    def get_entity_241_by_id(self, entity_id: int) -> Optional[LibraryModelEntity241]:
        return self.db.query(LibraryModelEntity241).filter(LibraryModelEntity241.id == entity_id).first()

    def create_entity_241(self, payload: LibrarySchemaEntity241Create) -> LibraryModelEntity241:
        db_obj = LibraryModelEntity241(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_241(self, entity_id: int, payload: LibrarySchemaEntity241Update) -> Optional[LibraryModelEntity241]:
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

    def get_entity_242_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity242]:
        return self.db.query(LibraryModelEntity242).offset(skip).limit(limit).all()

    def get_entity_242_by_id(self, entity_id: int) -> Optional[LibraryModelEntity242]:
        return self.db.query(LibraryModelEntity242).filter(LibraryModelEntity242.id == entity_id).first()

    def create_entity_242(self, payload: LibrarySchemaEntity242Create) -> LibraryModelEntity242:
        db_obj = LibraryModelEntity242(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_242(self, entity_id: int, payload: LibrarySchemaEntity242Update) -> Optional[LibraryModelEntity242]:
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

    def get_entity_243_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity243]:
        return self.db.query(LibraryModelEntity243).offset(skip).limit(limit).all()

    def get_entity_243_by_id(self, entity_id: int) -> Optional[LibraryModelEntity243]:
        return self.db.query(LibraryModelEntity243).filter(LibraryModelEntity243.id == entity_id).first()

    def create_entity_243(self, payload: LibrarySchemaEntity243Create) -> LibraryModelEntity243:
        db_obj = LibraryModelEntity243(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_243(self, entity_id: int, payload: LibrarySchemaEntity243Update) -> Optional[LibraryModelEntity243]:
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

    def get_entity_244_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity244]:
        return self.db.query(LibraryModelEntity244).offset(skip).limit(limit).all()

    def get_entity_244_by_id(self, entity_id: int) -> Optional[LibraryModelEntity244]:
        return self.db.query(LibraryModelEntity244).filter(LibraryModelEntity244.id == entity_id).first()

    def create_entity_244(self, payload: LibrarySchemaEntity244Create) -> LibraryModelEntity244:
        db_obj = LibraryModelEntity244(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_244(self, entity_id: int, payload: LibrarySchemaEntity244Update) -> Optional[LibraryModelEntity244]:
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

    def get_entity_245_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity245]:
        return self.db.query(LibraryModelEntity245).offset(skip).limit(limit).all()

    def get_entity_245_by_id(self, entity_id: int) -> Optional[LibraryModelEntity245]:
        return self.db.query(LibraryModelEntity245).filter(LibraryModelEntity245.id == entity_id).first()

    def create_entity_245(self, payload: LibrarySchemaEntity245Create) -> LibraryModelEntity245:
        db_obj = LibraryModelEntity245(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_245(self, entity_id: int, payload: LibrarySchemaEntity245Update) -> Optional[LibraryModelEntity245]:
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

    def get_entity_246_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity246]:
        return self.db.query(LibraryModelEntity246).offset(skip).limit(limit).all()

    def get_entity_246_by_id(self, entity_id: int) -> Optional[LibraryModelEntity246]:
        return self.db.query(LibraryModelEntity246).filter(LibraryModelEntity246.id == entity_id).first()

    def create_entity_246(self, payload: LibrarySchemaEntity246Create) -> LibraryModelEntity246:
        db_obj = LibraryModelEntity246(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_246(self, entity_id: int, payload: LibrarySchemaEntity246Update) -> Optional[LibraryModelEntity246]:
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

    def get_entity_247_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity247]:
        return self.db.query(LibraryModelEntity247).offset(skip).limit(limit).all()

    def get_entity_247_by_id(self, entity_id: int) -> Optional[LibraryModelEntity247]:
        return self.db.query(LibraryModelEntity247).filter(LibraryModelEntity247.id == entity_id).first()

    def create_entity_247(self, payload: LibrarySchemaEntity247Create) -> LibraryModelEntity247:
        db_obj = LibraryModelEntity247(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_247(self, entity_id: int, payload: LibrarySchemaEntity247Update) -> Optional[LibraryModelEntity247]:
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

    def get_entity_248_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity248]:
        return self.db.query(LibraryModelEntity248).offset(skip).limit(limit).all()

    def get_entity_248_by_id(self, entity_id: int) -> Optional[LibraryModelEntity248]:
        return self.db.query(LibraryModelEntity248).filter(LibraryModelEntity248.id == entity_id).first()

    def create_entity_248(self, payload: LibrarySchemaEntity248Create) -> LibraryModelEntity248:
        db_obj = LibraryModelEntity248(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_248(self, entity_id: int, payload: LibrarySchemaEntity248Update) -> Optional[LibraryModelEntity248]:
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

    def get_entity_249_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity249]:
        return self.db.query(LibraryModelEntity249).offset(skip).limit(limit).all()

    def get_entity_249_by_id(self, entity_id: int) -> Optional[LibraryModelEntity249]:
        return self.db.query(LibraryModelEntity249).filter(LibraryModelEntity249.id == entity_id).first()

    def create_entity_249(self, payload: LibrarySchemaEntity249Create) -> LibraryModelEntity249:
        db_obj = LibraryModelEntity249(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_249(self, entity_id: int, payload: LibrarySchemaEntity249Update) -> Optional[LibraryModelEntity249]:
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

    def get_entity_250_list(self, skip: int = 0, limit: int = 100) -> List[LibraryModelEntity250]:
        return self.db.query(LibraryModelEntity250).offset(skip).limit(limit).all()

    def get_entity_250_by_id(self, entity_id: int) -> Optional[LibraryModelEntity250]:
        return self.db.query(LibraryModelEntity250).filter(LibraryModelEntity250.id == entity_id).first()

    def create_entity_250(self, payload: LibrarySchemaEntity250Create) -> LibraryModelEntity250:
        db_obj = LibraryModelEntity250(
            entity_code=payload.entity_code,
            name=payload.name,
            category=payload.category,
            description=payload.description,
            value_amount=payload.value_amount,
            is_active=payload.is_active,
            attributes_json=payload.attributes_json or {}
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update_entity_250(self, entity_id: int, payload: LibrarySchemaEntity250Update) -> Optional[LibraryModelEntity250]:
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

