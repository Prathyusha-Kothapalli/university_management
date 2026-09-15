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

class LibraryRepository121:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity121]:
        return self.db.query(LibraryModelEntity121).filter(LibraryModelEntity121.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity121]:
        return self.db.query(LibraryModelEntity121).filter(LibraryModelEntity121.entity_code == code).first()

class LibraryRepository122:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity122]:
        return self.db.query(LibraryModelEntity122).filter(LibraryModelEntity122.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity122]:
        return self.db.query(LibraryModelEntity122).filter(LibraryModelEntity122.entity_code == code).first()

class LibraryRepository123:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity123]:
        return self.db.query(LibraryModelEntity123).filter(LibraryModelEntity123.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity123]:
        return self.db.query(LibraryModelEntity123).filter(LibraryModelEntity123.entity_code == code).first()

class LibraryRepository124:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity124]:
        return self.db.query(LibraryModelEntity124).filter(LibraryModelEntity124.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity124]:
        return self.db.query(LibraryModelEntity124).filter(LibraryModelEntity124.entity_code == code).first()

class LibraryRepository125:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity125]:
        return self.db.query(LibraryModelEntity125).filter(LibraryModelEntity125.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity125]:
        return self.db.query(LibraryModelEntity125).filter(LibraryModelEntity125.entity_code == code).first()

class LibraryRepository126:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity126]:
        return self.db.query(LibraryModelEntity126).filter(LibraryModelEntity126.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity126]:
        return self.db.query(LibraryModelEntity126).filter(LibraryModelEntity126.entity_code == code).first()

class LibraryRepository127:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity127]:
        return self.db.query(LibraryModelEntity127).filter(LibraryModelEntity127.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity127]:
        return self.db.query(LibraryModelEntity127).filter(LibraryModelEntity127.entity_code == code).first()

class LibraryRepository128:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity128]:
        return self.db.query(LibraryModelEntity128).filter(LibraryModelEntity128.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity128]:
        return self.db.query(LibraryModelEntity128).filter(LibraryModelEntity128.entity_code == code).first()

class LibraryRepository129:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity129]:
        return self.db.query(LibraryModelEntity129).filter(LibraryModelEntity129.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity129]:
        return self.db.query(LibraryModelEntity129).filter(LibraryModelEntity129.entity_code == code).first()

class LibraryRepository130:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity130]:
        return self.db.query(LibraryModelEntity130).filter(LibraryModelEntity130.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity130]:
        return self.db.query(LibraryModelEntity130).filter(LibraryModelEntity130.entity_code == code).first()

class LibraryRepository131:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity131]:
        return self.db.query(LibraryModelEntity131).filter(LibraryModelEntity131.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity131]:
        return self.db.query(LibraryModelEntity131).filter(LibraryModelEntity131.entity_code == code).first()

class LibraryRepository132:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity132]:
        return self.db.query(LibraryModelEntity132).filter(LibraryModelEntity132.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity132]:
        return self.db.query(LibraryModelEntity132).filter(LibraryModelEntity132.entity_code == code).first()

class LibraryRepository133:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity133]:
        return self.db.query(LibraryModelEntity133).filter(LibraryModelEntity133.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity133]:
        return self.db.query(LibraryModelEntity133).filter(LibraryModelEntity133.entity_code == code).first()

class LibraryRepository134:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity134]:
        return self.db.query(LibraryModelEntity134).filter(LibraryModelEntity134.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity134]:
        return self.db.query(LibraryModelEntity134).filter(LibraryModelEntity134.entity_code == code).first()

class LibraryRepository135:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity135]:
        return self.db.query(LibraryModelEntity135).filter(LibraryModelEntity135.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity135]:
        return self.db.query(LibraryModelEntity135).filter(LibraryModelEntity135.entity_code == code).first()

class LibraryRepository136:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity136]:
        return self.db.query(LibraryModelEntity136).filter(LibraryModelEntity136.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity136]:
        return self.db.query(LibraryModelEntity136).filter(LibraryModelEntity136.entity_code == code).first()

