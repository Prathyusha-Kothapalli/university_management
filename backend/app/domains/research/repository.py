"""
Research, Grants & Lab Inventory - Data Access Repository Layer
Module: app.domains.research.repository
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domains.research.models import *

class ResearchRepository1:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity1]:
        return self.db.query(ResearchModelEntity1).filter(ResearchModelEntity1.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity1]:
        return self.db.query(ResearchModelEntity1).filter(ResearchModelEntity1.entity_code == code).first()

class ResearchRepository2:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity2]:
        return self.db.query(ResearchModelEntity2).filter(ResearchModelEntity2.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity2]:
        return self.db.query(ResearchModelEntity2).filter(ResearchModelEntity2.entity_code == code).first()

class ResearchRepository3:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity3]:
        return self.db.query(ResearchModelEntity3).filter(ResearchModelEntity3.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity3]:
        return self.db.query(ResearchModelEntity3).filter(ResearchModelEntity3.entity_code == code).first()

class ResearchRepository4:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity4]:
        return self.db.query(ResearchModelEntity4).filter(ResearchModelEntity4.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity4]:
        return self.db.query(ResearchModelEntity4).filter(ResearchModelEntity4.entity_code == code).first()

class ResearchRepository5:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity5]:
        return self.db.query(ResearchModelEntity5).filter(ResearchModelEntity5.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity5]:
        return self.db.query(ResearchModelEntity5).filter(ResearchModelEntity5.entity_code == code).first()

class ResearchRepository6:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity6]:
        return self.db.query(ResearchModelEntity6).filter(ResearchModelEntity6.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity6]:
        return self.db.query(ResearchModelEntity6).filter(ResearchModelEntity6.entity_code == code).first()

class ResearchRepository7:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity7]:
        return self.db.query(ResearchModelEntity7).filter(ResearchModelEntity7.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity7]:
        return self.db.query(ResearchModelEntity7).filter(ResearchModelEntity7.entity_code == code).first()

class ResearchRepository8:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity8]:
        return self.db.query(ResearchModelEntity8).filter(ResearchModelEntity8.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity8]:
        return self.db.query(ResearchModelEntity8).filter(ResearchModelEntity8.entity_code == code).first()

class ResearchRepository9:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity9]:
        return self.db.query(ResearchModelEntity9).filter(ResearchModelEntity9.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity9]:
        return self.db.query(ResearchModelEntity9).filter(ResearchModelEntity9.entity_code == code).first()

class ResearchRepository10:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity10]:
        return self.db.query(ResearchModelEntity10).filter(ResearchModelEntity10.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity10]:
        return self.db.query(ResearchModelEntity10).filter(ResearchModelEntity10.entity_code == code).first()

class ResearchRepository11:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity11]:
        return self.db.query(ResearchModelEntity11).filter(ResearchModelEntity11.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity11]:
        return self.db.query(ResearchModelEntity11).filter(ResearchModelEntity11.entity_code == code).first()

class ResearchRepository12:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity12]:
        return self.db.query(ResearchModelEntity12).filter(ResearchModelEntity12.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity12]:
        return self.db.query(ResearchModelEntity12).filter(ResearchModelEntity12.entity_code == code).first()

class ResearchRepository13:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity13]:
        return self.db.query(ResearchModelEntity13).filter(ResearchModelEntity13.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity13]:
        return self.db.query(ResearchModelEntity13).filter(ResearchModelEntity13.entity_code == code).first()

class ResearchRepository14:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity14]:
        return self.db.query(ResearchModelEntity14).filter(ResearchModelEntity14.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity14]:
        return self.db.query(ResearchModelEntity14).filter(ResearchModelEntity14.entity_code == code).first()

class ResearchRepository15:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity15]:
        return self.db.query(ResearchModelEntity15).filter(ResearchModelEntity15.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity15]:
        return self.db.query(ResearchModelEntity15).filter(ResearchModelEntity15.entity_code == code).first()

class ResearchRepository16:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity16]:
        return self.db.query(ResearchModelEntity16).filter(ResearchModelEntity16.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity16]:
        return self.db.query(ResearchModelEntity16).filter(ResearchModelEntity16.entity_code == code).first()

class ResearchRepository17:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity17]:
        return self.db.query(ResearchModelEntity17).filter(ResearchModelEntity17.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity17]:
        return self.db.query(ResearchModelEntity17).filter(ResearchModelEntity17.entity_code == code).first()

class ResearchRepository18:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity18]:
        return self.db.query(ResearchModelEntity18).filter(ResearchModelEntity18.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity18]:
        return self.db.query(ResearchModelEntity18).filter(ResearchModelEntity18.entity_code == code).first()

class ResearchRepository19:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity19]:
        return self.db.query(ResearchModelEntity19).filter(ResearchModelEntity19.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity19]:
        return self.db.query(ResearchModelEntity19).filter(ResearchModelEntity19.entity_code == code).first()

class ResearchRepository20:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity20]:
        return self.db.query(ResearchModelEntity20).filter(ResearchModelEntity20.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity20]:
        return self.db.query(ResearchModelEntity20).filter(ResearchModelEntity20.entity_code == code).first()

class ResearchRepository21:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity21]:
        return self.db.query(ResearchModelEntity21).filter(ResearchModelEntity21.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity21]:
        return self.db.query(ResearchModelEntity21).filter(ResearchModelEntity21.entity_code == code).first()

class ResearchRepository22:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity22]:
        return self.db.query(ResearchModelEntity22).filter(ResearchModelEntity22.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity22]:
        return self.db.query(ResearchModelEntity22).filter(ResearchModelEntity22.entity_code == code).first()

class ResearchRepository23:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity23]:
        return self.db.query(ResearchModelEntity23).filter(ResearchModelEntity23.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity23]:
        return self.db.query(ResearchModelEntity23).filter(ResearchModelEntity23.entity_code == code).first()

class ResearchRepository24:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity24]:
        return self.db.query(ResearchModelEntity24).filter(ResearchModelEntity24.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity24]:
        return self.db.query(ResearchModelEntity24).filter(ResearchModelEntity24.entity_code == code).first()

class ResearchRepository25:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity25]:
        return self.db.query(ResearchModelEntity25).filter(ResearchModelEntity25.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity25]:
        return self.db.query(ResearchModelEntity25).filter(ResearchModelEntity25.entity_code == code).first()

class ResearchRepository26:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity26]:
        return self.db.query(ResearchModelEntity26).filter(ResearchModelEntity26.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity26]:
        return self.db.query(ResearchModelEntity26).filter(ResearchModelEntity26.entity_code == code).first()

class ResearchRepository27:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity27]:
        return self.db.query(ResearchModelEntity27).filter(ResearchModelEntity27.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity27]:
        return self.db.query(ResearchModelEntity27).filter(ResearchModelEntity27.entity_code == code).first()

class ResearchRepository28:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity28]:
        return self.db.query(ResearchModelEntity28).filter(ResearchModelEntity28.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity28]:
        return self.db.query(ResearchModelEntity28).filter(ResearchModelEntity28.entity_code == code).first()

class ResearchRepository29:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity29]:
        return self.db.query(ResearchModelEntity29).filter(ResearchModelEntity29.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity29]:
        return self.db.query(ResearchModelEntity29).filter(ResearchModelEntity29.entity_code == code).first()

class ResearchRepository30:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity30]:
        return self.db.query(ResearchModelEntity30).filter(ResearchModelEntity30.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity30]:
        return self.db.query(ResearchModelEntity30).filter(ResearchModelEntity30.entity_code == code).first()

class ResearchRepository31:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity31]:
        return self.db.query(ResearchModelEntity31).filter(ResearchModelEntity31.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity31]:
        return self.db.query(ResearchModelEntity31).filter(ResearchModelEntity31.entity_code == code).first()

class ResearchRepository32:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity32]:
        return self.db.query(ResearchModelEntity32).filter(ResearchModelEntity32.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity32]:
        return self.db.query(ResearchModelEntity32).filter(ResearchModelEntity32.entity_code == code).first()

class ResearchRepository33:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity33]:
        return self.db.query(ResearchModelEntity33).filter(ResearchModelEntity33.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity33]:
        return self.db.query(ResearchModelEntity33).filter(ResearchModelEntity33.entity_code == code).first()

class ResearchRepository34:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity34]:
        return self.db.query(ResearchModelEntity34).filter(ResearchModelEntity34.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity34]:
        return self.db.query(ResearchModelEntity34).filter(ResearchModelEntity34.entity_code == code).first()

class ResearchRepository35:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity35]:
        return self.db.query(ResearchModelEntity35).filter(ResearchModelEntity35.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity35]:
        return self.db.query(ResearchModelEntity35).filter(ResearchModelEntity35.entity_code == code).first()

class ResearchRepository36:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity36]:
        return self.db.query(ResearchModelEntity36).filter(ResearchModelEntity36.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity36]:
        return self.db.query(ResearchModelEntity36).filter(ResearchModelEntity36.entity_code == code).first()

class ResearchRepository37:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity37]:
        return self.db.query(ResearchModelEntity37).filter(ResearchModelEntity37.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity37]:
        return self.db.query(ResearchModelEntity37).filter(ResearchModelEntity37.entity_code == code).first()

class ResearchRepository38:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity38]:
        return self.db.query(ResearchModelEntity38).filter(ResearchModelEntity38.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity38]:
        return self.db.query(ResearchModelEntity38).filter(ResearchModelEntity38.entity_code == code).first()

class ResearchRepository39:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity39]:
        return self.db.query(ResearchModelEntity39).filter(ResearchModelEntity39.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity39]:
        return self.db.query(ResearchModelEntity39).filter(ResearchModelEntity39.entity_code == code).first()

class ResearchRepository40:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity40]:
        return self.db.query(ResearchModelEntity40).filter(ResearchModelEntity40.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity40]:
        return self.db.query(ResearchModelEntity40).filter(ResearchModelEntity40.entity_code == code).first()

class ResearchRepository41:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity41]:
        return self.db.query(ResearchModelEntity41).filter(ResearchModelEntity41.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity41]:
        return self.db.query(ResearchModelEntity41).filter(ResearchModelEntity41.entity_code == code).first()

class ResearchRepository42:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity42]:
        return self.db.query(ResearchModelEntity42).filter(ResearchModelEntity42.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity42]:
        return self.db.query(ResearchModelEntity42).filter(ResearchModelEntity42.entity_code == code).first()

class ResearchRepository43:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity43]:
        return self.db.query(ResearchModelEntity43).filter(ResearchModelEntity43.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity43]:
        return self.db.query(ResearchModelEntity43).filter(ResearchModelEntity43.entity_code == code).first()

class ResearchRepository44:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity44]:
        return self.db.query(ResearchModelEntity44).filter(ResearchModelEntity44.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity44]:
        return self.db.query(ResearchModelEntity44).filter(ResearchModelEntity44.entity_code == code).first()

class ResearchRepository45:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity45]:
        return self.db.query(ResearchModelEntity45).filter(ResearchModelEntity45.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity45]:
        return self.db.query(ResearchModelEntity45).filter(ResearchModelEntity45.entity_code == code).first()

class ResearchRepository46:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity46]:
        return self.db.query(ResearchModelEntity46).filter(ResearchModelEntity46.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity46]:
        return self.db.query(ResearchModelEntity46).filter(ResearchModelEntity46.entity_code == code).first()

class ResearchRepository47:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity47]:
        return self.db.query(ResearchModelEntity47).filter(ResearchModelEntity47.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity47]:
        return self.db.query(ResearchModelEntity47).filter(ResearchModelEntity47.entity_code == code).first()

class ResearchRepository48:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity48]:
        return self.db.query(ResearchModelEntity48).filter(ResearchModelEntity48.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity48]:
        return self.db.query(ResearchModelEntity48).filter(ResearchModelEntity48.entity_code == code).first()

class ResearchRepository49:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity49]:
        return self.db.query(ResearchModelEntity49).filter(ResearchModelEntity49.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity49]:
        return self.db.query(ResearchModelEntity49).filter(ResearchModelEntity49.entity_code == code).first()

class ResearchRepository50:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity50]:
        return self.db.query(ResearchModelEntity50).filter(ResearchModelEntity50.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity50]:
        return self.db.query(ResearchModelEntity50).filter(ResearchModelEntity50.entity_code == code).first()

class ResearchRepository51:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity51]:
        return self.db.query(ResearchModelEntity51).filter(ResearchModelEntity51.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity51]:
        return self.db.query(ResearchModelEntity51).filter(ResearchModelEntity51.entity_code == code).first()

class ResearchRepository52:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity52]:
        return self.db.query(ResearchModelEntity52).filter(ResearchModelEntity52.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity52]:
        return self.db.query(ResearchModelEntity52).filter(ResearchModelEntity52.entity_code == code).first()

class ResearchRepository53:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity53]:
        return self.db.query(ResearchModelEntity53).filter(ResearchModelEntity53.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity53]:
        return self.db.query(ResearchModelEntity53).filter(ResearchModelEntity53.entity_code == code).first()

class ResearchRepository54:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity54]:
        return self.db.query(ResearchModelEntity54).filter(ResearchModelEntity54.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity54]:
        return self.db.query(ResearchModelEntity54).filter(ResearchModelEntity54.entity_code == code).first()

class ResearchRepository55:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity55]:
        return self.db.query(ResearchModelEntity55).filter(ResearchModelEntity55.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity55]:
        return self.db.query(ResearchModelEntity55).filter(ResearchModelEntity55.entity_code == code).first()

class ResearchRepository56:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity56]:
        return self.db.query(ResearchModelEntity56).filter(ResearchModelEntity56.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity56]:
        return self.db.query(ResearchModelEntity56).filter(ResearchModelEntity56.entity_code == code).first()

class ResearchRepository57:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity57]:
        return self.db.query(ResearchModelEntity57).filter(ResearchModelEntity57.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity57]:
        return self.db.query(ResearchModelEntity57).filter(ResearchModelEntity57.entity_code == code).first()

class ResearchRepository58:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity58]:
        return self.db.query(ResearchModelEntity58).filter(ResearchModelEntity58.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity58]:
        return self.db.query(ResearchModelEntity58).filter(ResearchModelEntity58.entity_code == code).first()

class ResearchRepository59:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity59]:
        return self.db.query(ResearchModelEntity59).filter(ResearchModelEntity59.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity59]:
        return self.db.query(ResearchModelEntity59).filter(ResearchModelEntity59.entity_code == code).first()

class ResearchRepository60:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity60]:
        return self.db.query(ResearchModelEntity60).filter(ResearchModelEntity60.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity60]:
        return self.db.query(ResearchModelEntity60).filter(ResearchModelEntity60.entity_code == code).first()

class ResearchRepository61:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity61]:
        return self.db.query(ResearchModelEntity61).filter(ResearchModelEntity61.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity61]:
        return self.db.query(ResearchModelEntity61).filter(ResearchModelEntity61.entity_code == code).first()

class ResearchRepository62:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity62]:
        return self.db.query(ResearchModelEntity62).filter(ResearchModelEntity62.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity62]:
        return self.db.query(ResearchModelEntity62).filter(ResearchModelEntity62.entity_code == code).first()

class ResearchRepository63:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity63]:
        return self.db.query(ResearchModelEntity63).filter(ResearchModelEntity63.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity63]:
        return self.db.query(ResearchModelEntity63).filter(ResearchModelEntity63.entity_code == code).first()

class ResearchRepository64:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity64]:
        return self.db.query(ResearchModelEntity64).filter(ResearchModelEntity64.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity64]:
        return self.db.query(ResearchModelEntity64).filter(ResearchModelEntity64.entity_code == code).first()

class ResearchRepository65:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity65]:
        return self.db.query(ResearchModelEntity65).filter(ResearchModelEntity65.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity65]:
        return self.db.query(ResearchModelEntity65).filter(ResearchModelEntity65.entity_code == code).first()

class ResearchRepository66:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity66]:
        return self.db.query(ResearchModelEntity66).filter(ResearchModelEntity66.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity66]:
        return self.db.query(ResearchModelEntity66).filter(ResearchModelEntity66.entity_code == code).first()

class ResearchRepository67:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity67]:
        return self.db.query(ResearchModelEntity67).filter(ResearchModelEntity67.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity67]:
        return self.db.query(ResearchModelEntity67).filter(ResearchModelEntity67.entity_code == code).first()

class ResearchRepository68:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity68]:
        return self.db.query(ResearchModelEntity68).filter(ResearchModelEntity68.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity68]:
        return self.db.query(ResearchModelEntity68).filter(ResearchModelEntity68.entity_code == code).first()

class ResearchRepository69:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity69]:
        return self.db.query(ResearchModelEntity69).filter(ResearchModelEntity69.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity69]:
        return self.db.query(ResearchModelEntity69).filter(ResearchModelEntity69.entity_code == code).first()

class ResearchRepository70:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity70]:
        return self.db.query(ResearchModelEntity70).filter(ResearchModelEntity70.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity70]:
        return self.db.query(ResearchModelEntity70).filter(ResearchModelEntity70.entity_code == code).first()

class ResearchRepository71:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity71]:
        return self.db.query(ResearchModelEntity71).filter(ResearchModelEntity71.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity71]:
        return self.db.query(ResearchModelEntity71).filter(ResearchModelEntity71.entity_code == code).first()

class ResearchRepository72:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity72]:
        return self.db.query(ResearchModelEntity72).filter(ResearchModelEntity72.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity72]:
        return self.db.query(ResearchModelEntity72).filter(ResearchModelEntity72.entity_code == code).first()

class ResearchRepository73:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity73]:
        return self.db.query(ResearchModelEntity73).filter(ResearchModelEntity73.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity73]:
        return self.db.query(ResearchModelEntity73).filter(ResearchModelEntity73.entity_code == code).first()

class ResearchRepository74:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity74]:
        return self.db.query(ResearchModelEntity74).filter(ResearchModelEntity74.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity74]:
        return self.db.query(ResearchModelEntity74).filter(ResearchModelEntity74.entity_code == code).first()

class ResearchRepository75:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity75]:
        return self.db.query(ResearchModelEntity75).filter(ResearchModelEntity75.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity75]:
        return self.db.query(ResearchModelEntity75).filter(ResearchModelEntity75.entity_code == code).first()

class ResearchRepository76:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity76]:
        return self.db.query(ResearchModelEntity76).filter(ResearchModelEntity76.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity76]:
        return self.db.query(ResearchModelEntity76).filter(ResearchModelEntity76.entity_code == code).first()

class ResearchRepository77:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity77]:
        return self.db.query(ResearchModelEntity77).filter(ResearchModelEntity77.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity77]:
        return self.db.query(ResearchModelEntity77).filter(ResearchModelEntity77.entity_code == code).first()

class ResearchRepository78:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity78]:
        return self.db.query(ResearchModelEntity78).filter(ResearchModelEntity78.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity78]:
        return self.db.query(ResearchModelEntity78).filter(ResearchModelEntity78.entity_code == code).first()

class ResearchRepository79:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity79]:
        return self.db.query(ResearchModelEntity79).filter(ResearchModelEntity79.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity79]:
        return self.db.query(ResearchModelEntity79).filter(ResearchModelEntity79.entity_code == code).first()

class ResearchRepository80:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity80]:
        return self.db.query(ResearchModelEntity80).filter(ResearchModelEntity80.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity80]:
        return self.db.query(ResearchModelEntity80).filter(ResearchModelEntity80.entity_code == code).first()

class ResearchRepository81:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity81]:
        return self.db.query(ResearchModelEntity81).filter(ResearchModelEntity81.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity81]:
        return self.db.query(ResearchModelEntity81).filter(ResearchModelEntity81.entity_code == code).first()

class ResearchRepository82:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity82]:
        return self.db.query(ResearchModelEntity82).filter(ResearchModelEntity82.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity82]:
        return self.db.query(ResearchModelEntity82).filter(ResearchModelEntity82.entity_code == code).first()

class ResearchRepository83:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity83]:
        return self.db.query(ResearchModelEntity83).filter(ResearchModelEntity83.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity83]:
        return self.db.query(ResearchModelEntity83).filter(ResearchModelEntity83.entity_code == code).first()

class ResearchRepository84:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity84]:
        return self.db.query(ResearchModelEntity84).filter(ResearchModelEntity84.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity84]:
        return self.db.query(ResearchModelEntity84).filter(ResearchModelEntity84.entity_code == code).first()

class ResearchRepository85:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity85]:
        return self.db.query(ResearchModelEntity85).filter(ResearchModelEntity85.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity85]:
        return self.db.query(ResearchModelEntity85).filter(ResearchModelEntity85.entity_code == code).first()

class ResearchRepository86:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity86]:
        return self.db.query(ResearchModelEntity86).filter(ResearchModelEntity86.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity86]:
        return self.db.query(ResearchModelEntity86).filter(ResearchModelEntity86.entity_code == code).first()

class ResearchRepository87:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity87]:
        return self.db.query(ResearchModelEntity87).filter(ResearchModelEntity87.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity87]:
        return self.db.query(ResearchModelEntity87).filter(ResearchModelEntity87.entity_code == code).first()

class ResearchRepository88:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity88]:
        return self.db.query(ResearchModelEntity88).filter(ResearchModelEntity88.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity88]:
        return self.db.query(ResearchModelEntity88).filter(ResearchModelEntity88.entity_code == code).first()

class ResearchRepository89:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity89]:
        return self.db.query(ResearchModelEntity89).filter(ResearchModelEntity89.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity89]:
        return self.db.query(ResearchModelEntity89).filter(ResearchModelEntity89.entity_code == code).first()

class ResearchRepository90:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity90]:
        return self.db.query(ResearchModelEntity90).filter(ResearchModelEntity90.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity90]:
        return self.db.query(ResearchModelEntity90).filter(ResearchModelEntity90.entity_code == code).first()

class ResearchRepository91:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity91]:
        return self.db.query(ResearchModelEntity91).filter(ResearchModelEntity91.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity91]:
        return self.db.query(ResearchModelEntity91).filter(ResearchModelEntity91.entity_code == code).first()

class ResearchRepository92:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity92]:
        return self.db.query(ResearchModelEntity92).filter(ResearchModelEntity92.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity92]:
        return self.db.query(ResearchModelEntity92).filter(ResearchModelEntity92.entity_code == code).first()

class ResearchRepository93:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity93]:
        return self.db.query(ResearchModelEntity93).filter(ResearchModelEntity93.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity93]:
        return self.db.query(ResearchModelEntity93).filter(ResearchModelEntity93.entity_code == code).first()

class ResearchRepository94:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity94]:
        return self.db.query(ResearchModelEntity94).filter(ResearchModelEntity94.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity94]:
        return self.db.query(ResearchModelEntity94).filter(ResearchModelEntity94.entity_code == code).first()

class ResearchRepository95:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity95]:
        return self.db.query(ResearchModelEntity95).filter(ResearchModelEntity95.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity95]:
        return self.db.query(ResearchModelEntity95).filter(ResearchModelEntity95.entity_code == code).first()

class ResearchRepository96:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity96]:
        return self.db.query(ResearchModelEntity96).filter(ResearchModelEntity96.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity96]:
        return self.db.query(ResearchModelEntity96).filter(ResearchModelEntity96.entity_code == code).first()

class ResearchRepository97:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity97]:
        return self.db.query(ResearchModelEntity97).filter(ResearchModelEntity97.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity97]:
        return self.db.query(ResearchModelEntity97).filter(ResearchModelEntity97.entity_code == code).first()

class ResearchRepository98:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity98]:
        return self.db.query(ResearchModelEntity98).filter(ResearchModelEntity98.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity98]:
        return self.db.query(ResearchModelEntity98).filter(ResearchModelEntity98.entity_code == code).first()

class ResearchRepository99:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity99]:
        return self.db.query(ResearchModelEntity99).filter(ResearchModelEntity99.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity99]:
        return self.db.query(ResearchModelEntity99).filter(ResearchModelEntity99.entity_code == code).first()

class ResearchRepository100:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity100]:
        return self.db.query(ResearchModelEntity100).filter(ResearchModelEntity100.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity100]:
        return self.db.query(ResearchModelEntity100).filter(ResearchModelEntity100.entity_code == code).first()

class ResearchRepository101:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity101]:
        return self.db.query(ResearchModelEntity101).filter(ResearchModelEntity101.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity101]:
        return self.db.query(ResearchModelEntity101).filter(ResearchModelEntity101.entity_code == code).first()

class ResearchRepository102:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity102]:
        return self.db.query(ResearchModelEntity102).filter(ResearchModelEntity102.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity102]:
        return self.db.query(ResearchModelEntity102).filter(ResearchModelEntity102.entity_code == code).first()

class ResearchRepository103:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity103]:
        return self.db.query(ResearchModelEntity103).filter(ResearchModelEntity103.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity103]:
        return self.db.query(ResearchModelEntity103).filter(ResearchModelEntity103.entity_code == code).first()

class ResearchRepository104:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity104]:
        return self.db.query(ResearchModelEntity104).filter(ResearchModelEntity104.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity104]:
        return self.db.query(ResearchModelEntity104).filter(ResearchModelEntity104.entity_code == code).first()

class ResearchRepository105:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity105]:
        return self.db.query(ResearchModelEntity105).filter(ResearchModelEntity105.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity105]:
        return self.db.query(ResearchModelEntity105).filter(ResearchModelEntity105.entity_code == code).first()

class ResearchRepository106:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity106]:
        return self.db.query(ResearchModelEntity106).filter(ResearchModelEntity106.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity106]:
        return self.db.query(ResearchModelEntity106).filter(ResearchModelEntity106.entity_code == code).first()

class ResearchRepository107:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity107]:
        return self.db.query(ResearchModelEntity107).filter(ResearchModelEntity107.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity107]:
        return self.db.query(ResearchModelEntity107).filter(ResearchModelEntity107.entity_code == code).first()

class ResearchRepository108:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity108]:
        return self.db.query(ResearchModelEntity108).filter(ResearchModelEntity108.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity108]:
        return self.db.query(ResearchModelEntity108).filter(ResearchModelEntity108.entity_code == code).first()

class ResearchRepository109:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity109]:
        return self.db.query(ResearchModelEntity109).filter(ResearchModelEntity109.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity109]:
        return self.db.query(ResearchModelEntity109).filter(ResearchModelEntity109.entity_code == code).first()

class ResearchRepository110:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity110]:
        return self.db.query(ResearchModelEntity110).filter(ResearchModelEntity110.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity110]:
        return self.db.query(ResearchModelEntity110).filter(ResearchModelEntity110.entity_code == code).first()

class ResearchRepository111:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity111]:
        return self.db.query(ResearchModelEntity111).filter(ResearchModelEntity111.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity111]:
        return self.db.query(ResearchModelEntity111).filter(ResearchModelEntity111.entity_code == code).first()

class ResearchRepository112:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity112]:
        return self.db.query(ResearchModelEntity112).filter(ResearchModelEntity112.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity112]:
        return self.db.query(ResearchModelEntity112).filter(ResearchModelEntity112.entity_code == code).first()

class ResearchRepository113:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity113]:
        return self.db.query(ResearchModelEntity113).filter(ResearchModelEntity113.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity113]:
        return self.db.query(ResearchModelEntity113).filter(ResearchModelEntity113.entity_code == code).first()

class ResearchRepository114:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity114]:
        return self.db.query(ResearchModelEntity114).filter(ResearchModelEntity114.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity114]:
        return self.db.query(ResearchModelEntity114).filter(ResearchModelEntity114.entity_code == code).first()

class ResearchRepository115:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity115]:
        return self.db.query(ResearchModelEntity115).filter(ResearchModelEntity115.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity115]:
        return self.db.query(ResearchModelEntity115).filter(ResearchModelEntity115.entity_code == code).first()

class ResearchRepository116:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity116]:
        return self.db.query(ResearchModelEntity116).filter(ResearchModelEntity116.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity116]:
        return self.db.query(ResearchModelEntity116).filter(ResearchModelEntity116.entity_code == code).first()

class ResearchRepository117:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity117]:
        return self.db.query(ResearchModelEntity117).filter(ResearchModelEntity117.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity117]:
        return self.db.query(ResearchModelEntity117).filter(ResearchModelEntity117.entity_code == code).first()

class ResearchRepository118:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity118]:
        return self.db.query(ResearchModelEntity118).filter(ResearchModelEntity118.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity118]:
        return self.db.query(ResearchModelEntity118).filter(ResearchModelEntity118.entity_code == code).first()

class ResearchRepository119:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity119]:
        return self.db.query(ResearchModelEntity119).filter(ResearchModelEntity119.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity119]:
        return self.db.query(ResearchModelEntity119).filter(ResearchModelEntity119.entity_code == code).first()

class ResearchRepository120:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[ResearchModelEntity120]:
        return self.db.query(ResearchModelEntity120).filter(ResearchModelEntity120.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[ResearchModelEntity120]:
        return self.db.query(ResearchModelEntity120).filter(ResearchModelEntity120.entity_code == code).first()

