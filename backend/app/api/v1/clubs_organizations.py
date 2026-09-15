from uuid import uuid4
from typing import List, Dict, Any
from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/clubs",
    tags=["Clubs & Organizations"]
)

_clubs_db: List[Dict[str, Any]] = []


class ClubCreate(BaseModel):
    name: str
    category: str
    description: str
    annual_budget: float


@router.get("", status_code=status.HTTP_200_OK)
@router.get("/", status_code=status.HTTP_200_OK)
def get_clubs() -> List[Dict[str, Any]]:
    return _clubs_db


@router.post("", status_code=status.HTTP_201_CREATED)
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_club(payload: ClubCreate) -> Dict[str, Any]:
    club = {
        "id": str(uuid4()),
        "name": payload.name,
        "category": payload.category,
        "description": payload.description,
        "annual_budget": payload.annual_budget,
        "is_approved": True
    }
    _clubs_db.append(club)
    return club