class LibraryRepository137:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity137]:
        return self.db.query(LibraryModelEntity137).filter(LibraryModelEntity137.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity137]:
        return self.db.query(LibraryModelEntity137).filter(LibraryModelEntity137.entity_code == code).first()

class LibraryRepository138:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity138]:
        return self.db.query(LibraryModelEntity138).filter(LibraryModelEntity138.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity138]:
        return self.db.query(LibraryModelEntity138).filter(LibraryModelEntity138.entity_code == code).first()

class LibraryRepository139:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity139]:
        return self.db.query(LibraryModelEntity139).filter(LibraryModelEntity139.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity139]:
        return self.db.query(LibraryModelEntity139).filter(LibraryModelEntity139.entity_code == code).first()

class LibraryRepository140:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity140]:
        return self.db.query(LibraryModelEntity140).filter(LibraryModelEntity140.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity140]:
        return self.db.query(LibraryModelEntity140).filter(LibraryModelEntity140.entity_code == code).first()

class LibraryRepository141:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity141]:
        return self.db.query(LibraryModelEntity141).filter(LibraryModelEntity141.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity141]:
        return self.db.query(LibraryModelEntity141).filter(LibraryModelEntity141.entity_code == code).first()

class LibraryRepository142:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity142]:
        return self.db.query(LibraryModelEntity142).filter(LibraryModelEntity142.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity142]:
        return self.db.query(LibraryModelEntity142).filter(LibraryModelEntity142.entity_code == code).first()

class LibraryRepository143:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity143]:
        return self.db.query(LibraryModelEntity143).filter(LibraryModelEntity143.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity143]:
        return self.db.query(LibraryModelEntity143).filter(LibraryModelEntity143.entity_code == code).first()

class LibraryRepository144:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity144]:
        return self.db.query(LibraryModelEntity144).filter(LibraryModelEntity144.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity144]:
        return self.db.query(LibraryModelEntity144).filter(LibraryModelEntity144.entity_code == code).first()

class LibraryRepository145:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity145]:
        return self.db.query(LibraryModelEntity145).filter(LibraryModelEntity145.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity145]:
        return self.db.query(LibraryModelEntity145).filter(LibraryModelEntity145.entity_code == code).first()

class LibraryRepository146:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity146]:
        return self.db.query(LibraryModelEntity146).filter(LibraryModelEntity146.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity146]:
        return self.db.query(LibraryModelEntity146).filter(LibraryModelEntity146.entity_code == code).first()

class LibraryRepository147:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity147]:
        return self.db.query(LibraryModelEntity147).filter(LibraryModelEntity147.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity147]:
        return self.db.query(LibraryModelEntity147).filter(LibraryModelEntity147.entity_code == code).first()

class LibraryRepository148:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity148]:
        return self.db.query(LibraryModelEntity148).filter(LibraryModelEntity148.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity148]:
        return self.db.query(LibraryModelEntity148).filter(LibraryModelEntity148.entity_code == code).first()

class LibraryRepository149:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity149]:
        return self.db.query(LibraryModelEntity149).filter(LibraryModelEntity149.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity149]:
        return self.db.query(LibraryModelEntity149).filter(LibraryModelEntity149.entity_code == code).first()

class LibraryRepository150:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity150]:
        return self.db.query(LibraryModelEntity150).filter(LibraryModelEntity150.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity150]:
        return self.db.query(LibraryModelEntity150).filter(LibraryModelEntity150.entity_code == code).first()

class LibraryRepository151:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity151]:
        return self.db.query(LibraryModelEntity151).filter(LibraryModelEntity151.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity151]:
        return self.db.query(LibraryModelEntity151).filter(LibraryModelEntity151.entity_code == code).first()

class LibraryRepository152:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity152]:
        return self.db.query(LibraryModelEntity152).filter(LibraryModelEntity152.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity152]:
        return self.db.query(LibraryModelEntity152).filter(LibraryModelEntity152.entity_code == code).first()

