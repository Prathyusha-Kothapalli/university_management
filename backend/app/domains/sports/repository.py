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

