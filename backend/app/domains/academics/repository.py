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

class AcademicsRepository121:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity121]:
        return self.db.query(AcademicsModelEntity121).filter(AcademicsModelEntity121.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity121]:
        return self.db.query(AcademicsModelEntity121).filter(AcademicsModelEntity121.entity_code == code).first()

class AcademicsRepository122:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity122]:
        return self.db.query(AcademicsModelEntity122).filter(AcademicsModelEntity122.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity122]:
        return self.db.query(AcademicsModelEntity122).filter(AcademicsModelEntity122.entity_code == code).first()

class AcademicsRepository123:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity123]:
        return self.db.query(AcademicsModelEntity123).filter(AcademicsModelEntity123.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity123]:
        return self.db.query(AcademicsModelEntity123).filter(AcademicsModelEntity123.entity_code == code).first()

class AcademicsRepository124:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity124]:
        return self.db.query(AcademicsModelEntity124).filter(AcademicsModelEntity124.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity124]:
        return self.db.query(AcademicsModelEntity124).filter(AcademicsModelEntity124.entity_code == code).first()

class AcademicsRepository125:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity125]:
        return self.db.query(AcademicsModelEntity125).filter(AcademicsModelEntity125.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity125]:
        return self.db.query(AcademicsModelEntity125).filter(AcademicsModelEntity125.entity_code == code).first()

class AcademicsRepository126:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity126]:
        return self.db.query(AcademicsModelEntity126).filter(AcademicsModelEntity126.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity126]:
        return self.db.query(AcademicsModelEntity126).filter(AcademicsModelEntity126.entity_code == code).first()

class AcademicsRepository127:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity127]:
        return self.db.query(AcademicsModelEntity127).filter(AcademicsModelEntity127.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity127]:
        return self.db.query(AcademicsModelEntity127).filter(AcademicsModelEntity127.entity_code == code).first()

class AcademicsRepository128:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity128]:
        return self.db.query(AcademicsModelEntity128).filter(AcademicsModelEntity128.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity128]:
        return self.db.query(AcademicsModelEntity128).filter(AcademicsModelEntity128.entity_code == code).first()

class AcademicsRepository129:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity129]:
        return self.db.query(AcademicsModelEntity129).filter(AcademicsModelEntity129.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity129]:
        return self.db.query(AcademicsModelEntity129).filter(AcademicsModelEntity129.entity_code == code).first()

class AcademicsRepository130:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity130]:
        return self.db.query(AcademicsModelEntity130).filter(AcademicsModelEntity130.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity130]:
        return self.db.query(AcademicsModelEntity130).filter(AcademicsModelEntity130.entity_code == code).first()

class AcademicsRepository131:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity131]:
        return self.db.query(AcademicsModelEntity131).filter(AcademicsModelEntity131.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity131]:
        return self.db.query(AcademicsModelEntity131).filter(AcademicsModelEntity131.entity_code == code).first()

class AcademicsRepository132:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity132]:
        return self.db.query(AcademicsModelEntity132).filter(AcademicsModelEntity132.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity132]:
        return self.db.query(AcademicsModelEntity132).filter(AcademicsModelEntity132.entity_code == code).first()

class AcademicsRepository133:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity133]:
        return self.db.query(AcademicsModelEntity133).filter(AcademicsModelEntity133.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity133]:
        return self.db.query(AcademicsModelEntity133).filter(AcademicsModelEntity133.entity_code == code).first()

class AcademicsRepository134:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity134]:
        return self.db.query(AcademicsModelEntity134).filter(AcademicsModelEntity134.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity134]:
        return self.db.query(AcademicsModelEntity134).filter(AcademicsModelEntity134.entity_code == code).first()

class AcademicsRepository135:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity135]:
        return self.db.query(AcademicsModelEntity135).filter(AcademicsModelEntity135.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity135]:
        return self.db.query(AcademicsModelEntity135).filter(AcademicsModelEntity135.entity_code == code).first()

class AcademicsRepository136:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity136]:
        return self.db.query(AcademicsModelEntity136).filter(AcademicsModelEntity136.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity136]:
        return self.db.query(AcademicsModelEntity136).filter(AcademicsModelEntity136.entity_code == code).first()