class LibraryRepository153:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity153]:
        return self.db.query(LibraryModelEntity153).filter(LibraryModelEntity153.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity153]:
        return self.db.query(LibraryModelEntity153).filter(LibraryModelEntity153.entity_code == code).first()

class LibraryRepository154:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity154]:
        return self.db.query(LibraryModelEntity154).filter(LibraryModelEntity154.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity154]:
        return self.db.query(LibraryModelEntity154).filter(LibraryModelEntity154.entity_code == code).first()

class LibraryRepository155:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity155]:
        return self.db.query(LibraryModelEntity155).filter(LibraryModelEntity155.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity155]:
        return self.db.query(LibraryModelEntity155).filter(LibraryModelEntity155.entity_code == code).first()

class LibraryRepository156:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity156]:
        return self.db.query(LibraryModelEntity156).filter(LibraryModelEntity156.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity156]:
        return self.db.query(LibraryModelEntity156).filter(LibraryModelEntity156.entity_code == code).first()

class LibraryRepository157:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity157]:
        return self.db.query(LibraryModelEntity157).filter(LibraryModelEntity157.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity157]:
        return self.db.query(LibraryModelEntity157).filter(LibraryModelEntity157.entity_code == code).first()

class LibraryRepository158:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity158]:
        return self.db.query(LibraryModelEntity158).filter(LibraryModelEntity158.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity158]:
        return self.db.query(LibraryModelEntity158).filter(LibraryModelEntity158.entity_code == code).first()

class LibraryRepository159:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity159]:
        return self.db.query(LibraryModelEntity159).filter(LibraryModelEntity159.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity159]:
        return self.db.query(LibraryModelEntity159).filter(LibraryModelEntity159.entity_code == code).first()

class LibraryRepository160:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity160]:
        return self.db.query(LibraryModelEntity160).filter(LibraryModelEntity160.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity160]:
        return self.db.query(LibraryModelEntity160).filter(LibraryModelEntity160.entity_code == code).first()

class LibraryRepository161:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity161]:
        return self.db.query(LibraryModelEntity161).filter(LibraryModelEntity161.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity161]:
        return self.db.query(LibraryModelEntity161).filter(LibraryModelEntity161.entity_code == code).first()

class LibraryRepository162:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity162]:
        return self.db.query(LibraryModelEntity162).filter(LibraryModelEntity162.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity162]:
        return self.db.query(LibraryModelEntity162).filter(LibraryModelEntity162.entity_code == code).first()

class LibraryRepository163:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity163]:
        return self.db.query(LibraryModelEntity163).filter(LibraryModelEntity163.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity163]:
        return self.db.query(LibraryModelEntity163).filter(LibraryModelEntity163.entity_code == code).first()

class LibraryRepository164:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity164]:
        return self.db.query(LibraryModelEntity164).filter(LibraryModelEntity164.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity164]:
        return self.db.query(LibraryModelEntity164).filter(LibraryModelEntity164.entity_code == code).first()

class LibraryRepository165:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity165]:
        return self.db.query(LibraryModelEntity165).filter(LibraryModelEntity165.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity165]:
        return self.db.query(LibraryModelEntity165).filter(LibraryModelEntity165.entity_code == code).first()

class LibraryRepository166:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity166]:
        return self.db.query(LibraryModelEntity166).filter(LibraryModelEntity166.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity166]:
        return self.db.query(LibraryModelEntity166).filter(LibraryModelEntity166.entity_code == code).first()

class LibraryRepository167:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity167]:
        return self.db.query(LibraryModelEntity167).filter(LibraryModelEntity167.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity167]:
        return self.db.query(LibraryModelEntity167).filter(LibraryModelEntity167.entity_code == code).first()

class LibraryRepository168:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity168]:
        return self.db.query(LibraryModelEntity168).filter(LibraryModelEntity168.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity168]:
        return self.db.query(LibraryModelEntity168).filter(LibraryModelEntity168.entity_code == code).first()

class LibraryRepository169:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity169]:
        return self.db.query(LibraryModelEntity169).filter(LibraryModelEntity169.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity169]:
        return self.db.query(LibraryModelEntity169).filter(LibraryModelEntity169.entity_code == code).first()

