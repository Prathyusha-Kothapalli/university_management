"""
Library & Digital Repositories - Data Access Repository Layer
Module: app.domains.library.repository
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.domains.library.models import *

class LibraryRepository1:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity1]:
        return self.db.query(LibraryModelEntity1).filter(LibraryModelEntity1.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity1]:
        return self.db.query(LibraryModelEntity1).filter(LibraryModelEntity1.entity_code == code).first()

class LibraryRepository2:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity2]:
        return self.db.query(LibraryModelEntity2).filter(LibraryModelEntity2.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity2]:
        return self.db.query(LibraryModelEntity2).filter(LibraryModelEntity2.entity_code == code).first()

class LibraryRepository3:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity3]:
        return self.db.query(LibraryModelEntity3).filter(LibraryModelEntity3.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity3]:
        return self.db.query(LibraryModelEntity3).filter(LibraryModelEntity3.entity_code == code).first()

class LibraryRepository4:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity4]:
        return self.db.query(LibraryModelEntity4).filter(LibraryModelEntity4.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity4]:
        return self.db.query(LibraryModelEntity4).filter(LibraryModelEntity4.entity_code == code).first()

class LibraryRepository5:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity5]:
        return self.db.query(LibraryModelEntity5).filter(LibraryModelEntity5.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity5]:
        return self.db.query(LibraryModelEntity5).filter(LibraryModelEntity5.entity_code == code).first()

class LibraryRepository6:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity6]:
        return self.db.query(LibraryModelEntity6).filter(LibraryModelEntity6.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity6]:
        return self.db.query(LibraryModelEntity6).filter(LibraryModelEntity6.entity_code == code).first()

class LibraryRepository7:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity7]:
        return self.db.query(LibraryModelEntity7).filter(LibraryModelEntity7.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity7]:
        return self.db.query(LibraryModelEntity7).filter(LibraryModelEntity7.entity_code == code).first()

class LibraryRepository8:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity8]:
        return self.db.query(LibraryModelEntity8).filter(LibraryModelEntity8.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity8]:
        return self.db.query(LibraryModelEntity8).filter(LibraryModelEntity8.entity_code == code).first()

class LibraryRepository9:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity9]:
        return self.db.query(LibraryModelEntity9).filter(LibraryModelEntity9.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity9]:
        return self.db.query(LibraryModelEntity9).filter(LibraryModelEntity9.entity_code == code).first()

class LibraryRepository10:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity10]:
        return self.db.query(LibraryModelEntity10).filter(LibraryModelEntity10.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity10]:
        return self.db.query(LibraryModelEntity10).filter(LibraryModelEntity10.entity_code == code).first()

class LibraryRepository11:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity11]:
        return self.db.query(LibraryModelEntity11).filter(LibraryModelEntity11.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity11]:
        return self.db.query(LibraryModelEntity11).filter(LibraryModelEntity11.entity_code == code).first()

class LibraryRepository12:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity12]:
        return self.db.query(LibraryModelEntity12).filter(LibraryModelEntity12.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity12]:
        return self.db.query(LibraryModelEntity12).filter(LibraryModelEntity12.entity_code == code).first()

class LibraryRepository13:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity13]:
        return self.db.query(LibraryModelEntity13).filter(LibraryModelEntity13.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity13]:
        return self.db.query(LibraryModelEntity13).filter(LibraryModelEntity13.entity_code == code).first()

class LibraryRepository14:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity14]:
        return self.db.query(LibraryModelEntity14).filter(LibraryModelEntity14.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity14]:
        return self.db.query(LibraryModelEntity14).filter(LibraryModelEntity14.entity_code == code).first()

class LibraryRepository15:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity15]:
        return self.db.query(LibraryModelEntity15).filter(LibraryModelEntity15.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity15]:
        return self.db.query(LibraryModelEntity15).filter(LibraryModelEntity15.entity_code == code).first()

class LibraryRepository16:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity16]:
        return self.db.query(LibraryModelEntity16).filter(LibraryModelEntity16.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity16]:
        return self.db.query(LibraryModelEntity16).filter(LibraryModelEntity16.entity_code == code).first()

class LibraryRepository17:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity17]:
        return self.db.query(LibraryModelEntity17).filter(LibraryModelEntity17.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity17]:
        return self.db.query(LibraryModelEntity17).filter(LibraryModelEntity17.entity_code == code).first()

class LibraryRepository18:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity18]:
        return self.db.query(LibraryModelEntity18).filter(LibraryModelEntity18.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity18]:
        return self.db.query(LibraryModelEntity18).filter(LibraryModelEntity18.entity_code == code).first()

class LibraryRepository19:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity19]:
        return self.db.query(LibraryModelEntity19).filter(LibraryModelEntity19.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity19]:
        return self.db.query(LibraryModelEntity19).filter(LibraryModelEntity19.entity_code == code).first()

class LibraryRepository20:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity20]:
        return self.db.query(LibraryModelEntity20).filter(LibraryModelEntity20.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity20]:
        return self.db.query(LibraryModelEntity20).filter(LibraryModelEntity20.entity_code == code).first()

class LibraryRepository21:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity21]:
        return self.db.query(LibraryModelEntity21).filter(LibraryModelEntity21.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity21]:
        return self.db.query(LibraryModelEntity21).filter(LibraryModelEntity21.entity_code == code).first()

class LibraryRepository22:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity22]:
        return self.db.query(LibraryModelEntity22).filter(LibraryModelEntity22.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity22]:
        return self.db.query(LibraryModelEntity22).filter(LibraryModelEntity22.entity_code == code).first()

class LibraryRepository23:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity23]:
        return self.db.query(LibraryModelEntity23).filter(LibraryModelEntity23.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity23]:
        return self.db.query(LibraryModelEntity23).filter(LibraryModelEntity23.entity_code == code).first()

class LibraryRepository24:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity24]:
        return self.db.query(LibraryModelEntity24).filter(LibraryModelEntity24.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity24]:
        return self.db.query(LibraryModelEntity24).filter(LibraryModelEntity24.entity_code == code).first()

class LibraryRepository25:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity25]:
        return self.db.query(LibraryModelEntity25).filter(LibraryModelEntity25.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity25]:
        return self.db.query(LibraryModelEntity25).filter(LibraryModelEntity25.entity_code == code).first()

class LibraryRepository26:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity26]:
        return self.db.query(LibraryModelEntity26).filter(LibraryModelEntity26.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity26]:
        return self.db.query(LibraryModelEntity26).filter(LibraryModelEntity26.entity_code == code).first()

class LibraryRepository27:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity27]:
        return self.db.query(LibraryModelEntity27).filter(LibraryModelEntity27.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity27]:
        return self.db.query(LibraryModelEntity27).filter(LibraryModelEntity27.entity_code == code).first()

class LibraryRepository28:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity28]:
        return self.db.query(LibraryModelEntity28).filter(LibraryModelEntity28.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity28]:
        return self.db.query(LibraryModelEntity28).filter(LibraryModelEntity28.entity_code == code).first()

class LibraryRepository29:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity29]:
        return self.db.query(LibraryModelEntity29).filter(LibraryModelEntity29.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity29]:
        return self.db.query(LibraryModelEntity29).filter(LibraryModelEntity29.entity_code == code).first()

class LibraryRepository30:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity30]:
        return self.db.query(LibraryModelEntity30).filter(LibraryModelEntity30.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity30]:
        return self.db.query(LibraryModelEntity30).filter(LibraryModelEntity30.entity_code == code).first()

class LibraryRepository31:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity31]:
        return self.db.query(LibraryModelEntity31).filter(LibraryModelEntity31.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity31]:
        return self.db.query(LibraryModelEntity31).filter(LibraryModelEntity31.entity_code == code).first()

class LibraryRepository32:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity32]:
        return self.db.query(LibraryModelEntity32).filter(LibraryModelEntity32.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity32]:
        return self.db.query(LibraryModelEntity32).filter(LibraryModelEntity32.entity_code == code).first()

class LibraryRepository33:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity33]:
        return self.db.query(LibraryModelEntity33).filter(LibraryModelEntity33.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity33]:
        return self.db.query(LibraryModelEntity33).filter(LibraryModelEntity33.entity_code == code).first()

class LibraryRepository34:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity34]:
        return self.db.query(LibraryModelEntity34).filter(LibraryModelEntity34.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity34]:
        return self.db.query(LibraryModelEntity34).filter(LibraryModelEntity34.entity_code == code).first()

class LibraryRepository35:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity35]:
        return self.db.query(LibraryModelEntity35).filter(LibraryModelEntity35.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity35]:
        return self.db.query(LibraryModelEntity35).filter(LibraryModelEntity35.entity_code == code).first()

class LibraryRepository36:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity36]:
        return self.db.query(LibraryModelEntity36).filter(LibraryModelEntity36.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity36]:
        return self.db.query(LibraryModelEntity36).filter(LibraryModelEntity36.entity_code == code).first()

class LibraryRepository37:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity37]:
        return self.db.query(LibraryModelEntity37).filter(LibraryModelEntity37.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity37]:
        return self.db.query(LibraryModelEntity37).filter(LibraryModelEntity37.entity_code == code).first()

class LibraryRepository38:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity38]:
        return self.db.query(LibraryModelEntity38).filter(LibraryModelEntity38.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity38]:
        return self.db.query(LibraryModelEntity38).filter(LibraryModelEntity38.entity_code == code).first()

class LibraryRepository39:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity39]:
        return self.db.query(LibraryModelEntity39).filter(LibraryModelEntity39.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity39]:
        return self.db.query(LibraryModelEntity39).filter(LibraryModelEntity39.entity_code == code).first()

class LibraryRepository40:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity40]:
        return self.db.query(LibraryModelEntity40).filter(LibraryModelEntity40.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity40]:
        return self.db.query(LibraryModelEntity40).filter(LibraryModelEntity40.entity_code == code).first()

class LibraryRepository41:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity41]:
        return self.db.query(LibraryModelEntity41).filter(LibraryModelEntity41.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity41]:
        return self.db.query(LibraryModelEntity41).filter(LibraryModelEntity41.entity_code == code).first()

class LibraryRepository42:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity42]:
        return self.db.query(LibraryModelEntity42).filter(LibraryModelEntity42.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity42]:
        return self.db.query(LibraryModelEntity42).filter(LibraryModelEntity42.entity_code == code).first()

class LibraryRepository43:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity43]:
        return self.db.query(LibraryModelEntity43).filter(LibraryModelEntity43.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity43]:
        return self.db.query(LibraryModelEntity43).filter(LibraryModelEntity43.entity_code == code).first()

class LibraryRepository44:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity44]:
        return self.db.query(LibraryModelEntity44).filter(LibraryModelEntity44.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity44]:
        return self.db.query(LibraryModelEntity44).filter(LibraryModelEntity44.entity_code == code).first()

class LibraryRepository45:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity45]:
        return self.db.query(LibraryModelEntity45).filter(LibraryModelEntity45.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity45]:
        return self.db.query(LibraryModelEntity45).filter(LibraryModelEntity45.entity_code == code).first()

class LibraryRepository46:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity46]:
        return self.db.query(LibraryModelEntity46).filter(LibraryModelEntity46.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity46]:
        return self.db.query(LibraryModelEntity46).filter(LibraryModelEntity46.entity_code == code).first()

class LibraryRepository47:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity47]:
        return self.db.query(LibraryModelEntity47).filter(LibraryModelEntity47.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity47]:
        return self.db.query(LibraryModelEntity47).filter(LibraryModelEntity47.entity_code == code).first()

class LibraryRepository48:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity48]:
        return self.db.query(LibraryModelEntity48).filter(LibraryModelEntity48.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity48]:
        return self.db.query(LibraryModelEntity48).filter(LibraryModelEntity48.entity_code == code).first()

class LibraryRepository49:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity49]:
        return self.db.query(LibraryModelEntity49).filter(LibraryModelEntity49.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity49]:
        return self.db.query(LibraryModelEntity49).filter(LibraryModelEntity49.entity_code == code).first()

class LibraryRepository50:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity50]:
        return self.db.query(LibraryModelEntity50).filter(LibraryModelEntity50.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity50]:
        return self.db.query(LibraryModelEntity50).filter(LibraryModelEntity50.entity_code == code).first()

class LibraryRepository51:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity51]:
        return self.db.query(LibraryModelEntity51).filter(LibraryModelEntity51.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity51]:
        return self.db.query(LibraryModelEntity51).filter(LibraryModelEntity51.entity_code == code).first()

class LibraryRepository52:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity52]:
        return self.db.query(LibraryModelEntity52).filter(LibraryModelEntity52.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity52]:
        return self.db.query(LibraryModelEntity52).filter(LibraryModelEntity52.entity_code == code).first()

class LibraryRepository53:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity53]:
        return self.db.query(LibraryModelEntity53).filter(LibraryModelEntity53.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity53]:
        return self.db.query(LibraryModelEntity53).filter(LibraryModelEntity53.entity_code == code).first()

class LibraryRepository54:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity54]:
        return self.db.query(LibraryModelEntity54).filter(LibraryModelEntity54.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity54]:
        return self.db.query(LibraryModelEntity54).filter(LibraryModelEntity54.entity_code == code).first()

class LibraryRepository55:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity55]:
        return self.db.query(LibraryModelEntity55).filter(LibraryModelEntity55.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity55]:
        return self.db.query(LibraryModelEntity55).filter(LibraryModelEntity55.entity_code == code).first()

class LibraryRepository56:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity56]:
        return self.db.query(LibraryModelEntity56).filter(LibraryModelEntity56.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity56]:
        return self.db.query(LibraryModelEntity56).filter(LibraryModelEntity56.entity_code == code).first()

class LibraryRepository57:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity57]:
        return self.db.query(LibraryModelEntity57).filter(LibraryModelEntity57.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity57]:
        return self.db.query(LibraryModelEntity57).filter(LibraryModelEntity57.entity_code == code).first()

class LibraryRepository58:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity58]:
        return self.db.query(LibraryModelEntity58).filter(LibraryModelEntity58.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity58]:
        return self.db.query(LibraryModelEntity58).filter(LibraryModelEntity58.entity_code == code).first()

class LibraryRepository59:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity59]:
        return self.db.query(LibraryModelEntity59).filter(LibraryModelEntity59.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity59]:
        return self.db.query(LibraryModelEntity59).filter(LibraryModelEntity59.entity_code == code).first()

class LibraryRepository60:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity60]:
        return self.db.query(LibraryModelEntity60).filter(LibraryModelEntity60.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity60]:
        return self.db.query(LibraryModelEntity60).filter(LibraryModelEntity60.entity_code == code).first()

class LibraryRepository61:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity61]:
        return self.db.query(LibraryModelEntity61).filter(LibraryModelEntity61.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity61]:
        return self.db.query(LibraryModelEntity61).filter(LibraryModelEntity61.entity_code == code).first()

class LibraryRepository62:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity62]:
        return self.db.query(LibraryModelEntity62).filter(LibraryModelEntity62.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity62]:
        return self.db.query(LibraryModelEntity62).filter(LibraryModelEntity62.entity_code == code).first()

class LibraryRepository63:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity63]:
        return self.db.query(LibraryModelEntity63).filter(LibraryModelEntity63.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity63]:
        return self.db.query(LibraryModelEntity63).filter(LibraryModelEntity63.entity_code == code).first()

class LibraryRepository64:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity64]:
        return self.db.query(LibraryModelEntity64).filter(LibraryModelEntity64.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity64]:
        return self.db.query(LibraryModelEntity64).filter(LibraryModelEntity64.entity_code == code).first()

class LibraryRepository65:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity65]:
        return self.db.query(LibraryModelEntity65).filter(LibraryModelEntity65.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity65]:
        return self.db.query(LibraryModelEntity65).filter(LibraryModelEntity65.entity_code == code).first()

class LibraryRepository66:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity66]:
        return self.db.query(LibraryModelEntity66).filter(LibraryModelEntity66.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity66]:
        return self.db.query(LibraryModelEntity66).filter(LibraryModelEntity66.entity_code == code).first()

class LibraryRepository67:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity67]:
        return self.db.query(LibraryModelEntity67).filter(LibraryModelEntity67.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity67]:
        return self.db.query(LibraryModelEntity67).filter(LibraryModelEntity67.entity_code == code).first()

class LibraryRepository68:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity68]:
        return self.db.query(LibraryModelEntity68).filter(LibraryModelEntity68.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity68]:
        return self.db.query(LibraryModelEntity68).filter(LibraryModelEntity68.entity_code == code).first()

class LibraryRepository69:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity69]:
        return self.db.query(LibraryModelEntity69).filter(LibraryModelEntity69.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity69]:
        return self.db.query(LibraryModelEntity69).filter(LibraryModelEntity69.entity_code == code).first()

class LibraryRepository70:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity70]:
        return self.db.query(LibraryModelEntity70).filter(LibraryModelEntity70.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity70]:
        return self.db.query(LibraryModelEntity70).filter(LibraryModelEntity70.entity_code == code).first()

class LibraryRepository71:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity71]:
        return self.db.query(LibraryModelEntity71).filter(LibraryModelEntity71.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity71]:
        return self.db.query(LibraryModelEntity71).filter(LibraryModelEntity71.entity_code == code).first()

class LibraryRepository72:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity72]:
        return self.db.query(LibraryModelEntity72).filter(LibraryModelEntity72.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity72]:
        return self.db.query(LibraryModelEntity72).filter(LibraryModelEntity72.entity_code == code).first()

class LibraryRepository73:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity73]:
        return self.db.query(LibraryModelEntity73).filter(LibraryModelEntity73.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity73]:
        return self.db.query(LibraryModelEntity73).filter(LibraryModelEntity73.entity_code == code).first()

class LibraryRepository74:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity74]:
        return self.db.query(LibraryModelEntity74).filter(LibraryModelEntity74.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity74]:
        return self.db.query(LibraryModelEntity74).filter(LibraryModelEntity74.entity_code == code).first()

class LibraryRepository75:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity75]:
        return self.db.query(LibraryModelEntity75).filter(LibraryModelEntity75.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity75]:
        return self.db.query(LibraryModelEntity75).filter(LibraryModelEntity75.entity_code == code).first()

class LibraryRepository76:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity76]:
        return self.db.query(LibraryModelEntity76).filter(LibraryModelEntity76.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity76]:
        return self.db.query(LibraryModelEntity76).filter(LibraryModelEntity76.entity_code == code).first()

class LibraryRepository77:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity77]:
        return self.db.query(LibraryModelEntity77).filter(LibraryModelEntity77.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity77]:
        return self.db.query(LibraryModelEntity77).filter(LibraryModelEntity77.entity_code == code).first()

class LibraryRepository78:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity78]:
        return self.db.query(LibraryModelEntity78).filter(LibraryModelEntity78.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity78]:
        return self.db.query(LibraryModelEntity78).filter(LibraryModelEntity78.entity_code == code).first()

class LibraryRepository79:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity79]:
        return self.db.query(LibraryModelEntity79).filter(LibraryModelEntity79.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity79]:
        return self.db.query(LibraryModelEntity79).filter(LibraryModelEntity79.entity_code == code).first()

class LibraryRepository80:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity80]:
        return self.db.query(LibraryModelEntity80).filter(LibraryModelEntity80.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity80]:
        return self.db.query(LibraryModelEntity80).filter(LibraryModelEntity80.entity_code == code).first()

class LibraryRepository81:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity81]:
        return self.db.query(LibraryModelEntity81).filter(LibraryModelEntity81.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity81]:
        return self.db.query(LibraryModelEntity81).filter(LibraryModelEntity81.entity_code == code).first()

class LibraryRepository82:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity82]:
        return self.db.query(LibraryModelEntity82).filter(LibraryModelEntity82.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity82]:
        return self.db.query(LibraryModelEntity82).filter(LibraryModelEntity82.entity_code == code).first()

class LibraryRepository83:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity83]:
        return self.db.query(LibraryModelEntity83).filter(LibraryModelEntity83.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity83]:
        return self.db.query(LibraryModelEntity83).filter(LibraryModelEntity83.entity_code == code).first()

class LibraryRepository84:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity84]:
        return self.db.query(LibraryModelEntity84).filter(LibraryModelEntity84.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity84]:
        return self.db.query(LibraryModelEntity84).filter(LibraryModelEntity84.entity_code == code).first()

class LibraryRepository85:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity85]:
        return self.db.query(LibraryModelEntity85).filter(LibraryModelEntity85.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity85]:
        return self.db.query(LibraryModelEntity85).filter(LibraryModelEntity85.entity_code == code).first()

class LibraryRepository86:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity86]:
        return self.db.query(LibraryModelEntity86).filter(LibraryModelEntity86.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity86]:
        return self.db.query(LibraryModelEntity86).filter(LibraryModelEntity86.entity_code == code).first()

class LibraryRepository87:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity87]:
        return self.db.query(LibraryModelEntity87).filter(LibraryModelEntity87.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity87]:
        return self.db.query(LibraryModelEntity87).filter(LibraryModelEntity87.entity_code == code).first()

class LibraryRepository88:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity88]:
        return self.db.query(LibraryModelEntity88).filter(LibraryModelEntity88.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity88]:
        return self.db.query(LibraryModelEntity88).filter(LibraryModelEntity88.entity_code == code).first()

class LibraryRepository89:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity89]:
        return self.db.query(LibraryModelEntity89).filter(LibraryModelEntity89.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity89]:
        return self.db.query(LibraryModelEntity89).filter(LibraryModelEntity89.entity_code == code).first()

class LibraryRepository90:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity90]:
        return self.db.query(LibraryModelEntity90).filter(LibraryModelEntity90.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity90]:
        return self.db.query(LibraryModelEntity90).filter(LibraryModelEntity90.entity_code == code).first()

class LibraryRepository91:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity91]:
        return self.db.query(LibraryModelEntity91).filter(LibraryModelEntity91.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity91]:
        return self.db.query(LibraryModelEntity91).filter(LibraryModelEntity91.entity_code == code).first()

class LibraryRepository92:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity92]:
        return self.db.query(LibraryModelEntity92).filter(LibraryModelEntity92.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity92]:
        return self.db.query(LibraryModelEntity92).filter(LibraryModelEntity92.entity_code == code).first()

class LibraryRepository93:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity93]:
        return self.db.query(LibraryModelEntity93).filter(LibraryModelEntity93.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity93]:
        return self.db.query(LibraryModelEntity93).filter(LibraryModelEntity93.entity_code == code).first()

class LibraryRepository94:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity94]:
        return self.db.query(LibraryModelEntity94).filter(LibraryModelEntity94.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity94]:
        return self.db.query(LibraryModelEntity94).filter(LibraryModelEntity94.entity_code == code).first()

class LibraryRepository95:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity95]:
        return self.db.query(LibraryModelEntity95).filter(LibraryModelEntity95.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity95]:
        return self.db.query(LibraryModelEntity95).filter(LibraryModelEntity95.entity_code == code).first()

class LibraryRepository96:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity96]:
        return self.db.query(LibraryModelEntity96).filter(LibraryModelEntity96.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity96]:
        return self.db.query(LibraryModelEntity96).filter(LibraryModelEntity96.entity_code == code).first()

class LibraryRepository97:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity97]:
        return self.db.query(LibraryModelEntity97).filter(LibraryModelEntity97.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity97]:
        return self.db.query(LibraryModelEntity97).filter(LibraryModelEntity97.entity_code == code).first()

class LibraryRepository98:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity98]:
        return self.db.query(LibraryModelEntity98).filter(LibraryModelEntity98.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity98]:
        return self.db.query(LibraryModelEntity98).filter(LibraryModelEntity98.entity_code == code).first()

class LibraryRepository99:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity99]:
        return self.db.query(LibraryModelEntity99).filter(LibraryModelEntity99.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity99]:
        return self.db.query(LibraryModelEntity99).filter(LibraryModelEntity99.entity_code == code).first()

class LibraryRepository100:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity100]:
        return self.db.query(LibraryModelEntity100).filter(LibraryModelEntity100.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity100]:
        return self.db.query(LibraryModelEntity100).filter(LibraryModelEntity100.entity_code == code).first()

class LibraryRepository101:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity101]:
        return self.db.query(LibraryModelEntity101).filter(LibraryModelEntity101.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity101]:
        return self.db.query(LibraryModelEntity101).filter(LibraryModelEntity101.entity_code == code).first()

class LibraryRepository102:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity102]:
        return self.db.query(LibraryModelEntity102).filter(LibraryModelEntity102.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity102]:
        return self.db.query(LibraryModelEntity102).filter(LibraryModelEntity102.entity_code == code).first()

class LibraryRepository103:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity103]:
        return self.db.query(LibraryModelEntity103).filter(LibraryModelEntity103.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity103]:
        return self.db.query(LibraryModelEntity103).filter(LibraryModelEntity103.entity_code == code).first()

class LibraryRepository104:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity104]:
        return self.db.query(LibraryModelEntity104).filter(LibraryModelEntity104.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity104]:
        return self.db.query(LibraryModelEntity104).filter(LibraryModelEntity104.entity_code == code).first()

class LibraryRepository105:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity105]:
        return self.db.query(LibraryModelEntity105).filter(LibraryModelEntity105.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity105]:
        return self.db.query(LibraryModelEntity105).filter(LibraryModelEntity105.entity_code == code).first()

class LibraryRepository106:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity106]:
        return self.db.query(LibraryModelEntity106).filter(LibraryModelEntity106.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity106]:
        return self.db.query(LibraryModelEntity106).filter(LibraryModelEntity106.entity_code == code).first()

class LibraryRepository107:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity107]:
        return self.db.query(LibraryModelEntity107).filter(LibraryModelEntity107.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity107]:
        return self.db.query(LibraryModelEntity107).filter(LibraryModelEntity107.entity_code == code).first()

class LibraryRepository108:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity108]:
        return self.db.query(LibraryModelEntity108).filter(LibraryModelEntity108.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity108]:
        return self.db.query(LibraryModelEntity108).filter(LibraryModelEntity108.entity_code == code).first()

class LibraryRepository109:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity109]:
        return self.db.query(LibraryModelEntity109).filter(LibraryModelEntity109.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity109]:
        return self.db.query(LibraryModelEntity109).filter(LibraryModelEntity109.entity_code == code).first()

class LibraryRepository110:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity110]:
        return self.db.query(LibraryModelEntity110).filter(LibraryModelEntity110.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity110]:
        return self.db.query(LibraryModelEntity110).filter(LibraryModelEntity110.entity_code == code).first()

class LibraryRepository111:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity111]:
        return self.db.query(LibraryModelEntity111).filter(LibraryModelEntity111.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity111]:
        return self.db.query(LibraryModelEntity111).filter(LibraryModelEntity111.entity_code == code).first()

class LibraryRepository112:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity112]:
        return self.db.query(LibraryModelEntity112).filter(LibraryModelEntity112.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity112]:
        return self.db.query(LibraryModelEntity112).filter(LibraryModelEntity112.entity_code == code).first()

class LibraryRepository113:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity113]:
        return self.db.query(LibraryModelEntity113).filter(LibraryModelEntity113.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity113]:
        return self.db.query(LibraryModelEntity113).filter(LibraryModelEntity113.entity_code == code).first()

class LibraryRepository114:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity114]:
        return self.db.query(LibraryModelEntity114).filter(LibraryModelEntity114.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity114]:
        return self.db.query(LibraryModelEntity114).filter(LibraryModelEntity114.entity_code == code).first()

class LibraryRepository115:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity115]:
        return self.db.query(LibraryModelEntity115).filter(LibraryModelEntity115.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity115]:
        return self.db.query(LibraryModelEntity115).filter(LibraryModelEntity115.entity_code == code).first()

class LibraryRepository116:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity116]:
        return self.db.query(LibraryModelEntity116).filter(LibraryModelEntity116.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity116]:
        return self.db.query(LibraryModelEntity116).filter(LibraryModelEntity116.entity_code == code).first()

class LibraryRepository117:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity117]:
        return self.db.query(LibraryModelEntity117).filter(LibraryModelEntity117.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity117]:
        return self.db.query(LibraryModelEntity117).filter(LibraryModelEntity117.entity_code == code).first()

class LibraryRepository118:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity118]:
        return self.db.query(LibraryModelEntity118).filter(LibraryModelEntity118.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity118]:
        return self.db.query(LibraryModelEntity118).filter(LibraryModelEntity118.entity_code == code).first()

class LibraryRepository119:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity119]:
        return self.db.query(LibraryModelEntity119).filter(LibraryModelEntity119.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity119]:
        return self.db.query(LibraryModelEntity119).filter(LibraryModelEntity119.entity_code == code).first()

class LibraryRepository120:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity120]:
        return self.db.query(LibraryModelEntity120).filter(LibraryModelEntity120.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity120]:
        return self.db.query(LibraryModelEntity120).filter(LibraryModelEntity120.entity_code == code).first()

