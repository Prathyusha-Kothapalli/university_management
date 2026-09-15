"""
Transport & Fleet Logistics - Data Access Repository Layer
Module: app.domains.transport.repository
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domains.transport.models import *

class TransportRepository1:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity1]:
        return self.db.query(TransportModelEntity1).filter(TransportModelEntity1.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity1]:
        return self.db.query(TransportModelEntity1).filter(TransportModelEntity1.entity_code == code).first()

class TransportRepository2:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity2]:
        return self.db.query(TransportModelEntity2).filter(TransportModelEntity2.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity2]:
        return self.db.query(TransportModelEntity2).filter(TransportModelEntity2.entity_code == code).first()

class TransportRepository3:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity3]:
        return self.db.query(TransportModelEntity3).filter(TransportModelEntity3.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity3]:
        return self.db.query(TransportModelEntity3).filter(TransportModelEntity3.entity_code == code).first()

class TransportRepository4:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity4]:
        return self.db.query(TransportModelEntity4).filter(TransportModelEntity4.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity4]:
        return self.db.query(TransportModelEntity4).filter(TransportModelEntity4.entity_code == code).first()

class TransportRepository5:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity5]:
        return self.db.query(TransportModelEntity5).filter(TransportModelEntity5.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity5]:
        return self.db.query(TransportModelEntity5).filter(TransportModelEntity5.entity_code == code).first()

class TransportRepository6:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity6]:
        return self.db.query(TransportModelEntity6).filter(TransportModelEntity6.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity6]:
        return self.db.query(TransportModelEntity6).filter(TransportModelEntity6.entity_code == code).first()

class TransportRepository7:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity7]:
        return self.db.query(TransportModelEntity7).filter(TransportModelEntity7.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity7]:
        return self.db.query(TransportModelEntity7).filter(TransportModelEntity7.entity_code == code).first()

class TransportRepository8:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity8]:
        return self.db.query(TransportModelEntity8).filter(TransportModelEntity8.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity8]:
        return self.db.query(TransportModelEntity8).filter(TransportModelEntity8.entity_code == code).first()

class TransportRepository9:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity9]:
        return self.db.query(TransportModelEntity9).filter(TransportModelEntity9.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity9]:
        return self.db.query(TransportModelEntity9).filter(TransportModelEntity9.entity_code == code).first()

class TransportRepository10:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity10]:
        return self.db.query(TransportModelEntity10).filter(TransportModelEntity10.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity10]:
        return self.db.query(TransportModelEntity10).filter(TransportModelEntity10.entity_code == code).first()

class TransportRepository11:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity11]:
        return self.db.query(TransportModelEntity11).filter(TransportModelEntity11.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity11]:
        return self.db.query(TransportModelEntity11).filter(TransportModelEntity11.entity_code == code).first()

class TransportRepository12:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity12]:
        return self.db.query(TransportModelEntity12).filter(TransportModelEntity12.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity12]:
        return self.db.query(TransportModelEntity12).filter(TransportModelEntity12.entity_code == code).first()

class TransportRepository13:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity13]:
        return self.db.query(TransportModelEntity13).filter(TransportModelEntity13.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity13]:
        return self.db.query(TransportModelEntity13).filter(TransportModelEntity13.entity_code == code).first()

class TransportRepository14:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity14]:
        return self.db.query(TransportModelEntity14).filter(TransportModelEntity14.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity14]:
        return self.db.query(TransportModelEntity14).filter(TransportModelEntity14.entity_code == code).first()

class TransportRepository15:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity15]:
        return self.db.query(TransportModelEntity15).filter(TransportModelEntity15.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity15]:
        return self.db.query(TransportModelEntity15).filter(TransportModelEntity15.entity_code == code).first()

class TransportRepository16:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity16]:
        return self.db.query(TransportModelEntity16).filter(TransportModelEntity16.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity16]:
        return self.db.query(TransportModelEntity16).filter(TransportModelEntity16.entity_code == code).first()

class TransportRepository17:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity17]:
        return self.db.query(TransportModelEntity17).filter(TransportModelEntity17.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity17]:
        return self.db.query(TransportModelEntity17).filter(TransportModelEntity17.entity_code == code).first()

class TransportRepository18:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity18]:
        return self.db.query(TransportModelEntity18).filter(TransportModelEntity18.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity18]:
        return self.db.query(TransportModelEntity18).filter(TransportModelEntity18.entity_code == code).first()

class TransportRepository19:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity19]:
        return self.db.query(TransportModelEntity19).filter(TransportModelEntity19.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity19]:
        return self.db.query(TransportModelEntity19).filter(TransportModelEntity19.entity_code == code).first()

class TransportRepository20:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity20]:
        return self.db.query(TransportModelEntity20).filter(TransportModelEntity20.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity20]:
        return self.db.query(TransportModelEntity20).filter(TransportModelEntity20.entity_code == code).first()

class TransportRepository21:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity21]:
        return self.db.query(TransportModelEntity21).filter(TransportModelEntity21.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity21]:
        return self.db.query(TransportModelEntity21).filter(TransportModelEntity21.entity_code == code).first()

class TransportRepository22:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity22]:
        return self.db.query(TransportModelEntity22).filter(TransportModelEntity22.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity22]:
        return self.db.query(TransportModelEntity22).filter(TransportModelEntity22.entity_code == code).first()

class TransportRepository23:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity23]:
        return self.db.query(TransportModelEntity23).filter(TransportModelEntity23.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity23]:
        return self.db.query(TransportModelEntity23).filter(TransportModelEntity23.entity_code == code).first()

class TransportRepository24:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity24]:
        return self.db.query(TransportModelEntity24).filter(TransportModelEntity24.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity24]:
        return self.db.query(TransportModelEntity24).filter(TransportModelEntity24.entity_code == code).first()

class TransportRepository25:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity25]:
        return self.db.query(TransportModelEntity25).filter(TransportModelEntity25.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity25]:
        return self.db.query(TransportModelEntity25).filter(TransportModelEntity25.entity_code == code).first()

class TransportRepository26:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity26]:
        return self.db.query(TransportModelEntity26).filter(TransportModelEntity26.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity26]:
        return self.db.query(TransportModelEntity26).filter(TransportModelEntity26.entity_code == code).first()

class TransportRepository27:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity27]:
        return self.db.query(TransportModelEntity27).filter(TransportModelEntity27.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity27]:
        return self.db.query(TransportModelEntity27).filter(TransportModelEntity27.entity_code == code).first()

class TransportRepository28:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity28]:
        return self.db.query(TransportModelEntity28).filter(TransportModelEntity28.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity28]:
        return self.db.query(TransportModelEntity28).filter(TransportModelEntity28.entity_code == code).first()

class TransportRepository29:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity29]:
        return self.db.query(TransportModelEntity29).filter(TransportModelEntity29.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity29]:
        return self.db.query(TransportModelEntity29).filter(TransportModelEntity29.entity_code == code).first()

class TransportRepository30:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity30]:
        return self.db.query(TransportModelEntity30).filter(TransportModelEntity30.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity30]:
        return self.db.query(TransportModelEntity30).filter(TransportModelEntity30.entity_code == code).first()

class TransportRepository31:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity31]:
        return self.db.query(TransportModelEntity31).filter(TransportModelEntity31.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity31]:
        return self.db.query(TransportModelEntity31).filter(TransportModelEntity31.entity_code == code).first()

class TransportRepository32:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity32]:
        return self.db.query(TransportModelEntity32).filter(TransportModelEntity32.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity32]:
        return self.db.query(TransportModelEntity32).filter(TransportModelEntity32.entity_code == code).first()

class TransportRepository33:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity33]:
        return self.db.query(TransportModelEntity33).filter(TransportModelEntity33.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity33]:
        return self.db.query(TransportModelEntity33).filter(TransportModelEntity33.entity_code == code).first()

class TransportRepository34:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity34]:
        return self.db.query(TransportModelEntity34).filter(TransportModelEntity34.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity34]:
        return self.db.query(TransportModelEntity34).filter(TransportModelEntity34.entity_code == code).first()

class TransportRepository35:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity35]:
        return self.db.query(TransportModelEntity35).filter(TransportModelEntity35.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity35]:
        return self.db.query(TransportModelEntity35).filter(TransportModelEntity35.entity_code == code).first()

class TransportRepository36:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity36]:
        return self.db.query(TransportModelEntity36).filter(TransportModelEntity36.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity36]:
        return self.db.query(TransportModelEntity36).filter(TransportModelEntity36.entity_code == code).first()

class TransportRepository37:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity37]:
        return self.db.query(TransportModelEntity37).filter(TransportModelEntity37.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity37]:
        return self.db.query(TransportModelEntity37).filter(TransportModelEntity37.entity_code == code).first()

class TransportRepository38:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity38]:
        return self.db.query(TransportModelEntity38).filter(TransportModelEntity38.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity38]:
        return self.db.query(TransportModelEntity38).filter(TransportModelEntity38.entity_code == code).first()

class TransportRepository39:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity39]:
        return self.db.query(TransportModelEntity39).filter(TransportModelEntity39.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity39]:
        return self.db.query(TransportModelEntity39).filter(TransportModelEntity39.entity_code == code).first()

class TransportRepository40:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity40]:
        return self.db.query(TransportModelEntity40).filter(TransportModelEntity40.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity40]:
        return self.db.query(TransportModelEntity40).filter(TransportModelEntity40.entity_code == code).first()

class TransportRepository41:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity41]:
        return self.db.query(TransportModelEntity41).filter(TransportModelEntity41.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity41]:
        return self.db.query(TransportModelEntity41).filter(TransportModelEntity41.entity_code == code).first()

class TransportRepository42:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity42]:
        return self.db.query(TransportModelEntity42).filter(TransportModelEntity42.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity42]:
        return self.db.query(TransportModelEntity42).filter(TransportModelEntity42.entity_code == code).first()

class TransportRepository43:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity43]:
        return self.db.query(TransportModelEntity43).filter(TransportModelEntity43.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity43]:
        return self.db.query(TransportModelEntity43).filter(TransportModelEntity43.entity_code == code).first()

class TransportRepository44:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity44]:
        return self.db.query(TransportModelEntity44).filter(TransportModelEntity44.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity44]:
        return self.db.query(TransportModelEntity44).filter(TransportModelEntity44.entity_code == code).first()

class TransportRepository45:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity45]:
        return self.db.query(TransportModelEntity45).filter(TransportModelEntity45.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity45]:
        return self.db.query(TransportModelEntity45).filter(TransportModelEntity45.entity_code == code).first()

class TransportRepository46:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity46]:
        return self.db.query(TransportModelEntity46).filter(TransportModelEntity46.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity46]:
        return self.db.query(TransportModelEntity46).filter(TransportModelEntity46.entity_code == code).first()

class TransportRepository47:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity47]:
        return self.db.query(TransportModelEntity47).filter(TransportModelEntity47.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity47]:
        return self.db.query(TransportModelEntity47).filter(TransportModelEntity47.entity_code == code).first()

class TransportRepository48:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity48]:
        return self.db.query(TransportModelEntity48).filter(TransportModelEntity48.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity48]:
        return self.db.query(TransportModelEntity48).filter(TransportModelEntity48.entity_code == code).first()

class TransportRepository49:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity49]:
        return self.db.query(TransportModelEntity49).filter(TransportModelEntity49.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity49]:
        return self.db.query(TransportModelEntity49).filter(TransportModelEntity49.entity_code == code).first()

class TransportRepository50:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity50]:
        return self.db.query(TransportModelEntity50).filter(TransportModelEntity50.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity50]:
        return self.db.query(TransportModelEntity50).filter(TransportModelEntity50.entity_code == code).first()

class TransportRepository51:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity51]:
        return self.db.query(TransportModelEntity51).filter(TransportModelEntity51.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity51]:
        return self.db.query(TransportModelEntity51).filter(TransportModelEntity51.entity_code == code).first()

class TransportRepository52:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity52]:
        return self.db.query(TransportModelEntity52).filter(TransportModelEntity52.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity52]:
        return self.db.query(TransportModelEntity52).filter(TransportModelEntity52.entity_code == code).first()

class TransportRepository53:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity53]:
        return self.db.query(TransportModelEntity53).filter(TransportModelEntity53.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity53]:
        return self.db.query(TransportModelEntity53).filter(TransportModelEntity53.entity_code == code).first()

class TransportRepository54:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity54]:
        return self.db.query(TransportModelEntity54).filter(TransportModelEntity54.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity54]:
        return self.db.query(TransportModelEntity54).filter(TransportModelEntity54.entity_code == code).first()

class TransportRepository55:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity55]:
        return self.db.query(TransportModelEntity55).filter(TransportModelEntity55.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity55]:
        return self.db.query(TransportModelEntity55).filter(TransportModelEntity55.entity_code == code).first()

class TransportRepository56:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity56]:
        return self.db.query(TransportModelEntity56).filter(TransportModelEntity56.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity56]:
        return self.db.query(TransportModelEntity56).filter(TransportModelEntity56.entity_code == code).first()

class TransportRepository57:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity57]:
        return self.db.query(TransportModelEntity57).filter(TransportModelEntity57.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity57]:
        return self.db.query(TransportModelEntity57).filter(TransportModelEntity57.entity_code == code).first()

class TransportRepository58:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity58]:
        return self.db.query(TransportModelEntity58).filter(TransportModelEntity58.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity58]:
        return self.db.query(TransportModelEntity58).filter(TransportModelEntity58.entity_code == code).first()

class TransportRepository59:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity59]:
        return self.db.query(TransportModelEntity59).filter(TransportModelEntity59.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity59]:
        return self.db.query(TransportModelEntity59).filter(TransportModelEntity59.entity_code == code).first()

class TransportRepository60:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity60]:
        return self.db.query(TransportModelEntity60).filter(TransportModelEntity60.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity60]:
        return self.db.query(TransportModelEntity60).filter(TransportModelEntity60.entity_code == code).first()

class TransportRepository61:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity61]:
        return self.db.query(TransportModelEntity61).filter(TransportModelEntity61.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity61]:
        return self.db.query(TransportModelEntity61).filter(TransportModelEntity61.entity_code == code).first()

class TransportRepository62:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity62]:
        return self.db.query(TransportModelEntity62).filter(TransportModelEntity62.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity62]:
        return self.db.query(TransportModelEntity62).filter(TransportModelEntity62.entity_code == code).first()

class TransportRepository63:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity63]:
        return self.db.query(TransportModelEntity63).filter(TransportModelEntity63.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity63]:
        return self.db.query(TransportModelEntity63).filter(TransportModelEntity63.entity_code == code).first()

class TransportRepository64:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity64]:
        return self.db.query(TransportModelEntity64).filter(TransportModelEntity64.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity64]:
        return self.db.query(TransportModelEntity64).filter(TransportModelEntity64.entity_code == code).first()

class TransportRepository65:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity65]:
        return self.db.query(TransportModelEntity65).filter(TransportModelEntity65.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity65]:
        return self.db.query(TransportModelEntity65).filter(TransportModelEntity65.entity_code == code).first()

class TransportRepository66:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity66]:
        return self.db.query(TransportModelEntity66).filter(TransportModelEntity66.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity66]:
        return self.db.query(TransportModelEntity66).filter(TransportModelEntity66.entity_code == code).first()

class TransportRepository67:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity67]:
        return self.db.query(TransportModelEntity67).filter(TransportModelEntity67.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity67]:
        return self.db.query(TransportModelEntity67).filter(TransportModelEntity67.entity_code == code).first()

class TransportRepository68:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity68]:
        return self.db.query(TransportModelEntity68).filter(TransportModelEntity68.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity68]:
        return self.db.query(TransportModelEntity68).filter(TransportModelEntity68.entity_code == code).first()

class TransportRepository69:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity69]:
        return self.db.query(TransportModelEntity69).filter(TransportModelEntity69.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity69]:
        return self.db.query(TransportModelEntity69).filter(TransportModelEntity69.entity_code == code).first()

class TransportRepository70:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity70]:
        return self.db.query(TransportModelEntity70).filter(TransportModelEntity70.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity70]:
        return self.db.query(TransportModelEntity70).filter(TransportModelEntity70.entity_code == code).first()

class TransportRepository71:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity71]:
        return self.db.query(TransportModelEntity71).filter(TransportModelEntity71.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity71]:
        return self.db.query(TransportModelEntity71).filter(TransportModelEntity71.entity_code == code).first()

class TransportRepository72:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity72]:
        return self.db.query(TransportModelEntity72).filter(TransportModelEntity72.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity72]:
        return self.db.query(TransportModelEntity72).filter(TransportModelEntity72.entity_code == code).first()

class TransportRepository73:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity73]:
        return self.db.query(TransportModelEntity73).filter(TransportModelEntity73.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity73]:
        return self.db.query(TransportModelEntity73).filter(TransportModelEntity73.entity_code == code).first()

class TransportRepository74:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity74]:
        return self.db.query(TransportModelEntity74).filter(TransportModelEntity74.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity74]:
        return self.db.query(TransportModelEntity74).filter(TransportModelEntity74.entity_code == code).first()

class TransportRepository75:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity75]:
        return self.db.query(TransportModelEntity75).filter(TransportModelEntity75.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity75]:
        return self.db.query(TransportModelEntity75).filter(TransportModelEntity75.entity_code == code).first()

class TransportRepository76:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity76]:
        return self.db.query(TransportModelEntity76).filter(TransportModelEntity76.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity76]:
        return self.db.query(TransportModelEntity76).filter(TransportModelEntity76.entity_code == code).first()

class TransportRepository77:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity77]:
        return self.db.query(TransportModelEntity77).filter(TransportModelEntity77.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity77]:
        return self.db.query(TransportModelEntity77).filter(TransportModelEntity77.entity_code == code).first()

class TransportRepository78:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity78]:
        return self.db.query(TransportModelEntity78).filter(TransportModelEntity78.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity78]:
        return self.db.query(TransportModelEntity78).filter(TransportModelEntity78.entity_code == code).first()

class TransportRepository79:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity79]:
        return self.db.query(TransportModelEntity79).filter(TransportModelEntity79.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity79]:
        return self.db.query(TransportModelEntity79).filter(TransportModelEntity79.entity_code == code).first()

class TransportRepository80:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity80]:
        return self.db.query(TransportModelEntity80).filter(TransportModelEntity80.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity80]:
        return self.db.query(TransportModelEntity80).filter(TransportModelEntity80.entity_code == code).first()

class TransportRepository81:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity81]:
        return self.db.query(TransportModelEntity81).filter(TransportModelEntity81.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity81]:
        return self.db.query(TransportModelEntity81).filter(TransportModelEntity81.entity_code == code).first()

class TransportRepository82:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity82]:
        return self.db.query(TransportModelEntity82).filter(TransportModelEntity82.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity82]:
        return self.db.query(TransportModelEntity82).filter(TransportModelEntity82.entity_code == code).first()

class TransportRepository83:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity83]:
        return self.db.query(TransportModelEntity83).filter(TransportModelEntity83.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity83]:
        return self.db.query(TransportModelEntity83).filter(TransportModelEntity83.entity_code == code).first()

class TransportRepository84:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity84]:
        return self.db.query(TransportModelEntity84).filter(TransportModelEntity84.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity84]:
        return self.db.query(TransportModelEntity84).filter(TransportModelEntity84.entity_code == code).first()

class TransportRepository85:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity85]:
        return self.db.query(TransportModelEntity85).filter(TransportModelEntity85.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity85]:
        return self.db.query(TransportModelEntity85).filter(TransportModelEntity85.entity_code == code).first()

class TransportRepository86:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity86]:
        return self.db.query(TransportModelEntity86).filter(TransportModelEntity86.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity86]:
        return self.db.query(TransportModelEntity86).filter(TransportModelEntity86.entity_code == code).first()

class TransportRepository87:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity87]:
        return self.db.query(TransportModelEntity87).filter(TransportModelEntity87.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity87]:
        return self.db.query(TransportModelEntity87).filter(TransportModelEntity87.entity_code == code).first()

class TransportRepository88:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity88]:
        return self.db.query(TransportModelEntity88).filter(TransportModelEntity88.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity88]:
        return self.db.query(TransportModelEntity88).filter(TransportModelEntity88.entity_code == code).first()

class TransportRepository89:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity89]:
        return self.db.query(TransportModelEntity89).filter(TransportModelEntity89.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity89]:
        return self.db.query(TransportModelEntity89).filter(TransportModelEntity89.entity_code == code).first()

class TransportRepository90:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity90]:
        return self.db.query(TransportModelEntity90).filter(TransportModelEntity90.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity90]:
        return self.db.query(TransportModelEntity90).filter(TransportModelEntity90.entity_code == code).first()

class TransportRepository91:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity91]:
        return self.db.query(TransportModelEntity91).filter(TransportModelEntity91.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity91]:
        return self.db.query(TransportModelEntity91).filter(TransportModelEntity91.entity_code == code).first()

class TransportRepository92:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity92]:
        return self.db.query(TransportModelEntity92).filter(TransportModelEntity92.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity92]:
        return self.db.query(TransportModelEntity92).filter(TransportModelEntity92.entity_code == code).first()

class TransportRepository93:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity93]:
        return self.db.query(TransportModelEntity93).filter(TransportModelEntity93.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity93]:
        return self.db.query(TransportModelEntity93).filter(TransportModelEntity93.entity_code == code).first()

class TransportRepository94:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity94]:
        return self.db.query(TransportModelEntity94).filter(TransportModelEntity94.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity94]:
        return self.db.query(TransportModelEntity94).filter(TransportModelEntity94.entity_code == code).first()

class TransportRepository95:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity95]:
        return self.db.query(TransportModelEntity95).filter(TransportModelEntity95.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity95]:
        return self.db.query(TransportModelEntity95).filter(TransportModelEntity95.entity_code == code).first()

class TransportRepository96:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity96]:
        return self.db.query(TransportModelEntity96).filter(TransportModelEntity96.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity96]:
        return self.db.query(TransportModelEntity96).filter(TransportModelEntity96.entity_code == code).first()

class TransportRepository97:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity97]:
        return self.db.query(TransportModelEntity97).filter(TransportModelEntity97.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity97]:
        return self.db.query(TransportModelEntity97).filter(TransportModelEntity97.entity_code == code).first()

class TransportRepository98:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity98]:
        return self.db.query(TransportModelEntity98).filter(TransportModelEntity98.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity98]:
        return self.db.query(TransportModelEntity98).filter(TransportModelEntity98.entity_code == code).first()

class TransportRepository99:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity99]:
        return self.db.query(TransportModelEntity99).filter(TransportModelEntity99.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity99]:
        return self.db.query(TransportModelEntity99).filter(TransportModelEntity99.entity_code == code).first()

class TransportRepository100:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity100]:
        return self.db.query(TransportModelEntity100).filter(TransportModelEntity100.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity100]:
        return self.db.query(TransportModelEntity100).filter(TransportModelEntity100.entity_code == code).first()

class TransportRepository101:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity101]:
        return self.db.query(TransportModelEntity101).filter(TransportModelEntity101.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity101]:
        return self.db.query(TransportModelEntity101).filter(TransportModelEntity101.entity_code == code).first()

class TransportRepository102:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity102]:
        return self.db.query(TransportModelEntity102).filter(TransportModelEntity102.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity102]:
        return self.db.query(TransportModelEntity102).filter(TransportModelEntity102.entity_code == code).first()

class TransportRepository103:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity103]:
        return self.db.query(TransportModelEntity103).filter(TransportModelEntity103.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity103]:
        return self.db.query(TransportModelEntity103).filter(TransportModelEntity103.entity_code == code).first()

class TransportRepository104:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity104]:
        return self.db.query(TransportModelEntity104).filter(TransportModelEntity104.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity104]:
        return self.db.query(TransportModelEntity104).filter(TransportModelEntity104.entity_code == code).first()

class TransportRepository105:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity105]:
        return self.db.query(TransportModelEntity105).filter(TransportModelEntity105.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity105]:
        return self.db.query(TransportModelEntity105).filter(TransportModelEntity105.entity_code == code).first()

class TransportRepository106:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity106]:
        return self.db.query(TransportModelEntity106).filter(TransportModelEntity106.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity106]:
        return self.db.query(TransportModelEntity106).filter(TransportModelEntity106.entity_code == code).first()

class TransportRepository107:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity107]:
        return self.db.query(TransportModelEntity107).filter(TransportModelEntity107.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity107]:
        return self.db.query(TransportModelEntity107).filter(TransportModelEntity107.entity_code == code).first()

class TransportRepository108:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity108]:
        return self.db.query(TransportModelEntity108).filter(TransportModelEntity108.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity108]:
        return self.db.query(TransportModelEntity108).filter(TransportModelEntity108.entity_code == code).first()

class TransportRepository109:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity109]:
        return self.db.query(TransportModelEntity109).filter(TransportModelEntity109.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity109]:
        return self.db.query(TransportModelEntity109).filter(TransportModelEntity109.entity_code == code).first()

class TransportRepository110:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity110]:
        return self.db.query(TransportModelEntity110).filter(TransportModelEntity110.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity110]:
        return self.db.query(TransportModelEntity110).filter(TransportModelEntity110.entity_code == code).first()

class TransportRepository111:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity111]:
        return self.db.query(TransportModelEntity111).filter(TransportModelEntity111.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity111]:
        return self.db.query(TransportModelEntity111).filter(TransportModelEntity111.entity_code == code).first()

class TransportRepository112:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity112]:
        return self.db.query(TransportModelEntity112).filter(TransportModelEntity112.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity112]:
        return self.db.query(TransportModelEntity112).filter(TransportModelEntity112.entity_code == code).first()

class TransportRepository113:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity113]:
        return self.db.query(TransportModelEntity113).filter(TransportModelEntity113.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity113]:
        return self.db.query(TransportModelEntity113).filter(TransportModelEntity113.entity_code == code).first()

class TransportRepository114:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity114]:
        return self.db.query(TransportModelEntity114).filter(TransportModelEntity114.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity114]:
        return self.db.query(TransportModelEntity114).filter(TransportModelEntity114.entity_code == code).first()

class TransportRepository115:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity115]:
        return self.db.query(TransportModelEntity115).filter(TransportModelEntity115.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity115]:
        return self.db.query(TransportModelEntity115).filter(TransportModelEntity115.entity_code == code).first()

class TransportRepository116:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity116]:
        return self.db.query(TransportModelEntity116).filter(TransportModelEntity116.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity116]:
        return self.db.query(TransportModelEntity116).filter(TransportModelEntity116.entity_code == code).first()

class TransportRepository117:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity117]:
        return self.db.query(TransportModelEntity117).filter(TransportModelEntity117.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity117]:
        return self.db.query(TransportModelEntity117).filter(TransportModelEntity117.entity_code == code).first()

class TransportRepository118:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity118]:
        return self.db.query(TransportModelEntity118).filter(TransportModelEntity118.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity118]:
        return self.db.query(TransportModelEntity118).filter(TransportModelEntity118.entity_code == code).first()

class TransportRepository119:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity119]:
        return self.db.query(TransportModelEntity119).filter(TransportModelEntity119.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity119]:
        return self.db.query(TransportModelEntity119).filter(TransportModelEntity119.entity_code == code).first()

class TransportRepository120:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity120]:
        return self.db.query(TransportModelEntity120).filter(TransportModelEntity120.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity120]:
        return self.db.query(TransportModelEntity120).filter(TransportModelEntity120.entity_code == code).first()