class LibraryRepository170:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity170]:
        return self.db.query(LibraryModelEntity170).filter(LibraryModelEntity170.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity170]:
        return self.db.query(LibraryModelEntity170).filter(LibraryModelEntity170.entity_code == code).first()

class LibraryRepository171:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity171]:
        return self.db.query(LibraryModelEntity171).filter(LibraryModelEntity171.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity171]:
        return self.db.query(LibraryModelEntity171).filter(LibraryModelEntity171.entity_code == code).first()

class LibraryRepository172:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity172]:
        return self.db.query(LibraryModelEntity172).filter(LibraryModelEntity172.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity172]:
        return self.db.query(LibraryModelEntity172).filter(LibraryModelEntity172.entity_code == code).first()

class LibraryRepository173:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity173]:
        return self.db.query(LibraryModelEntity173).filter(LibraryModelEntity173.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity173]:
        return self.db.query(LibraryModelEntity173).filter(LibraryModelEntity173.entity_code == code).first()

class LibraryRepository174:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity174]:
        return self.db.query(LibraryModelEntity174).filter(LibraryModelEntity174.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity174]:
        return self.db.query(LibraryModelEntity174).filter(LibraryModelEntity174.entity_code == code).first()

class LibraryRepository175:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity175]:
        return self.db.query(LibraryModelEntity175).filter(LibraryModelEntity175.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity175]:
        return self.db.query(LibraryModelEntity175).filter(LibraryModelEntity175.entity_code == code).first()

class LibraryRepository176:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity176]:
        return self.db.query(LibraryModelEntity176).filter(LibraryModelEntity176.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity176]:
        return self.db.query(LibraryModelEntity176).filter(LibraryModelEntity176.entity_code == code).first()

class LibraryRepository177:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity177]:
        return self.db.query(LibraryModelEntity177).filter(LibraryModelEntity177.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity177]:
        return self.db.query(LibraryModelEntity177).filter(LibraryModelEntity177.entity_code == code).first()

class LibraryRepository178:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity178]:
        return self.db.query(LibraryModelEntity178).filter(LibraryModelEntity178.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity178]:
        return self.db.query(LibraryModelEntity178).filter(LibraryModelEntity178.entity_code == code).first()

class LibraryRepository179:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity179]:
        return self.db.query(LibraryModelEntity179).filter(LibraryModelEntity179.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity179]:
        return self.db.query(LibraryModelEntity179).filter(LibraryModelEntity179.entity_code == code).first()

class LibraryRepository180:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity180]:
        return self.db.query(LibraryModelEntity180).filter(LibraryModelEntity180.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity180]:
        return self.db.query(LibraryModelEntity180).filter(LibraryModelEntity180.entity_code == code).first()

class LibraryRepository181:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity181]:
        return self.db.query(LibraryModelEntity181).filter(LibraryModelEntity181.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity181]:
        return self.db.query(LibraryModelEntity181).filter(LibraryModelEntity181.entity_code == code).first()

class LibraryRepository182:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity182]:
        return self.db.query(LibraryModelEntity182).filter(LibraryModelEntity182.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity182]:
        return self.db.query(LibraryModelEntity182).filter(LibraryModelEntity182.entity_code == code).first()

class LibraryRepository183:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity183]:
        return self.db.query(LibraryModelEntity183).filter(LibraryModelEntity183.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity183]:
        return self.db.query(LibraryModelEntity183).filter(LibraryModelEntity183.entity_code == code).first()

class LibraryRepository184:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity184]:
        return self.db.query(LibraryModelEntity184).filter(LibraryModelEntity184.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity184]:
        return self.db.query(LibraryModelEntity184).filter(LibraryModelEntity184.entity_code == code).first()

class LibraryRepository185:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity185]:
        return self.db.query(LibraryModelEntity185).filter(LibraryModelEntity185.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity185]:
        return self.db.query(LibraryModelEntity185).filter(LibraryModelEntity185.entity_code == code).first()

