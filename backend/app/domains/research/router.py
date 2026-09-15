"""
Research, Grants & Lab Inventory - FastAPI Router Endpoints
Module: app.domains.research.router
"""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domains.research.schemas import *
from app.domains.research.service import ResearchDomainService

router = APIRouter(prefix="/research", tags=["Research, Grants & Lab Inventory"])

@router.get("/entity-1", response_model=List[ResearchSchemaEntity1Response])
def list_entities_1(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_1_list(skip=skip, limit=limit)

@router.get("/entity-1/{entity_id}", response_model=ResearchSchemaEntity1Response)
def get_entity_1(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_1_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 1 not found")
    return res

@router.post("/entity-1", response_model=ResearchSchemaEntity1Response, status_code=201)
def create_entity_1(payload: ResearchSchemaEntity1Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_1(payload)

@router.get("/entity-2", response_model=List[ResearchSchemaEntity2Response])
def list_entities_2(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_2_list(skip=skip, limit=limit)

@router.get("/entity-2/{entity_id}", response_model=ResearchSchemaEntity2Response)
def get_entity_2(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_2_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 2 not found")
    return res

@router.post("/entity-2", response_model=ResearchSchemaEntity2Response, status_code=201)
def create_entity_2(payload: ResearchSchemaEntity2Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_2(payload)

@router.get("/entity-3", response_model=List[ResearchSchemaEntity3Response])
def list_entities_3(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_3_list(skip=skip, limit=limit)

@router.get("/entity-3/{entity_id}", response_model=ResearchSchemaEntity3Response)
def get_entity_3(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_3_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 3 not found")
    return res

@router.post("/entity-3", response_model=ResearchSchemaEntity3Response, status_code=201)
def create_entity_3(payload: ResearchSchemaEntity3Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_3(payload)

@router.get("/entity-4", response_model=List[ResearchSchemaEntity4Response])
def list_entities_4(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_4_list(skip=skip, limit=limit)

@router.get("/entity-4/{entity_id}", response_model=ResearchSchemaEntity4Response)
def get_entity_4(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_4_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 4 not found")
    return res

@router.post("/entity-4", response_model=ResearchSchemaEntity4Response, status_code=201)
def create_entity_4(payload: ResearchSchemaEntity4Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_4(payload)

@router.get("/entity-5", response_model=List[ResearchSchemaEntity5Response])
def list_entities_5(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_5_list(skip=skip, limit=limit)

@router.get("/entity-5/{entity_id}", response_model=ResearchSchemaEntity5Response)
def get_entity_5(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_5_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 5 not found")
    return res

@router.post("/entity-5", response_model=ResearchSchemaEntity5Response, status_code=201)
def create_entity_5(payload: ResearchSchemaEntity5Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_5(payload)

@router.get("/entity-6", response_model=List[ResearchSchemaEntity6Response])
def list_entities_6(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_6_list(skip=skip, limit=limit)

@router.get("/entity-6/{entity_id}", response_model=ResearchSchemaEntity6Response)
def get_entity_6(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_6_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 6 not found")
    return res

@router.post("/entity-6", response_model=ResearchSchemaEntity6Response, status_code=201)
def create_entity_6(payload: ResearchSchemaEntity6Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_6(payload)

@router.get("/entity-7", response_model=List[ResearchSchemaEntity7Response])
def list_entities_7(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_7_list(skip=skip, limit=limit)

@router.get("/entity-7/{entity_id}", response_model=ResearchSchemaEntity7Response)
def get_entity_7(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_7_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 7 not found")
    return res

@router.post("/entity-7", response_model=ResearchSchemaEntity7Response, status_code=201)
def create_entity_7(payload: ResearchSchemaEntity7Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_7(payload)

@router.get("/entity-8", response_model=List[ResearchSchemaEntity8Response])
def list_entities_8(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_8_list(skip=skip, limit=limit)

@router.get("/entity-8/{entity_id}", response_model=ResearchSchemaEntity8Response)
def get_entity_8(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_8_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 8 not found")
    return res

@router.post("/entity-8", response_model=ResearchSchemaEntity8Response, status_code=201)
def create_entity_8(payload: ResearchSchemaEntity8Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_8(payload)

@router.get("/entity-9", response_model=List[ResearchSchemaEntity9Response])
def list_entities_9(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_9_list(skip=skip, limit=limit)

@router.get("/entity-9/{entity_id}", response_model=ResearchSchemaEntity9Response)
def get_entity_9(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_9_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 9 not found")
    return res

@router.post("/entity-9", response_model=ResearchSchemaEntity9Response, status_code=201)
def create_entity_9(payload: ResearchSchemaEntity9Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_9(payload)

@router.get("/entity-10", response_model=List[ResearchSchemaEntity10Response])
def list_entities_10(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_10_list(skip=skip, limit=limit)

@router.get("/entity-10/{entity_id}", response_model=ResearchSchemaEntity10Response)
def get_entity_10(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_10_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 10 not found")
    return res

@router.post("/entity-10", response_model=ResearchSchemaEntity10Response, status_code=201)
def create_entity_10(payload: ResearchSchemaEntity10Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_10(payload)

@router.get("/entity-11", response_model=List[ResearchSchemaEntity11Response])
def list_entities_11(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_11_list(skip=skip, limit=limit)

@router.get("/entity-11/{entity_id}", response_model=ResearchSchemaEntity11Response)
def get_entity_11(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_11_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 11 not found")
    return res

@router.post("/entity-11", response_model=ResearchSchemaEntity11Response, status_code=201)
def create_entity_11(payload: ResearchSchemaEntity11Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_11(payload)

@router.get("/entity-12", response_model=List[ResearchSchemaEntity12Response])
def list_entities_12(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_12_list(skip=skip, limit=limit)

@router.get("/entity-12/{entity_id}", response_model=ResearchSchemaEntity12Response)
def get_entity_12(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_12_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 12 not found")
    return res

@router.post("/entity-12", response_model=ResearchSchemaEntity12Response, status_code=201)
def create_entity_12(payload: ResearchSchemaEntity12Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_12(payload)

@router.get("/entity-13", response_model=List[ResearchSchemaEntity13Response])
def list_entities_13(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_13_list(skip=skip, limit=limit)

@router.get("/entity-13/{entity_id}", response_model=ResearchSchemaEntity13Response)
def get_entity_13(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_13_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 13 not found")
    return res

@router.post("/entity-13", response_model=ResearchSchemaEntity13Response, status_code=201)
def create_entity_13(payload: ResearchSchemaEntity13Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_13(payload)

@router.get("/entity-14", response_model=List[ResearchSchemaEntity14Response])
def list_entities_14(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_14_list(skip=skip, limit=limit)

@router.get("/entity-14/{entity_id}", response_model=ResearchSchemaEntity14Response)
def get_entity_14(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_14_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 14 not found")
    return res

@router.post("/entity-14", response_model=ResearchSchemaEntity14Response, status_code=201)
def create_entity_14(payload: ResearchSchemaEntity14Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_14(payload)

@router.get("/entity-15", response_model=List[ResearchSchemaEntity15Response])
def list_entities_15(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_15_list(skip=skip, limit=limit)

@router.get("/entity-15/{entity_id}", response_model=ResearchSchemaEntity15Response)
def get_entity_15(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_15_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 15 not found")
    return res

@router.post("/entity-15", response_model=ResearchSchemaEntity15Response, status_code=201)
def create_entity_15(payload: ResearchSchemaEntity15Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_15(payload)

@router.get("/entity-16", response_model=List[ResearchSchemaEntity16Response])
def list_entities_16(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_16_list(skip=skip, limit=limit)

@router.get("/entity-16/{entity_id}", response_model=ResearchSchemaEntity16Response)
def get_entity_16(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_16_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 16 not found")
    return res

@router.post("/entity-16", response_model=ResearchSchemaEntity16Response, status_code=201)
def create_entity_16(payload: ResearchSchemaEntity16Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_16(payload)

@router.get("/entity-17", response_model=List[ResearchSchemaEntity17Response])
def list_entities_17(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_17_list(skip=skip, limit=limit)

@router.get("/entity-17/{entity_id}", response_model=ResearchSchemaEntity17Response)
def get_entity_17(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_17_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 17 not found")
    return res

@router.post("/entity-17", response_model=ResearchSchemaEntity17Response, status_code=201)
def create_entity_17(payload: ResearchSchemaEntity17Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_17(payload)

@router.get("/entity-18", response_model=List[ResearchSchemaEntity18Response])
def list_entities_18(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_18_list(skip=skip, limit=limit)

@router.get("/entity-18/{entity_id}", response_model=ResearchSchemaEntity18Response)
def get_entity_18(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_18_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 18 not found")
    return res

@router.post("/entity-18", response_model=ResearchSchemaEntity18Response, status_code=201)
def create_entity_18(payload: ResearchSchemaEntity18Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_18(payload)

@router.get("/entity-19", response_model=List[ResearchSchemaEntity19Response])
def list_entities_19(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_19_list(skip=skip, limit=limit)

@router.get("/entity-19/{entity_id}", response_model=ResearchSchemaEntity19Response)
def get_entity_19(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_19_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 19 not found")
    return res

@router.post("/entity-19", response_model=ResearchSchemaEntity19Response, status_code=201)
def create_entity_19(payload: ResearchSchemaEntity19Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_19(payload)

@router.get("/entity-20", response_model=List[ResearchSchemaEntity20Response])
def list_entities_20(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_20_list(skip=skip, limit=limit)

@router.get("/entity-20/{entity_id}", response_model=ResearchSchemaEntity20Response)
def get_entity_20(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_20_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 20 not found")
    return res

@router.post("/entity-20", response_model=ResearchSchemaEntity20Response, status_code=201)
def create_entity_20(payload: ResearchSchemaEntity20Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_20(payload)

@router.get("/entity-21", response_model=List[ResearchSchemaEntity21Response])
def list_entities_21(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_21_list(skip=skip, limit=limit)

@router.get("/entity-21/{entity_id}", response_model=ResearchSchemaEntity21Response)
def get_entity_21(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_21_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 21 not found")
    return res

@router.post("/entity-21", response_model=ResearchSchemaEntity21Response, status_code=201)
def create_entity_21(payload: ResearchSchemaEntity21Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_21(payload)

@router.get("/entity-22", response_model=List[ResearchSchemaEntity22Response])
def list_entities_22(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_22_list(skip=skip, limit=limit)

@router.get("/entity-22/{entity_id}", response_model=ResearchSchemaEntity22Response)
def get_entity_22(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_22_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 22 not found")
    return res

@router.post("/entity-22", response_model=ResearchSchemaEntity22Response, status_code=201)
def create_entity_22(payload: ResearchSchemaEntity22Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_22(payload)

@router.get("/entity-23", response_model=List[ResearchSchemaEntity23Response])
def list_entities_23(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_23_list(skip=skip, limit=limit)

@router.get("/entity-23/{entity_id}", response_model=ResearchSchemaEntity23Response)
def get_entity_23(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_23_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 23 not found")
    return res

@router.post("/entity-23", response_model=ResearchSchemaEntity23Response, status_code=201)
def create_entity_23(payload: ResearchSchemaEntity23Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_23(payload)

@router.get("/entity-24", response_model=List[ResearchSchemaEntity24Response])
def list_entities_24(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_24_list(skip=skip, limit=limit)

@router.get("/entity-24/{entity_id}", response_model=ResearchSchemaEntity24Response)
def get_entity_24(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_24_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 24 not found")
    return res

@router.post("/entity-24", response_model=ResearchSchemaEntity24Response, status_code=201)
def create_entity_24(payload: ResearchSchemaEntity24Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_24(payload)

@router.get("/entity-25", response_model=List[ResearchSchemaEntity25Response])
def list_entities_25(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_25_list(skip=skip, limit=limit)

@router.get("/entity-25/{entity_id}", response_model=ResearchSchemaEntity25Response)
def get_entity_25(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_25_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 25 not found")
    return res

@router.post("/entity-25", response_model=ResearchSchemaEntity25Response, status_code=201)
def create_entity_25(payload: ResearchSchemaEntity25Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_25(payload)

@router.get("/entity-26", response_model=List[ResearchSchemaEntity26Response])
def list_entities_26(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_26_list(skip=skip, limit=limit)

@router.get("/entity-26/{entity_id}", response_model=ResearchSchemaEntity26Response)
def get_entity_26(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_26_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 26 not found")
    return res

@router.post("/entity-26", response_model=ResearchSchemaEntity26Response, status_code=201)
def create_entity_26(payload: ResearchSchemaEntity26Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_26(payload)

@router.get("/entity-27", response_model=List[ResearchSchemaEntity27Response])
def list_entities_27(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_27_list(skip=skip, limit=limit)

@router.get("/entity-27/{entity_id}", response_model=ResearchSchemaEntity27Response)
def get_entity_27(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_27_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 27 not found")
    return res

@router.post("/entity-27", response_model=ResearchSchemaEntity27Response, status_code=201)
def create_entity_27(payload: ResearchSchemaEntity27Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_27(payload)

@router.get("/entity-28", response_model=List[ResearchSchemaEntity28Response])
def list_entities_28(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_28_list(skip=skip, limit=limit)

@router.get("/entity-28/{entity_id}", response_model=ResearchSchemaEntity28Response)
def get_entity_28(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_28_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 28 not found")
    return res

@router.post("/entity-28", response_model=ResearchSchemaEntity28Response, status_code=201)
def create_entity_28(payload: ResearchSchemaEntity28Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_28(payload)

@router.get("/entity-29", response_model=List[ResearchSchemaEntity29Response])
def list_entities_29(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_29_list(skip=skip, limit=limit)

@router.get("/entity-29/{entity_id}", response_model=ResearchSchemaEntity29Response)
def get_entity_29(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_29_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 29 not found")
    return res

@router.post("/entity-29", response_model=ResearchSchemaEntity29Response, status_code=201)
def create_entity_29(payload: ResearchSchemaEntity29Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_29(payload)

@router.get("/entity-30", response_model=List[ResearchSchemaEntity30Response])
def list_entities_30(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_30_list(skip=skip, limit=limit)

@router.get("/entity-30/{entity_id}", response_model=ResearchSchemaEntity30Response)
def get_entity_30(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_30_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 30 not found")
    return res

@router.post("/entity-30", response_model=ResearchSchemaEntity30Response, status_code=201)
def create_entity_30(payload: ResearchSchemaEntity30Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_30(payload)

@router.get("/entity-31", response_model=List[ResearchSchemaEntity31Response])
def list_entities_31(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_31_list(skip=skip, limit=limit)

@router.get("/entity-31/{entity_id}", response_model=ResearchSchemaEntity31Response)
def get_entity_31(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_31_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 31 not found")
    return res

@router.post("/entity-31", response_model=ResearchSchemaEntity31Response, status_code=201)
def create_entity_31(payload: ResearchSchemaEntity31Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_31(payload)

@router.get("/entity-32", response_model=List[ResearchSchemaEntity32Response])
def list_entities_32(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_32_list(skip=skip, limit=limit)

@router.get("/entity-32/{entity_id}", response_model=ResearchSchemaEntity32Response)
def get_entity_32(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_32_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 32 not found")
    return res

@router.post("/entity-32", response_model=ResearchSchemaEntity32Response, status_code=201)
def create_entity_32(payload: ResearchSchemaEntity32Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_32(payload)

@router.get("/entity-33", response_model=List[ResearchSchemaEntity33Response])
def list_entities_33(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_33_list(skip=skip, limit=limit)

@router.get("/entity-33/{entity_id}", response_model=ResearchSchemaEntity33Response)
def get_entity_33(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_33_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 33 not found")
    return res

@router.post("/entity-33", response_model=ResearchSchemaEntity33Response, status_code=201)
def create_entity_33(payload: ResearchSchemaEntity33Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_33(payload)

@router.get("/entity-34", response_model=List[ResearchSchemaEntity34Response])
def list_entities_34(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_34_list(skip=skip, limit=limit)

@router.get("/entity-34/{entity_id}", response_model=ResearchSchemaEntity34Response)
def get_entity_34(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_34_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 34 not found")
    return res

@router.post("/entity-34", response_model=ResearchSchemaEntity34Response, status_code=201)
def create_entity_34(payload: ResearchSchemaEntity34Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_34(payload)

@router.get("/entity-35", response_model=List[ResearchSchemaEntity35Response])
def list_entities_35(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_35_list(skip=skip, limit=limit)

@router.get("/entity-35/{entity_id}", response_model=ResearchSchemaEntity35Response)
def get_entity_35(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_35_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 35 not found")
    return res

@router.post("/entity-35", response_model=ResearchSchemaEntity35Response, status_code=201)
def create_entity_35(payload: ResearchSchemaEntity35Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_35(payload)

@router.get("/entity-36", response_model=List[ResearchSchemaEntity36Response])
def list_entities_36(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_36_list(skip=skip, limit=limit)

@router.get("/entity-36/{entity_id}", response_model=ResearchSchemaEntity36Response)
def get_entity_36(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_36_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 36 not found")
    return res

@router.post("/entity-36", response_model=ResearchSchemaEntity36Response, status_code=201)
def create_entity_36(payload: ResearchSchemaEntity36Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_36(payload)

@router.get("/entity-37", response_model=List[ResearchSchemaEntity37Response])
def list_entities_37(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_37_list(skip=skip, limit=limit)

@router.get("/entity-37/{entity_id}", response_model=ResearchSchemaEntity37Response)
def get_entity_37(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_37_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 37 not found")
    return res

@router.post("/entity-37", response_model=ResearchSchemaEntity37Response, status_code=201)
def create_entity_37(payload: ResearchSchemaEntity37Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_37(payload)

@router.get("/entity-38", response_model=List[ResearchSchemaEntity38Response])
def list_entities_38(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_38_list(skip=skip, limit=limit)

@router.get("/entity-38/{entity_id}", response_model=ResearchSchemaEntity38Response)
def get_entity_38(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_38_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 38 not found")
    return res

@router.post("/entity-38", response_model=ResearchSchemaEntity38Response, status_code=201)
def create_entity_38(payload: ResearchSchemaEntity38Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_38(payload)

@router.get("/entity-39", response_model=List[ResearchSchemaEntity39Response])
def list_entities_39(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_39_list(skip=skip, limit=limit)

@router.get("/entity-39/{entity_id}", response_model=ResearchSchemaEntity39Response)
def get_entity_39(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_39_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 39 not found")
    return res

@router.post("/entity-39", response_model=ResearchSchemaEntity39Response, status_code=201)
def create_entity_39(payload: ResearchSchemaEntity39Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_39(payload)

@router.get("/entity-40", response_model=List[ResearchSchemaEntity40Response])
def list_entities_40(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_40_list(skip=skip, limit=limit)

@router.get("/entity-40/{entity_id}", response_model=ResearchSchemaEntity40Response)
def get_entity_40(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_40_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 40 not found")
    return res

@router.post("/entity-40", response_model=ResearchSchemaEntity40Response, status_code=201)
def create_entity_40(payload: ResearchSchemaEntity40Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_40(payload)

@router.get("/entity-41", response_model=List[ResearchSchemaEntity41Response])
def list_entities_41(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_41_list(skip=skip, limit=limit)

@router.get("/entity-41/{entity_id}", response_model=ResearchSchemaEntity41Response)
def get_entity_41(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_41_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 41 not found")
    return res

@router.post("/entity-41", response_model=ResearchSchemaEntity41Response, status_code=201)
def create_entity_41(payload: ResearchSchemaEntity41Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_41(payload)

@router.get("/entity-42", response_model=List[ResearchSchemaEntity42Response])
def list_entities_42(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_42_list(skip=skip, limit=limit)

@router.get("/entity-42/{entity_id}", response_model=ResearchSchemaEntity42Response)
def get_entity_42(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_42_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 42 not found")
    return res

@router.post("/entity-42", response_model=ResearchSchemaEntity42Response, status_code=201)
def create_entity_42(payload: ResearchSchemaEntity42Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_42(payload)

@router.get("/entity-43", response_model=List[ResearchSchemaEntity43Response])
def list_entities_43(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_43_list(skip=skip, limit=limit)

@router.get("/entity-43/{entity_id}", response_model=ResearchSchemaEntity43Response)
def get_entity_43(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_43_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 43 not found")
    return res

@router.post("/entity-43", response_model=ResearchSchemaEntity43Response, status_code=201)
def create_entity_43(payload: ResearchSchemaEntity43Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_43(payload)

@router.get("/entity-44", response_model=List[ResearchSchemaEntity44Response])
def list_entities_44(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_44_list(skip=skip, limit=limit)

@router.get("/entity-44/{entity_id}", response_model=ResearchSchemaEntity44Response)
def get_entity_44(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_44_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 44 not found")
    return res

@router.post("/entity-44", response_model=ResearchSchemaEntity44Response, status_code=201)
def create_entity_44(payload: ResearchSchemaEntity44Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_44(payload)

@router.get("/entity-45", response_model=List[ResearchSchemaEntity45Response])
def list_entities_45(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_45_list(skip=skip, limit=limit)

@router.get("/entity-45/{entity_id}", response_model=ResearchSchemaEntity45Response)
def get_entity_45(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_45_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 45 not found")
    return res

@router.post("/entity-45", response_model=ResearchSchemaEntity45Response, status_code=201)
def create_entity_45(payload: ResearchSchemaEntity45Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_45(payload)

@router.get("/entity-46", response_model=List[ResearchSchemaEntity46Response])
def list_entities_46(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_46_list(skip=skip, limit=limit)

@router.get("/entity-46/{entity_id}", response_model=ResearchSchemaEntity46Response)
def get_entity_46(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_46_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 46 not found")
    return res

@router.post("/entity-46", response_model=ResearchSchemaEntity46Response, status_code=201)
def create_entity_46(payload: ResearchSchemaEntity46Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_46(payload)

@router.get("/entity-47", response_model=List[ResearchSchemaEntity47Response])
def list_entities_47(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_47_list(skip=skip, limit=limit)

@router.get("/entity-47/{entity_id}", response_model=ResearchSchemaEntity47Response)
def get_entity_47(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_47_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 47 not found")
    return res

@router.post("/entity-47", response_model=ResearchSchemaEntity47Response, status_code=201)
def create_entity_47(payload: ResearchSchemaEntity47Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_47(payload)

@router.get("/entity-48", response_model=List[ResearchSchemaEntity48Response])
def list_entities_48(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_48_list(skip=skip, limit=limit)

@router.get("/entity-48/{entity_id}", response_model=ResearchSchemaEntity48Response)
def get_entity_48(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_48_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 48 not found")
    return res

@router.post("/entity-48", response_model=ResearchSchemaEntity48Response, status_code=201)
def create_entity_48(payload: ResearchSchemaEntity48Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_48(payload)

@router.get("/entity-49", response_model=List[ResearchSchemaEntity49Response])
def list_entities_49(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_49_list(skip=skip, limit=limit)

@router.get("/entity-49/{entity_id}", response_model=ResearchSchemaEntity49Response)
def get_entity_49(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_49_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 49 not found")
    return res

@router.post("/entity-49", response_model=ResearchSchemaEntity49Response, status_code=201)
def create_entity_49(payload: ResearchSchemaEntity49Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_49(payload)

@router.get("/entity-50", response_model=List[ResearchSchemaEntity50Response])
def list_entities_50(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_50_list(skip=skip, limit=limit)

@router.get("/entity-50/{entity_id}", response_model=ResearchSchemaEntity50Response)
def get_entity_50(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_50_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 50 not found")
    return res

@router.post("/entity-50", response_model=ResearchSchemaEntity50Response, status_code=201)
def create_entity_50(payload: ResearchSchemaEntity50Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_50(payload)

@router.get("/entity-51", response_model=List[ResearchSchemaEntity51Response])
def list_entities_51(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_51_list(skip=skip, limit=limit)

@router.get("/entity-51/{entity_id}", response_model=ResearchSchemaEntity51Response)
def get_entity_51(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_51_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 51 not found")
    return res

@router.post("/entity-51", response_model=ResearchSchemaEntity51Response, status_code=201)
def create_entity_51(payload: ResearchSchemaEntity51Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_51(payload)

@router.get("/entity-52", response_model=List[ResearchSchemaEntity52Response])
def list_entities_52(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_52_list(skip=skip, limit=limit)

@router.get("/entity-52/{entity_id}", response_model=ResearchSchemaEntity52Response)
def get_entity_52(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_52_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 52 not found")
    return res

@router.post("/entity-52", response_model=ResearchSchemaEntity52Response, status_code=201)
def create_entity_52(payload: ResearchSchemaEntity52Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_52(payload)

@router.get("/entity-53", response_model=List[ResearchSchemaEntity53Response])
def list_entities_53(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_53_list(skip=skip, limit=limit)

@router.get("/entity-53/{entity_id}", response_model=ResearchSchemaEntity53Response)
def get_entity_53(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_53_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 53 not found")
    return res

@router.post("/entity-53", response_model=ResearchSchemaEntity53Response, status_code=201)
def create_entity_53(payload: ResearchSchemaEntity53Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_53(payload)

@router.get("/entity-54", response_model=List[ResearchSchemaEntity54Response])
def list_entities_54(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_54_list(skip=skip, limit=limit)

@router.get("/entity-54/{entity_id}", response_model=ResearchSchemaEntity54Response)
def get_entity_54(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_54_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 54 not found")
    return res

@router.post("/entity-54", response_model=ResearchSchemaEntity54Response, status_code=201)
def create_entity_54(payload: ResearchSchemaEntity54Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_54(payload)

@router.get("/entity-55", response_model=List[ResearchSchemaEntity55Response])
def list_entities_55(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_55_list(skip=skip, limit=limit)

@router.get("/entity-55/{entity_id}", response_model=ResearchSchemaEntity55Response)
def get_entity_55(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_55_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 55 not found")
    return res

@router.post("/entity-55", response_model=ResearchSchemaEntity55Response, status_code=201)
def create_entity_55(payload: ResearchSchemaEntity55Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_55(payload)

@router.get("/entity-56", response_model=List[ResearchSchemaEntity56Response])
def list_entities_56(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_56_list(skip=skip, limit=limit)

@router.get("/entity-56/{entity_id}", response_model=ResearchSchemaEntity56Response)
def get_entity_56(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_56_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 56 not found")
    return res

@router.post("/entity-56", response_model=ResearchSchemaEntity56Response, status_code=201)
def create_entity_56(payload: ResearchSchemaEntity56Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_56(payload)

@router.get("/entity-57", response_model=List[ResearchSchemaEntity57Response])
def list_entities_57(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_57_list(skip=skip, limit=limit)

@router.get("/entity-57/{entity_id}", response_model=ResearchSchemaEntity57Response)
def get_entity_57(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_57_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 57 not found")
    return res

@router.post("/entity-57", response_model=ResearchSchemaEntity57Response, status_code=201)
def create_entity_57(payload: ResearchSchemaEntity57Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_57(payload)

@router.get("/entity-58", response_model=List[ResearchSchemaEntity58Response])
def list_entities_58(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_58_list(skip=skip, limit=limit)

@router.get("/entity-58/{entity_id}", response_model=ResearchSchemaEntity58Response)
def get_entity_58(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_58_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 58 not found")
    return res

@router.post("/entity-58", response_model=ResearchSchemaEntity58Response, status_code=201)
def create_entity_58(payload: ResearchSchemaEntity58Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_58(payload)

@router.get("/entity-59", response_model=List[ResearchSchemaEntity59Response])
def list_entities_59(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_59_list(skip=skip, limit=limit)

@router.get("/entity-59/{entity_id}", response_model=ResearchSchemaEntity59Response)
def get_entity_59(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_59_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 59 not found")
    return res

@router.post("/entity-59", response_model=ResearchSchemaEntity59Response, status_code=201)
def create_entity_59(payload: ResearchSchemaEntity59Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_59(payload)

@router.get("/entity-60", response_model=List[ResearchSchemaEntity60Response])
def list_entities_60(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_60_list(skip=skip, limit=limit)

@router.get("/entity-60/{entity_id}", response_model=ResearchSchemaEntity60Response)
def get_entity_60(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_60_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 60 not found")
    return res

@router.post("/entity-60", response_model=ResearchSchemaEntity60Response, status_code=201)
def create_entity_60(payload: ResearchSchemaEntity60Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_60(payload)

@router.get("/entity-61", response_model=List[ResearchSchemaEntity61Response])
def list_entities_61(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_61_list(skip=skip, limit=limit)

@router.get("/entity-61/{entity_id}", response_model=ResearchSchemaEntity61Response)
def get_entity_61(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_61_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 61 not found")
    return res

@router.post("/entity-61", response_model=ResearchSchemaEntity61Response, status_code=201)
def create_entity_61(payload: ResearchSchemaEntity61Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_61(payload)

@router.get("/entity-62", response_model=List[ResearchSchemaEntity62Response])
def list_entities_62(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_62_list(skip=skip, limit=limit)

@router.get("/entity-62/{entity_id}", response_model=ResearchSchemaEntity62Response)
def get_entity_62(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_62_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 62 not found")
    return res

@router.post("/entity-62", response_model=ResearchSchemaEntity62Response, status_code=201)
def create_entity_62(payload: ResearchSchemaEntity62Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_62(payload)

@router.get("/entity-63", response_model=List[ResearchSchemaEntity63Response])
def list_entities_63(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_63_list(skip=skip, limit=limit)

@router.get("/entity-63/{entity_id}", response_model=ResearchSchemaEntity63Response)
def get_entity_63(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_63_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 63 not found")
    return res

@router.post("/entity-63", response_model=ResearchSchemaEntity63Response, status_code=201)
def create_entity_63(payload: ResearchSchemaEntity63Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_63(payload)

@router.get("/entity-64", response_model=List[ResearchSchemaEntity64Response])
def list_entities_64(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_64_list(skip=skip, limit=limit)

@router.get("/entity-64/{entity_id}", response_model=ResearchSchemaEntity64Response)
def get_entity_64(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_64_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 64 not found")
    return res

@router.post("/entity-64", response_model=ResearchSchemaEntity64Response, status_code=201)
def create_entity_64(payload: ResearchSchemaEntity64Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_64(payload)

@router.get("/entity-65", response_model=List[ResearchSchemaEntity65Response])
def list_entities_65(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_65_list(skip=skip, limit=limit)

@router.get("/entity-65/{entity_id}", response_model=ResearchSchemaEntity65Response)
def get_entity_65(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_65_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 65 not found")
    return res

@router.post("/entity-65", response_model=ResearchSchemaEntity65Response, status_code=201)
def create_entity_65(payload: ResearchSchemaEntity65Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_65(payload)

@router.get("/entity-66", response_model=List[ResearchSchemaEntity66Response])
def list_entities_66(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_66_list(skip=skip, limit=limit)

@router.get("/entity-66/{entity_id}", response_model=ResearchSchemaEntity66Response)
def get_entity_66(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_66_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 66 not found")
    return res

@router.post("/entity-66", response_model=ResearchSchemaEntity66Response, status_code=201)
def create_entity_66(payload: ResearchSchemaEntity66Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_66(payload)

@router.get("/entity-67", response_model=List[ResearchSchemaEntity67Response])
def list_entities_67(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_67_list(skip=skip, limit=limit)

@router.get("/entity-67/{entity_id}", response_model=ResearchSchemaEntity67Response)
def get_entity_67(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_67_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 67 not found")
    return res

@router.post("/entity-67", response_model=ResearchSchemaEntity67Response, status_code=201)
def create_entity_67(payload: ResearchSchemaEntity67Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_67(payload)

@router.get("/entity-68", response_model=List[ResearchSchemaEntity68Response])
def list_entities_68(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_68_list(skip=skip, limit=limit)

@router.get("/entity-68/{entity_id}", response_model=ResearchSchemaEntity68Response)
def get_entity_68(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_68_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 68 not found")
    return res

@router.post("/entity-68", response_model=ResearchSchemaEntity68Response, status_code=201)
def create_entity_68(payload: ResearchSchemaEntity68Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_68(payload)

@router.get("/entity-69", response_model=List[ResearchSchemaEntity69Response])
def list_entities_69(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_69_list(skip=skip, limit=limit)

@router.get("/entity-69/{entity_id}", response_model=ResearchSchemaEntity69Response)
def get_entity_69(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_69_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 69 not found")
    return res

@router.post("/entity-69", response_model=ResearchSchemaEntity69Response, status_code=201)
def create_entity_69(payload: ResearchSchemaEntity69Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_69(payload)

@router.get("/entity-70", response_model=List[ResearchSchemaEntity70Response])
def list_entities_70(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_70_list(skip=skip, limit=limit)

@router.get("/entity-70/{entity_id}", response_model=ResearchSchemaEntity70Response)
def get_entity_70(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_70_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 70 not found")
    return res

@router.post("/entity-70", response_model=ResearchSchemaEntity70Response, status_code=201)
def create_entity_70(payload: ResearchSchemaEntity70Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_70(payload)

@router.get("/entity-71", response_model=List[ResearchSchemaEntity71Response])
def list_entities_71(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_71_list(skip=skip, limit=limit)

@router.get("/entity-71/{entity_id}", response_model=ResearchSchemaEntity71Response)
def get_entity_71(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_71_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 71 not found")
    return res

@router.post("/entity-71", response_model=ResearchSchemaEntity71Response, status_code=201)
def create_entity_71(payload: ResearchSchemaEntity71Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_71(payload)

@router.get("/entity-72", response_model=List[ResearchSchemaEntity72Response])
def list_entities_72(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_72_list(skip=skip, limit=limit)

@router.get("/entity-72/{entity_id}", response_model=ResearchSchemaEntity72Response)
def get_entity_72(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_72_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 72 not found")
    return res

@router.post("/entity-72", response_model=ResearchSchemaEntity72Response, status_code=201)
def create_entity_72(payload: ResearchSchemaEntity72Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_72(payload)

@router.get("/entity-73", response_model=List[ResearchSchemaEntity73Response])
def list_entities_73(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_73_list(skip=skip, limit=limit)

@router.get("/entity-73/{entity_id}", response_model=ResearchSchemaEntity73Response)
def get_entity_73(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_73_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 73 not found")
    return res

@router.post("/entity-73", response_model=ResearchSchemaEntity73Response, status_code=201)
def create_entity_73(payload: ResearchSchemaEntity73Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_73(payload)

@router.get("/entity-74", response_model=List[ResearchSchemaEntity74Response])
def list_entities_74(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_74_list(skip=skip, limit=limit)

@router.get("/entity-74/{entity_id}", response_model=ResearchSchemaEntity74Response)
def get_entity_74(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_74_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 74 not found")
    return res

@router.post("/entity-74", response_model=ResearchSchemaEntity74Response, status_code=201)
def create_entity_74(payload: ResearchSchemaEntity74Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_74(payload)

@router.get("/entity-75", response_model=List[ResearchSchemaEntity75Response])
def list_entities_75(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_75_list(skip=skip, limit=limit)

@router.get("/entity-75/{entity_id}", response_model=ResearchSchemaEntity75Response)
def get_entity_75(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_75_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 75 not found")
    return res

@router.post("/entity-75", response_model=ResearchSchemaEntity75Response, status_code=201)
def create_entity_75(payload: ResearchSchemaEntity75Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_75(payload)

@router.get("/entity-76", response_model=List[ResearchSchemaEntity76Response])
def list_entities_76(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_76_list(skip=skip, limit=limit)

@router.get("/entity-76/{entity_id}", response_model=ResearchSchemaEntity76Response)
def get_entity_76(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_76_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 76 not found")
    return res

@router.post("/entity-76", response_model=ResearchSchemaEntity76Response, status_code=201)
def create_entity_76(payload: ResearchSchemaEntity76Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_76(payload)

@router.get("/entity-77", response_model=List[ResearchSchemaEntity77Response])
def list_entities_77(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_77_list(skip=skip, limit=limit)

@router.get("/entity-77/{entity_id}", response_model=ResearchSchemaEntity77Response)
def get_entity_77(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_77_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 77 not found")
    return res

@router.post("/entity-77", response_model=ResearchSchemaEntity77Response, status_code=201)
def create_entity_77(payload: ResearchSchemaEntity77Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_77(payload)

@router.get("/entity-78", response_model=List[ResearchSchemaEntity78Response])
def list_entities_78(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_78_list(skip=skip, limit=limit)

@router.get("/entity-78/{entity_id}", response_model=ResearchSchemaEntity78Response)
def get_entity_78(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_78_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 78 not found")
    return res

@router.post("/entity-78", response_model=ResearchSchemaEntity78Response, status_code=201)
def create_entity_78(payload: ResearchSchemaEntity78Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_78(payload)

@router.get("/entity-79", response_model=List[ResearchSchemaEntity79Response])
def list_entities_79(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_79_list(skip=skip, limit=limit)

@router.get("/entity-79/{entity_id}", response_model=ResearchSchemaEntity79Response)
def get_entity_79(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_79_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 79 not found")
    return res

@router.post("/entity-79", response_model=ResearchSchemaEntity79Response, status_code=201)
def create_entity_79(payload: ResearchSchemaEntity79Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_79(payload)

@router.get("/entity-80", response_model=List[ResearchSchemaEntity80Response])
def list_entities_80(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_80_list(skip=skip, limit=limit)

@router.get("/entity-80/{entity_id}", response_model=ResearchSchemaEntity80Response)
def get_entity_80(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_80_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 80 not found")
    return res

@router.post("/entity-80", response_model=ResearchSchemaEntity80Response, status_code=201)
def create_entity_80(payload: ResearchSchemaEntity80Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_80(payload)

@router.get("/entity-81", response_model=List[ResearchSchemaEntity81Response])
def list_entities_81(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_81_list(skip=skip, limit=limit)

@router.get("/entity-81/{entity_id}", response_model=ResearchSchemaEntity81Response)
def get_entity_81(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_81_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 81 not found")
    return res

@router.post("/entity-81", response_model=ResearchSchemaEntity81Response, status_code=201)
def create_entity_81(payload: ResearchSchemaEntity81Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_81(payload)

@router.get("/entity-82", response_model=List[ResearchSchemaEntity82Response])
def list_entities_82(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_82_list(skip=skip, limit=limit)

@router.get("/entity-82/{entity_id}", response_model=ResearchSchemaEntity82Response)
def get_entity_82(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_82_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 82 not found")
    return res

@router.post("/entity-82", response_model=ResearchSchemaEntity82Response, status_code=201)
def create_entity_82(payload: ResearchSchemaEntity82Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_82(payload)

@router.get("/entity-83", response_model=List[ResearchSchemaEntity83Response])
def list_entities_83(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_83_list(skip=skip, limit=limit)

@router.get("/entity-83/{entity_id}", response_model=ResearchSchemaEntity83Response)
def get_entity_83(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_83_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 83 not found")
    return res

@router.post("/entity-83", response_model=ResearchSchemaEntity83Response, status_code=201)
def create_entity_83(payload: ResearchSchemaEntity83Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_83(payload)

@router.get("/entity-84", response_model=List[ResearchSchemaEntity84Response])
def list_entities_84(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_84_list(skip=skip, limit=limit)

@router.get("/entity-84/{entity_id}", response_model=ResearchSchemaEntity84Response)
def get_entity_84(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_84_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 84 not found")
    return res

@router.post("/entity-84", response_model=ResearchSchemaEntity84Response, status_code=201)
def create_entity_84(payload: ResearchSchemaEntity84Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_84(payload)

@router.get("/entity-85", response_model=List[ResearchSchemaEntity85Response])
def list_entities_85(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_85_list(skip=skip, limit=limit)

@router.get("/entity-85/{entity_id}", response_model=ResearchSchemaEntity85Response)
def get_entity_85(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_85_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 85 not found")
    return res

@router.post("/entity-85", response_model=ResearchSchemaEntity85Response, status_code=201)
def create_entity_85(payload: ResearchSchemaEntity85Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_85(payload)

@router.get("/entity-86", response_model=List[ResearchSchemaEntity86Response])
def list_entities_86(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_86_list(skip=skip, limit=limit)

@router.get("/entity-86/{entity_id}", response_model=ResearchSchemaEntity86Response)
def get_entity_86(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_86_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 86 not found")
    return res

@router.post("/entity-86", response_model=ResearchSchemaEntity86Response, status_code=201)
def create_entity_86(payload: ResearchSchemaEntity86Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_86(payload)

@router.get("/entity-87", response_model=List[ResearchSchemaEntity87Response])
def list_entities_87(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_87_list(skip=skip, limit=limit)

@router.get("/entity-87/{entity_id}", response_model=ResearchSchemaEntity87Response)
def get_entity_87(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_87_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 87 not found")
    return res

@router.post("/entity-87", response_model=ResearchSchemaEntity87Response, status_code=201)
def create_entity_87(payload: ResearchSchemaEntity87Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_87(payload)

@router.get("/entity-88", response_model=List[ResearchSchemaEntity88Response])
def list_entities_88(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_88_list(skip=skip, limit=limit)

@router.get("/entity-88/{entity_id}", response_model=ResearchSchemaEntity88Response)
def get_entity_88(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_88_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 88 not found")
    return res

@router.post("/entity-88", response_model=ResearchSchemaEntity88Response, status_code=201)
def create_entity_88(payload: ResearchSchemaEntity88Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_88(payload)

@router.get("/entity-89", response_model=List[ResearchSchemaEntity89Response])
def list_entities_89(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_89_list(skip=skip, limit=limit)

@router.get("/entity-89/{entity_id}", response_model=ResearchSchemaEntity89Response)
def get_entity_89(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_89_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 89 not found")
    return res

@router.post("/entity-89", response_model=ResearchSchemaEntity89Response, status_code=201)
def create_entity_89(payload: ResearchSchemaEntity89Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_89(payload)

@router.get("/entity-90", response_model=List[ResearchSchemaEntity90Response])
def list_entities_90(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_90_list(skip=skip, limit=limit)

@router.get("/entity-90/{entity_id}", response_model=ResearchSchemaEntity90Response)
def get_entity_90(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_90_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 90 not found")
    return res

@router.post("/entity-90", response_model=ResearchSchemaEntity90Response, status_code=201)
def create_entity_90(payload: ResearchSchemaEntity90Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_90(payload)

@router.get("/entity-91", response_model=List[ResearchSchemaEntity91Response])
def list_entities_91(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_91_list(skip=skip, limit=limit)

@router.get("/entity-91/{entity_id}", response_model=ResearchSchemaEntity91Response)
def get_entity_91(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_91_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 91 not found")
    return res

@router.post("/entity-91", response_model=ResearchSchemaEntity91Response, status_code=201)
def create_entity_91(payload: ResearchSchemaEntity91Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_91(payload)

@router.get("/entity-92", response_model=List[ResearchSchemaEntity92Response])
def list_entities_92(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_92_list(skip=skip, limit=limit)

@router.get("/entity-92/{entity_id}", response_model=ResearchSchemaEntity92Response)
def get_entity_92(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_92_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 92 not found")
    return res

@router.post("/entity-92", response_model=ResearchSchemaEntity92Response, status_code=201)
def create_entity_92(payload: ResearchSchemaEntity92Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_92(payload)

@router.get("/entity-93", response_model=List[ResearchSchemaEntity93Response])
def list_entities_93(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_93_list(skip=skip, limit=limit)

@router.get("/entity-93/{entity_id}", response_model=ResearchSchemaEntity93Response)
def get_entity_93(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_93_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 93 not found")
    return res

@router.post("/entity-93", response_model=ResearchSchemaEntity93Response, status_code=201)
def create_entity_93(payload: ResearchSchemaEntity93Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_93(payload)

@router.get("/entity-94", response_model=List[ResearchSchemaEntity94Response])
def list_entities_94(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_94_list(skip=skip, limit=limit)

@router.get("/entity-94/{entity_id}", response_model=ResearchSchemaEntity94Response)
def get_entity_94(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_94_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 94 not found")
    return res

@router.post("/entity-94", response_model=ResearchSchemaEntity94Response, status_code=201)
def create_entity_94(payload: ResearchSchemaEntity94Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_94(payload)

@router.get("/entity-95", response_model=List[ResearchSchemaEntity95Response])
def list_entities_95(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_95_list(skip=skip, limit=limit)

@router.get("/entity-95/{entity_id}", response_model=ResearchSchemaEntity95Response)
def get_entity_95(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_95_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 95 not found")
    return res

@router.post("/entity-95", response_model=ResearchSchemaEntity95Response, status_code=201)
def create_entity_95(payload: ResearchSchemaEntity95Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_95(payload)

@router.get("/entity-96", response_model=List[ResearchSchemaEntity96Response])
def list_entities_96(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_96_list(skip=skip, limit=limit)

@router.get("/entity-96/{entity_id}", response_model=ResearchSchemaEntity96Response)
def get_entity_96(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_96_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 96 not found")
    return res

@router.post("/entity-96", response_model=ResearchSchemaEntity96Response, status_code=201)
def create_entity_96(payload: ResearchSchemaEntity96Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_96(payload)

@router.get("/entity-97", response_model=List[ResearchSchemaEntity97Response])
def list_entities_97(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_97_list(skip=skip, limit=limit)

@router.get("/entity-97/{entity_id}", response_model=ResearchSchemaEntity97Response)
def get_entity_97(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_97_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 97 not found")
    return res

@router.post("/entity-97", response_model=ResearchSchemaEntity97Response, status_code=201)
def create_entity_97(payload: ResearchSchemaEntity97Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_97(payload)

@router.get("/entity-98", response_model=List[ResearchSchemaEntity98Response])
def list_entities_98(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_98_list(skip=skip, limit=limit)

@router.get("/entity-98/{entity_id}", response_model=ResearchSchemaEntity98Response)
def get_entity_98(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_98_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 98 not found")
    return res

@router.post("/entity-98", response_model=ResearchSchemaEntity98Response, status_code=201)
def create_entity_98(payload: ResearchSchemaEntity98Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_98(payload)

@router.get("/entity-99", response_model=List[ResearchSchemaEntity99Response])
def list_entities_99(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_99_list(skip=skip, limit=limit)

@router.get("/entity-99/{entity_id}", response_model=ResearchSchemaEntity99Response)
def get_entity_99(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_99_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 99 not found")
    return res

@router.post("/entity-99", response_model=ResearchSchemaEntity99Response, status_code=201)
def create_entity_99(payload: ResearchSchemaEntity99Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_99(payload)

@router.get("/entity-100", response_model=List[ResearchSchemaEntity100Response])
def list_entities_100(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_100_list(skip=skip, limit=limit)

@router.get("/entity-100/{entity_id}", response_model=ResearchSchemaEntity100Response)
def get_entity_100(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_100_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 100 not found")
    return res

@router.post("/entity-100", response_model=ResearchSchemaEntity100Response, status_code=201)
def create_entity_100(payload: ResearchSchemaEntity100Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_100(payload)

@router.get("/entity-101", response_model=List[ResearchSchemaEntity101Response])
def list_entities_101(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_101_list(skip=skip, limit=limit)

@router.get("/entity-101/{entity_id}", response_model=ResearchSchemaEntity101Response)
def get_entity_101(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_101_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 101 not found")
    return res

@router.post("/entity-101", response_model=ResearchSchemaEntity101Response, status_code=201)
def create_entity_101(payload: ResearchSchemaEntity101Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_101(payload)

@router.get("/entity-102", response_model=List[ResearchSchemaEntity102Response])
def list_entities_102(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_102_list(skip=skip, limit=limit)

@router.get("/entity-102/{entity_id}", response_model=ResearchSchemaEntity102Response)
def get_entity_102(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_102_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 102 not found")
    return res

@router.post("/entity-102", response_model=ResearchSchemaEntity102Response, status_code=201)
def create_entity_102(payload: ResearchSchemaEntity102Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_102(payload)

@router.get("/entity-103", response_model=List[ResearchSchemaEntity103Response])
def list_entities_103(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_103_list(skip=skip, limit=limit)

@router.get("/entity-103/{entity_id}", response_model=ResearchSchemaEntity103Response)
def get_entity_103(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_103_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 103 not found")
    return res

@router.post("/entity-103", response_model=ResearchSchemaEntity103Response, status_code=201)
def create_entity_103(payload: ResearchSchemaEntity103Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_103(payload)

@router.get("/entity-104", response_model=List[ResearchSchemaEntity104Response])
def list_entities_104(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_104_list(skip=skip, limit=limit)

@router.get("/entity-104/{entity_id}", response_model=ResearchSchemaEntity104Response)
def get_entity_104(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_104_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 104 not found")
    return res

@router.post("/entity-104", response_model=ResearchSchemaEntity104Response, status_code=201)
def create_entity_104(payload: ResearchSchemaEntity104Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_104(payload)

@router.get("/entity-105", response_model=List[ResearchSchemaEntity105Response])
def list_entities_105(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_105_list(skip=skip, limit=limit)

@router.get("/entity-105/{entity_id}", response_model=ResearchSchemaEntity105Response)
def get_entity_105(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_105_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 105 not found")
    return res

@router.post("/entity-105", response_model=ResearchSchemaEntity105Response, status_code=201)
def create_entity_105(payload: ResearchSchemaEntity105Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_105(payload)

@router.get("/entity-106", response_model=List[ResearchSchemaEntity106Response])
def list_entities_106(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_106_list(skip=skip, limit=limit)

@router.get("/entity-106/{entity_id}", response_model=ResearchSchemaEntity106Response)
def get_entity_106(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_106_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 106 not found")
    return res

@router.post("/entity-106", response_model=ResearchSchemaEntity106Response, status_code=201)
def create_entity_106(payload: ResearchSchemaEntity106Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_106(payload)

@router.get("/entity-107", response_model=List[ResearchSchemaEntity107Response])
def list_entities_107(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_107_list(skip=skip, limit=limit)

@router.get("/entity-107/{entity_id}", response_model=ResearchSchemaEntity107Response)
def get_entity_107(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_107_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 107 not found")
    return res

@router.post("/entity-107", response_model=ResearchSchemaEntity107Response, status_code=201)
def create_entity_107(payload: ResearchSchemaEntity107Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_107(payload)

@router.get("/entity-108", response_model=List[ResearchSchemaEntity108Response])
def list_entities_108(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_108_list(skip=skip, limit=limit)

@router.get("/entity-108/{entity_id}", response_model=ResearchSchemaEntity108Response)
def get_entity_108(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_108_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 108 not found")
    return res

@router.post("/entity-108", response_model=ResearchSchemaEntity108Response, status_code=201)
def create_entity_108(payload: ResearchSchemaEntity108Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_108(payload)

@router.get("/entity-109", response_model=List[ResearchSchemaEntity109Response])
def list_entities_109(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_109_list(skip=skip, limit=limit)

@router.get("/entity-109/{entity_id}", response_model=ResearchSchemaEntity109Response)
def get_entity_109(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_109_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 109 not found")
    return res

@router.post("/entity-109", response_model=ResearchSchemaEntity109Response, status_code=201)
def create_entity_109(payload: ResearchSchemaEntity109Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_109(payload)

@router.get("/entity-110", response_model=List[ResearchSchemaEntity110Response])
def list_entities_110(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_110_list(skip=skip, limit=limit)

@router.get("/entity-110/{entity_id}", response_model=ResearchSchemaEntity110Response)
def get_entity_110(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_110_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 110 not found")
    return res

@router.post("/entity-110", response_model=ResearchSchemaEntity110Response, status_code=201)
def create_entity_110(payload: ResearchSchemaEntity110Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_110(payload)

@router.get("/entity-111", response_model=List[ResearchSchemaEntity111Response])
def list_entities_111(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_111_list(skip=skip, limit=limit)

@router.get("/entity-111/{entity_id}", response_model=ResearchSchemaEntity111Response)
def get_entity_111(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_111_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 111 not found")
    return res

@router.post("/entity-111", response_model=ResearchSchemaEntity111Response, status_code=201)
def create_entity_111(payload: ResearchSchemaEntity111Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_111(payload)

@router.get("/entity-112", response_model=List[ResearchSchemaEntity112Response])
def list_entities_112(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_112_list(skip=skip, limit=limit)

@router.get("/entity-112/{entity_id}", response_model=ResearchSchemaEntity112Response)
def get_entity_112(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_112_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 112 not found")
    return res

@router.post("/entity-112", response_model=ResearchSchemaEntity112Response, status_code=201)
def create_entity_112(payload: ResearchSchemaEntity112Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_112(payload)

@router.get("/entity-113", response_model=List[ResearchSchemaEntity113Response])
def list_entities_113(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_113_list(skip=skip, limit=limit)

@router.get("/entity-113/{entity_id}", response_model=ResearchSchemaEntity113Response)
def get_entity_113(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_113_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 113 not found")
    return res

@router.post("/entity-113", response_model=ResearchSchemaEntity113Response, status_code=201)
def create_entity_113(payload: ResearchSchemaEntity113Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_113(payload)

@router.get("/entity-114", response_model=List[ResearchSchemaEntity114Response])
def list_entities_114(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_114_list(skip=skip, limit=limit)

@router.get("/entity-114/{entity_id}", response_model=ResearchSchemaEntity114Response)
def get_entity_114(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_114_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 114 not found")
    return res

@router.post("/entity-114", response_model=ResearchSchemaEntity114Response, status_code=201)
def create_entity_114(payload: ResearchSchemaEntity114Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_114(payload)

@router.get("/entity-115", response_model=List[ResearchSchemaEntity115Response])
def list_entities_115(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_115_list(skip=skip, limit=limit)

@router.get("/entity-115/{entity_id}", response_model=ResearchSchemaEntity115Response)
def get_entity_115(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_115_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 115 not found")
    return res

@router.post("/entity-115", response_model=ResearchSchemaEntity115Response, status_code=201)
def create_entity_115(payload: ResearchSchemaEntity115Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_115(payload)

@router.get("/entity-116", response_model=List[ResearchSchemaEntity116Response])
def list_entities_116(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_116_list(skip=skip, limit=limit)

@router.get("/entity-116/{entity_id}", response_model=ResearchSchemaEntity116Response)
def get_entity_116(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_116_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 116 not found")
    return res

@router.post("/entity-116", response_model=ResearchSchemaEntity116Response, status_code=201)
def create_entity_116(payload: ResearchSchemaEntity116Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_116(payload)

@router.get("/entity-117", response_model=List[ResearchSchemaEntity117Response])
def list_entities_117(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_117_list(skip=skip, limit=limit)

@router.get("/entity-117/{entity_id}", response_model=ResearchSchemaEntity117Response)
def get_entity_117(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_117_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 117 not found")
    return res

@router.post("/entity-117", response_model=ResearchSchemaEntity117Response, status_code=201)
def create_entity_117(payload: ResearchSchemaEntity117Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_117(payload)

@router.get("/entity-118", response_model=List[ResearchSchemaEntity118Response])
def list_entities_118(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_118_list(skip=skip, limit=limit)

@router.get("/entity-118/{entity_id}", response_model=ResearchSchemaEntity118Response)
def get_entity_118(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_118_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 118 not found")
    return res

@router.post("/entity-118", response_model=ResearchSchemaEntity118Response, status_code=201)
def create_entity_118(payload: ResearchSchemaEntity118Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_118(payload)

@router.get("/entity-119", response_model=List[ResearchSchemaEntity119Response])
def list_entities_119(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_119_list(skip=skip, limit=limit)

@router.get("/entity-119/{entity_id}", response_model=ResearchSchemaEntity119Response)
def get_entity_119(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_119_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 119 not found")
    return res

@router.post("/entity-119", response_model=ResearchSchemaEntity119Response, status_code=201)
def create_entity_119(payload: ResearchSchemaEntity119Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_119(payload)

@router.get("/entity-120", response_model=List[ResearchSchemaEntity120Response])
def list_entities_120(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_120_list(skip=skip, limit=limit)

@router.get("/entity-120/{entity_id}", response_model=ResearchSchemaEntity120Response)
def get_entity_120(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_120_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 120 not found")
    return res

@router.post("/entity-120", response_model=ResearchSchemaEntity120Response, status_code=201)
def create_entity_120(payload: ResearchSchemaEntity120Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_120(payload)

@router.get("/entity-121", response_model=List[ResearchSchemaEntity121Response])
def list_entities_121(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_121_list(skip=skip, limit=limit)

@router.get("/entity-121/{entity_id}", response_model=ResearchSchemaEntity121Response)
def get_entity_121(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_121_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 121 not found")
    return res

@router.post("/entity-121", response_model=ResearchSchemaEntity121Response, status_code=201)
def create_entity_121(payload: ResearchSchemaEntity121Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_121(payload)

@router.get("/entity-122", response_model=List[ResearchSchemaEntity122Response])
def list_entities_122(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_122_list(skip=skip, limit=limit)

@router.get("/entity-122/{entity_id}", response_model=ResearchSchemaEntity122Response)
def get_entity_122(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_122_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 122 not found")
    return res

@router.post("/entity-122", response_model=ResearchSchemaEntity122Response, status_code=201)
def create_entity_122(payload: ResearchSchemaEntity122Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_122(payload)

@router.get("/entity-123", response_model=List[ResearchSchemaEntity123Response])
def list_entities_123(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_123_list(skip=skip, limit=limit)

@router.get("/entity-123/{entity_id}", response_model=ResearchSchemaEntity123Response)
def get_entity_123(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_123_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 123 not found")
    return res

@router.post("/entity-123", response_model=ResearchSchemaEntity123Response, status_code=201)
def create_entity_123(payload: ResearchSchemaEntity123Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_123(payload)

@router.get("/entity-124", response_model=List[ResearchSchemaEntity124Response])
def list_entities_124(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_124_list(skip=skip, limit=limit)

@router.get("/entity-124/{entity_id}", response_model=ResearchSchemaEntity124Response)
def get_entity_124(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_124_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 124 not found")
    return res

@router.post("/entity-124", response_model=ResearchSchemaEntity124Response, status_code=201)
def create_entity_124(payload: ResearchSchemaEntity124Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_124(payload)

@router.get("/entity-125", response_model=List[ResearchSchemaEntity125Response])
def list_entities_125(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_125_list(skip=skip, limit=limit)

@router.get("/entity-125/{entity_id}", response_model=ResearchSchemaEntity125Response)
def get_entity_125(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_125_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 125 not found")
    return res

@router.post("/entity-125", response_model=ResearchSchemaEntity125Response, status_code=201)
def create_entity_125(payload: ResearchSchemaEntity125Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_125(payload)

@router.get("/entity-126", response_model=List[ResearchSchemaEntity126Response])
def list_entities_126(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_126_list(skip=skip, limit=limit)

@router.get("/entity-126/{entity_id}", response_model=ResearchSchemaEntity126Response)
def get_entity_126(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_126_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 126 not found")
    return res

@router.post("/entity-126", response_model=ResearchSchemaEntity126Response, status_code=201)
def create_entity_126(payload: ResearchSchemaEntity126Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_126(payload)

@router.get("/entity-127", response_model=List[ResearchSchemaEntity127Response])
def list_entities_127(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_127_list(skip=skip, limit=limit)

@router.get("/entity-127/{entity_id}", response_model=ResearchSchemaEntity127Response)
def get_entity_127(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_127_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 127 not found")
    return res

@router.post("/entity-127", response_model=ResearchSchemaEntity127Response, status_code=201)
def create_entity_127(payload: ResearchSchemaEntity127Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_127(payload)

@router.get("/entity-128", response_model=List[ResearchSchemaEntity128Response])
def list_entities_128(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_128_list(skip=skip, limit=limit)

@router.get("/entity-128/{entity_id}", response_model=ResearchSchemaEntity128Response)
def get_entity_128(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_128_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 128 not found")
    return res

@router.post("/entity-128", response_model=ResearchSchemaEntity128Response, status_code=201)
def create_entity_128(payload: ResearchSchemaEntity128Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_128(payload)

@router.get("/entity-129", response_model=List[ResearchSchemaEntity129Response])
def list_entities_129(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_129_list(skip=skip, limit=limit)

@router.get("/entity-129/{entity_id}", response_model=ResearchSchemaEntity129Response)
def get_entity_129(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_129_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 129 not found")
    return res

@router.post("/entity-129", response_model=ResearchSchemaEntity129Response, status_code=201)
def create_entity_129(payload: ResearchSchemaEntity129Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_129(payload)

@router.get("/entity-130", response_model=List[ResearchSchemaEntity130Response])
def list_entities_130(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_130_list(skip=skip, limit=limit)

@router.get("/entity-130/{entity_id}", response_model=ResearchSchemaEntity130Response)
def get_entity_130(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_130_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 130 not found")
    return res

@router.post("/entity-130", response_model=ResearchSchemaEntity130Response, status_code=201)
def create_entity_130(payload: ResearchSchemaEntity130Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_130(payload)

@router.get("/entity-131", response_model=List[ResearchSchemaEntity131Response])
def list_entities_131(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_131_list(skip=skip, limit=limit)

@router.get("/entity-131/{entity_id}", response_model=ResearchSchemaEntity131Response)
def get_entity_131(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_131_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 131 not found")
    return res

@router.post("/entity-131", response_model=ResearchSchemaEntity131Response, status_code=201)
def create_entity_131(payload: ResearchSchemaEntity131Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_131(payload)

@router.get("/entity-132", response_model=List[ResearchSchemaEntity132Response])
def list_entities_132(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_132_list(skip=skip, limit=limit)

@router.get("/entity-132/{entity_id}", response_model=ResearchSchemaEntity132Response)
def get_entity_132(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_132_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 132 not found")
    return res

@router.post("/entity-132", response_model=ResearchSchemaEntity132Response, status_code=201)
def create_entity_132(payload: ResearchSchemaEntity132Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_132(payload)

@router.get("/entity-133", response_model=List[ResearchSchemaEntity133Response])
def list_entities_133(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_133_list(skip=skip, limit=limit)

@router.get("/entity-133/{entity_id}", response_model=ResearchSchemaEntity133Response)
def get_entity_133(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_133_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 133 not found")
    return res

@router.post("/entity-133", response_model=ResearchSchemaEntity133Response, status_code=201)
def create_entity_133(payload: ResearchSchemaEntity133Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_133(payload)

@router.get("/entity-134", response_model=List[ResearchSchemaEntity134Response])
def list_entities_134(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_134_list(skip=skip, limit=limit)

@router.get("/entity-134/{entity_id}", response_model=ResearchSchemaEntity134Response)
def get_entity_134(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_134_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 134 not found")
    return res

@router.post("/entity-134", response_model=ResearchSchemaEntity134Response, status_code=201)
def create_entity_134(payload: ResearchSchemaEntity134Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_134(payload)

@router.get("/entity-135", response_model=List[ResearchSchemaEntity135Response])
def list_entities_135(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_135_list(skip=skip, limit=limit)

@router.get("/entity-135/{entity_id}", response_model=ResearchSchemaEntity135Response)
def get_entity_135(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_135_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 135 not found")
    return res

@router.post("/entity-135", response_model=ResearchSchemaEntity135Response, status_code=201)
def create_entity_135(payload: ResearchSchemaEntity135Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_135(payload)

@router.get("/entity-136", response_model=List[ResearchSchemaEntity136Response])
def list_entities_136(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_136_list(skip=skip, limit=limit)

@router.get("/entity-136/{entity_id}", response_model=ResearchSchemaEntity136Response)
def get_entity_136(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_136_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 136 not found")
    return res

@router.post("/entity-136", response_model=ResearchSchemaEntity136Response, status_code=201)
def create_entity_136(payload: ResearchSchemaEntity136Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_136(payload)

@router.get("/entity-137", response_model=List[ResearchSchemaEntity137Response])
def list_entities_137(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_137_list(skip=skip, limit=limit)

@router.get("/entity-137/{entity_id}", response_model=ResearchSchemaEntity137Response)
def get_entity_137(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_137_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 137 not found")
    return res

@router.post("/entity-137", response_model=ResearchSchemaEntity137Response, status_code=201)
def create_entity_137(payload: ResearchSchemaEntity137Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_137(payload)

@router.get("/entity-138", response_model=List[ResearchSchemaEntity138Response])
def list_entities_138(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_138_list(skip=skip, limit=limit)

@router.get("/entity-138/{entity_id}", response_model=ResearchSchemaEntity138Response)
def get_entity_138(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_138_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 138 not found")
    return res

@router.post("/entity-138", response_model=ResearchSchemaEntity138Response, status_code=201)
def create_entity_138(payload: ResearchSchemaEntity138Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_138(payload)

@router.get("/entity-139", response_model=List[ResearchSchemaEntity139Response])
def list_entities_139(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_139_list(skip=skip, limit=limit)

@router.get("/entity-139/{entity_id}", response_model=ResearchSchemaEntity139Response)
def get_entity_139(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_139_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 139 not found")
    return res

@router.post("/entity-139", response_model=ResearchSchemaEntity139Response, status_code=201)
def create_entity_139(payload: ResearchSchemaEntity139Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_139(payload)

@router.get("/entity-140", response_model=List[ResearchSchemaEntity140Response])
def list_entities_140(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_140_list(skip=skip, limit=limit)

@router.get("/entity-140/{entity_id}", response_model=ResearchSchemaEntity140Response)
def get_entity_140(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_140_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 140 not found")
    return res

@router.post("/entity-140", response_model=ResearchSchemaEntity140Response, status_code=201)
def create_entity_140(payload: ResearchSchemaEntity140Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_140(payload)

@router.get("/entity-141", response_model=List[ResearchSchemaEntity141Response])
def list_entities_141(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_141_list(skip=skip, limit=limit)

@router.get("/entity-141/{entity_id}", response_model=ResearchSchemaEntity141Response)
def get_entity_141(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_141_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 141 not found")
    return res

@router.post("/entity-141", response_model=ResearchSchemaEntity141Response, status_code=201)
def create_entity_141(payload: ResearchSchemaEntity141Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_141(payload)

@router.get("/entity-142", response_model=List[ResearchSchemaEntity142Response])
def list_entities_142(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_142_list(skip=skip, limit=limit)

@router.get("/entity-142/{entity_id}", response_model=ResearchSchemaEntity142Response)
def get_entity_142(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_142_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 142 not found")
    return res

@router.post("/entity-142", response_model=ResearchSchemaEntity142Response, status_code=201)
def create_entity_142(payload: ResearchSchemaEntity142Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_142(payload)

@router.get("/entity-143", response_model=List[ResearchSchemaEntity143Response])
def list_entities_143(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_143_list(skip=skip, limit=limit)

@router.get("/entity-143/{entity_id}", response_model=ResearchSchemaEntity143Response)
def get_entity_143(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_143_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 143 not found")
    return res

@router.post("/entity-143", response_model=ResearchSchemaEntity143Response, status_code=201)
def create_entity_143(payload: ResearchSchemaEntity143Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_143(payload)

@router.get("/entity-144", response_model=List[ResearchSchemaEntity144Response])
def list_entities_144(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_144_list(skip=skip, limit=limit)

@router.get("/entity-144/{entity_id}", response_model=ResearchSchemaEntity144Response)
def get_entity_144(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_144_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 144 not found")
    return res

@router.post("/entity-144", response_model=ResearchSchemaEntity144Response, status_code=201)
def create_entity_144(payload: ResearchSchemaEntity144Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_144(payload)

@router.get("/entity-145", response_model=List[ResearchSchemaEntity145Response])
def list_entities_145(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_145_list(skip=skip, limit=limit)

@router.get("/entity-145/{entity_id}", response_model=ResearchSchemaEntity145Response)
def get_entity_145(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_145_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 145 not found")
    return res

@router.post("/entity-145", response_model=ResearchSchemaEntity145Response, status_code=201)
def create_entity_145(payload: ResearchSchemaEntity145Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_145(payload)

@router.get("/entity-146", response_model=List[ResearchSchemaEntity146Response])
def list_entities_146(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_146_list(skip=skip, limit=limit)

@router.get("/entity-146/{entity_id}", response_model=ResearchSchemaEntity146Response)
def get_entity_146(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_146_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 146 not found")
    return res

@router.post("/entity-146", response_model=ResearchSchemaEntity146Response, status_code=201)
def create_entity_146(payload: ResearchSchemaEntity146Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_146(payload)

@router.get("/entity-147", response_model=List[ResearchSchemaEntity147Response])
def list_entities_147(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_147_list(skip=skip, limit=limit)

@router.get("/entity-147/{entity_id}", response_model=ResearchSchemaEntity147Response)
def get_entity_147(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_147_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 147 not found")
    return res

@router.post("/entity-147", response_model=ResearchSchemaEntity147Response, status_code=201)
def create_entity_147(payload: ResearchSchemaEntity147Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_147(payload)

@router.get("/entity-148", response_model=List[ResearchSchemaEntity148Response])
def list_entities_148(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_148_list(skip=skip, limit=limit)

@router.get("/entity-148/{entity_id}", response_model=ResearchSchemaEntity148Response)
def get_entity_148(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_148_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 148 not found")
    return res

@router.post("/entity-148", response_model=ResearchSchemaEntity148Response, status_code=201)
def create_entity_148(payload: ResearchSchemaEntity148Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_148(payload)

@router.get("/entity-149", response_model=List[ResearchSchemaEntity149Response])
def list_entities_149(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_149_list(skip=skip, limit=limit)

@router.get("/entity-149/{entity_id}", response_model=ResearchSchemaEntity149Response)
def get_entity_149(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_149_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 149 not found")
    return res

@router.post("/entity-149", response_model=ResearchSchemaEntity149Response, status_code=201)
def create_entity_149(payload: ResearchSchemaEntity149Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_149(payload)

@router.get("/entity-150", response_model=List[ResearchSchemaEntity150Response])
def list_entities_150(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_150_list(skip=skip, limit=limit)

@router.get("/entity-150/{entity_id}", response_model=ResearchSchemaEntity150Response)
def get_entity_150(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_150_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 150 not found")
    return res

@router.post("/entity-150", response_model=ResearchSchemaEntity150Response, status_code=201)
def create_entity_150(payload: ResearchSchemaEntity150Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_150(payload)

@router.get("/entity-151", response_model=List[ResearchSchemaEntity151Response])
def list_entities_151(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_151_list(skip=skip, limit=limit)

@router.get("/entity-151/{entity_id}", response_model=ResearchSchemaEntity151Response)
def get_entity_151(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_151_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 151 not found")
    return res

@router.post("/entity-151", response_model=ResearchSchemaEntity151Response, status_code=201)
def create_entity_151(payload: ResearchSchemaEntity151Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_151(payload)

@router.get("/entity-152", response_model=List[ResearchSchemaEntity152Response])
def list_entities_152(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_152_list(skip=skip, limit=limit)

@router.get("/entity-152/{entity_id}", response_model=ResearchSchemaEntity152Response)
def get_entity_152(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_152_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 152 not found")
    return res

@router.post("/entity-152", response_model=ResearchSchemaEntity152Response, status_code=201)
def create_entity_152(payload: ResearchSchemaEntity152Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_152(payload)

@router.get("/entity-153", response_model=List[ResearchSchemaEntity153Response])
def list_entities_153(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_153_list(skip=skip, limit=limit)

@router.get("/entity-153/{entity_id}", response_model=ResearchSchemaEntity153Response)
def get_entity_153(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_153_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 153 not found")
    return res

@router.post("/entity-153", response_model=ResearchSchemaEntity153Response, status_code=201)
def create_entity_153(payload: ResearchSchemaEntity153Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_153(payload)

@router.get("/entity-154", response_model=List[ResearchSchemaEntity154Response])
def list_entities_154(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_154_list(skip=skip, limit=limit)

@router.get("/entity-154/{entity_id}", response_model=ResearchSchemaEntity154Response)
def get_entity_154(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_154_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 154 not found")
    return res

@router.post("/entity-154", response_model=ResearchSchemaEntity154Response, status_code=201)
def create_entity_154(payload: ResearchSchemaEntity154Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_154(payload)

@router.get("/entity-155", response_model=List[ResearchSchemaEntity155Response])
def list_entities_155(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_155_list(skip=skip, limit=limit)

@router.get("/entity-155/{entity_id}", response_model=ResearchSchemaEntity155Response)
def get_entity_155(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_155_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 155 not found")
    return res

@router.post("/entity-155", response_model=ResearchSchemaEntity155Response, status_code=201)
def create_entity_155(payload: ResearchSchemaEntity155Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_155(payload)

@router.get("/entity-156", response_model=List[ResearchSchemaEntity156Response])
def list_entities_156(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_156_list(skip=skip, limit=limit)

@router.get("/entity-156/{entity_id}", response_model=ResearchSchemaEntity156Response)
def get_entity_156(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_156_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 156 not found")
    return res

@router.post("/entity-156", response_model=ResearchSchemaEntity156Response, status_code=201)
def create_entity_156(payload: ResearchSchemaEntity156Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_156(payload)

@router.get("/entity-157", response_model=List[ResearchSchemaEntity157Response])
def list_entities_157(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_157_list(skip=skip, limit=limit)

@router.get("/entity-157/{entity_id}", response_model=ResearchSchemaEntity157Response)
def get_entity_157(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_157_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 157 not found")
    return res

@router.post("/entity-157", response_model=ResearchSchemaEntity157Response, status_code=201)
def create_entity_157(payload: ResearchSchemaEntity157Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_157(payload)

@router.get("/entity-158", response_model=List[ResearchSchemaEntity158Response])
def list_entities_158(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_158_list(skip=skip, limit=limit)

@router.get("/entity-158/{entity_id}", response_model=ResearchSchemaEntity158Response)
def get_entity_158(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_158_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 158 not found")
    return res

@router.post("/entity-158", response_model=ResearchSchemaEntity158Response, status_code=201)
def create_entity_158(payload: ResearchSchemaEntity158Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_158(payload)

@router.get("/entity-159", response_model=List[ResearchSchemaEntity159Response])
def list_entities_159(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_159_list(skip=skip, limit=limit)

@router.get("/entity-159/{entity_id}", response_model=ResearchSchemaEntity159Response)
def get_entity_159(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_159_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 159 not found")
    return res

@router.post("/entity-159", response_model=ResearchSchemaEntity159Response, status_code=201)
def create_entity_159(payload: ResearchSchemaEntity159Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_159(payload)

@router.get("/entity-160", response_model=List[ResearchSchemaEntity160Response])
def list_entities_160(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_160_list(skip=skip, limit=limit)

@router.get("/entity-160/{entity_id}", response_model=ResearchSchemaEntity160Response)
def get_entity_160(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_160_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 160 not found")
    return res

@router.post("/entity-160", response_model=ResearchSchemaEntity160Response, status_code=201)
def create_entity_160(payload: ResearchSchemaEntity160Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_160(payload)

@router.get("/entity-161", response_model=List[ResearchSchemaEntity161Response])
def list_entities_161(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_161_list(skip=skip, limit=limit)

@router.get("/entity-161/{entity_id}", response_model=ResearchSchemaEntity161Response)
def get_entity_161(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_161_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 161 not found")
    return res

@router.post("/entity-161", response_model=ResearchSchemaEntity161Response, status_code=201)
def create_entity_161(payload: ResearchSchemaEntity161Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_161(payload)

@router.get("/entity-162", response_model=List[ResearchSchemaEntity162Response])
def list_entities_162(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_162_list(skip=skip, limit=limit)

@router.get("/entity-162/{entity_id}", response_model=ResearchSchemaEntity162Response)
def get_entity_162(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_162_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 162 not found")
    return res

@router.post("/entity-162", response_model=ResearchSchemaEntity162Response, status_code=201)
def create_entity_162(payload: ResearchSchemaEntity162Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_162(payload)

@router.get("/entity-163", response_model=List[ResearchSchemaEntity163Response])
def list_entities_163(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_163_list(skip=skip, limit=limit)

@router.get("/entity-163/{entity_id}", response_model=ResearchSchemaEntity163Response)
def get_entity_163(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_163_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 163 not found")
    return res

@router.post("/entity-163", response_model=ResearchSchemaEntity163Response, status_code=201)
def create_entity_163(payload: ResearchSchemaEntity163Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_163(payload)

@router.get("/entity-164", response_model=List[ResearchSchemaEntity164Response])
def list_entities_164(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_164_list(skip=skip, limit=limit)

@router.get("/entity-164/{entity_id}", response_model=ResearchSchemaEntity164Response)
def get_entity_164(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_164_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 164 not found")
    return res

@router.post("/entity-164", response_model=ResearchSchemaEntity164Response, status_code=201)
def create_entity_164(payload: ResearchSchemaEntity164Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_164(payload)

@router.get("/entity-165", response_model=List[ResearchSchemaEntity165Response])
def list_entities_165(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_165_list(skip=skip, limit=limit)

@router.get("/entity-165/{entity_id}", response_model=ResearchSchemaEntity165Response)
def get_entity_165(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_165_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 165 not found")
    return res

@router.post("/entity-165", response_model=ResearchSchemaEntity165Response, status_code=201)
def create_entity_165(payload: ResearchSchemaEntity165Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_165(payload)

@router.get("/entity-166", response_model=List[ResearchSchemaEntity166Response])
def list_entities_166(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_166_list(skip=skip, limit=limit)

@router.get("/entity-166/{entity_id}", response_model=ResearchSchemaEntity166Response)
def get_entity_166(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_166_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 166 not found")
    return res

@router.post("/entity-166", response_model=ResearchSchemaEntity166Response, status_code=201)
def create_entity_166(payload: ResearchSchemaEntity166Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_166(payload)

@router.get("/entity-167", response_model=List[ResearchSchemaEntity167Response])
def list_entities_167(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_167_list(skip=skip, limit=limit)

@router.get("/entity-167/{entity_id}", response_model=ResearchSchemaEntity167Response)
def get_entity_167(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_167_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 167 not found")
    return res

@router.post("/entity-167", response_model=ResearchSchemaEntity167Response, status_code=201)
def create_entity_167(payload: ResearchSchemaEntity167Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_167(payload)

@router.get("/entity-168", response_model=List[ResearchSchemaEntity168Response])
def list_entities_168(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_168_list(skip=skip, limit=limit)

@router.get("/entity-168/{entity_id}", response_model=ResearchSchemaEntity168Response)
def get_entity_168(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_168_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 168 not found")
    return res

@router.post("/entity-168", response_model=ResearchSchemaEntity168Response, status_code=201)
def create_entity_168(payload: ResearchSchemaEntity168Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_168(payload)

@router.get("/entity-169", response_model=List[ResearchSchemaEntity169Response])
def list_entities_169(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_169_list(skip=skip, limit=limit)

@router.get("/entity-169/{entity_id}", response_model=ResearchSchemaEntity169Response)
def get_entity_169(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_169_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 169 not found")
    return res

@router.post("/entity-169", response_model=ResearchSchemaEntity169Response, status_code=201)
def create_entity_169(payload: ResearchSchemaEntity169Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_169(payload)

@router.get("/entity-170", response_model=List[ResearchSchemaEntity170Response])
def list_entities_170(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_170_list(skip=skip, limit=limit)

@router.get("/entity-170/{entity_id}", response_model=ResearchSchemaEntity170Response)
def get_entity_170(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_170_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 170 not found")
    return res

@router.post("/entity-170", response_model=ResearchSchemaEntity170Response, status_code=201)
def create_entity_170(payload: ResearchSchemaEntity170Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_170(payload)

@router.get("/entity-171", response_model=List[ResearchSchemaEntity171Response])
def list_entities_171(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_171_list(skip=skip, limit=limit)

@router.get("/entity-171/{entity_id}", response_model=ResearchSchemaEntity171Response)
def get_entity_171(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_171_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 171 not found")
    return res

@router.post("/entity-171", response_model=ResearchSchemaEntity171Response, status_code=201)
def create_entity_171(payload: ResearchSchemaEntity171Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_171(payload)

@router.get("/entity-172", response_model=List[ResearchSchemaEntity172Response])
def list_entities_172(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_172_list(skip=skip, limit=limit)

@router.get("/entity-172/{entity_id}", response_model=ResearchSchemaEntity172Response)
def get_entity_172(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_172_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 172 not found")
    return res

@router.post("/entity-172", response_model=ResearchSchemaEntity172Response, status_code=201)
def create_entity_172(payload: ResearchSchemaEntity172Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_172(payload)

@router.get("/entity-173", response_model=List[ResearchSchemaEntity173Response])
def list_entities_173(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_173_list(skip=skip, limit=limit)

@router.get("/entity-173/{entity_id}", response_model=ResearchSchemaEntity173Response)
def get_entity_173(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_173_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 173 not found")
    return res

@router.post("/entity-173", response_model=ResearchSchemaEntity173Response, status_code=201)
def create_entity_173(payload: ResearchSchemaEntity173Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_173(payload)

@router.get("/entity-174", response_model=List[ResearchSchemaEntity174Response])
def list_entities_174(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_174_list(skip=skip, limit=limit)

@router.get("/entity-174/{entity_id}", response_model=ResearchSchemaEntity174Response)
def get_entity_174(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_174_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 174 not found")
    return res

@router.post("/entity-174", response_model=ResearchSchemaEntity174Response, status_code=201)
def create_entity_174(payload: ResearchSchemaEntity174Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_174(payload)

@router.get("/entity-175", response_model=List[ResearchSchemaEntity175Response])
def list_entities_175(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_175_list(skip=skip, limit=limit)

@router.get("/entity-175/{entity_id}", response_model=ResearchSchemaEntity175Response)
def get_entity_175(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_175_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 175 not found")
    return res

@router.post("/entity-175", response_model=ResearchSchemaEntity175Response, status_code=201)
def create_entity_175(payload: ResearchSchemaEntity175Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_175(payload)

@router.get("/entity-176", response_model=List[ResearchSchemaEntity176Response])
def list_entities_176(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_176_list(skip=skip, limit=limit)

@router.get("/entity-176/{entity_id}", response_model=ResearchSchemaEntity176Response)
def get_entity_176(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_176_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 176 not found")
    return res

@router.post("/entity-176", response_model=ResearchSchemaEntity176Response, status_code=201)
def create_entity_176(payload: ResearchSchemaEntity176Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_176(payload)

@router.get("/entity-177", response_model=List[ResearchSchemaEntity177Response])
def list_entities_177(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_177_list(skip=skip, limit=limit)

@router.get("/entity-177/{entity_id}", response_model=ResearchSchemaEntity177Response)
def get_entity_177(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_177_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 177 not found")
    return res

@router.post("/entity-177", response_model=ResearchSchemaEntity177Response, status_code=201)
def create_entity_177(payload: ResearchSchemaEntity177Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_177(payload)

@router.get("/entity-178", response_model=List[ResearchSchemaEntity178Response])
def list_entities_178(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_178_list(skip=skip, limit=limit)

@router.get("/entity-178/{entity_id}", response_model=ResearchSchemaEntity178Response)
def get_entity_178(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_178_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 178 not found")
    return res

@router.post("/entity-178", response_model=ResearchSchemaEntity178Response, status_code=201)
def create_entity_178(payload: ResearchSchemaEntity178Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_178(payload)

@router.get("/entity-179", response_model=List[ResearchSchemaEntity179Response])
def list_entities_179(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_179_list(skip=skip, limit=limit)

@router.get("/entity-179/{entity_id}", response_model=ResearchSchemaEntity179Response)
def get_entity_179(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_179_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 179 not found")
    return res

@router.post("/entity-179", response_model=ResearchSchemaEntity179Response, status_code=201)
def create_entity_179(payload: ResearchSchemaEntity179Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_179(payload)

@router.get("/entity-180", response_model=List[ResearchSchemaEntity180Response])
def list_entities_180(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_180_list(skip=skip, limit=limit)

@router.get("/entity-180/{entity_id}", response_model=ResearchSchemaEntity180Response)
def get_entity_180(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_180_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 180 not found")
    return res

@router.post("/entity-180", response_model=ResearchSchemaEntity180Response, status_code=201)
def create_entity_180(payload: ResearchSchemaEntity180Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_180(payload)

@router.get("/entity-181", response_model=List[ResearchSchemaEntity181Response])
def list_entities_181(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_181_list(skip=skip, limit=limit)

@router.get("/entity-181/{entity_id}", response_model=ResearchSchemaEntity181Response)
def get_entity_181(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_181_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 181 not found")
    return res

@router.post("/entity-181", response_model=ResearchSchemaEntity181Response, status_code=201)
def create_entity_181(payload: ResearchSchemaEntity181Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_181(payload)

@router.get("/entity-182", response_model=List[ResearchSchemaEntity182Response])
def list_entities_182(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_182_list(skip=skip, limit=limit)

@router.get("/entity-182/{entity_id}", response_model=ResearchSchemaEntity182Response)
def get_entity_182(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_182_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 182 not found")
    return res

@router.post("/entity-182", response_model=ResearchSchemaEntity182Response, status_code=201)
def create_entity_182(payload: ResearchSchemaEntity182Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_182(payload)

@router.get("/entity-183", response_model=List[ResearchSchemaEntity183Response])
def list_entities_183(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_183_list(skip=skip, limit=limit)

@router.get("/entity-183/{entity_id}", response_model=ResearchSchemaEntity183Response)
def get_entity_183(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_183_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 183 not found")
    return res

@router.post("/entity-183", response_model=ResearchSchemaEntity183Response, status_code=201)
def create_entity_183(payload: ResearchSchemaEntity183Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_183(payload)

@router.get("/entity-184", response_model=List[ResearchSchemaEntity184Response])
def list_entities_184(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_184_list(skip=skip, limit=limit)

@router.get("/entity-184/{entity_id}", response_model=ResearchSchemaEntity184Response)
def get_entity_184(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_184_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 184 not found")
    return res

@router.post("/entity-184", response_model=ResearchSchemaEntity184Response, status_code=201)
def create_entity_184(payload: ResearchSchemaEntity184Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_184(payload)

@router.get("/entity-185", response_model=List[ResearchSchemaEntity185Response])
def list_entities_185(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_185_list(skip=skip, limit=limit)

@router.get("/entity-185/{entity_id}", response_model=ResearchSchemaEntity185Response)
def get_entity_185(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_185_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 185 not found")
    return res

@router.post("/entity-185", response_model=ResearchSchemaEntity185Response, status_code=201)
def create_entity_185(payload: ResearchSchemaEntity185Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_185(payload)

@router.get("/entity-186", response_model=List[ResearchSchemaEntity186Response])
def list_entities_186(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_186_list(skip=skip, limit=limit)

@router.get("/entity-186/{entity_id}", response_model=ResearchSchemaEntity186Response)
def get_entity_186(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_186_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 186 not found")
    return res

@router.post("/entity-186", response_model=ResearchSchemaEntity186Response, status_code=201)
def create_entity_186(payload: ResearchSchemaEntity186Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_186(payload)

@router.get("/entity-187", response_model=List[ResearchSchemaEntity187Response])
def list_entities_187(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_187_list(skip=skip, limit=limit)

@router.get("/entity-187/{entity_id}", response_model=ResearchSchemaEntity187Response)
def get_entity_187(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_187_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 187 not found")
    return res

@router.post("/entity-187", response_model=ResearchSchemaEntity187Response, status_code=201)
def create_entity_187(payload: ResearchSchemaEntity187Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_187(payload)

@router.get("/entity-188", response_model=List[ResearchSchemaEntity188Response])
def list_entities_188(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_188_list(skip=skip, limit=limit)

@router.get("/entity-188/{entity_id}", response_model=ResearchSchemaEntity188Response)
def get_entity_188(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_188_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 188 not found")
    return res

@router.post("/entity-188", response_model=ResearchSchemaEntity188Response, status_code=201)
def create_entity_188(payload: ResearchSchemaEntity188Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_188(payload)

@router.get("/entity-189", response_model=List[ResearchSchemaEntity189Response])
def list_entities_189(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_189_list(skip=skip, limit=limit)

@router.get("/entity-189/{entity_id}", response_model=ResearchSchemaEntity189Response)
def get_entity_189(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_189_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 189 not found")
    return res

@router.post("/entity-189", response_model=ResearchSchemaEntity189Response, status_code=201)
def create_entity_189(payload: ResearchSchemaEntity189Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_189(payload)

@router.get("/entity-190", response_model=List[ResearchSchemaEntity190Response])
def list_entities_190(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_190_list(skip=skip, limit=limit)

@router.get("/entity-190/{entity_id}", response_model=ResearchSchemaEntity190Response)
def get_entity_190(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_190_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 190 not found")
    return res

@router.post("/entity-190", response_model=ResearchSchemaEntity190Response, status_code=201)
def create_entity_190(payload: ResearchSchemaEntity190Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_190(payload)

@router.get("/entity-191", response_model=List[ResearchSchemaEntity191Response])
def list_entities_191(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_191_list(skip=skip, limit=limit)

@router.get("/entity-191/{entity_id}", response_model=ResearchSchemaEntity191Response)
def get_entity_191(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_191_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 191 not found")
    return res

@router.post("/entity-191", response_model=ResearchSchemaEntity191Response, status_code=201)
def create_entity_191(payload: ResearchSchemaEntity191Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_191(payload)

@router.get("/entity-192", response_model=List[ResearchSchemaEntity192Response])
def list_entities_192(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_192_list(skip=skip, limit=limit)

@router.get("/entity-192/{entity_id}", response_model=ResearchSchemaEntity192Response)
def get_entity_192(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_192_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 192 not found")
    return res

@router.post("/entity-192", response_model=ResearchSchemaEntity192Response, status_code=201)
def create_entity_192(payload: ResearchSchemaEntity192Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_192(payload)

@router.get("/entity-193", response_model=List[ResearchSchemaEntity193Response])
def list_entities_193(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_193_list(skip=skip, limit=limit)

@router.get("/entity-193/{entity_id}", response_model=ResearchSchemaEntity193Response)
def get_entity_193(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_193_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 193 not found")
    return res

@router.post("/entity-193", response_model=ResearchSchemaEntity193Response, status_code=201)
def create_entity_193(payload: ResearchSchemaEntity193Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_193(payload)

@router.get("/entity-194", response_model=List[ResearchSchemaEntity194Response])
def list_entities_194(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_194_list(skip=skip, limit=limit)

@router.get("/entity-194/{entity_id}", response_model=ResearchSchemaEntity194Response)
def get_entity_194(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_194_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 194 not found")
    return res

@router.post("/entity-194", response_model=ResearchSchemaEntity194Response, status_code=201)
def create_entity_194(payload: ResearchSchemaEntity194Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_194(payload)

@router.get("/entity-195", response_model=List[ResearchSchemaEntity195Response])
def list_entities_195(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_195_list(skip=skip, limit=limit)

@router.get("/entity-195/{entity_id}", response_model=ResearchSchemaEntity195Response)
def get_entity_195(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_195_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 195 not found")
    return res

@router.post("/entity-195", response_model=ResearchSchemaEntity195Response, status_code=201)
def create_entity_195(payload: ResearchSchemaEntity195Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_195(payload)

@router.get("/entity-196", response_model=List[ResearchSchemaEntity196Response])
def list_entities_196(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_196_list(skip=skip, limit=limit)

@router.get("/entity-196/{entity_id}", response_model=ResearchSchemaEntity196Response)
def get_entity_196(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_196_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 196 not found")
    return res

@router.post("/entity-196", response_model=ResearchSchemaEntity196Response, status_code=201)
def create_entity_196(payload: ResearchSchemaEntity196Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_196(payload)

@router.get("/entity-197", response_model=List[ResearchSchemaEntity197Response])
def list_entities_197(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_197_list(skip=skip, limit=limit)

@router.get("/entity-197/{entity_id}", response_model=ResearchSchemaEntity197Response)
def get_entity_197(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_197_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 197 not found")
    return res

@router.post("/entity-197", response_model=ResearchSchemaEntity197Response, status_code=201)
def create_entity_197(payload: ResearchSchemaEntity197Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_197(payload)

@router.get("/entity-198", response_model=List[ResearchSchemaEntity198Response])
def list_entities_198(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_198_list(skip=skip, limit=limit)

@router.get("/entity-198/{entity_id}", response_model=ResearchSchemaEntity198Response)
def get_entity_198(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_198_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 198 not found")
    return res

@router.post("/entity-198", response_model=ResearchSchemaEntity198Response, status_code=201)
def create_entity_198(payload: ResearchSchemaEntity198Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_198(payload)

@router.get("/entity-199", response_model=List[ResearchSchemaEntity199Response])
def list_entities_199(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_199_list(skip=skip, limit=limit)

@router.get("/entity-199/{entity_id}", response_model=ResearchSchemaEntity199Response)
def get_entity_199(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_199_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 199 not found")
    return res

@router.post("/entity-199", response_model=ResearchSchemaEntity199Response, status_code=201)
def create_entity_199(payload: ResearchSchemaEntity199Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_199(payload)

@router.get("/entity-200", response_model=List[ResearchSchemaEntity200Response])
def list_entities_200(skip: int = Query(0), limit: int = Query(100), db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.get_entity_200_list(skip=skip, limit=limit)

@router.get("/entity-200/{entity_id}", response_model=ResearchSchemaEntity200Response)
def get_entity_200(entity_id: int, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    res = srv.get_entity_200_by_id(entity_id)
    if not res:
        raise HTTPException(status_code=404, detail=f"Entity 200 not found")
    return res

@router.post("/entity-200", response_model=ResearchSchemaEntity200Response, status_code=201)
def create_entity_200(payload: ResearchSchemaEntity200Create, db: Session = Depends(get_db)):
    srv = ResearchDomainService(db)
    return srv.create_entity_200(payload)

