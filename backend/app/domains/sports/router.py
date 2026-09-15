"""
Sports & Extracurricular Activities - FastAPI Router Endpoints
Module: app.domains.sports.router
"""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domains.sports.schemas import *
from app.domains.sports.service import SportsDomainService

router = APIRouter(prefix="/sports", tags=["Sports & Extracurricular Activities"])

@router.get("/entity-1", response_model=List[SportsSchemaEntity1Response])
def list_entities_1(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_1_list(skip=skip, limit=limit)

@router.get("/entity-1/{entity_id}", response_model=SportsSchemaEntity1Response)
def get_entity_1(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_1_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 1 not found")
    return res

@router.post("/entity-1", response_model=SportsSchemaEntity1Response, status_code=201)
def create_entity_1(payload: SportsSchemaEntity1Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_1(payload)

@router.get("/entity-2", response_model=List[SportsSchemaEntity2Response])
def list_entities_2(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_2_list(skip=skip, limit=limit)

@router.get("/entity-2/{entity_id}", response_model=SportsSchemaEntity2Response)
def get_entity_2(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_2_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 2 not found")
    return res

@router.post("/entity-2", response_model=SportsSchemaEntity2Response, status_code=201)
def create_entity_2(payload: SportsSchemaEntity2Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_2(payload)

@router.get("/entity-3", response_model=List[SportsSchemaEntity3Response])
def list_entities_3(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_3_list(skip=skip, limit=limit)

@router.get("/entity-3/{entity_id}", response_model=SportsSchemaEntity3Response)
def get_entity_3(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_3_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 3 not found")
    return res

@router.post("/entity-3", response_model=SportsSchemaEntity3Response, status_code=201)
def create_entity_3(payload: SportsSchemaEntity3Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_3(payload)

@router.get("/entity-4", response_model=List[SportsSchemaEntity4Response])
def list_entities_4(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_4_list(skip=skip, limit=limit)

@router.get("/entity-4/{entity_id}", response_model=SportsSchemaEntity4Response)
def get_entity_4(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_4_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 4 not found")
    return res

@router.post("/entity-4", response_model=SportsSchemaEntity4Response, status_code=201)
def create_entity_4(payload: SportsSchemaEntity4Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_4(payload)

@router.get("/entity-5", response_model=List[SportsSchemaEntity5Response])
def list_entities_5(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_5_list(skip=skip, limit=limit)

@router.get("/entity-5/{entity_id}", response_model=SportsSchemaEntity5Response)
def get_entity_5(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_5_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 5 not found")
    return res

@router.post("/entity-5", response_model=SportsSchemaEntity5Response, status_code=201)
def create_entity_5(payload: SportsSchemaEntity5Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_5(payload)

@router.get("/entity-6", response_model=List[SportsSchemaEntity6Response])
def list_entities_6(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_6_list(skip=skip, limit=limit)

@router.get("/entity-6/{entity_id}", response_model=SportsSchemaEntity6Response)
def get_entity_6(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_6_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 6 not found")
    return res

@router.post("/entity-6", response_model=SportsSchemaEntity6Response, status_code=201)
def create_entity_6(payload: SportsSchemaEntity6Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_6(payload)

@router.get("/entity-7", response_model=List[SportsSchemaEntity7Response])
def list_entities_7(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_7_list(skip=skip, limit=limit)

@router.get("/entity-7/{entity_id}", response_model=SportsSchemaEntity7Response)
def get_entity_7(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_7_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 7 not found")
    return res

@router.post("/entity-7", response_model=SportsSchemaEntity7Response, status_code=201)
def create_entity_7(payload: SportsSchemaEntity7Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_7(payload)

@router.get("/entity-8", response_model=List[SportsSchemaEntity8Response])
def list_entities_8(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_8_list(skip=skip, limit=limit)

@router.get("/entity-8/{entity_id}", response_model=SportsSchemaEntity8Response)
def get_entity_8(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_8_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 8 not found")
    return res

@router.post("/entity-8", response_model=SportsSchemaEntity8Response, status_code=201)
def create_entity_8(payload: SportsSchemaEntity8Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_8(payload)

@router.get("/entity-9", response_model=List[SportsSchemaEntity9Response])
def list_entities_9(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_9_list(skip=skip, limit=limit)

@router.get("/entity-9/{entity_id}", response_model=SportsSchemaEntity9Response)
def get_entity_9(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_9_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 9 not found")
    return res

@router.post("/entity-9", response_model=SportsSchemaEntity9Response, status_code=201)
def create_entity_9(payload: SportsSchemaEntity9Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_9(payload)

@router.get("/entity-10", response_model=List[SportsSchemaEntity10Response])
def list_entities_10(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_10_list(skip=skip, limit=limit)

@router.get("/entity-10/{entity_id}", response_model=SportsSchemaEntity10Response)
def get_entity_10(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_10_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 10 not found")
    return res

@router.post("/entity-10", response_model=SportsSchemaEntity10Response, status_code=201)
def create_entity_10(payload: SportsSchemaEntity10Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_10(payload)

@router.get("/entity-11", response_model=List[SportsSchemaEntity11Response])
def list_entities_11(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_11_list(skip=skip, limit=limit)

@router.get("/entity-11/{entity_id}", response_model=SportsSchemaEntity11Response)
def get_entity_11(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_11_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 11 not found")
    return res

@router.post("/entity-11", response_model=SportsSchemaEntity11Response, status_code=201)
def create_entity_11(payload: SportsSchemaEntity11Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_11(payload)

@router.get("/entity-12", response_model=List[SportsSchemaEntity12Response])
def list_entities_12(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_12_list(skip=skip, limit=limit)

@router.get("/entity-12/{entity_id}", response_model=SportsSchemaEntity12Response)
def get_entity_12(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_12_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 12 not found")
    return res

@router.post("/entity-12", response_model=SportsSchemaEntity12Response, status_code=201)
def create_entity_12(payload: SportsSchemaEntity12Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_12(payload)

@router.get("/entity-13", response_model=List[SportsSchemaEntity13Response])
def list_entities_13(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_13_list(skip=skip, limit=limit)

@router.get("/entity-13/{entity_id}", response_model=SportsSchemaEntity13Response)
def get_entity_13(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_13_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 13 not found")
    return res

@router.post("/entity-13", response_model=SportsSchemaEntity13Response, status_code=201)
def create_entity_13(payload: SportsSchemaEntity13Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_13(payload)

@router.get("/entity-14", response_model=List[SportsSchemaEntity14Response])
def list_entities_14(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_14_list(skip=skip, limit=limit)

@router.get("/entity-14/{entity_id}", response_model=SportsSchemaEntity14Response)
def get_entity_14(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_14_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 14 not found")
    return res

@router.post("/entity-14", response_model=SportsSchemaEntity14Response, status_code=201)
def create_entity_14(payload: SportsSchemaEntity14Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_14(payload)

@router.get("/entity-15", response_model=List[SportsSchemaEntity15Response])
def list_entities_15(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_15_list(skip=skip, limit=limit)

@router.get("/entity-15/{entity_id}", response_model=SportsSchemaEntity15Response)
def get_entity_15(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_15_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 15 not found")
    return res

@router.post("/entity-15", response_model=SportsSchemaEntity15Response, status_code=201)
def create_entity_15(payload: SportsSchemaEntity15Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_15(payload)

@router.get("/entity-16", response_model=List[SportsSchemaEntity16Response])
def list_entities_16(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_16_list(skip=skip, limit=limit)

@router.get("/entity-16/{entity_id}", response_model=SportsSchemaEntity16Response)
def get_entity_16(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_16_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 16 not found")
    return res

@router.post("/entity-16", response_model=SportsSchemaEntity16Response, status_code=201)
def create_entity_16(payload: SportsSchemaEntity16Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_16(payload)

@router.get("/entity-17", response_model=List[SportsSchemaEntity17Response])
def list_entities_17(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_17_list(skip=skip, limit=limit)

@router.get("/entity-17/{entity_id}", response_model=SportsSchemaEntity17Response)
def get_entity_17(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_17_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 17 not found")
    return res

@router.post("/entity-17", response_model=SportsSchemaEntity17Response, status_code=201)
def create_entity_17(payload: SportsSchemaEntity17Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_17(payload)

@router.get("/entity-18", response_model=List[SportsSchemaEntity18Response])
def list_entities_18(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_18_list(skip=skip, limit=limit)

@router.get("/entity-18/{entity_id}", response_model=SportsSchemaEntity18Response)
def get_entity_18(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_18_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 18 not found")
    return res

@router.post("/entity-18", response_model=SportsSchemaEntity18Response, status_code=201)
def create_entity_18(payload: SportsSchemaEntity18Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_18(payload)

@router.get("/entity-19", response_model=List[SportsSchemaEntity19Response])
def list_entities_19(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_19_list(skip=skip, limit=limit)

@router.get("/entity-19/{entity_id}", response_model=SportsSchemaEntity19Response)
def get_entity_19(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_19_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 19 not found")
    return res

@router.post("/entity-19", response_model=SportsSchemaEntity19Response, status_code=201)
def create_entity_19(payload: SportsSchemaEntity19Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_19(payload)

@router.get("/entity-20", response_model=List[SportsSchemaEntity20Response])
def list_entities_20(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_20_list(skip=skip, limit=limit)

@router.get("/entity-20/{entity_id}", response_model=SportsSchemaEntity20Response)
def get_entity_20(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_20_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 20 not found")
    return res

@router.post("/entity-20", response_model=SportsSchemaEntity20Response, status_code=201)
def create_entity_20(payload: SportsSchemaEntity20Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_20(payload)

@router.get("/entity-21", response_model=List[SportsSchemaEntity21Response])
def list_entities_21(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_21_list(skip=skip, limit=limit)

@router.get("/entity-21/{entity_id}", response_model=SportsSchemaEntity21Response)
def get_entity_21(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_21_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 21 not found")
    return res

@router.post("/entity-21", response_model=SportsSchemaEntity21Response, status_code=201)
def create_entity_21(payload: SportsSchemaEntity21Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_21(payload)

@router.get("/entity-22", response_model=List[SportsSchemaEntity22Response])
def list_entities_22(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_22_list(skip=skip, limit=limit)

@router.get("/entity-22/{entity_id}", response_model=SportsSchemaEntity22Response)
def get_entity_22(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_22_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 22 not found")
    return res

@router.post("/entity-22", response_model=SportsSchemaEntity22Response, status_code=201)
def create_entity_22(payload: SportsSchemaEntity22Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_22(payload)

@router.get("/entity-23", response_model=List[SportsSchemaEntity23Response])
def list_entities_23(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_23_list(skip=skip, limit=limit)

@router.get("/entity-23/{entity_id}", response_model=SportsSchemaEntity23Response)
def get_entity_23(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_23_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 23 not found")
    return res

@router.post("/entity-23", response_model=SportsSchemaEntity23Response, status_code=201)
def create_entity_23(payload: SportsSchemaEntity23Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_23(payload)

@router.get("/entity-24", response_model=List[SportsSchemaEntity24Response])
def list_entities_24(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_24_list(skip=skip, limit=limit)

@router.get("/entity-24/{entity_id}", response_model=SportsSchemaEntity24Response)
def get_entity_24(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_24_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 24 not found")
    return res

@router.post("/entity-24", response_model=SportsSchemaEntity24Response, status_code=201)
def create_entity_24(payload: SportsSchemaEntity24Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_24(payload)

@router.get("/entity-25", response_model=List[SportsSchemaEntity25Response])
def list_entities_25(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_25_list(skip=skip, limit=limit)

@router.get("/entity-25/{entity_id}", response_model=SportsSchemaEntity25Response)
def get_entity_25(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_25_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 25 not found")
    return res

@router.post("/entity-25", response_model=SportsSchemaEntity25Response, status_code=201)
def create_entity_25(payload: SportsSchemaEntity25Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_25(payload)

@router.get("/entity-26", response_model=List[SportsSchemaEntity26Response])
def list_entities_26(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_26_list(skip=skip, limit=limit)

@router.get("/entity-26/{entity_id}", response_model=SportsSchemaEntity26Response)
def get_entity_26(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_26_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 26 not found")
    return res

@router.post("/entity-26", response_model=SportsSchemaEntity26Response, status_code=201)
def create_entity_26(payload: SportsSchemaEntity26Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_26(payload)

@router.get("/entity-27", response_model=List[SportsSchemaEntity27Response])
def list_entities_27(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_27_list(skip=skip, limit=limit)

@router.get("/entity-27/{entity_id}", response_model=SportsSchemaEntity27Response)
def get_entity_27(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_27_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 27 not found")
    return res

@router.post("/entity-27", response_model=SportsSchemaEntity27Response, status_code=201)
def create_entity_27(payload: SportsSchemaEntity27Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_27(payload)

@router.get("/entity-28", response_model=List[SportsSchemaEntity28Response])
def list_entities_28(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_28_list(skip=skip, limit=limit)

@router.get("/entity-28/{entity_id}", response_model=SportsSchemaEntity28Response)
def get_entity_28(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_28_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 28 not found")
    return res

@router.post("/entity-28", response_model=SportsSchemaEntity28Response, status_code=201)
def create_entity_28(payload: SportsSchemaEntity28Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_28(payload)

@router.get("/entity-29", response_model=List[SportsSchemaEntity29Response])
def list_entities_29(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_29_list(skip=skip, limit=limit)

@router.get("/entity-29/{entity_id}", response_model=SportsSchemaEntity29Response)
def get_entity_29(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_29_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 29 not found")
    return res

@router.post("/entity-29", response_model=SportsSchemaEntity29Response, status_code=201)
def create_entity_29(payload: SportsSchemaEntity29Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_29(payload)

@router.get("/entity-30", response_model=List[SportsSchemaEntity30Response])
def list_entities_30(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_30_list(skip=skip, limit=limit)

@router.get("/entity-30/{entity_id}", response_model=SportsSchemaEntity30Response)
def get_entity_30(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_30_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 30 not found")
    return res

@router.post("/entity-30", response_model=SportsSchemaEntity30Response, status_code=201)
def create_entity_30(payload: SportsSchemaEntity30Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_30(payload)

@router.get("/entity-31", response_model=List[SportsSchemaEntity31Response])
def list_entities_31(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_31_list(skip=skip, limit=limit)

@router.get("/entity-31/{entity_id}", response_model=SportsSchemaEntity31Response)
def get_entity_31(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_31_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 31 not found")
    return res

@router.post("/entity-31", response_model=SportsSchemaEntity31Response, status_code=201)
def create_entity_31(payload: SportsSchemaEntity31Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_31(payload)

@router.get("/entity-32", response_model=List[SportsSchemaEntity32Response])
def list_entities_32(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_32_list(skip=skip, limit=limit)

@router.get("/entity-32/{entity_id}", response_model=SportsSchemaEntity32Response)
def get_entity_32(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_32_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 32 not found")
    return res

@router.post("/entity-32", response_model=SportsSchemaEntity32Response, status_code=201)
def create_entity_32(payload: SportsSchemaEntity32Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_32(payload)

@router.get("/entity-33", response_model=List[SportsSchemaEntity33Response])
def list_entities_33(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_33_list(skip=skip, limit=limit)

@router.get("/entity-33/{entity_id}", response_model=SportsSchemaEntity33Response)
def get_entity_33(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_33_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 33 not found")
    return res

@router.post("/entity-33", response_model=SportsSchemaEntity33Response, status_code=201)
def create_entity_33(payload: SportsSchemaEntity33Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_33(payload)

@router.get("/entity-34", response_model=List[SportsSchemaEntity34Response])
def list_entities_34(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_34_list(skip=skip, limit=limit)

@router.get("/entity-34/{entity_id}", response_model=SportsSchemaEntity34Response)
def get_entity_34(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_34_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 34 not found")
    return res

@router.post("/entity-34", response_model=SportsSchemaEntity34Response, status_code=201)
def create_entity_34(payload: SportsSchemaEntity34Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_34(payload)

@router.get("/entity-35", response_model=List[SportsSchemaEntity35Response])
def list_entities_35(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_35_list(skip=skip, limit=limit)

@router.get("/entity-35/{entity_id}", response_model=SportsSchemaEntity35Response)
def get_entity_35(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_35_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 35 not found")
    return res

@router.post("/entity-35", response_model=SportsSchemaEntity35Response, status_code=201)
def create_entity_35(payload: SportsSchemaEntity35Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_35(payload)

@router.get("/entity-36", response_model=List[SportsSchemaEntity36Response])
def list_entities_36(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_36_list(skip=skip, limit=limit)

@router.get("/entity-36/{entity_id}", response_model=SportsSchemaEntity36Response)
def get_entity_36(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_36_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 36 not found")
    return res

@router.post("/entity-36", response_model=SportsSchemaEntity36Response, status_code=201)
def create_entity_36(payload: SportsSchemaEntity36Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_36(payload)

@router.get("/entity-37", response_model=List[SportsSchemaEntity37Response])
def list_entities_37(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_37_list(skip=skip, limit=limit)

@router.get("/entity-37/{entity_id}", response_model=SportsSchemaEntity37Response)
def get_entity_37(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_37_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 37 not found")
    return res

@router.post("/entity-37", response_model=SportsSchemaEntity37Response, status_code=201)
def create_entity_37(payload: SportsSchemaEntity37Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_37(payload)

@router.get("/entity-38", response_model=List[SportsSchemaEntity38Response])
def list_entities_38(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_38_list(skip=skip, limit=limit)

@router.get("/entity-38/{entity_id}", response_model=SportsSchemaEntity38Response)
def get_entity_38(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_38_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 38 not found")
    return res

@router.post("/entity-38", response_model=SportsSchemaEntity38Response, status_code=201)
def create_entity_38(payload: SportsSchemaEntity38Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_38(payload)

@router.get("/entity-39", response_model=List[SportsSchemaEntity39Response])
def list_entities_39(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_39_list(skip=skip, limit=limit)

@router.get("/entity-39/{entity_id}", response_model=SportsSchemaEntity39Response)
def get_entity_39(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_39_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 39 not found")
    return res

@router.post("/entity-39", response_model=SportsSchemaEntity39Response, status_code=201)
def create_entity_39(payload: SportsSchemaEntity39Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_39(payload)

@router.get("/entity-40", response_model=List[SportsSchemaEntity40Response])
def list_entities_40(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_40_list(skip=skip, limit=limit)

@router.get("/entity-40/{entity_id}", response_model=SportsSchemaEntity40Response)
def get_entity_40(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_40_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 40 not found")
    return res

@router.post("/entity-40", response_model=SportsSchemaEntity40Response, status_code=201)
def create_entity_40(payload: SportsSchemaEntity40Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_40(payload)

@router.get("/entity-41", response_model=List[SportsSchemaEntity41Response])
def list_entities_41(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_41_list(skip=skip, limit=limit)

@router.get("/entity-41/{entity_id}", response_model=SportsSchemaEntity41Response)
def get_entity_41(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_41_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 41 not found")
    return res

@router.post("/entity-41", response_model=SportsSchemaEntity41Response, status_code=201)
def create_entity_41(payload: SportsSchemaEntity41Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_41(payload)

@router.get("/entity-42", response_model=List[SportsSchemaEntity42Response])
def list_entities_42(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_42_list(skip=skip, limit=limit)

@router.get("/entity-42/{entity_id}", response_model=SportsSchemaEntity42Response)
def get_entity_42(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_42_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 42 not found")
    return res

@router.post("/entity-42", response_model=SportsSchemaEntity42Response, status_code=201)
def create_entity_42(payload: SportsSchemaEntity42Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_42(payload)

@router.get("/entity-43", response_model=List[SportsSchemaEntity43Response])
def list_entities_43(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_43_list(skip=skip, limit=limit)

@router.get("/entity-43/{entity_id}", response_model=SportsSchemaEntity43Response)
def get_entity_43(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_43_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 43 not found")
    return res

@router.post("/entity-43", response_model=SportsSchemaEntity43Response, status_code=201)
def create_entity_43(payload: SportsSchemaEntity43Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_43(payload)

@router.get("/entity-44", response_model=List[SportsSchemaEntity44Response])
def list_entities_44(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_44_list(skip=skip, limit=limit)

@router.get("/entity-44/{entity_id}", response_model=SportsSchemaEntity44Response)
def get_entity_44(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_44_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 44 not found")
    return res

@router.post("/entity-44", response_model=SportsSchemaEntity44Response, status_code=201)
def create_entity_44(payload: SportsSchemaEntity44Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_44(payload)

@router.get("/entity-45", response_model=List[SportsSchemaEntity45Response])
def list_entities_45(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_45_list(skip=skip, limit=limit)

@router.get("/entity-45/{entity_id}", response_model=SportsSchemaEntity45Response)
def get_entity_45(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_45_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 45 not found")
    return res

@router.post("/entity-45", response_model=SportsSchemaEntity45Response, status_code=201)
def create_entity_45(payload: SportsSchemaEntity45Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_45(payload)

@router.get("/entity-46", response_model=List[SportsSchemaEntity46Response])
def list_entities_46(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_46_list(skip=skip, limit=limit)

@router.get("/entity-46/{entity_id}", response_model=SportsSchemaEntity46Response)
def get_entity_46(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_46_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 46 not found")
    return res

@router.post("/entity-46", response_model=SportsSchemaEntity46Response, status_code=201)
def create_entity_46(payload: SportsSchemaEntity46Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_46(payload)

@router.get("/entity-47", response_model=List[SportsSchemaEntity47Response])
def list_entities_47(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_47_list(skip=skip, limit=limit)

@router.get("/entity-47/{entity_id}", response_model=SportsSchemaEntity47Response)
def get_entity_47(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_47_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 47 not found")
    return res

@router.post("/entity-47", response_model=SportsSchemaEntity47Response, status_code=201)
def create_entity_47(payload: SportsSchemaEntity47Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_47(payload)

@router.get("/entity-48", response_model=List[SportsSchemaEntity48Response])
def list_entities_48(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_48_list(skip=skip, limit=limit)

@router.get("/entity-48/{entity_id}", response_model=SportsSchemaEntity48Response)
def get_entity_48(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_48_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 48 not found")
    return res

@router.post("/entity-48", response_model=SportsSchemaEntity48Response, status_code=201)
def create_entity_48(payload: SportsSchemaEntity48Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_48(payload)

@router.get("/entity-49", response_model=List[SportsSchemaEntity49Response])
def list_entities_49(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_49_list(skip=skip, limit=limit)

@router.get("/entity-49/{entity_id}", response_model=SportsSchemaEntity49Response)
def get_entity_49(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_49_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 49 not found")
    return res

@router.post("/entity-49", response_model=SportsSchemaEntity49Response, status_code=201)
def create_entity_49(payload: SportsSchemaEntity49Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_49(payload)

@router.get("/entity-50", response_model=List[SportsSchemaEntity50Response])
def list_entities_50(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_50_list(skip=skip, limit=limit)

@router.get("/entity-50/{entity_id}", response_model=SportsSchemaEntity50Response)
def get_entity_50(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_50_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 50 not found")
    return res

@router.post("/entity-50", response_model=SportsSchemaEntity50Response, status_code=201)
def create_entity_50(payload: SportsSchemaEntity50Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_50(payload)