class AcademicsRepository137:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity137]:
        return self.db.query(AcademicsModelEntity137).filter(AcademicsModelEntity137.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity137]:
        return self.db.query(AcademicsModelEntity137).filter(AcademicsModelEntity137.entity_code == code).first()

class AcademicsRepository138:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity138]:
        return self.db.query(AcademicsModelEntity138).filter(AcademicsModelEntity138.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity138]:
        return self.db.query(AcademicsModelEntity138).filter(AcademicsModelEntity138.entity_code == code).first()

class AcademicsRepository139:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity139]:
        return self.db.query(AcademicsModelEntity139).filter(AcademicsModelEntity139.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity139]:
        return self.db.query(AcademicsModelEntity139).filter(AcademicsModelEntity139.entity_code == code).first()

class AcademicsRepository140:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity140]:
        return self.db.query(AcademicsModelEntity140).filter(AcademicsModelEntity140.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity140]:
        return self.db.query(AcademicsModelEntity140).filter(AcademicsModelEntity140.entity_code == code).first()

class AcademicsRepository141:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity141]:
        return self.db.query(AcademicsModelEntity141).filter(AcademicsModelEntity141.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity141]:
        return self.db.query(AcademicsModelEntity141).filter(AcademicsModelEntity141.entity_code == code).first()

class AcademicsRepository142:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity142]:
        return self.db.query(AcademicsModelEntity142).filter(AcademicsModelEntity142.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity142]:
        return self.db.query(AcademicsModelEntity142).filter(AcademicsModelEntity142.entity_code == code).first()

class AcademicsRepository143:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity143]:
        return self.db.query(AcademicsModelEntity143).filter(AcademicsModelEntity143.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity143]:
        return self.db.query(AcademicsModelEntity143).filter(AcademicsModelEntity143.entity_code == code).first()

class AcademicsRepository144:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity144]:
        return self.db.query(AcademicsModelEntity144).filter(AcademicsModelEntity144.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity144]:
        return self.db.query(AcademicsModelEntity144).filter(AcademicsModelEntity144.entity_code == code).first()

class AcademicsRepository145:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity145]:
        return self.db.query(AcademicsModelEntity145).filter(AcademicsModelEntity145.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity145]:
        return self.db.query(AcademicsModelEntity145).filter(AcademicsModelEntity145.entity_code == code).first()

class AcademicsRepository146:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity146]:
        return self.db.query(AcademicsModelEntity146).filter(AcademicsModelEntity146.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity146]:
        return self.db.query(AcademicsModelEntity146).filter(AcademicsModelEntity146.entity_code == code).first()

class AcademicsRepository147:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity147]:
        return self.db.query(AcademicsModelEntity147).filter(AcademicsModelEntity147.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity147]:
        return self.db.query(AcademicsModelEntity147).filter(AcademicsModelEntity147.entity_code == code).first()

class AcademicsRepository148:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity148]:
        return self.db.query(AcademicsModelEntity148).filter(AcademicsModelEntity148.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity148]:
        return self.db.query(AcademicsModelEntity148).filter(AcademicsModelEntity148.entity_code == code).first()

class AcademicsRepository149:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity149]:
        return self.db.query(AcademicsModelEntity149).filter(AcademicsModelEntity149.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity149]:
        return self.db.query(AcademicsModelEntity149).filter(AcademicsModelEntity149.entity_code == code).first()

class AcademicsRepository150:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity150]:
        return self.db.query(AcademicsModelEntity150).filter(AcademicsModelEntity150.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity150]:
        return self.db.query(AcademicsModelEntity150).filter(AcademicsModelEntity150.entity_code == code).first()

class AcademicsRepository151:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity151]:
        return self.db.query(AcademicsModelEntity151).filter(AcademicsModelEntity151.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity151]:
        return self.db.query(AcademicsModelEntity151).filter(AcademicsModelEntity151.entity_code == code).first()

class AcademicsRepository152:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity152]:
        return self.db.query(AcademicsModelEntity152).filter(AcademicsModelEntity152.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity152]:
        return self.db.query(AcademicsModelEntity152).filter(AcademicsModelEntity152.entity_code == code).first()

