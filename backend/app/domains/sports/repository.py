"""
Sports & Extracurricular Activities - Data Access Repository Layer
Module: app.domains.sports.repository
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domains.sports.models import *

class SportsRepository1:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity1]:
        return self.db.query(SportsModelEntity1).filter(SportsModelEntity1.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity1]:
        return self.db.query(SportsModelEntity1).filter(SportsModelEntity1.entity_code == code).first()

class SportsRepository2:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity2]:
        return self.db.query(SportsModelEntity2).filter(SportsModelEntity2.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity2]:
        return self.db.query(SportsModelEntity2).filter(SportsModelEntity2.entity_code == code).first()

class SportsRepository3:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity3]:
        return self.db.query(SportsModelEntity3).filter(SportsModelEntity3.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity3]:
        return self.db.query(SportsModelEntity3).filter(SportsModelEntity3.entity_code == code).first()

class SportsRepository4:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity4]:
        return self.db.query(SportsModelEntity4).filter(SportsModelEntity4.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity4]:
        return self.db.query(SportsModelEntity4).filter(SportsModelEntity4.entity_code == code).first()

class SportsRepository5:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity5]:
        return self.db.query(SportsModelEntity5).filter(SportsModelEntity5.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity5]:
        return self.db.query(SportsModelEntity5).filter(SportsModelEntity5.entity_code == code).first()

class SportsRepository6:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity6]:
        return self.db.query(SportsModelEntity6).filter(SportsModelEntity6.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity6]:
        return self.db.query(SportsModelEntity6).filter(SportsModelEntity6.entity_code == code).first()

class SportsRepository7:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity7]:
        return self.db.query(SportsModelEntity7).filter(SportsModelEntity7.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity7]:
        return self.db.query(SportsModelEntity7).filter(SportsModelEntity7.entity_code == code).first()

class SportsRepository8:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity8]:
        return self.db.query(SportsModelEntity8).filter(SportsModelEntity8.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity8]:
        return self.db.query(SportsModelEntity8).filter(SportsModelEntity8.entity_code == code).first()

class SportsRepository9:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity9]:
        return self.db.query(SportsModelEntity9).filter(SportsModelEntity9.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity9]:
        return self.db.query(SportsModelEntity9).filter(SportsModelEntity9.entity_code == code).first()

class SportsRepository10:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity10]:
        return self.db.query(SportsModelEntity10).filter(SportsModelEntity10.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity10]:
        return self.db.query(SportsModelEntity10).filter(SportsModelEntity10.entity_code == code).first()

class SportsRepository11:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity11]:
        return self.db.query(SportsModelEntity11).filter(SportsModelEntity11.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity11]:
        return self.db.query(SportsModelEntity11).filter(SportsModelEntity11.entity_code == code).first()

class SportsRepository12:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity12]:
        return self.db.query(SportsModelEntity12).filter(SportsModelEntity12.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity12]:
        return self.db.query(SportsModelEntity12).filter(SportsModelEntity12.entity_code == code).first()

class SportsRepository13:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity13]:
        return self.db.query(SportsModelEntity13).filter(SportsModelEntity13.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity13]:
        return self.db.query(SportsModelEntity13).filter(SportsModelEntity13.entity_code == code).first()

class SportsRepository14:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity14]:
        return self.db.query(SportsModelEntity14).filter(SportsModelEntity14.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity14]:
        return self.db.query(SportsModelEntity14).filter(SportsModelEntity14.entity_code == code).first()

class SportsRepository15:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity15]:
        return self.db.query(SportsModelEntity15).filter(SportsModelEntity15.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity15]:
        return self.db.query(SportsModelEntity15).filter(SportsModelEntity15.entity_code == code).first()

class SportsRepository16:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity16]:
        return self.db.query(SportsModelEntity16).filter(SportsModelEntity16.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity16]:
        return self.db.query(SportsModelEntity16).filter(SportsModelEntity16.entity_code == code).first()

class SportsRepository17:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity17]:
        return self.db.query(SportsModelEntity17).filter(SportsModelEntity17.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity17]:
        return self.db.query(SportsModelEntity17).filter(SportsModelEntity17.entity_code == code).first()

class SportsRepository18:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity18]:
        return self.db.query(SportsModelEntity18).filter(SportsModelEntity18.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity18]:
        return self.db.query(SportsModelEntity18).filter(SportsModelEntity18.entity_code == code).first()

class SportsRepository19:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity19]:
        return self.db.query(SportsModelEntity19).filter(SportsModelEntity19.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity19]:
        return self.db.query(SportsModelEntity19).filter(SportsModelEntity19.entity_code == code).first()

class SportsRepository20:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity20]:
        return self.db.query(SportsModelEntity20).filter(SportsModelEntity20.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity20]:
        return self.db.query(SportsModelEntity20).filter(SportsModelEntity20.entity_code == code).first()

class SportsRepository21:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity21]:
        return self.db.query(SportsModelEntity21).filter(SportsModelEntity21.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity21]:
        return self.db.query(SportsModelEntity21).filter(SportsModelEntity21.entity_code == code).first()

class SportsRepository22:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity22]:
        return self.db.query(SportsModelEntity22).filter(SportsModelEntity22.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity22]:
        return self.db.query(SportsModelEntity22).filter(SportsModelEntity22.entity_code == code).first()

class SportsRepository23:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity23]:
        return self.db.query(SportsModelEntity23).filter(SportsModelEntity23.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity23]:
        return self.db.query(SportsModelEntity23).filter(SportsModelEntity23.entity_code == code).first()

class SportsRepository24:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity24]:
        return self.db.query(SportsModelEntity24).filter(SportsModelEntity24.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity24]:
        return self.db.query(SportsModelEntity24).filter(SportsModelEntity24.entity_code == code).first()

class SportsRepository25:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity25]:
        return self.db.query(SportsModelEntity25).filter(SportsModelEntity25.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity25]:
        return self.db.query(SportsModelEntity25).filter(SportsModelEntity25.entity_code == code).first()

class SportsRepository26:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity26]:
        return self.db.query(SportsModelEntity26).filter(SportsModelEntity26.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity26]:
        return self.db.query(SportsModelEntity26).filter(SportsModelEntity26.entity_code == code).first()

class SportsRepository27:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity27]:
        return self.db.query(SportsModelEntity27).filter(SportsModelEntity27.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity27]:
        return self.db.query(SportsModelEntity27).filter(SportsModelEntity27.entity_code == code).first()

class SportsRepository28:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity28]:
        return self.db.query(SportsModelEntity28).filter(SportsModelEntity28.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity28]:
        return self.db.query(SportsModelEntity28).filter(SportsModelEntity28.entity_code == code).first()

class SportsRepository29:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity29]:
        return self.db.query(SportsModelEntity29).filter(SportsModelEntity29.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity29]:
        return self.db.query(SportsModelEntity29).filter(SportsModelEntity29.entity_code == code).first()

class SportsRepository30:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity30]:
        return self.db.query(SportsModelEntity30).filter(SportsModelEntity30.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity30]:
        return self.db.query(SportsModelEntity30).filter(SportsModelEntity30.entity_code == code).first()

class SportsRepository31:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity31]:
        return self.db.query(SportsModelEntity31).filter(SportsModelEntity31.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity31]:
        return self.db.query(SportsModelEntity31).filter(SportsModelEntity31.entity_code == code).first()

class SportsRepository32:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity32]:
        return self.db.query(SportsModelEntity32).filter(SportsModelEntity32.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity32]:
        return self.db.query(SportsModelEntity32).filter(SportsModelEntity32.entity_code == code).first()

class SportsRepository33:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity33]:
        return self.db.query(SportsModelEntity33).filter(SportsModelEntity33.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity33]:
        return self.db.query(SportsModelEntity33).filter(SportsModelEntity33.entity_code == code).first()

class SportsRepository34:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity34]:
        return self.db.query(SportsModelEntity34).filter(SportsModelEntity34.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity34]:
        return self.db.query(SportsModelEntity34).filter(SportsModelEntity34.entity_code == code).first()

class SportsRepository35:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity35]:
        return self.db.query(SportsModelEntity35).filter(SportsModelEntity35.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity35]:
        return self.db.query(SportsModelEntity35).filter(SportsModelEntity35.entity_code == code).first()

class SportsRepository36:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity36]:
        return self.db.query(SportsModelEntity36).filter(SportsModelEntity36.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity36]:
        return self.db.query(SportsModelEntity36).filter(SportsModelEntity36.entity_code == code).first()

class SportsRepository37:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity37]:
        return self.db.query(SportsModelEntity37).filter(SportsModelEntity37.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity37]:
        return self.db.query(SportsModelEntity37).filter(SportsModelEntity37.entity_code == code).first()

class SportsRepository38:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity38]:
        return self.db.query(SportsModelEntity38).filter(SportsModelEntity38.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity38]:
        return self.db.query(SportsModelEntity38).filter(SportsModelEntity38.entity_code == code).first()

class SportsRepository39:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity39]:
        return self.db.query(SportsModelEntity39).filter(SportsModelEntity39.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity39]:
        return self.db.query(SportsModelEntity39).filter(SportsModelEntity39.entity_code == code).first()

class SportsRepository40:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity40]:
        return self.db.query(SportsModelEntity40).filter(SportsModelEntity40.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity40]:
        return self.db.query(SportsModelEntity40).filter(SportsModelEntity40.entity_code == code).first()

class SportsRepository41:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity41]:
        return self.db.query(SportsModelEntity41).filter(SportsModelEntity41.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity41]:
        return self.db.query(SportsModelEntity41).filter(SportsModelEntity41.entity_code == code).first()

class SportsRepository42:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity42]:
        return self.db.query(SportsModelEntity42).filter(SportsModelEntity42.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity42]:
        return self.db.query(SportsModelEntity42).filter(SportsModelEntity42.entity_code == code).first()

class SportsRepository43:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity43]:
        return self.db.query(SportsModelEntity43).filter(SportsModelEntity43.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity43]:
        return self.db.query(SportsModelEntity43).filter(SportsModelEntity43.entity_code == code).first()

class SportsRepository44:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity44]:
        return self.db.query(SportsModelEntity44).filter(SportsModelEntity44.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity44]:
        return self.db.query(SportsModelEntity44).filter(SportsModelEntity44.entity_code == code).first()

class SportsRepository45:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity45]:
        return self.db.query(SportsModelEntity45).filter(SportsModelEntity45.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity45]:
        return self.db.query(SportsModelEntity45).filter(SportsModelEntity45.entity_code == code).first()

class SportsRepository46:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity46]:
        return self.db.query(SportsModelEntity46).filter(SportsModelEntity46.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity46]:
        return self.db.query(SportsModelEntity46).filter(SportsModelEntity46.entity_code == code).first()

class SportsRepository47:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity47]:
        return self.db.query(SportsModelEntity47).filter(SportsModelEntity47.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity47]:
        return self.db.query(SportsModelEntity47).filter(SportsModelEntity47.entity_code == code).first()

class SportsRepository48:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity48]:
        return self.db.query(SportsModelEntity48).filter(SportsModelEntity48.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity48]:
        return self.db.query(SportsModelEntity48).filter(SportsModelEntity48.entity_code == code).first()

class SportsRepository49:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity49]:
        return self.db.query(SportsModelEntity49).filter(SportsModelEntity49.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity49]:
        return self.db.query(SportsModelEntity49).filter(SportsModelEntity49.entity_code == code).first()

class SportsRepository50:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity50]:
        return self.db.query(SportsModelEntity50).filter(SportsModelEntity50.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity50]:
        return self.db.query(SportsModelEntity50).filter(SportsModelEntity50.entity_code == code).first()

class SportsRepository51:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity51]:
        return self.db.query(SportsModelEntity51).filter(SportsModelEntity51.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity51]:
        return self.db.query(SportsModelEntity51).filter(SportsModelEntity51.entity_code == code).first()

class SportsRepository52:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity52]:
        return self.db.query(SportsModelEntity52).filter(SportsModelEntity52.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity52]:
        return self.db.query(SportsModelEntity52).filter(SportsModelEntity52.entity_code == code).first()

class SportsRepository53:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity53]:
        return self.db.query(SportsModelEntity53).filter(SportsModelEntity53.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity53]:
        return self.db.query(SportsModelEntity53).filter(SportsModelEntity53.entity_code == code).first()

class SportsRepository54:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity54]:
        return self.db.query(SportsModelEntity54).filter(SportsModelEntity54.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity54]:
        return self.db.query(SportsModelEntity54).filter(SportsModelEntity54.entity_code == code).first()

class SportsRepository55:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity55]:
        return self.db.query(SportsModelEntity55).filter(SportsModelEntity55.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity55]:
        return self.db.query(SportsModelEntity55).filter(SportsModelEntity55.entity_code == code).first()

class SportsRepository56:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity56]:
        return self.db.query(SportsModelEntity56).filter(SportsModelEntity56.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity56]:
        return self.db.query(SportsModelEntity56).filter(SportsModelEntity56.entity_code == code).first()

class SportsRepository57:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity57]:
        return self.db.query(SportsModelEntity57).filter(SportsModelEntity57.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity57]:
        return self.db.query(SportsModelEntity57).filter(SportsModelEntity57.entity_code == code).first()

class SportsRepository58:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity58]:
        return self.db.query(SportsModelEntity58).filter(SportsModelEntity58.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity58]:
        return self.db.query(SportsModelEntity58).filter(SportsModelEntity58.entity_code == code).first()

class SportsRepository59:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity59]:
        return self.db.query(SportsModelEntity59).filter(SportsModelEntity59.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity59]:
        return self.db.query(SportsModelEntity59).filter(SportsModelEntity59.entity_code == code).first()

class SportsRepository60:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity60]:
        return self.db.query(SportsModelEntity60).filter(SportsModelEntity60.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity60]:
        return self.db.query(SportsModelEntity60).filter(SportsModelEntity60.entity_code == code).first()

class SportsRepository61:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity61]:
        return self.db.query(SportsModelEntity61).filter(SportsModelEntity61.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity61]:
        return self.db.query(SportsModelEntity61).filter(SportsModelEntity61.entity_code == code).first()

class SportsRepository62:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity62]:
        return self.db.query(SportsModelEntity62).filter(SportsModelEntity62.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity62]:
        return self.db.query(SportsModelEntity62).filter(SportsModelEntity62.entity_code == code).first()

class SportsRepository63:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity63]:
        return self.db.query(SportsModelEntity63).filter(SportsModelEntity63.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity63]:
        return self.db.query(SportsModelEntity63).filter(SportsModelEntity63.entity_code == code).first()

class SportsRepository64:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity64]:
        return self.db.query(SportsModelEntity64).filter(SportsModelEntity64.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity64]:
        return self.db.query(SportsModelEntity64).filter(SportsModelEntity64.entity_code == code).first()

class SportsRepository65:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity65]:
        return self.db.query(SportsModelEntity65).filter(SportsModelEntity65.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity65]:
        return self.db.query(SportsModelEntity65).filter(SportsModelEntity65.entity_code == code).first()

class SportsRepository66:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity66]:
        return self.db.query(SportsModelEntity66).filter(SportsModelEntity66.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity66]:
        return self.db.query(SportsModelEntity66).filter(SportsModelEntity66.entity_code == code).first()

class SportsRepository67:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity67]:
        return self.db.query(SportsModelEntity67).filter(SportsModelEntity67.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity67]:
        return self.db.query(SportsModelEntity67).filter(SportsModelEntity67.entity_code == code).first()

class SportsRepository68:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity68]:
        return self.db.query(SportsModelEntity68).filter(SportsModelEntity68.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity68]:
        return self.db.query(SportsModelEntity68).filter(SportsModelEntity68.entity_code == code).first()

class SportsRepository69:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity69]:
        return self.db.query(SportsModelEntity69).filter(SportsModelEntity69.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity69]:
        return self.db.query(SportsModelEntity69).filter(SportsModelEntity69.entity_code == code).first()

class SportsRepository70:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity70]:
        return self.db.query(SportsModelEntity70).filter(SportsModelEntity70.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity70]:
        return self.db.query(SportsModelEntity70).filter(SportsModelEntity70.entity_code == code).first()

class SportsRepository71:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity71]:
        return self.db.query(SportsModelEntity71).filter(SportsModelEntity71.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity71]:
        return self.db.query(SportsModelEntity71).filter(SportsModelEntity71.entity_code == code).first()

class SportsRepository72:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity72]:
        return self.db.query(SportsModelEntity72).filter(SportsModelEntity72.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity72]:
        return self.db.query(SportsModelEntity72).filter(SportsModelEntity72.entity_code == code).first()

class SportsRepository73:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity73]:
        return self.db.query(SportsModelEntity73).filter(SportsModelEntity73.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity73]:
        return self.db.query(SportsModelEntity73).filter(SportsModelEntity73.entity_code == code).first()

class SportsRepository74:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity74]:
        return self.db.query(SportsModelEntity74).filter(SportsModelEntity74.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity74]:
        return self.db.query(SportsModelEntity74).filter(SportsModelEntity74.entity_code == code).first()

class SportsRepository75:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity75]:
        return self.db.query(SportsModelEntity75).filter(SportsModelEntity75.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity75]:
        return self.db.query(SportsModelEntity75).filter(SportsModelEntity75.entity_code == code).first()

class SportsRepository76:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity76]:
        return self.db.query(SportsModelEntity76).filter(SportsModelEntity76.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity76]:
        return self.db.query(SportsModelEntity76).filter(SportsModelEntity76.entity_code == code).first()

class SportsRepository77:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity77]:
        return self.db.query(SportsModelEntity77).filter(SportsModelEntity77.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity77]:
        return self.db.query(SportsModelEntity77).filter(SportsModelEntity77.entity_code == code).first()

class SportsRepository78:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity78]:
        return self.db.query(SportsModelEntity78).filter(SportsModelEntity78.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity78]:
        return self.db.query(SportsModelEntity78).filter(SportsModelEntity78.entity_code == code).first()

class SportsRepository79:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity79]:
        return self.db.query(SportsModelEntity79).filter(SportsModelEntity79.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity79]:
        return self.db.query(SportsModelEntity79).filter(SportsModelEntity79.entity_code == code).first()

class SportsRepository80:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity80]:
        return self.db.query(SportsModelEntity80).filter(SportsModelEntity80.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity80]:
        return self.db.query(SportsModelEntity80).filter(SportsModelEntity80.entity_code == code).first()

class SportsRepository81:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity81]:
        return self.db.query(SportsModelEntity81).filter(SportsModelEntity81.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity81]:
        return self.db.query(SportsModelEntity81).filter(SportsModelEntity81.entity_code == code).first()

class SportsRepository82:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity82]:
        return self.db.query(SportsModelEntity82).filter(SportsModelEntity82.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity82]:
        return self.db.query(SportsModelEntity82).filter(SportsModelEntity82.entity_code == code).first()

class SportsRepository83:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity83]:
        return self.db.query(SportsModelEntity83).filter(SportsModelEntity83.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity83]:
        return self.db.query(SportsModelEntity83).filter(SportsModelEntity83.entity_code == code).first()

class SportsRepository84:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity84]:
        return self.db.query(SportsModelEntity84).filter(SportsModelEntity84.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity84]:
        return self.db.query(SportsModelEntity84).filter(SportsModelEntity84.entity_code == code).first()

class SportsRepository85:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity85]:
        return self.db.query(SportsModelEntity85).filter(SportsModelEntity85.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity85]:
        return self.db.query(SportsModelEntity85).filter(SportsModelEntity85.entity_code == code).first()

class SportsRepository86:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity86]:
        return self.db.query(SportsModelEntity86).filter(SportsModelEntity86.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity86]:
        return self.db.query(SportsModelEntity86).filter(SportsModelEntity86.entity_code == code).first()

class SportsRepository87:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity87]:
        return self.db.query(SportsModelEntity87).filter(SportsModelEntity87.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity87]:
        return self.db.query(SportsModelEntity87).filter(SportsModelEntity87.entity_code == code).first()

class SportsRepository88:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity88]:
        return self.db.query(SportsModelEntity88).filter(SportsModelEntity88.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity88]:
        return self.db.query(SportsModelEntity88).filter(SportsModelEntity88.entity_code == code).first()

class SportsRepository89:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity89]:
        return self.db.query(SportsModelEntity89).filter(SportsModelEntity89.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity89]:
        return self.db.query(SportsModelEntity89).filter(SportsModelEntity89.entity_code == code).first()

class SportsRepository90:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity90]:
        return self.db.query(SportsModelEntity90).filter(SportsModelEntity90.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity90]:
        return self.db.query(SportsModelEntity90).filter(SportsModelEntity90.entity_code == code).first()

class SportsRepository91:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity91]:
        return self.db.query(SportsModelEntity91).filter(SportsModelEntity91.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity91]:
        return self.db.query(SportsModelEntity91).filter(SportsModelEntity91.entity_code == code).first()

class SportsRepository92:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity92]:
        return self.db.query(SportsModelEntity92).filter(SportsModelEntity92.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity92]:
        return self.db.query(SportsModelEntity92).filter(SportsModelEntity92.entity_code == code).first()

class SportsRepository93:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity93]:
        return self.db.query(SportsModelEntity93).filter(SportsModelEntity93.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity93]:
        return self.db.query(SportsModelEntity93).filter(SportsModelEntity93.entity_code == code).first()

class SportsRepository94:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity94]:
        return self.db.query(SportsModelEntity94).filter(SportsModelEntity94.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity94]:
        return self.db.query(SportsModelEntity94).filter(SportsModelEntity94.entity_code == code).first()

class SportsRepository95:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity95]:
        return self.db.query(SportsModelEntity95).filter(SportsModelEntity95.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity95]:
        return self.db.query(SportsModelEntity95).filter(SportsModelEntity95.entity_code == code).first()

class SportsRepository96:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity96]:
        return self.db.query(SportsModelEntity96).filter(SportsModelEntity96.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity96]:
        return self.db.query(SportsModelEntity96).filter(SportsModelEntity96.entity_code == code).first()

class SportsRepository97:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity97]:
        return self.db.query(SportsModelEntity97).filter(SportsModelEntity97.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity97]:
        return self.db.query(SportsModelEntity97).filter(SportsModelEntity97.entity_code == code).first()

class SportsRepository98:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity98]:
        return self.db.query(SportsModelEntity98).filter(SportsModelEntity98.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity98]:
        return self.db.query(SportsModelEntity98).filter(SportsModelEntity98.entity_code == code).first()

class SportsRepository99:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity99]:
        return self.db.query(SportsModelEntity99).filter(SportsModelEntity99.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity99]:
        return self.db.query(SportsModelEntity99).filter(SportsModelEntity99.entity_code == code).first()

class SportsRepository100:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity100]:
        return self.db.query(SportsModelEntity100).filter(SportsModelEntity100.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity100]:
        return self.db.query(SportsModelEntity100).filter(SportsModelEntity100.entity_code == code).first()

class SportsRepository101:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity101]:
        return self.db.query(SportsModelEntity101).filter(SportsModelEntity101.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity101]:
        return self.db.query(SportsModelEntity101).filter(SportsModelEntity101.entity_code == code).first()

class SportsRepository102:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity102]:
        return self.db.query(SportsModelEntity102).filter(SportsModelEntity102.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity102]:
        return self.db.query(SportsModelEntity102).filter(SportsModelEntity102.entity_code == code).first()

class SportsRepository103:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity103]:
        return self.db.query(SportsModelEntity103).filter(SportsModelEntity103.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity103]:
        return self.db.query(SportsModelEntity103).filter(SportsModelEntity103.entity_code == code).first()

class SportsRepository104:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity104]:
        return self.db.query(SportsModelEntity104).filter(SportsModelEntity104.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity104]:
        return self.db.query(SportsModelEntity104).filter(SportsModelEntity104.entity_code == code).first()

class SportsRepository105:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity105]:
        return self.db.query(SportsModelEntity105).filter(SportsModelEntity105.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity105]:
        return self.db.query(SportsModelEntity105).filter(SportsModelEntity105.entity_code == code).first()

class SportsRepository106:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity106]:
        return self.db.query(SportsModelEntity106).filter(SportsModelEntity106.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity106]:
        return self.db.query(SportsModelEntity106).filter(SportsModelEntity106.entity_code == code).first()

class SportsRepository107:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity107]:
        return self.db.query(SportsModelEntity107).filter(SportsModelEntity107.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity107]:
        return self.db.query(SportsModelEntity107).filter(SportsModelEntity107.entity_code == code).first()

class SportsRepository108:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity108]:
        return self.db.query(SportsModelEntity108).filter(SportsModelEntity108.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity108]:
        return self.db.query(SportsModelEntity108).filter(SportsModelEntity108.entity_code == code).first()

class SportsRepository109:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity109]:
        return self.db.query(SportsModelEntity109).filter(SportsModelEntity109.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity109]:
        return self.db.query(SportsModelEntity109).filter(SportsModelEntity109.entity_code == code).first()

class SportsRepository110:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity110]:
        return self.db.query(SportsModelEntity110).filter(SportsModelEntity110.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity110]:
        return self.db.query(SportsModelEntity110).filter(SportsModelEntity110.entity_code == code).first()

class SportsRepository111:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity111]:
        return self.db.query(SportsModelEntity111).filter(SportsModelEntity111.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity111]:
        return self.db.query(SportsModelEntity111).filter(SportsModelEntity111.entity_code == code).first()

class SportsRepository112:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity112]:
        return self.db.query(SportsModelEntity112).filter(SportsModelEntity112.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity112]:
        return self.db.query(SportsModelEntity112).filter(SportsModelEntity112.entity_code == code).first()

class SportsRepository113:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity113]:
        return self.db.query(SportsModelEntity113).filter(SportsModelEntity113.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity113]:
        return self.db.query(SportsModelEntity113).filter(SportsModelEntity113.entity_code == code).first()

class SportsRepository114:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity114]:
        return self.db.query(SportsModelEntity114).filter(SportsModelEntity114.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity114]:
        return self.db.query(SportsModelEntity114).filter(SportsModelEntity114.entity_code == code).first()

class SportsRepository115:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity115]:
        return self.db.query(SportsModelEntity115).filter(SportsModelEntity115.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity115]:
        return self.db.query(SportsModelEntity115).filter(SportsModelEntity115.entity_code == code).first()

class SportsRepository116:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity116]:
        return self.db.query(SportsModelEntity116).filter(SportsModelEntity116.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity116]:
        return self.db.query(SportsModelEntity116).filter(SportsModelEntity116.entity_code == code).first()

class SportsRepository117:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity117]:
        return self.db.query(SportsModelEntity117).filter(SportsModelEntity117.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity117]:
        return self.db.query(SportsModelEntity117).filter(SportsModelEntity117.entity_code == code).first()

class SportsRepository118:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity118]:
        return self.db.query(SportsModelEntity118).filter(SportsModelEntity118.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity118]:
        return self.db.query(SportsModelEntity118).filter(SportsModelEntity118.entity_code == code).first()

class SportsRepository119:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity119]:
        return self.db.query(SportsModelEntity119).filter(SportsModelEntity119.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity119]:
        return self.db.query(SportsModelEntity119).filter(SportsModelEntity119.entity_code == code).first()

class SportsRepository120:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity120]:
        return self.db.query(SportsModelEntity120).filter(SportsModelEntity120.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity120]:
        return self.db.query(SportsModelEntity120).filter(SportsModelEntity120.entity_code == code).first()

class SportsRepository121:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity121]:
        return self.db.query(SportsModelEntity121).filter(SportsModelEntity121.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity121]:
        return self.db.query(SportsModelEntity121).filter(SportsModelEntity121.entity_code == code).first()

class SportsRepository122:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity122]:
        return self.db.query(SportsModelEntity122).filter(SportsModelEntity122.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity122]:
        return self.db.query(SportsModelEntity122).filter(SportsModelEntity122.entity_code == code).first()

class SportsRepository123:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity123]:
        return self.db.query(SportsModelEntity123).filter(SportsModelEntity123.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity123]:
        return self.db.query(SportsModelEntity123).filter(SportsModelEntity123.entity_code == code).first()

class SportsRepository124:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity124]:
        return self.db.query(SportsModelEntity124).filter(SportsModelEntity124.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity124]:
        return self.db.query(SportsModelEntity124).filter(SportsModelEntity124.entity_code == code).first()

class SportsRepository125:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity125]:
        return self.db.query(SportsModelEntity125).filter(SportsModelEntity125.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity125]:
        return self.db.query(SportsModelEntity125).filter(SportsModelEntity125.entity_code == code).first()

class SportsRepository126:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity126]:
        return self.db.query(SportsModelEntity126).filter(SportsModelEntity126.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity126]:
        return self.db.query(SportsModelEntity126).filter(SportsModelEntity126.entity_code == code).first()

class SportsRepository127:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity127]:
        return self.db.query(SportsModelEntity127).filter(SportsModelEntity127.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity127]:
        return self.db.query(SportsModelEntity127).filter(SportsModelEntity127.entity_code == code).first()

class SportsRepository128:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity128]:
        return self.db.query(SportsModelEntity128).filter(SportsModelEntity128.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity128]:
        return self.db.query(SportsModelEntity128).filter(SportsModelEntity128.entity_code == code).first()

class SportsRepository129:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity129]:
        return self.db.query(SportsModelEntity129).filter(SportsModelEntity129.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity129]:
        return self.db.query(SportsModelEntity129).filter(SportsModelEntity129.entity_code == code).first()

class SportsRepository130:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity130]:
        return self.db.query(SportsModelEntity130).filter(SportsModelEntity130.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity130]:
        return self.db.query(SportsModelEntity130).filter(SportsModelEntity130.entity_code == code).first()

class SportsRepository131:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity131]:
        return self.db.query(SportsModelEntity131).filter(SportsModelEntity131.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity131]:
        return self.db.query(SportsModelEntity131).filter(SportsModelEntity131.entity_code == code).first()

class SportsRepository132:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity132]:
        return self.db.query(SportsModelEntity132).filter(SportsModelEntity132.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity132]:
        return self.db.query(SportsModelEntity132).filter(SportsModelEntity132.entity_code == code).first()

class SportsRepository133:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity133]:
        return self.db.query(SportsModelEntity133).filter(SportsModelEntity133.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity133]:
        return self.db.query(SportsModelEntity133).filter(SportsModelEntity133.entity_code == code).first()

class SportsRepository134:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity134]:
        return self.db.query(SportsModelEntity134).filter(SportsModelEntity134.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity134]:
        return self.db.query(SportsModelEntity134).filter(SportsModelEntity134.entity_code == code).first()

class SportsRepository135:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity135]:
        return self.db.query(SportsModelEntity135).filter(SportsModelEntity135.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity135]:
        return self.db.query(SportsModelEntity135).filter(SportsModelEntity135.entity_code == code).first()

class SportsRepository136:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity136]:
        return self.db.query(SportsModelEntity136).filter(SportsModelEntity136.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity136]:
        return self.db.query(SportsModelEntity136).filter(SportsModelEntity136.entity_code == code).first()

class SportsRepository137:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity137]:
        return self.db.query(SportsModelEntity137).filter(SportsModelEntity137.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity137]:
        return self.db.query(SportsModelEntity137).filter(SportsModelEntity137.entity_code == code).first()

class SportsRepository138:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity138]:
        return self.db.query(SportsModelEntity138).filter(SportsModelEntity138.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity138]:
        return self.db.query(SportsModelEntity138).filter(SportsModelEntity138.entity_code == code).first()

class SportsRepository139:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity139]:
        return self.db.query(SportsModelEntity139).filter(SportsModelEntity139.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity139]:
        return self.db.query(SportsModelEntity139).filter(SportsModelEntity139.entity_code == code).first()

class SportsRepository140:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity140]:
        return self.db.query(SportsModelEntity140).filter(SportsModelEntity140.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity140]:
        return self.db.query(SportsModelEntity140).filter(SportsModelEntity140.entity_code == code).first()

class SportsRepository141:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity141]:
        return self.db.query(SportsModelEntity141).filter(SportsModelEntity141.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity141]:
        return self.db.query(SportsModelEntity141).filter(SportsModelEntity141.entity_code == code).first()

class SportsRepository142:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity142]:
        return self.db.query(SportsModelEntity142).filter(SportsModelEntity142.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity142]:
        return self.db.query(SportsModelEntity142).filter(SportsModelEntity142.entity_code == code).first()

class SportsRepository143:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity143]:
        return self.db.query(SportsModelEntity143).filter(SportsModelEntity143.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity143]:
        return self.db.query(SportsModelEntity143).filter(SportsModelEntity143.entity_code == code).first()

class SportsRepository144:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity144]:
        return self.db.query(SportsModelEntity144).filter(SportsModelEntity144.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity144]:
        return self.db.query(SportsModelEntity144).filter(SportsModelEntity144.entity_code == code).first()

class SportsRepository145:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity145]:
        return self.db.query(SportsModelEntity145).filter(SportsModelEntity145.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity145]:
        return self.db.query(SportsModelEntity145).filter(SportsModelEntity145.entity_code == code).first()

class SportsRepository146:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity146]:
        return self.db.query(SportsModelEntity146).filter(SportsModelEntity146.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity146]:
        return self.db.query(SportsModelEntity146).filter(SportsModelEntity146.entity_code == code).first()

class SportsRepository147:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity147]:
        return self.db.query(SportsModelEntity147).filter(SportsModelEntity147.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity147]:
        return self.db.query(SportsModelEntity147).filter(SportsModelEntity147.entity_code == code).first()

class SportsRepository148:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity148]:
        return self.db.query(SportsModelEntity148).filter(SportsModelEntity148.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity148]:
        return self.db.query(SportsModelEntity148).filter(SportsModelEntity148.entity_code == code).first()

class SportsRepository149:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity149]:
        return self.db.query(SportsModelEntity149).filter(SportsModelEntity149.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity149]:
        return self.db.query(SportsModelEntity149).filter(SportsModelEntity149.entity_code == code).first()

class SportsRepository150:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity150]:
        return self.db.query(SportsModelEntity150).filter(SportsModelEntity150.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity150]:
        return self.db.query(SportsModelEntity150).filter(SportsModelEntity150.entity_code == code).first()

class SportsRepository151:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity151]:
        return self.db.query(SportsModelEntity151).filter(SportsModelEntity151.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity151]:
        return self.db.query(SportsModelEntity151).filter(SportsModelEntity151.entity_code == code).first()

class SportsRepository152:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity152]:
        return self.db.query(SportsModelEntity152).filter(SportsModelEntity152.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity152]:
        return self.db.query(SportsModelEntity152).filter(SportsModelEntity152.entity_code == code).first()

class SportsRepository153:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity153]:
        return self.db.query(SportsModelEntity153).filter(SportsModelEntity153.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity153]:
        return self.db.query(SportsModelEntity153).filter(SportsModelEntity153.entity_code == code).first()

class SportsRepository154:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity154]:
        return self.db.query(SportsModelEntity154).filter(SportsModelEntity154.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity154]:
        return self.db.query(SportsModelEntity154).filter(SportsModelEntity154.entity_code == code).first()

class SportsRepository155:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity155]:
        return self.db.query(SportsModelEntity155).filter(SportsModelEntity155.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity155]:
        return self.db.query(SportsModelEntity155).filter(SportsModelEntity155.entity_code == code).first()

class SportsRepository156:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity156]:
        return self.db.query(SportsModelEntity156).filter(SportsModelEntity156.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity156]:
        return self.db.query(SportsModelEntity156).filter(SportsModelEntity156.entity_code == code).first()

class SportsRepository157:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity157]:
        return self.db.query(SportsModelEntity157).filter(SportsModelEntity157.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity157]:
        return self.db.query(SportsModelEntity157).filter(SportsModelEntity157.entity_code == code).first()

class SportsRepository158:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity158]:
        return self.db.query(SportsModelEntity158).filter(SportsModelEntity158.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity158]:
        return self.db.query(SportsModelEntity158).filter(SportsModelEntity158.entity_code == code).first()

class SportsRepository159:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity159]:
        return self.db.query(SportsModelEntity159).filter(SportsModelEntity159.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity159]:
        return self.db.query(SportsModelEntity159).filter(SportsModelEntity159.entity_code == code).first()

class SportsRepository160:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity160]:
        return self.db.query(SportsModelEntity160).filter(SportsModelEntity160.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity160]:
        return self.db.query(SportsModelEntity160).filter(SportsModelEntity160.entity_code == code).first()

class SportsRepository161:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity161]:
        return self.db.query(SportsModelEntity161).filter(SportsModelEntity161.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity161]:
        return self.db.query(SportsModelEntity161).filter(SportsModelEntity161.entity_code == code).first()

class SportsRepository162:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity162]:
        return self.db.query(SportsModelEntity162).filter(SportsModelEntity162.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity162]:
        return self.db.query(SportsModelEntity162).filter(SportsModelEntity162.entity_code == code).first()

class SportsRepository163:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity163]:
        return self.db.query(SportsModelEntity163).filter(SportsModelEntity163.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity163]:
        return self.db.query(SportsModelEntity163).filter(SportsModelEntity163.entity_code == code).first()

class SportsRepository164:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity164]:
        return self.db.query(SportsModelEntity164).filter(SportsModelEntity164.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity164]:
        return self.db.query(SportsModelEntity164).filter(SportsModelEntity164.entity_code == code).first()

class SportsRepository165:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity165]:
        return self.db.query(SportsModelEntity165).filter(SportsModelEntity165.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity165]:
        return self.db.query(SportsModelEntity165).filter(SportsModelEntity165.entity_code == code).first()

class SportsRepository166:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity166]:
        return self.db.query(SportsModelEntity166).filter(SportsModelEntity166.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity166]:
        return self.db.query(SportsModelEntity166).filter(SportsModelEntity166.entity_code == code).first()

class SportsRepository167:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity167]:
        return self.db.query(SportsModelEntity167).filter(SportsModelEntity167.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity167]:
        return self.db.query(SportsModelEntity167).filter(SportsModelEntity167.entity_code == code).first()

class SportsRepository168:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity168]:
        return self.db.query(SportsModelEntity168).filter(SportsModelEntity168.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity168]:
        return self.db.query(SportsModelEntity168).filter(SportsModelEntity168.entity_code == code).first()

class SportsRepository169:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity169]:
        return self.db.query(SportsModelEntity169).filter(SportsModelEntity169.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity169]:
        return self.db.query(SportsModelEntity169).filter(SportsModelEntity169.entity_code == code).first()

class SportsRepository170:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity170]:
        return self.db.query(SportsModelEntity170).filter(SportsModelEntity170.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity170]:
        return self.db.query(SportsModelEntity170).filter(SportsModelEntity170.entity_code == code).first()

class SportsRepository171:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity171]:
        return self.db.query(SportsModelEntity171).filter(SportsModelEntity171.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity171]:
        return self.db.query(SportsModelEntity171).filter(SportsModelEntity171.entity_code == code).first()

class SportsRepository172:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity172]:
        return self.db.query(SportsModelEntity172).filter(SportsModelEntity172.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity172]:
        return self.db.query(SportsModelEntity172).filter(SportsModelEntity172.entity_code == code).first()

class SportsRepository173:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity173]:
        return self.db.query(SportsModelEntity173).filter(SportsModelEntity173.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity173]:
        return self.db.query(SportsModelEntity173).filter(SportsModelEntity173.entity_code == code).first()

class SportsRepository174:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity174]:
        return self.db.query(SportsModelEntity174).filter(SportsModelEntity174.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity174]:
        return self.db.query(SportsModelEntity174).filter(SportsModelEntity174.entity_code == code).first()

class SportsRepository175:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity175]:
        return self.db.query(SportsModelEntity175).filter(SportsModelEntity175.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity175]:
        return self.db.query(SportsModelEntity175).filter(SportsModelEntity175.entity_code == code).first()

class SportsRepository176:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity176]:
        return self.db.query(SportsModelEntity176).filter(SportsModelEntity176.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity176]:
        return self.db.query(SportsModelEntity176).filter(SportsModelEntity176.entity_code == code).first()

class SportsRepository177:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity177]:
        return self.db.query(SportsModelEntity177).filter(SportsModelEntity177.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity177]:
        return self.db.query(SportsModelEntity177).filter(SportsModelEntity177.entity_code == code).first()

class SportsRepository178:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity178]:
        return self.db.query(SportsModelEntity178).filter(SportsModelEntity178.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity178]:
        return self.db.query(SportsModelEntity178).filter(SportsModelEntity178.entity_code == code).first()

class SportsRepository179:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity179]:
        return self.db.query(SportsModelEntity179).filter(SportsModelEntity179.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity179]:
        return self.db.query(SportsModelEntity179).filter(SportsModelEntity179.entity_code == code).first()

class SportsRepository180:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity180]:
        return self.db.query(SportsModelEntity180).filter(SportsModelEntity180.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity180]:
        return self.db.query(SportsModelEntity180).filter(SportsModelEntity180.entity_code == code).first()

class SportsRepository181:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity181]:
        return self.db.query(SportsModelEntity181).filter(SportsModelEntity181.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity181]:
        return self.db.query(SportsModelEntity181).filter(SportsModelEntity181.entity_code == code).first()

class SportsRepository182:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity182]:
        return self.db.query(SportsModelEntity182).filter(SportsModelEntity182.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity182]:
        return self.db.query(SportsModelEntity182).filter(SportsModelEntity182.entity_code == code).first()

class SportsRepository183:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity183]:
        return self.db.query(SportsModelEntity183).filter(SportsModelEntity183.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity183]:
        return self.db.query(SportsModelEntity183).filter(SportsModelEntity183.entity_code == code).first()

class SportsRepository184:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity184]:
        return self.db.query(SportsModelEntity184).filter(SportsModelEntity184.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity184]:
        return self.db.query(SportsModelEntity184).filter(SportsModelEntity184.entity_code == code).first()

class SportsRepository185:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity185]:
        return self.db.query(SportsModelEntity185).filter(SportsModelEntity185.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity185]:
        return self.db.query(SportsModelEntity185).filter(SportsModelEntity185.entity_code == code).first()

class SportsRepository186:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity186]:
        return self.db.query(SportsModelEntity186).filter(SportsModelEntity186.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity186]:
        return self.db.query(SportsModelEntity186).filter(SportsModelEntity186.entity_code == code).first()

class SportsRepository187:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity187]:
        return self.db.query(SportsModelEntity187).filter(SportsModelEntity187.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity187]:
        return self.db.query(SportsModelEntity187).filter(SportsModelEntity187.entity_code == code).first()

class SportsRepository188:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity188]:
        return self.db.query(SportsModelEntity188).filter(SportsModelEntity188.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity188]:
        return self.db.query(SportsModelEntity188).filter(SportsModelEntity188.entity_code == code).first()

class SportsRepository189:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity189]:
        return self.db.query(SportsModelEntity189).filter(SportsModelEntity189.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity189]:
        return self.db.query(SportsModelEntity189).filter(SportsModelEntity189.entity_code == code).first()

class SportsRepository190:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity190]:
        return self.db.query(SportsModelEntity190).filter(SportsModelEntity190.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity190]:
        return self.db.query(SportsModelEntity190).filter(SportsModelEntity190.entity_code == code).first()

class SportsRepository191:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity191]:
        return self.db.query(SportsModelEntity191).filter(SportsModelEntity191.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity191]:
        return self.db.query(SportsModelEntity191).filter(SportsModelEntity191.entity_code == code).first()

class SportsRepository192:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity192]:
        return self.db.query(SportsModelEntity192).filter(SportsModelEntity192.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity192]:
        return self.db.query(SportsModelEntity192).filter(SportsModelEntity192.entity_code == code).first()

class SportsRepository193:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity193]:
        return self.db.query(SportsModelEntity193).filter(SportsModelEntity193.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity193]:
        return self.db.query(SportsModelEntity193).filter(SportsModelEntity193.entity_code == code).first()

class SportsRepository194:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity194]:
        return self.db.query(SportsModelEntity194).filter(SportsModelEntity194.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity194]:
        return self.db.query(SportsModelEntity194).filter(SportsModelEntity194.entity_code == code).first()

class SportsRepository195:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity195]:
        return self.db.query(SportsModelEntity195).filter(SportsModelEntity195.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity195]:
        return self.db.query(SportsModelEntity195).filter(SportsModelEntity195.entity_code == code).first()

class SportsRepository196:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity196]:
        return self.db.query(SportsModelEntity196).filter(SportsModelEntity196.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity196]:
        return self.db.query(SportsModelEntity196).filter(SportsModelEntity196.entity_code == code).first()

class SportsRepository197:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity197]:
        return self.db.query(SportsModelEntity197).filter(SportsModelEntity197.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity197]:
        return self.db.query(SportsModelEntity197).filter(SportsModelEntity197.entity_code == code).first()

class SportsRepository198:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity198]:
        return self.db.query(SportsModelEntity198).filter(SportsModelEntity198.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity198]:
        return self.db.query(SportsModelEntity198).filter(SportsModelEntity198.entity_code == code).first()

class SportsRepository199:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity199]:
        return self.db.query(SportsModelEntity199).filter(SportsModelEntity199.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity199]:
        return self.db.query(SportsModelEntity199).filter(SportsModelEntity199.entity_code == code).first()

class SportsRepository200:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity200]:
        return self.db.query(SportsModelEntity200).filter(SportsModelEntity200.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity200]:
        return self.db.query(SportsModelEntity200).filter(SportsModelEntity200.entity_code == code).first()

class SportsRepository201:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity201]:
        return self.db.query(SportsModelEntity201).filter(SportsModelEntity201.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity201]:
        return self.db.query(SportsModelEntity201).filter(SportsModelEntity201.entity_code == code).first()

class SportsRepository202:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity202]:
        return self.db.query(SportsModelEntity202).filter(SportsModelEntity202.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity202]:
        return self.db.query(SportsModelEntity202).filter(SportsModelEntity202.entity_code == code).first()

class SportsRepository203:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity203]:
        return self.db.query(SportsModelEntity203).filter(SportsModelEntity203.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity203]:
        return self.db.query(SportsModelEntity203).filter(SportsModelEntity203.entity_code == code).first()

class SportsRepository204:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity204]:
        return self.db.query(SportsModelEntity204).filter(SportsModelEntity204.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity204]:
        return self.db.query(SportsModelEntity204).filter(SportsModelEntity204.entity_code == code).first()

class SportsRepository205:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity205]:
        return self.db.query(SportsModelEntity205).filter(SportsModelEntity205.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity205]:
        return self.db.query(SportsModelEntity205).filter(SportsModelEntity205.entity_code == code).first()

class SportsRepository206:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity206]:
        return self.db.query(SportsModelEntity206).filter(SportsModelEntity206.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity206]:
        return self.db.query(SportsModelEntity206).filter(SportsModelEntity206.entity_code == code).first()

class SportsRepository207:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity207]:
        return self.db.query(SportsModelEntity207).filter(SportsModelEntity207.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity207]:
        return self.db.query(SportsModelEntity207).filter(SportsModelEntity207.entity_code == code).first()

class SportsRepository208:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity208]:
        return self.db.query(SportsModelEntity208).filter(SportsModelEntity208.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity208]:
        return self.db.query(SportsModelEntity208).filter(SportsModelEntity208.entity_code == code).first()

class SportsRepository209:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity209]:
        return self.db.query(SportsModelEntity209).filter(SportsModelEntity209.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity209]:
        return self.db.query(SportsModelEntity209).filter(SportsModelEntity209.entity_code == code).first()

class SportsRepository210:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity210]:
        return self.db.query(SportsModelEntity210).filter(SportsModelEntity210.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity210]:
        return self.db.query(SportsModelEntity210).filter(SportsModelEntity210.entity_code == code).first()

class SportsRepository211:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity211]:
        return self.db.query(SportsModelEntity211).filter(SportsModelEntity211.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity211]:
        return self.db.query(SportsModelEntity211).filter(SportsModelEntity211.entity_code == code).first()

class SportsRepository212:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity212]:
        return self.db.query(SportsModelEntity212).filter(SportsModelEntity212.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity212]:
        return self.db.query(SportsModelEntity212).filter(SportsModelEntity212.entity_code == code).first()

class SportsRepository213:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity213]:
        return self.db.query(SportsModelEntity213).filter(SportsModelEntity213.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity213]:
        return self.db.query(SportsModelEntity213).filter(SportsModelEntity213.entity_code == code).first()

class SportsRepository214:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity214]:
        return self.db.query(SportsModelEntity214).filter(SportsModelEntity214.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity214]:
        return self.db.query(SportsModelEntity214).filter(SportsModelEntity214.entity_code == code).first()

class SportsRepository215:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity215]:
        return self.db.query(SportsModelEntity215).filter(SportsModelEntity215.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity215]:
        return self.db.query(SportsModelEntity215).filter(SportsModelEntity215.entity_code == code).first()

class SportsRepository216:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity216]:
        return self.db.query(SportsModelEntity216).filter(SportsModelEntity216.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity216]:
        return self.db.query(SportsModelEntity216).filter(SportsModelEntity216.entity_code == code).first()

class SportsRepository217:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity217]:
        return self.db.query(SportsModelEntity217).filter(SportsModelEntity217.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity217]:
        return self.db.query(SportsModelEntity217).filter(SportsModelEntity217.entity_code == code).first()

class SportsRepository218:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity218]:
        return self.db.query(SportsModelEntity218).filter(SportsModelEntity218.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity218]:
        return self.db.query(SportsModelEntity218).filter(SportsModelEntity218.entity_code == code).first()

class SportsRepository219:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity219]:
        return self.db.query(SportsModelEntity219).filter(SportsModelEntity219.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity219]:
        return self.db.query(SportsModelEntity219).filter(SportsModelEntity219.entity_code == code).first()

class SportsRepository220:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity220]:
        return self.db.query(SportsModelEntity220).filter(SportsModelEntity220.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity220]:
        return self.db.query(SportsModelEntity220).filter(SportsModelEntity220.entity_code == code).first()

class SportsRepository221:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity221]:
        return self.db.query(SportsModelEntity221).filter(SportsModelEntity221.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity221]:
        return self.db.query(SportsModelEntity221).filter(SportsModelEntity221.entity_code == code).first()

class SportsRepository222:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity222]:
        return self.db.query(SportsModelEntity222).filter(SportsModelEntity222.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity222]:
        return self.db.query(SportsModelEntity222).filter(SportsModelEntity222.entity_code == code).first()

class SportsRepository223:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity223]:
        return self.db.query(SportsModelEntity223).filter(SportsModelEntity223.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity223]:
        return self.db.query(SportsModelEntity223).filter(SportsModelEntity223.entity_code == code).first()

class SportsRepository224:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity224]:
        return self.db.query(SportsModelEntity224).filter(SportsModelEntity224.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity224]:
        return self.db.query(SportsModelEntity224).filter(SportsModelEntity224.entity_code == code).first()

class SportsRepository225:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity225]:
        return self.db.query(SportsModelEntity225).filter(SportsModelEntity225.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity225]:
        return self.db.query(SportsModelEntity225).filter(SportsModelEntity225.entity_code == code).first()

class SportsRepository226:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity226]:
        return self.db.query(SportsModelEntity226).filter(SportsModelEntity226.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity226]:
        return self.db.query(SportsModelEntity226).filter(SportsModelEntity226.entity_code == code).first()

class SportsRepository227:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity227]:
        return self.db.query(SportsModelEntity227).filter(SportsModelEntity227.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity227]:
        return self.db.query(SportsModelEntity227).filter(SportsModelEntity227.entity_code == code).first()

class SportsRepository228:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity228]:
        return self.db.query(SportsModelEntity228).filter(SportsModelEntity228.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity228]:
        return self.db.query(SportsModelEntity228).filter(SportsModelEntity228.entity_code == code).first()

class SportsRepository229:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity229]:
        return self.db.query(SportsModelEntity229).filter(SportsModelEntity229.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity229]:
        return self.db.query(SportsModelEntity229).filter(SportsModelEntity229.entity_code == code).first()

class SportsRepository230:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity230]:
        return self.db.query(SportsModelEntity230).filter(SportsModelEntity230.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity230]:
        return self.db.query(SportsModelEntity230).filter(SportsModelEntity230.entity_code == code).first()

class SportsRepository231:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity231]:
        return self.db.query(SportsModelEntity231).filter(SportsModelEntity231.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity231]:
        return self.db.query(SportsModelEntity231).filter(SportsModelEntity231.entity_code == code).first()

class SportsRepository232:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity232]:
        return self.db.query(SportsModelEntity232).filter(SportsModelEntity232.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity232]:
        return self.db.query(SportsModelEntity232).filter(SportsModelEntity232.entity_code == code).first()

class SportsRepository233:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity233]:
        return self.db.query(SportsModelEntity233).filter(SportsModelEntity233.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity233]:
        return self.db.query(SportsModelEntity233).filter(SportsModelEntity233.entity_code == code).first()

class SportsRepository234:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity234]:
        return self.db.query(SportsModelEntity234).filter(SportsModelEntity234.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity234]:
        return self.db.query(SportsModelEntity234).filter(SportsModelEntity234.entity_code == code).first()

class SportsRepository235:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity235]:
        return self.db.query(SportsModelEntity235).filter(SportsModelEntity235.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity235]:
        return self.db.query(SportsModelEntity235).filter(SportsModelEntity235.entity_code == code).first()

class SportsRepository236:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity236]:
        return self.db.query(SportsModelEntity236).filter(SportsModelEntity236.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity236]:
        return self.db.query(SportsModelEntity236).filter(SportsModelEntity236.entity_code == code).first()

class SportsRepository237:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity237]:
        return self.db.query(SportsModelEntity237).filter(SportsModelEntity237.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity237]:
        return self.db.query(SportsModelEntity237).filter(SportsModelEntity237.entity_code == code).first()

class SportsRepository238:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity238]:
        return self.db.query(SportsModelEntity238).filter(SportsModelEntity238.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity238]:
        return self.db.query(SportsModelEntity238).filter(SportsModelEntity238.entity_code == code).first()

class SportsRepository239:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity239]:
        return self.db.query(SportsModelEntity239).filter(SportsModelEntity239.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity239]:
        return self.db.query(SportsModelEntity239).filter(SportsModelEntity239.entity_code == code).first()

class SportsRepository240:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity240]:
        return self.db.query(SportsModelEntity240).filter(SportsModelEntity240.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity240]:
        return self.db.query(SportsModelEntity240).filter(SportsModelEntity240.entity_code == code).first()

class SportsRepository241:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity241]:
        return self.db.query(SportsModelEntity241).filter(SportsModelEntity241.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity241]:
        return self.db.query(SportsModelEntity241).filter(SportsModelEntity241.entity_code == code).first()

class SportsRepository242:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity242]:
        return self.db.query(SportsModelEntity242).filter(SportsModelEntity242.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity242]:
        return self.db.query(SportsModelEntity242).filter(SportsModelEntity242.entity_code == code).first()

class SportsRepository243:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity243]:
        return self.db.query(SportsModelEntity243).filter(SportsModelEntity243.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity243]:
        return self.db.query(SportsModelEntity243).filter(SportsModelEntity243.entity_code == code).first()

class SportsRepository244:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity244]:
        return self.db.query(SportsModelEntity244).filter(SportsModelEntity244.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity244]:
        return self.db.query(SportsModelEntity244).filter(SportsModelEntity244.entity_code == code).first()

class SportsRepository245:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity245]:
        return self.db.query(SportsModelEntity245).filter(SportsModelEntity245.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity245]:
        return self.db.query(SportsModelEntity245).filter(SportsModelEntity245.entity_code == code).first()

class SportsRepository246:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity246]:
        return self.db.query(SportsModelEntity246).filter(SportsModelEntity246.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity246]:
        return self.db.query(SportsModelEntity246).filter(SportsModelEntity246.entity_code == code).first()

class SportsRepository247:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity247]:
        return self.db.query(SportsModelEntity247).filter(SportsModelEntity247.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity247]:
        return self.db.query(SportsModelEntity247).filter(SportsModelEntity247.entity_code == code).first()

class SportsRepository248:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity248]:
        return self.db.query(SportsModelEntity248).filter(SportsModelEntity248.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity248]:
        return self.db.query(SportsModelEntity248).filter(SportsModelEntity248.entity_code == code).first()

class SportsRepository249:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity249]:
        return self.db.query(SportsModelEntity249).filter(SportsModelEntity249.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity249]:
        return self.db.query(SportsModelEntity249).filter(SportsModelEntity249.entity_code == code).first()

class SportsRepository250:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[SportsModelEntity250]:
        return self.db.query(SportsModelEntity250).filter(SportsModelEntity250.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[SportsModelEntity250]:
        return self.db.query(SportsModelEntity250).filter(SportsModelEntity250.entity_code == code).first()

