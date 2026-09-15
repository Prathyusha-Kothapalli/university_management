"""
Academic & Curriculum Management - Data Access Repository Layer
Module: app.domains.academics.repository
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domains.academics.models import *

class AcademicsRepository1:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity1]:
        return self.db.query(AcademicsModelEntity1).filter(AcademicsModelEntity1.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity1]:
        return self.db.query(AcademicsModelEntity1).filter(AcademicsModelEntity1.entity_code == code).first()

class AcademicsRepository2:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity2]:
        return self.db.query(AcademicsModelEntity2).filter(AcademicsModelEntity2.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity2]:
        return self.db.query(AcademicsModelEntity2).filter(AcademicsModelEntity2.entity_code == code).first()

class AcademicsRepository3:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity3]:
        return self.db.query(AcademicsModelEntity3).filter(AcademicsModelEntity3.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity3]:
        return self.db.query(AcademicsModelEntity3).filter(AcademicsModelEntity3.entity_code == code).first()

class AcademicsRepository4:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity4]:
        return self.db.query(AcademicsModelEntity4).filter(AcademicsModelEntity4.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity4]:
        return self.db.query(AcademicsModelEntity4).filter(AcademicsModelEntity4.entity_code == code).first()

class AcademicsRepository5:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity5]:
        return self.db.query(AcademicsModelEntity5).filter(AcademicsModelEntity5.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity5]:
        return self.db.query(AcademicsModelEntity5).filter(AcademicsModelEntity5.entity_code == code).first()

class AcademicsRepository6:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity6]:
        return self.db.query(AcademicsModelEntity6).filter(AcademicsModelEntity6.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity6]:
        return self.db.query(AcademicsModelEntity6).filter(AcademicsModelEntity6.entity_code == code).first()

class AcademicsRepository7:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity7]:
        return self.db.query(AcademicsModelEntity7).filter(AcademicsModelEntity7.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity7]:
        return self.db.query(AcademicsModelEntity7).filter(AcademicsModelEntity7.entity_code == code).first()

class AcademicsRepository8:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity8]:
        return self.db.query(AcademicsModelEntity8).filter(AcademicsModelEntity8.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity8]:
        return self.db.query(AcademicsModelEntity8).filter(AcademicsModelEntity8.entity_code == code).first()

class AcademicsRepository9:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity9]:
        return self.db.query(AcademicsModelEntity9).filter(AcademicsModelEntity9.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity9]:
        return self.db.query(AcademicsModelEntity9).filter(AcademicsModelEntity9.entity_code == code).first()

class AcademicsRepository10:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity10]:
        return self.db.query(AcademicsModelEntity10).filter(AcademicsModelEntity10.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity10]:
        return self.db.query(AcademicsModelEntity10).filter(AcademicsModelEntity10.entity_code == code).first()

class AcademicsRepository11:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity11]:
        return self.db.query(AcademicsModelEntity11).filter(AcademicsModelEntity11.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity11]:
        return self.db.query(AcademicsModelEntity11).filter(AcademicsModelEntity11.entity_code == code).first()

class AcademicsRepository12:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity12]:
        return self.db.query(AcademicsModelEntity12).filter(AcademicsModelEntity12.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity12]:
        return self.db.query(AcademicsModelEntity12).filter(AcademicsModelEntity12.entity_code == code).first()

class AcademicsRepository13:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity13]:
        return self.db.query(AcademicsModelEntity13).filter(AcademicsModelEntity13.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity13]:
        return self.db.query(AcademicsModelEntity13).filter(AcademicsModelEntity13.entity_code == code).first()

class AcademicsRepository14:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity14]:
        return self.db.query(AcademicsModelEntity14).filter(AcademicsModelEntity14.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity14]:
        return self.db.query(AcademicsModelEntity14).filter(AcademicsModelEntity14.entity_code == code).first()

class AcademicsRepository15:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity15]:
        return self.db.query(AcademicsModelEntity15).filter(AcademicsModelEntity15.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity15]:
        return self.db.query(AcademicsModelEntity15).filter(AcademicsModelEntity15.entity_code == code).first()

class AcademicsRepository16:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity16]:
        return self.db.query(AcademicsModelEntity16).filter(AcademicsModelEntity16.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity16]:
        return self.db.query(AcademicsModelEntity16).filter(AcademicsModelEntity16.entity_code == code).first()

class AcademicsRepository17:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity17]:
        return self.db.query(AcademicsModelEntity17).filter(AcademicsModelEntity17.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity17]:
        return self.db.query(AcademicsModelEntity17).filter(AcademicsModelEntity17.entity_code == code).first()

class AcademicsRepository18:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity18]:
        return self.db.query(AcademicsModelEntity18).filter(AcademicsModelEntity18.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity18]:
        return self.db.query(AcademicsModelEntity18).filter(AcademicsModelEntity18.entity_code == code).first()

class AcademicsRepository19:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity19]:
        return self.db.query(AcademicsModelEntity19).filter(AcademicsModelEntity19.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity19]:
        return self.db.query(AcademicsModelEntity19).filter(AcademicsModelEntity19.entity_code == code).first()

class AcademicsRepository20:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity20]:
        return self.db.query(AcademicsModelEntity20).filter(AcademicsModelEntity20.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity20]:
        return self.db.query(AcademicsModelEntity20).filter(AcademicsModelEntity20.entity_code == code).first()

class AcademicsRepository21:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity21]:
        return self.db.query(AcademicsModelEntity21).filter(AcademicsModelEntity21.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity21]:
        return self.db.query(AcademicsModelEntity21).filter(AcademicsModelEntity21.entity_code == code).first()

class AcademicsRepository22:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity22]:
        return self.db.query(AcademicsModelEntity22).filter(AcademicsModelEntity22.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity22]:
        return self.db.query(AcademicsModelEntity22).filter(AcademicsModelEntity22.entity_code == code).first()

class AcademicsRepository23:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity23]:
        return self.db.query(AcademicsModelEntity23).filter(AcademicsModelEntity23.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity23]:
        return self.db.query(AcademicsModelEntity23).filter(AcademicsModelEntity23.entity_code == code).first()

class AcademicsRepository24:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity24]:
        return self.db.query(AcademicsModelEntity24).filter(AcademicsModelEntity24.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity24]:
        return self.db.query(AcademicsModelEntity24).filter(AcademicsModelEntity24.entity_code == code).first()

class AcademicsRepository25:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity25]:
        return self.db.query(AcademicsModelEntity25).filter(AcademicsModelEntity25.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity25]:
        return self.db.query(AcademicsModelEntity25).filter(AcademicsModelEntity25.entity_code == code).first()

class AcademicsRepository26:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity26]:
        return self.db.query(AcademicsModelEntity26).filter(AcademicsModelEntity26.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity26]:
        return self.db.query(AcademicsModelEntity26).filter(AcademicsModelEntity26.entity_code == code).first()

class AcademicsRepository27:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity27]:
        return self.db.query(AcademicsModelEntity27).filter(AcademicsModelEntity27.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity27]:
        return self.db.query(AcademicsModelEntity27).filter(AcademicsModelEntity27.entity_code == code).first()

class AcademicsRepository28:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity28]:
        return self.db.query(AcademicsModelEntity28).filter(AcademicsModelEntity28.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity28]:
        return self.db.query(AcademicsModelEntity28).filter(AcademicsModelEntity28.entity_code == code).first()

class AcademicsRepository29:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity29]:
        return self.db.query(AcademicsModelEntity29).filter(AcademicsModelEntity29.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity29]:
        return self.db.query(AcademicsModelEntity29).filter(AcademicsModelEntity29.entity_code == code).first()

class AcademicsRepository30:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity30]:
        return self.db.query(AcademicsModelEntity30).filter(AcademicsModelEntity30.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity30]:
        return self.db.query(AcademicsModelEntity30).filter(AcademicsModelEntity30.entity_code == code).first()

class AcademicsRepository31:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity31]:
        return self.db.query(AcademicsModelEntity31).filter(AcademicsModelEntity31.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity31]:
        return self.db.query(AcademicsModelEntity31).filter(AcademicsModelEntity31.entity_code == code).first()

class AcademicsRepository32:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity32]:
        return self.db.query(AcademicsModelEntity32).filter(AcademicsModelEntity32.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity32]:
        return self.db.query(AcademicsModelEntity32).filter(AcademicsModelEntity32.entity_code == code).first()

class AcademicsRepository33:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity33]:
        return self.db.query(AcademicsModelEntity33).filter(AcademicsModelEntity33.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity33]:
        return self.db.query(AcademicsModelEntity33).filter(AcademicsModelEntity33.entity_code == code).first()

class AcademicsRepository34:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity34]:
        return self.db.query(AcademicsModelEntity34).filter(AcademicsModelEntity34.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity34]:
        return self.db.query(AcademicsModelEntity34).filter(AcademicsModelEntity34.entity_code == code).first()

class AcademicsRepository35:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity35]:
        return self.db.query(AcademicsModelEntity35).filter(AcademicsModelEntity35.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity35]:
        return self.db.query(AcademicsModelEntity35).filter(AcademicsModelEntity35.entity_code == code).first()

class AcademicsRepository36:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity36]:
        return self.db.query(AcademicsModelEntity36).filter(AcademicsModelEntity36.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity36]:
        return self.db.query(AcademicsModelEntity36).filter(AcademicsModelEntity36.entity_code == code).first()

class AcademicsRepository37:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity37]:
        return self.db.query(AcademicsModelEntity37).filter(AcademicsModelEntity37.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity37]:
        return self.db.query(AcademicsModelEntity37).filter(AcademicsModelEntity37.entity_code == code).first()

class AcademicsRepository38:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity38]:
        return self.db.query(AcademicsModelEntity38).filter(AcademicsModelEntity38.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity38]:
        return self.db.query(AcademicsModelEntity38).filter(AcademicsModelEntity38.entity_code == code).first()

class AcademicsRepository39:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity39]:
        return self.db.query(AcademicsModelEntity39).filter(AcademicsModelEntity39.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity39]:
        return self.db.query(AcademicsModelEntity39).filter(AcademicsModelEntity39.entity_code == code).first()

class AcademicsRepository40:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity40]:
        return self.db.query(AcademicsModelEntity40).filter(AcademicsModelEntity40.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity40]:
        return self.db.query(AcademicsModelEntity40).filter(AcademicsModelEntity40.entity_code == code).first()

class AcademicsRepository41:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity41]:
        return self.db.query(AcademicsModelEntity41).filter(AcademicsModelEntity41.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity41]:
        return self.db.query(AcademicsModelEntity41).filter(AcademicsModelEntity41.entity_code == code).first()

class AcademicsRepository42:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity42]:
        return self.db.query(AcademicsModelEntity42).filter(AcademicsModelEntity42.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity42]:
        return self.db.query(AcademicsModelEntity42).filter(AcademicsModelEntity42.entity_code == code).first()

class AcademicsRepository43:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity43]:
        return self.db.query(AcademicsModelEntity43).filter(AcademicsModelEntity43.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity43]:
        return self.db.query(AcademicsModelEntity43).filter(AcademicsModelEntity43.entity_code == code).first()

class AcademicsRepository44:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity44]:
        return self.db.query(AcademicsModelEntity44).filter(AcademicsModelEntity44.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity44]:
        return self.db.query(AcademicsModelEntity44).filter(AcademicsModelEntity44.entity_code == code).first()

class AcademicsRepository45:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity45]:
        return self.db.query(AcademicsModelEntity45).filter(AcademicsModelEntity45.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity45]:
        return self.db.query(AcademicsModelEntity45).filter(AcademicsModelEntity45.entity_code == code).first()

class AcademicsRepository46:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity46]:
        return self.db.query(AcademicsModelEntity46).filter(AcademicsModelEntity46.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity46]:
        return self.db.query(AcademicsModelEntity46).filter(AcademicsModelEntity46.entity_code == code).first()

class AcademicsRepository47:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity47]:
        return self.db.query(AcademicsModelEntity47).filter(AcademicsModelEntity47.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity47]:
        return self.db.query(AcademicsModelEntity47).filter(AcademicsModelEntity47.entity_code == code).first()

class AcademicsRepository48:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity48]:
        return self.db.query(AcademicsModelEntity48).filter(AcademicsModelEntity48.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity48]:
        return self.db.query(AcademicsModelEntity48).filter(AcademicsModelEntity48.entity_code == code).first()

class AcademicsRepository49:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity49]:
        return self.db.query(AcademicsModelEntity49).filter(AcademicsModelEntity49.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity49]:
        return self.db.query(AcademicsModelEntity49).filter(AcademicsModelEntity49.entity_code == code).first()

class AcademicsRepository50:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity50]:
        return self.db.query(AcademicsModelEntity50).filter(AcademicsModelEntity50.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity50]:
        return self.db.query(AcademicsModelEntity50).filter(AcademicsModelEntity50.entity_code == code).first()

class AcademicsRepository51:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity51]:
        return self.db.query(AcademicsModelEntity51).filter(AcademicsModelEntity51.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity51]:
        return self.db.query(AcademicsModelEntity51).filter(AcademicsModelEntity51.entity_code == code).first()

class AcademicsRepository52:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity52]:
        return self.db.query(AcademicsModelEntity52).filter(AcademicsModelEntity52.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity52]:
        return self.db.query(AcademicsModelEntity52).filter(AcademicsModelEntity52.entity_code == code).first()

class AcademicsRepository53:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity53]:
        return self.db.query(AcademicsModelEntity53).filter(AcademicsModelEntity53.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity53]:
        return self.db.query(AcademicsModelEntity53).filter(AcademicsModelEntity53.entity_code == code).first()

class AcademicsRepository54:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity54]:
        return self.db.query(AcademicsModelEntity54).filter(AcademicsModelEntity54.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity54]:
        return self.db.query(AcademicsModelEntity54).filter(AcademicsModelEntity54.entity_code == code).first()

class AcademicsRepository55:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity55]:
        return self.db.query(AcademicsModelEntity55).filter(AcademicsModelEntity55.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity55]:
        return self.db.query(AcademicsModelEntity55).filter(AcademicsModelEntity55.entity_code == code).first()

class AcademicsRepository56:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity56]:
        return self.db.query(AcademicsModelEntity56).filter(AcademicsModelEntity56.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity56]:
        return self.db.query(AcademicsModelEntity56).filter(AcademicsModelEntity56.entity_code == code).first()

class AcademicsRepository57:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity57]:
        return self.db.query(AcademicsModelEntity57).filter(AcademicsModelEntity57.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity57]:
        return self.db.query(AcademicsModelEntity57).filter(AcademicsModelEntity57.entity_code == code).first()

class AcademicsRepository58:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity58]:
        return self.db.query(AcademicsModelEntity58).filter(AcademicsModelEntity58.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity58]:
        return self.db.query(AcademicsModelEntity58).filter(AcademicsModelEntity58.entity_code == code).first()

class AcademicsRepository59:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity59]:
        return self.db.query(AcademicsModelEntity59).filter(AcademicsModelEntity59.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity59]:
        return self.db.query(AcademicsModelEntity59).filter(AcademicsModelEntity59.entity_code == code).first()

class AcademicsRepository60:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity60]:
        return self.db.query(AcademicsModelEntity60).filter(AcademicsModelEntity60.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity60]:
        return self.db.query(AcademicsModelEntity60).filter(AcademicsModelEntity60.entity_code == code).first()

class AcademicsRepository61:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity61]:
        return self.db.query(AcademicsModelEntity61).filter(AcademicsModelEntity61.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity61]:
        return self.db.query(AcademicsModelEntity61).filter(AcademicsModelEntity61.entity_code == code).first()

class AcademicsRepository62:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity62]:
        return self.db.query(AcademicsModelEntity62).filter(AcademicsModelEntity62.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity62]:
        return self.db.query(AcademicsModelEntity62).filter(AcademicsModelEntity62.entity_code == code).first()

class AcademicsRepository63:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity63]:
        return self.db.query(AcademicsModelEntity63).filter(AcademicsModelEntity63.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity63]:
        return self.db.query(AcademicsModelEntity63).filter(AcademicsModelEntity63.entity_code == code).first()

class AcademicsRepository64:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity64]:
        return self.db.query(AcademicsModelEntity64).filter(AcademicsModelEntity64.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity64]:
        return self.db.query(AcademicsModelEntity64).filter(AcademicsModelEntity64.entity_code == code).first()

class AcademicsRepository65:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity65]:
        return self.db.query(AcademicsModelEntity65).filter(AcademicsModelEntity65.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity65]:
        return self.db.query(AcademicsModelEntity65).filter(AcademicsModelEntity65.entity_code == code).first()

class AcademicsRepository66:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity66]:
        return self.db.query(AcademicsModelEntity66).filter(AcademicsModelEntity66.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity66]:
        return self.db.query(AcademicsModelEntity66).filter(AcademicsModelEntity66.entity_code == code).first()

class AcademicsRepository67:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity67]:
        return self.db.query(AcademicsModelEntity67).filter(AcademicsModelEntity67.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity67]:
        return self.db.query(AcademicsModelEntity67).filter(AcademicsModelEntity67.entity_code == code).first()

class AcademicsRepository68:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity68]:
        return self.db.query(AcademicsModelEntity68).filter(AcademicsModelEntity68.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity68]:
        return self.db.query(AcademicsModelEntity68).filter(AcademicsModelEntity68.entity_code == code).first()

class AcademicsRepository69:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity69]:
        return self.db.query(AcademicsModelEntity69).filter(AcademicsModelEntity69.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity69]:
        return self.db.query(AcademicsModelEntity69).filter(AcademicsModelEntity69.entity_code == code).first()

class AcademicsRepository70:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity70]:
        return self.db.query(AcademicsModelEntity70).filter(AcademicsModelEntity70.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity70]:
        return self.db.query(AcademicsModelEntity70).filter(AcademicsModelEntity70.entity_code == code).first()

class AcademicsRepository71:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity71]:
        return self.db.query(AcademicsModelEntity71).filter(AcademicsModelEntity71.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity71]:
        return self.db.query(AcademicsModelEntity71).filter(AcademicsModelEntity71.entity_code == code).first()

class AcademicsRepository72:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity72]:
        return self.db.query(AcademicsModelEntity72).filter(AcademicsModelEntity72.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity72]:
        return self.db.query(AcademicsModelEntity72).filter(AcademicsModelEntity72.entity_code == code).first()

class AcademicsRepository73:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity73]:
        return self.db.query(AcademicsModelEntity73).filter(AcademicsModelEntity73.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity73]:
        return self.db.query(AcademicsModelEntity73).filter(AcademicsModelEntity73.entity_code == code).first()

class AcademicsRepository74:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity74]:
        return self.db.query(AcademicsModelEntity74).filter(AcademicsModelEntity74.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity74]:
        return self.db.query(AcademicsModelEntity74).filter(AcademicsModelEntity74.entity_code == code).first()

class AcademicsRepository75:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity75]:
        return self.db.query(AcademicsModelEntity75).filter(AcademicsModelEntity75.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity75]:
        return self.db.query(AcademicsModelEntity75).filter(AcademicsModelEntity75.entity_code == code).first()

class AcademicsRepository76:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity76]:
        return self.db.query(AcademicsModelEntity76).filter(AcademicsModelEntity76.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity76]:
        return self.db.query(AcademicsModelEntity76).filter(AcademicsModelEntity76.entity_code == code).first()

class AcademicsRepository77:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity77]:
        return self.db.query(AcademicsModelEntity77).filter(AcademicsModelEntity77.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity77]:
        return self.db.query(AcademicsModelEntity77).filter(AcademicsModelEntity77.entity_code == code).first()

class AcademicsRepository78:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity78]:
        return self.db.query(AcademicsModelEntity78).filter(AcademicsModelEntity78.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity78]:
        return self.db.query(AcademicsModelEntity78).filter(AcademicsModelEntity78.entity_code == code).first()

class AcademicsRepository79:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity79]:
        return self.db.query(AcademicsModelEntity79).filter(AcademicsModelEntity79.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity79]:
        return self.db.query(AcademicsModelEntity79).filter(AcademicsModelEntity79.entity_code == code).first()

class AcademicsRepository80:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity80]:
        return self.db.query(AcademicsModelEntity80).filter(AcademicsModelEntity80.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity80]:
        return self.db.query(AcademicsModelEntity80).filter(AcademicsModelEntity80.entity_code == code).first()

class AcademicsRepository81:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity81]:
        return self.db.query(AcademicsModelEntity81).filter(AcademicsModelEntity81.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity81]:
        return self.db.query(AcademicsModelEntity81).filter(AcademicsModelEntity81.entity_code == code).first()

class AcademicsRepository82:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity82]:
        return self.db.query(AcademicsModelEntity82).filter(AcademicsModelEntity82.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity82]:
        return self.db.query(AcademicsModelEntity82).filter(AcademicsModelEntity82.entity_code == code).first()

class AcademicsRepository83:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity83]:
        return self.db.query(AcademicsModelEntity83).filter(AcademicsModelEntity83.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity83]:
        return self.db.query(AcademicsModelEntity83).filter(AcademicsModelEntity83.entity_code == code).first()

class AcademicsRepository84:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity84]:
        return self.db.query(AcademicsModelEntity84).filter(AcademicsModelEntity84.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity84]:
        return self.db.query(AcademicsModelEntity84).filter(AcademicsModelEntity84.entity_code == code).first()

class AcademicsRepository85:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity85]:
        return self.db.query(AcademicsModelEntity85).filter(AcademicsModelEntity85.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity85]:
        return self.db.query(AcademicsModelEntity85).filter(AcademicsModelEntity85.entity_code == code).first()

class AcademicsRepository86:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity86]:
        return self.db.query(AcademicsModelEntity86).filter(AcademicsModelEntity86.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity86]:
        return self.db.query(AcademicsModelEntity86).filter(AcademicsModelEntity86.entity_code == code).first()

class AcademicsRepository87:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity87]:
        return self.db.query(AcademicsModelEntity87).filter(AcademicsModelEntity87.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity87]:
        return self.db.query(AcademicsModelEntity87).filter(AcademicsModelEntity87.entity_code == code).first()

class AcademicsRepository88:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity88]:
        return self.db.query(AcademicsModelEntity88).filter(AcademicsModelEntity88.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity88]:
        return self.db.query(AcademicsModelEntity88).filter(AcademicsModelEntity88.entity_code == code).first()

class AcademicsRepository89:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity89]:
        return self.db.query(AcademicsModelEntity89).filter(AcademicsModelEntity89.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity89]:
        return self.db.query(AcademicsModelEntity89).filter(AcademicsModelEntity89.entity_code == code).first()

class AcademicsRepository90:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity90]:
        return self.db.query(AcademicsModelEntity90).filter(AcademicsModelEntity90.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity90]:
        return self.db.query(AcademicsModelEntity90).filter(AcademicsModelEntity90.entity_code == code).first()

class AcademicsRepository91:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity91]:
        return self.db.query(AcademicsModelEntity91).filter(AcademicsModelEntity91.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity91]:
        return self.db.query(AcademicsModelEntity91).filter(AcademicsModelEntity91.entity_code == code).first()

class AcademicsRepository92:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity92]:
        return self.db.query(AcademicsModelEntity92).filter(AcademicsModelEntity92.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity92]:
        return self.db.query(AcademicsModelEntity92).filter(AcademicsModelEntity92.entity_code == code).first()

class AcademicsRepository93:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity93]:
        return self.db.query(AcademicsModelEntity93).filter(AcademicsModelEntity93.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity93]:
        return self.db.query(AcademicsModelEntity93).filter(AcademicsModelEntity93.entity_code == code).first()

class AcademicsRepository94:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity94]:
        return self.db.query(AcademicsModelEntity94).filter(AcademicsModelEntity94.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity94]:
        return self.db.query(AcademicsModelEntity94).filter(AcademicsModelEntity94.entity_code == code).first()

class AcademicsRepository95:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity95]:
        return self.db.query(AcademicsModelEntity95).filter(AcademicsModelEntity95.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity95]:
        return self.db.query(AcademicsModelEntity95).filter(AcademicsModelEntity95.entity_code == code).first()

class AcademicsRepository96:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity96]:
        return self.db.query(AcademicsModelEntity96).filter(AcademicsModelEntity96.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity96]:
        return self.db.query(AcademicsModelEntity96).filter(AcademicsModelEntity96.entity_code == code).first()

class AcademicsRepository97:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity97]:
        return self.db.query(AcademicsModelEntity97).filter(AcademicsModelEntity97.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity97]:
        return self.db.query(AcademicsModelEntity97).filter(AcademicsModelEntity97.entity_code == code).first()

class AcademicsRepository98:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity98]:
        return self.db.query(AcademicsModelEntity98).filter(AcademicsModelEntity98.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity98]:
        return self.db.query(AcademicsModelEntity98).filter(AcademicsModelEntity98.entity_code == code).first()

class AcademicsRepository99:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity99]:
        return self.db.query(AcademicsModelEntity99).filter(AcademicsModelEntity99.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity99]:
        return self.db.query(AcademicsModelEntity99).filter(AcademicsModelEntity99.entity_code == code).first()

class AcademicsRepository100:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity100]:
        return self.db.query(AcademicsModelEntity100).filter(AcademicsModelEntity100.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity100]:
        return self.db.query(AcademicsModelEntity100).filter(AcademicsModelEntity100.entity_code == code).first()

class AcademicsRepository101:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity101]:
        return self.db.query(AcademicsModelEntity101).filter(AcademicsModelEntity101.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity101]:
        return self.db.query(AcademicsModelEntity101).filter(AcademicsModelEntity101.entity_code == code).first()

class AcademicsRepository102:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity102]:
        return self.db.query(AcademicsModelEntity102).filter(AcademicsModelEntity102.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity102]:
        return self.db.query(AcademicsModelEntity102).filter(AcademicsModelEntity102.entity_code == code).first()

class AcademicsRepository103:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity103]:
        return self.db.query(AcademicsModelEntity103).filter(AcademicsModelEntity103.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity103]:
        return self.db.query(AcademicsModelEntity103).filter(AcademicsModelEntity103.entity_code == code).first()

class AcademicsRepository104:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity104]:
        return self.db.query(AcademicsModelEntity104).filter(AcademicsModelEntity104.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity104]:
        return self.db.query(AcademicsModelEntity104).filter(AcademicsModelEntity104.entity_code == code).first()

class AcademicsRepository105:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity105]:
        return self.db.query(AcademicsModelEntity105).filter(AcademicsModelEntity105.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity105]:
        return self.db.query(AcademicsModelEntity105).filter(AcademicsModelEntity105.entity_code == code).first()

class AcademicsRepository106:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity106]:
        return self.db.query(AcademicsModelEntity106).filter(AcademicsModelEntity106.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity106]:
        return self.db.query(AcademicsModelEntity106).filter(AcademicsModelEntity106.entity_code == code).first()

class AcademicsRepository107:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity107]:
        return self.db.query(AcademicsModelEntity107).filter(AcademicsModelEntity107.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity107]:
        return self.db.query(AcademicsModelEntity107).filter(AcademicsModelEntity107.entity_code == code).first()

class AcademicsRepository108:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity108]:
        return self.db.query(AcademicsModelEntity108).filter(AcademicsModelEntity108.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity108]:
        return self.db.query(AcademicsModelEntity108).filter(AcademicsModelEntity108.entity_code == code).first()

class AcademicsRepository109:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity109]:
        return self.db.query(AcademicsModelEntity109).filter(AcademicsModelEntity109.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity109]:
        return self.db.query(AcademicsModelEntity109).filter(AcademicsModelEntity109.entity_code == code).first()

class AcademicsRepository110:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity110]:
        return self.db.query(AcademicsModelEntity110).filter(AcademicsModelEntity110.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity110]:
        return self.db.query(AcademicsModelEntity110).filter(AcademicsModelEntity110.entity_code == code).first()

class AcademicsRepository111:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity111]:
        return self.db.query(AcademicsModelEntity111).filter(AcademicsModelEntity111.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity111]:
        return self.db.query(AcademicsModelEntity111).filter(AcademicsModelEntity111.entity_code == code).first()

class AcademicsRepository112:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity112]:
        return self.db.query(AcademicsModelEntity112).filter(AcademicsModelEntity112.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity112]:
        return self.db.query(AcademicsModelEntity112).filter(AcademicsModelEntity112.entity_code == code).first()

class AcademicsRepository113:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity113]:
        return self.db.query(AcademicsModelEntity113).filter(AcademicsModelEntity113.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity113]:
        return self.db.query(AcademicsModelEntity113).filter(AcademicsModelEntity113.entity_code == code).first()

class AcademicsRepository114:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity114]:
        return self.db.query(AcademicsModelEntity114).filter(AcademicsModelEntity114.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity114]:
        return self.db.query(AcademicsModelEntity114).filter(AcademicsModelEntity114.entity_code == code).first()

class AcademicsRepository115:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity115]:
        return self.db.query(AcademicsModelEntity115).filter(AcademicsModelEntity115.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity115]:
        return self.db.query(AcademicsModelEntity115).filter(AcademicsModelEntity115.entity_code == code).first()

class AcademicsRepository116:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity116]:
        return self.db.query(AcademicsModelEntity116).filter(AcademicsModelEntity116.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity116]:
        return self.db.query(AcademicsModelEntity116).filter(AcademicsModelEntity116.entity_code == code).first()

class AcademicsRepository117:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity117]:
        return self.db.query(AcademicsModelEntity117).filter(AcademicsModelEntity117.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity117]:
        return self.db.query(AcademicsModelEntity117).filter(AcademicsModelEntity117.entity_code == code).first()

class AcademicsRepository118:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity118]:
        return self.db.query(AcademicsModelEntity118).filter(AcademicsModelEntity118.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity118]:
        return self.db.query(AcademicsModelEntity118).filter(AcademicsModelEntity118.entity_code == code).first()

class AcademicsRepository119:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity119]:
        return self.db.query(AcademicsModelEntity119).filter(AcademicsModelEntity119.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity119]:
        return self.db.query(AcademicsModelEntity119).filter(AcademicsModelEntity119.entity_code == code).first()

class AcademicsRepository120:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity120]:
        return self.db.query(AcademicsModelEntity120).filter(AcademicsModelEntity120.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity120]:
        return self.db.query(AcademicsModelEntity120).filter(AcademicsModelEntity120.entity_code == code).first()