class LibraryRepository186:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity186]:
        return self.db.query(LibraryModelEntity186).filter(LibraryModelEntity186.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity186]:
        return self.db.query(LibraryModelEntity186).filter(LibraryModelEntity186.entity_code == code).first()

class LibraryRepository187:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity187]:
        return self.db.query(LibraryModelEntity187).filter(LibraryModelEntity187.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity187]:
        return self.db.query(LibraryModelEntity187).filter(LibraryModelEntity187.entity_code == code).first()

class LibraryRepository188:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity188]:
        return self.db.query(LibraryModelEntity188).filter(LibraryModelEntity188.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity188]:
        return self.db.query(LibraryModelEntity188).filter(LibraryModelEntity188.entity_code == code).first()

class LibraryRepository189:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity189]:
        return self.db.query(LibraryModelEntity189).filter(LibraryModelEntity189.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity189]:
        return self.db.query(LibraryModelEntity189).filter(LibraryModelEntity189.entity_code == code).first()

class LibraryRepository190:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity190]:
        return self.db.query(LibraryModelEntity190).filter(LibraryModelEntity190.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity190]:
        return self.db.query(LibraryModelEntity190).filter(LibraryModelEntity190.entity_code == code).first()

class LibraryRepository191:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity191]:
        return self.db.query(LibraryModelEntity191).filter(LibraryModelEntity191.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity191]:
        return self.db.query(LibraryModelEntity191).filter(LibraryModelEntity191.entity_code == code).first()

class LibraryRepository192:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity192]:
        return self.db.query(LibraryModelEntity192).filter(LibraryModelEntity192.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity192]:
        return self.db.query(LibraryModelEntity192).filter(LibraryModelEntity192.entity_code == code).first()

class LibraryRepository193:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity193]:
        return self.db.query(LibraryModelEntity193).filter(LibraryModelEntity193.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity193]:
        return self.db.query(LibraryModelEntity193).filter(LibraryModelEntity193.entity_code == code).first()

class LibraryRepository194:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity194]:
        return self.db.query(LibraryModelEntity194).filter(LibraryModelEntity194.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity194]:
        return self.db.query(LibraryModelEntity194).filter(LibraryModelEntity194.entity_code == code).first()

class LibraryRepository195:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity195]:
        return self.db.query(LibraryModelEntity195).filter(LibraryModelEntity195.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity195]:
        return self.db.query(LibraryModelEntity195).filter(LibraryModelEntity195.entity_code == code).first()

class LibraryRepository196:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity196]:
        return self.db.query(LibraryModelEntity196).filter(LibraryModelEntity196.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity196]:
        return self.db.query(LibraryModelEntity196).filter(LibraryModelEntity196.entity_code == code).first()

class LibraryRepository197:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity197]:
        return self.db.query(LibraryModelEntity197).filter(LibraryModelEntity197.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity197]:
        return self.db.query(LibraryModelEntity197).filter(LibraryModelEntity197.entity_code == code).first()

class LibraryRepository198:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity198]:
        return self.db.query(LibraryModelEntity198).filter(LibraryModelEntity198.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity198]:
        return self.db.query(LibraryModelEntity198).filter(LibraryModelEntity198.entity_code == code).first()

class LibraryRepository199:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity199]:
        return self.db.query(LibraryModelEntity199).filter(LibraryModelEntity199.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity199]:
        return self.db.query(LibraryModelEntity199).filter(LibraryModelEntity199.entity_code == code).first()

class LibraryRepository200:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity200]:
        return self.db.query(LibraryModelEntity200).filter(LibraryModelEntity200.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity200]:
        return self.db.query(LibraryModelEntity200).filter(LibraryModelEntity200.entity_code == code).first()

class LibraryRepository201:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity201]:
        return self.db.query(LibraryModelEntity201).filter(LibraryModelEntity201.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity201]:
        return self.db.query(LibraryModelEntity201).filter(LibraryModelEntity201.entity_code == code).first()

class LibraryRepository202:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity202]:
        return self.db.query(LibraryModelEntity202).filter(LibraryModelEntity202.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity202]:
        return self.db.query(LibraryModelEntity202).filter(LibraryModelEntity202.entity_code == code).first()

