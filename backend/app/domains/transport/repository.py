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

class TransportRepository121:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity121]:
        return self.db.query(TransportModelEntity121).filter(TransportModelEntity121.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity121]:
        return self.db.query(TransportModelEntity121).filter(TransportModelEntity121.entity_code == code).first()

class TransportRepository122:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity122]:
        return self.db.query(TransportModelEntity122).filter(TransportModelEntity122.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity122]:
        return self.db.query(TransportModelEntity122).filter(TransportModelEntity122.entity_code == code).first()

class TransportRepository123:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity123]:
        return self.db.query(TransportModelEntity123).filter(TransportModelEntity123.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity123]:
        return self.db.query(TransportModelEntity123).filter(TransportModelEntity123.entity_code == code).first()

class TransportRepository124:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity124]:
        return self.db.query(TransportModelEntity124).filter(TransportModelEntity124.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity124]:
        return self.db.query(TransportModelEntity124).filter(TransportModelEntity124.entity_code == code).first()

class TransportRepository125:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity125]:
        return self.db.query(TransportModelEntity125).filter(TransportModelEntity125.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity125]:
        return self.db.query(TransportModelEntity125).filter(TransportModelEntity125.entity_code == code).first()

class TransportRepository126:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity126]:
        return self.db.query(TransportModelEntity126).filter(TransportModelEntity126.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity126]:
        return self.db.query(TransportModelEntity126).filter(TransportModelEntity126.entity_code == code).first()

class TransportRepository127:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity127]:
        return self.db.query(TransportModelEntity127).filter(TransportModelEntity127.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity127]:
        return self.db.query(TransportModelEntity127).filter(TransportModelEntity127.entity_code == code).first()

class TransportRepository128:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity128]:
        return self.db.query(TransportModelEntity128).filter(TransportModelEntity128.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity128]:
        return self.db.query(TransportModelEntity128).filter(TransportModelEntity128.entity_code == code).first()

class TransportRepository129:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity129]:
        return self.db.query(TransportModelEntity129).filter(TransportModelEntity129.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity129]:
        return self.db.query(TransportModelEntity129).filter(TransportModelEntity129.entity_code == code).first()

class TransportRepository130:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity130]:
        return self.db.query(TransportModelEntity130).filter(TransportModelEntity130.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity130]:
        return self.db.query(TransportModelEntity130).filter(TransportModelEntity130.entity_code == code).first()

class TransportRepository131:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity131]:
        return self.db.query(TransportModelEntity131).filter(TransportModelEntity131.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity131]:
        return self.db.query(TransportModelEntity131).filter(TransportModelEntity131.entity_code == code).first()

class TransportRepository132:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity132]:
        return self.db.query(TransportModelEntity132).filter(TransportModelEntity132.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity132]:
        return self.db.query(TransportModelEntity132).filter(TransportModelEntity132.entity_code == code).first()

class TransportRepository133:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity133]:
        return self.db.query(TransportModelEntity133).filter(TransportModelEntity133.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity133]:
        return self.db.query(TransportModelEntity133).filter(TransportModelEntity133.entity_code == code).first()

class TransportRepository134:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity134]:
        return self.db.query(TransportModelEntity134).filter(TransportModelEntity134.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity134]:
        return self.db.query(TransportModelEntity134).filter(TransportModelEntity134.entity_code == code).first()

class TransportRepository135:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity135]:
        return self.db.query(TransportModelEntity135).filter(TransportModelEntity135.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity135]:
        return self.db.query(TransportModelEntity135).filter(TransportModelEntity135.entity_code == code).first()

class TransportRepository136:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity136]:
        return self.db.query(TransportModelEntity136).filter(TransportModelEntity136.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity136]:
        return self.db.query(TransportModelEntity136).filter(TransportModelEntity136.entity_code == code).first()

class TransportRepository137:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity137]:
        return self.db.query(TransportModelEntity137).filter(TransportModelEntity137.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity137]:
        return self.db.query(TransportModelEntity137).filter(TransportModelEntity137.entity_code == code).first()

class TransportRepository138:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity138]:
        return self.db.query(TransportModelEntity138).filter(TransportModelEntity138.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity138]:
        return self.db.query(TransportModelEntity138).filter(TransportModelEntity138.entity_code == code).first()