class AcademicsRepository153:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity153]:
        return self.db.query(AcademicsModelEntity153).filter(AcademicsModelEntity153.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity153]:
        return self.db.query(AcademicsModelEntity153).filter(AcademicsModelEntity153.entity_code == code).first()

class AcademicsRepository154:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity154]:
        return self.db.query(AcademicsModelEntity154).filter(AcademicsModelEntity154.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity154]:
        return self.db.query(AcademicsModelEntity154).filter(AcademicsModelEntity154.entity_code == code).first()

class AcademicsRepository155:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity155]:
        return self.db.query(AcademicsModelEntity155).filter(AcademicsModelEntity155.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity155]:
        return self.db.query(AcademicsModelEntity155).filter(AcademicsModelEntity155.entity_code == code).first()

class AcademicsRepository156:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity156]:
        return self.db.query(AcademicsModelEntity156).filter(AcademicsModelEntity156.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity156]:
        return self.db.query(AcademicsModelEntity156).filter(AcademicsModelEntity156.entity_code == code).first()

class AcademicsRepository157:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity157]:
        return self.db.query(AcademicsModelEntity157).filter(AcademicsModelEntity157.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity157]:
        return self.db.query(AcademicsModelEntity157).filter(AcademicsModelEntity157.entity_code == code).first()

class AcademicsRepository158:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity158]:
        return self.db.query(AcademicsModelEntity158).filter(AcademicsModelEntity158.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity158]:
        return self.db.query(AcademicsModelEntity158).filter(AcademicsModelEntity158.entity_code == code).first()

class AcademicsRepository159:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity159]:
        return self.db.query(AcademicsModelEntity159).filter(AcademicsModelEntity159.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity159]:
        return self.db.query(AcademicsModelEntity159).filter(AcademicsModelEntity159.entity_code == code).first()

class AcademicsRepository160:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity160]:
        return self.db.query(AcademicsModelEntity160).filter(AcademicsModelEntity160.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity160]:
        return self.db.query(AcademicsModelEntity160).filter(AcademicsModelEntity160.entity_code == code).first()

class AcademicsRepository161:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity161]:
        return self.db.query(AcademicsModelEntity161).filter(AcademicsModelEntity161.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity161]:
        return self.db.query(AcademicsModelEntity161).filter(AcademicsModelEntity161.entity_code == code).first()

class AcademicsRepository162:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity162]:
        return self.db.query(AcademicsModelEntity162).filter(AcademicsModelEntity162.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity162]:
        return self.db.query(AcademicsModelEntity162).filter(AcademicsModelEntity162.entity_code == code).first()

class AcademicsRepository163:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity163]:
        return self.db.query(AcademicsModelEntity163).filter(AcademicsModelEntity163.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity163]:
        return self.db.query(AcademicsModelEntity163).filter(AcademicsModelEntity163.entity_code == code).first()

class AcademicsRepository164:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity164]:
        return self.db.query(AcademicsModelEntity164).filter(AcademicsModelEntity164.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity164]:
        return self.db.query(AcademicsModelEntity164).filter(AcademicsModelEntity164.entity_code == code).first()

class AcademicsRepository165:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity165]:
        return self.db.query(AcademicsModelEntity165).filter(AcademicsModelEntity165.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity165]:
        return self.db.query(AcademicsModelEntity165).filter(AcademicsModelEntity165.entity_code == code).first()

class AcademicsRepository166:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity166]:
        return self.db.query(AcademicsModelEntity166).filter(AcademicsModelEntity166.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity166]:
        return self.db.query(AcademicsModelEntity166).filter(AcademicsModelEntity166.entity_code == code).first()

class AcademicsRepository167:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity167]:
        return self.db.query(AcademicsModelEntity167).filter(AcademicsModelEntity167.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity167]:
        return self.db.query(AcademicsModelEntity167).filter(AcademicsModelEntity167.entity_code == code).first()

class AcademicsRepository168:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity168]:
        return self.db.query(AcademicsModelEntity168).filter(AcademicsModelEntity168.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity168]:
        return self.db.query(AcademicsModelEntity168).filter(AcademicsModelEntity168.entity_code == code).first()

class AcademicsRepository169:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity169]:
        return self.db.query(AcademicsModelEntity169).filter(AcademicsModelEntity169.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity169]:
        return self.db.query(AcademicsModelEntity169).filter(AcademicsModelEntity169.entity_code == code).first()