class LibraryRepository203:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity203]:
        return self.db.query(LibraryModelEntity203).filter(LibraryModelEntity203.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity203]:
        return self.db.query(LibraryModelEntity203).filter(LibraryModelEntity203.entity_code == code).first()

class LibraryRepository204:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity204]:
        return self.db.query(LibraryModelEntity204).filter(LibraryModelEntity204.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity204]:
        return self.db.query(LibraryModelEntity204).filter(LibraryModelEntity204.entity_code == code).first()

class LibraryRepository205:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity205]:
        return self.db.query(LibraryModelEntity205).filter(LibraryModelEntity205.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity205]:
        return self.db.query(LibraryModelEntity205).filter(LibraryModelEntity205.entity_code == code).first()

class LibraryRepository206:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity206]:
        return self.db.query(LibraryModelEntity206).filter(LibraryModelEntity206.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity206]:
        return self.db.query(LibraryModelEntity206).filter(LibraryModelEntity206.entity_code == code).first()

class LibraryRepository207:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity207]:
        return self.db.query(LibraryModelEntity207).filter(LibraryModelEntity207.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity207]:
        return self.db.query(LibraryModelEntity207).filter(LibraryModelEntity207.entity_code == code).first()

class LibraryRepository208:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity208]:
        return self.db.query(LibraryModelEntity208).filter(LibraryModelEntity208.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity208]:
        return self.db.query(LibraryModelEntity208).filter(LibraryModelEntity208.entity_code == code).first()

class LibraryRepository209:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity209]:
        return self.db.query(LibraryModelEntity209).filter(LibraryModelEntity209.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity209]:
        return self.db.query(LibraryModelEntity209).filter(LibraryModelEntity209.entity_code == code).first()

class LibraryRepository210:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity210]:
        return self.db.query(LibraryModelEntity210).filter(LibraryModelEntity210.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity210]:
        return self.db.query(LibraryModelEntity210).filter(LibraryModelEntity210.entity_code == code).first()

class LibraryRepository211:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity211]:
        return self.db.query(LibraryModelEntity211).filter(LibraryModelEntity211.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity211]:
        return self.db.query(LibraryModelEntity211).filter(LibraryModelEntity211.entity_code == code).first()

class LibraryRepository212:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity212]:
        return self.db.query(LibraryModelEntity212).filter(LibraryModelEntity212.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity212]:
        return self.db.query(LibraryModelEntity212).filter(LibraryModelEntity212.entity_code == code).first()

class LibraryRepository213:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity213]:
        return self.db.query(LibraryModelEntity213).filter(LibraryModelEntity213.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity213]:
        return self.db.query(LibraryModelEntity213).filter(LibraryModelEntity213.entity_code == code).first()

class LibraryRepository214:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity214]:
        return self.db.query(LibraryModelEntity214).filter(LibraryModelEntity214.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity214]:
        return self.db.query(LibraryModelEntity214).filter(LibraryModelEntity214.entity_code == code).first()

class LibraryRepository215:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity215]:
        return self.db.query(LibraryModelEntity215).filter(LibraryModelEntity215.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity215]:
        return self.db.query(LibraryModelEntity215).filter(LibraryModelEntity215.entity_code == code).first()

class LibraryRepository216:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity216]:
        return self.db.query(LibraryModelEntity216).filter(LibraryModelEntity216.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity216]:
        return self.db.query(LibraryModelEntity216).filter(LibraryModelEntity216.entity_code == code).first()

class LibraryRepository217:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity217]:
        return self.db.query(LibraryModelEntity217).filter(LibraryModelEntity217.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity217]:
        return self.db.query(LibraryModelEntity217).filter(LibraryModelEntity217.entity_code == code).first()

class LibraryRepository218:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity218]:
        return self.db.query(LibraryModelEntity218).filter(LibraryModelEntity218.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity218]:
        return self.db.query(LibraryModelEntity218).filter(LibraryModelEntity218.entity_code == code).first()