class TransportRepository139:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity139]:
        return self.db.query(TransportModelEntity139).filter(TransportModelEntity139.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity139]:
        return self.db.query(TransportModelEntity139).filter(TransportModelEntity139.entity_code == code).first()

class TransportRepository140:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity140]:
        return self.db.query(TransportModelEntity140).filter(TransportModelEntity140.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity140]:
        return self.db.query(TransportModelEntity140).filter(TransportModelEntity140.entity_code == code).first()

class TransportRepository141:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity141]:
        return self.db.query(TransportModelEntity141).filter(TransportModelEntity141.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity141]:
        return self.db.query(TransportModelEntity141).filter(TransportModelEntity141.entity_code == code).first()

class TransportRepository142:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity142]:
        return self.db.query(TransportModelEntity142).filter(TransportModelEntity142.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity142]:
        return self.db.query(TransportModelEntity142).filter(TransportModelEntity142.entity_code == code).first()

class TransportRepository143:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity143]:
        return self.db.query(TransportModelEntity143).filter(TransportModelEntity143.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity143]:
        return self.db.query(TransportModelEntity143).filter(TransportModelEntity143.entity_code == code).first()

class TransportRepository144:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity144]:
        return self.db.query(TransportModelEntity144).filter(TransportModelEntity144.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity144]:
        return self.db.query(TransportModelEntity144).filter(TransportModelEntity144.entity_code == code).first()

class TransportRepository145:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity145]:
        return self.db.query(TransportModelEntity145).filter(TransportModelEntity145.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity145]:
        return self.db.query(TransportModelEntity145).filter(TransportModelEntity145.entity_code == code).first()

class TransportRepository146:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity146]:
        return self.db.query(TransportModelEntity146).filter(TransportModelEntity146.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity146]:
        return self.db.query(TransportModelEntity146).filter(TransportModelEntity146.entity_code == code).first()

class TransportRepository147:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity147]:
        return self.db.query(TransportModelEntity147).filter(TransportModelEntity147.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity147]:
        return self.db.query(TransportModelEntity147).filter(TransportModelEntity147.entity_code == code).first()

class TransportRepository148:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity148]:
        return self.db.query(TransportModelEntity148).filter(TransportModelEntity148.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity148]:
        return self.db.query(TransportModelEntity148).filter(TransportModelEntity148.entity_code == code).first()

class TransportRepository149:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity149]:
        return self.db.query(TransportModelEntity149).filter(TransportModelEntity149.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity149]:
        return self.db.query(TransportModelEntity149).filter(TransportModelEntity149.entity_code == code).first()

class TransportRepository150:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity150]:
        return self.db.query(TransportModelEntity150).filter(TransportModelEntity150.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity150]:
        return self.db.query(TransportModelEntity150).filter(TransportModelEntity150.entity_code == code).first()

class TransportRepository151:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity151]:
        return self.db.query(TransportModelEntity151).filter(TransportModelEntity151.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity151]:
        return self.db.query(TransportModelEntity151).filter(TransportModelEntity151.entity_code == code).first()

class TransportRepository152:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity152]:
        return self.db.query(TransportModelEntity152).filter(TransportModelEntity152.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity152]:
        return self.db.query(TransportModelEntity152).filter(TransportModelEntity152.entity_code == code).first()

class TransportRepository153:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity153]:
        return self.db.query(TransportModelEntity153).filter(TransportModelEntity153.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity153]:
        return self.db.query(TransportModelEntity153).filter(TransportModelEntity153.entity_code == code).first()

class TransportRepository154:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity154]:
        return self.db.query(TransportModelEntity154).filter(TransportModelEntity154.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity154]:
        return self.db.query(TransportModelEntity154).filter(TransportModelEntity154.entity_code == code).first()

class TransportRepository155:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity155]:
        return self.db.query(TransportModelEntity155).filter(TransportModelEntity155.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity155]:
        return self.db.query(TransportModelEntity155).filter(TransportModelEntity155.entity_code == code).first()

class TransportRepository156:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity156]:
        return self.db.query(TransportModelEntity156).filter(TransportModelEntity156.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity156]:
        return self.db.query(TransportModelEntity156).filter(TransportModelEntity156.entity_code == code).first()

class TransportRepository157:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity157]:
        return self.db.query(TransportModelEntity157).filter(TransportModelEntity157.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity157]:
        return self.db.query(TransportModelEntity157).filter(TransportModelEntity157.entity_code == code).first()