class AcademicsRepository170:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity170]:
        return self.db.query(AcademicsModelEntity170).filter(AcademicsModelEntity170.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity170]:
        return self.db.query(AcademicsModelEntity170).filter(AcademicsModelEntity170.entity_code == code).first()

class AcademicsRepository171:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity171]:
        return self.db.query(AcademicsModelEntity171).filter(AcademicsModelEntity171.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity171]:
        return self.db.query(AcademicsModelEntity171).filter(AcademicsModelEntity171.entity_code == code).first()

class AcademicsRepository172:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity172]:
        return self.db.query(AcademicsModelEntity172).filter(AcademicsModelEntity172.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity172]:
        return self.db.query(AcademicsModelEntity172).filter(AcademicsModelEntity172.entity_code == code).first()

class AcademicsRepository173:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity173]:
        return self.db.query(AcademicsModelEntity173).filter(AcademicsModelEntity173.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity173]:
        return self.db.query(AcademicsModelEntity173).filter(AcademicsModelEntity173.entity_code == code).first()

class AcademicsRepository174:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity174]:
        return self.db.query(AcademicsModelEntity174).filter(AcademicsModelEntity174.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity174]:
        return self.db.query(AcademicsModelEntity174).filter(AcademicsModelEntity174.entity_code == code).first()

class AcademicsRepository175:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity175]:
        return self.db.query(AcademicsModelEntity175).filter(AcademicsModelEntity175.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity175]:
        return self.db.query(AcademicsModelEntity175).filter(AcademicsModelEntity175.entity_code == code).first()

class AcademicsRepository176:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity176]:
        return self.db.query(AcademicsModelEntity176).filter(AcademicsModelEntity176.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity176]:
        return self.db.query(AcademicsModelEntity176).filter(AcademicsModelEntity176.entity_code == code).first()

class AcademicsRepository177:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity177]:
        return self.db.query(AcademicsModelEntity177).filter(AcademicsModelEntity177.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity177]:
        return self.db.query(AcademicsModelEntity177).filter(AcademicsModelEntity177.entity_code == code).first()

class AcademicsRepository178:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity178]:
        return self.db.query(AcademicsModelEntity178).filter(AcademicsModelEntity178.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity178]:
        return self.db.query(AcademicsModelEntity178).filter(AcademicsModelEntity178.entity_code == code).first()

class AcademicsRepository179:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity179]:
        return self.db.query(AcademicsModelEntity179).filter(AcademicsModelEntity179.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity179]:
        return self.db.query(AcademicsModelEntity179).filter(AcademicsModelEntity179.entity_code == code).first()

class AcademicsRepository180:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity180]:
        return self.db.query(AcademicsModelEntity180).filter(AcademicsModelEntity180.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity180]:
        return self.db.query(AcademicsModelEntity180).filter(AcademicsModelEntity180.entity_code == code).first()

class AcademicsRepository181:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity181]:
        return self.db.query(AcademicsModelEntity181).filter(AcademicsModelEntity181.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity181]:
        return self.db.query(AcademicsModelEntity181).filter(AcademicsModelEntity181.entity_code == code).first()

class AcademicsRepository182:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity182]:
        return self.db.query(AcademicsModelEntity182).filter(AcademicsModelEntity182.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity182]:
        return self.db.query(AcademicsModelEntity182).filter(AcademicsModelEntity182.entity_code == code).first()

class AcademicsRepository183:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity183]:
        return self.db.query(AcademicsModelEntity183).filter(AcademicsModelEntity183.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity183]:
        return self.db.query(AcademicsModelEntity183).filter(AcademicsModelEntity183.entity_code == code).first()

class AcademicsRepository184:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity184]:
        return self.db.query(AcademicsModelEntity184).filter(AcademicsModelEntity184.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity184]:
        return self.db.query(AcademicsModelEntity184).filter(AcademicsModelEntity184.entity_code == code).first()

class AcademicsRepository185:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity185]:
        return self.db.query(AcademicsModelEntity185).filter(AcademicsModelEntity185.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity185]:
        return self.db.query(AcademicsModelEntity185).filter(AcademicsModelEntity185.entity_code == code).first()

