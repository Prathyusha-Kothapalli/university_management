"""
Transport & Fleet Logistics - FastAPI Router Endpoints
Module: app.domains.transport.router
"""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domains.transport.schemas import *
from app.domains.transport.service import TransportDomainService

router = APIRouter(prefix="/transport", tags=["Transport & Fleet Logistics"])

@router.get("/entity-1", response_model=List[TransportSchemaEntity1Response])
def list_entities_1(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_1_list(skip=skip, limit=limit)

@router.get("/entity-1/{entity_id}", response_model=TransportSchemaEntity1Response)
def get_entity_1(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_1_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 1 not found")
    return res

@router.post("/entity-1", response_model=TransportSchemaEntity1Response, status_code=201)
def create_entity_1(payload: TransportSchemaEntity1Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_1(payload)

@router.get("/entity-2", response_model=List[TransportSchemaEntity2Response])
def list_entities_2(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_2_list(skip=skip, limit=limit)

@router.get("/entity-2/{entity_id}", response_model=TransportSchemaEntity2Response)
def get_entity_2(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_2_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 2 not found")
    return res

@router.post("/entity-2", response_model=TransportSchemaEntity2Response, status_code=201)
def create_entity_2(payload: TransportSchemaEntity2Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_2(payload)

@router.get("/entity-3", response_model=List[TransportSchemaEntity3Response])
def list_entities_3(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_3_list(skip=skip, limit=limit)

@router.get("/entity-3/{entity_id}", response_model=TransportSchemaEntity3Response)
def get_entity_3(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_3_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 3 not found")
    return res

@router.post("/entity-3", response_model=TransportSchemaEntity3Response, status_code=201)
def create_entity_3(payload: TransportSchemaEntity3Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_3(payload)

@router.get("/entity-4", response_model=List[TransportSchemaEntity4Response])
def list_entities_4(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_4_list(skip=skip, limit=limit)

@router.get("/entity-4/{entity_id}", response_model=TransportSchemaEntity4Response)
def get_entity_4(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_4_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 4 not found")
    return res

@router.post("/entity-4", response_model=TransportSchemaEntity4Response, status_code=201)
def create_entity_4(payload: TransportSchemaEntity4Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_4(payload)

@router.get("/entity-5", response_model=List[TransportSchemaEntity5Response])
def list_entities_5(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_5_list(skip=skip, limit=limit)

@router.get("/entity-5/{entity_id}", response_model=TransportSchemaEntity5Response)
def get_entity_5(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_5_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 5 not found")
    return res

@router.post("/entity-5", response_model=TransportSchemaEntity5Response, status_code=201)
def create_entity_5(payload: TransportSchemaEntity5Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_5(payload)

@router.get("/entity-6", response_model=List[TransportSchemaEntity6Response])
def list_entities_6(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_6_list(skip=skip, limit=limit)

@router.get("/entity-6/{entity_id}", response_model=TransportSchemaEntity6Response)
def get_entity_6(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_6_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 6 not found")
    return res

@router.post("/entity-6", response_model=TransportSchemaEntity6Response, status_code=201)
def create_entity_6(payload: TransportSchemaEntity6Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_6(payload)

@router.get("/entity-7", response_model=List[TransportSchemaEntity7Response])
def list_entities_7(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_7_list(skip=skip, limit=limit)

@router.get("/entity-7/{entity_id}", response_model=TransportSchemaEntity7Response)
def get_entity_7(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_7_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 7 not found")
    return res

@router.post("/entity-7", response_model=TransportSchemaEntity7Response, status_code=201)
def create_entity_7(payload: TransportSchemaEntity7Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_7(payload)

@router.get("/entity-8", response_model=List[TransportSchemaEntity8Response])
def list_entities_8(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_8_list(skip=skip, limit=limit)

@router.get("/entity-8/{entity_id}", response_model=TransportSchemaEntity8Response)
def get_entity_8(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_8_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 8 not found")
    return res

@router.post("/entity-8", response_model=TransportSchemaEntity8Response, status_code=201)
def create_entity_8(payload: TransportSchemaEntity8Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_8(payload)

@router.get("/entity-9", response_model=List[TransportSchemaEntity9Response])
def list_entities_9(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_9_list(skip=skip, limit=limit)

@router.get("/entity-9/{entity_id}", response_model=TransportSchemaEntity9Response)
def get_entity_9(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_9_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 9 not found")
    return res

@router.post("/entity-9", response_model=TransportSchemaEntity9Response, status_code=201)
def create_entity_9(payload: TransportSchemaEntity9Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_9(payload)

@router.get("/entity-10", response_model=List[TransportSchemaEntity10Response])
def list_entities_10(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_10_list(skip=skip, limit=limit)

@router.get("/entity-10/{entity_id}", response_model=TransportSchemaEntity10Response)
def get_entity_10(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_10_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 10 not found")
    return res

@router.post("/entity-10", response_model=TransportSchemaEntity10Response, status_code=201)
def create_entity_10(payload: TransportSchemaEntity10Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_10(payload)

@router.get("/entity-11", response_model=List[TransportSchemaEntity11Response])
def list_entities_11(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_11_list(skip=skip, limit=limit)

@router.get("/entity-11/{entity_id}", response_model=TransportSchemaEntity11Response)
def get_entity_11(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_11_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 11 not found")
    return res

@router.post("/entity-11", response_model=TransportSchemaEntity11Response, status_code=201)
def create_entity_11(payload: TransportSchemaEntity11Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_11(payload)

@router.get("/entity-12", response_model=List[TransportSchemaEntity12Response])
def list_entities_12(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_12_list(skip=skip, limit=limit)

@router.get("/entity-12/{entity_id}", response_model=TransportSchemaEntity12Response)
def get_entity_12(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_12_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 12 not found")
    return res

@router.post("/entity-12", response_model=TransportSchemaEntity12Response, status_code=201)
def create_entity_12(payload: TransportSchemaEntity12Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_12(payload)

@router.get("/entity-13", response_model=List[TransportSchemaEntity13Response])
def list_entities_13(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_13_list(skip=skip, limit=limit)

@router.get("/entity-13/{entity_id}", response_model=TransportSchemaEntity13Response)
def get_entity_13(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_13_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 13 not found")
    return res

@router.post("/entity-13", response_model=TransportSchemaEntity13Response, status_code=201)
def create_entity_13(payload: TransportSchemaEntity13Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_13(payload)

@router.get("/entity-14", response_model=List[TransportSchemaEntity14Response])
def list_entities_14(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_14_list(skip=skip, limit=limit)

@router.get("/entity-14/{entity_id}", response_model=TransportSchemaEntity14Response)
def get_entity_14(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_14_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 14 not found")
    return res

@router.post("/entity-14", response_model=TransportSchemaEntity14Response, status_code=201)
def create_entity_14(payload: TransportSchemaEntity14Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_14(payload)

@router.get("/entity-15", response_model=List[TransportSchemaEntity15Response])
def list_entities_15(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_15_list(skip=skip, limit=limit)

@router.get("/entity-15/{entity_id}", response_model=TransportSchemaEntity15Response)
def get_entity_15(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_15_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 15 not found")
    return res

@router.post("/entity-15", response_model=TransportSchemaEntity15Response, status_code=201)
def create_entity_15(payload: TransportSchemaEntity15Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_15(payload)

@router.get("/entity-16", response_model=List[TransportSchemaEntity16Response])
def list_entities_16(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_16_list(skip=skip, limit=limit)

@router.get("/entity-16/{entity_id}", response_model=TransportSchemaEntity16Response)
def get_entity_16(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_16_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 16 not found")
    return res

@router.post("/entity-16", response_model=TransportSchemaEntity16Response, status_code=201)
def create_entity_16(payload: TransportSchemaEntity16Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_16(payload)

@router.get("/entity-17", response_model=List[TransportSchemaEntity17Response])
def list_entities_17(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_17_list(skip=skip, limit=limit)

@router.get("/entity-17/{entity_id}", response_model=TransportSchemaEntity17Response)
def get_entity_17(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_17_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 17 not found")
    return res

@router.post("/entity-17", response_model=TransportSchemaEntity17Response, status_code=201)
def create_entity_17(payload: TransportSchemaEntity17Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_17(payload)

@router.get("/entity-18", response_model=List[TransportSchemaEntity18Response])
def list_entities_18(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_18_list(skip=skip, limit=limit)

@router.get("/entity-18/{entity_id}", response_model=TransportSchemaEntity18Response)
def get_entity_18(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_18_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 18 not found")
    return res

@router.post("/entity-18", response_model=TransportSchemaEntity18Response, status_code=201)
def create_entity_18(payload: TransportSchemaEntity18Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_18(payload)

@router.get("/entity-19", response_model=List[TransportSchemaEntity19Response])
def list_entities_19(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_19_list(skip=skip, limit=limit)

@router.get("/entity-19/{entity_id}", response_model=TransportSchemaEntity19Response)
def get_entity_19(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_19_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 19 not found")
    return res

@router.post("/entity-19", response_model=TransportSchemaEntity19Response, status_code=201)
def create_entity_19(payload: TransportSchemaEntity19Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_19(payload)

@router.get("/entity-20", response_model=List[TransportSchemaEntity20Response])
def list_entities_20(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_20_list(skip=skip, limit=limit)

@router.get("/entity-20/{entity_id}", response_model=TransportSchemaEntity20Response)
def get_entity_20(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_20_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 20 not found")
    return res

@router.post("/entity-20", response_model=TransportSchemaEntity20Response, status_code=201)
def create_entity_20(payload: TransportSchemaEntity20Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_20(payload)

@router.get("/entity-21", response_model=List[TransportSchemaEntity21Response])
def list_entities_21(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_21_list(skip=skip, limit=limit)

@router.get("/entity-21/{entity_id}", response_model=TransportSchemaEntity21Response)
def get_entity_21(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_21_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 21 not found")
    return res

@router.post("/entity-21", response_model=TransportSchemaEntity21Response, status_code=201)
def create_entity_21(payload: TransportSchemaEntity21Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_21(payload)

@router.get("/entity-22", response_model=List[TransportSchemaEntity22Response])
def list_entities_22(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_22_list(skip=skip, limit=limit)

@router.get("/entity-22/{entity_id}", response_model=TransportSchemaEntity22Response)
def get_entity_22(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_22_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 22 not found")
    return res

@router.post("/entity-22", response_model=TransportSchemaEntity22Response, status_code=201)
def create_entity_22(payload: TransportSchemaEntity22Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_22(payload)

@router.get("/entity-23", response_model=List[TransportSchemaEntity23Response])
def list_entities_23(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_23_list(skip=skip, limit=limit)

@router.get("/entity-23/{entity_id}", response_model=TransportSchemaEntity23Response)
def get_entity_23(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_23_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 23 not found")
    return res

@router.post("/entity-23", response_model=TransportSchemaEntity23Response, status_code=201)
def create_entity_23(payload: TransportSchemaEntity23Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_23(payload)

@router.get("/entity-24", response_model=List[TransportSchemaEntity24Response])
def list_entities_24(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_24_list(skip=skip, limit=limit)

@router.get("/entity-24/{entity_id}", response_model=TransportSchemaEntity24Response)
def get_entity_24(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_24_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 24 not found")
    return res

@router.post("/entity-24", response_model=TransportSchemaEntity24Response, status_code=201)
def create_entity_24(payload: TransportSchemaEntity24Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_24(payload)

@router.get("/entity-25", response_model=List[TransportSchemaEntity25Response])
def list_entities_25(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_25_list(skip=skip, limit=limit)

@router.get("/entity-25/{entity_id}", response_model=TransportSchemaEntity25Response)
def get_entity_25(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_25_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 25 not found")
    return res

@router.post("/entity-25", response_model=TransportSchemaEntity25Response, status_code=201)
def create_entity_25(payload: TransportSchemaEntity25Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_25(payload)

@router.get("/entity-26", response_model=List[TransportSchemaEntity26Response])
def list_entities_26(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_26_list(skip=skip, limit=limit)

@router.get("/entity-26/{entity_id}", response_model=TransportSchemaEntity26Response)
def get_entity_26(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_26_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 26 not found")
    return res

@router.post("/entity-26", response_model=TransportSchemaEntity26Response, status_code=201)
def create_entity_26(payload: TransportSchemaEntity26Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_26(payload)

@router.get("/entity-27", response_model=List[TransportSchemaEntity27Response])
def list_entities_27(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_27_list(skip=skip, limit=limit)

@router.get("/entity-27/{entity_id}", response_model=TransportSchemaEntity27Response)
def get_entity_27(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_27_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 27 not found")
    return res

@router.post("/entity-27", response_model=TransportSchemaEntity27Response, status_code=201)
def create_entity_27(payload: TransportSchemaEntity27Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_27(payload)

@router.get("/entity-28", response_model=List[TransportSchemaEntity28Response])
def list_entities_28(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_28_list(skip=skip, limit=limit)

@router.get("/entity-28/{entity_id}", response_model=TransportSchemaEntity28Response)
def get_entity_28(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_28_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 28 not found")
    return res

@router.post("/entity-28", response_model=TransportSchemaEntity28Response, status_code=201)
def create_entity_28(payload: TransportSchemaEntity28Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_28(payload)

@router.get("/entity-29", response_model=List[TransportSchemaEntity29Response])
def list_entities_29(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_29_list(skip=skip, limit=limit)

@router.get("/entity-29/{entity_id}", response_model=TransportSchemaEntity29Response)
def get_entity_29(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_29_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 29 not found")
    return res

@router.post("/entity-29", response_model=TransportSchemaEntity29Response, status_code=201)
def create_entity_29(payload: TransportSchemaEntity29Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_29(payload)

@router.get("/entity-30", response_model=List[TransportSchemaEntity30Response])
def list_entities_30(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_30_list(skip=skip, limit=limit)

@router.get("/entity-30/{entity_id}", response_model=TransportSchemaEntity30Response)
def get_entity_30(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_30_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 30 not found")
    return res

@router.post("/entity-30", response_model=TransportSchemaEntity30Response, status_code=201)
def create_entity_30(payload: TransportSchemaEntity30Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_30(payload)

@router.get("/entity-31", response_model=List[TransportSchemaEntity31Response])
def list_entities_31(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_31_list(skip=skip, limit=limit)

@router.get("/entity-31/{entity_id}", response_model=TransportSchemaEntity31Response)
def get_entity_31(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_31_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 31 not found")
    return res

@router.post("/entity-31", response_model=TransportSchemaEntity31Response, status_code=201)
def create_entity_31(payload: TransportSchemaEntity31Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_31(payload)

@router.get("/entity-32", response_model=List[TransportSchemaEntity32Response])
def list_entities_32(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_32_list(skip=skip, limit=limit)

@router.get("/entity-32/{entity_id}", response_model=TransportSchemaEntity32Response)
def get_entity_32(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_32_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 32 not found")
    return res

@router.post("/entity-32", response_model=TransportSchemaEntity32Response, status_code=201)
def create_entity_32(payload: TransportSchemaEntity32Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_32(payload)

@router.get("/entity-33", response_model=List[TransportSchemaEntity33Response])
def list_entities_33(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_33_list(skip=skip, limit=limit)

@router.get("/entity-33/{entity_id}", response_model=TransportSchemaEntity33Response)
def get_entity_33(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_33_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 33 not found")
    return res

@router.post("/entity-33", response_model=TransportSchemaEntity33Response, status_code=201)
def create_entity_33(payload: TransportSchemaEntity33Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_33(payload)

@router.get("/entity-34", response_model=List[TransportSchemaEntity34Response])
def list_entities_34(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_34_list(skip=skip, limit=limit)

@router.get("/entity-34/{entity_id}", response_model=TransportSchemaEntity34Response)
def get_entity_34(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_34_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 34 not found")
    return res

@router.post("/entity-34", response_model=TransportSchemaEntity34Response, status_code=201)
def create_entity_34(payload: TransportSchemaEntity34Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_34(payload)

@router.get("/entity-35", response_model=List[TransportSchemaEntity35Response])
def list_entities_35(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_35_list(skip=skip, limit=limit)

@router.get("/entity-35/{entity_id}", response_model=TransportSchemaEntity35Response)
def get_entity_35(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_35_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 35 not found")
    return res

@router.post("/entity-35", response_model=TransportSchemaEntity35Response, status_code=201)
def create_entity_35(payload: TransportSchemaEntity35Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_35(payload)

@router.get("/entity-36", response_model=List[TransportSchemaEntity36Response])
def list_entities_36(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_36_list(skip=skip, limit=limit)

@router.get("/entity-36/{entity_id}", response_model=TransportSchemaEntity36Response)
def get_entity_36(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_36_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 36 not found")
    return res

@router.post("/entity-36", response_model=TransportSchemaEntity36Response, status_code=201)
def create_entity_36(payload: TransportSchemaEntity36Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_36(payload)

@router.get("/entity-37", response_model=List[TransportSchemaEntity37Response])
def list_entities_37(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_37_list(skip=skip, limit=limit)

@router.get("/entity-37/{entity_id}", response_model=TransportSchemaEntity37Response)
def get_entity_37(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_37_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 37 not found")
    return res

@router.post("/entity-37", response_model=TransportSchemaEntity37Response, status_code=201)
def create_entity_37(payload: TransportSchemaEntity37Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_37(payload)

@router.get("/entity-38", response_model=List[TransportSchemaEntity38Response])
def list_entities_38(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_38_list(skip=skip, limit=limit)

@router.get("/entity-38/{entity_id}", response_model=TransportSchemaEntity38Response)
def get_entity_38(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_38_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 38 not found")
    return res

@router.post("/entity-38", response_model=TransportSchemaEntity38Response, status_code=201)
def create_entity_38(payload: TransportSchemaEntity38Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_38(payload)

@router.get("/entity-39", response_model=List[TransportSchemaEntity39Response])
def list_entities_39(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_39_list(skip=skip, limit=limit)

@router.get("/entity-39/{entity_id}", response_model=TransportSchemaEntity39Response)
def get_entity_39(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_39_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 39 not found")
    return res

@router.post("/entity-39", response_model=TransportSchemaEntity39Response, status_code=201)
def create_entity_39(payload: TransportSchemaEntity39Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_39(payload)

@router.get("/entity-40", response_model=List[TransportSchemaEntity40Response])
def list_entities_40(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_40_list(skip=skip, limit=limit)

@router.get("/entity-40/{entity_id}", response_model=TransportSchemaEntity40Response)
def get_entity_40(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_40_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 40 not found")
    return res

@router.post("/entity-40", response_model=TransportSchemaEntity40Response, status_code=201)
def create_entity_40(payload: TransportSchemaEntity40Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_40(payload)

@router.get("/entity-41", response_model=List[TransportSchemaEntity41Response])
def list_entities_41(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_41_list(skip=skip, limit=limit)

@router.get("/entity-41/{entity_id}", response_model=TransportSchemaEntity41Response)
def get_entity_41(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_41_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 41 not found")
    return res

@router.post("/entity-41", response_model=TransportSchemaEntity41Response, status_code=201)
def create_entity_41(payload: TransportSchemaEntity41Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_41(payload)

@router.get("/entity-42", response_model=List[TransportSchemaEntity42Response])
def list_entities_42(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_42_list(skip=skip, limit=limit)

@router.get("/entity-42/{entity_id}", response_model=TransportSchemaEntity42Response)
def get_entity_42(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_42_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 42 not found")
    return res

@router.post("/entity-42", response_model=TransportSchemaEntity42Response, status_code=201)
def create_entity_42(payload: TransportSchemaEntity42Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_42(payload)

@router.get("/entity-43", response_model=List[TransportSchemaEntity43Response])
def list_entities_43(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_43_list(skip=skip, limit=limit)

@router.get("/entity-43/{entity_id}", response_model=TransportSchemaEntity43Response)
def get_entity_43(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_43_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 43 not found")
    return res

@router.post("/entity-43", response_model=TransportSchemaEntity43Response, status_code=201)
def create_entity_43(payload: TransportSchemaEntity43Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_43(payload)

@router.get("/entity-44", response_model=List[TransportSchemaEntity44Response])
def list_entities_44(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_44_list(skip=skip, limit=limit)

@router.get("/entity-44/{entity_id}", response_model=TransportSchemaEntity44Response)
def get_entity_44(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_44_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 44 not found")
    return res

@router.post("/entity-44", response_model=TransportSchemaEntity44Response, status_code=201)
def create_entity_44(payload: TransportSchemaEntity44Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_44(payload)

@router.get("/entity-45", response_model=List[TransportSchemaEntity45Response])
def list_entities_45(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_45_list(skip=skip, limit=limit)

@router.get("/entity-45/{entity_id}", response_model=TransportSchemaEntity45Response)
def get_entity_45(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_45_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 45 not found")
    return res

@router.post("/entity-45", response_model=TransportSchemaEntity45Response, status_code=201)
def create_entity_45(payload: TransportSchemaEntity45Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_45(payload)

@router.get("/entity-46", response_model=List[TransportSchemaEntity46Response])
def list_entities_46(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_46_list(skip=skip, limit=limit)

@router.get("/entity-46/{entity_id}", response_model=TransportSchemaEntity46Response)
def get_entity_46(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_46_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 46 not found")
    return res

@router.post("/entity-46", response_model=TransportSchemaEntity46Response, status_code=201)
def create_entity_46(payload: TransportSchemaEntity46Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_46(payload)

@router.get("/entity-47", response_model=List[TransportSchemaEntity47Response])
def list_entities_47(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_47_list(skip=skip, limit=limit)

@router.get("/entity-47/{entity_id}", response_model=TransportSchemaEntity47Response)
def get_entity_47(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_47_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 47 not found")
    return res

@router.post("/entity-47", response_model=TransportSchemaEntity47Response, status_code=201)
def create_entity_47(payload: TransportSchemaEntity47Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_47(payload)

@router.get("/entity-48", response_model=List[TransportSchemaEntity48Response])
def list_entities_48(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_48_list(skip=skip, limit=limit)

@router.get("/entity-48/{entity_id}", response_model=TransportSchemaEntity48Response)
def get_entity_48(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_48_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 48 not found")
    return res

@router.post("/entity-48", response_model=TransportSchemaEntity48Response, status_code=201)
def create_entity_48(payload: TransportSchemaEntity48Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_48(payload)

@router.get("/entity-49", response_model=List[TransportSchemaEntity49Response])
def list_entities_49(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_49_list(skip=skip, limit=limit)

@router.get("/entity-49/{entity_id}", response_model=TransportSchemaEntity49Response)
def get_entity_49(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_49_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 49 not found")
    return res

@router.post("/entity-49", response_model=TransportSchemaEntity49Response, status_code=201)
def create_entity_49(payload: TransportSchemaEntity49Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_49(payload)

@router.get("/entity-50", response_model=List[TransportSchemaEntity50Response])
def list_entities_50(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_50_list(skip=skip, limit=limit)

@router.get("/entity-50/{entity_id}", response_model=TransportSchemaEntity50Response)
def get_entity_50(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_50_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 50 not found")
    return res

@router.post("/entity-50", response_model=TransportSchemaEntity50Response, status_code=201)
def create_entity_50(payload: TransportSchemaEntity50Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_50(payload)

@router.get("/entity-51", response_model=List[TransportSchemaEntity51Response])
def list_entities_51(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_51_list(skip=skip, limit=limit)

@router.get("/entity-51/{entity_id}", response_model=TransportSchemaEntity51Response)
def get_entity_51(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_51_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 51 not found")
    return res

@router.post("/entity-51", response_model=TransportSchemaEntity51Response, status_code=201)
def create_entity_51(payload: TransportSchemaEntity51Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_51(payload)

@router.get("/entity-52", response_model=List[TransportSchemaEntity52Response])
def list_entities_52(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_52_list(skip=skip, limit=limit)

@router.get("/entity-52/{entity_id}", response_model=TransportSchemaEntity52Response)
def get_entity_52(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_52_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 52 not found")
    return res

@router.post("/entity-52", response_model=TransportSchemaEntity52Response, status_code=201)
def create_entity_52(payload: TransportSchemaEntity52Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_52(payload)

@router.get("/entity-53", response_model=List[TransportSchemaEntity53Response])
def list_entities_53(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_53_list(skip=skip, limit=limit)

@router.get("/entity-53/{entity_id}", response_model=TransportSchemaEntity53Response)
def get_entity_53(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_53_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 53 not found")
    return res

@router.post("/entity-53", response_model=TransportSchemaEntity53Response, status_code=201)
def create_entity_53(payload: TransportSchemaEntity53Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_53(payload)

@router.get("/entity-54", response_model=List[TransportSchemaEntity54Response])
def list_entities_54(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_54_list(skip=skip, limit=limit)

@router.get("/entity-54/{entity_id}", response_model=TransportSchemaEntity54Response)
def get_entity_54(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_54_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 54 not found")
    return res

@router.post("/entity-54", response_model=TransportSchemaEntity54Response, status_code=201)
def create_entity_54(payload: TransportSchemaEntity54Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_54(payload)

@router.get("/entity-55", response_model=List[TransportSchemaEntity55Response])
def list_entities_55(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_55_list(skip=skip, limit=limit)

@router.get("/entity-55/{entity_id}", response_model=TransportSchemaEntity55Response)
def get_entity_55(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_55_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 55 not found")
    return res

@router.post("/entity-55", response_model=TransportSchemaEntity55Response, status_code=201)
def create_entity_55(payload: TransportSchemaEntity55Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_55(payload)

@router.get("/entity-56", response_model=List[TransportSchemaEntity56Response])
def list_entities_56(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_56_list(skip=skip, limit=limit)

@router.get("/entity-56/{entity_id}", response_model=TransportSchemaEntity56Response)
def get_entity_56(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_56_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 56 not found")
    return res

@router.post("/entity-56", response_model=TransportSchemaEntity56Response, status_code=201)
def create_entity_56(payload: TransportSchemaEntity56Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_56(payload)

@router.get("/entity-57", response_model=List[TransportSchemaEntity57Response])
def list_entities_57(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_57_list(skip=skip, limit=limit)

@router.get("/entity-57/{entity_id}", response_model=TransportSchemaEntity57Response)
def get_entity_57(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_57_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 57 not found")
    return res

@router.post("/entity-57", response_model=TransportSchemaEntity57Response, status_code=201)
def create_entity_57(payload: TransportSchemaEntity57Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_57(payload)

@router.get("/entity-58", response_model=List[TransportSchemaEntity58Response])
def list_entities_58(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_58_list(skip=skip, limit=limit)

@router.get("/entity-58/{entity_id}", response_model=TransportSchemaEntity58Response)
def get_entity_58(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_58_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 58 not found")
    return res

@router.post("/entity-58", response_model=TransportSchemaEntity58Response, status_code=201)
def create_entity_58(payload: TransportSchemaEntity58Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_58(payload)

@router.get("/entity-59", response_model=List[TransportSchemaEntity59Response])
def list_entities_59(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_59_list(skip=skip, limit=limit)

@router.get("/entity-59/{entity_id}", response_model=TransportSchemaEntity59Response)
def get_entity_59(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_59_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 59 not found")
    return res

@router.post("/entity-59", response_model=TransportSchemaEntity59Response, status_code=201)
def create_entity_59(payload: TransportSchemaEntity59Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_59(payload)

@router.get("/entity-60", response_model=List[TransportSchemaEntity60Response])
def list_entities_60(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_60_list(skip=skip, limit=limit)

@router.get("/entity-60/{entity_id}", response_model=TransportSchemaEntity60Response)
def get_entity_60(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_60_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 60 not found")
    return res

@router.post("/entity-60", response_model=TransportSchemaEntity60Response, status_code=201)
def create_entity_60(payload: TransportSchemaEntity60Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_60(payload)

@router.get("/entity-61", response_model=List[TransportSchemaEntity61Response])
def list_entities_61(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_61_list(skip=skip, limit=limit)

@router.get("/entity-61/{entity_id}", response_model=TransportSchemaEntity61Response)
def get_entity_61(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_61_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 61 not found")
    return res

@router.post("/entity-61", response_model=TransportSchemaEntity61Response, status_code=201)
def create_entity_61(payload: TransportSchemaEntity61Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_61(payload)

@router.get("/entity-62", response_model=List[TransportSchemaEntity62Response])
def list_entities_62(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_62_list(skip=skip, limit=limit)

@router.get("/entity-62/{entity_id}", response_model=TransportSchemaEntity62Response)
def get_entity_62(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_62_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 62 not found")
    return res

@router.post("/entity-62", response_model=TransportSchemaEntity62Response, status_code=201)
def create_entity_62(payload: TransportSchemaEntity62Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_62(payload)

@router.get("/entity-63", response_model=List[TransportSchemaEntity63Response])
def list_entities_63(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_63_list(skip=skip, limit=limit)

@router.get("/entity-63/{entity_id}", response_model=TransportSchemaEntity63Response)
def get_entity_63(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_63_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 63 not found")
    return res

@router.post("/entity-63", response_model=TransportSchemaEntity63Response, status_code=201)
def create_entity_63(payload: TransportSchemaEntity63Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_63(payload)

@router.get("/entity-64", response_model=List[TransportSchemaEntity64Response])
def list_entities_64(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_64_list(skip=skip, limit=limit)

@router.get("/entity-64/{entity_id}", response_model=TransportSchemaEntity64Response)
def get_entity_64(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_64_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 64 not found")
    return res

@router.post("/entity-64", response_model=TransportSchemaEntity64Response, status_code=201)
def create_entity_64(payload: TransportSchemaEntity64Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_64(payload)

@router.get("/entity-65", response_model=List[TransportSchemaEntity65Response])
def list_entities_65(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_65_list(skip=skip, limit=limit)

@router.get("/entity-65/{entity_id}", response_model=TransportSchemaEntity65Response)
def get_entity_65(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_65_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 65 not found")
    return res

@router.post("/entity-65", response_model=TransportSchemaEntity65Response, status_code=201)
def create_entity_65(payload: TransportSchemaEntity65Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_65(payload)

@router.get("/entity-66", response_model=List[TransportSchemaEntity66Response])
def list_entities_66(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_66_list(skip=skip, limit=limit)

@router.get("/entity-66/{entity_id}", response_model=TransportSchemaEntity66Response)
def get_entity_66(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_66_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 66 not found")
    return res

@router.post("/entity-66", response_model=TransportSchemaEntity66Response, status_code=201)
def create_entity_66(payload: TransportSchemaEntity66Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_66(payload)

@router.get("/entity-67", response_model=List[TransportSchemaEntity67Response])
def list_entities_67(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_67_list(skip=skip, limit=limit)

@router.get("/entity-67/{entity_id}", response_model=TransportSchemaEntity67Response)
def get_entity_67(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_67_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 67 not found")
    return res

@router.post("/entity-67", response_model=TransportSchemaEntity67Response, status_code=201)
def create_entity_67(payload: TransportSchemaEntity67Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_67(payload)

@router.get("/entity-68", response_model=List[TransportSchemaEntity68Response])
def list_entities_68(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_68_list(skip=skip, limit=limit)

@router.get("/entity-68/{entity_id}", response_model=TransportSchemaEntity68Response)
def get_entity_68(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_68_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 68 not found")
    return res

@router.post("/entity-68", response_model=TransportSchemaEntity68Response, status_code=201)
def create_entity_68(payload: TransportSchemaEntity68Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_68(payload)

@router.get("/entity-69", response_model=List[TransportSchemaEntity69Response])
def list_entities_69(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_69_list(skip=skip, limit=limit)

@router.get("/entity-69/{entity_id}", response_model=TransportSchemaEntity69Response)
def get_entity_69(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_69_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 69 not found")
    return res

@router.post("/entity-69", response_model=TransportSchemaEntity69Response, status_code=201)
def create_entity_69(payload: TransportSchemaEntity69Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_69(payload)

@router.get("/entity-70", response_model=List[TransportSchemaEntity70Response])
def list_entities_70(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_70_list(skip=skip, limit=limit)

@router.get("/entity-70/{entity_id}", response_model=TransportSchemaEntity70Response)
def get_entity_70(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_70_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 70 not found")
    return res

@router.post("/entity-70", response_model=TransportSchemaEntity70Response, status_code=201)
def create_entity_70(payload: TransportSchemaEntity70Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_70(payload)

@router.get("/entity-71", response_model=List[TransportSchemaEntity71Response])
def list_entities_71(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_71_list(skip=skip, limit=limit)

@router.get("/entity-71/{entity_id}", response_model=TransportSchemaEntity71Response)
def get_entity_71(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_71_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 71 not found")
    return res

@router.post("/entity-71", response_model=TransportSchemaEntity71Response, status_code=201)
def create_entity_71(payload: TransportSchemaEntity71Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_71(payload)

@router.get("/entity-72", response_model=List[TransportSchemaEntity72Response])
def list_entities_72(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_72_list(skip=skip, limit=limit)

@router.get("/entity-72/{entity_id}", response_model=TransportSchemaEntity72Response)
def get_entity_72(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_72_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 72 not found")
    return res

@router.post("/entity-72", response_model=TransportSchemaEntity72Response, status_code=201)
def create_entity_72(payload: TransportSchemaEntity72Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_72(payload)

@router.get("/entity-73", response_model=List[TransportSchemaEntity73Response])
def list_entities_73(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_73_list(skip=skip, limit=limit)

@router.get("/entity-73/{entity_id}", response_model=TransportSchemaEntity73Response)
def get_entity_73(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_73_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 73 not found")
    return res

@router.post("/entity-73", response_model=TransportSchemaEntity73Response, status_code=201)
def create_entity_73(payload: TransportSchemaEntity73Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_73(payload)

@router.get("/entity-74", response_model=List[TransportSchemaEntity74Response])
def list_entities_74(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_74_list(skip=skip, limit=limit)

@router.get("/entity-74/{entity_id}", response_model=TransportSchemaEntity74Response)
def get_entity_74(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_74_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 74 not found")
    return res

@router.post("/entity-74", response_model=TransportSchemaEntity74Response, status_code=201)
def create_entity_74(payload: TransportSchemaEntity74Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_74(payload)

@router.get("/entity-75", response_model=List[TransportSchemaEntity75Response])
def list_entities_75(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_75_list(skip=skip, limit=limit)

@router.get("/entity-75/{entity_id}", response_model=TransportSchemaEntity75Response)
def get_entity_75(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_75_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 75 not found")
    return res

@router.post("/entity-75", response_model=TransportSchemaEntity75Response, status_code=201)
def create_entity_75(payload: TransportSchemaEntity75Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_75(payload)

@router.get("/entity-76", response_model=List[TransportSchemaEntity76Response])
def list_entities_76(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_76_list(skip=skip, limit=limit)

@router.get("/entity-76/{entity_id}", response_model=TransportSchemaEntity76Response)
def get_entity_76(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_76_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 76 not found")
    return res

@router.post("/entity-76", response_model=TransportSchemaEntity76Response, status_code=201)
def create_entity_76(payload: TransportSchemaEntity76Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_76(payload)

@router.get("/entity-77", response_model=List[TransportSchemaEntity77Response])
def list_entities_77(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_77_list(skip=skip, limit=limit)

@router.get("/entity-77/{entity_id}", response_model=TransportSchemaEntity77Response)
def get_entity_77(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_77_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 77 not found")
    return res

@router.post("/entity-77", response_model=TransportSchemaEntity77Response, status_code=201)
def create_entity_77(payload: TransportSchemaEntity77Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_77(payload)

@router.get("/entity-78", response_model=List[TransportSchemaEntity78Response])
def list_entities_78(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_78_list(skip=skip, limit=limit)

@router.get("/entity-78/{entity_id}", response_model=TransportSchemaEntity78Response)
def get_entity_78(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_78_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 78 not found")
    return res

@router.post("/entity-78", response_model=TransportSchemaEntity78Response, status_code=201)
def create_entity_78(payload: TransportSchemaEntity78Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_78(payload)

@router.get("/entity-79", response_model=List[TransportSchemaEntity79Response])
def list_entities_79(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_79_list(skip=skip, limit=limit)

@router.get("/entity-79/{entity_id}", response_model=TransportSchemaEntity79Response)
def get_entity_79(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_79_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 79 not found")
    return res

@router.post("/entity-79", response_model=TransportSchemaEntity79Response, status_code=201)
def create_entity_79(payload: TransportSchemaEntity79Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_79(payload)

@router.get("/entity-80", response_model=List[TransportSchemaEntity80Response])
def list_entities_80(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_80_list(skip=skip, limit=limit)

@router.get("/entity-80/{entity_id}", response_model=TransportSchemaEntity80Response)
def get_entity_80(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_80_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 80 not found")
    return res

@router.post("/entity-80", response_model=TransportSchemaEntity80Response, status_code=201)
def create_entity_80(payload: TransportSchemaEntity80Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_80(payload)

@router.get("/entity-81", response_model=List[TransportSchemaEntity81Response])
def list_entities_81(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_81_list(skip=skip, limit=limit)

@router.get("/entity-81/{entity_id}", response_model=TransportSchemaEntity81Response)
def get_entity_81(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_81_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 81 not found")
    return res

@router.post("/entity-81", response_model=TransportSchemaEntity81Response, status_code=201)
def create_entity_81(payload: TransportSchemaEntity81Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_81(payload)

@router.get("/entity-82", response_model=List[TransportSchemaEntity82Response])
def list_entities_82(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_82_list(skip=skip, limit=limit)

@router.get("/entity-82/{entity_id}", response_model=TransportSchemaEntity82Response)
def get_entity_82(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_82_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 82 not found")
    return res

@router.post("/entity-82", response_model=TransportSchemaEntity82Response, status_code=201)
def create_entity_82(payload: TransportSchemaEntity82Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_82(payload)

@router.get("/entity-83", response_model=List[TransportSchemaEntity83Response])
def list_entities_83(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_83_list(skip=skip, limit=limit)

@router.get("/entity-83/{entity_id}", response_model=TransportSchemaEntity83Response)
def get_entity_83(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_83_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 83 not found")
    return res

@router.post("/entity-83", response_model=TransportSchemaEntity83Response, status_code=201)
def create_entity_83(payload: TransportSchemaEntity83Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_83(payload)

@router.get("/entity-84", response_model=List[TransportSchemaEntity84Response])
def list_entities_84(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_84_list(skip=skip, limit=limit)

@router.get("/entity-84/{entity_id}", response_model=TransportSchemaEntity84Response)
def get_entity_84(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_84_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 84 not found")
    return res

@router.post("/entity-84", response_model=TransportSchemaEntity84Response, status_code=201)
def create_entity_84(payload: TransportSchemaEntity84Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_84(payload)

@router.get("/entity-85", response_model=List[TransportSchemaEntity85Response])
def list_entities_85(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_85_list(skip=skip, limit=limit)

@router.get("/entity-85/{entity_id}", response_model=TransportSchemaEntity85Response)
def get_entity_85(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_85_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 85 not found")
    return res

@router.post("/entity-85", response_model=TransportSchemaEntity85Response, status_code=201)
def create_entity_85(payload: TransportSchemaEntity85Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_85(payload)

@router.get("/entity-86", response_model=List[TransportSchemaEntity86Response])
def list_entities_86(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_86_list(skip=skip, limit=limit)

@router.get("/entity-86/{entity_id}", response_model=TransportSchemaEntity86Response)
def get_entity_86(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_86_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 86 not found")
    return res

@router.post("/entity-86", response_model=TransportSchemaEntity86Response, status_code=201)
def create_entity_86(payload: TransportSchemaEntity86Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_86(payload)

@router.get("/entity-87", response_model=List[TransportSchemaEntity87Response])
def list_entities_87(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_87_list(skip=skip, limit=limit)

@router.get("/entity-87/{entity_id}", response_model=TransportSchemaEntity87Response)
def get_entity_87(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_87_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 87 not found")
    return res

@router.post("/entity-87", response_model=TransportSchemaEntity87Response, status_code=201)
def create_entity_87(payload: TransportSchemaEntity87Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_87(payload)

@router.get("/entity-88", response_model=List[TransportSchemaEntity88Response])
def list_entities_88(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_88_list(skip=skip, limit=limit)

@router.get("/entity-88/{entity_id}", response_model=TransportSchemaEntity88Response)
def get_entity_88(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_88_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 88 not found")
    return res

@router.post("/entity-88", response_model=TransportSchemaEntity88Response, status_code=201)
def create_entity_88(payload: TransportSchemaEntity88Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_88(payload)

@router.get("/entity-89", response_model=List[TransportSchemaEntity89Response])
def list_entities_89(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_89_list(skip=skip, limit=limit)

@router.get("/entity-89/{entity_id}", response_model=TransportSchemaEntity89Response)
def get_entity_89(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_89_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 89 not found")
    return res

@router.post("/entity-89", response_model=TransportSchemaEntity89Response, status_code=201)
def create_entity_89(payload: TransportSchemaEntity89Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_89(payload)

@router.get("/entity-90", response_model=List[TransportSchemaEntity90Response])
def list_entities_90(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_90_list(skip=skip, limit=limit)

@router.get("/entity-90/{entity_id}", response_model=TransportSchemaEntity90Response)
def get_entity_90(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_90_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 90 not found")
    return res

@router.post("/entity-90", response_model=TransportSchemaEntity90Response, status_code=201)
def create_entity_90(payload: TransportSchemaEntity90Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_90(payload)

@router.get("/entity-91", response_model=List[TransportSchemaEntity91Response])
def list_entities_91(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_91_list(skip=skip, limit=limit)

@router.get("/entity-91/{entity_id}", response_model=TransportSchemaEntity91Response)
def get_entity_91(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_91_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 91 not found")
    return res

@router.post("/entity-91", response_model=TransportSchemaEntity91Response, status_code=201)
def create_entity_91(payload: TransportSchemaEntity91Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_91(payload)

@router.get("/entity-92", response_model=List[TransportSchemaEntity92Response])
def list_entities_92(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_92_list(skip=skip, limit=limit)

@router.get("/entity-92/{entity_id}", response_model=TransportSchemaEntity92Response)
def get_entity_92(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_92_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 92 not found")
    return res

@router.post("/entity-92", response_model=TransportSchemaEntity92Response, status_code=201)
def create_entity_92(payload: TransportSchemaEntity92Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_92(payload)

@router.get("/entity-93", response_model=List[TransportSchemaEntity93Response])
def list_entities_93(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_93_list(skip=skip, limit=limit)

@router.get("/entity-93/{entity_id}", response_model=TransportSchemaEntity93Response)
def get_entity_93(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_93_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 93 not found")
    return res

@router.post("/entity-93", response_model=TransportSchemaEntity93Response, status_code=201)
def create_entity_93(payload: TransportSchemaEntity93Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_93(payload)

@router.get("/entity-94", response_model=List[TransportSchemaEntity94Response])
def list_entities_94(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_94_list(skip=skip, limit=limit)

@router.get("/entity-94/{entity_id}", response_model=TransportSchemaEntity94Response)
def get_entity_94(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_94_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 94 not found")
    return res

@router.post("/entity-94", response_model=TransportSchemaEntity94Response, status_code=201)
def create_entity_94(payload: TransportSchemaEntity94Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_94(payload)

@router.get("/entity-95", response_model=List[TransportSchemaEntity95Response])
def list_entities_95(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_95_list(skip=skip, limit=limit)

@router.get("/entity-95/{entity_id}", response_model=TransportSchemaEntity95Response)
def get_entity_95(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_95_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 95 not found")
    return res

@router.post("/entity-95", response_model=TransportSchemaEntity95Response, status_code=201)
def create_entity_95(payload: TransportSchemaEntity95Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_95(payload)

@router.get("/entity-96", response_model=List[TransportSchemaEntity96Response])
def list_entities_96(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_96_list(skip=skip, limit=limit)

@router.get("/entity-96/{entity_id}", response_model=TransportSchemaEntity96Response)
def get_entity_96(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_96_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 96 not found")
    return res

@router.post("/entity-96", response_model=TransportSchemaEntity96Response, status_code=201)
def create_entity_96(payload: TransportSchemaEntity96Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_96(payload)

@router.get("/entity-97", response_model=List[TransportSchemaEntity97Response])
def list_entities_97(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_97_list(skip=skip, limit=limit)

@router.get("/entity-97/{entity_id}", response_model=TransportSchemaEntity97Response)
def get_entity_97(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_97_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 97 not found")
    return res

@router.post("/entity-97", response_model=TransportSchemaEntity97Response, status_code=201)
def create_entity_97(payload: TransportSchemaEntity97Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_97(payload)

@router.get("/entity-98", response_model=List[TransportSchemaEntity98Response])
def list_entities_98(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_98_list(skip=skip, limit=limit)

@router.get("/entity-98/{entity_id}", response_model=TransportSchemaEntity98Response)
def get_entity_98(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_98_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 98 not found")
    return res

@router.post("/entity-98", response_model=TransportSchemaEntity98Response, status_code=201)
def create_entity_98(payload: TransportSchemaEntity98Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_98(payload)

@router.get("/entity-99", response_model=List[TransportSchemaEntity99Response])
def list_entities_99(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_99_list(skip=skip, limit=limit)

@router.get("/entity-99/{entity_id}", response_model=TransportSchemaEntity99Response)
def get_entity_99(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_99_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 99 not found")
    return res

@router.post("/entity-99", response_model=TransportSchemaEntity99Response, status_code=201)
def create_entity_99(payload: TransportSchemaEntity99Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_99(payload)

@router.get("/entity-100", response_model=List[TransportSchemaEntity100Response])
def list_entities_100(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_100_list(skip=skip, limit=limit)

@router.get("/entity-100/{entity_id}", response_model=TransportSchemaEntity100Response)
def get_entity_100(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_100_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 100 not found")
    return res

@router.post("/entity-100", response_model=TransportSchemaEntity100Response, status_code=201)
def create_entity_100(payload: TransportSchemaEntity100Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_100(payload)

@router.get("/entity-101", response_model=List[TransportSchemaEntity101Response])
def list_entities_101(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_101_list(skip=skip, limit=limit)

@router.get("/entity-101/{entity_id}", response_model=TransportSchemaEntity101Response)
def get_entity_101(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_101_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 101 not found")
    return res

@router.post("/entity-101", response_model=TransportSchemaEntity101Response, status_code=201)
def create_entity_101(payload: TransportSchemaEntity101Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_101(payload)

@router.get("/entity-102", response_model=List[TransportSchemaEntity102Response])
def list_entities_102(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_102_list(skip=skip, limit=limit)

@router.get("/entity-102/{entity_id}", response_model=TransportSchemaEntity102Response)
def get_entity_102(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_102_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 102 not found")
    return res

@router.post("/entity-102", response_model=TransportSchemaEntity102Response, status_code=201)
def create_entity_102(payload: TransportSchemaEntity102Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_102(payload)

@router.get("/entity-103", response_model=List[TransportSchemaEntity103Response])
def list_entities_103(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_103_list(skip=skip, limit=limit)

@router.get("/entity-103/{entity_id}", response_model=TransportSchemaEntity103Response)
def get_entity_103(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_103_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 103 not found")
    return res

@router.post("/entity-103", response_model=TransportSchemaEntity103Response, status_code=201)
def create_entity_103(payload: TransportSchemaEntity103Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_103(payload)

@router.get("/entity-104", response_model=List[TransportSchemaEntity104Response])
def list_entities_104(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_104_list(skip=skip, limit=limit)

@router.get("/entity-104/{entity_id}", response_model=TransportSchemaEntity104Response)
def get_entity_104(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_104_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 104 not found")
    return res

@router.post("/entity-104", response_model=TransportSchemaEntity104Response, status_code=201)
def create_entity_104(payload: TransportSchemaEntity104Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_104(payload)

@router.get("/entity-105", response_model=List[TransportSchemaEntity105Response])
def list_entities_105(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_105_list(skip=skip, limit=limit)

@router.get("/entity-105/{entity_id}", response_model=TransportSchemaEntity105Response)
def get_entity_105(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_105_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 105 not found")
    return res

@router.post("/entity-105", response_model=TransportSchemaEntity105Response, status_code=201)
def create_entity_105(payload: TransportSchemaEntity105Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_105(payload)

@router.get("/entity-106", response_model=List[TransportSchemaEntity106Response])
def list_entities_106(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_106_list(skip=skip, limit=limit)

@router.get("/entity-106/{entity_id}", response_model=TransportSchemaEntity106Response)
def get_entity_106(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_106_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 106 not found")
    return res

@router.post("/entity-106", response_model=TransportSchemaEntity106Response, status_code=201)
def create_entity_106(payload: TransportSchemaEntity106Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_106(payload)

@router.get("/entity-107", response_model=List[TransportSchemaEntity107Response])
def list_entities_107(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_107_list(skip=skip, limit=limit)

@router.get("/entity-107/{entity_id}", response_model=TransportSchemaEntity107Response)
def get_entity_107(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_107_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 107 not found")
    return res

@router.post("/entity-107", response_model=TransportSchemaEntity107Response, status_code=201)
def create_entity_107(payload: TransportSchemaEntity107Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_107(payload)

@router.get("/entity-108", response_model=List[TransportSchemaEntity108Response])
def list_entities_108(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_108_list(skip=skip, limit=limit)

@router.get("/entity-108/{entity_id}", response_model=TransportSchemaEntity108Response)
def get_entity_108(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_108_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 108 not found")
    return res

@router.post("/entity-108", response_model=TransportSchemaEntity108Response, status_code=201)
def create_entity_108(payload: TransportSchemaEntity108Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_108(payload)

@router.get("/entity-109", response_model=List[TransportSchemaEntity109Response])
def list_entities_109(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_109_list(skip=skip, limit=limit)

@router.get("/entity-109/{entity_id}", response_model=TransportSchemaEntity109Response)
def get_entity_109(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_109_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 109 not found")
    return res

@router.post("/entity-109", response_model=TransportSchemaEntity109Response, status_code=201)
def create_entity_109(payload: TransportSchemaEntity109Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_109(payload)

@router.get("/entity-110", response_model=List[TransportSchemaEntity110Response])
def list_entities_110(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_110_list(skip=skip, limit=limit)

@router.get("/entity-110/{entity_id}", response_model=TransportSchemaEntity110Response)
def get_entity_110(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_110_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 110 not found")
    return res

@router.post("/entity-110", response_model=TransportSchemaEntity110Response, status_code=201)
def create_entity_110(payload: TransportSchemaEntity110Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_110(payload)

@router.get("/entity-111", response_model=List[TransportSchemaEntity111Response])
def list_entities_111(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_111_list(skip=skip, limit=limit)

@router.get("/entity-111/{entity_id}", response_model=TransportSchemaEntity111Response)
def get_entity_111(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_111_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 111 not found")
    return res

@router.post("/entity-111", response_model=TransportSchemaEntity111Response, status_code=201)
def create_entity_111(payload: TransportSchemaEntity111Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_111(payload)

@router.get("/entity-112", response_model=List[TransportSchemaEntity112Response])
def list_entities_112(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_112_list(skip=skip, limit=limit)

@router.get("/entity-112/{entity_id}", response_model=TransportSchemaEntity112Response)
def get_entity_112(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_112_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 112 not found")
    return res

@router.post("/entity-112", response_model=TransportSchemaEntity112Response, status_code=201)
def create_entity_112(payload: TransportSchemaEntity112Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_112(payload)

@router.get("/entity-113", response_model=List[TransportSchemaEntity113Response])
def list_entities_113(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_113_list(skip=skip, limit=limit)

@router.get("/entity-113/{entity_id}", response_model=TransportSchemaEntity113Response)
def get_entity_113(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_113_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 113 not found")
    return res

@router.post("/entity-113", response_model=TransportSchemaEntity113Response, status_code=201)
def create_entity_113(payload: TransportSchemaEntity113Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_113(payload)

@router.get("/entity-114", response_model=List[TransportSchemaEntity114Response])
def list_entities_114(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_114_list(skip=skip, limit=limit)

@router.get("/entity-114/{entity_id}", response_model=TransportSchemaEntity114Response)
def get_entity_114(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_114_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 114 not found")
    return res

@router.post("/entity-114", response_model=TransportSchemaEntity114Response, status_code=201)
def create_entity_114(payload: TransportSchemaEntity114Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_114(payload)

@router.get("/entity-115", response_model=List[TransportSchemaEntity115Response])
def list_entities_115(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_115_list(skip=skip, limit=limit)

@router.get("/entity-115/{entity_id}", response_model=TransportSchemaEntity115Response)
def get_entity_115(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_115_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 115 not found")
    return res

@router.post("/entity-115", response_model=TransportSchemaEntity115Response, status_code=201)
def create_entity_115(payload: TransportSchemaEntity115Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_115(payload)

@router.get("/entity-116", response_model=List[TransportSchemaEntity116Response])
def list_entities_116(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_116_list(skip=skip, limit=limit)

@router.get("/entity-116/{entity_id}", response_model=TransportSchemaEntity116Response)
def get_entity_116(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_116_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 116 not found")
    return res

@router.post("/entity-116", response_model=TransportSchemaEntity116Response, status_code=201)
def create_entity_116(payload: TransportSchemaEntity116Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_116(payload)

@router.get("/entity-117", response_model=List[TransportSchemaEntity117Response])
def list_entities_117(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_117_list(skip=skip, limit=limit)

@router.get("/entity-117/{entity_id}", response_model=TransportSchemaEntity117Response)
def get_entity_117(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_117_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 117 not found")
    return res

@router.post("/entity-117", response_model=TransportSchemaEntity117Response, status_code=201)
def create_entity_117(payload: TransportSchemaEntity117Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_117(payload)

@router.get("/entity-118", response_model=List[TransportSchemaEntity118Response])
def list_entities_118(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_118_list(skip=skip, limit=limit)

@router.get("/entity-118/{entity_id}", response_model=TransportSchemaEntity118Response)
def get_entity_118(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_118_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 118 not found")
    return res

@router.post("/entity-118", response_model=TransportSchemaEntity118Response, status_code=201)
def create_entity_118(payload: TransportSchemaEntity118Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_118(payload)

@router.get("/entity-119", response_model=List[TransportSchemaEntity119Response])
def list_entities_119(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_119_list(skip=skip, limit=limit)

@router.get("/entity-119/{entity_id}", response_model=TransportSchemaEntity119Response)
def get_entity_119(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_119_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 119 not found")
    return res

@router.post("/entity-119", response_model=TransportSchemaEntity119Response, status_code=201)
def create_entity_119(payload: TransportSchemaEntity119Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_119(payload)

@router.get("/entity-120", response_model=List[TransportSchemaEntity120Response])
def list_entities_120(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.get_entity_120_list(skip=skip, limit=limit)

@router.get("/entity-120/{entity_id}", response_model=TransportSchemaEntity120Response)
def get_entity_120(entity_id: int, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    res = srv.get_entity_120_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 120 not found")
    return res

@router.post("/entity-120", response_model=TransportSchemaEntity120Response, status_code=201)
def create_entity_120(payload: TransportSchemaEntity120Create, db: Session = Depends(get_db)):
    srv = TransportDomainService(db)
    return srv.create_entity_120(payload)