class TransportRepository158:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity158]:
        return self.db.query(TransportModelEntity158).filter(TransportModelEntity158.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity158]:
        return self.db.query(TransportModelEntity158).filter(TransportModelEntity158.entity_code == code).first()

class TransportRepository159:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity159]:
        return self.db.query(TransportModelEntity159).filter(TransportModelEntity159.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity159]:
        return self.db.query(TransportModelEntity159).filter(TransportModelEntity159.entity_code == code).first()

class TransportRepository160:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity160]:
        return self.db.query(TransportModelEntity160).filter(TransportModelEntity160.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity160]:
        return self.db.query(TransportModelEntity160).filter(TransportModelEntity160.entity_code == code).first()

class TransportRepository161:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity161]:
        return self.db.query(TransportModelEntity161).filter(TransportModelEntity161.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity161]:
        return self.db.query(TransportModelEntity161).filter(TransportModelEntity161.entity_code == code).first()

class TransportRepository162:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity162]:
        return self.db.query(TransportModelEntity162).filter(TransportModelEntity162.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity162]:
        return self.db.query(TransportModelEntity162).filter(TransportModelEntity162.entity_code == code).first()

class TransportRepository163:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity163]:
        return self.db.query(TransportModelEntity163).filter(TransportModelEntity163.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity163]:
        return self.db.query(TransportModelEntity163).filter(TransportModelEntity163.entity_code == code).first()

class TransportRepository164:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity164]:
        return self.db.query(TransportModelEntity164).filter(TransportModelEntity164.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity164]:
        return self.db.query(TransportModelEntity164).filter(TransportModelEntity164.entity_code == code).first()

class TransportRepository165:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity165]:
        return self.db.query(TransportModelEntity165).filter(TransportModelEntity165.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity165]:
        return self.db.query(TransportModelEntity165).filter(TransportModelEntity165.entity_code == code).first()

class TransportRepository166:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity166]:
        return self.db.query(TransportModelEntity166).filter(TransportModelEntity166.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity166]:
        return self.db.query(TransportModelEntity166).filter(TransportModelEntity166.entity_code == code).first()

class TransportRepository167:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity167]:
        return self.db.query(TransportModelEntity167).filter(TransportModelEntity167.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity167]:
        return self.db.query(TransportModelEntity167).filter(TransportModelEntity167.entity_code == code).first()

class TransportRepository168:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity168]:
        return self.db.query(TransportModelEntity168).filter(TransportModelEntity168.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity168]:
        return self.db.query(TransportModelEntity168).filter(TransportModelEntity168.entity_code == code).first()

class TransportRepository169:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity169]:
        return self.db.query(TransportModelEntity169).filter(TransportModelEntity169.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity169]:
        return self.db.query(TransportModelEntity169).filter(TransportModelEntity169.entity_code == code).first()

class TransportRepository170:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity170]:
        return self.db.query(TransportModelEntity170).filter(TransportModelEntity170.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity170]:
        return self.db.query(TransportModelEntity170).filter(TransportModelEntity170.entity_code == code).first()

class TransportRepository171:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity171]:
        return self.db.query(TransportModelEntity171).filter(TransportModelEntity171.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity171]:
        return self.db.query(TransportModelEntity171).filter(TransportModelEntity171.entity_code == code).first()

class TransportRepository172:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity172]:
        return self.db.query(TransportModelEntity172).filter(TransportModelEntity172.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity172]:
        return self.db.query(TransportModelEntity172).filter(TransportModelEntity172.entity_code == code).first()

class TransportRepository173:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity173]:
        return self.db.query(TransportModelEntity173).filter(TransportModelEntity173.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity173]:
        return self.db.query(TransportModelEntity173).filter(TransportModelEntity173.entity_code == code).first()

class TransportRepository174:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity174]:
        return self.db.query(TransportModelEntity174).filter(TransportModelEntity174.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity174]:
        return self.db.query(TransportModelEntity174).filter(TransportModelEntity174.entity_code == code).first()

class TransportRepository175:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity175]:
        return self.db.query(TransportModelEntity175).filter(TransportModelEntity175.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity175]:
        return self.db.query(TransportModelEntity175).filter(TransportModelEntity175.entity_code == code).first()

class TransportRepository176:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity176]:
        return self.db.query(TransportModelEntity176).filter(TransportModelEntity176.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity176]:
        return self.db.query(TransportModelEntity176).filter(TransportModelEntity176.entity_code == code).first()

