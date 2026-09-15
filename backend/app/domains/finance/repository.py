"""
Finance, Billing & Payroll - Data Access Repository Layer
Module: app.domains.finance.repository
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domains.finance.models import *

class FinanceRepository1:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity1]:
        return self.db.query(FinanceModelEntity1).filter(FinanceModelEntity1.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity1]:
        return self.db.query(FinanceModelEntity1).filter(FinanceModelEntity1.entity_code == code).first()

class FinanceRepository2:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity2]:
        return self.db.query(FinanceModelEntity2).filter(FinanceModelEntity2.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity2]:
        return self.db.query(FinanceModelEntity2).filter(FinanceModelEntity2.entity_code == code).first()

class FinanceRepository3:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity3]:
        return self.db.query(FinanceModelEntity3).filter(FinanceModelEntity3.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity3]:
        return self.db.query(FinanceModelEntity3).filter(FinanceModelEntity3.entity_code == code).first()

class FinanceRepository4:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity4]:
        return self.db.query(FinanceModelEntity4).filter(FinanceModelEntity4.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity4]:
        return self.db.query(FinanceModelEntity4).filter(FinanceModelEntity4.entity_code == code).first()

class FinanceRepository5:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity5]:
        return self.db.query(FinanceModelEntity5).filter(FinanceModelEntity5.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity5]:
        return self.db.query(FinanceModelEntity5).filter(FinanceModelEntity5.entity_code == code).first()

class FinanceRepository6:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity6]:
        return self.db.query(FinanceModelEntity6).filter(FinanceModelEntity6.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity6]:
        return self.db.query(FinanceModelEntity6).filter(FinanceModelEntity6.entity_code == code).first()

class FinanceRepository7:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity7]:
        return self.db.query(FinanceModelEntity7).filter(FinanceModelEntity7.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity7]:
        return self.db.query(FinanceModelEntity7).filter(FinanceModelEntity7.entity_code == code).first()

class FinanceRepository8:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity8]:
        return self.db.query(FinanceModelEntity8).filter(FinanceModelEntity8.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity8]:
        return self.db.query(FinanceModelEntity8).filter(FinanceModelEntity8.entity_code == code).first()

class FinanceRepository9:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity9]:
        return self.db.query(FinanceModelEntity9).filter(FinanceModelEntity9.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity9]:
        return self.db.query(FinanceModelEntity9).filter(FinanceModelEntity9.entity_code == code).first()

class FinanceRepository10:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity10]:
        return self.db.query(FinanceModelEntity10).filter(FinanceModelEntity10.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity10]:
        return self.db.query(FinanceModelEntity10).filter(FinanceModelEntity10.entity_code == code).first()

class FinanceRepository11:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity11]:
        return self.db.query(FinanceModelEntity11).filter(FinanceModelEntity11.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity11]:
        return self.db.query(FinanceModelEntity11).filter(FinanceModelEntity11.entity_code == code).first()

class FinanceRepository12:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity12]:
        return self.db.query(FinanceModelEntity12).filter(FinanceModelEntity12.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity12]:
        return self.db.query(FinanceModelEntity12).filter(FinanceModelEntity12.entity_code == code).first()

class FinanceRepository13:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity13]:
        return self.db.query(FinanceModelEntity13).filter(FinanceModelEntity13.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity13]:
        return self.db.query(FinanceModelEntity13).filter(FinanceModelEntity13.entity_code == code).first()

class FinanceRepository14:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity14]:
        return self.db.query(FinanceModelEntity14).filter(FinanceModelEntity14.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity14]:
        return self.db.query(FinanceModelEntity14).filter(FinanceModelEntity14.entity_code == code).first()

class FinanceRepository15:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity15]:
        return self.db.query(FinanceModelEntity15).filter(FinanceModelEntity15.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity15]:
        return self.db.query(FinanceModelEntity15).filter(FinanceModelEntity15.entity_code == code).first()

class FinanceRepository16:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity16]:
        return self.db.query(FinanceModelEntity16).filter(FinanceModelEntity16.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity16]:
        return self.db.query(FinanceModelEntity16).filter(FinanceModelEntity16.entity_code == code).first()

class FinanceRepository17:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity17]:
        return self.db.query(FinanceModelEntity17).filter(FinanceModelEntity17.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity17]:
        return self.db.query(FinanceModelEntity17).filter(FinanceModelEntity17.entity_code == code).first()

class FinanceRepository18:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity18]:
        return self.db.query(FinanceModelEntity18).filter(FinanceModelEntity18.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity18]:
        return self.db.query(FinanceModelEntity18).filter(FinanceModelEntity18.entity_code == code).first()

class FinanceRepository19:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity19]:
        return self.db.query(FinanceModelEntity19).filter(FinanceModelEntity19.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity19]:
        return self.db.query(FinanceModelEntity19).filter(FinanceModelEntity19.entity_code == code).first()

class FinanceRepository20:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity20]:
        return self.db.query(FinanceModelEntity20).filter(FinanceModelEntity20.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity20]:
        return self.db.query(FinanceModelEntity20).filter(FinanceModelEntity20.entity_code == code).first()

class FinanceRepository21:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity21]:
        return self.db.query(FinanceModelEntity21).filter(FinanceModelEntity21.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity21]:
        return self.db.query(FinanceModelEntity21).filter(FinanceModelEntity21.entity_code == code).first()

class FinanceRepository22:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity22]:
        return self.db.query(FinanceModelEntity22).filter(FinanceModelEntity22.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity22]:
        return self.db.query(FinanceModelEntity22).filter(FinanceModelEntity22.entity_code == code).first()

class FinanceRepository23:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity23]:
        return self.db.query(FinanceModelEntity23).filter(FinanceModelEntity23.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity23]:
        return self.db.query(FinanceModelEntity23).filter(FinanceModelEntity23.entity_code == code).first()

class FinanceRepository24:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity24]:
        return self.db.query(FinanceModelEntity24).filter(FinanceModelEntity24.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity24]:
        return self.db.query(FinanceModelEntity24).filter(FinanceModelEntity24.entity_code == code).first()

class FinanceRepository25:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity25]:
        return self.db.query(FinanceModelEntity25).filter(FinanceModelEntity25.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity25]:
        return self.db.query(FinanceModelEntity25).filter(FinanceModelEntity25.entity_code == code).first()

class FinanceRepository26:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity26]:
        return self.db.query(FinanceModelEntity26).filter(FinanceModelEntity26.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity26]:
        return self.db.query(FinanceModelEntity26).filter(FinanceModelEntity26.entity_code == code).first()

class FinanceRepository27:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity27]:
        return self.db.query(FinanceModelEntity27).filter(FinanceModelEntity27.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity27]:
        return self.db.query(FinanceModelEntity27).filter(FinanceModelEntity27.entity_code == code).first()

class FinanceRepository28:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity28]:
        return self.db.query(FinanceModelEntity28).filter(FinanceModelEntity28.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity28]:
        return self.db.query(FinanceModelEntity28).filter(FinanceModelEntity28.entity_code == code).first()

class FinanceRepository29:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity29]:
        return self.db.query(FinanceModelEntity29).filter(FinanceModelEntity29.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity29]:
        return self.db.query(FinanceModelEntity29).filter(FinanceModelEntity29.entity_code == code).first()

class FinanceRepository30:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity30]:
        return self.db.query(FinanceModelEntity30).filter(FinanceModelEntity30.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity30]:
        return self.db.query(FinanceModelEntity30).filter(FinanceModelEntity30.entity_code == code).first()

class FinanceRepository31:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity31]:
        return self.db.query(FinanceModelEntity31).filter(FinanceModelEntity31.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity31]:
        return self.db.query(FinanceModelEntity31).filter(FinanceModelEntity31.entity_code == code).first()

class FinanceRepository32:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity32]:
        return self.db.query(FinanceModelEntity32).filter(FinanceModelEntity32.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity32]:
        return self.db.query(FinanceModelEntity32).filter(FinanceModelEntity32.entity_code == code).first()

class FinanceRepository33:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity33]:
        return self.db.query(FinanceModelEntity33).filter(FinanceModelEntity33.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity33]:
        return self.db.query(FinanceModelEntity33).filter(FinanceModelEntity33.entity_code == code).first()

class FinanceRepository34:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity34]:
        return self.db.query(FinanceModelEntity34).filter(FinanceModelEntity34.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity34]:
        return self.db.query(FinanceModelEntity34).filter(FinanceModelEntity34.entity_code == code).first()

class FinanceRepository35:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity35]:
        return self.db.query(FinanceModelEntity35).filter(FinanceModelEntity35.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity35]:
        return self.db.query(FinanceModelEntity35).filter(FinanceModelEntity35.entity_code == code).first()

class FinanceRepository36:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity36]:
        return self.db.query(FinanceModelEntity36).filter(FinanceModelEntity36.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity36]:
        return self.db.query(FinanceModelEntity36).filter(FinanceModelEntity36.entity_code == code).first()

class FinanceRepository37:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity37]:
        return self.db.query(FinanceModelEntity37).filter(FinanceModelEntity37.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity37]:
        return self.db.query(FinanceModelEntity37).filter(FinanceModelEntity37.entity_code == code).first()

class FinanceRepository38:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity38]:
        return self.db.query(FinanceModelEntity38).filter(FinanceModelEntity38.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity38]:
        return self.db.query(FinanceModelEntity38).filter(FinanceModelEntity38.entity_code == code).first()

class FinanceRepository39:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity39]:
        return self.db.query(FinanceModelEntity39).filter(FinanceModelEntity39.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity39]:
        return self.db.query(FinanceModelEntity39).filter(FinanceModelEntity39.entity_code == code).first()

class FinanceRepository40:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity40]:
        return self.db.query(FinanceModelEntity40).filter(FinanceModelEntity40.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity40]:
        return self.db.query(FinanceModelEntity40).filter(FinanceModelEntity40.entity_code == code).first()

class FinanceRepository41:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity41]:
        return self.db.query(FinanceModelEntity41).filter(FinanceModelEntity41.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity41]:
        return self.db.query(FinanceModelEntity41).filter(FinanceModelEntity41.entity_code == code).first()

class FinanceRepository42:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity42]:
        return self.db.query(FinanceModelEntity42).filter(FinanceModelEntity42.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity42]:
        return self.db.query(FinanceModelEntity42).filter(FinanceModelEntity42.entity_code == code).first()

class FinanceRepository43:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity43]:
        return self.db.query(FinanceModelEntity43).filter(FinanceModelEntity43.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity43]:
        return self.db.query(FinanceModelEntity43).filter(FinanceModelEntity43.entity_code == code).first()

class FinanceRepository44:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity44]:
        return self.db.query(FinanceModelEntity44).filter(FinanceModelEntity44.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity44]:
        return self.db.query(FinanceModelEntity44).filter(FinanceModelEntity44.entity_code == code).first()

class FinanceRepository45:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity45]:
        return self.db.query(FinanceModelEntity45).filter(FinanceModelEntity45.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity45]:
        return self.db.query(FinanceModelEntity45).filter(FinanceModelEntity45.entity_code == code).first()

class FinanceRepository46:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity46]:
        return self.db.query(FinanceModelEntity46).filter(FinanceModelEntity46.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity46]:
        return self.db.query(FinanceModelEntity46).filter(FinanceModelEntity46.entity_code == code).first()

class FinanceRepository47:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity47]:
        return self.db.query(FinanceModelEntity47).filter(FinanceModelEntity47.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity47]:
        return self.db.query(FinanceModelEntity47).filter(FinanceModelEntity47.entity_code == code).first()

class FinanceRepository48:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity48]:
        return self.db.query(FinanceModelEntity48).filter(FinanceModelEntity48.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity48]:
        return self.db.query(FinanceModelEntity48).filter(FinanceModelEntity48.entity_code == code).first()

class FinanceRepository49:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity49]:
        return self.db.query(FinanceModelEntity49).filter(FinanceModelEntity49.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity49]:
        return self.db.query(FinanceModelEntity49).filter(FinanceModelEntity49.entity_code == code).first()

class FinanceRepository50:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity50]:
        return self.db.query(FinanceModelEntity50).filter(FinanceModelEntity50.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity50]:
        return self.db.query(FinanceModelEntity50).filter(FinanceModelEntity50.entity_code == code).first()

class FinanceRepository51:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity51]:
        return self.db.query(FinanceModelEntity51).filter(FinanceModelEntity51.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity51]:
        return self.db.query(FinanceModelEntity51).filter(FinanceModelEntity51.entity_code == code).first()

class FinanceRepository52:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity52]:
        return self.db.query(FinanceModelEntity52).filter(FinanceModelEntity52.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity52]:
        return self.db.query(FinanceModelEntity52).filter(FinanceModelEntity52.entity_code == code).first()

class FinanceRepository53:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity53]:
        return self.db.query(FinanceModelEntity53).filter(FinanceModelEntity53.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity53]:
        return self.db.query(FinanceModelEntity53).filter(FinanceModelEntity53.entity_code == code).first()

class FinanceRepository54:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity54]:
        return self.db.query(FinanceModelEntity54).filter(FinanceModelEntity54.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity54]:
        return self.db.query(FinanceModelEntity54).filter(FinanceModelEntity54.entity_code == code).first()

class FinanceRepository55:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity55]:
        return self.db.query(FinanceModelEntity55).filter(FinanceModelEntity55.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity55]:
        return self.db.query(FinanceModelEntity55).filter(FinanceModelEntity55.entity_code == code).first()

class FinanceRepository56:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity56]:
        return self.db.query(FinanceModelEntity56).filter(FinanceModelEntity56.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity56]:
        return self.db.query(FinanceModelEntity56).filter(FinanceModelEntity56.entity_code == code).first()

class FinanceRepository57:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity57]:
        return self.db.query(FinanceModelEntity57).filter(FinanceModelEntity57.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity57]:
        return self.db.query(FinanceModelEntity57).filter(FinanceModelEntity57.entity_code == code).first()

class FinanceRepository58:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity58]:
        return self.db.query(FinanceModelEntity58).filter(FinanceModelEntity58.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity58]:
        return self.db.query(FinanceModelEntity58).filter(FinanceModelEntity58.entity_code == code).first()

class FinanceRepository59:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity59]:
        return self.db.query(FinanceModelEntity59).filter(FinanceModelEntity59.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity59]:
        return self.db.query(FinanceModelEntity59).filter(FinanceModelEntity59.entity_code == code).first()

class FinanceRepository60:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity60]:
        return self.db.query(FinanceModelEntity60).filter(FinanceModelEntity60.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity60]:
        return self.db.query(FinanceModelEntity60).filter(FinanceModelEntity60.entity_code == code).first()

class FinanceRepository61:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity61]:
        return self.db.query(FinanceModelEntity61).filter(FinanceModelEntity61.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity61]:
        return self.db.query(FinanceModelEntity61).filter(FinanceModelEntity61.entity_code == code).first()

class FinanceRepository62:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity62]:
        return self.db.query(FinanceModelEntity62).filter(FinanceModelEntity62.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity62]:
        return self.db.query(FinanceModelEntity62).filter(FinanceModelEntity62.entity_code == code).first()

class FinanceRepository63:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity63]:
        return self.db.query(FinanceModelEntity63).filter(FinanceModelEntity63.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity63]:
        return self.db.query(FinanceModelEntity63).filter(FinanceModelEntity63.entity_code == code).first()

class FinanceRepository64:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity64]:
        return self.db.query(FinanceModelEntity64).filter(FinanceModelEntity64.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity64]:
        return self.db.query(FinanceModelEntity64).filter(FinanceModelEntity64.entity_code == code).first()

class FinanceRepository65:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity65]:
        return self.db.query(FinanceModelEntity65).filter(FinanceModelEntity65.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity65]:
        return self.db.query(FinanceModelEntity65).filter(FinanceModelEntity65.entity_code == code).first()

class FinanceRepository66:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity66]:
        return self.db.query(FinanceModelEntity66).filter(FinanceModelEntity66.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity66]:
        return self.db.query(FinanceModelEntity66).filter(FinanceModelEntity66.entity_code == code).first()

class FinanceRepository67:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity67]:
        return self.db.query(FinanceModelEntity67).filter(FinanceModelEntity67.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity67]:
        return self.db.query(FinanceModelEntity67).filter(FinanceModelEntity67.entity_code == code).first()

class FinanceRepository68:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity68]:
        return self.db.query(FinanceModelEntity68).filter(FinanceModelEntity68.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity68]:
        return self.db.query(FinanceModelEntity68).filter(FinanceModelEntity68.entity_code == code).first()

class FinanceRepository69:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity69]:
        return self.db.query(FinanceModelEntity69).filter(FinanceModelEntity69.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity69]:
        return self.db.query(FinanceModelEntity69).filter(FinanceModelEntity69.entity_code == code).first()

class FinanceRepository70:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity70]:
        return self.db.query(FinanceModelEntity70).filter(FinanceModelEntity70.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity70]:
        return self.db.query(FinanceModelEntity70).filter(FinanceModelEntity70.entity_code == code).first()

class FinanceRepository71:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity71]:
        return self.db.query(FinanceModelEntity71).filter(FinanceModelEntity71.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity71]:
        return self.db.query(FinanceModelEntity71).filter(FinanceModelEntity71.entity_code == code).first()

class FinanceRepository72:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity72]:
        return self.db.query(FinanceModelEntity72).filter(FinanceModelEntity72.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity72]:
        return self.db.query(FinanceModelEntity72).filter(FinanceModelEntity72.entity_code == code).first()

class FinanceRepository73:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity73]:
        return self.db.query(FinanceModelEntity73).filter(FinanceModelEntity73.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity73]:
        return self.db.query(FinanceModelEntity73).filter(FinanceModelEntity73.entity_code == code).first()

class FinanceRepository74:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity74]:
        return self.db.query(FinanceModelEntity74).filter(FinanceModelEntity74.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity74]:
        return self.db.query(FinanceModelEntity74).filter(FinanceModelEntity74.entity_code == code).first()

class FinanceRepository75:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity75]:
        return self.db.query(FinanceModelEntity75).filter(FinanceModelEntity75.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity75]:
        return self.db.query(FinanceModelEntity75).filter(FinanceModelEntity75.entity_code == code).first()

class FinanceRepository76:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity76]:
        return self.db.query(FinanceModelEntity76).filter(FinanceModelEntity76.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity76]:
        return self.db.query(FinanceModelEntity76).filter(FinanceModelEntity76.entity_code == code).first()

class FinanceRepository77:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity77]:
        return self.db.query(FinanceModelEntity77).filter(FinanceModelEntity77.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity77]:
        return self.db.query(FinanceModelEntity77).filter(FinanceModelEntity77.entity_code == code).first()

class FinanceRepository78:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity78]:
        return self.db.query(FinanceModelEntity78).filter(FinanceModelEntity78.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity78]:
        return self.db.query(FinanceModelEntity78).filter(FinanceModelEntity78.entity_code == code).first()

class FinanceRepository79:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity79]:
        return self.db.query(FinanceModelEntity79).filter(FinanceModelEntity79.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity79]:
        return self.db.query(FinanceModelEntity79).filter(FinanceModelEntity79.entity_code == code).first()

class FinanceRepository80:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity80]:
        return self.db.query(FinanceModelEntity80).filter(FinanceModelEntity80.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity80]:
        return self.db.query(FinanceModelEntity80).filter(FinanceModelEntity80.entity_code == code).first()

class FinanceRepository81:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity81]:
        return self.db.query(FinanceModelEntity81).filter(FinanceModelEntity81.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity81]:
        return self.db.query(FinanceModelEntity81).filter(FinanceModelEntity81.entity_code == code).first()

class FinanceRepository82:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity82]:
        return self.db.query(FinanceModelEntity82).filter(FinanceModelEntity82.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity82]:
        return self.db.query(FinanceModelEntity82).filter(FinanceModelEntity82.entity_code == code).first()

class FinanceRepository83:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity83]:
        return self.db.query(FinanceModelEntity83).filter(FinanceModelEntity83.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity83]:
        return self.db.query(FinanceModelEntity83).filter(FinanceModelEntity83.entity_code == code).first()

class FinanceRepository84:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity84]:
        return self.db.query(FinanceModelEntity84).filter(FinanceModelEntity84.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity84]:
        return self.db.query(FinanceModelEntity84).filter(FinanceModelEntity84.entity_code == code).first()

class FinanceRepository85:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity85]:
        return self.db.query(FinanceModelEntity85).filter(FinanceModelEntity85.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity85]:
        return self.db.query(FinanceModelEntity85).filter(FinanceModelEntity85.entity_code == code).first()

class FinanceRepository86:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity86]:
        return self.db.query(FinanceModelEntity86).filter(FinanceModelEntity86.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity86]:
        return self.db.query(FinanceModelEntity86).filter(FinanceModelEntity86.entity_code == code).first()

class FinanceRepository87:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity87]:
        return self.db.query(FinanceModelEntity87).filter(FinanceModelEntity87.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity87]:
        return self.db.query(FinanceModelEntity87).filter(FinanceModelEntity87.entity_code == code).first()

class FinanceRepository88:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity88]:
        return self.db.query(FinanceModelEntity88).filter(FinanceModelEntity88.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity88]:
        return self.db.query(FinanceModelEntity88).filter(FinanceModelEntity88.entity_code == code).first()

class FinanceRepository89:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity89]:
        return self.db.query(FinanceModelEntity89).filter(FinanceModelEntity89.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity89]:
        return self.db.query(FinanceModelEntity89).filter(FinanceModelEntity89.entity_code == code).first()

class FinanceRepository90:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity90]:
        return self.db.query(FinanceModelEntity90).filter(FinanceModelEntity90.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity90]:
        return self.db.query(FinanceModelEntity90).filter(FinanceModelEntity90.entity_code == code).first()

class FinanceRepository91:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity91]:
        return self.db.query(FinanceModelEntity91).filter(FinanceModelEntity91.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity91]:
        return self.db.query(FinanceModelEntity91).filter(FinanceModelEntity91.entity_code == code).first()

class FinanceRepository92:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity92]:
        return self.db.query(FinanceModelEntity92).filter(FinanceModelEntity92.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity92]:
        return self.db.query(FinanceModelEntity92).filter(FinanceModelEntity92.entity_code == code).first()

class FinanceRepository93:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity93]:
        return self.db.query(FinanceModelEntity93).filter(FinanceModelEntity93.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity93]:
        return self.db.query(FinanceModelEntity93).filter(FinanceModelEntity93.entity_code == code).first()

class FinanceRepository94:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity94]:
        return self.db.query(FinanceModelEntity94).filter(FinanceModelEntity94.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity94]:
        return self.db.query(FinanceModelEntity94).filter(FinanceModelEntity94.entity_code == code).first()

class FinanceRepository95:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity95]:
        return self.db.query(FinanceModelEntity95).filter(FinanceModelEntity95.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity95]:
        return self.db.query(FinanceModelEntity95).filter(FinanceModelEntity95.entity_code == code).first()

class FinanceRepository96:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity96]:
        return self.db.query(FinanceModelEntity96).filter(FinanceModelEntity96.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity96]:
        return self.db.query(FinanceModelEntity96).filter(FinanceModelEntity96.entity_code == code).first()

class FinanceRepository97:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity97]:
        return self.db.query(FinanceModelEntity97).filter(FinanceModelEntity97.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity97]:
        return self.db.query(FinanceModelEntity97).filter(FinanceModelEntity97.entity_code == code).first()

class FinanceRepository98:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity98]:
        return self.db.query(FinanceModelEntity98).filter(FinanceModelEntity98.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity98]:
        return self.db.query(FinanceModelEntity98).filter(FinanceModelEntity98.entity_code == code).first()

class FinanceRepository99:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity99]:
        return self.db.query(FinanceModelEntity99).filter(FinanceModelEntity99.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity99]:
        return self.db.query(FinanceModelEntity99).filter(FinanceModelEntity99.entity_code == code).first()

class FinanceRepository100:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity100]:
        return self.db.query(FinanceModelEntity100).filter(FinanceModelEntity100.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity100]:
        return self.db.query(FinanceModelEntity100).filter(FinanceModelEntity100.entity_code == code).first()

class FinanceRepository101:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity101]:
        return self.db.query(FinanceModelEntity101).filter(FinanceModelEntity101.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity101]:
        return self.db.query(FinanceModelEntity101).filter(FinanceModelEntity101.entity_code == code).first()

class FinanceRepository102:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity102]:
        return self.db.query(FinanceModelEntity102).filter(FinanceModelEntity102.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity102]:
        return self.db.query(FinanceModelEntity102).filter(FinanceModelEntity102.entity_code == code).first()

class FinanceRepository103:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity103]:
        return self.db.query(FinanceModelEntity103).filter(FinanceModelEntity103.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity103]:
        return self.db.query(FinanceModelEntity103).filter(FinanceModelEntity103.entity_code == code).first()

class FinanceRepository104:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity104]:
        return self.db.query(FinanceModelEntity104).filter(FinanceModelEntity104.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity104]:
        return self.db.query(FinanceModelEntity104).filter(FinanceModelEntity104.entity_code == code).first()

class FinanceRepository105:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity105]:
        return self.db.query(FinanceModelEntity105).filter(FinanceModelEntity105.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity105]:
        return self.db.query(FinanceModelEntity105).filter(FinanceModelEntity105.entity_code == code).first()

class FinanceRepository106:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity106]:
        return self.db.query(FinanceModelEntity106).filter(FinanceModelEntity106.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity106]:
        return self.db.query(FinanceModelEntity106).filter(FinanceModelEntity106.entity_code == code).first()

class FinanceRepository107:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity107]:
        return self.db.query(FinanceModelEntity107).filter(FinanceModelEntity107.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity107]:
        return self.db.query(FinanceModelEntity107).filter(FinanceModelEntity107.entity_code == code).first()

class FinanceRepository108:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity108]:
        return self.db.query(FinanceModelEntity108).filter(FinanceModelEntity108.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity108]:
        return self.db.query(FinanceModelEntity108).filter(FinanceModelEntity108.entity_code == code).first()

class FinanceRepository109:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity109]:
        return self.db.query(FinanceModelEntity109).filter(FinanceModelEntity109.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity109]:
        return self.db.query(FinanceModelEntity109).filter(FinanceModelEntity109.entity_code == code).first()

class FinanceRepository110:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity110]:
        return self.db.query(FinanceModelEntity110).filter(FinanceModelEntity110.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity110]:
        return self.db.query(FinanceModelEntity110).filter(FinanceModelEntity110.entity_code == code).first()

class FinanceRepository111:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity111]:
        return self.db.query(FinanceModelEntity111).filter(FinanceModelEntity111.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity111]:
        return self.db.query(FinanceModelEntity111).filter(FinanceModelEntity111.entity_code == code).first()

class FinanceRepository112:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity112]:
        return self.db.query(FinanceModelEntity112).filter(FinanceModelEntity112.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity112]:
        return self.db.query(FinanceModelEntity112).filter(FinanceModelEntity112.entity_code == code).first()

class FinanceRepository113:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity113]:
        return self.db.query(FinanceModelEntity113).filter(FinanceModelEntity113.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity113]:
        return self.db.query(FinanceModelEntity113).filter(FinanceModelEntity113.entity_code == code).first()

class FinanceRepository114:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity114]:
        return self.db.query(FinanceModelEntity114).filter(FinanceModelEntity114.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity114]:
        return self.db.query(FinanceModelEntity114).filter(FinanceModelEntity114.entity_code == code).first()

class FinanceRepository115:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity115]:
        return self.db.query(FinanceModelEntity115).filter(FinanceModelEntity115.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity115]:
        return self.db.query(FinanceModelEntity115).filter(FinanceModelEntity115.entity_code == code).first()

class FinanceRepository116:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity116]:
        return self.db.query(FinanceModelEntity116).filter(FinanceModelEntity116.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity116]:
        return self.db.query(FinanceModelEntity116).filter(FinanceModelEntity116.entity_code == code).first()

class FinanceRepository117:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity117]:
        return self.db.query(FinanceModelEntity117).filter(FinanceModelEntity117.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity117]:
        return self.db.query(FinanceModelEntity117).filter(FinanceModelEntity117.entity_code == code).first()

class FinanceRepository118:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity118]:
        return self.db.query(FinanceModelEntity118).filter(FinanceModelEntity118.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity118]:
        return self.db.query(FinanceModelEntity118).filter(FinanceModelEntity118.entity_code == code).first()

class FinanceRepository119:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity119]:
        return self.db.query(FinanceModelEntity119).filter(FinanceModelEntity119.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity119]:
        return self.db.query(FinanceModelEntity119).filter(FinanceModelEntity119.entity_code == code).first()

class FinanceRepository120:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[FinanceModelEntity120]:
        return self.db.query(FinanceModelEntity120).filter(FinanceModelEntity120.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[FinanceModelEntity120]:
        return self.db.query(FinanceModelEntity120).filter(FinanceModelEntity120.entity_code == code).first()

