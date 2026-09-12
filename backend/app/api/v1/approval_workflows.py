from uuid import uuid4
from typing import Dict, Any
from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/approval-workflows",
    tags=["Approval Workflows"]
)


class ApprovalChainCreate(BaseModel):
    name: str
    module_name: str
    description: str
    total_steps: int


@router.post("/chains", status_code=status.HTTP_201_CREATED)
def create_approval_chain(payload: ApprovalChainCreate) -> Dict[str, Any]:
    return {
        "id": str(uuid4()),
        "name": payload.name,
        "module_name": payload.module_name,
        "description": payload.description,
        "total_steps": payload.total_steps
    }