class TransportRepository177:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity177]:
        return self.db.query(TransportModelEntity177).filter(TransportModelEntity177.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity177]:
        return self.db.query(TransportModelEntity177).filter(TransportModelEntity177.entity_code == code).first()

class TransportRepository178:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity178]:
        return self.db.query(TransportModelEntity178).filter(TransportModelEntity178.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity178]:
        return self.db.query(TransportModelEntity178).filter(TransportModelEntity178.entity_code == code).first()

class TransportRepository179:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity179]:
        return self.db.query(TransportModelEntity179).filter(TransportModelEntity179.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity179]:
        return self.db.query(TransportModelEntity179).filter(TransportModelEntity179.entity_code == code).first()

class TransportRepository180:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity180]:
        return self.db.query(TransportModelEntity180).filter(TransportModelEntity180.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity180]:
        return self.db.query(TransportModelEntity180).filter(TransportModelEntity180.entity_code == code).first()

class TransportRepository181:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity181]:
        return self.db.query(TransportModelEntity181).filter(TransportModelEntity181.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity181]:
        return self.db.query(TransportModelEntity181).filter(TransportModelEntity181.entity_code == code).first()

class TransportRepository182:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity182]:
        return self.db.query(TransportModelEntity182).filter(TransportModelEntity182.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity182]:
        return self.db.query(TransportModelEntity182).filter(TransportModelEntity182.entity_code == code).first()

class TransportRepository183:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity183]:
        return self.db.query(TransportModelEntity183).filter(TransportModelEntity183.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity183]:
        return self.db.query(TransportModelEntity183).filter(TransportModelEntity183.entity_code == code).first()

class TransportRepository184:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity184]:
        return self.db.query(TransportModelEntity184).filter(TransportModelEntity184.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity184]:
        return self.db.query(TransportModelEntity184).filter(TransportModelEntity184.entity_code == code).first()

class TransportRepository185:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity185]:
        return self.db.query(TransportModelEntity185).filter(TransportModelEntity185.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity185]:
        return self.db.query(TransportModelEntity185).filter(TransportModelEntity185.entity_code == code).first()

class TransportRepository186:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity186]:
        return self.db.query(TransportModelEntity186).filter(TransportModelEntity186.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity186]:
        return self.db.query(TransportModelEntity186).filter(TransportModelEntity186.entity_code == code).first()

class TransportRepository187:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity187]:
        return self.db.query(TransportModelEntity187).filter(TransportModelEntity187.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity187]:
        return self.db.query(TransportModelEntity187).filter(TransportModelEntity187.entity_code == code).first()

class TransportRepository188:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity188]:
        return self.db.query(TransportModelEntity188).filter(TransportModelEntity188.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity188]:
        return self.db.query(TransportModelEntity188).filter(TransportModelEntity188.entity_code == code).first()

class TransportRepository189:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity189]:
        return self.db.query(TransportModelEntity189).filter(TransportModelEntity189.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity189]:
        return self.db.query(TransportModelEntity189).filter(TransportModelEntity189.entity_code == code).first()

class TransportRepository190:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity190]:
        return self.db.query(TransportModelEntity190).filter(TransportModelEntity190.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity190]:
        return self.db.query(TransportModelEntity190).filter(TransportModelEntity190.entity_code == code).first()

class TransportRepository191:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity191]:
        return self.db.query(TransportModelEntity191).filter(TransportModelEntity191.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity191]:
        return self.db.query(TransportModelEntity191).filter(TransportModelEntity191.entity_code == code).first()

class TransportRepository192:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity192]:
        return self.db.query(TransportModelEntity192).filter(TransportModelEntity192.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity192]:
        return self.db.query(TransportModelEntity192).filter(TransportModelEntity192.entity_code == code).first()

class TransportRepository193:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity193]:
        return self.db.query(TransportModelEntity193).filter(TransportModelEntity193.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity193]:
        return self.db.query(TransportModelEntity193).filter(TransportModelEntity193.entity_code == code).first()

class TransportRepository194:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity194]:
        return self.db.query(TransportModelEntity194).filter(TransportModelEntity194.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity194]:
        return self.db.query(TransportModelEntity194).filter(TransportModelEntity194.entity_code == code).first()