class LibraryRepository219:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity219]:
        return self.db.query(LibraryModelEntity219).filter(LibraryModelEntity219.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity219]:
        return self.db.query(LibraryModelEntity219).filter(LibraryModelEntity219.entity_code == code).first()

class LibraryRepository220:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity220]:
        return self.db.query(LibraryModelEntity220).filter(LibraryModelEntity220.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity220]:
        return self.db.query(LibraryModelEntity220).filter(LibraryModelEntity220.entity_code == code).first()

class LibraryRepository221:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity221]:
        return self.db.query(LibraryModelEntity221).filter(LibraryModelEntity221.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity221]:
        return self.db.query(LibraryModelEntity221).filter(LibraryModelEntity221.entity_code == code).first()

class LibraryRepository222:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity222]:
        return self.db.query(LibraryModelEntity222).filter(LibraryModelEntity222.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity222]:
        return self.db.query(LibraryModelEntity222).filter(LibraryModelEntity222.entity_code == code).first()

class LibraryRepository223:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity223]:
        return self.db.query(LibraryModelEntity223).filter(LibraryModelEntity223.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity223]:
        return self.db.query(LibraryModelEntity223).filter(LibraryModelEntity223.entity_code == code).first()

class LibraryRepository224:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity224]:
        return self.db.query(LibraryModelEntity224).filter(LibraryModelEntity224.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity224]:
        return self.db.query(LibraryModelEntity224).filter(LibraryModelEntity224.entity_code == code).first()

class LibraryRepository225:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity225]:
        return self.db.query(LibraryModelEntity225).filter(LibraryModelEntity225.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity225]:
        return self.db.query(LibraryModelEntity225).filter(LibraryModelEntity225.entity_code == code).first()

class LibraryRepository226:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity226]:
        return self.db.query(LibraryModelEntity226).filter(LibraryModelEntity226.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity226]:
        return self.db.query(LibraryModelEntity226).filter(LibraryModelEntity226.entity_code == code).first()

class LibraryRepository227:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity227]:
        return self.db.query(LibraryModelEntity227).filter(LibraryModelEntity227.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity227]:
        return self.db.query(LibraryModelEntity227).filter(LibraryModelEntity227.entity_code == code).first()

class LibraryRepository228:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity228]:
        return self.db.query(LibraryModelEntity228).filter(LibraryModelEntity228.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity228]:
        return self.db.query(LibraryModelEntity228).filter(LibraryModelEntity228.entity_code == code).first()

class LibraryRepository229:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity229]:
        return self.db.query(LibraryModelEntity229).filter(LibraryModelEntity229.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity229]:
        return self.db.query(LibraryModelEntity229).filter(LibraryModelEntity229.entity_code == code).first()

class LibraryRepository230:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity230]:
        return self.db.query(LibraryModelEntity230).filter(LibraryModelEntity230.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity230]:
        return self.db.query(LibraryModelEntity230).filter(LibraryModelEntity230.entity_code == code).first()

class LibraryRepository231:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity231]:
        return self.db.query(LibraryModelEntity231).filter(LibraryModelEntity231.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity231]:
        return self.db.query(LibraryModelEntity231).filter(LibraryModelEntity231.entity_code == code).first()

class LibraryRepository232:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity232]:
        return self.db.query(LibraryModelEntity232).filter(LibraryModelEntity232.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity232]:
        return self.db.query(LibraryModelEntity232).filter(LibraryModelEntity232.entity_code == code).first()

class LibraryRepository233:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity233]:
        return self.db.query(LibraryModelEntity233).filter(LibraryModelEntity233.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity233]:
        return self.db.query(LibraryModelEntity233).filter(LibraryModelEntity233.entity_code == code).first()

class LibraryRepository234:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity234]:
        return self.db.query(LibraryModelEntity234).filter(LibraryModelEntity234.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity234]:
        return self.db.query(LibraryModelEntity234).filter(LibraryModelEntity234.entity_code == code).first()