class AcademicsRepository186:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity186]:
        return self.db.query(AcademicsModelEntity186).filter(AcademicsModelEntity186.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity186]:
        return self.db.query(AcademicsModelEntity186).filter(AcademicsModelEntity186.entity_code == code).first()

class AcademicsRepository187:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity187]:
        return self.db.query(AcademicsModelEntity187).filter(AcademicsModelEntity187.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity187]:
        return self.db.query(AcademicsModelEntity187).filter(AcademicsModelEntity187.entity_code == code).first()

class AcademicsRepository188:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity188]:
        return self.db.query(AcademicsModelEntity188).filter(AcademicsModelEntity188.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity188]:
        return self.db.query(AcademicsModelEntity188).filter(AcademicsModelEntity188.entity_code == code).first()

class AcademicsRepository189:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity189]:
        return self.db.query(AcademicsModelEntity189).filter(AcademicsModelEntity189.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity189]:
        return self.db.query(AcademicsModelEntity189).filter(AcademicsModelEntity189.entity_code == code).first()

class AcademicsRepository190:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity190]:
        return self.db.query(AcademicsModelEntity190).filter(AcademicsModelEntity190.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity190]:
        return self.db.query(AcademicsModelEntity190).filter(AcademicsModelEntity190.entity_code == code).first()

class AcademicsRepository191:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity191]:
        return self.db.query(AcademicsModelEntity191).filter(AcademicsModelEntity191.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity191]:
        return self.db.query(AcademicsModelEntity191).filter(AcademicsModelEntity191.entity_code == code).first()

class AcademicsRepository192:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity192]:
        return self.db.query(AcademicsModelEntity192).filter(AcademicsModelEntity192.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity192]:
        return self.db.query(AcademicsModelEntity192).filter(AcademicsModelEntity192.entity_code == code).first()

class AcademicsRepository193:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity193]:
        return self.db.query(AcademicsModelEntity193).filter(AcademicsModelEntity193.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity193]:
        return self.db.query(AcademicsModelEntity193).filter(AcademicsModelEntity193.entity_code == code).first()

class AcademicsRepository194:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity194]:
        return self.db.query(AcademicsModelEntity194).filter(AcademicsModelEntity194.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity194]:
        return self.db.query(AcademicsModelEntity194).filter(AcademicsModelEntity194.entity_code == code).first()

class AcademicsRepository195:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity195]:
        return self.db.query(AcademicsModelEntity195).filter(AcademicsModelEntity195.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity195]:
        return self.db.query(AcademicsModelEntity195).filter(AcademicsModelEntity195.entity_code == code).first()

class AcademicsRepository196:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity196]:
        return self.db.query(AcademicsModelEntity196).filter(AcademicsModelEntity196.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity196]:
        return self.db.query(AcademicsModelEntity196).filter(AcademicsModelEntity196.entity_code == code).first()

class AcademicsRepository197:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity197]:
        return self.db.query(AcademicsModelEntity197).filter(AcademicsModelEntity197.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity197]:
        return self.db.query(AcademicsModelEntity197).filter(AcademicsModelEntity197.entity_code == code).first()

class AcademicsRepository198:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity198]:
        return self.db.query(AcademicsModelEntity198).filter(AcademicsModelEntity198.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity198]:
        return self.db.query(AcademicsModelEntity198).filter(AcademicsModelEntity198.entity_code == code).first()

class AcademicsRepository199:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity199]:
        return self.db.query(AcademicsModelEntity199).filter(AcademicsModelEntity199.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity199]:
        return self.db.query(AcademicsModelEntity199).filter(AcademicsModelEntity199.entity_code == code).first()

class AcademicsRepository200:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity200]:
        return self.db.query(AcademicsModelEntity200).filter(AcademicsModelEntity200.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity200]:
        return self.db.query(AcademicsModelEntity200).filter(AcademicsModelEntity200.entity_code == code).first()

class AcademicsRepository201:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity201]:
        return self.db.query(AcademicsModelEntity201).filter(AcademicsModelEntity201.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity201]:
        return self.db.query(AcademicsModelEntity201).filter(AcademicsModelEntity201.entity_code == code).first()