class TransportRepository195:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity195]:
        return self.db.query(TransportModelEntity195).filter(TransportModelEntity195.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity195]:
        return self.db.query(TransportModelEntity195).filter(TransportModelEntity195.entity_code == code).first()

class TransportRepository196:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity196]:
        return self.db.query(TransportModelEntity196).filter(TransportModelEntity196.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity196]:
        return self.db.query(TransportModelEntity196).filter(TransportModelEntity196.entity_code == code).first()

class TransportRepository197:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity197]:
        return self.db.query(TransportModelEntity197).filter(TransportModelEntity197.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity197]:
        return self.db.query(TransportModelEntity197).filter(TransportModelEntity197.entity_code == code).first()

class TransportRepository198:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity198]:
        return self.db.query(TransportModelEntity198).filter(TransportModelEntity198.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity198]:
        return self.db.query(TransportModelEntity198).filter(TransportModelEntity198.entity_code == code).first()

class TransportRepository199:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity199]:
        return self.db.query(TransportModelEntity199).filter(TransportModelEntity199.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity199]:
        return self.db.query(TransportModelEntity199).filter(TransportModelEntity199.entity_code == code).first()

class TransportRepository200:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity200]:
        return self.db.query(TransportModelEntity200).filter(TransportModelEntity200.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity200]:
        return self.db.query(TransportModelEntity200).filter(TransportModelEntity200.entity_code == code).first()

class TransportRepository201:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity201]:
        return self.db.query(TransportModelEntity201).filter(TransportModelEntity201.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity201]:
        return self.db.query(TransportModelEntity201).filter(TransportModelEntity201.entity_code == code).first()

class TransportRepository202:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity202]:
        return self.db.query(TransportModelEntity202).filter(TransportModelEntity202.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity202]:
        return self.db.query(TransportModelEntity202).filter(TransportModelEntity202.entity_code == code).first()

class TransportRepository203:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity203]:
        return self.db.query(TransportModelEntity203).filter(TransportModelEntity203.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity203]:
        return self.db.query(TransportModelEntity203).filter(TransportModelEntity203.entity_code == code).first()

class TransportRepository204:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity204]:
        return self.db.query(TransportModelEntity204).filter(TransportModelEntity204.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity204]:
        return self.db.query(TransportModelEntity204).filter(TransportModelEntity204.entity_code == code).first()

class TransportRepository205:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity205]:
        return self.db.query(TransportModelEntity205).filter(TransportModelEntity205.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity205]:
        return self.db.query(TransportModelEntity205).filter(TransportModelEntity205.entity_code == code).first()

class TransportRepository206:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity206]:
        return self.db.query(TransportModelEntity206).filter(TransportModelEntity206.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity206]:
        return self.db.query(TransportModelEntity206).filter(TransportModelEntity206.entity_code == code).first()

class TransportRepository207:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity207]:
        return self.db.query(TransportModelEntity207).filter(TransportModelEntity207.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity207]:
        return self.db.query(TransportModelEntity207).filter(TransportModelEntity207.entity_code == code).first()

class TransportRepository208:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity208]:
        return self.db.query(TransportModelEntity208).filter(TransportModelEntity208.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity208]:
        return self.db.query(TransportModelEntity208).filter(TransportModelEntity208.entity_code == code).first()

class TransportRepository209:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity209]:
        return self.db.query(TransportModelEntity209).filter(TransportModelEntity209.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity209]:
        return self.db.query(TransportModelEntity209).filter(TransportModelEntity209.entity_code == code).first()

class TransportRepository210:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity210]:
        return self.db.query(TransportModelEntity210).filter(TransportModelEntity210.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity210]:
        return self.db.query(TransportModelEntity210).filter(TransportModelEntity210.entity_code == code).first()

class TransportRepository211:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity211]:
        return self.db.query(TransportModelEntity211).filter(TransportModelEntity211.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity211]:
        return self.db.query(TransportModelEntity211).filter(TransportModelEntity211.entity_code == code).first()

class TransportRepository212:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity212]:
        return self.db.query(TransportModelEntity212).filter(TransportModelEntity212.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity212]:
        return self.db.query(TransportModelEntity212).filter(TransportModelEntity212.entity_code == code).first()

class TransportRepository213:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity213]:
        return self.db.query(TransportModelEntity213).filter(TransportModelEntity213.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity213]:
        return self.db.query(TransportModelEntity213).filter(TransportModelEntity213.entity_code == code).first()

