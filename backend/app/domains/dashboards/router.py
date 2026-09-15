"""
Executive & Departmental Dashboards - FastAPI Router Endpoints
Module: app.domains.dashboards.router
"""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domains.dashboards.schemas import *
from app.domains.dashboards.service import DashboardsDomainService

router = APIRouter(prefix="/dashboards", tags=["Executive & Departmental Dashboards"])

@router.get("/entity-1", response_model=List[DashboardsSchemaEntity1Response])
def list_entities_1(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_1_list(skip=skip, limit=limit)

@router.get("/entity-1/{entity_id}", response_model=DashboardsSchemaEntity1Response)
def get_entity_1(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_1_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 1 not found")
    return res

@router.post("/entity-1", response_model=DashboardsSchemaEntity1Response, status_code=201)
def create_entity_1(payload: DashboardsSchemaEntity1Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_1(payload)

@router.get("/entity-2", response_model=List[DashboardsSchemaEntity2Response])
def list_entities_2(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_2_list(skip=skip, limit=limit)

@router.get("/entity-2/{entity_id}", response_model=DashboardsSchemaEntity2Response)
def get_entity_2(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_2_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 2 not found")
    return res

@router.post("/entity-2", response_model=DashboardsSchemaEntity2Response, status_code=201)
def create_entity_2(payload: DashboardsSchemaEntity2Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_2(payload)

@router.get("/entity-3", response_model=List[DashboardsSchemaEntity3Response])
def list_entities_3(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_3_list(skip=skip, limit=limit)

@router.get("/entity-3/{entity_id}", response_model=DashboardsSchemaEntity3Response)
def get_entity_3(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_3_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 3 not found")
    return res

@router.post("/entity-3", response_model=DashboardsSchemaEntity3Response, status_code=201)
def create_entity_3(payload: DashboardsSchemaEntity3Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_3(payload)

@router.get("/entity-4", response_model=List[DashboardsSchemaEntity4Response])
def list_entities_4(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_4_list(skip=skip, limit=limit)

@router.get("/entity-4/{entity_id}", response_model=DashboardsSchemaEntity4Response)
def get_entity_4(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_4_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 4 not found")
    return res

@router.post("/entity-4", response_model=DashboardsSchemaEntity4Response, status_code=201)
def create_entity_4(payload: DashboardsSchemaEntity4Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_4(payload)

@router.get("/entity-5", response_model=List[DashboardsSchemaEntity5Response])
def list_entities_5(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_5_list(skip=skip, limit=limit)

@router.get("/entity-5/{entity_id}", response_model=DashboardsSchemaEntity5Response)
def get_entity_5(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_5_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 5 not found")
    return res

@router.post("/entity-5", response_model=DashboardsSchemaEntity5Response, status_code=201)
def create_entity_5(payload: DashboardsSchemaEntity5Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_5(payload)

@router.get("/entity-6", response_model=List[DashboardsSchemaEntity6Response])
def list_entities_6(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_6_list(skip=skip, limit=limit)

@router.get("/entity-6/{entity_id}", response_model=DashboardsSchemaEntity6Response)
def get_entity_6(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_6_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 6 not found")
    return res

@router.post("/entity-6", response_model=DashboardsSchemaEntity6Response, status_code=201)
def create_entity_6(payload: DashboardsSchemaEntity6Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_6(payload)

@router.get("/entity-7", response_model=List[DashboardsSchemaEntity7Response])
def list_entities_7(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_7_list(skip=skip, limit=limit)

@router.get("/entity-7/{entity_id}", response_model=DashboardsSchemaEntity7Response)
def get_entity_7(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_7_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 7 not found")
    return res

@router.post("/entity-7", response_model=DashboardsSchemaEntity7Response, status_code=201)
def create_entity_7(payload: DashboardsSchemaEntity7Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_7(payload)

@router.get("/entity-8", response_model=List[DashboardsSchemaEntity8Response])
def list_entities_8(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_8_list(skip=skip, limit=limit)

@router.get("/entity-8/{entity_id}", response_model=DashboardsSchemaEntity8Response)
def get_entity_8(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_8_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 8 not found")
    return res

@router.post("/entity-8", response_model=DashboardsSchemaEntity8Response, status_code=201)
def create_entity_8(payload: DashboardsSchemaEntity8Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_8(payload)

@router.get("/entity-9", response_model=List[DashboardsSchemaEntity9Response])
def list_entities_9(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_9_list(skip=skip, limit=limit)

@router.get("/entity-9/{entity_id}", response_model=DashboardsSchemaEntity9Response)
def get_entity_9(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_9_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 9 not found")
    return res

@router.post("/entity-9", response_model=DashboardsSchemaEntity9Response, status_code=201)
def create_entity_9(payload: DashboardsSchemaEntity9Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_9(payload)

@router.get("/entity-10", response_model=List[DashboardsSchemaEntity10Response])
def list_entities_10(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_10_list(skip=skip, limit=limit)

@router.get("/entity-10/{entity_id}", response_model=DashboardsSchemaEntity10Response)
def get_entity_10(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_10_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 10 not found")
    return res

@router.post("/entity-10", response_model=DashboardsSchemaEntity10Response, status_code=201)
def create_entity_10(payload: DashboardsSchemaEntity10Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_10(payload)

@router.get("/entity-11", response_model=List[DashboardsSchemaEntity11Response])
def list_entities_11(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_11_list(skip=skip, limit=limit)

@router.get("/entity-11/{entity_id}", response_model=DashboardsSchemaEntity11Response)
def get_entity_11(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_11_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 11 not found")
    return res

@router.post("/entity-11", response_model=DashboardsSchemaEntity11Response, status_code=201)
def create_entity_11(payload: DashboardsSchemaEntity11Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_11(payload)

@router.get("/entity-12", response_model=List[DashboardsSchemaEntity12Response])
def list_entities_12(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_12_list(skip=skip, limit=limit)

@router.get("/entity-12/{entity_id}", response_model=DashboardsSchemaEntity12Response)
def get_entity_12(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_12_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 12 not found")
    return res

@router.post("/entity-12", response_model=DashboardsSchemaEntity12Response, status_code=201)
def create_entity_12(payload: DashboardsSchemaEntity12Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_12(payload)

@router.get("/entity-13", response_model=List[DashboardsSchemaEntity13Response])
def list_entities_13(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_13_list(skip=skip, limit=limit)

@router.get("/entity-13/{entity_id}", response_model=DashboardsSchemaEntity13Response)
def get_entity_13(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_13_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 13 not found")
    return res

@router.post("/entity-13", response_model=DashboardsSchemaEntity13Response, status_code=201)
def create_entity_13(payload: DashboardsSchemaEntity13Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_13(payload)

@router.get("/entity-14", response_model=List[DashboardsSchemaEntity14Response])
def list_entities_14(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_14_list(skip=skip, limit=limit)

@router.get("/entity-14/{entity_id}", response_model=DashboardsSchemaEntity14Response)
def get_entity_14(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_14_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 14 not found")
    return res

@router.post("/entity-14", response_model=DashboardsSchemaEntity14Response, status_code=201)
def create_entity_14(payload: DashboardsSchemaEntity14Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_14(payload)

@router.get("/entity-15", response_model=List[DashboardsSchemaEntity15Response])
def list_entities_15(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_15_list(skip=skip, limit=limit)

@router.get("/entity-15/{entity_id}", response_model=DashboardsSchemaEntity15Response)
def get_entity_15(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_15_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 15 not found")
    return res

@router.post("/entity-15", response_model=DashboardsSchemaEntity15Response, status_code=201)
def create_entity_15(payload: DashboardsSchemaEntity15Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_15(payload)

@router.get("/entity-16", response_model=List[DashboardsSchemaEntity16Response])
def list_entities_16(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_16_list(skip=skip, limit=limit)

@router.get("/entity-16/{entity_id}", response_model=DashboardsSchemaEntity16Response)
def get_entity_16(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_16_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 16 not found")
    return res

@router.post("/entity-16", response_model=DashboardsSchemaEntity16Response, status_code=201)
def create_entity_16(payload: DashboardsSchemaEntity16Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_16(payload)

@router.get("/entity-17", response_model=List[DashboardsSchemaEntity17Response])
def list_entities_17(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_17_list(skip=skip, limit=limit)

@router.get("/entity-17/{entity_id}", response_model=DashboardsSchemaEntity17Response)
def get_entity_17(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_17_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 17 not found")
    return res

@router.post("/entity-17", response_model=DashboardsSchemaEntity17Response, status_code=201)
def create_entity_17(payload: DashboardsSchemaEntity17Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_17(payload)

@router.get("/entity-18", response_model=List[DashboardsSchemaEntity18Response])
def list_entities_18(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_18_list(skip=skip, limit=limit)

@router.get("/entity-18/{entity_id}", response_model=DashboardsSchemaEntity18Response)
def get_entity_18(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_18_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 18 not found")
    return res

@router.post("/entity-18", response_model=DashboardsSchemaEntity18Response, status_code=201)
def create_entity_18(payload: DashboardsSchemaEntity18Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_18(payload)

@router.get("/entity-19", response_model=List[DashboardsSchemaEntity19Response])
def list_entities_19(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_19_list(skip=skip, limit=limit)

@router.get("/entity-19/{entity_id}", response_model=DashboardsSchemaEntity19Response)
def get_entity_19(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_19_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 19 not found")
    return res

@router.post("/entity-19", response_model=DashboardsSchemaEntity19Response, status_code=201)
def create_entity_19(payload: DashboardsSchemaEntity19Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_19(payload)

@router.get("/entity-20", response_model=List[DashboardsSchemaEntity20Response])
def list_entities_20(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_20_list(skip=skip, limit=limit)

@router.get("/entity-20/{entity_id}", response_model=DashboardsSchemaEntity20Response)
def get_entity_20(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_20_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 20 not found")
    return res

@router.post("/entity-20", response_model=DashboardsSchemaEntity20Response, status_code=201)
def create_entity_20(payload: DashboardsSchemaEntity20Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_20(payload)

@router.get("/entity-21", response_model=List[DashboardsSchemaEntity21Response])
def list_entities_21(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_21_list(skip=skip, limit=limit)

@router.get("/entity-21/{entity_id}", response_model=DashboardsSchemaEntity21Response)
def get_entity_21(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_21_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 21 not found")
    return res

@router.post("/entity-21", response_model=DashboardsSchemaEntity21Response, status_code=201)
def create_entity_21(payload: DashboardsSchemaEntity21Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_21(payload)

@router.get("/entity-22", response_model=List[DashboardsSchemaEntity22Response])
def list_entities_22(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_22_list(skip=skip, limit=limit)

@router.get("/entity-22/{entity_id}", response_model=DashboardsSchemaEntity22Response)
def get_entity_22(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_22_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 22 not found")
    return res

@router.post("/entity-22", response_model=DashboardsSchemaEntity22Response, status_code=201)
def create_entity_22(payload: DashboardsSchemaEntity22Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_22(payload)

@router.get("/entity-23", response_model=List[DashboardsSchemaEntity23Response])
def list_entities_23(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_23_list(skip=skip, limit=limit)

@router.get("/entity-23/{entity_id}", response_model=DashboardsSchemaEntity23Response)
def get_entity_23(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_23_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 23 not found")
    return res

@router.post("/entity-23", response_model=DashboardsSchemaEntity23Response, status_code=201)
def create_entity_23(payload: DashboardsSchemaEntity23Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_23(payload)

@router.get("/entity-24", response_model=List[DashboardsSchemaEntity24Response])
def list_entities_24(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_24_list(skip=skip, limit=limit)

@router.get("/entity-24/{entity_id}", response_model=DashboardsSchemaEntity24Response)
def get_entity_24(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_24_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 24 not found")
    return res

@router.post("/entity-24", response_model=DashboardsSchemaEntity24Response, status_code=201)
def create_entity_24(payload: DashboardsSchemaEntity24Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_24(payload)

@router.get("/entity-25", response_model=List[DashboardsSchemaEntity25Response])
def list_entities_25(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_25_list(skip=skip, limit=limit)

@router.get("/entity-25/{entity_id}", response_model=DashboardsSchemaEntity25Response)
def get_entity_25(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_25_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 25 not found")
    return res

@router.post("/entity-25", response_model=DashboardsSchemaEntity25Response, status_code=201)
def create_entity_25(payload: DashboardsSchemaEntity25Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_25(payload)

@router.get("/entity-26", response_model=List[DashboardsSchemaEntity26Response])
def list_entities_26(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_26_list(skip=skip, limit=limit)

@router.get("/entity-26/{entity_id}", response_model=DashboardsSchemaEntity26Response)
def get_entity_26(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_26_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 26 not found")
    return res

@router.post("/entity-26", response_model=DashboardsSchemaEntity26Response, status_code=201)
def create_entity_26(payload: DashboardsSchemaEntity26Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_26(payload)

@router.get("/entity-27", response_model=List[DashboardsSchemaEntity27Response])
def list_entities_27(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_27_list(skip=skip, limit=limit)

@router.get("/entity-27/{entity_id}", response_model=DashboardsSchemaEntity27Response)
def get_entity_27(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_27_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 27 not found")
    return res

@router.post("/entity-27", response_model=DashboardsSchemaEntity27Response, status_code=201)
def create_entity_27(payload: DashboardsSchemaEntity27Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_27(payload)

@router.get("/entity-28", response_model=List[DashboardsSchemaEntity28Response])
def list_entities_28(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_28_list(skip=skip, limit=limit)

@router.get("/entity-28/{entity_id}", response_model=DashboardsSchemaEntity28Response)
def get_entity_28(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_28_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 28 not found")
    return res

@router.post("/entity-28", response_model=DashboardsSchemaEntity28Response, status_code=201)
def create_entity_28(payload: DashboardsSchemaEntity28Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_28(payload)

@router.get("/entity-29", response_model=List[DashboardsSchemaEntity29Response])
def list_entities_29(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_29_list(skip=skip, limit=limit)

@router.get("/entity-29/{entity_id}", response_model=DashboardsSchemaEntity29Response)
def get_entity_29(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_29_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 29 not found")
    return res

@router.post("/entity-29", response_model=DashboardsSchemaEntity29Response, status_code=201)
def create_entity_29(payload: DashboardsSchemaEntity29Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_29(payload)

@router.get("/entity-30", response_model=List[DashboardsSchemaEntity30Response])
def list_entities_30(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_30_list(skip=skip, limit=limit)

@router.get("/entity-30/{entity_id}", response_model=DashboardsSchemaEntity30Response)
def get_entity_30(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_30_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 30 not found")
    return res

@router.post("/entity-30", response_model=DashboardsSchemaEntity30Response, status_code=201)
def create_entity_30(payload: DashboardsSchemaEntity30Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_30(payload)

@router.get("/entity-31", response_model=List[DashboardsSchemaEntity31Response])
def list_entities_31(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_31_list(skip=skip, limit=limit)

@router.get("/entity-31/{entity_id}", response_model=DashboardsSchemaEntity31Response)
def get_entity_31(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_31_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 31 not found")
    return res

@router.post("/entity-31", response_model=DashboardsSchemaEntity31Response, status_code=201)
def create_entity_31(payload: DashboardsSchemaEntity31Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_31(payload)

@router.get("/entity-32", response_model=List[DashboardsSchemaEntity32Response])
def list_entities_32(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_32_list(skip=skip, limit=limit)

@router.get("/entity-32/{entity_id}", response_model=DashboardsSchemaEntity32Response)
def get_entity_32(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_32_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 32 not found")
    return res

@router.post("/entity-32", response_model=DashboardsSchemaEntity32Response, status_code=201)
def create_entity_32(payload: DashboardsSchemaEntity32Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_32(payload)

@router.get("/entity-33", response_model=List[DashboardsSchemaEntity33Response])
def list_entities_33(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_33_list(skip=skip, limit=limit)

@router.get("/entity-33/{entity_id}", response_model=DashboardsSchemaEntity33Response)
def get_entity_33(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_33_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 33 not found")
    return res

@router.post("/entity-33", response_model=DashboardsSchemaEntity33Response, status_code=201)
def create_entity_33(payload: DashboardsSchemaEntity33Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_33(payload)

@router.get("/entity-34", response_model=List[DashboardsSchemaEntity34Response])
def list_entities_34(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_34_list(skip=skip, limit=limit)

@router.get("/entity-34/{entity_id}", response_model=DashboardsSchemaEntity34Response)
def get_entity_34(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_34_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 34 not found")
    return res

@router.post("/entity-34", response_model=DashboardsSchemaEntity34Response, status_code=201)
def create_entity_34(payload: DashboardsSchemaEntity34Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_34(payload)

@router.get("/entity-35", response_model=List[DashboardsSchemaEntity35Response])
def list_entities_35(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_35_list(skip=skip, limit=limit)

@router.get("/entity-35/{entity_id}", response_model=DashboardsSchemaEntity35Response)
def get_entity_35(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_35_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 35 not found")
    return res

@router.post("/entity-35", response_model=DashboardsSchemaEntity35Response, status_code=201)
def create_entity_35(payload: DashboardsSchemaEntity35Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_35(payload)

@router.get("/entity-36", response_model=List[DashboardsSchemaEntity36Response])
def list_entities_36(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_36_list(skip=skip, limit=limit)

@router.get("/entity-36/{entity_id}", response_model=DashboardsSchemaEntity36Response)
def get_entity_36(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_36_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 36 not found")
    return res

@router.post("/entity-36", response_model=DashboardsSchemaEntity36Response, status_code=201)
def create_entity_36(payload: DashboardsSchemaEntity36Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_36(payload)

@router.get("/entity-37", response_model=List[DashboardsSchemaEntity37Response])
def list_entities_37(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_37_list(skip=skip, limit=limit)

@router.get("/entity-37/{entity_id}", response_model=DashboardsSchemaEntity37Response)
def get_entity_37(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_37_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 37 not found")
    return res

@router.post("/entity-37", response_model=DashboardsSchemaEntity37Response, status_code=201)
def create_entity_37(payload: DashboardsSchemaEntity37Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_37(payload)

@router.get("/entity-38", response_model=List[DashboardsSchemaEntity38Response])
def list_entities_38(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_38_list(skip=skip, limit=limit)

@router.get("/entity-38/{entity_id}", response_model=DashboardsSchemaEntity38Response)
def get_entity_38(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_38_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 38 not found")
    return res

@router.post("/entity-38", response_model=DashboardsSchemaEntity38Response, status_code=201)
def create_entity_38(payload: DashboardsSchemaEntity38Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_38(payload)

@router.get("/entity-39", response_model=List[DashboardsSchemaEntity39Response])
def list_entities_39(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_39_list(skip=skip, limit=limit)

@router.get("/entity-39/{entity_id}", response_model=DashboardsSchemaEntity39Response)
def get_entity_39(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_39_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 39 not found")
    return res

@router.post("/entity-39", response_model=DashboardsSchemaEntity39Response, status_code=201)
def create_entity_39(payload: DashboardsSchemaEntity39Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_39(payload)

@router.get("/entity-40", response_model=List[DashboardsSchemaEntity40Response])
def list_entities_40(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_40_list(skip=skip, limit=limit)

@router.get("/entity-40/{entity_id}", response_model=DashboardsSchemaEntity40Response)
def get_entity_40(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_40_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 40 not found")
    return res

@router.post("/entity-40", response_model=DashboardsSchemaEntity40Response, status_code=201)
def create_entity_40(payload: DashboardsSchemaEntity40Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_40(payload)

@router.get("/entity-41", response_model=List[DashboardsSchemaEntity41Response])
def list_entities_41(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_41_list(skip=skip, limit=limit)

@router.get("/entity-41/{entity_id}", response_model=DashboardsSchemaEntity41Response)
def get_entity_41(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_41_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 41 not found")
    return res

@router.post("/entity-41", response_model=DashboardsSchemaEntity41Response, status_code=201)
def create_entity_41(payload: DashboardsSchemaEntity41Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_41(payload)

@router.get("/entity-42", response_model=List[DashboardsSchemaEntity42Response])
def list_entities_42(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_42_list(skip=skip, limit=limit)

@router.get("/entity-42/{entity_id}", response_model=DashboardsSchemaEntity42Response)
def get_entity_42(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_42_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 42 not found")
    return res

@router.post("/entity-42", response_model=DashboardsSchemaEntity42Response, status_code=201)
def create_entity_42(payload: DashboardsSchemaEntity42Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_42(payload)

@router.get("/entity-43", response_model=List[DashboardsSchemaEntity43Response])
def list_entities_43(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_43_list(skip=skip, limit=limit)

@router.get("/entity-43/{entity_id}", response_model=DashboardsSchemaEntity43Response)
def get_entity_43(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_43_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 43 not found")
    return res

@router.post("/entity-43", response_model=DashboardsSchemaEntity43Response, status_code=201)
def create_entity_43(payload: DashboardsSchemaEntity43Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_43(payload)

@router.get("/entity-44", response_model=List[DashboardsSchemaEntity44Response])
def list_entities_44(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_44_list(skip=skip, limit=limit)

@router.get("/entity-44/{entity_id}", response_model=DashboardsSchemaEntity44Response)
def get_entity_44(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_44_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 44 not found")
    return res

@router.post("/entity-44", response_model=DashboardsSchemaEntity44Response, status_code=201)
def create_entity_44(payload: DashboardsSchemaEntity44Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_44(payload)

@router.get("/entity-45", response_model=List[DashboardsSchemaEntity45Response])
def list_entities_45(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_45_list(skip=skip, limit=limit)

@router.get("/entity-45/{entity_id}", response_model=DashboardsSchemaEntity45Response)
def get_entity_45(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_45_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 45 not found")
    return res

@router.post("/entity-45", response_model=DashboardsSchemaEntity45Response, status_code=201)
def create_entity_45(payload: DashboardsSchemaEntity45Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_45(payload)

@router.get("/entity-46", response_model=List[DashboardsSchemaEntity46Response])
def list_entities_46(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_46_list(skip=skip, limit=limit)

@router.get("/entity-46/{entity_id}", response_model=DashboardsSchemaEntity46Response)
def get_entity_46(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_46_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 46 not found")
    return res

@router.post("/entity-46", response_model=DashboardsSchemaEntity46Response, status_code=201)
def create_entity_46(payload: DashboardsSchemaEntity46Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_46(payload)

@router.get("/entity-47", response_model=List[DashboardsSchemaEntity47Response])
def list_entities_47(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_47_list(skip=skip, limit=limit)

@router.get("/entity-47/{entity_id}", response_model=DashboardsSchemaEntity47Response)
def get_entity_47(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_47_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 47 not found")
    return res

@router.post("/entity-47", response_model=DashboardsSchemaEntity47Response, status_code=201)
def create_entity_47(payload: DashboardsSchemaEntity47Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_47(payload)

@router.get("/entity-48", response_model=List[DashboardsSchemaEntity48Response])
def list_entities_48(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_48_list(skip=skip, limit=limit)

@router.get("/entity-48/{entity_id}", response_model=DashboardsSchemaEntity48Response)
def get_entity_48(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_48_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 48 not found")
    return res

@router.post("/entity-48", response_model=DashboardsSchemaEntity48Response, status_code=201)
def create_entity_48(payload: DashboardsSchemaEntity48Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_48(payload)

@router.get("/entity-49", response_model=List[DashboardsSchemaEntity49Response])
def list_entities_49(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_49_list(skip=skip, limit=limit)

@router.get("/entity-49/{entity_id}", response_model=DashboardsSchemaEntity49Response)
def get_entity_49(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_49_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 49 not found")
    return res

@router.post("/entity-49", response_model=DashboardsSchemaEntity49Response, status_code=201)
def create_entity_49(payload: DashboardsSchemaEntity49Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_49(payload)

@router.get("/entity-50", response_model=List[DashboardsSchemaEntity50Response])
def list_entities_50(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_50_list(skip=skip, limit=limit)

@router.get("/entity-50/{entity_id}", response_model=DashboardsSchemaEntity50Response)
def get_entity_50(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_50_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 50 not found")
    return res

@router.post("/entity-50", response_model=DashboardsSchemaEntity50Response, status_code=201)
def create_entity_50(payload: DashboardsSchemaEntity50Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_50(payload)

@router.get("/entity-51", response_model=List[DashboardsSchemaEntity51Response])
def list_entities_51(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_51_list(skip=skip, limit=limit)

@router.get("/entity-51/{entity_id}", response_model=DashboardsSchemaEntity51Response)
def get_entity_51(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_51_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 51 not found")
    return res

@router.post("/entity-51", response_model=DashboardsSchemaEntity51Response, status_code=201)
def create_entity_51(payload: DashboardsSchemaEntity51Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_51(payload)

@router.get("/entity-52", response_model=List[DashboardsSchemaEntity52Response])
def list_entities_52(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_52_list(skip=skip, limit=limit)

@router.get("/entity-52/{entity_id}", response_model=DashboardsSchemaEntity52Response)
def get_entity_52(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_52_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 52 not found")
    return res

@router.post("/entity-52", response_model=DashboardsSchemaEntity52Response, status_code=201)
def create_entity_52(payload: DashboardsSchemaEntity52Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_52(payload)

@router.get("/entity-53", response_model=List[DashboardsSchemaEntity53Response])
def list_entities_53(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_53_list(skip=skip, limit=limit)

@router.get("/entity-53/{entity_id}", response_model=DashboardsSchemaEntity53Response)
def get_entity_53(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_53_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 53 not found")
    return res

@router.post("/entity-53", response_model=DashboardsSchemaEntity53Response, status_code=201)
def create_entity_53(payload: DashboardsSchemaEntity53Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_53(payload)

@router.get("/entity-54", response_model=List[DashboardsSchemaEntity54Response])
def list_entities_54(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_54_list(skip=skip, limit=limit)

@router.get("/entity-54/{entity_id}", response_model=DashboardsSchemaEntity54Response)
def get_entity_54(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_54_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 54 not found")
    return res

@router.post("/entity-54", response_model=DashboardsSchemaEntity54Response, status_code=201)
def create_entity_54(payload: DashboardsSchemaEntity54Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_54(payload)

@router.get("/entity-55", response_model=List[DashboardsSchemaEntity55Response])
def list_entities_55(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_55_list(skip=skip, limit=limit)

@router.get("/entity-55/{entity_id}", response_model=DashboardsSchemaEntity55Response)
def get_entity_55(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_55_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 55 not found")
    return res

@router.post("/entity-55", response_model=DashboardsSchemaEntity55Response, status_code=201)
def create_entity_55(payload: DashboardsSchemaEntity55Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_55(payload)

@router.get("/entity-56", response_model=List[DashboardsSchemaEntity56Response])
def list_entities_56(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_56_list(skip=skip, limit=limit)

@router.get("/entity-56/{entity_id}", response_model=DashboardsSchemaEntity56Response)
def get_entity_56(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_56_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 56 not found")
    return res

@router.post("/entity-56", response_model=DashboardsSchemaEntity56Response, status_code=201)
def create_entity_56(payload: DashboardsSchemaEntity56Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_56(payload)

@router.get("/entity-57", response_model=List[DashboardsSchemaEntity57Response])
def list_entities_57(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_57_list(skip=skip, limit=limit)

@router.get("/entity-57/{entity_id}", response_model=DashboardsSchemaEntity57Response)
def get_entity_57(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_57_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 57 not found")
    return res

@router.post("/entity-57", response_model=DashboardsSchemaEntity57Response, status_code=201)
def create_entity_57(payload: DashboardsSchemaEntity57Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_57(payload)

@router.get("/entity-58", response_model=List[DashboardsSchemaEntity58Response])
def list_entities_58(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_58_list(skip=skip, limit=limit)

@router.get("/entity-58/{entity_id}", response_model=DashboardsSchemaEntity58Response)
def get_entity_58(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_58_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 58 not found")
    return res

@router.post("/entity-58", response_model=DashboardsSchemaEntity58Response, status_code=201)
def create_entity_58(payload: DashboardsSchemaEntity58Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_58(payload)

@router.get("/entity-59", response_model=List[DashboardsSchemaEntity59Response])
def list_entities_59(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_59_list(skip=skip, limit=limit)

@router.get("/entity-59/{entity_id}", response_model=DashboardsSchemaEntity59Response)
def get_entity_59(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_59_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 59 not found")
    return res

@router.post("/entity-59", response_model=DashboardsSchemaEntity59Response, status_code=201)
def create_entity_59(payload: DashboardsSchemaEntity59Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_59(payload)

@router.get("/entity-60", response_model=List[DashboardsSchemaEntity60Response])
def list_entities_60(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_60_list(skip=skip, limit=limit)

@router.get("/entity-60/{entity_id}", response_model=DashboardsSchemaEntity60Response)
def get_entity_60(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_60_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 60 not found")
    return res

@router.post("/entity-60", response_model=DashboardsSchemaEntity60Response, status_code=201)
def create_entity_60(payload: DashboardsSchemaEntity60Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_60(payload)

@router.get("/entity-61", response_model=List[DashboardsSchemaEntity61Response])
def list_entities_61(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_61_list(skip=skip, limit=limit)

@router.get("/entity-61/{entity_id}", response_model=DashboardsSchemaEntity61Response)
def get_entity_61(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_61_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 61 not found")
    return res

@router.post("/entity-61", response_model=DashboardsSchemaEntity61Response, status_code=201)
def create_entity_61(payload: DashboardsSchemaEntity61Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_61(payload)

@router.get("/entity-62", response_model=List[DashboardsSchemaEntity62Response])
def list_entities_62(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_62_list(skip=skip, limit=limit)

@router.get("/entity-62/{entity_id}", response_model=DashboardsSchemaEntity62Response)
def get_entity_62(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_62_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 62 not found")
    return res

@router.post("/entity-62", response_model=DashboardsSchemaEntity62Response, status_code=201)
def create_entity_62(payload: DashboardsSchemaEntity62Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_62(payload)

@router.get("/entity-63", response_model=List[DashboardsSchemaEntity63Response])
def list_entities_63(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_63_list(skip=skip, limit=limit)

@router.get("/entity-63/{entity_id}", response_model=DashboardsSchemaEntity63Response)
def get_entity_63(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_63_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 63 not found")
    return res

@router.post("/entity-63", response_model=DashboardsSchemaEntity63Response, status_code=201)
def create_entity_63(payload: DashboardsSchemaEntity63Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_63(payload)

@router.get("/entity-64", response_model=List[DashboardsSchemaEntity64Response])
def list_entities_64(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_64_list(skip=skip, limit=limit)

@router.get("/entity-64/{entity_id}", response_model=DashboardsSchemaEntity64Response)
def get_entity_64(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_64_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 64 not found")
    return res

@router.post("/entity-64", response_model=DashboardsSchemaEntity64Response, status_code=201)
def create_entity_64(payload: DashboardsSchemaEntity64Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_64(payload)

@router.get("/entity-65", response_model=List[DashboardsSchemaEntity65Response])
def list_entities_65(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_65_list(skip=skip, limit=limit)

@router.get("/entity-65/{entity_id}", response_model=DashboardsSchemaEntity65Response)
def get_entity_65(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_65_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 65 not found")
    return res

@router.post("/entity-65", response_model=DashboardsSchemaEntity65Response, status_code=201)
def create_entity_65(payload: DashboardsSchemaEntity65Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_65(payload)

@router.get("/entity-66", response_model=List[DashboardsSchemaEntity66Response])
def list_entities_66(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_66_list(skip=skip, limit=limit)

@router.get("/entity-66/{entity_id}", response_model=DashboardsSchemaEntity66Response)
def get_entity_66(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_66_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 66 not found")
    return res

@router.post("/entity-66", response_model=DashboardsSchemaEntity66Response, status_code=201)
def create_entity_66(payload: DashboardsSchemaEntity66Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_66(payload)

@router.get("/entity-67", response_model=List[DashboardsSchemaEntity67Response])
def list_entities_67(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_67_list(skip=skip, limit=limit)

@router.get("/entity-67/{entity_id}", response_model=DashboardsSchemaEntity67Response)
def get_entity_67(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_67_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 67 not found")
    return res

@router.post("/entity-67", response_model=DashboardsSchemaEntity67Response, status_code=201)
def create_entity_67(payload: DashboardsSchemaEntity67Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_67(payload)

@router.get("/entity-68", response_model=List[DashboardsSchemaEntity68Response])
def list_entities_68(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_68_list(skip=skip, limit=limit)

@router.get("/entity-68/{entity_id}", response_model=DashboardsSchemaEntity68Response)
def get_entity_68(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_68_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 68 not found")
    return res

@router.post("/entity-68", response_model=DashboardsSchemaEntity68Response, status_code=201)
def create_entity_68(payload: DashboardsSchemaEntity68Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_68(payload)

@router.get("/entity-69", response_model=List[DashboardsSchemaEntity69Response])
def list_entities_69(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_69_list(skip=skip, limit=limit)

@router.get("/entity-69/{entity_id}", response_model=DashboardsSchemaEntity69Response)
def get_entity_69(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_69_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 69 not found")
    return res

@router.post("/entity-69", response_model=DashboardsSchemaEntity69Response, status_code=201)
def create_entity_69(payload: DashboardsSchemaEntity69Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_69(payload)

@router.get("/entity-70", response_model=List[DashboardsSchemaEntity70Response])
def list_entities_70(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_70_list(skip=skip, limit=limit)

@router.get("/entity-70/{entity_id}", response_model=DashboardsSchemaEntity70Response)
def get_entity_70(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_70_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 70 not found")
    return res

@router.post("/entity-70", response_model=DashboardsSchemaEntity70Response, status_code=201)
def create_entity_70(payload: DashboardsSchemaEntity70Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_70(payload)

@router.get("/entity-71", response_model=List[DashboardsSchemaEntity71Response])
def list_entities_71(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_71_list(skip=skip, limit=limit)

@router.get("/entity-71/{entity_id}", response_model=DashboardsSchemaEntity71Response)
def get_entity_71(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_71_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 71 not found")
    return res

@router.post("/entity-71", response_model=DashboardsSchemaEntity71Response, status_code=201)
def create_entity_71(payload: DashboardsSchemaEntity71Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_71(payload)

@router.get("/entity-72", response_model=List[DashboardsSchemaEntity72Response])
def list_entities_72(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_72_list(skip=skip, limit=limit)

@router.get("/entity-72/{entity_id}", response_model=DashboardsSchemaEntity72Response)
def get_entity_72(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_72_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 72 not found")
    return res

@router.post("/entity-72", response_model=DashboardsSchemaEntity72Response, status_code=201)
def create_entity_72(payload: DashboardsSchemaEntity72Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_72(payload)

@router.get("/entity-73", response_model=List[DashboardsSchemaEntity73Response])
def list_entities_73(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_73_list(skip=skip, limit=limit)

@router.get("/entity-73/{entity_id}", response_model=DashboardsSchemaEntity73Response)
def get_entity_73(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_73_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 73 not found")
    return res

@router.post("/entity-73", response_model=DashboardsSchemaEntity73Response, status_code=201)
def create_entity_73(payload: DashboardsSchemaEntity73Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_73(payload)

@router.get("/entity-74", response_model=List[DashboardsSchemaEntity74Response])
def list_entities_74(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_74_list(skip=skip, limit=limit)

@router.get("/entity-74/{entity_id}", response_model=DashboardsSchemaEntity74Response)
def get_entity_74(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_74_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 74 not found")
    return res

@router.post("/entity-74", response_model=DashboardsSchemaEntity74Response, status_code=201)
def create_entity_74(payload: DashboardsSchemaEntity74Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_74(payload)

@router.get("/entity-75", response_model=List[DashboardsSchemaEntity75Response])
def list_entities_75(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_75_list(skip=skip, limit=limit)

@router.get("/entity-75/{entity_id}", response_model=DashboardsSchemaEntity75Response)
def get_entity_75(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_75_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 75 not found")
    return res

@router.post("/entity-75", response_model=DashboardsSchemaEntity75Response, status_code=201)
def create_entity_75(payload: DashboardsSchemaEntity75Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_75(payload)

@router.get("/entity-76", response_model=List[DashboardsSchemaEntity76Response])
def list_entities_76(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_76_list(skip=skip, limit=limit)

@router.get("/entity-76/{entity_id}", response_model=DashboardsSchemaEntity76Response)
def get_entity_76(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_76_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 76 not found")
    return res

@router.post("/entity-76", response_model=DashboardsSchemaEntity76Response, status_code=201)
def create_entity_76(payload: DashboardsSchemaEntity76Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_76(payload)

@router.get("/entity-77", response_model=List[DashboardsSchemaEntity77Response])
def list_entities_77(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_77_list(skip=skip, limit=limit)

@router.get("/entity-77/{entity_id}", response_model=DashboardsSchemaEntity77Response)
def get_entity_77(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_77_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 77 not found")
    return res

@router.post("/entity-77", response_model=DashboardsSchemaEntity77Response, status_code=201)
def create_entity_77(payload: DashboardsSchemaEntity77Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_77(payload)

@router.get("/entity-78", response_model=List[DashboardsSchemaEntity78Response])
def list_entities_78(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_78_list(skip=skip, limit=limit)

@router.get("/entity-78/{entity_id}", response_model=DashboardsSchemaEntity78Response)
def get_entity_78(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_78_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 78 not found")
    return res

@router.post("/entity-78", response_model=DashboardsSchemaEntity78Response, status_code=201)
def create_entity_78(payload: DashboardsSchemaEntity78Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_78(payload)

@router.get("/entity-79", response_model=List[DashboardsSchemaEntity79Response])
def list_entities_79(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_79_list(skip=skip, limit=limit)

@router.get("/entity-79/{entity_id}", response_model=DashboardsSchemaEntity79Response)
def get_entity_79(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_79_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 79 not found")
    return res

@router.post("/entity-79", response_model=DashboardsSchemaEntity79Response, status_code=201)
def create_entity_79(payload: DashboardsSchemaEntity79Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_79(payload)

@router.get("/entity-80", response_model=List[DashboardsSchemaEntity80Response])
def list_entities_80(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_80_list(skip=skip, limit=limit)

@router.get("/entity-80/{entity_id}", response_model=DashboardsSchemaEntity80Response)
def get_entity_80(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_80_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 80 not found")
    return res

@router.post("/entity-80", response_model=DashboardsSchemaEntity80Response, status_code=201)
def create_entity_80(payload: DashboardsSchemaEntity80Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_80(payload)

@router.get("/entity-81", response_model=List[DashboardsSchemaEntity81Response])
def list_entities_81(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_81_list(skip=skip, limit=limit)

@router.get("/entity-81/{entity_id}", response_model=DashboardsSchemaEntity81Response)
def get_entity_81(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_81_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 81 not found")
    return res

@router.post("/entity-81", response_model=DashboardsSchemaEntity81Response, status_code=201)
def create_entity_81(payload: DashboardsSchemaEntity81Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_81(payload)

@router.get("/entity-82", response_model=List[DashboardsSchemaEntity82Response])
def list_entities_82(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_82_list(skip=skip, limit=limit)

@router.get("/entity-82/{entity_id}", response_model=DashboardsSchemaEntity82Response)
def get_entity_82(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_82_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 82 not found")
    return res

@router.post("/entity-82", response_model=DashboardsSchemaEntity82Response, status_code=201)
def create_entity_82(payload: DashboardsSchemaEntity82Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_82(payload)

@router.get("/entity-83", response_model=List[DashboardsSchemaEntity83Response])
def list_entities_83(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_83_list(skip=skip, limit=limit)

@router.get("/entity-83/{entity_id}", response_model=DashboardsSchemaEntity83Response)
def get_entity_83(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_83_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 83 not found")
    return res

@router.post("/entity-83", response_model=DashboardsSchemaEntity83Response, status_code=201)
def create_entity_83(payload: DashboardsSchemaEntity83Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_83(payload)

@router.get("/entity-84", response_model=List[DashboardsSchemaEntity84Response])
def list_entities_84(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_84_list(skip=skip, limit=limit)

@router.get("/entity-84/{entity_id}", response_model=DashboardsSchemaEntity84Response)
def get_entity_84(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_84_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 84 not found")
    return res

@router.post("/entity-84", response_model=DashboardsSchemaEntity84Response, status_code=201)
def create_entity_84(payload: DashboardsSchemaEntity84Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_84(payload)

@router.get("/entity-85", response_model=List[DashboardsSchemaEntity85Response])
def list_entities_85(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_85_list(skip=skip, limit=limit)

@router.get("/entity-85/{entity_id}", response_model=DashboardsSchemaEntity85Response)
def get_entity_85(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_85_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 85 not found")
    return res

@router.post("/entity-85", response_model=DashboardsSchemaEntity85Response, status_code=201)
def create_entity_85(payload: DashboardsSchemaEntity85Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_85(payload)

@router.get("/entity-86", response_model=List[DashboardsSchemaEntity86Response])
def list_entities_86(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_86_list(skip=skip, limit=limit)

@router.get("/entity-86/{entity_id}", response_model=DashboardsSchemaEntity86Response)
def get_entity_86(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_86_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 86 not found")
    return res

@router.post("/entity-86", response_model=DashboardsSchemaEntity86Response, status_code=201)
def create_entity_86(payload: DashboardsSchemaEntity86Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_86(payload)

@router.get("/entity-87", response_model=List[DashboardsSchemaEntity87Response])
def list_entities_87(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_87_list(skip=skip, limit=limit)

@router.get("/entity-87/{entity_id}", response_model=DashboardsSchemaEntity87Response)
def get_entity_87(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_87_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 87 not found")
    return res

@router.post("/entity-87", response_model=DashboardsSchemaEntity87Response, status_code=201)
def create_entity_87(payload: DashboardsSchemaEntity87Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_87(payload)

@router.get("/entity-88", response_model=List[DashboardsSchemaEntity88Response])
def list_entities_88(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_88_list(skip=skip, limit=limit)

@router.get("/entity-88/{entity_id}", response_model=DashboardsSchemaEntity88Response)
def get_entity_88(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_88_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 88 not found")
    return res

@router.post("/entity-88", response_model=DashboardsSchemaEntity88Response, status_code=201)
def create_entity_88(payload: DashboardsSchemaEntity88Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_88(payload)

@router.get("/entity-89", response_model=List[DashboardsSchemaEntity89Response])
def list_entities_89(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_89_list(skip=skip, limit=limit)

@router.get("/entity-89/{entity_id}", response_model=DashboardsSchemaEntity89Response)
def get_entity_89(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_89_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 89 not found")
    return res

@router.post("/entity-89", response_model=DashboardsSchemaEntity89Response, status_code=201)
def create_entity_89(payload: DashboardsSchemaEntity89Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_89(payload)

@router.get("/entity-90", response_model=List[DashboardsSchemaEntity90Response])
def list_entities_90(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_90_list(skip=skip, limit=limit)

@router.get("/entity-90/{entity_id}", response_model=DashboardsSchemaEntity90Response)
def get_entity_90(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_90_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 90 not found")
    return res

@router.post("/entity-90", response_model=DashboardsSchemaEntity90Response, status_code=201)
def create_entity_90(payload: DashboardsSchemaEntity90Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_90(payload)

@router.get("/entity-91", response_model=List[DashboardsSchemaEntity91Response])
def list_entities_91(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_91_list(skip=skip, limit=limit)

@router.get("/entity-91/{entity_id}", response_model=DashboardsSchemaEntity91Response)
def get_entity_91(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_91_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 91 not found")
    return res

@router.post("/entity-91", response_model=DashboardsSchemaEntity91Response, status_code=201)
def create_entity_91(payload: DashboardsSchemaEntity91Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_91(payload)

@router.get("/entity-92", response_model=List[DashboardsSchemaEntity92Response])
def list_entities_92(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_92_list(skip=skip, limit=limit)

@router.get("/entity-92/{entity_id}", response_model=DashboardsSchemaEntity92Response)
def get_entity_92(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_92_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 92 not found")
    return res

@router.post("/entity-92", response_model=DashboardsSchemaEntity92Response, status_code=201)
def create_entity_92(payload: DashboardsSchemaEntity92Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_92(payload)

@router.get("/entity-93", response_model=List[DashboardsSchemaEntity93Response])
def list_entities_93(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_93_list(skip=skip, limit=limit)

@router.get("/entity-93/{entity_id}", response_model=DashboardsSchemaEntity93Response)
def get_entity_93(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_93_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 93 not found")
    return res

@router.post("/entity-93", response_model=DashboardsSchemaEntity93Response, status_code=201)
def create_entity_93(payload: DashboardsSchemaEntity93Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_93(payload)

@router.get("/entity-94", response_model=List[DashboardsSchemaEntity94Response])
def list_entities_94(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_94_list(skip=skip, limit=limit)

@router.get("/entity-94/{entity_id}", response_model=DashboardsSchemaEntity94Response)
def get_entity_94(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_94_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 94 not found")
    return res

@router.post("/entity-94", response_model=DashboardsSchemaEntity94Response, status_code=201)
def create_entity_94(payload: DashboardsSchemaEntity94Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_94(payload)

@router.get("/entity-95", response_model=List[DashboardsSchemaEntity95Response])
def list_entities_95(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_95_list(skip=skip, limit=limit)

@router.get("/entity-95/{entity_id}", response_model=DashboardsSchemaEntity95Response)
def get_entity_95(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_95_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 95 not found")
    return res

@router.post("/entity-95", response_model=DashboardsSchemaEntity95Response, status_code=201)
def create_entity_95(payload: DashboardsSchemaEntity95Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_95(payload)

@router.get("/entity-96", response_model=List[DashboardsSchemaEntity96Response])
def list_entities_96(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_96_list(skip=skip, limit=limit)

@router.get("/entity-96/{entity_id}", response_model=DashboardsSchemaEntity96Response)
def get_entity_96(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_96_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 96 not found")
    return res

@router.post("/entity-96", response_model=DashboardsSchemaEntity96Response, status_code=201)
def create_entity_96(payload: DashboardsSchemaEntity96Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_96(payload)

@router.get("/entity-97", response_model=List[DashboardsSchemaEntity97Response])
def list_entities_97(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_97_list(skip=skip, limit=limit)

@router.get("/entity-97/{entity_id}", response_model=DashboardsSchemaEntity97Response)
def get_entity_97(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_97_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 97 not found")
    return res

@router.post("/entity-97", response_model=DashboardsSchemaEntity97Response, status_code=201)
def create_entity_97(payload: DashboardsSchemaEntity97Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_97(payload)

@router.get("/entity-98", response_model=List[DashboardsSchemaEntity98Response])
def list_entities_98(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_98_list(skip=skip, limit=limit)

@router.get("/entity-98/{entity_id}", response_model=DashboardsSchemaEntity98Response)
def get_entity_98(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_98_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 98 not found")
    return res

@router.post("/entity-98", response_model=DashboardsSchemaEntity98Response, status_code=201)
def create_entity_98(payload: DashboardsSchemaEntity98Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_98(payload)

@router.get("/entity-99", response_model=List[DashboardsSchemaEntity99Response])
def list_entities_99(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_99_list(skip=skip, limit=limit)

@router.get("/entity-99/{entity_id}", response_model=DashboardsSchemaEntity99Response)
def get_entity_99(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_99_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 99 not found")
    return res

@router.post("/entity-99", response_model=DashboardsSchemaEntity99Response, status_code=201)
def create_entity_99(payload: DashboardsSchemaEntity99Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_99(payload)

@router.get("/entity-100", response_model=List[DashboardsSchemaEntity100Response])
def list_entities_100(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_100_list(skip=skip, limit=limit)

@router.get("/entity-100/{entity_id}", response_model=DashboardsSchemaEntity100Response)
def get_entity_100(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_100_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 100 not found")
    return res

@router.post("/entity-100", response_model=DashboardsSchemaEntity100Response, status_code=201)
def create_entity_100(payload: DashboardsSchemaEntity100Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_100(payload)

@router.get("/entity-101", response_model=List[DashboardsSchemaEntity101Response])
def list_entities_101(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_101_list(skip=skip, limit=limit)

@router.get("/entity-101/{entity_id}", response_model=DashboardsSchemaEntity101Response)
def get_entity_101(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_101_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 101 not found")
    return res

@router.post("/entity-101", response_model=DashboardsSchemaEntity101Response, status_code=201)
def create_entity_101(payload: DashboardsSchemaEntity101Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_101(payload)

@router.get("/entity-102", response_model=List[DashboardsSchemaEntity102Response])
def list_entities_102(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_102_list(skip=skip, limit=limit)

@router.get("/entity-102/{entity_id}", response_model=DashboardsSchemaEntity102Response)
def get_entity_102(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_102_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 102 not found")
    return res

@router.post("/entity-102", response_model=DashboardsSchemaEntity102Response, status_code=201)
def create_entity_102(payload: DashboardsSchemaEntity102Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_102(payload)

@router.get("/entity-103", response_model=List[DashboardsSchemaEntity103Response])
def list_entities_103(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_103_list(skip=skip, limit=limit)

@router.get("/entity-103/{entity_id}", response_model=DashboardsSchemaEntity103Response)
def get_entity_103(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_103_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 103 not found")
    return res

@router.post("/entity-103", response_model=DashboardsSchemaEntity103Response, status_code=201)
def create_entity_103(payload: DashboardsSchemaEntity103Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_103(payload)

@router.get("/entity-104", response_model=List[DashboardsSchemaEntity104Response])
def list_entities_104(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_104_list(skip=skip, limit=limit)

@router.get("/entity-104/{entity_id}", response_model=DashboardsSchemaEntity104Response)
def get_entity_104(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_104_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 104 not found")
    return res

@router.post("/entity-104", response_model=DashboardsSchemaEntity104Response, status_code=201)
def create_entity_104(payload: DashboardsSchemaEntity104Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_104(payload)

@router.get("/entity-105", response_model=List[DashboardsSchemaEntity105Response])
def list_entities_105(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_105_list(skip=skip, limit=limit)

@router.get("/entity-105/{entity_id}", response_model=DashboardsSchemaEntity105Response)
def get_entity_105(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_105_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 105 not found")
    return res

@router.post("/entity-105", response_model=DashboardsSchemaEntity105Response, status_code=201)
def create_entity_105(payload: DashboardsSchemaEntity105Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_105(payload)

@router.get("/entity-106", response_model=List[DashboardsSchemaEntity106Response])
def list_entities_106(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_106_list(skip=skip, limit=limit)

@router.get("/entity-106/{entity_id}", response_model=DashboardsSchemaEntity106Response)
def get_entity_106(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_106_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 106 not found")
    return res

@router.post("/entity-106", response_model=DashboardsSchemaEntity106Response, status_code=201)
def create_entity_106(payload: DashboardsSchemaEntity106Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_106(payload)

@router.get("/entity-107", response_model=List[DashboardsSchemaEntity107Response])
def list_entities_107(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_107_list(skip=skip, limit=limit)

@router.get("/entity-107/{entity_id}", response_model=DashboardsSchemaEntity107Response)
def get_entity_107(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_107_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 107 not found")
    return res

@router.post("/entity-107", response_model=DashboardsSchemaEntity107Response, status_code=201)
def create_entity_107(payload: DashboardsSchemaEntity107Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_107(payload)

@router.get("/entity-108", response_model=List[DashboardsSchemaEntity108Response])
def list_entities_108(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_108_list(skip=skip, limit=limit)

@router.get("/entity-108/{entity_id}", response_model=DashboardsSchemaEntity108Response)
def get_entity_108(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_108_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 108 not found")
    return res

@router.post("/entity-108", response_model=DashboardsSchemaEntity108Response, status_code=201)
def create_entity_108(payload: DashboardsSchemaEntity108Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_108(payload)

@router.get("/entity-109", response_model=List[DashboardsSchemaEntity109Response])
def list_entities_109(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_109_list(skip=skip, limit=limit)

@router.get("/entity-109/{entity_id}", response_model=DashboardsSchemaEntity109Response)
def get_entity_109(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_109_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 109 not found")
    return res

@router.post("/entity-109", response_model=DashboardsSchemaEntity109Response, status_code=201)
def create_entity_109(payload: DashboardsSchemaEntity109Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_109(payload)

@router.get("/entity-110", response_model=List[DashboardsSchemaEntity110Response])
def list_entities_110(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_110_list(skip=skip, limit=limit)

@router.get("/entity-110/{entity_id}", response_model=DashboardsSchemaEntity110Response)
def get_entity_110(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_110_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 110 not found")
    return res

@router.post("/entity-110", response_model=DashboardsSchemaEntity110Response, status_code=201)
def create_entity_110(payload: DashboardsSchemaEntity110Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_110(payload)

@router.get("/entity-111", response_model=List[DashboardsSchemaEntity111Response])
def list_entities_111(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_111_list(skip=skip, limit=limit)

@router.get("/entity-111/{entity_id}", response_model=DashboardsSchemaEntity111Response)
def get_entity_111(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_111_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 111 not found")
    return res

@router.post("/entity-111", response_model=DashboardsSchemaEntity111Response, status_code=201)
def create_entity_111(payload: DashboardsSchemaEntity111Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_111(payload)

@router.get("/entity-112", response_model=List[DashboardsSchemaEntity112Response])
def list_entities_112(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_112_list(skip=skip, limit=limit)

@router.get("/entity-112/{entity_id}", response_model=DashboardsSchemaEntity112Response)
def get_entity_112(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_112_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 112 not found")
    return res

@router.post("/entity-112", response_model=DashboardsSchemaEntity112Response, status_code=201)
def create_entity_112(payload: DashboardsSchemaEntity112Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_112(payload)

@router.get("/entity-113", response_model=List[DashboardsSchemaEntity113Response])
def list_entities_113(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_113_list(skip=skip, limit=limit)

@router.get("/entity-113/{entity_id}", response_model=DashboardsSchemaEntity113Response)
def get_entity_113(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_113_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 113 not found")
    return res

@router.post("/entity-113", response_model=DashboardsSchemaEntity113Response, status_code=201)
def create_entity_113(payload: DashboardsSchemaEntity113Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_113(payload)

@router.get("/entity-114", response_model=List[DashboardsSchemaEntity114Response])
def list_entities_114(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_114_list(skip=skip, limit=limit)

@router.get("/entity-114/{entity_id}", response_model=DashboardsSchemaEntity114Response)
def get_entity_114(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_114_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 114 not found")
    return res

@router.post("/entity-114", response_model=DashboardsSchemaEntity114Response, status_code=201)
def create_entity_114(payload: DashboardsSchemaEntity114Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_114(payload)

@router.get("/entity-115", response_model=List[DashboardsSchemaEntity115Response])
def list_entities_115(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_115_list(skip=skip, limit=limit)

@router.get("/entity-115/{entity_id}", response_model=DashboardsSchemaEntity115Response)
def get_entity_115(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_115_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 115 not found")
    return res

@router.post("/entity-115", response_model=DashboardsSchemaEntity115Response, status_code=201)
def create_entity_115(payload: DashboardsSchemaEntity115Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_115(payload)

@router.get("/entity-116", response_model=List[DashboardsSchemaEntity116Response])
def list_entities_116(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_116_list(skip=skip, limit=limit)

@router.get("/entity-116/{entity_id}", response_model=DashboardsSchemaEntity116Response)
def get_entity_116(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_116_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 116 not found")
    return res

@router.post("/entity-116", response_model=DashboardsSchemaEntity116Response, status_code=201)
def create_entity_116(payload: DashboardsSchemaEntity116Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_116(payload)

@router.get("/entity-117", response_model=List[DashboardsSchemaEntity117Response])
def list_entities_117(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_117_list(skip=skip, limit=limit)

@router.get("/entity-117/{entity_id}", response_model=DashboardsSchemaEntity117Response)
def get_entity_117(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_117_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 117 not found")
    return res

@router.post("/entity-117", response_model=DashboardsSchemaEntity117Response, status_code=201)
def create_entity_117(payload: DashboardsSchemaEntity117Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_117(payload)

@router.get("/entity-118", response_model=List[DashboardsSchemaEntity118Response])
def list_entities_118(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_118_list(skip=skip, limit=limit)

@router.get("/entity-118/{entity_id}", response_model=DashboardsSchemaEntity118Response)
def get_entity_118(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_118_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 118 not found")
    return res

@router.post("/entity-118", response_model=DashboardsSchemaEntity118Response, status_code=201)
def create_entity_118(payload: DashboardsSchemaEntity118Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_118(payload)

@router.get("/entity-119", response_model=List[DashboardsSchemaEntity119Response])
def list_entities_119(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_119_list(skip=skip, limit=limit)

@router.get("/entity-119/{entity_id}", response_model=DashboardsSchemaEntity119Response)
def get_entity_119(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_119_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 119 not found")
    return res

@router.post("/entity-119", response_model=DashboardsSchemaEntity119Response, status_code=201)
def create_entity_119(payload: DashboardsSchemaEntity119Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_119(payload)

@router.get("/entity-120", response_model=List[DashboardsSchemaEntity120Response])
def list_entities_120(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_120_list(skip=skip, limit=limit)

@router.get("/entity-120/{entity_id}", response_model=DashboardsSchemaEntity120Response)
def get_entity_120(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_120_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 120 not found")
    return res

@router.post("/entity-120", response_model=DashboardsSchemaEntity120Response, status_code=201)
def create_entity_120(payload: DashboardsSchemaEntity120Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_120(payload)

@router.get("/entity-121", response_model=List[DashboardsSchemaEntity121Response])
def list_entities_121(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_121_list(skip=skip, limit=limit)

@router.get("/entity-121/{entity_id}", response_model=DashboardsSchemaEntity121Response)
def get_entity_121(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_121_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 121 not found")
    return res

@router.post("/entity-121", response_model=DashboardsSchemaEntity121Response, status_code=201)
def create_entity_121(payload: DashboardsSchemaEntity121Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_121(payload)

@router.get("/entity-122", response_model=List[DashboardsSchemaEntity122Response])
def list_entities_122(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_122_list(skip=skip, limit=limit)

@router.get("/entity-122/{entity_id}", response_model=DashboardsSchemaEntity122Response)
def get_entity_122(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_122_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 122 not found")
    return res

@router.post("/entity-122", response_model=DashboardsSchemaEntity122Response, status_code=201)
def create_entity_122(payload: DashboardsSchemaEntity122Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_122(payload)

@router.get("/entity-123", response_model=List[DashboardsSchemaEntity123Response])
def list_entities_123(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_123_list(skip=skip, limit=limit)

@router.get("/entity-123/{entity_id}", response_model=DashboardsSchemaEntity123Response)
def get_entity_123(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_123_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 123 not found")
    return res

@router.post("/entity-123", response_model=DashboardsSchemaEntity123Response, status_code=201)
def create_entity_123(payload: DashboardsSchemaEntity123Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_123(payload)

@router.get("/entity-124", response_model=List[DashboardsSchemaEntity124Response])
def list_entities_124(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_124_list(skip=skip, limit=limit)

@router.get("/entity-124/{entity_id}", response_model=DashboardsSchemaEntity124Response)
def get_entity_124(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_124_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 124 not found")
    return res

@router.post("/entity-124", response_model=DashboardsSchemaEntity124Response, status_code=201)
def create_entity_124(payload: DashboardsSchemaEntity124Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_124(payload)

@router.get("/entity-125", response_model=List[DashboardsSchemaEntity125Response])
def list_entities_125(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_125_list(skip=skip, limit=limit)

@router.get("/entity-125/{entity_id}", response_model=DashboardsSchemaEntity125Response)
def get_entity_125(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_125_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 125 not found")
    return res

@router.post("/entity-125", response_model=DashboardsSchemaEntity125Response, status_code=201)
def create_entity_125(payload: DashboardsSchemaEntity125Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_125(payload)

@router.get("/entity-126", response_model=List[DashboardsSchemaEntity126Response])
def list_entities_126(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_126_list(skip=skip, limit=limit)

@router.get("/entity-126/{entity_id}", response_model=DashboardsSchemaEntity126Response)
def get_entity_126(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_126_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 126 not found")
    return res

@router.post("/entity-126", response_model=DashboardsSchemaEntity126Response, status_code=201)
def create_entity_126(payload: DashboardsSchemaEntity126Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_126(payload)

@router.get("/entity-127", response_model=List[DashboardsSchemaEntity127Response])
def list_entities_127(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_127_list(skip=skip, limit=limit)

@router.get("/entity-127/{entity_id}", response_model=DashboardsSchemaEntity127Response)
def get_entity_127(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_127_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 127 not found")
    return res

@router.post("/entity-127", response_model=DashboardsSchemaEntity127Response, status_code=201)
def create_entity_127(payload: DashboardsSchemaEntity127Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_127(payload)

@router.get("/entity-128", response_model=List[DashboardsSchemaEntity128Response])
def list_entities_128(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_128_list(skip=skip, limit=limit)

@router.get("/entity-128/{entity_id}", response_model=DashboardsSchemaEntity128Response)
def get_entity_128(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_128_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 128 not found")
    return res

@router.post("/entity-128", response_model=DashboardsSchemaEntity128Response, status_code=201)
def create_entity_128(payload: DashboardsSchemaEntity128Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_128(payload)

@router.get("/entity-129", response_model=List[DashboardsSchemaEntity129Response])
def list_entities_129(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_129_list(skip=skip, limit=limit)

@router.get("/entity-129/{entity_id}", response_model=DashboardsSchemaEntity129Response)
def get_entity_129(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_129_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 129 not found")
    return res

@router.post("/entity-129", response_model=DashboardsSchemaEntity129Response, status_code=201)
def create_entity_129(payload: DashboardsSchemaEntity129Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_129(payload)

@router.get("/entity-130", response_model=List[DashboardsSchemaEntity130Response])
def list_entities_130(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_130_list(skip=skip, limit=limit)

@router.get("/entity-130/{entity_id}", response_model=DashboardsSchemaEntity130Response)
def get_entity_130(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_130_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 130 not found")
    return res

@router.post("/entity-130", response_model=DashboardsSchemaEntity130Response, status_code=201)
def create_entity_130(payload: DashboardsSchemaEntity130Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_130(payload)

@router.get("/entity-131", response_model=List[DashboardsSchemaEntity131Response])
def list_entities_131(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_131_list(skip=skip, limit=limit)

@router.get("/entity-131/{entity_id}", response_model=DashboardsSchemaEntity131Response)
def get_entity_131(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_131_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 131 not found")
    return res

@router.post("/entity-131", response_model=DashboardsSchemaEntity131Response, status_code=201)
def create_entity_131(payload: DashboardsSchemaEntity131Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_131(payload)

@router.get("/entity-132", response_model=List[DashboardsSchemaEntity132Response])
def list_entities_132(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_132_list(skip=skip, limit=limit)

@router.get("/entity-132/{entity_id}", response_model=DashboardsSchemaEntity132Response)
def get_entity_132(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_132_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 132 not found")
    return res

@router.post("/entity-132", response_model=DashboardsSchemaEntity132Response, status_code=201)
def create_entity_132(payload: DashboardsSchemaEntity132Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_132(payload)

@router.get("/entity-133", response_model=List[DashboardsSchemaEntity133Response])
def list_entities_133(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_133_list(skip=skip, limit=limit)

@router.get("/entity-133/{entity_id}", response_model=DashboardsSchemaEntity133Response)
def get_entity_133(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_133_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 133 not found")
    return res

@router.post("/entity-133", response_model=DashboardsSchemaEntity133Response, status_code=201)
def create_entity_133(payload: DashboardsSchemaEntity133Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_133(payload)

@router.get("/entity-134", response_model=List[DashboardsSchemaEntity134Response])
def list_entities_134(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_134_list(skip=skip, limit=limit)

@router.get("/entity-134/{entity_id}", response_model=DashboardsSchemaEntity134Response)
def get_entity_134(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_134_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 134 not found")
    return res

@router.post("/entity-134", response_model=DashboardsSchemaEntity134Response, status_code=201)
def create_entity_134(payload: DashboardsSchemaEntity134Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_134(payload)

@router.get("/entity-135", response_model=List[DashboardsSchemaEntity135Response])
def list_entities_135(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_135_list(skip=skip, limit=limit)

@router.get("/entity-135/{entity_id}", response_model=DashboardsSchemaEntity135Response)
def get_entity_135(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_135_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 135 not found")
    return res

@router.post("/entity-135", response_model=DashboardsSchemaEntity135Response, status_code=201)
def create_entity_135(payload: DashboardsSchemaEntity135Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_135(payload)

@router.get("/entity-136", response_model=List[DashboardsSchemaEntity136Response])
def list_entities_136(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_136_list(skip=skip, limit=limit)

@router.get("/entity-136/{entity_id}", response_model=DashboardsSchemaEntity136Response)
def get_entity_136(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_136_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 136 not found")
    return res

@router.post("/entity-136", response_model=DashboardsSchemaEntity136Response, status_code=201)
def create_entity_136(payload: DashboardsSchemaEntity136Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_136(payload)

@router.get("/entity-137", response_model=List[DashboardsSchemaEntity137Response])
def list_entities_137(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_137_list(skip=skip, limit=limit)

@router.get("/entity-137/{entity_id}", response_model=DashboardsSchemaEntity137Response)
def get_entity_137(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_137_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 137 not found")
    return res

@router.post("/entity-137", response_model=DashboardsSchemaEntity137Response, status_code=201)
def create_entity_137(payload: DashboardsSchemaEntity137Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_137(payload)

@router.get("/entity-138", response_model=List[DashboardsSchemaEntity138Response])
def list_entities_138(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_138_list(skip=skip, limit=limit)

@router.get("/entity-138/{entity_id}", response_model=DashboardsSchemaEntity138Response)
def get_entity_138(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_138_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 138 not found")
    return res

@router.post("/entity-138", response_model=DashboardsSchemaEntity138Response, status_code=201)
def create_entity_138(payload: DashboardsSchemaEntity138Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_138(payload)

@router.get("/entity-139", response_model=List[DashboardsSchemaEntity139Response])
def list_entities_139(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_139_list(skip=skip, limit=limit)

@router.get("/entity-139/{entity_id}", response_model=DashboardsSchemaEntity139Response)
def get_entity_139(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_139_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 139 not found")
    return res

@router.post("/entity-139", response_model=DashboardsSchemaEntity139Response, status_code=201)
def create_entity_139(payload: DashboardsSchemaEntity139Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_139(payload)

@router.get("/entity-140", response_model=List[DashboardsSchemaEntity140Response])
def list_entities_140(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_140_list(skip=skip, limit=limit)

@router.get("/entity-140/{entity_id}", response_model=DashboardsSchemaEntity140Response)
def get_entity_140(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_140_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 140 not found")
    return res

@router.post("/entity-140", response_model=DashboardsSchemaEntity140Response, status_code=201)
def create_entity_140(payload: DashboardsSchemaEntity140Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_140(payload)

@router.get("/entity-141", response_model=List[DashboardsSchemaEntity141Response])
def list_entities_141(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_141_list(skip=skip, limit=limit)

@router.get("/entity-141/{entity_id}", response_model=DashboardsSchemaEntity141Response)
def get_entity_141(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_141_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 141 not found")
    return res

@router.post("/entity-141", response_model=DashboardsSchemaEntity141Response, status_code=201)
def create_entity_141(payload: DashboardsSchemaEntity141Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_141(payload)

@router.get("/entity-142", response_model=List[DashboardsSchemaEntity142Response])
def list_entities_142(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_142_list(skip=skip, limit=limit)

@router.get("/entity-142/{entity_id}", response_model=DashboardsSchemaEntity142Response)
def get_entity_142(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_142_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 142 not found")
    return res

@router.post("/entity-142", response_model=DashboardsSchemaEntity142Response, status_code=201)
def create_entity_142(payload: DashboardsSchemaEntity142Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_142(payload)

@router.get("/entity-143", response_model=List[DashboardsSchemaEntity143Response])
def list_entities_143(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_143_list(skip=skip, limit=limit)

@router.get("/entity-143/{entity_id}", response_model=DashboardsSchemaEntity143Response)
def get_entity_143(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_143_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 143 not found")
    return res

@router.post("/entity-143", response_model=DashboardsSchemaEntity143Response, status_code=201)
def create_entity_143(payload: DashboardsSchemaEntity143Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_143(payload)

@router.get("/entity-144", response_model=List[DashboardsSchemaEntity144Response])
def list_entities_144(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_144_list(skip=skip, limit=limit)

@router.get("/entity-144/{entity_id}", response_model=DashboardsSchemaEntity144Response)
def get_entity_144(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_144_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 144 not found")
    return res

@router.post("/entity-144", response_model=DashboardsSchemaEntity144Response, status_code=201)
def create_entity_144(payload: DashboardsSchemaEntity144Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_144(payload)

@router.get("/entity-145", response_model=List[DashboardsSchemaEntity145Response])
def list_entities_145(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_145_list(skip=skip, limit=limit)

@router.get("/entity-145/{entity_id}", response_model=DashboardsSchemaEntity145Response)
def get_entity_145(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_145_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 145 not found")
    return res

@router.post("/entity-145", response_model=DashboardsSchemaEntity145Response, status_code=201)
def create_entity_145(payload: DashboardsSchemaEntity145Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_145(payload)

@router.get("/entity-146", response_model=List[DashboardsSchemaEntity146Response])
def list_entities_146(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_146_list(skip=skip, limit=limit)

@router.get("/entity-146/{entity_id}", response_model=DashboardsSchemaEntity146Response)
def get_entity_146(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_146_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 146 not found")
    return res

@router.post("/entity-146", response_model=DashboardsSchemaEntity146Response, status_code=201)
def create_entity_146(payload: DashboardsSchemaEntity146Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_146(payload)

@router.get("/entity-147", response_model=List[DashboardsSchemaEntity147Response])
def list_entities_147(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_147_list(skip=skip, limit=limit)

@router.get("/entity-147/{entity_id}", response_model=DashboardsSchemaEntity147Response)
def get_entity_147(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_147_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 147 not found")
    return res

@router.post("/entity-147", response_model=DashboardsSchemaEntity147Response, status_code=201)
def create_entity_147(payload: DashboardsSchemaEntity147Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_147(payload)

@router.get("/entity-148", response_model=List[DashboardsSchemaEntity148Response])
def list_entities_148(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_148_list(skip=skip, limit=limit)

@router.get("/entity-148/{entity_id}", response_model=DashboardsSchemaEntity148Response)
def get_entity_148(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_148_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 148 not found")
    return res

@router.post("/entity-148", response_model=DashboardsSchemaEntity148Response, status_code=201)
def create_entity_148(payload: DashboardsSchemaEntity148Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_148(payload)

@router.get("/entity-149", response_model=List[DashboardsSchemaEntity149Response])
def list_entities_149(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_149_list(skip=skip, limit=limit)

@router.get("/entity-149/{entity_id}", response_model=DashboardsSchemaEntity149Response)
def get_entity_149(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_149_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 149 not found")
    return res

@router.post("/entity-149", response_model=DashboardsSchemaEntity149Response, status_code=201)
def create_entity_149(payload: DashboardsSchemaEntity149Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_149(payload)

@router.get("/entity-150", response_model=List[DashboardsSchemaEntity150Response])
def list_entities_150(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_150_list(skip=skip, limit=limit)

@router.get("/entity-150/{entity_id}", response_model=DashboardsSchemaEntity150Response)
def get_entity_150(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_150_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 150 not found")
    return res

@router.post("/entity-150", response_model=DashboardsSchemaEntity150Response, status_code=201)
def create_entity_150(payload: DashboardsSchemaEntity150Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_150(payload)

@router.get("/entity-151", response_model=List[DashboardsSchemaEntity151Response])
def list_entities_151(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_151_list(skip=skip, limit=limit)

@router.get("/entity-151/{entity_id}", response_model=DashboardsSchemaEntity151Response)
def get_entity_151(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_151_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 151 not found")
    return res

@router.post("/entity-151", response_model=DashboardsSchemaEntity151Response, status_code=201)
def create_entity_151(payload: DashboardsSchemaEntity151Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_151(payload)

@router.get("/entity-152", response_model=List[DashboardsSchemaEntity152Response])
def list_entities_152(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_152_list(skip=skip, limit=limit)

@router.get("/entity-152/{entity_id}", response_model=DashboardsSchemaEntity152Response)
def get_entity_152(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_152_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 152 not found")
    return res

@router.post("/entity-152", response_model=DashboardsSchemaEntity152Response, status_code=201)
def create_entity_152(payload: DashboardsSchemaEntity152Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_152(payload)

@router.get("/entity-153", response_model=List[DashboardsSchemaEntity153Response])
def list_entities_153(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_153_list(skip=skip, limit=limit)

@router.get("/entity-153/{entity_id}", response_model=DashboardsSchemaEntity153Response)
def get_entity_153(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_153_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 153 not found")
    return res

@router.post("/entity-153", response_model=DashboardsSchemaEntity153Response, status_code=201)
def create_entity_153(payload: DashboardsSchemaEntity153Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_153(payload)

@router.get("/entity-154", response_model=List[DashboardsSchemaEntity154Response])
def list_entities_154(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_154_list(skip=skip, limit=limit)

@router.get("/entity-154/{entity_id}", response_model=DashboardsSchemaEntity154Response)
def get_entity_154(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_154_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 154 not found")
    return res

@router.post("/entity-154", response_model=DashboardsSchemaEntity154Response, status_code=201)
def create_entity_154(payload: DashboardsSchemaEntity154Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_154(payload)

@router.get("/entity-155", response_model=List[DashboardsSchemaEntity155Response])
def list_entities_155(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_155_list(skip=skip, limit=limit)

@router.get("/entity-155/{entity_id}", response_model=DashboardsSchemaEntity155Response)
def get_entity_155(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_155_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 155 not found")
    return res

@router.post("/entity-155", response_model=DashboardsSchemaEntity155Response, status_code=201)
def create_entity_155(payload: DashboardsSchemaEntity155Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_155(payload)

@router.get("/entity-156", response_model=List[DashboardsSchemaEntity156Response])
def list_entities_156(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_156_list(skip=skip, limit=limit)

@router.get("/entity-156/{entity_id}", response_model=DashboardsSchemaEntity156Response)
def get_entity_156(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_156_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 156 not found")
    return res

@router.post("/entity-156", response_model=DashboardsSchemaEntity156Response, status_code=201)
def create_entity_156(payload: DashboardsSchemaEntity156Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_156(payload)

@router.get("/entity-157", response_model=List[DashboardsSchemaEntity157Response])
def list_entities_157(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_157_list(skip=skip, limit=limit)

@router.get("/entity-157/{entity_id}", response_model=DashboardsSchemaEntity157Response)
def get_entity_157(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_157_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 157 not found")
    return res

@router.post("/entity-157", response_model=DashboardsSchemaEntity157Response, status_code=201)
def create_entity_157(payload: DashboardsSchemaEntity157Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_157(payload)

@router.get("/entity-158", response_model=List[DashboardsSchemaEntity158Response])
def list_entities_158(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_158_list(skip=skip, limit=limit)

@router.get("/entity-158/{entity_id}", response_model=DashboardsSchemaEntity158Response)
def get_entity_158(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_158_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 158 not found")
    return res

@router.post("/entity-158", response_model=DashboardsSchemaEntity158Response, status_code=201)
def create_entity_158(payload: DashboardsSchemaEntity158Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_158(payload)

@router.get("/entity-159", response_model=List[DashboardsSchemaEntity159Response])
def list_entities_159(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_159_list(skip=skip, limit=limit)

@router.get("/entity-159/{entity_id}", response_model=DashboardsSchemaEntity159Response)
def get_entity_159(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_159_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 159 not found")
    return res

@router.post("/entity-159", response_model=DashboardsSchemaEntity159Response, status_code=201)
def create_entity_159(payload: DashboardsSchemaEntity159Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_159(payload)

@router.get("/entity-160", response_model=List[DashboardsSchemaEntity160Response])
def list_entities_160(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_160_list(skip=skip, limit=limit)

@router.get("/entity-160/{entity_id}", response_model=DashboardsSchemaEntity160Response)
def get_entity_160(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_160_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 160 not found")
    return res

@router.post("/entity-160", response_model=DashboardsSchemaEntity160Response, status_code=201)
def create_entity_160(payload: DashboardsSchemaEntity160Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_160(payload)

@router.get("/entity-161", response_model=List[DashboardsSchemaEntity161Response])
def list_entities_161(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_161_list(skip=skip, limit=limit)

@router.get("/entity-161/{entity_id}", response_model=DashboardsSchemaEntity161Response)
def get_entity_161(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_161_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 161 not found")
    return res

@router.post("/entity-161", response_model=DashboardsSchemaEntity161Response, status_code=201)
def create_entity_161(payload: DashboardsSchemaEntity161Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_161(payload)

@router.get("/entity-162", response_model=List[DashboardsSchemaEntity162Response])
def list_entities_162(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_162_list(skip=skip, limit=limit)

@router.get("/entity-162/{entity_id}", response_model=DashboardsSchemaEntity162Response)
def get_entity_162(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_162_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 162 not found")
    return res

@router.post("/entity-162", response_model=DashboardsSchemaEntity162Response, status_code=201)
def create_entity_162(payload: DashboardsSchemaEntity162Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_162(payload)

@router.get("/entity-163", response_model=List[DashboardsSchemaEntity163Response])
def list_entities_163(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_163_list(skip=skip, limit=limit)

@router.get("/entity-163/{entity_id}", response_model=DashboardsSchemaEntity163Response)
def get_entity_163(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_163_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 163 not found")
    return res

@router.post("/entity-163", response_model=DashboardsSchemaEntity163Response, status_code=201)
def create_entity_163(payload: DashboardsSchemaEntity163Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_163(payload)

@router.get("/entity-164", response_model=List[DashboardsSchemaEntity164Response])
def list_entities_164(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_164_list(skip=skip, limit=limit)

@router.get("/entity-164/{entity_id}", response_model=DashboardsSchemaEntity164Response)
def get_entity_164(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_164_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 164 not found")
    return res

@router.post("/entity-164", response_model=DashboardsSchemaEntity164Response, status_code=201)
def create_entity_164(payload: DashboardsSchemaEntity164Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_164(payload)

@router.get("/entity-165", response_model=List[DashboardsSchemaEntity165Response])
def list_entities_165(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_165_list(skip=skip, limit=limit)

@router.get("/entity-165/{entity_id}", response_model=DashboardsSchemaEntity165Response)
def get_entity_165(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_165_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 165 not found")
    return res

@router.post("/entity-165", response_model=DashboardsSchemaEntity165Response, status_code=201)
def create_entity_165(payload: DashboardsSchemaEntity165Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_165(payload)

@router.get("/entity-166", response_model=List[DashboardsSchemaEntity166Response])
def list_entities_166(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_166_list(skip=skip, limit=limit)

@router.get("/entity-166/{entity_id}", response_model=DashboardsSchemaEntity166Response)
def get_entity_166(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_166_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 166 not found")
    return res

@router.post("/entity-166", response_model=DashboardsSchemaEntity166Response, status_code=201)
def create_entity_166(payload: DashboardsSchemaEntity166Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_166(payload)

@router.get("/entity-167", response_model=List[DashboardsSchemaEntity167Response])
def list_entities_167(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_167_list(skip=skip, limit=limit)

@router.get("/entity-167/{entity_id}", response_model=DashboardsSchemaEntity167Response)
def get_entity_167(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_167_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 167 not found")
    return res

@router.post("/entity-167", response_model=DashboardsSchemaEntity167Response, status_code=201)
def create_entity_167(payload: DashboardsSchemaEntity167Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_167(payload)

@router.get("/entity-168", response_model=List[DashboardsSchemaEntity168Response])
def list_entities_168(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_168_list(skip=skip, limit=limit)

@router.get("/entity-168/{entity_id}", response_model=DashboardsSchemaEntity168Response)
def get_entity_168(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_168_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 168 not found")
    return res

@router.post("/entity-168", response_model=DashboardsSchemaEntity168Response, status_code=201)
def create_entity_168(payload: DashboardsSchemaEntity168Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_168(payload)

@router.get("/entity-169", response_model=List[DashboardsSchemaEntity169Response])
def list_entities_169(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_169_list(skip=skip, limit=limit)

@router.get("/entity-169/{entity_id}", response_model=DashboardsSchemaEntity169Response)
def get_entity_169(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_169_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 169 not found")
    return res

@router.post("/entity-169", response_model=DashboardsSchemaEntity169Response, status_code=201)
def create_entity_169(payload: DashboardsSchemaEntity169Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_169(payload)

@router.get("/entity-170", response_model=List[DashboardsSchemaEntity170Response])
def list_entities_170(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_170_list(skip=skip, limit=limit)

@router.get("/entity-170/{entity_id}", response_model=DashboardsSchemaEntity170Response)
def get_entity_170(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_170_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 170 not found")
    return res

@router.post("/entity-170", response_model=DashboardsSchemaEntity170Response, status_code=201)
def create_entity_170(payload: DashboardsSchemaEntity170Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_170(payload)

@router.get("/entity-171", response_model=List[DashboardsSchemaEntity171Response])
def list_entities_171(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_171_list(skip=skip, limit=limit)

@router.get("/entity-171/{entity_id}", response_model=DashboardsSchemaEntity171Response)
def get_entity_171(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_171_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 171 not found")
    return res

@router.post("/entity-171", response_model=DashboardsSchemaEntity171Response, status_code=201)
def create_entity_171(payload: DashboardsSchemaEntity171Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_171(payload)

@router.get("/entity-172", response_model=List[DashboardsSchemaEntity172Response])
def list_entities_172(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_172_list(skip=skip, limit=limit)

@router.get("/entity-172/{entity_id}", response_model=DashboardsSchemaEntity172Response)
def get_entity_172(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_172_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 172 not found")
    return res

@router.post("/entity-172", response_model=DashboardsSchemaEntity172Response, status_code=201)
def create_entity_172(payload: DashboardsSchemaEntity172Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_172(payload)

@router.get("/entity-173", response_model=List[DashboardsSchemaEntity173Response])
def list_entities_173(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_173_list(skip=skip, limit=limit)

@router.get("/entity-173/{entity_id}", response_model=DashboardsSchemaEntity173Response)
def get_entity_173(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_173_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 173 not found")
    return res

@router.post("/entity-173", response_model=DashboardsSchemaEntity173Response, status_code=201)
def create_entity_173(payload: DashboardsSchemaEntity173Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_173(payload)

@router.get("/entity-174", response_model=List[DashboardsSchemaEntity174Response])
def list_entities_174(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_174_list(skip=skip, limit=limit)

@router.get("/entity-174/{entity_id}", response_model=DashboardsSchemaEntity174Response)
def get_entity_174(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_174_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 174 not found")
    return res

@router.post("/entity-174", response_model=DashboardsSchemaEntity174Response, status_code=201)
def create_entity_174(payload: DashboardsSchemaEntity174Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_174(payload)

@router.get("/entity-175", response_model=List[DashboardsSchemaEntity175Response])
def list_entities_175(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_175_list(skip=skip, limit=limit)

@router.get("/entity-175/{entity_id}", response_model=DashboardsSchemaEntity175Response)
def get_entity_175(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_175_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 175 not found")
    return res

@router.post("/entity-175", response_model=DashboardsSchemaEntity175Response, status_code=201)
def create_entity_175(payload: DashboardsSchemaEntity175Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_175(payload)

@router.get("/entity-176", response_model=List[DashboardsSchemaEntity176Response])
def list_entities_176(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_176_list(skip=skip, limit=limit)

@router.get("/entity-176/{entity_id}", response_model=DashboardsSchemaEntity176Response)
def get_entity_176(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_176_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 176 not found")
    return res

@router.post("/entity-176", response_model=DashboardsSchemaEntity176Response, status_code=201)
def create_entity_176(payload: DashboardsSchemaEntity176Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_176(payload)

@router.get("/entity-177", response_model=List[DashboardsSchemaEntity177Response])
def list_entities_177(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_177_list(skip=skip, limit=limit)

@router.get("/entity-177/{entity_id}", response_model=DashboardsSchemaEntity177Response)
def get_entity_177(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_177_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 177 not found")
    return res

@router.post("/entity-177", response_model=DashboardsSchemaEntity177Response, status_code=201)
def create_entity_177(payload: DashboardsSchemaEntity177Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_177(payload)

@router.get("/entity-178", response_model=List[DashboardsSchemaEntity178Response])
def list_entities_178(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_178_list(skip=skip, limit=limit)

@router.get("/entity-178/{entity_id}", response_model=DashboardsSchemaEntity178Response)
def get_entity_178(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_178_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 178 not found")
    return res

@router.post("/entity-178", response_model=DashboardsSchemaEntity178Response, status_code=201)
def create_entity_178(payload: DashboardsSchemaEntity178Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_178(payload)

@router.get("/entity-179", response_model=List[DashboardsSchemaEntity179Response])
def list_entities_179(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_179_list(skip=skip, limit=limit)

@router.get("/entity-179/{entity_id}", response_model=DashboardsSchemaEntity179Response)
def get_entity_179(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_179_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 179 not found")
    return res

@router.post("/entity-179", response_model=DashboardsSchemaEntity179Response, status_code=201)
def create_entity_179(payload: DashboardsSchemaEntity179Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_179(payload)

@router.get("/entity-180", response_model=List[DashboardsSchemaEntity180Response])
def list_entities_180(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_180_list(skip=skip, limit=limit)

@router.get("/entity-180/{entity_id}", response_model=DashboardsSchemaEntity180Response)
def get_entity_180(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_180_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 180 not found")
    return res

@router.post("/entity-180", response_model=DashboardsSchemaEntity180Response, status_code=201)
def create_entity_180(payload: DashboardsSchemaEntity180Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_180(payload)

@router.get("/entity-181", response_model=List[DashboardsSchemaEntity181Response])
def list_entities_181(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_181_list(skip=skip, limit=limit)

@router.get("/entity-181/{entity_id}", response_model=DashboardsSchemaEntity181Response)
def get_entity_181(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_181_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 181 not found")
    return res

@router.post("/entity-181", response_model=DashboardsSchemaEntity181Response, status_code=201)
def create_entity_181(payload: DashboardsSchemaEntity181Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_181(payload)

@router.get("/entity-182", response_model=List[DashboardsSchemaEntity182Response])
def list_entities_182(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_182_list(skip=skip, limit=limit)

@router.get("/entity-182/{entity_id}", response_model=DashboardsSchemaEntity182Response)
def get_entity_182(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_182_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 182 not found")
    return res

@router.post("/entity-182", response_model=DashboardsSchemaEntity182Response, status_code=201)
def create_entity_182(payload: DashboardsSchemaEntity182Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_182(payload)

@router.get("/entity-183", response_model=List[DashboardsSchemaEntity183Response])
def list_entities_183(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_183_list(skip=skip, limit=limit)

@router.get("/entity-183/{entity_id}", response_model=DashboardsSchemaEntity183Response)
def get_entity_183(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_183_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 183 not found")
    return res

@router.post("/entity-183", response_model=DashboardsSchemaEntity183Response, status_code=201)
def create_entity_183(payload: DashboardsSchemaEntity183Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_183(payload)

@router.get("/entity-184", response_model=List[DashboardsSchemaEntity184Response])
def list_entities_184(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_184_list(skip=skip, limit=limit)

@router.get("/entity-184/{entity_id}", response_model=DashboardsSchemaEntity184Response)
def get_entity_184(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_184_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 184 not found")
    return res

@router.post("/entity-184", response_model=DashboardsSchemaEntity184Response, status_code=201)
def create_entity_184(payload: DashboardsSchemaEntity184Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_184(payload)

@router.get("/entity-185", response_model=List[DashboardsSchemaEntity185Response])
def list_entities_185(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_185_list(skip=skip, limit=limit)

@router.get("/entity-185/{entity_id}", response_model=DashboardsSchemaEntity185Response)
def get_entity_185(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_185_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 185 not found")
    return res

@router.post("/entity-185", response_model=DashboardsSchemaEntity185Response, status_code=201)
def create_entity_185(payload: DashboardsSchemaEntity185Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_185(payload)

@router.get("/entity-186", response_model=List[DashboardsSchemaEntity186Response])
def list_entities_186(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_186_list(skip=skip, limit=limit)

@router.get("/entity-186/{entity_id}", response_model=DashboardsSchemaEntity186Response)
def get_entity_186(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_186_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 186 not found")
    return res

@router.post("/entity-186", response_model=DashboardsSchemaEntity186Response, status_code=201)
def create_entity_186(payload: DashboardsSchemaEntity186Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_186(payload)

@router.get("/entity-187", response_model=List[DashboardsSchemaEntity187Response])
def list_entities_187(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_187_list(skip=skip, limit=limit)

@router.get("/entity-187/{entity_id}", response_model=DashboardsSchemaEntity187Response)
def get_entity_187(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_187_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 187 not found")
    return res

@router.post("/entity-187", response_model=DashboardsSchemaEntity187Response, status_code=201)
def create_entity_187(payload: DashboardsSchemaEntity187Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_187(payload)

@router.get("/entity-188", response_model=List[DashboardsSchemaEntity188Response])
def list_entities_188(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_188_list(skip=skip, limit=limit)

@router.get("/entity-188/{entity_id}", response_model=DashboardsSchemaEntity188Response)
def get_entity_188(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_188_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 188 not found")
    return res

@router.post("/entity-188", response_model=DashboardsSchemaEntity188Response, status_code=201)
def create_entity_188(payload: DashboardsSchemaEntity188Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_188(payload)

@router.get("/entity-189", response_model=List[DashboardsSchemaEntity189Response])
def list_entities_189(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_189_list(skip=skip, limit=limit)

@router.get("/entity-189/{entity_id}", response_model=DashboardsSchemaEntity189Response)
def get_entity_189(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_189_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 189 not found")
    return res

@router.post("/entity-189", response_model=DashboardsSchemaEntity189Response, status_code=201)
def create_entity_189(payload: DashboardsSchemaEntity189Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_189(payload)

@router.get("/entity-190", response_model=List[DashboardsSchemaEntity190Response])
def list_entities_190(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_190_list(skip=skip, limit=limit)

@router.get("/entity-190/{entity_id}", response_model=DashboardsSchemaEntity190Response)
def get_entity_190(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_190_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 190 not found")
    return res

@router.post("/entity-190", response_model=DashboardsSchemaEntity190Response, status_code=201)
def create_entity_190(payload: DashboardsSchemaEntity190Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_190(payload)

@router.get("/entity-191", response_model=List[DashboardsSchemaEntity191Response])
def list_entities_191(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_191_list(skip=skip, limit=limit)

@router.get("/entity-191/{entity_id}", response_model=DashboardsSchemaEntity191Response)
def get_entity_191(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_191_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 191 not found")
    return res

@router.post("/entity-191", response_model=DashboardsSchemaEntity191Response, status_code=201)
def create_entity_191(payload: DashboardsSchemaEntity191Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_191(payload)

@router.get("/entity-192", response_model=List[DashboardsSchemaEntity192Response])
def list_entities_192(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_192_list(skip=skip, limit=limit)

@router.get("/entity-192/{entity_id}", response_model=DashboardsSchemaEntity192Response)
def get_entity_192(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_192_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 192 not found")
    return res

@router.post("/entity-192", response_model=DashboardsSchemaEntity192Response, status_code=201)
def create_entity_192(payload: DashboardsSchemaEntity192Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_192(payload)

@router.get("/entity-193", response_model=List[DashboardsSchemaEntity193Response])
def list_entities_193(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_193_list(skip=skip, limit=limit)

@router.get("/entity-193/{entity_id}", response_model=DashboardsSchemaEntity193Response)
def get_entity_193(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_193_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 193 not found")
    return res

@router.post("/entity-193", response_model=DashboardsSchemaEntity193Response, status_code=201)
def create_entity_193(payload: DashboardsSchemaEntity193Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_193(payload)

@router.get("/entity-194", response_model=List[DashboardsSchemaEntity194Response])
def list_entities_194(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_194_list(skip=skip, limit=limit)

@router.get("/entity-194/{entity_id}", response_model=DashboardsSchemaEntity194Response)
def get_entity_194(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_194_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 194 not found")
    return res

@router.post("/entity-194", response_model=DashboardsSchemaEntity194Response, status_code=201)
def create_entity_194(payload: DashboardsSchemaEntity194Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_194(payload)

@router.get("/entity-195", response_model=List[DashboardsSchemaEntity195Response])
def list_entities_195(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_195_list(skip=skip, limit=limit)

@router.get("/entity-195/{entity_id}", response_model=DashboardsSchemaEntity195Response)
def get_entity_195(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_195_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 195 not found")
    return res

@router.post("/entity-195", response_model=DashboardsSchemaEntity195Response, status_code=201)
def create_entity_195(payload: DashboardsSchemaEntity195Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_195(payload)

@router.get("/entity-196", response_model=List[DashboardsSchemaEntity196Response])
def list_entities_196(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_196_list(skip=skip, limit=limit)

@router.get("/entity-196/{entity_id}", response_model=DashboardsSchemaEntity196Response)
def get_entity_196(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_196_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 196 not found")
    return res

@router.post("/entity-196", response_model=DashboardsSchemaEntity196Response, status_code=201)
def create_entity_196(payload: DashboardsSchemaEntity196Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_196(payload)

@router.get("/entity-197", response_model=List[DashboardsSchemaEntity197Response])
def list_entities_197(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_197_list(skip=skip, limit=limit)

@router.get("/entity-197/{entity_id}", response_model=DashboardsSchemaEntity197Response)
def get_entity_197(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_197_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 197 not found")
    return res

@router.post("/entity-197", response_model=DashboardsSchemaEntity197Response, status_code=201)
def create_entity_197(payload: DashboardsSchemaEntity197Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_197(payload)

@router.get("/entity-198", response_model=List[DashboardsSchemaEntity198Response])
def list_entities_198(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_198_list(skip=skip, limit=limit)

@router.get("/entity-198/{entity_id}", response_model=DashboardsSchemaEntity198Response)
def get_entity_198(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_198_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 198 not found")
    return res

@router.post("/entity-198", response_model=DashboardsSchemaEntity198Response, status_code=201)
def create_entity_198(payload: DashboardsSchemaEntity198Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_198(payload)

@router.get("/entity-199", response_model=List[DashboardsSchemaEntity199Response])
def list_entities_199(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_199_list(skip=skip, limit=limit)

@router.get("/entity-199/{entity_id}", response_model=DashboardsSchemaEntity199Response)
def get_entity_199(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_199_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 199 not found")
    return res

@router.post("/entity-199", response_model=DashboardsSchemaEntity199Response, status_code=201)
def create_entity_199(payload: DashboardsSchemaEntity199Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_199(payload)

@router.get("/entity-200", response_model=List[DashboardsSchemaEntity200Response])
def list_entities_200(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.get_entity_200_list(skip=skip, limit=limit)

@router.get("/entity-200/{entity_id}", response_model=DashboardsSchemaEntity200Response)
def get_entity_200(entity_id: int, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    res = srv.get_entity_200_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 200 not found")
    return res

@router.post("/entity-200", response_model=DashboardsSchemaEntity200Response, status_code=201)
def create_entity_200(payload: DashboardsSchemaEntity200Create, db: Session = Depends(get_db)):
    srv = DashboardsDomainService(db)
    return srv.create_entity_200(payload)