class AcademicsRepository202:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity202]:
        return self.db.query(AcademicsModelEntity202).filter(AcademicsModelEntity202.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity202]:
        return self.db.query(AcademicsModelEntity202).filter(AcademicsModelEntity202.entity_code == code).first()

class AcademicsRepository203:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity203]:
        return self.db.query(AcademicsModelEntity203).filter(AcademicsModelEntity203.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity203]:
        return self.db.query(AcademicsModelEntity203).filter(AcademicsModelEntity203.entity_code == code).first()

class AcademicsRepository204:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity204]:
        return self.db.query(AcademicsModelEntity204).filter(AcademicsModelEntity204.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity204]:
        return self.db.query(AcademicsModelEntity204).filter(AcademicsModelEntity204.entity_code == code).first()

class AcademicsRepository205:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity205]:
        return self.db.query(AcademicsModelEntity205).filter(AcademicsModelEntity205.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity205]:
        return self.db.query(AcademicsModelEntity205).filter(AcademicsModelEntity205.entity_code == code).first()

class AcademicsRepository206:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity206]:
        return self.db.query(AcademicsModelEntity206).filter(AcademicsModelEntity206.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity206]:
        return self.db.query(AcademicsModelEntity206).filter(AcademicsModelEntity206.entity_code == code).first()

class AcademicsRepository207:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity207]:
        return self.db.query(AcademicsModelEntity207).filter(AcademicsModelEntity207.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity207]:
        return self.db.query(AcademicsModelEntity207).filter(AcademicsModelEntity207.entity_code == code).first()

class AcademicsRepository208:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity208]:
        return self.db.query(AcademicsModelEntity208).filter(AcademicsModelEntity208.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity208]:
        return self.db.query(AcademicsModelEntity208).filter(AcademicsModelEntity208.entity_code == code).first()

class AcademicsRepository209:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity209]:
        return self.db.query(AcademicsModelEntity209).filter(AcademicsModelEntity209.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity209]:
        return self.db.query(AcademicsModelEntity209).filter(AcademicsModelEntity209.entity_code == code).first()

class AcademicsRepository210:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity210]:
        return self.db.query(AcademicsModelEntity210).filter(AcademicsModelEntity210.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity210]:
        return self.db.query(AcademicsModelEntity210).filter(AcademicsModelEntity210.entity_code == code).first()

class AcademicsRepository211:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity211]:
        return self.db.query(AcademicsModelEntity211).filter(AcademicsModelEntity211.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity211]:
        return self.db.query(AcademicsModelEntity211).filter(AcademicsModelEntity211.entity_code == code).first()

class AcademicsRepository212:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity212]:
        return self.db.query(AcademicsModelEntity212).filter(AcademicsModelEntity212.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity212]:
        return self.db.query(AcademicsModelEntity212).filter(AcademicsModelEntity212.entity_code == code).first()

class AcademicsRepository213:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity213]:
        return self.db.query(AcademicsModelEntity213).filter(AcademicsModelEntity213.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity213]:
        return self.db.query(AcademicsModelEntity213).filter(AcademicsModelEntity213.entity_code == code).first()

class AcademicsRepository214:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity214]:
        return self.db.query(AcademicsModelEntity214).filter(AcademicsModelEntity214.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity214]:
        return self.db.query(AcademicsModelEntity214).filter(AcademicsModelEntity214.entity_code == code).first()

class AcademicsRepository215:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity215]:
        return self.db.query(AcademicsModelEntity215).filter(AcademicsModelEntity215.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity215]:
        return self.db.query(AcademicsModelEntity215).filter(AcademicsModelEntity215.entity_code == code).first()

class AcademicsRepository216:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity216]:
        return self.db.query(AcademicsModelEntity216).filter(AcademicsModelEntity216.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity216]:
        return self.db.query(AcademicsModelEntity216).filter(AcademicsModelEntity216.entity_code == code).first()

class AcademicsRepository217:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity217]:
        return self.db.query(AcademicsModelEntity217).filter(AcademicsModelEntity217.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity217]:
        return self.db.query(AcademicsModelEntity217).filter(AcademicsModelEntity217.entity_code == code).first()

class AcademicsRepository218:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity218]:
        return self.db.query(AcademicsModelEntity218).filter(AcademicsModelEntity218.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity218]:
        return self.db.query(AcademicsModelEntity218).filter(AcademicsModelEntity218.entity_code == code).first()