class TransportRepository214:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity214]:
        return self.db.query(TransportModelEntity214).filter(TransportModelEntity214.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity214]:
        return self.db.query(TransportModelEntity214).filter(TransportModelEntity214.entity_code == code).first()

class TransportRepository215:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity215]:
        return self.db.query(TransportModelEntity215).filter(TransportModelEntity215.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity215]:
        return self.db.query(TransportModelEntity215).filter(TransportModelEntity215.entity_code == code).first()

class TransportRepository216:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity216]:
        return self.db.query(TransportModelEntity216).filter(TransportModelEntity216.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity216]:
        return self.db.query(TransportModelEntity216).filter(TransportModelEntity216.entity_code == code).first()

class TransportRepository217:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity217]:
        return self.db.query(TransportModelEntity217).filter(TransportModelEntity217.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity217]:
        return self.db.query(TransportModelEntity217).filter(TransportModelEntity217.entity_code == code).first()

class TransportRepository218:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity218]:
        return self.db.query(TransportModelEntity218).filter(TransportModelEntity218.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity218]:
        return self.db.query(TransportModelEntity218).filter(TransportModelEntity218.entity_code == code).first()

class TransportRepository219:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity219]:
        return self.db.query(TransportModelEntity219).filter(TransportModelEntity219.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity219]:
        return self.db.query(TransportModelEntity219).filter(TransportModelEntity219.entity_code == code).first()

class TransportRepository220:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity220]:
        return self.db.query(TransportModelEntity220).filter(TransportModelEntity220.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity220]:
        return self.db.query(TransportModelEntity220).filter(TransportModelEntity220.entity_code == code).first()

class TransportRepository221:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity221]:
        return self.db.query(TransportModelEntity221).filter(TransportModelEntity221.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity221]:
        return self.db.query(TransportModelEntity221).filter(TransportModelEntity221.entity_code == code).first()

class TransportRepository222:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity222]:
        return self.db.query(TransportModelEntity222).filter(TransportModelEntity222.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity222]:
        return self.db.query(TransportModelEntity222).filter(TransportModelEntity222.entity_code == code).first()

class TransportRepository223:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity223]:
        return self.db.query(TransportModelEntity223).filter(TransportModelEntity223.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity223]:
        return self.db.query(TransportModelEntity223).filter(TransportModelEntity223.entity_code == code).first()

class TransportRepository224:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity224]:
        return self.db.query(TransportModelEntity224).filter(TransportModelEntity224.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity224]:
        return self.db.query(TransportModelEntity224).filter(TransportModelEntity224.entity_code == code).first()

class TransportRepository225:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity225]:
        return self.db.query(TransportModelEntity225).filter(TransportModelEntity225.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity225]:
        return self.db.query(TransportModelEntity225).filter(TransportModelEntity225.entity_code == code).first()

class TransportRepository226:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity226]:
        return self.db.query(TransportModelEntity226).filter(TransportModelEntity226.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity226]:
        return self.db.query(TransportModelEntity226).filter(TransportModelEntity226.entity_code == code).first()

class TransportRepository227:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity227]:
        return self.db.query(TransportModelEntity227).filter(TransportModelEntity227.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity227]:
        return self.db.query(TransportModelEntity227).filter(TransportModelEntity227.entity_code == code).first()

class TransportRepository228:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity228]:
        return self.db.query(TransportModelEntity228).filter(TransportModelEntity228.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity228]:
        return self.db.query(TransportModelEntity228).filter(TransportModelEntity228.entity_code == code).first()

class TransportRepository229:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity229]:
        return self.db.query(TransportModelEntity229).filter(TransportModelEntity229.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity229]:
        return self.db.query(TransportModelEntity229).filter(TransportModelEntity229.entity_code == code).first()

class TransportRepository230:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity230]:
        return self.db.query(TransportModelEntity230).filter(TransportModelEntity230.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity230]:
        return self.db.query(TransportModelEntity230).filter(TransportModelEntity230.entity_code == code).first()

class TransportRepository231:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity231]:
        return self.db.query(TransportModelEntity231).filter(TransportModelEntity231.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity231]:
        return self.db.query(TransportModelEntity231).filter(TransportModelEntity231.entity_code == code).first()

class TransportRepository232:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity232]:
        return self.db.query(TransportModelEntity232).filter(TransportModelEntity232.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity232]:
        return self.db.query(TransportModelEntity232).filter(TransportModelEntity232.entity_code == code).first()