class LibraryRepository235:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity235]:
        return self.db.query(LibraryModelEntity235).filter(LibraryModelEntity235.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity235]:
        return self.db.query(LibraryModelEntity235).filter(LibraryModelEntity235.entity_code == code).first()

class LibraryRepository236:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity236]:
        return self.db.query(LibraryModelEntity236).filter(LibraryModelEntity236.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity236]:
        return self.db.query(LibraryModelEntity236).filter(LibraryModelEntity236.entity_code == code).first()

class LibraryRepository237:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity237]:
        return self.db.query(LibraryModelEntity237).filter(LibraryModelEntity237.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity237]:
        return self.db.query(LibraryModelEntity237).filter(LibraryModelEntity237.entity_code == code).first()

class LibraryRepository238:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity238]:
        return self.db.query(LibraryModelEntity238).filter(LibraryModelEntity238.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity238]:
        return self.db.query(LibraryModelEntity238).filter(LibraryModelEntity238.entity_code == code).first()

class LibraryRepository239:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity239]:
        return self.db.query(LibraryModelEntity239).filter(LibraryModelEntity239.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity239]:
        return self.db.query(LibraryModelEntity239).filter(LibraryModelEntity239.entity_code == code).first()

class LibraryRepository240:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity240]:
        return self.db.query(LibraryModelEntity240).filter(LibraryModelEntity240.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity240]:
        return self.db.query(LibraryModelEntity240).filter(LibraryModelEntity240.entity_code == code).first()

class LibraryRepository241:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity241]:
        return self.db.query(LibraryModelEntity241).filter(LibraryModelEntity241.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity241]:
        return self.db.query(LibraryModelEntity241).filter(LibraryModelEntity241.entity_code == code).first()

class LibraryRepository242:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity242]:
        return self.db.query(LibraryModelEntity242).filter(LibraryModelEntity242.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity242]:
        return self.db.query(LibraryModelEntity242).filter(LibraryModelEntity242.entity_code == code).first()

class LibraryRepository243:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity243]:
        return self.db.query(LibraryModelEntity243).filter(LibraryModelEntity243.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity243]:
        return self.db.query(LibraryModelEntity243).filter(LibraryModelEntity243.entity_code == code).first()

class LibraryRepository244:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity244]:
        return self.db.query(LibraryModelEntity244).filter(LibraryModelEntity244.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity244]:
        return self.db.query(LibraryModelEntity244).filter(LibraryModelEntity244.entity_code == code).first()

class LibraryRepository245:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity245]:
        return self.db.query(LibraryModelEntity245).filter(LibraryModelEntity245.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity245]:
        return self.db.query(LibraryModelEntity245).filter(LibraryModelEntity245.entity_code == code).first()

class LibraryRepository246:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity246]:
        return self.db.query(LibraryModelEntity246).filter(LibraryModelEntity246.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity246]:
        return self.db.query(LibraryModelEntity246).filter(LibraryModelEntity246.entity_code == code).first()

class LibraryRepository247:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity247]:
        return self.db.query(LibraryModelEntity247).filter(LibraryModelEntity247.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity247]:
        return self.db.query(LibraryModelEntity247).filter(LibraryModelEntity247.entity_code == code).first()

class LibraryRepository248:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity248]:
        return self.db.query(LibraryModelEntity248).filter(LibraryModelEntity248.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity248]:
        return self.db.query(LibraryModelEntity248).filter(LibraryModelEntity248.entity_code == code).first()

class LibraryRepository249:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity249]:
        return self.db.query(LibraryModelEntity249).filter(LibraryModelEntity249.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity249]:
        return self.db.query(LibraryModelEntity249).filter(LibraryModelEntity249.entity_code == code).first()

class LibraryRepository250:
    def __init__(self, db: Session):
        self.db = db

    def query_all(self, limit: int = 50) -> List[LibraryModelEntity250]:
        return self.db.query(LibraryModelEntity250).filter(LibraryModelEntity250.is_active == True).limit(limit).all()

    def find_by_code(self, code: str) -> Optional[LibraryModelEntity250]:
        return self.db.query(LibraryModelEntity250).filter(LibraryModelEntity250.entity_code == code).first()