class AcademicsRepository219:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity219]:
        return self.db.query(AcademicsModelEntity219).filter(AcademicsModelEntity219.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity219]:
        return self.db.query(AcademicsModelEntity219).filter(AcademicsModelEntity219.entity_code == code).first()

class AcademicsRepository220:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity220]:
        return self.db.query(AcademicsModelEntity220).filter(AcademicsModelEntity220.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity220]:
        return self.db.query(AcademicsModelEntity220).filter(AcademicsModelEntity220.entity_code == code).first()

class AcademicsRepository221:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity221]:
        return self.db.query(AcademicsModelEntity221).filter(AcademicsModelEntity221.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity221]:
        return self.db.query(AcademicsModelEntity221).filter(AcademicsModelEntity221.entity_code == code).first()

class AcademicsRepository222:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity222]:
        return self.db.query(AcademicsModelEntity222).filter(AcademicsModelEntity222.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity222]:
        return self.db.query(AcademicsModelEntity222).filter(AcademicsModelEntity222.entity_code == code).first()

class AcademicsRepository223:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity223]:
        return self.db.query(AcademicsModelEntity223).filter(AcademicsModelEntity223.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity223]:
        return self.db.query(AcademicsModelEntity223).filter(AcademicsModelEntity223.entity_code == code).first()

class AcademicsRepository224:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity224]:
        return self.db.query(AcademicsModelEntity224).filter(AcademicsModelEntity224.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity224]:
        return self.db.query(AcademicsModelEntity224).filter(AcademicsModelEntity224.entity_code == code).first()

class AcademicsRepository225:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity225]:
        return self.db.query(AcademicsModelEntity225).filter(AcademicsModelEntity225.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity225]:
        return self.db.query(AcademicsModelEntity225).filter(AcademicsModelEntity225.entity_code == code).first()

class AcademicsRepository226:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity226]:
        return self.db.query(AcademicsModelEntity226).filter(AcademicsModelEntity226.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity226]:
        return self.db.query(AcademicsModelEntity226).filter(AcademicsModelEntity226.entity_code == code).first()

class AcademicsRepository227:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity227]:
        return self.db.query(AcademicsModelEntity227).filter(AcademicsModelEntity227.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity227]:
        return self.db.query(AcademicsModelEntity227).filter(AcademicsModelEntity227.entity_code == code).first()

class AcademicsRepository228:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity228]:
        return self.db.query(AcademicsModelEntity228).filter(AcademicsModelEntity228.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity228]:
        return self.db.query(AcademicsModelEntity228).filter(AcademicsModelEntity228.entity_code == code).first()

class AcademicsRepository229:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity229]:
        return self.db.query(AcademicsModelEntity229).filter(AcademicsModelEntity229.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity229]:
        return self.db.query(AcademicsModelEntity229).filter(AcademicsModelEntity229.entity_code == code).first()

class AcademicsRepository230:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity230]:
        return self.db.query(AcademicsModelEntity230).filter(AcademicsModelEntity230.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity230]:
        return self.db.query(AcademicsModelEntity230).filter(AcademicsModelEntity230.entity_code == code).first()

class AcademicsRepository231:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity231]:
        return self.db.query(AcademicsModelEntity231).filter(AcademicsModelEntity231.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity231]:
        return self.db.query(AcademicsModelEntity231).filter(AcademicsModelEntity231.entity_code == code).first()

class AcademicsRepository232:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity232]:
        return self.db.query(AcademicsModelEntity232).filter(AcademicsModelEntity232.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity232]:
        return self.db.query(AcademicsModelEntity232).filter(AcademicsModelEntity232.entity_code == code).first()

class AcademicsRepository233:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity233]:
        return self.db.query(AcademicsModelEntity233).filter(AcademicsModelEntity233.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity233]:
        return self.db.query(AcademicsModelEntity233).filter(AcademicsModelEntity233.entity_code == code).first()

class AcademicsRepository234:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity234]:
        return self.db.query(AcademicsModelEntity234).filter(AcademicsModelEntity234.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity234]:
        return self.db.query(AcademicsModelEntity234).filter(AcademicsModelEntity234.entity_code == code).first()