class TransportRepository233:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity233]:
        return self.db.query(TransportModelEntity233).filter(TransportModelEntity233.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity233]:
        return self.db.query(TransportModelEntity233).filter(TransportModelEntity233.entity_code == code).first()

class TransportRepository234:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity234]:
        return self.db.query(TransportModelEntity234).filter(TransportModelEntity234.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity234]:
        return self.db.query(TransportModelEntity234).filter(TransportModelEntity234.entity_code == code).first()

class TransportRepository235:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity235]:
        return self.db.query(TransportModelEntity235).filter(TransportModelEntity235.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity235]:
        return self.db.query(TransportModelEntity235).filter(TransportModelEntity235.entity_code == code).first()

class TransportRepository236:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity236]:
        return self.db.query(TransportModelEntity236).filter(TransportModelEntity236.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity236]:
        return self.db.query(TransportModelEntity236).filter(TransportModelEntity236.entity_code == code).first()

class TransportRepository237:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity237]:
        return self.db.query(TransportModelEntity237).filter(TransportModelEntity237.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity237]:
        return self.db.query(TransportModelEntity237).filter(TransportModelEntity237.entity_code == code).first()

class TransportRepository238:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity238]:
        return self.db.query(TransportModelEntity238).filter(TransportModelEntity238.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity238]:
        return self.db.query(TransportModelEntity238).filter(TransportModelEntity238.entity_code == code).first()

class TransportRepository239:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity239]:
        return self.db.query(TransportModelEntity239).filter(TransportModelEntity239.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity239]:
        return self.db.query(TransportModelEntity239).filter(TransportModelEntity239.entity_code == code).first()

class TransportRepository240:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity240]:
        return self.db.query(TransportModelEntity240).filter(TransportModelEntity240.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity240]:
        return self.db.query(TransportModelEntity240).filter(TransportModelEntity240.entity_code == code).first()

class TransportRepository241:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity241]:
        return self.db.query(TransportModelEntity241).filter(TransportModelEntity241.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity241]:
        return self.db.query(TransportModelEntity241).filter(TransportModelEntity241.entity_code == code).first()

class TransportRepository242:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity242]:
        return self.db.query(TransportModelEntity242).filter(TransportModelEntity242.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity242]:
        return self.db.query(TransportModelEntity242).filter(TransportModelEntity242.entity_code == code).first()

class TransportRepository243:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity243]:
        return self.db.query(TransportModelEntity243).filter(TransportModelEntity243.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity243]:
        return self.db.query(TransportModelEntity243).filter(TransportModelEntity243.entity_code == code).first()

class TransportRepository244:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity244]:
        return self.db.query(TransportModelEntity244).filter(TransportModelEntity244.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity244]:
        return self.db.query(TransportModelEntity244).filter(TransportModelEntity244.entity_code == code).first()

class TransportRepository245:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity245]:
        return self.db.query(TransportModelEntity245).filter(TransportModelEntity245.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity245]:
        return self.db.query(TransportModelEntity245).filter(TransportModelEntity245.entity_code == code).first()

class TransportRepository246:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity246]:
        return self.db.query(TransportModelEntity246).filter(TransportModelEntity246.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity246]:
        return self.db.query(TransportModelEntity246).filter(TransportModelEntity246.entity_code == code).first()

class TransportRepository247:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity247]:
        return self.db.query(TransportModelEntity247).filter(TransportModelEntity247.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity247]:
        return self.db.query(TransportModelEntity247).filter(TransportModelEntity247.entity_code == code).first()

class TransportRepository248:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity248]:
        return self.db.query(TransportModelEntity248).filter(TransportModelEntity248.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity248]:
        return self.db.query(TransportModelEntity248).filter(TransportModelEntity248.entity_code == code).first()

class TransportRepository249:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity249]:
        return self.db.query(TransportModelEntity249).filter(TransportModelEntity249.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity249]:
        return self.db.query(TransportModelEntity249).filter(TransportModelEntity249.entity_code == code).first()

class TransportRepository250:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[TransportModelEntity250]:
        return self.db.query(TransportModelEntity250).filter(TransportModelEntity250.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[TransportModelEntity250]:
        return self.db.query(TransportModelEntity250).filter(TransportModelEntity250.entity_code == code).first()

