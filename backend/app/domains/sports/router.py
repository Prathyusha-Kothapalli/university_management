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

@router.get("/entity-51", response_model=List[SportsSchemaEntity51Response])
def list_entities_51(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_51_list(skip=skip, limit=limit)

@router.get("/entity-51/{entity_id}", response_model=SportsSchemaEntity51Response)
def get_entity_51(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_51_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 51 not found")
    return res

@router.post("/entity-51", response_model=SportsSchemaEntity51Response, status_code=201)
def create_entity_51(payload: SportsSchemaEntity51Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_51(payload)

@router.get("/entity-52", response_model=List[SportsSchemaEntity52Response])
def list_entities_52(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_52_list(skip=skip, limit=limit)

@router.get("/entity-52/{entity_id}", response_model=SportsSchemaEntity52Response)
def get_entity_52(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_52_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 52 not found")
    return res

@router.post("/entity-52", response_model=SportsSchemaEntity52Response, status_code=201)
def create_entity_52(payload: SportsSchemaEntity52Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_52(payload)

@router.get("/entity-53", response_model=List[SportsSchemaEntity53Response])
def list_entities_53(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_53_list(skip=skip, limit=limit)

@router.get("/entity-53/{entity_id}", response_model=SportsSchemaEntity53Response)
def get_entity_53(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_53_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 53 not found")
    return res

@router.post("/entity-53", response_model=SportsSchemaEntity53Response, status_code=201)
def create_entity_53(payload: SportsSchemaEntity53Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_53(payload)

@router.get("/entity-54", response_model=List[SportsSchemaEntity54Response])
def list_entities_54(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_54_list(skip=skip, limit=limit)

@router.get("/entity-54/{entity_id}", response_model=SportsSchemaEntity54Response)
def get_entity_54(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_54_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 54 not found")
    return res

@router.post("/entity-54", response_model=SportsSchemaEntity54Response, status_code=201)
def create_entity_54(payload: SportsSchemaEntity54Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_54(payload)

@router.get("/entity-55", response_model=List[SportsSchemaEntity55Response])
def list_entities_55(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_55_list(skip=skip, limit=limit)

@router.get("/entity-55/{entity_id}", response_model=SportsSchemaEntity55Response)
def get_entity_55(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_55_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 55 not found")
    return res

@router.post("/entity-55", response_model=SportsSchemaEntity55Response, status_code=201)
def create_entity_55(payload: SportsSchemaEntity55Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_55(payload)

@router.get("/entity-56", response_model=List[SportsSchemaEntity56Response])
def list_entities_56(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_56_list(skip=skip, limit=limit)

@router.get("/entity-56/{entity_id}", response_model=SportsSchemaEntity56Response)
def get_entity_56(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_56_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 56 not found")
    return res

@router.post("/entity-56", response_model=SportsSchemaEntity56Response, status_code=201)
def create_entity_56(payload: SportsSchemaEntity56Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_56(payload)

@router.get("/entity-57", response_model=List[SportsSchemaEntity57Response])
def list_entities_57(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_57_list(skip=skip, limit=limit)

@router.get("/entity-57/{entity_id}", response_model=SportsSchemaEntity57Response)
def get_entity_57(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_57_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 57 not found")
    return res

@router.post("/entity-57", response_model=SportsSchemaEntity57Response, status_code=201)
def create_entity_57(payload: SportsSchemaEntity57Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_57(payload)

@router.get("/entity-58", response_model=List[SportsSchemaEntity58Response])
def list_entities_58(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_58_list(skip=skip, limit=limit)

@router.get("/entity-58/{entity_id}", response_model=SportsSchemaEntity58Response)
def get_entity_58(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_58_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 58 not found")
    return res

@router.post("/entity-58", response_model=SportsSchemaEntity58Response, status_code=201)
def create_entity_58(payload: SportsSchemaEntity58Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_58(payload)

@router.get("/entity-59", response_model=List[SportsSchemaEntity59Response])
def list_entities_59(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_59_list(skip=skip, limit=limit)

@router.get("/entity-59/{entity_id}", response_model=SportsSchemaEntity59Response)
def get_entity_59(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_59_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 59 not found")
    return res

@router.post("/entity-59", response_model=SportsSchemaEntity59Response, status_code=201)
def create_entity_59(payload: SportsSchemaEntity59Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_59(payload)

@router.get("/entity-60", response_model=List[SportsSchemaEntity60Response])
def list_entities_60(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_60_list(skip=skip, limit=limit)

@router.get("/entity-60/{entity_id}", response_model=SportsSchemaEntity60Response)
def get_entity_60(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_60_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 60 not found")
    return res

@router.post("/entity-60", response_model=SportsSchemaEntity60Response, status_code=201)
def create_entity_60(payload: SportsSchemaEntity60Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_60(payload)

@router.get("/entity-61", response_model=List[SportsSchemaEntity61Response])
def list_entities_61(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_61_list(skip=skip, limit=limit)

@router.get("/entity-61/{entity_id}", response_model=SportsSchemaEntity61Response)
def get_entity_61(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_61_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 61 not found")
    return res

@router.post("/entity-61", response_model=SportsSchemaEntity61Response, status_code=201)
def create_entity_61(payload: SportsSchemaEntity61Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_61(payload)

@router.get("/entity-62", response_model=List[SportsSchemaEntity62Response])
def list_entities_62(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_62_list(skip=skip, limit=limit)

@router.get("/entity-62/{entity_id}", response_model=SportsSchemaEntity62Response)
def get_entity_62(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_62_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 62 not found")
    return res

@router.post("/entity-62", response_model=SportsSchemaEntity62Response, status_code=201)
def create_entity_62(payload: SportsSchemaEntity62Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_62(payload)

@router.get("/entity-63", response_model=List[SportsSchemaEntity63Response])
def list_entities_63(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_63_list(skip=skip, limit=limit)

@router.get("/entity-63/{entity_id}", response_model=SportsSchemaEntity63Response)
def get_entity_63(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_63_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 63 not found")
    return res

@router.post("/entity-63", response_model=SportsSchemaEntity63Response, status_code=201)
def create_entity_63(payload: SportsSchemaEntity63Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_63(payload)

@router.get("/entity-64", response_model=List[SportsSchemaEntity64Response])
def list_entities_64(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_64_list(skip=skip, limit=limit)

@router.get("/entity-64/{entity_id}", response_model=SportsSchemaEntity64Response)
def get_entity_64(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_64_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 64 not found")
    return res

@router.post("/entity-64", response_model=SportsSchemaEntity64Response, status_code=201)
def create_entity_64(payload: SportsSchemaEntity64Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_64(payload)

@router.get("/entity-65", response_model=List[SportsSchemaEntity65Response])
def list_entities_65(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_65_list(skip=skip, limit=limit)

@router.get("/entity-65/{entity_id}", response_model=SportsSchemaEntity65Response)
def get_entity_65(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_65_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 65 not found")
    return res

@router.post("/entity-65", response_model=SportsSchemaEntity65Response, status_code=201)
def create_entity_65(payload: SportsSchemaEntity65Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_65(payload)

@router.get("/entity-66", response_model=List[SportsSchemaEntity66Response])
def list_entities_66(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_66_list(skip=skip, limit=limit)

@router.get("/entity-66/{entity_id}", response_model=SportsSchemaEntity66Response)
def get_entity_66(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_66_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 66 not found")
    return res

@router.post("/entity-66", response_model=SportsSchemaEntity66Response, status_code=201)
def create_entity_66(payload: SportsSchemaEntity66Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_66(payload)

@router.get("/entity-67", response_model=List[SportsSchemaEntity67Response])
def list_entities_67(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_67_list(skip=skip, limit=limit)

@router.get("/entity-67/{entity_id}", response_model=SportsSchemaEntity67Response)
def get_entity_67(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_67_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 67 not found")
    return res

@router.post("/entity-67", response_model=SportsSchemaEntity67Response, status_code=201)
def create_entity_67(payload: SportsSchemaEntity67Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_67(payload)

@router.get("/entity-68", response_model=List[SportsSchemaEntity68Response])
def list_entities_68(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_68_list(skip=skip, limit=limit)

@router.get("/entity-68/{entity_id}", response_model=SportsSchemaEntity68Response)
def get_entity_68(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_68_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 68 not found")
    return res

@router.post("/entity-68", response_model=SportsSchemaEntity68Response, status_code=201)
def create_entity_68(payload: SportsSchemaEntity68Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_68(payload)

@router.get("/entity-69", response_model=List[SportsSchemaEntity69Response])
def list_entities_69(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_69_list(skip=skip, limit=limit)

@router.get("/entity-69/{entity_id}", response_model=SportsSchemaEntity69Response)
def get_entity_69(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_69_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 69 not found")
    return res

@router.post("/entity-69", response_model=SportsSchemaEntity69Response, status_code=201)
def create_entity_69(payload: SportsSchemaEntity69Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_69(payload)

@router.get("/entity-70", response_model=List[SportsSchemaEntity70Response])
def list_entities_70(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_70_list(skip=skip, limit=limit)

@router.get("/entity-70/{entity_id}", response_model=SportsSchemaEntity70Response)
def get_entity_70(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_70_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 70 not found")
    return res

@router.post("/entity-70", response_model=SportsSchemaEntity70Response, status_code=201)
def create_entity_70(payload: SportsSchemaEntity70Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_70(payload)

@router.get("/entity-71", response_model=List[SportsSchemaEntity71Response])
def list_entities_71(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_71_list(skip=skip, limit=limit)

@router.get("/entity-71/{entity_id}", response_model=SportsSchemaEntity71Response)
def get_entity_71(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_71_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 71 not found")
    return res

@router.post("/entity-71", response_model=SportsSchemaEntity71Response, status_code=201)
def create_entity_71(payload: SportsSchemaEntity71Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_71(payload)

@router.get("/entity-72", response_model=List[SportsSchemaEntity72Response])
def list_entities_72(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_72_list(skip=skip, limit=limit)

@router.get("/entity-72/{entity_id}", response_model=SportsSchemaEntity72Response)
def get_entity_72(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_72_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 72 not found")
    return res

@router.post("/entity-72", response_model=SportsSchemaEntity72Response, status_code=201)
def create_entity_72(payload: SportsSchemaEntity72Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_72(payload)

@router.get("/entity-73", response_model=List[SportsSchemaEntity73Response])
def list_entities_73(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_73_list(skip=skip, limit=limit)

@router.get("/entity-73/{entity_id}", response_model=SportsSchemaEntity73Response)
def get_entity_73(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_73_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 73 not found")
    return res

@router.post("/entity-73", response_model=SportsSchemaEntity73Response, status_code=201)
def create_entity_73(payload: SportsSchemaEntity73Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_73(payload)

@router.get("/entity-74", response_model=List[SportsSchemaEntity74Response])
def list_entities_74(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_74_list(skip=skip, limit=limit)

@router.get("/entity-74/{entity_id}", response_model=SportsSchemaEntity74Response)
def get_entity_74(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_74_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 74 not found")
    return res

@router.post("/entity-74", response_model=SportsSchemaEntity74Response, status_code=201)
def create_entity_74(payload: SportsSchemaEntity74Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_74(payload)

@router.get("/entity-75", response_model=List[SportsSchemaEntity75Response])
def list_entities_75(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_75_list(skip=skip, limit=limit)

@router.get("/entity-75/{entity_id}", response_model=SportsSchemaEntity75Response)
def get_entity_75(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_75_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 75 not found")
    return res

@router.post("/entity-75", response_model=SportsSchemaEntity75Response, status_code=201)
def create_entity_75(payload: SportsSchemaEntity75Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_75(payload)

@router.get("/entity-76", response_model=List[SportsSchemaEntity76Response])
def list_entities_76(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_76_list(skip=skip, limit=limit)

@router.get("/entity-76/{entity_id}", response_model=SportsSchemaEntity76Response)
def get_entity_76(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_76_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 76 not found")
    return res

@router.post("/entity-76", response_model=SportsSchemaEntity76Response, status_code=201)
def create_entity_76(payload: SportsSchemaEntity76Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_76(payload)

@router.get("/entity-77", response_model=List[SportsSchemaEntity77Response])
def list_entities_77(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_77_list(skip=skip, limit=limit)

@router.get("/entity-77/{entity_id}", response_model=SportsSchemaEntity77Response)
def get_entity_77(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_77_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 77 not found")
    return res

@router.post("/entity-77", response_model=SportsSchemaEntity77Response, status_code=201)
def create_entity_77(payload: SportsSchemaEntity77Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_77(payload)

@router.get("/entity-78", response_model=List[SportsSchemaEntity78Response])
def list_entities_78(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_78_list(skip=skip, limit=limit)

@router.get("/entity-78/{entity_id}", response_model=SportsSchemaEntity78Response)
def get_entity_78(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_78_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 78 not found")
    return res

@router.post("/entity-78", response_model=SportsSchemaEntity78Response, status_code=201)
def create_entity_78(payload: SportsSchemaEntity78Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_78(payload)

@router.get("/entity-79", response_model=List[SportsSchemaEntity79Response])
def list_entities_79(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_79_list(skip=skip, limit=limit)

@router.get("/entity-79/{entity_id}", response_model=SportsSchemaEntity79Response)
def get_entity_79(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_79_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 79 not found")
    return res

@router.post("/entity-79", response_model=SportsSchemaEntity79Response, status_code=201)
def create_entity_79(payload: SportsSchemaEntity79Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_79(payload)

@router.get("/entity-80", response_model=List[SportsSchemaEntity80Response])
def list_entities_80(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_80_list(skip=skip, limit=limit)

@router.get("/entity-80/{entity_id}", response_model=SportsSchemaEntity80Response)
def get_entity_80(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_80_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 80 not found")
    return res

@router.post("/entity-80", response_model=SportsSchemaEntity80Response, status_code=201)
def create_entity_80(payload: SportsSchemaEntity80Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_80(payload)

@router.get("/entity-81", response_model=List[SportsSchemaEntity81Response])
def list_entities_81(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_81_list(skip=skip, limit=limit)

@router.get("/entity-81/{entity_id}", response_model=SportsSchemaEntity81Response)
def get_entity_81(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_81_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 81 not found")
    return res

@router.post("/entity-81", response_model=SportsSchemaEntity81Response, status_code=201)
def create_entity_81(payload: SportsSchemaEntity81Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_81(payload)

@router.get("/entity-82", response_model=List[SportsSchemaEntity82Response])
def list_entities_82(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_82_list(skip=skip, limit=limit)

@router.get("/entity-82/{entity_id}", response_model=SportsSchemaEntity82Response)
def get_entity_82(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_82_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 82 not found")
    return res

@router.post("/entity-82", response_model=SportsSchemaEntity82Response, status_code=201)
def create_entity_82(payload: SportsSchemaEntity82Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_82(payload)

@router.get("/entity-83", response_model=List[SportsSchemaEntity83Response])
def list_entities_83(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_83_list(skip=skip, limit=limit)

@router.get("/entity-83/{entity_id}", response_model=SportsSchemaEntity83Response)
def get_entity_83(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_83_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 83 not found")
    return res

@router.post("/entity-83", response_model=SportsSchemaEntity83Response, status_code=201)
def create_entity_83(payload: SportsSchemaEntity83Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_83(payload)

@router.get("/entity-84", response_model=List[SportsSchemaEntity84Response])
def list_entities_84(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_84_list(skip=skip, limit=limit)

@router.get("/entity-84/{entity_id}", response_model=SportsSchemaEntity84Response)
def get_entity_84(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_84_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 84 not found")
    return res

@router.post("/entity-84", response_model=SportsSchemaEntity84Response, status_code=201)
def create_entity_84(payload: SportsSchemaEntity84Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_84(payload)

@router.get("/entity-85", response_model=List[SportsSchemaEntity85Response])
def list_entities_85(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_85_list(skip=skip, limit=limit)

@router.get("/entity-85/{entity_id}", response_model=SportsSchemaEntity85Response)
def get_entity_85(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_85_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 85 not found")
    return res

@router.post("/entity-85", response_model=SportsSchemaEntity85Response, status_code=201)
def create_entity_85(payload: SportsSchemaEntity85Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_85(payload)

@router.get("/entity-86", response_model=List[SportsSchemaEntity86Response])
def list_entities_86(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_86_list(skip=skip, limit=limit)

@router.get("/entity-86/{entity_id}", response_model=SportsSchemaEntity86Response)
def get_entity_86(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_86_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 86 not found")
    return res

@router.post("/entity-86", response_model=SportsSchemaEntity86Response, status_code=201)
def create_entity_86(payload: SportsSchemaEntity86Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_86(payload)

@router.get("/entity-87", response_model=List[SportsSchemaEntity87Response])
def list_entities_87(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_87_list(skip=skip, limit=limit)

@router.get("/entity-87/{entity_id}", response_model=SportsSchemaEntity87Response)
def get_entity_87(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_87_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 87 not found")
    return res

@router.post("/entity-87", response_model=SportsSchemaEntity87Response, status_code=201)
def create_entity_87(payload: SportsSchemaEntity87Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_87(payload)

@router.get("/entity-88", response_model=List[SportsSchemaEntity88Response])
def list_entities_88(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_88_list(skip=skip, limit=limit)

@router.get("/entity-88/{entity_id}", response_model=SportsSchemaEntity88Response)
def get_entity_88(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_88_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 88 not found")
    return res

@router.post("/entity-88", response_model=SportsSchemaEntity88Response, status_code=201)
def create_entity_88(payload: SportsSchemaEntity88Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_88(payload)

@router.get("/entity-89", response_model=List[SportsSchemaEntity89Response])
def list_entities_89(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_89_list(skip=skip, limit=limit)

@router.get("/entity-89/{entity_id}", response_model=SportsSchemaEntity89Response)
def get_entity_89(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_89_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 89 not found")
    return res

@router.post("/entity-89", response_model=SportsSchemaEntity89Response, status_code=201)
def create_entity_89(payload: SportsSchemaEntity89Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_89(payload)

@router.get("/entity-90", response_model=List[SportsSchemaEntity90Response])
def list_entities_90(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_90_list(skip=skip, limit=limit)

@router.get("/entity-90/{entity_id}", response_model=SportsSchemaEntity90Response)
def get_entity_90(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_90_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 90 not found")
    return res

@router.post("/entity-90", response_model=SportsSchemaEntity90Response, status_code=201)
def create_entity_90(payload: SportsSchemaEntity90Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_90(payload)

@router.get("/entity-91", response_model=List[SportsSchemaEntity91Response])
def list_entities_91(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_91_list(skip=skip, limit=limit)

@router.get("/entity-91/{entity_id}", response_model=SportsSchemaEntity91Response)
def get_entity_91(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_91_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 91 not found")
    return res

@router.post("/entity-91", response_model=SportsSchemaEntity91Response, status_code=201)
def create_entity_91(payload: SportsSchemaEntity91Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_91(payload)

@router.get("/entity-92", response_model=List[SportsSchemaEntity92Response])
def list_entities_92(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_92_list(skip=skip, limit=limit)

@router.get("/entity-92/{entity_id}", response_model=SportsSchemaEntity92Response)
def get_entity_92(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_92_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 92 not found")
    return res

@router.post("/entity-92", response_model=SportsSchemaEntity92Response, status_code=201)
def create_entity_92(payload: SportsSchemaEntity92Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_92(payload)

@router.get("/entity-93", response_model=List[SportsSchemaEntity93Response])
def list_entities_93(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_93_list(skip=skip, limit=limit)

@router.get("/entity-93/{entity_id}", response_model=SportsSchemaEntity93Response)
def get_entity_93(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_93_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 93 not found")
    return res

@router.post("/entity-93", response_model=SportsSchemaEntity93Response, status_code=201)
def create_entity_93(payload: SportsSchemaEntity93Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_93(payload)

@router.get("/entity-94", response_model=List[SportsSchemaEntity94Response])
def list_entities_94(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_94_list(skip=skip, limit=limit)

@router.get("/entity-94/{entity_id}", response_model=SportsSchemaEntity94Response)
def get_entity_94(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_94_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 94 not found")
    return res

@router.post("/entity-94", response_model=SportsSchemaEntity94Response, status_code=201)
def create_entity_94(payload: SportsSchemaEntity94Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_94(payload)

@router.get("/entity-95", response_model=List[SportsSchemaEntity95Response])
def list_entities_95(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_95_list(skip=skip, limit=limit)

@router.get("/entity-95/{entity_id}", response_model=SportsSchemaEntity95Response)
def get_entity_95(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_95_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 95 not found")
    return res

@router.post("/entity-95", response_model=SportsSchemaEntity95Response, status_code=201)
def create_entity_95(payload: SportsSchemaEntity95Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_95(payload)

@router.get("/entity-96", response_model=List[SportsSchemaEntity96Response])
def list_entities_96(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_96_list(skip=skip, limit=limit)

@router.get("/entity-96/{entity_id}", response_model=SportsSchemaEntity96Response)
def get_entity_96(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_96_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 96 not found")
    return res

@router.post("/entity-96", response_model=SportsSchemaEntity96Response, status_code=201)
def create_entity_96(payload: SportsSchemaEntity96Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_96(payload)

@router.get("/entity-97", response_model=List[SportsSchemaEntity97Response])
def list_entities_97(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_97_list(skip=skip, limit=limit)

@router.get("/entity-97/{entity_id}", response_model=SportsSchemaEntity97Response)
def get_entity_97(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_97_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 97 not found")
    return res

@router.post("/entity-97", response_model=SportsSchemaEntity97Response, status_code=201)
def create_entity_97(payload: SportsSchemaEntity97Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_97(payload)

@router.get("/entity-98", response_model=List[SportsSchemaEntity98Response])
def list_entities_98(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_98_list(skip=skip, limit=limit)

@router.get("/entity-98/{entity_id}", response_model=SportsSchemaEntity98Response)
def get_entity_98(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_98_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 98 not found")
    return res

@router.post("/entity-98", response_model=SportsSchemaEntity98Response, status_code=201)
def create_entity_98(payload: SportsSchemaEntity98Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_98(payload)

@router.get("/entity-99", response_model=List[SportsSchemaEntity99Response])
def list_entities_99(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_99_list(skip=skip, limit=limit)

@router.get("/entity-99/{entity_id}", response_model=SportsSchemaEntity99Response)
def get_entity_99(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_99_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 99 not found")
    return res

@router.post("/entity-99", response_model=SportsSchemaEntity99Response, status_code=201)
def create_entity_99(payload: SportsSchemaEntity99Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_99(payload)

@router.get("/entity-100", response_model=List[SportsSchemaEntity100Response])
def list_entities_100(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_100_list(skip=skip, limit=limit)

@router.get("/entity-100/{entity_id}", response_model=SportsSchemaEntity100Response)
def get_entity_100(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_100_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 100 not found")
    return res

@router.post("/entity-100", response_model=SportsSchemaEntity100Response, status_code=201)
def create_entity_100(payload: SportsSchemaEntity100Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_100(payload)

@router.get("/entity-101", response_model=List[SportsSchemaEntity101Response])
def list_entities_101(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_101_list(skip=skip, limit=limit)

@router.get("/entity-101/{entity_id}", response_model=SportsSchemaEntity101Response)
def get_entity_101(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_101_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 101 not found")
    return res

@router.post("/entity-101", response_model=SportsSchemaEntity101Response, status_code=201)
def create_entity_101(payload: SportsSchemaEntity101Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_101(payload)

@router.get("/entity-102", response_model=List[SportsSchemaEntity102Response])
def list_entities_102(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_102_list(skip=skip, limit=limit)

@router.get("/entity-102/{entity_id}", response_model=SportsSchemaEntity102Response)
def get_entity_102(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_102_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 102 not found")
    return res

@router.post("/entity-102", response_model=SportsSchemaEntity102Response, status_code=201)
def create_entity_102(payload: SportsSchemaEntity102Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_102(payload)

@router.get("/entity-103", response_model=List[SportsSchemaEntity103Response])
def list_entities_103(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_103_list(skip=skip, limit=limit)

@router.get("/entity-103/{entity_id}", response_model=SportsSchemaEntity103Response)
def get_entity_103(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_103_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 103 not found")
    return res

@router.post("/entity-103", response_model=SportsSchemaEntity103Response, status_code=201)
def create_entity_103(payload: SportsSchemaEntity103Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_103(payload)

@router.get("/entity-104", response_model=List[SportsSchemaEntity104Response])
def list_entities_104(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_104_list(skip=skip, limit=limit)

@router.get("/entity-104/{entity_id}", response_model=SportsSchemaEntity104Response)
def get_entity_104(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_104_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 104 not found")
    return res

@router.post("/entity-104", response_model=SportsSchemaEntity104Response, status_code=201)
def create_entity_104(payload: SportsSchemaEntity104Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_104(payload)

@router.get("/entity-105", response_model=List[SportsSchemaEntity105Response])
def list_entities_105(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_105_list(skip=skip, limit=limit)

@router.get("/entity-105/{entity_id}", response_model=SportsSchemaEntity105Response)
def get_entity_105(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_105_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 105 not found")
    return res

@router.post("/entity-105", response_model=SportsSchemaEntity105Response, status_code=201)
def create_entity_105(payload: SportsSchemaEntity105Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_105(payload)

@router.get("/entity-106", response_model=List[SportsSchemaEntity106Response])
def list_entities_106(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_106_list(skip=skip, limit=limit)

@router.get("/entity-106/{entity_id}", response_model=SportsSchemaEntity106Response)
def get_entity_106(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_106_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 106 not found")
    return res

@router.post("/entity-106", response_model=SportsSchemaEntity106Response, status_code=201)
def create_entity_106(payload: SportsSchemaEntity106Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_106(payload)

@router.get("/entity-107", response_model=List[SportsSchemaEntity107Response])
def list_entities_107(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_107_list(skip=skip, limit=limit)

@router.get("/entity-107/{entity_id}", response_model=SportsSchemaEntity107Response)
def get_entity_107(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_107_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 107 not found")
    return res

@router.post("/entity-107", response_model=SportsSchemaEntity107Response, status_code=201)
def create_entity_107(payload: SportsSchemaEntity107Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_107(payload)

@router.get("/entity-108", response_model=List[SportsSchemaEntity108Response])
def list_entities_108(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_108_list(skip=skip, limit=limit)

@router.get("/entity-108/{entity_id}", response_model=SportsSchemaEntity108Response)
def get_entity_108(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_108_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 108 not found")
    return res

@router.post("/entity-108", response_model=SportsSchemaEntity108Response, status_code=201)
def create_entity_108(payload: SportsSchemaEntity108Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_108(payload)

@router.get("/entity-109", response_model=List[SportsSchemaEntity109Response])
def list_entities_109(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_109_list(skip=skip, limit=limit)

@router.get("/entity-109/{entity_id}", response_model=SportsSchemaEntity109Response)
def get_entity_109(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_109_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 109 not found")
    return res

@router.post("/entity-109", response_model=SportsSchemaEntity109Response, status_code=201)
def create_entity_109(payload: SportsSchemaEntity109Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_109(payload)

@router.get("/entity-110", response_model=List[SportsSchemaEntity110Response])
def list_entities_110(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_110_list(skip=skip, limit=limit)

@router.get("/entity-110/{entity_id}", response_model=SportsSchemaEntity110Response)
def get_entity_110(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_110_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 110 not found")
    return res

@router.post("/entity-110", response_model=SportsSchemaEntity110Response, status_code=201)
def create_entity_110(payload: SportsSchemaEntity110Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_110(payload)

@router.get("/entity-111", response_model=List[SportsSchemaEntity111Response])
def list_entities_111(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_111_list(skip=skip, limit=limit)

@router.get("/entity-111/{entity_id}", response_model=SportsSchemaEntity111Response)
def get_entity_111(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_111_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 111 not found")
    return res

@router.post("/entity-111", response_model=SportsSchemaEntity111Response, status_code=201)
def create_entity_111(payload: SportsSchemaEntity111Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_111(payload)

@router.get("/entity-112", response_model=List[SportsSchemaEntity112Response])
def list_entities_112(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_112_list(skip=skip, limit=limit)

@router.get("/entity-112/{entity_id}", response_model=SportsSchemaEntity112Response)
def get_entity_112(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_112_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 112 not found")
    return res

@router.post("/entity-112", response_model=SportsSchemaEntity112Response, status_code=201)
def create_entity_112(payload: SportsSchemaEntity112Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_112(payload)

@router.get("/entity-113", response_model=List[SportsSchemaEntity113Response])
def list_entities_113(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_113_list(skip=skip, limit=limit)

@router.get("/entity-113/{entity_id}", response_model=SportsSchemaEntity113Response)
def get_entity_113(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_113_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 113 not found")
    return res

@router.post("/entity-113", response_model=SportsSchemaEntity113Response, status_code=201)
def create_entity_113(payload: SportsSchemaEntity113Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_113(payload)

@router.get("/entity-114", response_model=List[SportsSchemaEntity114Response])
def list_entities_114(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_114_list(skip=skip, limit=limit)

@router.get("/entity-114/{entity_id}", response_model=SportsSchemaEntity114Response)
def get_entity_114(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_114_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 114 not found")
    return res

@router.post("/entity-114", response_model=SportsSchemaEntity114Response, status_code=201)
def create_entity_114(payload: SportsSchemaEntity114Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_114(payload)

@router.get("/entity-115", response_model=List[SportsSchemaEntity115Response])
def list_entities_115(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_115_list(skip=skip, limit=limit)

@router.get("/entity-115/{entity_id}", response_model=SportsSchemaEntity115Response)
def get_entity_115(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_115_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 115 not found")
    return res

@router.post("/entity-115", response_model=SportsSchemaEntity115Response, status_code=201)
def create_entity_115(payload: SportsSchemaEntity115Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_115(payload)

@router.get("/entity-116", response_model=List[SportsSchemaEntity116Response])
def list_entities_116(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_116_list(skip=skip, limit=limit)

@router.get("/entity-116/{entity_id}", response_model=SportsSchemaEntity116Response)
def get_entity_116(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_116_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 116 not found")
    return res

@router.post("/entity-116", response_model=SportsSchemaEntity116Response, status_code=201)
def create_entity_116(payload: SportsSchemaEntity116Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_116(payload)

@router.get("/entity-117", response_model=List[SportsSchemaEntity117Response])
def list_entities_117(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_117_list(skip=skip, limit=limit)

@router.get("/entity-117/{entity_id}", response_model=SportsSchemaEntity117Response)
def get_entity_117(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_117_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 117 not found")
    return res

@router.post("/entity-117", response_model=SportsSchemaEntity117Response, status_code=201)
def create_entity_117(payload: SportsSchemaEntity117Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_117(payload)

@router.get("/entity-118", response_model=List[SportsSchemaEntity118Response])
def list_entities_118(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_118_list(skip=skip, limit=limit)

@router.get("/entity-118/{entity_id}", response_model=SportsSchemaEntity118Response)
def get_entity_118(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_118_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 118 not found")
    return res

@router.post("/entity-118", response_model=SportsSchemaEntity118Response, status_code=201)
def create_entity_118(payload: SportsSchemaEntity118Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_118(payload)

@router.get("/entity-119", response_model=List[SportsSchemaEntity119Response])
def list_entities_119(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_119_list(skip=skip, limit=limit)

@router.get("/entity-119/{entity_id}", response_model=SportsSchemaEntity119Response)
def get_entity_119(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_119_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 119 not found")
    return res

@router.post("/entity-119", response_model=SportsSchemaEntity119Response, status_code=201)
def create_entity_119(payload: SportsSchemaEntity119Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_119(payload)

@router.get("/entity-120", response_model=List[SportsSchemaEntity120Response])
def list_entities_120(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_120_list(skip=skip, limit=limit)

@router.get("/entity-120/{entity_id}", response_model=SportsSchemaEntity120Response)
def get_entity_120(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_120_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 120 not found")
    return res

@router.post("/entity-120", response_model=SportsSchemaEntity120Response, status_code=201)
def create_entity_120(payload: SportsSchemaEntity120Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_120(payload)

@router.get("/entity-121", response_model=List[SportsSchemaEntity121Response])
def list_entities_121(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_121_list(skip=skip, limit=limit)

@router.get("/entity-121/{entity_id}", response_model=SportsSchemaEntity121Response)
def get_entity_121(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_121_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 121 not found")
    return res

@router.post("/entity-121", response_model=SportsSchemaEntity121Response, status_code=201)
def create_entity_121(payload: SportsSchemaEntity121Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_121(payload)

@router.get("/entity-122", response_model=List[SportsSchemaEntity122Response])
def list_entities_122(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_122_list(skip=skip, limit=limit)

@router.get("/entity-122/{entity_id}", response_model=SportsSchemaEntity122Response)
def get_entity_122(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_122_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 122 not found")
    return res

@router.post("/entity-122", response_model=SportsSchemaEntity122Response, status_code=201)
def create_entity_122(payload: SportsSchemaEntity122Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_122(payload)

@router.get("/entity-123", response_model=List[SportsSchemaEntity123Response])
def list_entities_123(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_123_list(skip=skip, limit=limit)

@router.get("/entity-123/{entity_id}", response_model=SportsSchemaEntity123Response)
def get_entity_123(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_123_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 123 not found")
    return res

@router.post("/entity-123", response_model=SportsSchemaEntity123Response, status_code=201)
def create_entity_123(payload: SportsSchemaEntity123Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_123(payload)

@router.get("/entity-124", response_model=List[SportsSchemaEntity124Response])
def list_entities_124(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_124_list(skip=skip, limit=limit)

@router.get("/entity-124/{entity_id}", response_model=SportsSchemaEntity124Response)
def get_entity_124(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_124_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 124 not found")
    return res

@router.post("/entity-124", response_model=SportsSchemaEntity124Response, status_code=201)
def create_entity_124(payload: SportsSchemaEntity124Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_124(payload)

@router.get("/entity-125", response_model=List[SportsSchemaEntity125Response])
def list_entities_125(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_125_list(skip=skip, limit=limit)

@router.get("/entity-125/{entity_id}", response_model=SportsSchemaEntity125Response)
def get_entity_125(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_125_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 125 not found")
    return res

@router.post("/entity-125", response_model=SportsSchemaEntity125Response, status_code=201)
def create_entity_125(payload: SportsSchemaEntity125Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_125(payload)

@router.get("/entity-126", response_model=List[SportsSchemaEntity126Response])
def list_entities_126(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_126_list(skip=skip, limit=limit)

@router.get("/entity-126/{entity_id}", response_model=SportsSchemaEntity126Response)
def get_entity_126(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_126_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 126 not found")
    return res

@router.post("/entity-126", response_model=SportsSchemaEntity126Response, status_code=201)
def create_entity_126(payload: SportsSchemaEntity126Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_126(payload)

@router.get("/entity-127", response_model=List[SportsSchemaEntity127Response])
def list_entities_127(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_127_list(skip=skip, limit=limit)

@router.get("/entity-127/{entity_id}", response_model=SportsSchemaEntity127Response)
def get_entity_127(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_127_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 127 not found")
    return res

@router.post("/entity-127", response_model=SportsSchemaEntity127Response, status_code=201)
def create_entity_127(payload: SportsSchemaEntity127Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_127(payload)

@router.get("/entity-128", response_model=List[SportsSchemaEntity128Response])
def list_entities_128(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_128_list(skip=skip, limit=limit)

@router.get("/entity-128/{entity_id}", response_model=SportsSchemaEntity128Response)
def get_entity_128(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_128_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 128 not found")
    return res

@router.post("/entity-128", response_model=SportsSchemaEntity128Response, status_code=201)
def create_entity_128(payload: SportsSchemaEntity128Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_128(payload)

@router.get("/entity-129", response_model=List[SportsSchemaEntity129Response])
def list_entities_129(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_129_list(skip=skip, limit=limit)

@router.get("/entity-129/{entity_id}", response_model=SportsSchemaEntity129Response)
def get_entity_129(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_129_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 129 not found")
    return res

@router.post("/entity-129", response_model=SportsSchemaEntity129Response, status_code=201)
def create_entity_129(payload: SportsSchemaEntity129Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_129(payload)

@router.get("/entity-130", response_model=List[SportsSchemaEntity130Response])
def list_entities_130(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_130_list(skip=skip, limit=limit)

@router.get("/entity-130/{entity_id}", response_model=SportsSchemaEntity130Response)
def get_entity_130(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_130_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 130 not found")
    return res

@router.post("/entity-130", response_model=SportsSchemaEntity130Response, status_code=201)
def create_entity_130(payload: SportsSchemaEntity130Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_130(payload)

@router.get("/entity-131", response_model=List[SportsSchemaEntity131Response])
def list_entities_131(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_131_list(skip=skip, limit=limit)

@router.get("/entity-131/{entity_id}", response_model=SportsSchemaEntity131Response)
def get_entity_131(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_131_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 131 not found")
    return res

@router.post("/entity-131", response_model=SportsSchemaEntity131Response, status_code=201)
def create_entity_131(payload: SportsSchemaEntity131Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_131(payload)

@router.get("/entity-132", response_model=List[SportsSchemaEntity132Response])
def list_entities_132(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_132_list(skip=skip, limit=limit)

@router.get("/entity-132/{entity_id}", response_model=SportsSchemaEntity132Response)
def get_entity_132(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_132_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 132 not found")
    return res

@router.post("/entity-132", response_model=SportsSchemaEntity132Response, status_code=201)
def create_entity_132(payload: SportsSchemaEntity132Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_132(payload)

@router.get("/entity-133", response_model=List[SportsSchemaEntity133Response])
def list_entities_133(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_133_list(skip=skip, limit=limit)

@router.get("/entity-133/{entity_id}", response_model=SportsSchemaEntity133Response)
def get_entity_133(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_133_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 133 not found")
    return res

@router.post("/entity-133", response_model=SportsSchemaEntity133Response, status_code=201)
def create_entity_133(payload: SportsSchemaEntity133Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_133(payload)

@router.get("/entity-134", response_model=List[SportsSchemaEntity134Response])
def list_entities_134(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_134_list(skip=skip, limit=limit)

@router.get("/entity-134/{entity_id}", response_model=SportsSchemaEntity134Response)
def get_entity_134(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_134_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 134 not found")
    return res

@router.post("/entity-134", response_model=SportsSchemaEntity134Response, status_code=201)
def create_entity_134(payload: SportsSchemaEntity134Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_134(payload)

@router.get("/entity-135", response_model=List[SportsSchemaEntity135Response])
def list_entities_135(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_135_list(skip=skip, limit=limit)

@router.get("/entity-135/{entity_id}", response_model=SportsSchemaEntity135Response)
def get_entity_135(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_135_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 135 not found")
    return res

@router.post("/entity-135", response_model=SportsSchemaEntity135Response, status_code=201)
def create_entity_135(payload: SportsSchemaEntity135Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_135(payload)

@router.get("/entity-136", response_model=List[SportsSchemaEntity136Response])
def list_entities_136(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_136_list(skip=skip, limit=limit)

@router.get("/entity-136/{entity_id}", response_model=SportsSchemaEntity136Response)
def get_entity_136(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_136_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 136 not found")
    return res

@router.post("/entity-136", response_model=SportsSchemaEntity136Response, status_code=201)
def create_entity_136(payload: SportsSchemaEntity136Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_136(payload)

@router.get("/entity-137", response_model=List[SportsSchemaEntity137Response])
def list_entities_137(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_137_list(skip=skip, limit=limit)

@router.get("/entity-137/{entity_id}", response_model=SportsSchemaEntity137Response)
def get_entity_137(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_137_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 137 not found")
    return res

@router.post("/entity-137", response_model=SportsSchemaEntity137Response, status_code=201)
def create_entity_137(payload: SportsSchemaEntity137Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_137(payload)

@router.get("/entity-138", response_model=List[SportsSchemaEntity138Response])
def list_entities_138(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_138_list(skip=skip, limit=limit)

@router.get("/entity-138/{entity_id}", response_model=SportsSchemaEntity138Response)
def get_entity_138(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_138_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 138 not found")
    return res

@router.post("/entity-138", response_model=SportsSchemaEntity138Response, status_code=201)
def create_entity_138(payload: SportsSchemaEntity138Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_138(payload)

@router.get("/entity-139", response_model=List[SportsSchemaEntity139Response])
def list_entities_139(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_139_list(skip=skip, limit=limit)

@router.get("/entity-139/{entity_id}", response_model=SportsSchemaEntity139Response)
def get_entity_139(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_139_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 139 not found")
    return res

@router.post("/entity-139", response_model=SportsSchemaEntity139Response, status_code=201)
def create_entity_139(payload: SportsSchemaEntity139Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_139(payload)

@router.get("/entity-140", response_model=List[SportsSchemaEntity140Response])
def list_entities_140(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_140_list(skip=skip, limit=limit)

@router.get("/entity-140/{entity_id}", response_model=SportsSchemaEntity140Response)
def get_entity_140(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_140_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 140 not found")
    return res

@router.post("/entity-140", response_model=SportsSchemaEntity140Response, status_code=201)
def create_entity_140(payload: SportsSchemaEntity140Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_140(payload)

@router.get("/entity-141", response_model=List[SportsSchemaEntity141Response])
def list_entities_141(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_141_list(skip=skip, limit=limit)

@router.get("/entity-141/{entity_id}", response_model=SportsSchemaEntity141Response)
def get_entity_141(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_141_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 141 not found")
    return res

@router.post("/entity-141", response_model=SportsSchemaEntity141Response, status_code=201)
def create_entity_141(payload: SportsSchemaEntity141Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_141(payload)

@router.get("/entity-142", response_model=List[SportsSchemaEntity142Response])
def list_entities_142(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_142_list(skip=skip, limit=limit)

@router.get("/entity-142/{entity_id}", response_model=SportsSchemaEntity142Response)
def get_entity_142(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_142_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 142 not found")
    return res

@router.post("/entity-142", response_model=SportsSchemaEntity142Response, status_code=201)
def create_entity_142(payload: SportsSchemaEntity142Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_142(payload)

@router.get("/entity-143", response_model=List[SportsSchemaEntity143Response])
def list_entities_143(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_143_list(skip=skip, limit=limit)

@router.get("/entity-143/{entity_id}", response_model=SportsSchemaEntity143Response)
def get_entity_143(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_143_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 143 not found")
    return res

@router.post("/entity-143", response_model=SportsSchemaEntity143Response, status_code=201)
def create_entity_143(payload: SportsSchemaEntity143Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_143(payload)

@router.get("/entity-144", response_model=List[SportsSchemaEntity144Response])
def list_entities_144(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_144_list(skip=skip, limit=limit)

@router.get("/entity-144/{entity_id}", response_model=SportsSchemaEntity144Response)
def get_entity_144(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_144_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 144 not found")
    return res

@router.post("/entity-144", response_model=SportsSchemaEntity144Response, status_code=201)
def create_entity_144(payload: SportsSchemaEntity144Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_144(payload)

@router.get("/entity-145", response_model=List[SportsSchemaEntity145Response])
def list_entities_145(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_145_list(skip=skip, limit=limit)

@router.get("/entity-145/{entity_id}", response_model=SportsSchemaEntity145Response)
def get_entity_145(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_145_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 145 not found")
    return res

@router.post("/entity-145", response_model=SportsSchemaEntity145Response, status_code=201)
def create_entity_145(payload: SportsSchemaEntity145Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_145(payload)

@router.get("/entity-146", response_model=List[SportsSchemaEntity146Response])
def list_entities_146(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_146_list(skip=skip, limit=limit)

@router.get("/entity-146/{entity_id}", response_model=SportsSchemaEntity146Response)
def get_entity_146(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_146_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 146 not found")
    return res

@router.post("/entity-146", response_model=SportsSchemaEntity146Response, status_code=201)
def create_entity_146(payload: SportsSchemaEntity146Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_146(payload)

@router.get("/entity-147", response_model=List[SportsSchemaEntity147Response])
def list_entities_147(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_147_list(skip=skip, limit=limit)

@router.get("/entity-147/{entity_id}", response_model=SportsSchemaEntity147Response)
def get_entity_147(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_147_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 147 not found")
    return res

@router.post("/entity-147", response_model=SportsSchemaEntity147Response, status_code=201)
def create_entity_147(payload: SportsSchemaEntity147Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_147(payload)

@router.get("/entity-148", response_model=List[SportsSchemaEntity148Response])
def list_entities_148(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_148_list(skip=skip, limit=limit)

@router.get("/entity-148/{entity_id}", response_model=SportsSchemaEntity148Response)
def get_entity_148(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_148_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 148 not found")
    return res

@router.post("/entity-148", response_model=SportsSchemaEntity148Response, status_code=201)
def create_entity_148(payload: SportsSchemaEntity148Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_148(payload)

@router.get("/entity-149", response_model=List[SportsSchemaEntity149Response])
def list_entities_149(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_149_list(skip=skip, limit=limit)

@router.get("/entity-149/{entity_id}", response_model=SportsSchemaEntity149Response)
def get_entity_149(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_149_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 149 not found")
    return res

@router.post("/entity-149", response_model=SportsSchemaEntity149Response, status_code=201)
def create_entity_149(payload: SportsSchemaEntity149Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_149(payload)

@router.get("/entity-150", response_model=List[SportsSchemaEntity150Response])
def list_entities_150(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_150_list(skip=skip, limit=limit)

@router.get("/entity-150/{entity_id}", response_model=SportsSchemaEntity150Response)
def get_entity_150(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_150_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 150 not found")
    return res

@router.post("/entity-150", response_model=SportsSchemaEntity150Response, status_code=201)
def create_entity_150(payload: SportsSchemaEntity150Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_150(payload)

@router.get("/entity-151", response_model=List[SportsSchemaEntity151Response])
def list_entities_151(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_151_list(skip=skip, limit=limit)

@router.get("/entity-151/{entity_id}", response_model=SportsSchemaEntity151Response)
def get_entity_151(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_151_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 151 not found")
    return res

@router.post("/entity-151", response_model=SportsSchemaEntity151Response, status_code=201)
def create_entity_151(payload: SportsSchemaEntity151Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_151(payload)

@router.get("/entity-152", response_model=List[SportsSchemaEntity152Response])
def list_entities_152(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_152_list(skip=skip, limit=limit)

@router.get("/entity-152/{entity_id}", response_model=SportsSchemaEntity152Response)
def get_entity_152(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_152_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 152 not found")
    return res

@router.post("/entity-152", response_model=SportsSchemaEntity152Response, status_code=201)
def create_entity_152(payload: SportsSchemaEntity152Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_152(payload)

@router.get("/entity-153", response_model=List[SportsSchemaEntity153Response])
def list_entities_153(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_153_list(skip=skip, limit=limit)

@router.get("/entity-153/{entity_id}", response_model=SportsSchemaEntity153Response)
def get_entity_153(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_153_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 153 not found")
    return res

@router.post("/entity-153", response_model=SportsSchemaEntity153Response, status_code=201)
def create_entity_153(payload: SportsSchemaEntity153Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_153(payload)

@router.get("/entity-154", response_model=List[SportsSchemaEntity154Response])
def list_entities_154(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_154_list(skip=skip, limit=limit)

@router.get("/entity-154/{entity_id}", response_model=SportsSchemaEntity154Response)
def get_entity_154(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_154_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 154 not found")
    return res

@router.post("/entity-154", response_model=SportsSchemaEntity154Response, status_code=201)
def create_entity_154(payload: SportsSchemaEntity154Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_154(payload)

@router.get("/entity-155", response_model=List[SportsSchemaEntity155Response])
def list_entities_155(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_155_list(skip=skip, limit=limit)

@router.get("/entity-155/{entity_id}", response_model=SportsSchemaEntity155Response)
def get_entity_155(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_155_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 155 not found")
    return res

@router.post("/entity-155", response_model=SportsSchemaEntity155Response, status_code=201)
def create_entity_155(payload: SportsSchemaEntity155Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_155(payload)

@router.get("/entity-156", response_model=List[SportsSchemaEntity156Response])
def list_entities_156(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_156_list(skip=skip, limit=limit)

@router.get("/entity-156/{entity_id}", response_model=SportsSchemaEntity156Response)
def get_entity_156(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_156_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 156 not found")
    return res

@router.post("/entity-156", response_model=SportsSchemaEntity156Response, status_code=201)
def create_entity_156(payload: SportsSchemaEntity156Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_156(payload)

@router.get("/entity-157", response_model=List[SportsSchemaEntity157Response])
def list_entities_157(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_157_list(skip=skip, limit=limit)

@router.get("/entity-157/{entity_id}", response_model=SportsSchemaEntity157Response)
def get_entity_157(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_157_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 157 not found")
    return res

@router.post("/entity-157", response_model=SportsSchemaEntity157Response, status_code=201)
def create_entity_157(payload: SportsSchemaEntity157Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_157(payload)

@router.get("/entity-158", response_model=List[SportsSchemaEntity158Response])
def list_entities_158(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_158_list(skip=skip, limit=limit)

@router.get("/entity-158/{entity_id}", response_model=SportsSchemaEntity158Response)
def get_entity_158(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_158_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 158 not found")
    return res

@router.post("/entity-158", response_model=SportsSchemaEntity158Response, status_code=201)
def create_entity_158(payload: SportsSchemaEntity158Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_158(payload)

@router.get("/entity-159", response_model=List[SportsSchemaEntity159Response])
def list_entities_159(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_159_list(skip=skip, limit=limit)

@router.get("/entity-159/{entity_id}", response_model=SportsSchemaEntity159Response)
def get_entity_159(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_159_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 159 not found")
    return res

@router.post("/entity-159", response_model=SportsSchemaEntity159Response, status_code=201)
def create_entity_159(payload: SportsSchemaEntity159Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_159(payload)

@router.get("/entity-160", response_model=List[SportsSchemaEntity160Response])
def list_entities_160(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_160_list(skip=skip, limit=limit)

@router.get("/entity-160/{entity_id}", response_model=SportsSchemaEntity160Response)
def get_entity_160(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_160_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 160 not found")
    return res

@router.post("/entity-160", response_model=SportsSchemaEntity160Response, status_code=201)
def create_entity_160(payload: SportsSchemaEntity160Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_160(payload)

@router.get("/entity-161", response_model=List[SportsSchemaEntity161Response])
def list_entities_161(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_161_list(skip=skip, limit=limit)

@router.get("/entity-161/{entity_id}", response_model=SportsSchemaEntity161Response)
def get_entity_161(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_161_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 161 not found")
    return res

@router.post("/entity-161", response_model=SportsSchemaEntity161Response, status_code=201)
def create_entity_161(payload: SportsSchemaEntity161Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_161(payload)

@router.get("/entity-162", response_model=List[SportsSchemaEntity162Response])
def list_entities_162(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_162_list(skip=skip, limit=limit)

@router.get("/entity-162/{entity_id}", response_model=SportsSchemaEntity162Response)
def get_entity_162(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_162_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 162 not found")
    return res

@router.post("/entity-162", response_model=SportsSchemaEntity162Response, status_code=201)
def create_entity_162(payload: SportsSchemaEntity162Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_162(payload)

@router.get("/entity-163", response_model=List[SportsSchemaEntity163Response])
def list_entities_163(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_163_list(skip=skip, limit=limit)

@router.get("/entity-163/{entity_id}", response_model=SportsSchemaEntity163Response)
def get_entity_163(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_163_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 163 not found")
    return res

@router.post("/entity-163", response_model=SportsSchemaEntity163Response, status_code=201)
def create_entity_163(payload: SportsSchemaEntity163Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_163(payload)

@router.get("/entity-164", response_model=List[SportsSchemaEntity164Response])
def list_entities_164(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_164_list(skip=skip, limit=limit)

@router.get("/entity-164/{entity_id}", response_model=SportsSchemaEntity164Response)
def get_entity_164(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_164_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 164 not found")
    return res

@router.post("/entity-164", response_model=SportsSchemaEntity164Response, status_code=201)
def create_entity_164(payload: SportsSchemaEntity164Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_164(payload)

@router.get("/entity-165", response_model=List[SportsSchemaEntity165Response])
def list_entities_165(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_165_list(skip=skip, limit=limit)

@router.get("/entity-165/{entity_id}", response_model=SportsSchemaEntity165Response)
def get_entity_165(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_165_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 165 not found")
    return res

@router.post("/entity-165", response_model=SportsSchemaEntity165Response, status_code=201)
def create_entity_165(payload: SportsSchemaEntity165Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_165(payload)

@router.get("/entity-166", response_model=List[SportsSchemaEntity166Response])
def list_entities_166(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_166_list(skip=skip, limit=limit)

@router.get("/entity-166/{entity_id}", response_model=SportsSchemaEntity166Response)
def get_entity_166(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_166_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 166 not found")
    return res

@router.post("/entity-166", response_model=SportsSchemaEntity166Response, status_code=201)
def create_entity_166(payload: SportsSchemaEntity166Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_166(payload)

@router.get("/entity-167", response_model=List[SportsSchemaEntity167Response])
def list_entities_167(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_167_list(skip=skip, limit=limit)

@router.get("/entity-167/{entity_id}", response_model=SportsSchemaEntity167Response)
def get_entity_167(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_167_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 167 not found")
    return res

@router.post("/entity-167", response_model=SportsSchemaEntity167Response, status_code=201)
def create_entity_167(payload: SportsSchemaEntity167Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_167(payload)

@router.get("/entity-168", response_model=List[SportsSchemaEntity168Response])
def list_entities_168(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_168_list(skip=skip, limit=limit)

@router.get("/entity-168/{entity_id}", response_model=SportsSchemaEntity168Response)
def get_entity_168(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_168_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 168 not found")
    return res

@router.post("/entity-168", response_model=SportsSchemaEntity168Response, status_code=201)
def create_entity_168(payload: SportsSchemaEntity168Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_168(payload)

@router.get("/entity-169", response_model=List[SportsSchemaEntity169Response])
def list_entities_169(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_169_list(skip=skip, limit=limit)

@router.get("/entity-169/{entity_id}", response_model=SportsSchemaEntity169Response)
def get_entity_169(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_169_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 169 not found")
    return res

@router.post("/entity-169", response_model=SportsSchemaEntity169Response, status_code=201)
def create_entity_169(payload: SportsSchemaEntity169Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_169(payload)

@router.get("/entity-170", response_model=List[SportsSchemaEntity170Response])
def list_entities_170(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_170_list(skip=skip, limit=limit)

@router.get("/entity-170/{entity_id}", response_model=SportsSchemaEntity170Response)
def get_entity_170(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_170_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 170 not found")
    return res

@router.post("/entity-170", response_model=SportsSchemaEntity170Response, status_code=201)
def create_entity_170(payload: SportsSchemaEntity170Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_170(payload)

@router.get("/entity-171", response_model=List[SportsSchemaEntity171Response])
def list_entities_171(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_171_list(skip=skip, limit=limit)

@router.get("/entity-171/{entity_id}", response_model=SportsSchemaEntity171Response)
def get_entity_171(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_171_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 171 not found")
    return res

@router.post("/entity-171", response_model=SportsSchemaEntity171Response, status_code=201)
def create_entity_171(payload: SportsSchemaEntity171Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_171(payload)

@router.get("/entity-172", response_model=List[SportsSchemaEntity172Response])
def list_entities_172(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_172_list(skip=skip, limit=limit)

@router.get("/entity-172/{entity_id}", response_model=SportsSchemaEntity172Response)
def get_entity_172(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_172_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 172 not found")
    return res

@router.post("/entity-172", response_model=SportsSchemaEntity172Response, status_code=201)
def create_entity_172(payload: SportsSchemaEntity172Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_172(payload)

@router.get("/entity-173", response_model=List[SportsSchemaEntity173Response])
def list_entities_173(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_173_list(skip=skip, limit=limit)

@router.get("/entity-173/{entity_id}", response_model=SportsSchemaEntity173Response)
def get_entity_173(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_173_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 173 not found")
    return res

@router.post("/entity-173", response_model=SportsSchemaEntity173Response, status_code=201)
def create_entity_173(payload: SportsSchemaEntity173Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_173(payload)

@router.get("/entity-174", response_model=List[SportsSchemaEntity174Response])
def list_entities_174(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_174_list(skip=skip, limit=limit)

@router.get("/entity-174/{entity_id}", response_model=SportsSchemaEntity174Response)
def get_entity_174(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_174_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 174 not found")
    return res

@router.post("/entity-174", response_model=SportsSchemaEntity174Response, status_code=201)
def create_entity_174(payload: SportsSchemaEntity174Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_174(payload)

@router.get("/entity-175", response_model=List[SportsSchemaEntity175Response])
def list_entities_175(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_175_list(skip=skip, limit=limit)

@router.get("/entity-175/{entity_id}", response_model=SportsSchemaEntity175Response)
def get_entity_175(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_175_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 175 not found")
    return res

@router.post("/entity-175", response_model=SportsSchemaEntity175Response, status_code=201)
def create_entity_175(payload: SportsSchemaEntity175Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_175(payload)

@router.get("/entity-176", response_model=List[SportsSchemaEntity176Response])
def list_entities_176(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_176_list(skip=skip, limit=limit)

@router.get("/entity-176/{entity_id}", response_model=SportsSchemaEntity176Response)
def get_entity_176(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_176_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 176 not found")
    return res

@router.post("/entity-176", response_model=SportsSchemaEntity176Response, status_code=201)
def create_entity_176(payload: SportsSchemaEntity176Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_176(payload)

@router.get("/entity-177", response_model=List[SportsSchemaEntity177Response])
def list_entities_177(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_177_list(skip=skip, limit=limit)

@router.get("/entity-177/{entity_id}", response_model=SportsSchemaEntity177Response)
def get_entity_177(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_177_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 177 not found")
    return res

@router.post("/entity-177", response_model=SportsSchemaEntity177Response, status_code=201)
def create_entity_177(payload: SportsSchemaEntity177Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_177(payload)

@router.get("/entity-178", response_model=List[SportsSchemaEntity178Response])
def list_entities_178(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_178_list(skip=skip, limit=limit)

@router.get("/entity-178/{entity_id}", response_model=SportsSchemaEntity178Response)
def get_entity_178(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_178_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 178 not found")
    return res

@router.post("/entity-178", response_model=SportsSchemaEntity178Response, status_code=201)
def create_entity_178(payload: SportsSchemaEntity178Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_178(payload)

@router.get("/entity-179", response_model=List[SportsSchemaEntity179Response])
def list_entities_179(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_179_list(skip=skip, limit=limit)

@router.get("/entity-179/{entity_id}", response_model=SportsSchemaEntity179Response)
def get_entity_179(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_179_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 179 not found")
    return res

@router.post("/entity-179", response_model=SportsSchemaEntity179Response, status_code=201)
def create_entity_179(payload: SportsSchemaEntity179Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_179(payload)

@router.get("/entity-180", response_model=List[SportsSchemaEntity180Response])
def list_entities_180(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_180_list(skip=skip, limit=limit)

@router.get("/entity-180/{entity_id}", response_model=SportsSchemaEntity180Response)
def get_entity_180(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_180_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 180 not found")
    return res

@router.post("/entity-180", response_model=SportsSchemaEntity180Response, status_code=201)
def create_entity_180(payload: SportsSchemaEntity180Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_180(payload)

@router.get("/entity-181", response_model=List[SportsSchemaEntity181Response])
def list_entities_181(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_181_list(skip=skip, limit=limit)

@router.get("/entity-181/{entity_id}", response_model=SportsSchemaEntity181Response)
def get_entity_181(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_181_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 181 not found")
    return res

@router.post("/entity-181", response_model=SportsSchemaEntity181Response, status_code=201)
def create_entity_181(payload: SportsSchemaEntity181Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_181(payload)

@router.get("/entity-182", response_model=List[SportsSchemaEntity182Response])
def list_entities_182(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_182_list(skip=skip, limit=limit)

@router.get("/entity-182/{entity_id}", response_model=SportsSchemaEntity182Response)
def get_entity_182(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_182_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 182 not found")
    return res

@router.post("/entity-182", response_model=SportsSchemaEntity182Response, status_code=201)
def create_entity_182(payload: SportsSchemaEntity182Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_182(payload)

@router.get("/entity-183", response_model=List[SportsSchemaEntity183Response])
def list_entities_183(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_183_list(skip=skip, limit=limit)

@router.get("/entity-183/{entity_id}", response_model=SportsSchemaEntity183Response)
def get_entity_183(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_183_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 183 not found")
    return res

@router.post("/entity-183", response_model=SportsSchemaEntity183Response, status_code=201)
def create_entity_183(payload: SportsSchemaEntity183Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_183(payload)

@router.get("/entity-184", response_model=List[SportsSchemaEntity184Response])
def list_entities_184(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_184_list(skip=skip, limit=limit)

@router.get("/entity-184/{entity_id}", response_model=SportsSchemaEntity184Response)
def get_entity_184(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_184_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 184 not found")
    return res

@router.post("/entity-184", response_model=SportsSchemaEntity184Response, status_code=201)
def create_entity_184(payload: SportsSchemaEntity184Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_184(payload)

@router.get("/entity-185", response_model=List[SportsSchemaEntity185Response])
def list_entities_185(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_185_list(skip=skip, limit=limit)

@router.get("/entity-185/{entity_id}", response_model=SportsSchemaEntity185Response)
def get_entity_185(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_185_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 185 not found")
    return res

@router.post("/entity-185", response_model=SportsSchemaEntity185Response, status_code=201)
def create_entity_185(payload: SportsSchemaEntity185Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_185(payload)

@router.get("/entity-186", response_model=List[SportsSchemaEntity186Response])
def list_entities_186(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_186_list(skip=skip, limit=limit)

@router.get("/entity-186/{entity_id}", response_model=SportsSchemaEntity186Response)
def get_entity_186(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_186_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 186 not found")
    return res

@router.post("/entity-186", response_model=SportsSchemaEntity186Response, status_code=201)
def create_entity_186(payload: SportsSchemaEntity186Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_186(payload)

@router.get("/entity-187", response_model=List[SportsSchemaEntity187Response])
def list_entities_187(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_187_list(skip=skip, limit=limit)

@router.get("/entity-187/{entity_id}", response_model=SportsSchemaEntity187Response)
def get_entity_187(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_187_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 187 not found")
    return res

@router.post("/entity-187", response_model=SportsSchemaEntity187Response, status_code=201)
def create_entity_187(payload: SportsSchemaEntity187Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_187(payload)

@router.get("/entity-188", response_model=List[SportsSchemaEntity188Response])
def list_entities_188(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_188_list(skip=skip, limit=limit)

@router.get("/entity-188/{entity_id}", response_model=SportsSchemaEntity188Response)
def get_entity_188(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_188_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 188 not found")
    return res

@router.post("/entity-188", response_model=SportsSchemaEntity188Response, status_code=201)
def create_entity_188(payload: SportsSchemaEntity188Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_188(payload)

@router.get("/entity-189", response_model=List[SportsSchemaEntity189Response])
def list_entities_189(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_189_list(skip=skip, limit=limit)

@router.get("/entity-189/{entity_id}", response_model=SportsSchemaEntity189Response)
def get_entity_189(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_189_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 189 not found")
    return res

@router.post("/entity-189", response_model=SportsSchemaEntity189Response, status_code=201)
def create_entity_189(payload: SportsSchemaEntity189Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_189(payload)

@router.get("/entity-190", response_model=List[SportsSchemaEntity190Response])
def list_entities_190(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_190_list(skip=skip, limit=limit)

@router.get("/entity-190/{entity_id}", response_model=SportsSchemaEntity190Response)
def get_entity_190(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_190_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 190 not found")
    return res

@router.post("/entity-190", response_model=SportsSchemaEntity190Response, status_code=201)
def create_entity_190(payload: SportsSchemaEntity190Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_190(payload)

@router.get("/entity-191", response_model=List[SportsSchemaEntity191Response])
def list_entities_191(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_191_list(skip=skip, limit=limit)

@router.get("/entity-191/{entity_id}", response_model=SportsSchemaEntity191Response)
def get_entity_191(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_191_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 191 not found")
    return res

@router.post("/entity-191", response_model=SportsSchemaEntity191Response, status_code=201)
def create_entity_191(payload: SportsSchemaEntity191Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_191(payload)

@router.get("/entity-192", response_model=List[SportsSchemaEntity192Response])
def list_entities_192(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_192_list(skip=skip, limit=limit)

@router.get("/entity-192/{entity_id}", response_model=SportsSchemaEntity192Response)
def get_entity_192(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_192_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 192 not found")
    return res

@router.post("/entity-192", response_model=SportsSchemaEntity192Response, status_code=201)
def create_entity_192(payload: SportsSchemaEntity192Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_192(payload)

@router.get("/entity-193", response_model=List[SportsSchemaEntity193Response])
def list_entities_193(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_193_list(skip=skip, limit=limit)

@router.get("/entity-193/{entity_id}", response_model=SportsSchemaEntity193Response)
def get_entity_193(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_193_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 193 not found")
    return res

@router.post("/entity-193", response_model=SportsSchemaEntity193Response, status_code=201)
def create_entity_193(payload: SportsSchemaEntity193Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_193(payload)

@router.get("/entity-194", response_model=List[SportsSchemaEntity194Response])
def list_entities_194(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_194_list(skip=skip, limit=limit)

@router.get("/entity-194/{entity_id}", response_model=SportsSchemaEntity194Response)
def get_entity_194(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_194_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 194 not found")
    return res

@router.post("/entity-194", response_model=SportsSchemaEntity194Response, status_code=201)
def create_entity_194(payload: SportsSchemaEntity194Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_194(payload)

@router.get("/entity-195", response_model=List[SportsSchemaEntity195Response])
def list_entities_195(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_195_list(skip=skip, limit=limit)

@router.get("/entity-195/{entity_id}", response_model=SportsSchemaEntity195Response)
def get_entity_195(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_195_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 195 not found")
    return res

@router.post("/entity-195", response_model=SportsSchemaEntity195Response, status_code=201)
def create_entity_195(payload: SportsSchemaEntity195Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_195(payload)

@router.get("/entity-196", response_model=List[SportsSchemaEntity196Response])
def list_entities_196(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_196_list(skip=skip, limit=limit)

@router.get("/entity-196/{entity_id}", response_model=SportsSchemaEntity196Response)
def get_entity_196(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_196_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 196 not found")
    return res

@router.post("/entity-196", response_model=SportsSchemaEntity196Response, status_code=201)
def create_entity_196(payload: SportsSchemaEntity196Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_196(payload)

@router.get("/entity-197", response_model=List[SportsSchemaEntity197Response])
def list_entities_197(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_197_list(skip=skip, limit=limit)

@router.get("/entity-197/{entity_id}", response_model=SportsSchemaEntity197Response)
def get_entity_197(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_197_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 197 not found")
    return res

@router.post("/entity-197", response_model=SportsSchemaEntity197Response, status_code=201)
def create_entity_197(payload: SportsSchemaEntity197Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_197(payload)

@router.get("/entity-198", response_model=List[SportsSchemaEntity198Response])
def list_entities_198(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_198_list(skip=skip, limit=limit)

@router.get("/entity-198/{entity_id}", response_model=SportsSchemaEntity198Response)
def get_entity_198(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_198_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 198 not found")
    return res

@router.post("/entity-198", response_model=SportsSchemaEntity198Response, status_code=201)
def create_entity_198(payload: SportsSchemaEntity198Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_198(payload)

@router.get("/entity-199", response_model=List[SportsSchemaEntity199Response])
def list_entities_199(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_199_list(skip=skip, limit=limit)

@router.get("/entity-199/{entity_id}", response_model=SportsSchemaEntity199Response)
def get_entity_199(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_199_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 199 not found")
    return res

@router.post("/entity-199", response_model=SportsSchemaEntity199Response, status_code=201)
def create_entity_199(payload: SportsSchemaEntity199Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_199(payload)

@router.get("/entity-200", response_model=List[SportsSchemaEntity200Response])
def list_entities_200(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_200_list(skip=skip, limit=limit)

@router.get("/entity-200/{entity_id}", response_model=SportsSchemaEntity200Response)
def get_entity_200(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_200_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 200 not found")
    return res

@router.post("/entity-200", response_model=SportsSchemaEntity200Response, status_code=201)
def create_entity_200(payload: SportsSchemaEntity200Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_200(payload)

@router.get("/entity-201", response_model=List[SportsSchemaEntity201Response])
def list_entities_201(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_201_list(skip=skip, limit=limit)

@router.get("/entity-201/{entity_id}", response_model=SportsSchemaEntity201Response)
def get_entity_201(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_201_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 201 not found")
    return res

@router.post("/entity-201", response_model=SportsSchemaEntity201Response, status_code=201)
def create_entity_201(payload: SportsSchemaEntity201Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_201(payload)

@router.get("/entity-202", response_model=List[SportsSchemaEntity202Response])
def list_entities_202(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_202_list(skip=skip, limit=limit)

@router.get("/entity-202/{entity_id}", response_model=SportsSchemaEntity202Response)
def get_entity_202(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_202_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 202 not found")
    return res

@router.post("/entity-202", response_model=SportsSchemaEntity202Response, status_code=201)
def create_entity_202(payload: SportsSchemaEntity202Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_202(payload)

@router.get("/entity-203", response_model=List[SportsSchemaEntity203Response])
def list_entities_203(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_203_list(skip=skip, limit=limit)

@router.get("/entity-203/{entity_id}", response_model=SportsSchemaEntity203Response)
def get_entity_203(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_203_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 203 not found")
    return res

@router.post("/entity-203", response_model=SportsSchemaEntity203Response, status_code=201)
def create_entity_203(payload: SportsSchemaEntity203Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_203(payload)

@router.get("/entity-204", response_model=List[SportsSchemaEntity204Response])
def list_entities_204(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_204_list(skip=skip, limit=limit)

@router.get("/entity-204/{entity_id}", response_model=SportsSchemaEntity204Response)
def get_entity_204(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_204_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 204 not found")
    return res

@router.post("/entity-204", response_model=SportsSchemaEntity204Response, status_code=201)
def create_entity_204(payload: SportsSchemaEntity204Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_204(payload)

@router.get("/entity-205", response_model=List[SportsSchemaEntity205Response])
def list_entities_205(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_205_list(skip=skip, limit=limit)

@router.get("/entity-205/{entity_id}", response_model=SportsSchemaEntity205Response)
def get_entity_205(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_205_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 205 not found")
    return res

@router.post("/entity-205", response_model=SportsSchemaEntity205Response, status_code=201)
def create_entity_205(payload: SportsSchemaEntity205Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_205(payload)

@router.get("/entity-206", response_model=List[SportsSchemaEntity206Response])
def list_entities_206(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_206_list(skip=skip, limit=limit)

@router.get("/entity-206/{entity_id}", response_model=SportsSchemaEntity206Response)
def get_entity_206(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_206_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 206 not found")
    return res

@router.post("/entity-206", response_model=SportsSchemaEntity206Response, status_code=201)
def create_entity_206(payload: SportsSchemaEntity206Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_206(payload)

@router.get("/entity-207", response_model=List[SportsSchemaEntity207Response])
def list_entities_207(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_207_list(skip=skip, limit=limit)

@router.get("/entity-207/{entity_id}", response_model=SportsSchemaEntity207Response)
def get_entity_207(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_207_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 207 not found")
    return res

@router.post("/entity-207", response_model=SportsSchemaEntity207Response, status_code=201)
def create_entity_207(payload: SportsSchemaEntity207Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_207(payload)

@router.get("/entity-208", response_model=List[SportsSchemaEntity208Response])
def list_entities_208(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_208_list(skip=skip, limit=limit)

@router.get("/entity-208/{entity_id}", response_model=SportsSchemaEntity208Response)
def get_entity_208(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_208_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 208 not found")
    return res

@router.post("/entity-208", response_model=SportsSchemaEntity208Response, status_code=201)
def create_entity_208(payload: SportsSchemaEntity208Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_208(payload)

@router.get("/entity-209", response_model=List[SportsSchemaEntity209Response])
def list_entities_209(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_209_list(skip=skip, limit=limit)

@router.get("/entity-209/{entity_id}", response_model=SportsSchemaEntity209Response)
def get_entity_209(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_209_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 209 not found")
    return res

@router.post("/entity-209", response_model=SportsSchemaEntity209Response, status_code=201)
def create_entity_209(payload: SportsSchemaEntity209Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_209(payload)

@router.get("/entity-210", response_model=List[SportsSchemaEntity210Response])
def list_entities_210(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_210_list(skip=skip, limit=limit)

@router.get("/entity-210/{entity_id}", response_model=SportsSchemaEntity210Response)
def get_entity_210(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_210_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 210 not found")
    return res

@router.post("/entity-210", response_model=SportsSchemaEntity210Response, status_code=201)
def create_entity_210(payload: SportsSchemaEntity210Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_210(payload)

@router.get("/entity-211", response_model=List[SportsSchemaEntity211Response])
def list_entities_211(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_211_list(skip=skip, limit=limit)

@router.get("/entity-211/{entity_id}", response_model=SportsSchemaEntity211Response)
def get_entity_211(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_211_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 211 not found")
    return res

@router.post("/entity-211", response_model=SportsSchemaEntity211Response, status_code=201)
def create_entity_211(payload: SportsSchemaEntity211Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_211(payload)

@router.get("/entity-212", response_model=List[SportsSchemaEntity212Response])
def list_entities_212(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_212_list(skip=skip, limit=limit)

@router.get("/entity-212/{entity_id}", response_model=SportsSchemaEntity212Response)
def get_entity_212(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_212_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 212 not found")
    return res

@router.post("/entity-212", response_model=SportsSchemaEntity212Response, status_code=201)
def create_entity_212(payload: SportsSchemaEntity212Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_212(payload)

@router.get("/entity-213", response_model=List[SportsSchemaEntity213Response])
def list_entities_213(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_213_list(skip=skip, limit=limit)

@router.get("/entity-213/{entity_id}", response_model=SportsSchemaEntity213Response)
def get_entity_213(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_213_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 213 not found")
    return res

@router.post("/entity-213", response_model=SportsSchemaEntity213Response, status_code=201)
def create_entity_213(payload: SportsSchemaEntity213Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_213(payload)

@router.get("/entity-214", response_model=List[SportsSchemaEntity214Response])
def list_entities_214(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_214_list(skip=skip, limit=limit)

@router.get("/entity-214/{entity_id}", response_model=SportsSchemaEntity214Response)
def get_entity_214(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_214_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 214 not found")
    return res

@router.post("/entity-214", response_model=SportsSchemaEntity214Response, status_code=201)
def create_entity_214(payload: SportsSchemaEntity214Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_214(payload)

@router.get("/entity-215", response_model=List[SportsSchemaEntity215Response])
def list_entities_215(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_215_list(skip=skip, limit=limit)

@router.get("/entity-215/{entity_id}", response_model=SportsSchemaEntity215Response)
def get_entity_215(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_215_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 215 not found")
    return res

@router.post("/entity-215", response_model=SportsSchemaEntity215Response, status_code=201)
def create_entity_215(payload: SportsSchemaEntity215Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_215(payload)

@router.get("/entity-216", response_model=List[SportsSchemaEntity216Response])
def list_entities_216(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_216_list(skip=skip, limit=limit)

@router.get("/entity-216/{entity_id}", response_model=SportsSchemaEntity216Response)
def get_entity_216(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_216_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 216 not found")
    return res

@router.post("/entity-216", response_model=SportsSchemaEntity216Response, status_code=201)
def create_entity_216(payload: SportsSchemaEntity216Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_216(payload)

@router.get("/entity-217", response_model=List[SportsSchemaEntity217Response])
def list_entities_217(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_217_list(skip=skip, limit=limit)

@router.get("/entity-217/{entity_id}", response_model=SportsSchemaEntity217Response)
def get_entity_217(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_217_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 217 not found")
    return res

@router.post("/entity-217", response_model=SportsSchemaEntity217Response, status_code=201)
def create_entity_217(payload: SportsSchemaEntity217Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_217(payload)

@router.get("/entity-218", response_model=List[SportsSchemaEntity218Response])
def list_entities_218(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_218_list(skip=skip, limit=limit)

@router.get("/entity-218/{entity_id}", response_model=SportsSchemaEntity218Response)
def get_entity_218(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_218_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 218 not found")
    return res

@router.post("/entity-218", response_model=SportsSchemaEntity218Response, status_code=201)
def create_entity_218(payload: SportsSchemaEntity218Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_218(payload)

@router.get("/entity-219", response_model=List[SportsSchemaEntity219Response])
def list_entities_219(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_219_list(skip=skip, limit=limit)

@router.get("/entity-219/{entity_id}", response_model=SportsSchemaEntity219Response)
def get_entity_219(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_219_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 219 not found")
    return res

@router.post("/entity-219", response_model=SportsSchemaEntity219Response, status_code=201)
def create_entity_219(payload: SportsSchemaEntity219Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_219(payload)

@router.get("/entity-220", response_model=List[SportsSchemaEntity220Response])
def list_entities_220(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_220_list(skip=skip, limit=limit)

@router.get("/entity-220/{entity_id}", response_model=SportsSchemaEntity220Response)
def get_entity_220(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_220_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 220 not found")
    return res

@router.post("/entity-220", response_model=SportsSchemaEntity220Response, status_code=201)
def create_entity_220(payload: SportsSchemaEntity220Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_220(payload)

@router.get("/entity-221", response_model=List[SportsSchemaEntity221Response])
def list_entities_221(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_221_list(skip=skip, limit=limit)

@router.get("/entity-221/{entity_id}", response_model=SportsSchemaEntity221Response)
def get_entity_221(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_221_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 221 not found")
    return res

@router.post("/entity-221", response_model=SportsSchemaEntity221Response, status_code=201)
def create_entity_221(payload: SportsSchemaEntity221Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_221(payload)

@router.get("/entity-222", response_model=List[SportsSchemaEntity222Response])
def list_entities_222(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_222_list(skip=skip, limit=limit)

@router.get("/entity-222/{entity_id}", response_model=SportsSchemaEntity222Response)
def get_entity_222(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_222_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 222 not found")
    return res

@router.post("/entity-222", response_model=SportsSchemaEntity222Response, status_code=201)
def create_entity_222(payload: SportsSchemaEntity222Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_222(payload)

@router.get("/entity-223", response_model=List[SportsSchemaEntity223Response])
def list_entities_223(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_223_list(skip=skip, limit=limit)

@router.get("/entity-223/{entity_id}", response_model=SportsSchemaEntity223Response)
def get_entity_223(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_223_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 223 not found")
    return res

@router.post("/entity-223", response_model=SportsSchemaEntity223Response, status_code=201)
def create_entity_223(payload: SportsSchemaEntity223Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_223(payload)

@router.get("/entity-224", response_model=List[SportsSchemaEntity224Response])
def list_entities_224(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_224_list(skip=skip, limit=limit)

@router.get("/entity-224/{entity_id}", response_model=SportsSchemaEntity224Response)
def get_entity_224(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_224_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 224 not found")
    return res

@router.post("/entity-224", response_model=SportsSchemaEntity224Response, status_code=201)
def create_entity_224(payload: SportsSchemaEntity224Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_224(payload)

@router.get("/entity-225", response_model=List[SportsSchemaEntity225Response])
def list_entities_225(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_225_list(skip=skip, limit=limit)

@router.get("/entity-225/{entity_id}", response_model=SportsSchemaEntity225Response)
def get_entity_225(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_225_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 225 not found")
    return res

@router.post("/entity-225", response_model=SportsSchemaEntity225Response, status_code=201)
def create_entity_225(payload: SportsSchemaEntity225Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_225(payload)

@router.get("/entity-226", response_model=List[SportsSchemaEntity226Response])
def list_entities_226(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_226_list(skip=skip, limit=limit)

@router.get("/entity-226/{entity_id}", response_model=SportsSchemaEntity226Response)
def get_entity_226(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_226_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 226 not found")
    return res

@router.post("/entity-226", response_model=SportsSchemaEntity226Response, status_code=201)
def create_entity_226(payload: SportsSchemaEntity226Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_226(payload)

@router.get("/entity-227", response_model=List[SportsSchemaEntity227Response])
def list_entities_227(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_227_list(skip=skip, limit=limit)

@router.get("/entity-227/{entity_id}", response_model=SportsSchemaEntity227Response)
def get_entity_227(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_227_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 227 not found")
    return res

@router.post("/entity-227", response_model=SportsSchemaEntity227Response, status_code=201)
def create_entity_227(payload: SportsSchemaEntity227Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_227(payload)

@router.get("/entity-228", response_model=List[SportsSchemaEntity228Response])
def list_entities_228(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_228_list(skip=skip, limit=limit)

@router.get("/entity-228/{entity_id}", response_model=SportsSchemaEntity228Response)
def get_entity_228(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_228_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 228 not found")
    return res

@router.post("/entity-228", response_model=SportsSchemaEntity228Response, status_code=201)
def create_entity_228(payload: SportsSchemaEntity228Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_228(payload)

@router.get("/entity-229", response_model=List[SportsSchemaEntity229Response])
def list_entities_229(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_229_list(skip=skip, limit=limit)

@router.get("/entity-229/{entity_id}", response_model=SportsSchemaEntity229Response)
def get_entity_229(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_229_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 229 not found")
    return res

@router.post("/entity-229", response_model=SportsSchemaEntity229Response, status_code=201)
def create_entity_229(payload: SportsSchemaEntity229Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_229(payload)

@router.get("/entity-230", response_model=List[SportsSchemaEntity230Response])
def list_entities_230(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_230_list(skip=skip, limit=limit)

@router.get("/entity-230/{entity_id}", response_model=SportsSchemaEntity230Response)
def get_entity_230(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_230_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 230 not found")
    return res

@router.post("/entity-230", response_model=SportsSchemaEntity230Response, status_code=201)
def create_entity_230(payload: SportsSchemaEntity230Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_230(payload)

@router.get("/entity-231", response_model=List[SportsSchemaEntity231Response])
def list_entities_231(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_231_list(skip=skip, limit=limit)

@router.get("/entity-231/{entity_id}", response_model=SportsSchemaEntity231Response)
def get_entity_231(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_231_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 231 not found")
    return res

@router.post("/entity-231", response_model=SportsSchemaEntity231Response, status_code=201)
def create_entity_231(payload: SportsSchemaEntity231Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_231(payload)

@router.get("/entity-232", response_model=List[SportsSchemaEntity232Response])
def list_entities_232(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_232_list(skip=skip, limit=limit)

@router.get("/entity-232/{entity_id}", response_model=SportsSchemaEntity232Response)
def get_entity_232(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_232_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 232 not found")
    return res

@router.post("/entity-232", response_model=SportsSchemaEntity232Response, status_code=201)
def create_entity_232(payload: SportsSchemaEntity232Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_232(payload)

@router.get("/entity-233", response_model=List[SportsSchemaEntity233Response])
def list_entities_233(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_233_list(skip=skip, limit=limit)

@router.get("/entity-233/{entity_id}", response_model=SportsSchemaEntity233Response)
def get_entity_233(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_233_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 233 not found")
    return res

@router.post("/entity-233", response_model=SportsSchemaEntity233Response, status_code=201)
def create_entity_233(payload: SportsSchemaEntity233Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_233(payload)

@router.get("/entity-234", response_model=List[SportsSchemaEntity234Response])
def list_entities_234(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_234_list(skip=skip, limit=limit)

@router.get("/entity-234/{entity_id}", response_model=SportsSchemaEntity234Response)
def get_entity_234(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_234_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 234 not found")
    return res

@router.post("/entity-234", response_model=SportsSchemaEntity234Response, status_code=201)
def create_entity_234(payload: SportsSchemaEntity234Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_234(payload)

@router.get("/entity-235", response_model=List[SportsSchemaEntity235Response])
def list_entities_235(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_235_list(skip=skip, limit=limit)

@router.get("/entity-235/{entity_id}", response_model=SportsSchemaEntity235Response)
def get_entity_235(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_235_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 235 not found")
    return res

@router.post("/entity-235", response_model=SportsSchemaEntity235Response, status_code=201)
def create_entity_235(payload: SportsSchemaEntity235Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_235(payload)

@router.get("/entity-236", response_model=List[SportsSchemaEntity236Response])
def list_entities_236(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_236_list(skip=skip, limit=limit)

@router.get("/entity-236/{entity_id}", response_model=SportsSchemaEntity236Response)
def get_entity_236(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_236_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 236 not found")
    return res

@router.post("/entity-236", response_model=SportsSchemaEntity236Response, status_code=201)
def create_entity_236(payload: SportsSchemaEntity236Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_236(payload)

@router.get("/entity-237", response_model=List[SportsSchemaEntity237Response])
def list_entities_237(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_237_list(skip=skip, limit=limit)

@router.get("/entity-237/{entity_id}", response_model=SportsSchemaEntity237Response)
def get_entity_237(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_237_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 237 not found")
    return res

@router.post("/entity-237", response_model=SportsSchemaEntity237Response, status_code=201)
def create_entity_237(payload: SportsSchemaEntity237Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_237(payload)

@router.get("/entity-238", response_model=List[SportsSchemaEntity238Response])
def list_entities_238(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_238_list(skip=skip, limit=limit)

@router.get("/entity-238/{entity_id}", response_model=SportsSchemaEntity238Response)
def get_entity_238(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_238_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 238 not found")
    return res

@router.post("/entity-238", response_model=SportsSchemaEntity238Response, status_code=201)
def create_entity_238(payload: SportsSchemaEntity238Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_238(payload)

@router.get("/entity-239", response_model=List[SportsSchemaEntity239Response])
def list_entities_239(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_239_list(skip=skip, limit=limit)

@router.get("/entity-239/{entity_id}", response_model=SportsSchemaEntity239Response)
def get_entity_239(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_239_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 239 not found")
    return res

@router.post("/entity-239", response_model=SportsSchemaEntity239Response, status_code=201)
def create_entity_239(payload: SportsSchemaEntity239Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_239(payload)

@router.get("/entity-240", response_model=List[SportsSchemaEntity240Response])
def list_entities_240(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_240_list(skip=skip, limit=limit)

@router.get("/entity-240/{entity_id}", response_model=SportsSchemaEntity240Response)
def get_entity_240(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_240_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 240 not found")
    return res

@router.post("/entity-240", response_model=SportsSchemaEntity240Response, status_code=201)
def create_entity_240(payload: SportsSchemaEntity240Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_240(payload)

@router.get("/entity-241", response_model=List[SportsSchemaEntity241Response])
def list_entities_241(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_241_list(skip=skip, limit=limit)

@router.get("/entity-241/{entity_id}", response_model=SportsSchemaEntity241Response)
def get_entity_241(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_241_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 241 not found")
    return res

@router.post("/entity-241", response_model=SportsSchemaEntity241Response, status_code=201)
def create_entity_241(payload: SportsSchemaEntity241Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_241(payload)

@router.get("/entity-242", response_model=List[SportsSchemaEntity242Response])
def list_entities_242(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_242_list(skip=skip, limit=limit)

@router.get("/entity-242/{entity_id}", response_model=SportsSchemaEntity242Response)
def get_entity_242(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_242_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 242 not found")
    return res

@router.post("/entity-242", response_model=SportsSchemaEntity242Response, status_code=201)
def create_entity_242(payload: SportsSchemaEntity242Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_242(payload)

@router.get("/entity-243", response_model=List[SportsSchemaEntity243Response])
def list_entities_243(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_243_list(skip=skip, limit=limit)

@router.get("/entity-243/{entity_id}", response_model=SportsSchemaEntity243Response)
def get_entity_243(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_243_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 243 not found")
    return res

@router.post("/entity-243", response_model=SportsSchemaEntity243Response, status_code=201)
def create_entity_243(payload: SportsSchemaEntity243Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_243(payload)

@router.get("/entity-244", response_model=List[SportsSchemaEntity244Response])
def list_entities_244(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_244_list(skip=skip, limit=limit)

@router.get("/entity-244/{entity_id}", response_model=SportsSchemaEntity244Response)
def get_entity_244(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_244_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 244 not found")
    return res

@router.post("/entity-244", response_model=SportsSchemaEntity244Response, status_code=201)
def create_entity_244(payload: SportsSchemaEntity244Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_244(payload)

@router.get("/entity-245", response_model=List[SportsSchemaEntity245Response])
def list_entities_245(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_245_list(skip=skip, limit=limit)

@router.get("/entity-245/{entity_id}", response_model=SportsSchemaEntity245Response)
def get_entity_245(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_245_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 245 not found")
    return res

@router.post("/entity-245", response_model=SportsSchemaEntity245Response, status_code=201)
def create_entity_245(payload: SportsSchemaEntity245Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_245(payload)

@router.get("/entity-246", response_model=List[SportsSchemaEntity246Response])
def list_entities_246(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_246_list(skip=skip, limit=limit)

@router.get("/entity-246/{entity_id}", response_model=SportsSchemaEntity246Response)
def get_entity_246(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_246_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 246 not found")
    return res

@router.post("/entity-246", response_model=SportsSchemaEntity246Response, status_code=201)
def create_entity_246(payload: SportsSchemaEntity246Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_246(payload)

@router.get("/entity-247", response_model=List[SportsSchemaEntity247Response])
def list_entities_247(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_247_list(skip=skip, limit=limit)

@router.get("/entity-247/{entity_id}", response_model=SportsSchemaEntity247Response)
def get_entity_247(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_247_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 247 not found")
    return res

@router.post("/entity-247", response_model=SportsSchemaEntity247Response, status_code=201)
def create_entity_247(payload: SportsSchemaEntity247Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_247(payload)

@router.get("/entity-248", response_model=List[SportsSchemaEntity248Response])
def list_entities_248(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_248_list(skip=skip, limit=limit)

@router.get("/entity-248/{entity_id}", response_model=SportsSchemaEntity248Response)
def get_entity_248(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_248_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 248 not found")
    return res

@router.post("/entity-248", response_model=SportsSchemaEntity248Response, status_code=201)
def create_entity_248(payload: SportsSchemaEntity248Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_248(payload)

@router.get("/entity-249", response_model=List[SportsSchemaEntity249Response])
def list_entities_249(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_249_list(skip=skip, limit=limit)

@router.get("/entity-249/{entity_id}", response_model=SportsSchemaEntity249Response)
def get_entity_249(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_249_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 249 not found")
    return res

@router.post("/entity-249", response_model=SportsSchemaEntity249Response, status_code=201)
def create_entity_249(payload: SportsSchemaEntity249Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_249(payload)

@router.get("/entity-250", response_model=List[SportsSchemaEntity250Response])
def list_entities_250(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.get_entity_250_list(skip=skip, limit=limit)

@router.get("/entity-250/{entity_id}", response_model=SportsSchemaEntity250Response)
def get_entity_250(entity_id: int, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    res = srv.get_entity_250_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 250 not found")
    return res

@router.post("/entity-250", response_model=SportsSchemaEntity250Response, status_code=201)
def create_entity_250(payload: SportsSchemaEntity250Create, db: Session = Depends(get_db)):
    srv = SportsDomainService(db)
    return srv.create_entity_250(payload)