class AcademicsRepository235:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity235]:
        return self.db.query(AcademicsModelEntity235).filter(AcademicsModelEntity235.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity235]:
        return self.db.query(AcademicsModelEntity235).filter(AcademicsModelEntity235.entity_code == code).first()

class AcademicsRepository236:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity236]:
        return self.db.query(AcademicsModelEntity236).filter(AcademicsModelEntity236.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity236]:
        return self.db.query(AcademicsModelEntity236).filter(AcademicsModelEntity236.entity_code == code).first()

class AcademicsRepository237:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity237]:
        return self.db.query(AcademicsModelEntity237).filter(AcademicsModelEntity237.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity237]:
        return self.db.query(AcademicsModelEntity237).filter(AcademicsModelEntity237.entity_code == code).first()

class AcademicsRepository238:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity238]:
        return self.db.query(AcademicsModelEntity238).filter(AcademicsModelEntity238.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity238]:
        return self.db.query(AcademicsModelEntity238).filter(AcademicsModelEntity238.entity_code == code).first()

class AcademicsRepository239:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity239]:
        return self.db.query(AcademicsModelEntity239).filter(AcademicsModelEntity239.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity239]:
        return self.db.query(AcademicsModelEntity239).filter(AcademicsModelEntity239.entity_code == code).first()

class AcademicsRepository240:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity240]:
        return self.db.query(AcademicsModelEntity240).filter(AcademicsModelEntity240.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity240]:
        return self.db.query(AcademicsModelEntity240).filter(AcademicsModelEntity240.entity_code == code).first()

class AcademicsRepository241:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity241]:
        return self.db.query(AcademicsModelEntity241).filter(AcademicsModelEntity241.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity241]:
        return self.db.query(AcademicsModelEntity241).filter(AcademicsModelEntity241.entity_code == code).first()

class AcademicsRepository242:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity242]:
        return self.db.query(AcademicsModelEntity242).filter(AcademicsModelEntity242.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity242]:
        return self.db.query(AcademicsModelEntity242).filter(AcademicsModelEntity242.entity_code == code).first()

class AcademicsRepository243:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity243]:
        return self.db.query(AcademicsModelEntity243).filter(AcademicsModelEntity243.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity243]:
        return self.db.query(AcademicsModelEntity243).filter(AcademicsModelEntity243.entity_code == code).first()

class AcademicsRepository244:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity244]:
        return self.db.query(AcademicsModelEntity244).filter(AcademicsModelEntity244.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity244]:
        return self.db.query(AcademicsModelEntity244).filter(AcademicsModelEntity244.entity_code == code).first()

class AcademicsRepository245:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity245]:
        return self.db.query(AcademicsModelEntity245).filter(AcademicsModelEntity245.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity245]:
        return self.db.query(AcademicsModelEntity245).filter(AcademicsModelEntity245.entity_code == code).first()

class AcademicsRepository246:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity246]:
        return self.db.query(AcademicsModelEntity246).filter(AcademicsModelEntity246.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity246]:
        return self.db.query(AcademicsModelEntity246).filter(AcademicsModelEntity246.entity_code == code).first()

class AcademicsRepository247:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity247]:
        return self.db.query(AcademicsModelEntity247).filter(AcademicsModelEntity247.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity247]:
        return self.db.query(AcademicsModelEntity247).filter(AcademicsModelEntity247.entity_code == code).first()

class AcademicsRepository248:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity248]:
        return self.db.query(AcademicsModelEntity248).filter(AcademicsModelEntity248.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity248]:
        return self.db.query(AcademicsModelEntity248).filter(AcademicsModelEntity248.entity_code == code).first()

class AcademicsRepository249:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity249]:
        return self.db.query(AcademicsModelEntity249).filter(AcademicsModelEntity249.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity249]:
        return self.db.query(AcademicsModelEntity249).filter(AcademicsModelEntity249.entity_code == code).first()

class AcademicsRepository250:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[AcademicsModelEntity250]:
        return self.db.query(AcademicsModelEntity250).filter(AcademicsModelEntity250.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[AcademicsModelEntity250]:
        return self.db.query(AcademicsModelEntity250).filter(AcademicsModelEntity250.entity_code == code).first()

