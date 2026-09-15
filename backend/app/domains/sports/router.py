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

