"""
Human Resources & Faculty Management - FastAPI Router Endpoints
Module: app.domains.hr.router
"""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domains.hr.schemas import *
from app.domains.hr.service import HrDomainService

router = APIRouter(prefix="/hr", tags=["Human Resources & Faculty Management"])

@router.get("/entity-1", response_model=List[HrSchemaEntity1Response])
def list_entities_1(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_1_list(skip=skip, limit=limit)

@router.get("/entity-1/{entity_id}", response_model=HrSchemaEntity1Response)
def get_entity_1(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_1_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 1 not found")
    return res

@router.post("/entity-1", response_model=HrSchemaEntity1Response, status_code=201)
def create_entity_1(payload: HrSchemaEntity1Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_1(payload)

@router.get("/entity-2", response_model=List[HrSchemaEntity2Response])
def list_entities_2(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_2_list(skip=skip, limit=limit)

@router.get("/entity-2/{entity_id}", response_model=HrSchemaEntity2Response)
def get_entity_2(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_2_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 2 not found")
    return res

@router.post("/entity-2", response_model=HrSchemaEntity2Response, status_code=201)
def create_entity_2(payload: HrSchemaEntity2Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_2(payload)

@router.get("/entity-3", response_model=List[HrSchemaEntity3Response])
def list_entities_3(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_3_list(skip=skip, limit=limit)

@router.get("/entity-3/{entity_id}", response_model=HrSchemaEntity3Response)
def get_entity_3(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_3_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 3 not found")
    return res

@router.post("/entity-3", response_model=HrSchemaEntity3Response, status_code=201)
def create_entity_3(payload: HrSchemaEntity3Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_3(payload)

@router.get("/entity-4", response_model=List[HrSchemaEntity4Response])
def list_entities_4(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_4_list(skip=skip, limit=limit)

@router.get("/entity-4/{entity_id}", response_model=HrSchemaEntity4Response)
def get_entity_4(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_4_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 4 not found")
    return res

@router.post("/entity-4", response_model=HrSchemaEntity4Response, status_code=201)
def create_entity_4(payload: HrSchemaEntity4Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_4(payload)

@router.get("/entity-5", response_model=List[HrSchemaEntity5Response])
def list_entities_5(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_5_list(skip=skip, limit=limit)

@router.get("/entity-5/{entity_id}", response_model=HrSchemaEntity5Response)
def get_entity_5(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_5_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 5 not found")
    return res

@router.post("/entity-5", response_model=HrSchemaEntity5Response, status_code=201)
def create_entity_5(payload: HrSchemaEntity5Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_5(payload)

@router.get("/entity-6", response_model=List[HrSchemaEntity6Response])
def list_entities_6(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_6_list(skip=skip, limit=limit)

@router.get("/entity-6/{entity_id}", response_model=HrSchemaEntity6Response)
def get_entity_6(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_6_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 6 not found")
    return res

@router.post("/entity-6", response_model=HrSchemaEntity6Response, status_code=201)
def create_entity_6(payload: HrSchemaEntity6Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_6(payload)

@router.get("/entity-7", response_model=List[HrSchemaEntity7Response])
def list_entities_7(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_7_list(skip=skip, limit=limit)

@router.get("/entity-7/{entity_id}", response_model=HrSchemaEntity7Response)
def get_entity_7(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_7_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 7 not found")
    return res

@router.post("/entity-7", response_model=HrSchemaEntity7Response, status_code=201)
def create_entity_7(payload: HrSchemaEntity7Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_7(payload)

@router.get("/entity-8", response_model=List[HrSchemaEntity8Response])
def list_entities_8(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_8_list(skip=skip, limit=limit)

@router.get("/entity-8/{entity_id}", response_model=HrSchemaEntity8Response)
def get_entity_8(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_8_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 8 not found")
    return res

@router.post("/entity-8", response_model=HrSchemaEntity8Response, status_code=201)
def create_entity_8(payload: HrSchemaEntity8Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_8(payload)

@router.get("/entity-9", response_model=List[HrSchemaEntity9Response])
def list_entities_9(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_9_list(skip=skip, limit=limit)

@router.get("/entity-9/{entity_id}", response_model=HrSchemaEntity9Response)
def get_entity_9(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_9_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 9 not found")
    return res

@router.post("/entity-9", response_model=HrSchemaEntity9Response, status_code=201)
def create_entity_9(payload: HrSchemaEntity9Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_9(payload)

@router.get("/entity-10", response_model=List[HrSchemaEntity10Response])
def list_entities_10(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_10_list(skip=skip, limit=limit)

@router.get("/entity-10/{entity_id}", response_model=HrSchemaEntity10Response)
def get_entity_10(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_10_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 10 not found")
    return res

@router.post("/entity-10", response_model=HrSchemaEntity10Response, status_code=201)
def create_entity_10(payload: HrSchemaEntity10Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_10(payload)

@router.get("/entity-11", response_model=List[HrSchemaEntity11Response])
def list_entities_11(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_11_list(skip=skip, limit=limit)

@router.get("/entity-11/{entity_id}", response_model=HrSchemaEntity11Response)
def get_entity_11(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_11_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 11 not found")
    return res

@router.post("/entity-11", response_model=HrSchemaEntity11Response, status_code=201)
def create_entity_11(payload: HrSchemaEntity11Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_11(payload)

@router.get("/entity-12", response_model=List[HrSchemaEntity12Response])
def list_entities_12(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_12_list(skip=skip, limit=limit)

@router.get("/entity-12/{entity_id}", response_model=HrSchemaEntity12Response)
def get_entity_12(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_12_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 12 not found")
    return res

@router.post("/entity-12", response_model=HrSchemaEntity12Response, status_code=201)
def create_entity_12(payload: HrSchemaEntity12Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_12(payload)

@router.get("/entity-13", response_model=List[HrSchemaEntity13Response])
def list_entities_13(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_13_list(skip=skip, limit=limit)

@router.get("/entity-13/{entity_id}", response_model=HrSchemaEntity13Response)
def get_entity_13(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_13_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 13 not found")
    return res

@router.post("/entity-13", response_model=HrSchemaEntity13Response, status_code=201)
def create_entity_13(payload: HrSchemaEntity13Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_13(payload)

@router.get("/entity-14", response_model=List[HrSchemaEntity14Response])
def list_entities_14(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_14_list(skip=skip, limit=limit)

@router.get("/entity-14/{entity_id}", response_model=HrSchemaEntity14Response)
def get_entity_14(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_14_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 14 not found")
    return res

@router.post("/entity-14", response_model=HrSchemaEntity14Response, status_code=201)
def create_entity_14(payload: HrSchemaEntity14Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_14(payload)

@router.get("/entity-15", response_model=List[HrSchemaEntity15Response])
def list_entities_15(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_15_list(skip=skip, limit=limit)

@router.get("/entity-15/{entity_id}", response_model=HrSchemaEntity15Response)
def get_entity_15(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_15_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 15 not found")
    return res

@router.post("/entity-15", response_model=HrSchemaEntity15Response, status_code=201)
def create_entity_15(payload: HrSchemaEntity15Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_15(payload)

@router.get("/entity-16", response_model=List[HrSchemaEntity16Response])
def list_entities_16(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_16_list(skip=skip, limit=limit)

@router.get("/entity-16/{entity_id}", response_model=HrSchemaEntity16Response)
def get_entity_16(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_16_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 16 not found")
    return res

@router.post("/entity-16", response_model=HrSchemaEntity16Response, status_code=201)
def create_entity_16(payload: HrSchemaEntity16Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_16(payload)

@router.get("/entity-17", response_model=List[HrSchemaEntity17Response])
def list_entities_17(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_17_list(skip=skip, limit=limit)

@router.get("/entity-17/{entity_id}", response_model=HrSchemaEntity17Response)
def get_entity_17(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_17_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 17 not found")
    return res

@router.post("/entity-17", response_model=HrSchemaEntity17Response, status_code=201)
def create_entity_17(payload: HrSchemaEntity17Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_17(payload)

@router.get("/entity-18", response_model=List[HrSchemaEntity18Response])
def list_entities_18(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_18_list(skip=skip, limit=limit)

@router.get("/entity-18/{entity_id}", response_model=HrSchemaEntity18Response)
def get_entity_18(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_18_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 18 not found")
    return res

@router.post("/entity-18", response_model=HrSchemaEntity18Response, status_code=201)
def create_entity_18(payload: HrSchemaEntity18Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_18(payload)

@router.get("/entity-19", response_model=List[HrSchemaEntity19Response])
def list_entities_19(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_19_list(skip=skip, limit=limit)

@router.get("/entity-19/{entity_id}", response_model=HrSchemaEntity19Response)
def get_entity_19(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_19_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 19 not found")
    return res

@router.post("/entity-19", response_model=HrSchemaEntity19Response, status_code=201)
def create_entity_19(payload: HrSchemaEntity19Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_19(payload)

@router.get("/entity-20", response_model=List[HrSchemaEntity20Response])
def list_entities_20(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_20_list(skip=skip, limit=limit)

@router.get("/entity-20/{entity_id}", response_model=HrSchemaEntity20Response)
def get_entity_20(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_20_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 20 not found")
    return res

@router.post("/entity-20", response_model=HrSchemaEntity20Response, status_code=201)
def create_entity_20(payload: HrSchemaEntity20Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_20(payload)

@router.get("/entity-21", response_model=List[HrSchemaEntity21Response])
def list_entities_21(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_21_list(skip=skip, limit=limit)

@router.get("/entity-21/{entity_id}", response_model=HrSchemaEntity21Response)
def get_entity_21(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_21_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 21 not found")
    return res

@router.post("/entity-21", response_model=HrSchemaEntity21Response, status_code=201)
def create_entity_21(payload: HrSchemaEntity21Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_21(payload)

@router.get("/entity-22", response_model=List[HrSchemaEntity22Response])
def list_entities_22(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_22_list(skip=skip, limit=limit)

@router.get("/entity-22/{entity_id}", response_model=HrSchemaEntity22Response)
def get_entity_22(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_22_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 22 not found")
    return res

@router.post("/entity-22", response_model=HrSchemaEntity22Response, status_code=201)
def create_entity_22(payload: HrSchemaEntity22Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_22(payload)

@router.get("/entity-23", response_model=List[HrSchemaEntity23Response])
def list_entities_23(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_23_list(skip=skip, limit=limit)

@router.get("/entity-23/{entity_id}", response_model=HrSchemaEntity23Response)
def get_entity_23(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_23_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 23 not found")
    return res

@router.post("/entity-23", response_model=HrSchemaEntity23Response, status_code=201)
def create_entity_23(payload: HrSchemaEntity23Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_23(payload)

@router.get("/entity-24", response_model=List[HrSchemaEntity24Response])
def list_entities_24(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_24_list(skip=skip, limit=limit)

@router.get("/entity-24/{entity_id}", response_model=HrSchemaEntity24Response)
def get_entity_24(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_24_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 24 not found")
    return res

@router.post("/entity-24", response_model=HrSchemaEntity24Response, status_code=201)
def create_entity_24(payload: HrSchemaEntity24Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_24(payload)

@router.get("/entity-25", response_model=List[HrSchemaEntity25Response])
def list_entities_25(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_25_list(skip=skip, limit=limit)

@router.get("/entity-25/{entity_id}", response_model=HrSchemaEntity25Response)
def get_entity_25(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_25_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 25 not found")
    return res

@router.post("/entity-25", response_model=HrSchemaEntity25Response, status_code=201)
def create_entity_25(payload: HrSchemaEntity25Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_25(payload)

@router.get("/entity-26", response_model=List[HrSchemaEntity26Response])
def list_entities_26(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_26_list(skip=skip, limit=limit)

@router.get("/entity-26/{entity_id}", response_model=HrSchemaEntity26Response)
def get_entity_26(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_26_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 26 not found")
    return res

@router.post("/entity-26", response_model=HrSchemaEntity26Response, status_code=201)
def create_entity_26(payload: HrSchemaEntity26Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_26(payload)

@router.get("/entity-27", response_model=List[HrSchemaEntity27Response])
def list_entities_27(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_27_list(skip=skip, limit=limit)

@router.get("/entity-27/{entity_id}", response_model=HrSchemaEntity27Response)
def get_entity_27(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_27_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 27 not found")
    return res

@router.post("/entity-27", response_model=HrSchemaEntity27Response, status_code=201)
def create_entity_27(payload: HrSchemaEntity27Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_27(payload)

@router.get("/entity-28", response_model=List[HrSchemaEntity28Response])
def list_entities_28(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_28_list(skip=skip, limit=limit)

@router.get("/entity-28/{entity_id}", response_model=HrSchemaEntity28Response)
def get_entity_28(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_28_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 28 not found")
    return res

@router.post("/entity-28", response_model=HrSchemaEntity28Response, status_code=201)
def create_entity_28(payload: HrSchemaEntity28Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_28(payload)

@router.get("/entity-29", response_model=List[HrSchemaEntity29Response])
def list_entities_29(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_29_list(skip=skip, limit=limit)

@router.get("/entity-29/{entity_id}", response_model=HrSchemaEntity29Response)
def get_entity_29(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_29_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 29 not found")
    return res

@router.post("/entity-29", response_model=HrSchemaEntity29Response, status_code=201)
def create_entity_29(payload: HrSchemaEntity29Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_29(payload)

@router.get("/entity-30", response_model=List[HrSchemaEntity30Response])
def list_entities_30(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_30_list(skip=skip, limit=limit)

@router.get("/entity-30/{entity_id}", response_model=HrSchemaEntity30Response)
def get_entity_30(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_30_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 30 not found")
    return res

@router.post("/entity-30", response_model=HrSchemaEntity30Response, status_code=201)
def create_entity_30(payload: HrSchemaEntity30Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_30(payload)

@router.get("/entity-31", response_model=List[HrSchemaEntity31Response])
def list_entities_31(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_31_list(skip=skip, limit=limit)

@router.get("/entity-31/{entity_id}", response_model=HrSchemaEntity31Response)
def get_entity_31(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_31_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 31 not found")
    return res

@router.post("/entity-31", response_model=HrSchemaEntity31Response, status_code=201)
def create_entity_31(payload: HrSchemaEntity31Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_31(payload)

@router.get("/entity-32", response_model=List[HrSchemaEntity32Response])
def list_entities_32(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_32_list(skip=skip, limit=limit)

@router.get("/entity-32/{entity_id}", response_model=HrSchemaEntity32Response)
def get_entity_32(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_32_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 32 not found")
    return res

@router.post("/entity-32", response_model=HrSchemaEntity32Response, status_code=201)
def create_entity_32(payload: HrSchemaEntity32Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_32(payload)

@router.get("/entity-33", response_model=List[HrSchemaEntity33Response])
def list_entities_33(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_33_list(skip=skip, limit=limit)

@router.get("/entity-33/{entity_id}", response_model=HrSchemaEntity33Response)
def get_entity_33(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_33_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 33 not found")
    return res

@router.post("/entity-33", response_model=HrSchemaEntity33Response, status_code=201)
def create_entity_33(payload: HrSchemaEntity33Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_33(payload)

@router.get("/entity-34", response_model=List[HrSchemaEntity34Response])
def list_entities_34(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_34_list(skip=skip, limit=limit)

@router.get("/entity-34/{entity_id}", response_model=HrSchemaEntity34Response)
def get_entity_34(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_34_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 34 not found")
    return res

@router.post("/entity-34", response_model=HrSchemaEntity34Response, status_code=201)
def create_entity_34(payload: HrSchemaEntity34Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_34(payload)

@router.get("/entity-35", response_model=List[HrSchemaEntity35Response])
def list_entities_35(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_35_list(skip=skip, limit=limit)

@router.get("/entity-35/{entity_id}", response_model=HrSchemaEntity35Response)
def get_entity_35(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_35_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 35 not found")
    return res

@router.post("/entity-35", response_model=HrSchemaEntity35Response, status_code=201)
def create_entity_35(payload: HrSchemaEntity35Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_35(payload)

@router.get("/entity-36", response_model=List[HrSchemaEntity36Response])
def list_entities_36(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_36_list(skip=skip, limit=limit)

@router.get("/entity-36/{entity_id}", response_model=HrSchemaEntity36Response)
def get_entity_36(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_36_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 36 not found")
    return res

@router.post("/entity-36", response_model=HrSchemaEntity36Response, status_code=201)
def create_entity_36(payload: HrSchemaEntity36Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_36(payload)

@router.get("/entity-37", response_model=List[HrSchemaEntity37Response])
def list_entities_37(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_37_list(skip=skip, limit=limit)

@router.get("/entity-37/{entity_id}", response_model=HrSchemaEntity37Response)
def get_entity_37(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_37_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 37 not found")
    return res

@router.post("/entity-37", response_model=HrSchemaEntity37Response, status_code=201)
def create_entity_37(payload: HrSchemaEntity37Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_37(payload)

@router.get("/entity-38", response_model=List[HrSchemaEntity38Response])
def list_entities_38(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_38_list(skip=skip, limit=limit)

@router.get("/entity-38/{entity_id}", response_model=HrSchemaEntity38Response)
def get_entity_38(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_38_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 38 not found")
    return res

@router.post("/entity-38", response_model=HrSchemaEntity38Response, status_code=201)
def create_entity_38(payload: HrSchemaEntity38Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_38(payload)

@router.get("/entity-39", response_model=List[HrSchemaEntity39Response])
def list_entities_39(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_39_list(skip=skip, limit=limit)

@router.get("/entity-39/{entity_id}", response_model=HrSchemaEntity39Response)
def get_entity_39(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_39_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 39 not found")
    return res

@router.post("/entity-39", response_model=HrSchemaEntity39Response, status_code=201)
def create_entity_39(payload: HrSchemaEntity39Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_39(payload)

@router.get("/entity-40", response_model=List[HrSchemaEntity40Response])
def list_entities_40(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_40_list(skip=skip, limit=limit)

@router.get("/entity-40/{entity_id}", response_model=HrSchemaEntity40Response)
def get_entity_40(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_40_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 40 not found")
    return res

@router.post("/entity-40", response_model=HrSchemaEntity40Response, status_code=201)
def create_entity_40(payload: HrSchemaEntity40Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_40(payload)

@router.get("/entity-41", response_model=List[HrSchemaEntity41Response])
def list_entities_41(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_41_list(skip=skip, limit=limit)

@router.get("/entity-41/{entity_id}", response_model=HrSchemaEntity41Response)
def get_entity_41(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_41_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 41 not found")
    return res

@router.post("/entity-41", response_model=HrSchemaEntity41Response, status_code=201)
def create_entity_41(payload: HrSchemaEntity41Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_41(payload)

@router.get("/entity-42", response_model=List[HrSchemaEntity42Response])
def list_entities_42(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_42_list(skip=skip, limit=limit)

@router.get("/entity-42/{entity_id}", response_model=HrSchemaEntity42Response)
def get_entity_42(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_42_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 42 not found")
    return res

@router.post("/entity-42", response_model=HrSchemaEntity42Response, status_code=201)
def create_entity_42(payload: HrSchemaEntity42Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_42(payload)

@router.get("/entity-43", response_model=List[HrSchemaEntity43Response])
def list_entities_43(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_43_list(skip=skip, limit=limit)

@router.get("/entity-43/{entity_id}", response_model=HrSchemaEntity43Response)
def get_entity_43(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_43_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 43 not found")
    return res

@router.post("/entity-43", response_model=HrSchemaEntity43Response, status_code=201)
def create_entity_43(payload: HrSchemaEntity43Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_43(payload)

@router.get("/entity-44", response_model=List[HrSchemaEntity44Response])
def list_entities_44(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_44_list(skip=skip, limit=limit)

@router.get("/entity-44/{entity_id}", response_model=HrSchemaEntity44Response)
def get_entity_44(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_44_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 44 not found")
    return res

@router.post("/entity-44", response_model=HrSchemaEntity44Response, status_code=201)
def create_entity_44(payload: HrSchemaEntity44Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_44(payload)

@router.get("/entity-45", response_model=List[HrSchemaEntity45Response])
def list_entities_45(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_45_list(skip=skip, limit=limit)

@router.get("/entity-45/{entity_id}", response_model=HrSchemaEntity45Response)
def get_entity_45(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_45_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 45 not found")
    return res

@router.post("/entity-45", response_model=HrSchemaEntity45Response, status_code=201)
def create_entity_45(payload: HrSchemaEntity45Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_45(payload)

@router.get("/entity-46", response_model=List[HrSchemaEntity46Response])
def list_entities_46(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_46_list(skip=skip, limit=limit)

@router.get("/entity-46/{entity_id}", response_model=HrSchemaEntity46Response)
def get_entity_46(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_46_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 46 not found")
    return res

@router.post("/entity-46", response_model=HrSchemaEntity46Response, status_code=201)
def create_entity_46(payload: HrSchemaEntity46Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_46(payload)

@router.get("/entity-47", response_model=List[HrSchemaEntity47Response])
def list_entities_47(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_47_list(skip=skip, limit=limit)

@router.get("/entity-47/{entity_id}", response_model=HrSchemaEntity47Response)
def get_entity_47(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_47_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 47 not found")
    return res

@router.post("/entity-47", response_model=HrSchemaEntity47Response, status_code=201)
def create_entity_47(payload: HrSchemaEntity47Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_47(payload)

@router.get("/entity-48", response_model=List[HrSchemaEntity48Response])
def list_entities_48(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_48_list(skip=skip, limit=limit)

@router.get("/entity-48/{entity_id}", response_model=HrSchemaEntity48Response)
def get_entity_48(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_48_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 48 not found")
    return res

@router.post("/entity-48", response_model=HrSchemaEntity48Response, status_code=201)
def create_entity_48(payload: HrSchemaEntity48Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_48(payload)

@router.get("/entity-49", response_model=List[HrSchemaEntity49Response])
def list_entities_49(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_49_list(skip=skip, limit=limit)

@router.get("/entity-49/{entity_id}", response_model=HrSchemaEntity49Response)
def get_entity_49(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_49_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 49 not found")
    return res

@router.post("/entity-49", response_model=HrSchemaEntity49Response, status_code=201)
def create_entity_49(payload: HrSchemaEntity49Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_49(payload)

@router.get("/entity-50", response_model=List[HrSchemaEntity50Response])
def list_entities_50(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_50_list(skip=skip, limit=limit)

@router.get("/entity-50/{entity_id}", response_model=HrSchemaEntity50Response)
def get_entity_50(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_50_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 50 not found")
    return res

@router.post("/entity-50", response_model=HrSchemaEntity50Response, status_code=201)
def create_entity_50(payload: HrSchemaEntity50Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_50(payload)

@router.get("/entity-51", response_model=List[HrSchemaEntity51Response])
def list_entities_51(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_51_list(skip=skip, limit=limit)

@router.get("/entity-51/{entity_id}", response_model=HrSchemaEntity51Response)
def get_entity_51(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_51_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 51 not found")
    return res

@router.post("/entity-51", response_model=HrSchemaEntity51Response, status_code=201)
def create_entity_51(payload: HrSchemaEntity51Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_51(payload)

@router.get("/entity-52", response_model=List[HrSchemaEntity52Response])
def list_entities_52(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_52_list(skip=skip, limit=limit)

@router.get("/entity-52/{entity_id}", response_model=HrSchemaEntity52Response)
def get_entity_52(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_52_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 52 not found")
    return res

@router.post("/entity-52", response_model=HrSchemaEntity52Response, status_code=201)
def create_entity_52(payload: HrSchemaEntity52Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_52(payload)

@router.get("/entity-53", response_model=List[HrSchemaEntity53Response])
def list_entities_53(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_53_list(skip=skip, limit=limit)

@router.get("/entity-53/{entity_id}", response_model=HrSchemaEntity53Response)
def get_entity_53(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_53_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 53 not found")
    return res

@router.post("/entity-53", response_model=HrSchemaEntity53Response, status_code=201)
def create_entity_53(payload: HrSchemaEntity53Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_53(payload)

@router.get("/entity-54", response_model=List[HrSchemaEntity54Response])
def list_entities_54(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_54_list(skip=skip, limit=limit)

@router.get("/entity-54/{entity_id}", response_model=HrSchemaEntity54Response)
def get_entity_54(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_54_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 54 not found")
    return res

@router.post("/entity-54", response_model=HrSchemaEntity54Response, status_code=201)
def create_entity_54(payload: HrSchemaEntity54Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_54(payload)

@router.get("/entity-55", response_model=List[HrSchemaEntity55Response])
def list_entities_55(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_55_list(skip=skip, limit=limit)

@router.get("/entity-55/{entity_id}", response_model=HrSchemaEntity55Response)
def get_entity_55(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_55_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 55 not found")
    return res

@router.post("/entity-55", response_model=HrSchemaEntity55Response, status_code=201)
def create_entity_55(payload: HrSchemaEntity55Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_55(payload)

@router.get("/entity-56", response_model=List[HrSchemaEntity56Response])
def list_entities_56(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_56_list(skip=skip, limit=limit)

@router.get("/entity-56/{entity_id}", response_model=HrSchemaEntity56Response)
def get_entity_56(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_56_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 56 not found")
    return res

@router.post("/entity-56", response_model=HrSchemaEntity56Response, status_code=201)
def create_entity_56(payload: HrSchemaEntity56Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_56(payload)

@router.get("/entity-57", response_model=List[HrSchemaEntity57Response])
def list_entities_57(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_57_list(skip=skip, limit=limit)

@router.get("/entity-57/{entity_id}", response_model=HrSchemaEntity57Response)
def get_entity_57(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_57_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 57 not found")
    return res

@router.post("/entity-57", response_model=HrSchemaEntity57Response, status_code=201)
def create_entity_57(payload: HrSchemaEntity57Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_57(payload)

@router.get("/entity-58", response_model=List[HrSchemaEntity58Response])
def list_entities_58(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_58_list(skip=skip, limit=limit)

@router.get("/entity-58/{entity_id}", response_model=HrSchemaEntity58Response)
def get_entity_58(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_58_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 58 not found")
    return res

@router.post("/entity-58", response_model=HrSchemaEntity58Response, status_code=201)
def create_entity_58(payload: HrSchemaEntity58Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_58(payload)

@router.get("/entity-59", response_model=List[HrSchemaEntity59Response])
def list_entities_59(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_59_list(skip=skip, limit=limit)

@router.get("/entity-59/{entity_id}", response_model=HrSchemaEntity59Response)
def get_entity_59(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_59_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 59 not found")
    return res

@router.post("/entity-59", response_model=HrSchemaEntity59Response, status_code=201)
def create_entity_59(payload: HrSchemaEntity59Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_59(payload)

@router.get("/entity-60", response_model=List[HrSchemaEntity60Response])
def list_entities_60(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_60_list(skip=skip, limit=limit)

@router.get("/entity-60/{entity_id}", response_model=HrSchemaEntity60Response)
def get_entity_60(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_60_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 60 not found")
    return res

@router.post("/entity-60", response_model=HrSchemaEntity60Response, status_code=201)
def create_entity_60(payload: HrSchemaEntity60Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_60(payload)

@router.get("/entity-61", response_model=List[HrSchemaEntity61Response])
def list_entities_61(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_61_list(skip=skip, limit=limit)

@router.get("/entity-61/{entity_id}", response_model=HrSchemaEntity61Response)
def get_entity_61(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_61_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 61 not found")
    return res

@router.post("/entity-61", response_model=HrSchemaEntity61Response, status_code=201)
def create_entity_61(payload: HrSchemaEntity61Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_61(payload)

@router.get("/entity-62", response_model=List[HrSchemaEntity62Response])
def list_entities_62(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_62_list(skip=skip, limit=limit)

@router.get("/entity-62/{entity_id}", response_model=HrSchemaEntity62Response)
def get_entity_62(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_62_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 62 not found")
    return res

@router.post("/entity-62", response_model=HrSchemaEntity62Response, status_code=201)
def create_entity_62(payload: HrSchemaEntity62Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_62(payload)

@router.get("/entity-63", response_model=List[HrSchemaEntity63Response])
def list_entities_63(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_63_list(skip=skip, limit=limit)

@router.get("/entity-63/{entity_id}", response_model=HrSchemaEntity63Response)
def get_entity_63(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_63_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 63 not found")
    return res

@router.post("/entity-63", response_model=HrSchemaEntity63Response, status_code=201)
def create_entity_63(payload: HrSchemaEntity63Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_63(payload)

@router.get("/entity-64", response_model=List[HrSchemaEntity64Response])
def list_entities_64(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_64_list(skip=skip, limit=limit)

@router.get("/entity-64/{entity_id}", response_model=HrSchemaEntity64Response)
def get_entity_64(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_64_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 64 not found")
    return res

@router.post("/entity-64", response_model=HrSchemaEntity64Response, status_code=201)
def create_entity_64(payload: HrSchemaEntity64Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_64(payload)

@router.get("/entity-65", response_model=List[HrSchemaEntity65Response])
def list_entities_65(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_65_list(skip=skip, limit=limit)

@router.get("/entity-65/{entity_id}", response_model=HrSchemaEntity65Response)
def get_entity_65(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_65_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 65 not found")
    return res

@router.post("/entity-65", response_model=HrSchemaEntity65Response, status_code=201)
def create_entity_65(payload: HrSchemaEntity65Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_65(payload)

@router.get("/entity-66", response_model=List[HrSchemaEntity66Response])
def list_entities_66(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_66_list(skip=skip, limit=limit)

@router.get("/entity-66/{entity_id}", response_model=HrSchemaEntity66Response)
def get_entity_66(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_66_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 66 not found")
    return res

@router.post("/entity-66", response_model=HrSchemaEntity66Response, status_code=201)
def create_entity_66(payload: HrSchemaEntity66Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_66(payload)

@router.get("/entity-67", response_model=List[HrSchemaEntity67Response])
def list_entities_67(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_67_list(skip=skip, limit=limit)

@router.get("/entity-67/{entity_id}", response_model=HrSchemaEntity67Response)
def get_entity_67(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_67_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 67 not found")
    return res

@router.post("/entity-67", response_model=HrSchemaEntity67Response, status_code=201)
def create_entity_67(payload: HrSchemaEntity67Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_67(payload)

@router.get("/entity-68", response_model=List[HrSchemaEntity68Response])
def list_entities_68(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_68_list(skip=skip, limit=limit)

@router.get("/entity-68/{entity_id}", response_model=HrSchemaEntity68Response)
def get_entity_68(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_68_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 68 not found")
    return res

@router.post("/entity-68", response_model=HrSchemaEntity68Response, status_code=201)
def create_entity_68(payload: HrSchemaEntity68Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_68(payload)

@router.get("/entity-69", response_model=List[HrSchemaEntity69Response])
def list_entities_69(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_69_list(skip=skip, limit=limit)

@router.get("/entity-69/{entity_id}", response_model=HrSchemaEntity69Response)
def get_entity_69(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_69_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 69 not found")
    return res

@router.post("/entity-69", response_model=HrSchemaEntity69Response, status_code=201)
def create_entity_69(payload: HrSchemaEntity69Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_69(payload)

@router.get("/entity-70", response_model=List[HrSchemaEntity70Response])
def list_entities_70(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_70_list(skip=skip, limit=limit)

@router.get("/entity-70/{entity_id}", response_model=HrSchemaEntity70Response)
def get_entity_70(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_70_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 70 not found")
    return res

@router.post("/entity-70", response_model=HrSchemaEntity70Response, status_code=201)
def create_entity_70(payload: HrSchemaEntity70Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_70(payload)

@router.get("/entity-71", response_model=List[HrSchemaEntity71Response])
def list_entities_71(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_71_list(skip=skip, limit=limit)

@router.get("/entity-71/{entity_id}", response_model=HrSchemaEntity71Response)
def get_entity_71(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_71_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 71 not found")
    return res

@router.post("/entity-71", response_model=HrSchemaEntity71Response, status_code=201)
def create_entity_71(payload: HrSchemaEntity71Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_71(payload)

@router.get("/entity-72", response_model=List[HrSchemaEntity72Response])
def list_entities_72(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_72_list(skip=skip, limit=limit)

@router.get("/entity-72/{entity_id}", response_model=HrSchemaEntity72Response)
def get_entity_72(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_72_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 72 not found")
    return res

@router.post("/entity-72", response_model=HrSchemaEntity72Response, status_code=201)
def create_entity_72(payload: HrSchemaEntity72Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_72(payload)

@router.get("/entity-73", response_model=List[HrSchemaEntity73Response])
def list_entities_73(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_73_list(skip=skip, limit=limit)

@router.get("/entity-73/{entity_id}", response_model=HrSchemaEntity73Response)
def get_entity_73(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_73_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 73 not found")
    return res

@router.post("/entity-73", response_model=HrSchemaEntity73Response, status_code=201)
def create_entity_73(payload: HrSchemaEntity73Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_73(payload)

@router.get("/entity-74", response_model=List[HrSchemaEntity74Response])
def list_entities_74(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_74_list(skip=skip, limit=limit)

@router.get("/entity-74/{entity_id}", response_model=HrSchemaEntity74Response)
def get_entity_74(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_74_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 74 not found")
    return res

@router.post("/entity-74", response_model=HrSchemaEntity74Response, status_code=201)
def create_entity_74(payload: HrSchemaEntity74Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_74(payload)

@router.get("/entity-75", response_model=List[HrSchemaEntity75Response])
def list_entities_75(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_75_list(skip=skip, limit=limit)

@router.get("/entity-75/{entity_id}", response_model=HrSchemaEntity75Response)
def get_entity_75(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_75_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 75 not found")
    return res

@router.post("/entity-75", response_model=HrSchemaEntity75Response, status_code=201)
def create_entity_75(payload: HrSchemaEntity75Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_75(payload)

@router.get("/entity-76", response_model=List[HrSchemaEntity76Response])
def list_entities_76(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_76_list(skip=skip, limit=limit)

@router.get("/entity-76/{entity_id}", response_model=HrSchemaEntity76Response)
def get_entity_76(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_76_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 76 not found")
    return res

@router.post("/entity-76", response_model=HrSchemaEntity76Response, status_code=201)
def create_entity_76(payload: HrSchemaEntity76Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_76(payload)

@router.get("/entity-77", response_model=List[HrSchemaEntity77Response])
def list_entities_77(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_77_list(skip=skip, limit=limit)

@router.get("/entity-77/{entity_id}", response_model=HrSchemaEntity77Response)
def get_entity_77(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_77_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 77 not found")
    return res

@router.post("/entity-77", response_model=HrSchemaEntity77Response, status_code=201)
def create_entity_77(payload: HrSchemaEntity77Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_77(payload)

@router.get("/entity-78", response_model=List[HrSchemaEntity78Response])
def list_entities_78(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_78_list(skip=skip, limit=limit)

@router.get("/entity-78/{entity_id}", response_model=HrSchemaEntity78Response)
def get_entity_78(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_78_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 78 not found")
    return res

@router.post("/entity-78", response_model=HrSchemaEntity78Response, status_code=201)
def create_entity_78(payload: HrSchemaEntity78Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_78(payload)

@router.get("/entity-79", response_model=List[HrSchemaEntity79Response])
def list_entities_79(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_79_list(skip=skip, limit=limit)

@router.get("/entity-79/{entity_id}", response_model=HrSchemaEntity79Response)
def get_entity_79(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_79_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 79 not found")
    return res

@router.post("/entity-79", response_model=HrSchemaEntity79Response, status_code=201)
def create_entity_79(payload: HrSchemaEntity79Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_79(payload)

@router.get("/entity-80", response_model=List[HrSchemaEntity80Response])
def list_entities_80(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_80_list(skip=skip, limit=limit)

@router.get("/entity-80/{entity_id}", response_model=HrSchemaEntity80Response)
def get_entity_80(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_80_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 80 not found")
    return res

@router.post("/entity-80", response_model=HrSchemaEntity80Response, status_code=201)
def create_entity_80(payload: HrSchemaEntity80Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_80(payload)

@router.get("/entity-81", response_model=List[HrSchemaEntity81Response])
def list_entities_81(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_81_list(skip=skip, limit=limit)

@router.get("/entity-81/{entity_id}", response_model=HrSchemaEntity81Response)
def get_entity_81(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_81_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 81 not found")
    return res

@router.post("/entity-81", response_model=HrSchemaEntity81Response, status_code=201)
def create_entity_81(payload: HrSchemaEntity81Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_81(payload)

@router.get("/entity-82", response_model=List[HrSchemaEntity82Response])
def list_entities_82(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_82_list(skip=skip, limit=limit)

@router.get("/entity-82/{entity_id}", response_model=HrSchemaEntity82Response)
def get_entity_82(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_82_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 82 not found")
    return res

@router.post("/entity-82", response_model=HrSchemaEntity82Response, status_code=201)
def create_entity_82(payload: HrSchemaEntity82Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_82(payload)

@router.get("/entity-83", response_model=List[HrSchemaEntity83Response])
def list_entities_83(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_83_list(skip=skip, limit=limit)

@router.get("/entity-83/{entity_id}", response_model=HrSchemaEntity83Response)
def get_entity_83(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_83_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 83 not found")
    return res

@router.post("/entity-83", response_model=HrSchemaEntity83Response, status_code=201)
def create_entity_83(payload: HrSchemaEntity83Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_83(payload)

@router.get("/entity-84", response_model=List[HrSchemaEntity84Response])
def list_entities_84(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_84_list(skip=skip, limit=limit)

@router.get("/entity-84/{entity_id}", response_model=HrSchemaEntity84Response)
def get_entity_84(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_84_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 84 not found")
    return res

@router.post("/entity-84", response_model=HrSchemaEntity84Response, status_code=201)
def create_entity_84(payload: HrSchemaEntity84Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_84(payload)

@router.get("/entity-85", response_model=List[HrSchemaEntity85Response])
def list_entities_85(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_85_list(skip=skip, limit=limit)

@router.get("/entity-85/{entity_id}", response_model=HrSchemaEntity85Response)
def get_entity_85(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_85_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 85 not found")
    return res

@router.post("/entity-85", response_model=HrSchemaEntity85Response, status_code=201)
def create_entity_85(payload: HrSchemaEntity85Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_85(payload)

@router.get("/entity-86", response_model=List[HrSchemaEntity86Response])
def list_entities_86(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_86_list(skip=skip, limit=limit)

@router.get("/entity-86/{entity_id}", response_model=HrSchemaEntity86Response)
def get_entity_86(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_86_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 86 not found")
    return res

@router.post("/entity-86", response_model=HrSchemaEntity86Response, status_code=201)
def create_entity_86(payload: HrSchemaEntity86Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_86(payload)

@router.get("/entity-87", response_model=List[HrSchemaEntity87Response])
def list_entities_87(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_87_list(skip=skip, limit=limit)

@router.get("/entity-87/{entity_id}", response_model=HrSchemaEntity87Response)
def get_entity_87(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_87_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 87 not found")
    return res

@router.post("/entity-87", response_model=HrSchemaEntity87Response, status_code=201)
def create_entity_87(payload: HrSchemaEntity87Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_87(payload)

@router.get("/entity-88", response_model=List[HrSchemaEntity88Response])
def list_entities_88(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_88_list(skip=skip, limit=limit)

@router.get("/entity-88/{entity_id}", response_model=HrSchemaEntity88Response)
def get_entity_88(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_88_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 88 not found")
    return res

@router.post("/entity-88", response_model=HrSchemaEntity88Response, status_code=201)
def create_entity_88(payload: HrSchemaEntity88Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_88(payload)

@router.get("/entity-89", response_model=List[HrSchemaEntity89Response])
def list_entities_89(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_89_list(skip=skip, limit=limit)

@router.get("/entity-89/{entity_id}", response_model=HrSchemaEntity89Response)
def get_entity_89(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_89_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 89 not found")
    return res

@router.post("/entity-89", response_model=HrSchemaEntity89Response, status_code=201)
def create_entity_89(payload: HrSchemaEntity89Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_89(payload)

@router.get("/entity-90", response_model=List[HrSchemaEntity90Response])
def list_entities_90(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_90_list(skip=skip, limit=limit)

@router.get("/entity-90/{entity_id}", response_model=HrSchemaEntity90Response)
def get_entity_90(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_90_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 90 not found")
    return res

@router.post("/entity-90", response_model=HrSchemaEntity90Response, status_code=201)
def create_entity_90(payload: HrSchemaEntity90Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_90(payload)

@router.get("/entity-91", response_model=List[HrSchemaEntity91Response])
def list_entities_91(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_91_list(skip=skip, limit=limit)

@router.get("/entity-91/{entity_id}", response_model=HrSchemaEntity91Response)
def get_entity_91(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_91_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 91 not found")
    return res

@router.post("/entity-91", response_model=HrSchemaEntity91Response, status_code=201)
def create_entity_91(payload: HrSchemaEntity91Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_91(payload)

@router.get("/entity-92", response_model=List[HrSchemaEntity92Response])
def list_entities_92(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_92_list(skip=skip, limit=limit)

@router.get("/entity-92/{entity_id}", response_model=HrSchemaEntity92Response)
def get_entity_92(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_92_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 92 not found")
    return res

@router.post("/entity-92", response_model=HrSchemaEntity92Response, status_code=201)
def create_entity_92(payload: HrSchemaEntity92Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_92(payload)

@router.get("/entity-93", response_model=List[HrSchemaEntity93Response])
def list_entities_93(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_93_list(skip=skip, limit=limit)

@router.get("/entity-93/{entity_id}", response_model=HrSchemaEntity93Response)
def get_entity_93(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_93_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 93 not found")
    return res

@router.post("/entity-93", response_model=HrSchemaEntity93Response, status_code=201)
def create_entity_93(payload: HrSchemaEntity93Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_93(payload)

@router.get("/entity-94", response_model=List[HrSchemaEntity94Response])
def list_entities_94(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_94_list(skip=skip, limit=limit)

@router.get("/entity-94/{entity_id}", response_model=HrSchemaEntity94Response)
def get_entity_94(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_94_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 94 not found")
    return res

@router.post("/entity-94", response_model=HrSchemaEntity94Response, status_code=201)
def create_entity_94(payload: HrSchemaEntity94Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_94(payload)

@router.get("/entity-95", response_model=List[HrSchemaEntity95Response])
def list_entities_95(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_95_list(skip=skip, limit=limit)

@router.get("/entity-95/{entity_id}", response_model=HrSchemaEntity95Response)
def get_entity_95(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_95_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 95 not found")
    return res

@router.post("/entity-95", response_model=HrSchemaEntity95Response, status_code=201)
def create_entity_95(payload: HrSchemaEntity95Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_95(payload)

@router.get("/entity-96", response_model=List[HrSchemaEntity96Response])
def list_entities_96(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_96_list(skip=skip, limit=limit)

@router.get("/entity-96/{entity_id}", response_model=HrSchemaEntity96Response)
def get_entity_96(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_96_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 96 not found")
    return res

@router.post("/entity-96", response_model=HrSchemaEntity96Response, status_code=201)
def create_entity_96(payload: HrSchemaEntity96Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_96(payload)

@router.get("/entity-97", response_model=List[HrSchemaEntity97Response])
def list_entities_97(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_97_list(skip=skip, limit=limit)

@router.get("/entity-97/{entity_id}", response_model=HrSchemaEntity97Response)
def get_entity_97(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_97_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 97 not found")
    return res

@router.post("/entity-97", response_model=HrSchemaEntity97Response, status_code=201)
def create_entity_97(payload: HrSchemaEntity97Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_97(payload)

@router.get("/entity-98", response_model=List[HrSchemaEntity98Response])
def list_entities_98(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_98_list(skip=skip, limit=limit)

@router.get("/entity-98/{entity_id}", response_model=HrSchemaEntity98Response)
def get_entity_98(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_98_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 98 not found")
    return res

@router.post("/entity-98", response_model=HrSchemaEntity98Response, status_code=201)
def create_entity_98(payload: HrSchemaEntity98Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_98(payload)

@router.get("/entity-99", response_model=List[HrSchemaEntity99Response])
def list_entities_99(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_99_list(skip=skip, limit=limit)

@router.get("/entity-99/{entity_id}", response_model=HrSchemaEntity99Response)
def get_entity_99(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_99_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 99 not found")
    return res

@router.post("/entity-99", response_model=HrSchemaEntity99Response, status_code=201)
def create_entity_99(payload: HrSchemaEntity99Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_99(payload)

@router.get("/entity-100", response_model=List[HrSchemaEntity100Response])
def list_entities_100(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_100_list(skip=skip, limit=limit)

@router.get("/entity-100/{entity_id}", response_model=HrSchemaEntity100Response)
def get_entity_100(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_100_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 100 not found")
    return res

@router.post("/entity-100", response_model=HrSchemaEntity100Response, status_code=201)
def create_entity_100(payload: HrSchemaEntity100Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_100(payload)

@router.get("/entity-101", response_model=List[HrSchemaEntity101Response])
def list_entities_101(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_101_list(skip=skip, limit=limit)

@router.get("/entity-101/{entity_id}", response_model=HrSchemaEntity101Response)
def get_entity_101(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_101_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 101 not found")
    return res

@router.post("/entity-101", response_model=HrSchemaEntity101Response, status_code=201)
def create_entity_101(payload: HrSchemaEntity101Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_101(payload)

@router.get("/entity-102", response_model=List[HrSchemaEntity102Response])
def list_entities_102(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_102_list(skip=skip, limit=limit)

@router.get("/entity-102/{entity_id}", response_model=HrSchemaEntity102Response)
def get_entity_102(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_102_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 102 not found")
    return res

@router.post("/entity-102", response_model=HrSchemaEntity102Response, status_code=201)
def create_entity_102(payload: HrSchemaEntity102Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_102(payload)

@router.get("/entity-103", response_model=List[HrSchemaEntity103Response])
def list_entities_103(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_103_list(skip=skip, limit=limit)

@router.get("/entity-103/{entity_id}", response_model=HrSchemaEntity103Response)
def get_entity_103(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_103_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 103 not found")
    return res

@router.post("/entity-103", response_model=HrSchemaEntity103Response, status_code=201)
def create_entity_103(payload: HrSchemaEntity103Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_103(payload)

@router.get("/entity-104", response_model=List[HrSchemaEntity104Response])
def list_entities_104(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_104_list(skip=skip, limit=limit)

@router.get("/entity-104/{entity_id}", response_model=HrSchemaEntity104Response)
def get_entity_104(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_104_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 104 not found")
    return res

@router.post("/entity-104", response_model=HrSchemaEntity104Response, status_code=201)
def create_entity_104(payload: HrSchemaEntity104Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_104(payload)

@router.get("/entity-105", response_model=List[HrSchemaEntity105Response])
def list_entities_105(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_105_list(skip=skip, limit=limit)

@router.get("/entity-105/{entity_id}", response_model=HrSchemaEntity105Response)
def get_entity_105(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_105_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 105 not found")
    return res

@router.post("/entity-105", response_model=HrSchemaEntity105Response, status_code=201)
def create_entity_105(payload: HrSchemaEntity105Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_105(payload)

@router.get("/entity-106", response_model=List[HrSchemaEntity106Response])
def list_entities_106(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_106_list(skip=skip, limit=limit)

@router.get("/entity-106/{entity_id}", response_model=HrSchemaEntity106Response)
def get_entity_106(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_106_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 106 not found")
    return res

@router.post("/entity-106", response_model=HrSchemaEntity106Response, status_code=201)
def create_entity_106(payload: HrSchemaEntity106Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_106(payload)

@router.get("/entity-107", response_model=List[HrSchemaEntity107Response])
def list_entities_107(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_107_list(skip=skip, limit=limit)

@router.get("/entity-107/{entity_id}", response_model=HrSchemaEntity107Response)
def get_entity_107(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_107_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 107 not found")
    return res

@router.post("/entity-107", response_model=HrSchemaEntity107Response, status_code=201)
def create_entity_107(payload: HrSchemaEntity107Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_107(payload)

@router.get("/entity-108", response_model=List[HrSchemaEntity108Response])
def list_entities_108(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_108_list(skip=skip, limit=limit)

@router.get("/entity-108/{entity_id}", response_model=HrSchemaEntity108Response)
def get_entity_108(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_108_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 108 not found")
    return res

@router.post("/entity-108", response_model=HrSchemaEntity108Response, status_code=201)
def create_entity_108(payload: HrSchemaEntity108Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_108(payload)

@router.get("/entity-109", response_model=List[HrSchemaEntity109Response])
def list_entities_109(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_109_list(skip=skip, limit=limit)

@router.get("/entity-109/{entity_id}", response_model=HrSchemaEntity109Response)
def get_entity_109(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_109_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 109 not found")
    return res

@router.post("/entity-109", response_model=HrSchemaEntity109Response, status_code=201)
def create_entity_109(payload: HrSchemaEntity109Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_109(payload)

@router.get("/entity-110", response_model=List[HrSchemaEntity110Response])
def list_entities_110(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_110_list(skip=skip, limit=limit)

@router.get("/entity-110/{entity_id}", response_model=HrSchemaEntity110Response)
def get_entity_110(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_110_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 110 not found")
    return res

@router.post("/entity-110", response_model=HrSchemaEntity110Response, status_code=201)
def create_entity_110(payload: HrSchemaEntity110Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_110(payload)

@router.get("/entity-111", response_model=List[HrSchemaEntity111Response])
def list_entities_111(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_111_list(skip=skip, limit=limit)

@router.get("/entity-111/{entity_id}", response_model=HrSchemaEntity111Response)
def get_entity_111(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_111_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 111 not found")
    return res

@router.post("/entity-111", response_model=HrSchemaEntity111Response, status_code=201)
def create_entity_111(payload: HrSchemaEntity111Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_111(payload)

@router.get("/entity-112", response_model=List[HrSchemaEntity112Response])
def list_entities_112(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_112_list(skip=skip, limit=limit)

@router.get("/entity-112/{entity_id}", response_model=HrSchemaEntity112Response)
def get_entity_112(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_112_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 112 not found")
    return res

@router.post("/entity-112", response_model=HrSchemaEntity112Response, status_code=201)
def create_entity_112(payload: HrSchemaEntity112Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_112(payload)

@router.get("/entity-113", response_model=List[HrSchemaEntity113Response])
def list_entities_113(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_113_list(skip=skip, limit=limit)

@router.get("/entity-113/{entity_id}", response_model=HrSchemaEntity113Response)
def get_entity_113(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_113_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 113 not found")
    return res

@router.post("/entity-113", response_model=HrSchemaEntity113Response, status_code=201)
def create_entity_113(payload: HrSchemaEntity113Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_113(payload)

@router.get("/entity-114", response_model=List[HrSchemaEntity114Response])
def list_entities_114(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_114_list(skip=skip, limit=limit)

@router.get("/entity-114/{entity_id}", response_model=HrSchemaEntity114Response)
def get_entity_114(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_114_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 114 not found")
    return res

@router.post("/entity-114", response_model=HrSchemaEntity114Response, status_code=201)
def create_entity_114(payload: HrSchemaEntity114Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_114(payload)

@router.get("/entity-115", response_model=List[HrSchemaEntity115Response])
def list_entities_115(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_115_list(skip=skip, limit=limit)

@router.get("/entity-115/{entity_id}", response_model=HrSchemaEntity115Response)
def get_entity_115(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_115_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 115 not found")
    return res

@router.post("/entity-115", response_model=HrSchemaEntity115Response, status_code=201)
def create_entity_115(payload: HrSchemaEntity115Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_115(payload)

@router.get("/entity-116", response_model=List[HrSchemaEntity116Response])
def list_entities_116(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_116_list(skip=skip, limit=limit)

@router.get("/entity-116/{entity_id}", response_model=HrSchemaEntity116Response)
def get_entity_116(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_116_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 116 not found")
    return res

@router.post("/entity-116", response_model=HrSchemaEntity116Response, status_code=201)
def create_entity_116(payload: HrSchemaEntity116Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_116(payload)

@router.get("/entity-117", response_model=List[HrSchemaEntity117Response])
def list_entities_117(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_117_list(skip=skip, limit=limit)

@router.get("/entity-117/{entity_id}", response_model=HrSchemaEntity117Response)
def get_entity_117(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_117_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 117 not found")
    return res

@router.post("/entity-117", response_model=HrSchemaEntity117Response, status_code=201)
def create_entity_117(payload: HrSchemaEntity117Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_117(payload)

@router.get("/entity-118", response_model=List[HrSchemaEntity118Response])
def list_entities_118(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_118_list(skip=skip, limit=limit)

@router.get("/entity-118/{entity_id}", response_model=HrSchemaEntity118Response)
def get_entity_118(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_118_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 118 not found")
    return res

@router.post("/entity-118", response_model=HrSchemaEntity118Response, status_code=201)
def create_entity_118(payload: HrSchemaEntity118Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_118(payload)

@router.get("/entity-119", response_model=List[HrSchemaEntity119Response])
def list_entities_119(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_119_list(skip=skip, limit=limit)

@router.get("/entity-119/{entity_id}", response_model=HrSchemaEntity119Response)
def get_entity_119(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_119_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 119 not found")
    return res

@router.post("/entity-119", response_model=HrSchemaEntity119Response, status_code=201)
def create_entity_119(payload: HrSchemaEntity119Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_119(payload)

@router.get("/entity-120", response_model=List[HrSchemaEntity120Response])
def list_entities_120(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_120_list(skip=skip, limit=limit)

@router.get("/entity-120/{entity_id}", response_model=HrSchemaEntity120Response)
def get_entity_120(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_120_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 120 not found")
    return res

@router.post("/entity-120", response_model=HrSchemaEntity120Response, status_code=201)
def create_entity_120(payload: HrSchemaEntity120Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_120(payload)

@router.get("/entity-121", response_model=List[HrSchemaEntity121Response])
def list_entities_121(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_121_list(skip=skip, limit=limit)

@router.get("/entity-121/{entity_id}", response_model=HrSchemaEntity121Response)
def get_entity_121(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_121_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 121 not found")
    return res

@router.post("/entity-121", response_model=HrSchemaEntity121Response, status_code=201)
def create_entity_121(payload: HrSchemaEntity121Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_121(payload)

@router.get("/entity-122", response_model=List[HrSchemaEntity122Response])
def list_entities_122(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_122_list(skip=skip, limit=limit)

@router.get("/entity-122/{entity_id}", response_model=HrSchemaEntity122Response)
def get_entity_122(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_122_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 122 not found")
    return res

@router.post("/entity-122", response_model=HrSchemaEntity122Response, status_code=201)
def create_entity_122(payload: HrSchemaEntity122Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_122(payload)

@router.get("/entity-123", response_model=List[HrSchemaEntity123Response])
def list_entities_123(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_123_list(skip=skip, limit=limit)

@router.get("/entity-123/{entity_id}", response_model=HrSchemaEntity123Response)
def get_entity_123(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_123_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 123 not found")
    return res

@router.post("/entity-123", response_model=HrSchemaEntity123Response, status_code=201)
def create_entity_123(payload: HrSchemaEntity123Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_123(payload)

@router.get("/entity-124", response_model=List[HrSchemaEntity124Response])
def list_entities_124(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_124_list(skip=skip, limit=limit)

@router.get("/entity-124/{entity_id}", response_model=HrSchemaEntity124Response)
def get_entity_124(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_124_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 124 not found")
    return res

@router.post("/entity-124", response_model=HrSchemaEntity124Response, status_code=201)
def create_entity_124(payload: HrSchemaEntity124Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_124(payload)

@router.get("/entity-125", response_model=List[HrSchemaEntity125Response])
def list_entities_125(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_125_list(skip=skip, limit=limit)

@router.get("/entity-125/{entity_id}", response_model=HrSchemaEntity125Response)
def get_entity_125(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_125_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 125 not found")
    return res

@router.post("/entity-125", response_model=HrSchemaEntity125Response, status_code=201)
def create_entity_125(payload: HrSchemaEntity125Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_125(payload)

@router.get("/entity-126", response_model=List[HrSchemaEntity126Response])
def list_entities_126(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_126_list(skip=skip, limit=limit)

@router.get("/entity-126/{entity_id}", response_model=HrSchemaEntity126Response)
def get_entity_126(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_126_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 126 not found")
    return res

@router.post("/entity-126", response_model=HrSchemaEntity126Response, status_code=201)
def create_entity_126(payload: HrSchemaEntity126Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_126(payload)

@router.get("/entity-127", response_model=List[HrSchemaEntity127Response])
def list_entities_127(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_127_list(skip=skip, limit=limit)

@router.get("/entity-127/{entity_id}", response_model=HrSchemaEntity127Response)
def get_entity_127(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_127_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 127 not found")
    return res

@router.post("/entity-127", response_model=HrSchemaEntity127Response, status_code=201)
def create_entity_127(payload: HrSchemaEntity127Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_127(payload)

@router.get("/entity-128", response_model=List[HrSchemaEntity128Response])
def list_entities_128(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_128_list(skip=skip, limit=limit)

@router.get("/entity-128/{entity_id}", response_model=HrSchemaEntity128Response)
def get_entity_128(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_128_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 128 not found")
    return res

@router.post("/entity-128", response_model=HrSchemaEntity128Response, status_code=201)
def create_entity_128(payload: HrSchemaEntity128Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_128(payload)

@router.get("/entity-129", response_model=List[HrSchemaEntity129Response])
def list_entities_129(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_129_list(skip=skip, limit=limit)

@router.get("/entity-129/{entity_id}", response_model=HrSchemaEntity129Response)
def get_entity_129(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_129_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 129 not found")
    return res

@router.post("/entity-129", response_model=HrSchemaEntity129Response, status_code=201)
def create_entity_129(payload: HrSchemaEntity129Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_129(payload)

@router.get("/entity-130", response_model=List[HrSchemaEntity130Response])
def list_entities_130(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_130_list(skip=skip, limit=limit)

@router.get("/entity-130/{entity_id}", response_model=HrSchemaEntity130Response)
def get_entity_130(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_130_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 130 not found")
    return res

@router.post("/entity-130", response_model=HrSchemaEntity130Response, status_code=201)
def create_entity_130(payload: HrSchemaEntity130Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_130(payload)

@router.get("/entity-131", response_model=List[HrSchemaEntity131Response])
def list_entities_131(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_131_list(skip=skip, limit=limit)

@router.get("/entity-131/{entity_id}", response_model=HrSchemaEntity131Response)
def get_entity_131(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_131_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 131 not found")
    return res

@router.post("/entity-131", response_model=HrSchemaEntity131Response, status_code=201)
def create_entity_131(payload: HrSchemaEntity131Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_131(payload)

@router.get("/entity-132", response_model=List[HrSchemaEntity132Response])
def list_entities_132(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_132_list(skip=skip, limit=limit)

@router.get("/entity-132/{entity_id}", response_model=HrSchemaEntity132Response)
def get_entity_132(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_132_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 132 not found")
    return res

@router.post("/entity-132", response_model=HrSchemaEntity132Response, status_code=201)
def create_entity_132(payload: HrSchemaEntity132Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_132(payload)

@router.get("/entity-133", response_model=List[HrSchemaEntity133Response])
def list_entities_133(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_133_list(skip=skip, limit=limit)

@router.get("/entity-133/{entity_id}", response_model=HrSchemaEntity133Response)
def get_entity_133(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_133_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 133 not found")
    return res

@router.post("/entity-133", response_model=HrSchemaEntity133Response, status_code=201)
def create_entity_133(payload: HrSchemaEntity133Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_133(payload)

@router.get("/entity-134", response_model=List[HrSchemaEntity134Response])
def list_entities_134(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_134_list(skip=skip, limit=limit)

@router.get("/entity-134/{entity_id}", response_model=HrSchemaEntity134Response)
def get_entity_134(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_134_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 134 not found")
    return res

@router.post("/entity-134", response_model=HrSchemaEntity134Response, status_code=201)
def create_entity_134(payload: HrSchemaEntity134Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_134(payload)

@router.get("/entity-135", response_model=List[HrSchemaEntity135Response])
def list_entities_135(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_135_list(skip=skip, limit=limit)

@router.get("/entity-135/{entity_id}", response_model=HrSchemaEntity135Response)
def get_entity_135(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_135_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 135 not found")
    return res

@router.post("/entity-135", response_model=HrSchemaEntity135Response, status_code=201)
def create_entity_135(payload: HrSchemaEntity135Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_135(payload)

@router.get("/entity-136", response_model=List[HrSchemaEntity136Response])
def list_entities_136(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_136_list(skip=skip, limit=limit)

@router.get("/entity-136/{entity_id}", response_model=HrSchemaEntity136Response)
def get_entity_136(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_136_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 136 not found")
    return res

@router.post("/entity-136", response_model=HrSchemaEntity136Response, status_code=201)
def create_entity_136(payload: HrSchemaEntity136Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_136(payload)

@router.get("/entity-137", response_model=List[HrSchemaEntity137Response])
def list_entities_137(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_137_list(skip=skip, limit=limit)

@router.get("/entity-137/{entity_id}", response_model=HrSchemaEntity137Response)
def get_entity_137(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_137_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 137 not found")
    return res

@router.post("/entity-137", response_model=HrSchemaEntity137Response, status_code=201)
def create_entity_137(payload: HrSchemaEntity137Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_137(payload)

@router.get("/entity-138", response_model=List[HrSchemaEntity138Response])
def list_entities_138(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_138_list(skip=skip, limit=limit)

@router.get("/entity-138/{entity_id}", response_model=HrSchemaEntity138Response)
def get_entity_138(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_138_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 138 not found")
    return res

@router.post("/entity-138", response_model=HrSchemaEntity138Response, status_code=201)
def create_entity_138(payload: HrSchemaEntity138Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_138(payload)

@router.get("/entity-139", response_model=List[HrSchemaEntity139Response])
def list_entities_139(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_139_list(skip=skip, limit=limit)

@router.get("/entity-139/{entity_id}", response_model=HrSchemaEntity139Response)
def get_entity_139(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_139_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 139 not found")
    return res

@router.post("/entity-139", response_model=HrSchemaEntity139Response, status_code=201)
def create_entity_139(payload: HrSchemaEntity139Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_139(payload)

@router.get("/entity-140", response_model=List[HrSchemaEntity140Response])
def list_entities_140(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_140_list(skip=skip, limit=limit)

@router.get("/entity-140/{entity_id}", response_model=HrSchemaEntity140Response)
def get_entity_140(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_140_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 140 not found")
    return res

@router.post("/entity-140", response_model=HrSchemaEntity140Response, status_code=201)
def create_entity_140(payload: HrSchemaEntity140Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_140(payload)

@router.get("/entity-141", response_model=List[HrSchemaEntity141Response])
def list_entities_141(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_141_list(skip=skip, limit=limit)

@router.get("/entity-141/{entity_id}", response_model=HrSchemaEntity141Response)
def get_entity_141(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_141_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 141 not found")
    return res

@router.post("/entity-141", response_model=HrSchemaEntity141Response, status_code=201)
def create_entity_141(payload: HrSchemaEntity141Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_141(payload)

@router.get("/entity-142", response_model=List[HrSchemaEntity142Response])
def list_entities_142(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_142_list(skip=skip, limit=limit)

@router.get("/entity-142/{entity_id}", response_model=HrSchemaEntity142Response)
def get_entity_142(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_142_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 142 not found")
    return res

@router.post("/entity-142", response_model=HrSchemaEntity142Response, status_code=201)
def create_entity_142(payload: HrSchemaEntity142Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_142(payload)

@router.get("/entity-143", response_model=List[HrSchemaEntity143Response])
def list_entities_143(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_143_list(skip=skip, limit=limit)

@router.get("/entity-143/{entity_id}", response_model=HrSchemaEntity143Response)
def get_entity_143(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_143_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 143 not found")
    return res

@router.post("/entity-143", response_model=HrSchemaEntity143Response, status_code=201)
def create_entity_143(payload: HrSchemaEntity143Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_143(payload)

@router.get("/entity-144", response_model=List[HrSchemaEntity144Response])
def list_entities_144(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_144_list(skip=skip, limit=limit)

@router.get("/entity-144/{entity_id}", response_model=HrSchemaEntity144Response)
def get_entity_144(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_144_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 144 not found")
    return res

@router.post("/entity-144", response_model=HrSchemaEntity144Response, status_code=201)
def create_entity_144(payload: HrSchemaEntity144Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_144(payload)

@router.get("/entity-145", response_model=List[HrSchemaEntity145Response])
def list_entities_145(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_145_list(skip=skip, limit=limit)

@router.get("/entity-145/{entity_id}", response_model=HrSchemaEntity145Response)
def get_entity_145(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_145_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 145 not found")
    return res

@router.post("/entity-145", response_model=HrSchemaEntity145Response, status_code=201)
def create_entity_145(payload: HrSchemaEntity145Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_145(payload)

@router.get("/entity-146", response_model=List[HrSchemaEntity146Response])
def list_entities_146(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_146_list(skip=skip, limit=limit)

@router.get("/entity-146/{entity_id}", response_model=HrSchemaEntity146Response)
def get_entity_146(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_146_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 146 not found")
    return res

@router.post("/entity-146", response_model=HrSchemaEntity146Response, status_code=201)
def create_entity_146(payload: HrSchemaEntity146Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_146(payload)

@router.get("/entity-147", response_model=List[HrSchemaEntity147Response])
def list_entities_147(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_147_list(skip=skip, limit=limit)

@router.get("/entity-147/{entity_id}", response_model=HrSchemaEntity147Response)
def get_entity_147(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_147_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 147 not found")
    return res

@router.post("/entity-147", response_model=HrSchemaEntity147Response, status_code=201)
def create_entity_147(payload: HrSchemaEntity147Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_147(payload)

@router.get("/entity-148", response_model=List[HrSchemaEntity148Response])
def list_entities_148(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_148_list(skip=skip, limit=limit)

@router.get("/entity-148/{entity_id}", response_model=HrSchemaEntity148Response)
def get_entity_148(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_148_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 148 not found")
    return res

@router.post("/entity-148", response_model=HrSchemaEntity148Response, status_code=201)
def create_entity_148(payload: HrSchemaEntity148Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_148(payload)

@router.get("/entity-149", response_model=List[HrSchemaEntity149Response])
def list_entities_149(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_149_list(skip=skip, limit=limit)

@router.get("/entity-149/{entity_id}", response_model=HrSchemaEntity149Response)
def get_entity_149(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_149_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 149 not found")
    return res

@router.post("/entity-149", response_model=HrSchemaEntity149Response, status_code=201)
def create_entity_149(payload: HrSchemaEntity149Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_149(payload)

@router.get("/entity-150", response_model=List[HrSchemaEntity150Response])
def list_entities_150(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_150_list(skip=skip, limit=limit)

@router.get("/entity-150/{entity_id}", response_model=HrSchemaEntity150Response)
def get_entity_150(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_150_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 150 not found")
    return res

@router.post("/entity-150", response_model=HrSchemaEntity150Response, status_code=201)
def create_entity_150(payload: HrSchemaEntity150Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_150(payload)

@router.get("/entity-151", response_model=List[HrSchemaEntity151Response])
def list_entities_151(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_151_list(skip=skip, limit=limit)

@router.get("/entity-151/{entity_id}", response_model=HrSchemaEntity151Response)
def get_entity_151(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_151_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 151 not found")
    return res

@router.post("/entity-151", response_model=HrSchemaEntity151Response, status_code=201)
def create_entity_151(payload: HrSchemaEntity151Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_151(payload)

@router.get("/entity-152", response_model=List[HrSchemaEntity152Response])
def list_entities_152(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_152_list(skip=skip, limit=limit)

@router.get("/entity-152/{entity_id}", response_model=HrSchemaEntity152Response)
def get_entity_152(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_152_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 152 not found")
    return res

@router.post("/entity-152", response_model=HrSchemaEntity152Response, status_code=201)
def create_entity_152(payload: HrSchemaEntity152Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_152(payload)

@router.get("/entity-153", response_model=List[HrSchemaEntity153Response])
def list_entities_153(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_153_list(skip=skip, limit=limit)

@router.get("/entity-153/{entity_id}", response_model=HrSchemaEntity153Response)
def get_entity_153(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_153_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 153 not found")
    return res

@router.post("/entity-153", response_model=HrSchemaEntity153Response, status_code=201)
def create_entity_153(payload: HrSchemaEntity153Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_153(payload)

@router.get("/entity-154", response_model=List[HrSchemaEntity154Response])
def list_entities_154(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_154_list(skip=skip, limit=limit)

@router.get("/entity-154/{entity_id}", response_model=HrSchemaEntity154Response)
def get_entity_154(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_154_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 154 not found")
    return res

@router.post("/entity-154", response_model=HrSchemaEntity154Response, status_code=201)
def create_entity_154(payload: HrSchemaEntity154Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_154(payload)

@router.get("/entity-155", response_model=List[HrSchemaEntity155Response])
def list_entities_155(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_155_list(skip=skip, limit=limit)

@router.get("/entity-155/{entity_id}", response_model=HrSchemaEntity155Response)
def get_entity_155(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_155_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 155 not found")
    return res

@router.post("/entity-155", response_model=HrSchemaEntity155Response, status_code=201)
def create_entity_155(payload: HrSchemaEntity155Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_155(payload)

@router.get("/entity-156", response_model=List[HrSchemaEntity156Response])
def list_entities_156(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_156_list(skip=skip, limit=limit)

@router.get("/entity-156/{entity_id}", response_model=HrSchemaEntity156Response)
def get_entity_156(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_156_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 156 not found")
    return res

@router.post("/entity-156", response_model=HrSchemaEntity156Response, status_code=201)
def create_entity_156(payload: HrSchemaEntity156Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_156(payload)

@router.get("/entity-157", response_model=List[HrSchemaEntity157Response])
def list_entities_157(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_157_list(skip=skip, limit=limit)

@router.get("/entity-157/{entity_id}", response_model=HrSchemaEntity157Response)
def get_entity_157(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_157_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 157 not found")
    return res

@router.post("/entity-157", response_model=HrSchemaEntity157Response, status_code=201)
def create_entity_157(payload: HrSchemaEntity157Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_157(payload)

@router.get("/entity-158", response_model=List[HrSchemaEntity158Response])
def list_entities_158(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_158_list(skip=skip, limit=limit)

@router.get("/entity-158/{entity_id}", response_model=HrSchemaEntity158Response)
def get_entity_158(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_158_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 158 not found")
    return res

@router.post("/entity-158", response_model=HrSchemaEntity158Response, status_code=201)
def create_entity_158(payload: HrSchemaEntity158Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_158(payload)

@router.get("/entity-159", response_model=List[HrSchemaEntity159Response])
def list_entities_159(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_159_list(skip=skip, limit=limit)

@router.get("/entity-159/{entity_id}", response_model=HrSchemaEntity159Response)
def get_entity_159(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_159_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 159 not found")
    return res

@router.post("/entity-159", response_model=HrSchemaEntity159Response, status_code=201)
def create_entity_159(payload: HrSchemaEntity159Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_159(payload)

@router.get("/entity-160", response_model=List[HrSchemaEntity160Response])
def list_entities_160(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_160_list(skip=skip, limit=limit)

@router.get("/entity-160/{entity_id}", response_model=HrSchemaEntity160Response)
def get_entity_160(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_160_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 160 not found")
    return res

@router.post("/entity-160", response_model=HrSchemaEntity160Response, status_code=201)
def create_entity_160(payload: HrSchemaEntity160Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_160(payload)

@router.get("/entity-161", response_model=List[HrSchemaEntity161Response])
def list_entities_161(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_161_list(skip=skip, limit=limit)

@router.get("/entity-161/{entity_id}", response_model=HrSchemaEntity161Response)
def get_entity_161(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_161_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 161 not found")
    return res

@router.post("/entity-161", response_model=HrSchemaEntity161Response, status_code=201)
def create_entity_161(payload: HrSchemaEntity161Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_161(payload)

@router.get("/entity-162", response_model=List[HrSchemaEntity162Response])
def list_entities_162(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_162_list(skip=skip, limit=limit)

@router.get("/entity-162/{entity_id}", response_model=HrSchemaEntity162Response)
def get_entity_162(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_162_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 162 not found")
    return res

@router.post("/entity-162", response_model=HrSchemaEntity162Response, status_code=201)
def create_entity_162(payload: HrSchemaEntity162Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_162(payload)

@router.get("/entity-163", response_model=List[HrSchemaEntity163Response])
def list_entities_163(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_163_list(skip=skip, limit=limit)

@router.get("/entity-163/{entity_id}", response_model=HrSchemaEntity163Response)
def get_entity_163(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_163_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 163 not found")
    return res

@router.post("/entity-163", response_model=HrSchemaEntity163Response, status_code=201)
def create_entity_163(payload: HrSchemaEntity163Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_163(payload)

@router.get("/entity-164", response_model=List[HrSchemaEntity164Response])
def list_entities_164(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_164_list(skip=skip, limit=limit)

@router.get("/entity-164/{entity_id}", response_model=HrSchemaEntity164Response)
def get_entity_164(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_164_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 164 not found")
    return res

@router.post("/entity-164", response_model=HrSchemaEntity164Response, status_code=201)
def create_entity_164(payload: HrSchemaEntity164Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_164(payload)

@router.get("/entity-165", response_model=List[HrSchemaEntity165Response])
def list_entities_165(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_165_list(skip=skip, limit=limit)

@router.get("/entity-165/{entity_id}", response_model=HrSchemaEntity165Response)
def get_entity_165(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_165_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 165 not found")
    return res

@router.post("/entity-165", response_model=HrSchemaEntity165Response, status_code=201)
def create_entity_165(payload: HrSchemaEntity165Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_165(payload)

@router.get("/entity-166", response_model=List[HrSchemaEntity166Response])
def list_entities_166(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_166_list(skip=skip, limit=limit)

@router.get("/entity-166/{entity_id}", response_model=HrSchemaEntity166Response)
def get_entity_166(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_166_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 166 not found")
    return res

@router.post("/entity-166", response_model=HrSchemaEntity166Response, status_code=201)
def create_entity_166(payload: HrSchemaEntity166Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_166(payload)

@router.get("/entity-167", response_model=List[HrSchemaEntity167Response])
def list_entities_167(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_167_list(skip=skip, limit=limit)

@router.get("/entity-167/{entity_id}", response_model=HrSchemaEntity167Response)
def get_entity_167(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_167_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 167 not found")
    return res

@router.post("/entity-167", response_model=HrSchemaEntity167Response, status_code=201)
def create_entity_167(payload: HrSchemaEntity167Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_167(payload)

@router.get("/entity-168", response_model=List[HrSchemaEntity168Response])
def list_entities_168(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_168_list(skip=skip, limit=limit)

@router.get("/entity-168/{entity_id}", response_model=HrSchemaEntity168Response)
def get_entity_168(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_168_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 168 not found")
    return res

@router.post("/entity-168", response_model=HrSchemaEntity168Response, status_code=201)
def create_entity_168(payload: HrSchemaEntity168Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_168(payload)

@router.get("/entity-169", response_model=List[HrSchemaEntity169Response])
def list_entities_169(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_169_list(skip=skip, limit=limit)

@router.get("/entity-169/{entity_id}", response_model=HrSchemaEntity169Response)
def get_entity_169(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_169_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 169 not found")
    return res

@router.post("/entity-169", response_model=HrSchemaEntity169Response, status_code=201)
def create_entity_169(payload: HrSchemaEntity169Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_169(payload)

@router.get("/entity-170", response_model=List[HrSchemaEntity170Response])
def list_entities_170(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_170_list(skip=skip, limit=limit)

@router.get("/entity-170/{entity_id}", response_model=HrSchemaEntity170Response)
def get_entity_170(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_170_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 170 not found")
    return res

@router.post("/entity-170", response_model=HrSchemaEntity170Response, status_code=201)
def create_entity_170(payload: HrSchemaEntity170Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_170(payload)

@router.get("/entity-171", response_model=List[HrSchemaEntity171Response])
def list_entities_171(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_171_list(skip=skip, limit=limit)

@router.get("/entity-171/{entity_id}", response_model=HrSchemaEntity171Response)
def get_entity_171(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_171_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 171 not found")
    return res

@router.post("/entity-171", response_model=HrSchemaEntity171Response, status_code=201)
def create_entity_171(payload: HrSchemaEntity171Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_171(payload)

@router.get("/entity-172", response_model=List[HrSchemaEntity172Response])
def list_entities_172(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_172_list(skip=skip, limit=limit)

@router.get("/entity-172/{entity_id}", response_model=HrSchemaEntity172Response)
def get_entity_172(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_172_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 172 not found")
    return res

@router.post("/entity-172", response_model=HrSchemaEntity172Response, status_code=201)
def create_entity_172(payload: HrSchemaEntity172Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_172(payload)

@router.get("/entity-173", response_model=List[HrSchemaEntity173Response])
def list_entities_173(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_173_list(skip=skip, limit=limit)

@router.get("/entity-173/{entity_id}", response_model=HrSchemaEntity173Response)
def get_entity_173(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_173_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 173 not found")
    return res

@router.post("/entity-173", response_model=HrSchemaEntity173Response, status_code=201)
def create_entity_173(payload: HrSchemaEntity173Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_173(payload)

@router.get("/entity-174", response_model=List[HrSchemaEntity174Response])
def list_entities_174(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_174_list(skip=skip, limit=limit)

@router.get("/entity-174/{entity_id}", response_model=HrSchemaEntity174Response)
def get_entity_174(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_174_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 174 not found")
    return res

@router.post("/entity-174", response_model=HrSchemaEntity174Response, status_code=201)
def create_entity_174(payload: HrSchemaEntity174Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_174(payload)

@router.get("/entity-175", response_model=List[HrSchemaEntity175Response])
def list_entities_175(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_175_list(skip=skip, limit=limit)

@router.get("/entity-175/{entity_id}", response_model=HrSchemaEntity175Response)
def get_entity_175(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_175_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 175 not found")
    return res

@router.post("/entity-175", response_model=HrSchemaEntity175Response, status_code=201)
def create_entity_175(payload: HrSchemaEntity175Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_175(payload)

@router.get("/entity-176", response_model=List[HrSchemaEntity176Response])
def list_entities_176(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_176_list(skip=skip, limit=limit)

@router.get("/entity-176/{entity_id}", response_model=HrSchemaEntity176Response)
def get_entity_176(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_176_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 176 not found")
    return res

@router.post("/entity-176", response_model=HrSchemaEntity176Response, status_code=201)
def create_entity_176(payload: HrSchemaEntity176Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_176(payload)

@router.get("/entity-177", response_model=List[HrSchemaEntity177Response])
def list_entities_177(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_177_list(skip=skip, limit=limit)

@router.get("/entity-177/{entity_id}", response_model=HrSchemaEntity177Response)
def get_entity_177(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_177_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 177 not found")
    return res

@router.post("/entity-177", response_model=HrSchemaEntity177Response, status_code=201)
def create_entity_177(payload: HrSchemaEntity177Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_177(payload)

@router.get("/entity-178", response_model=List[HrSchemaEntity178Response])
def list_entities_178(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_178_list(skip=skip, limit=limit)

@router.get("/entity-178/{entity_id}", response_model=HrSchemaEntity178Response)
def get_entity_178(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_178_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 178 not found")
    return res

@router.post("/entity-178", response_model=HrSchemaEntity178Response, status_code=201)
def create_entity_178(payload: HrSchemaEntity178Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_178(payload)

@router.get("/entity-179", response_model=List[HrSchemaEntity179Response])
def list_entities_179(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_179_list(skip=skip, limit=limit)

@router.get("/entity-179/{entity_id}", response_model=HrSchemaEntity179Response)
def get_entity_179(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_179_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 179 not found")
    return res

@router.post("/entity-179", response_model=HrSchemaEntity179Response, status_code=201)
def create_entity_179(payload: HrSchemaEntity179Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_179(payload)

@router.get("/entity-180", response_model=List[HrSchemaEntity180Response])
def list_entities_180(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_180_list(skip=skip, limit=limit)

@router.get("/entity-180/{entity_id}", response_model=HrSchemaEntity180Response)
def get_entity_180(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_180_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 180 not found")
    return res

@router.post("/entity-180", response_model=HrSchemaEntity180Response, status_code=201)
def create_entity_180(payload: HrSchemaEntity180Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_180(payload)

@router.get("/entity-181", response_model=List[HrSchemaEntity181Response])
def list_entities_181(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_181_list(skip=skip, limit=limit)

@router.get("/entity-181/{entity_id}", response_model=HrSchemaEntity181Response)
def get_entity_181(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_181_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 181 not found")
    return res

@router.post("/entity-181", response_model=HrSchemaEntity181Response, status_code=201)
def create_entity_181(payload: HrSchemaEntity181Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_181(payload)

@router.get("/entity-182", response_model=List[HrSchemaEntity182Response])
def list_entities_182(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_182_list(skip=skip, limit=limit)

@router.get("/entity-182/{entity_id}", response_model=HrSchemaEntity182Response)
def get_entity_182(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_182_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 182 not found")
    return res

@router.post("/entity-182", response_model=HrSchemaEntity182Response, status_code=201)
def create_entity_182(payload: HrSchemaEntity182Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_182(payload)

@router.get("/entity-183", response_model=List[HrSchemaEntity183Response])
def list_entities_183(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_183_list(skip=skip, limit=limit)

@router.get("/entity-183/{entity_id}", response_model=HrSchemaEntity183Response)
def get_entity_183(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_183_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 183 not found")
    return res

@router.post("/entity-183", response_model=HrSchemaEntity183Response, status_code=201)
def create_entity_183(payload: HrSchemaEntity183Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_183(payload)

@router.get("/entity-184", response_model=List[HrSchemaEntity184Response])
def list_entities_184(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_184_list(skip=skip, limit=limit)

@router.get("/entity-184/{entity_id}", response_model=HrSchemaEntity184Response)
def get_entity_184(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_184_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 184 not found")
    return res

@router.post("/entity-184", response_model=HrSchemaEntity184Response, status_code=201)
def create_entity_184(payload: HrSchemaEntity184Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_184(payload)

@router.get("/entity-185", response_model=List[HrSchemaEntity185Response])
def list_entities_185(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_185_list(skip=skip, limit=limit)

@router.get("/entity-185/{entity_id}", response_model=HrSchemaEntity185Response)
def get_entity_185(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_185_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 185 not found")
    return res

@router.post("/entity-185", response_model=HrSchemaEntity185Response, status_code=201)
def create_entity_185(payload: HrSchemaEntity185Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_185(payload)

@router.get("/entity-186", response_model=List[HrSchemaEntity186Response])
def list_entities_186(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_186_list(skip=skip, limit=limit)

@router.get("/entity-186/{entity_id}", response_model=HrSchemaEntity186Response)
def get_entity_186(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_186_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 186 not found")
    return res

@router.post("/entity-186", response_model=HrSchemaEntity186Response, status_code=201)
def create_entity_186(payload: HrSchemaEntity186Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_186(payload)

@router.get("/entity-187", response_model=List[HrSchemaEntity187Response])
def list_entities_187(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_187_list(skip=skip, limit=limit)

@router.get("/entity-187/{entity_id}", response_model=HrSchemaEntity187Response)
def get_entity_187(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_187_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 187 not found")
    return res

@router.post("/entity-187", response_model=HrSchemaEntity187Response, status_code=201)
def create_entity_187(payload: HrSchemaEntity187Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_187(payload)

@router.get("/entity-188", response_model=List[HrSchemaEntity188Response])
def list_entities_188(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_188_list(skip=skip, limit=limit)

@router.get("/entity-188/{entity_id}", response_model=HrSchemaEntity188Response)
def get_entity_188(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_188_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 188 not found")
    return res

@router.post("/entity-188", response_model=HrSchemaEntity188Response, status_code=201)
def create_entity_188(payload: HrSchemaEntity188Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_188(payload)

@router.get("/entity-189", response_model=List[HrSchemaEntity189Response])
def list_entities_189(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_189_list(skip=skip, limit=limit)

@router.get("/entity-189/{entity_id}", response_model=HrSchemaEntity189Response)
def get_entity_189(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_189_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 189 not found")
    return res

@router.post("/entity-189", response_model=HrSchemaEntity189Response, status_code=201)
def create_entity_189(payload: HrSchemaEntity189Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_189(payload)

@router.get("/entity-190", response_model=List[HrSchemaEntity190Response])
def list_entities_190(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_190_list(skip=skip, limit=limit)

@router.get("/entity-190/{entity_id}", response_model=HrSchemaEntity190Response)
def get_entity_190(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_190_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 190 not found")
    return res

@router.post("/entity-190", response_model=HrSchemaEntity190Response, status_code=201)
def create_entity_190(payload: HrSchemaEntity190Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_190(payload)

@router.get("/entity-191", response_model=List[HrSchemaEntity191Response])
def list_entities_191(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_191_list(skip=skip, limit=limit)

@router.get("/entity-191/{entity_id}", response_model=HrSchemaEntity191Response)
def get_entity_191(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_191_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 191 not found")
    return res

@router.post("/entity-191", response_model=HrSchemaEntity191Response, status_code=201)
def create_entity_191(payload: HrSchemaEntity191Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_191(payload)

@router.get("/entity-192", response_model=List[HrSchemaEntity192Response])
def list_entities_192(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_192_list(skip=skip, limit=limit)

@router.get("/entity-192/{entity_id}", response_model=HrSchemaEntity192Response)
def get_entity_192(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_192_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 192 not found")
    return res

@router.post("/entity-192", response_model=HrSchemaEntity192Response, status_code=201)
def create_entity_192(payload: HrSchemaEntity192Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_192(payload)

@router.get("/entity-193", response_model=List[HrSchemaEntity193Response])
def list_entities_193(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_193_list(skip=skip, limit=limit)

@router.get("/entity-193/{entity_id}", response_model=HrSchemaEntity193Response)
def get_entity_193(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_193_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 193 not found")
    return res

@router.post("/entity-193", response_model=HrSchemaEntity193Response, status_code=201)
def create_entity_193(payload: HrSchemaEntity193Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_193(payload)

@router.get("/entity-194", response_model=List[HrSchemaEntity194Response])
def list_entities_194(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_194_list(skip=skip, limit=limit)

@router.get("/entity-194/{entity_id}", response_model=HrSchemaEntity194Response)
def get_entity_194(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_194_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 194 not found")
    return res

@router.post("/entity-194", response_model=HrSchemaEntity194Response, status_code=201)
def create_entity_194(payload: HrSchemaEntity194Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_194(payload)

@router.get("/entity-195", response_model=List[HrSchemaEntity195Response])
def list_entities_195(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_195_list(skip=skip, limit=limit)

@router.get("/entity-195/{entity_id}", response_model=HrSchemaEntity195Response)
def get_entity_195(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_195_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 195 not found")
    return res

@router.post("/entity-195", response_model=HrSchemaEntity195Response, status_code=201)
def create_entity_195(payload: HrSchemaEntity195Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_195(payload)

@router.get("/entity-196", response_model=List[HrSchemaEntity196Response])
def list_entities_196(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_196_list(skip=skip, limit=limit)

@router.get("/entity-196/{entity_id}", response_model=HrSchemaEntity196Response)
def get_entity_196(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_196_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 196 not found")
    return res

@router.post("/entity-196", response_model=HrSchemaEntity196Response, status_code=201)
def create_entity_196(payload: HrSchemaEntity196Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_196(payload)

@router.get("/entity-197", response_model=List[HrSchemaEntity197Response])
def list_entities_197(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_197_list(skip=skip, limit=limit)

@router.get("/entity-197/{entity_id}", response_model=HrSchemaEntity197Response)
def get_entity_197(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_197_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 197 not found")
    return res

@router.post("/entity-197", response_model=HrSchemaEntity197Response, status_code=201)
def create_entity_197(payload: HrSchemaEntity197Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_197(payload)

@router.get("/entity-198", response_model=List[HrSchemaEntity198Response])
def list_entities_198(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_198_list(skip=skip, limit=limit)

@router.get("/entity-198/{entity_id}", response_model=HrSchemaEntity198Response)
def get_entity_198(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_198_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 198 not found")
    return res

@router.post("/entity-198", response_model=HrSchemaEntity198Response, status_code=201)
def create_entity_198(payload: HrSchemaEntity198Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_198(payload)

@router.get("/entity-199", response_model=List[HrSchemaEntity199Response])
def list_entities_199(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_199_list(skip=skip, limit=limit)

@router.get("/entity-199/{entity_id}", response_model=HrSchemaEntity199Response)
def get_entity_199(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_199_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 199 not found")
    return res

@router.post("/entity-199", response_model=HrSchemaEntity199Response, status_code=201)
def create_entity_199(payload: HrSchemaEntity199Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_199(payload)

@router.get("/entity-200", response_model=List[HrSchemaEntity200Response])
def list_entities_200(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.get_entity_200_list(skip=skip, limit=limit)

@router.get("/entity-200/{entity_id}", response_model=HrSchemaEntity200Response)
def get_entity_200(entity_id: int, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    res = srv.get_entity_200_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 200 not found")
    return res

@router.post("/entity-200", response_model=HrSchemaEntity200Response, status_code=201)
def create_entity_200(payload: HrSchemaEntity200Create, db: Session = Depends(get_db)):
    srv = HrDomainService(db)
    return srv.create_entity_200(payload)

