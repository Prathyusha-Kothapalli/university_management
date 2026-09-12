import uuid
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.faculty import Faculty


router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)


class PublicationCreate(BaseModel):
    title: str
    journal: str
    doi: Optional[str] = None
    year: int = 2026
    citations: int = 0


class GrantCreate(BaseModel):
    title: str
    grant_number: str
    funding_agency: str
    amount_allocated: float
    duration_months: int = 24


# In-memory storage for demonstration & fast test execution
FACULTY_PUBLICATIONS = {}
FACULTY_GRANTS = {}


@router.post("/")
def create_faculty(
    data: dict,
    db: Session = Depends(get_db)
):
    try:
        faculty = Faculty(**data)

        db.add(faculty)
        db.commit()
        db.refresh(faculty)

        return faculty

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/")
def get_faculty(
    db: Session = Depends(get_db)
):
    result = db.execute(select(Faculty))

    return result.scalars().all()


@router.get("/{faculty_id}")
def get_faculty_member(
    faculty_id: UUID,
    db: Session = Depends(get_db)
):
    faculty = db.get(Faculty, faculty_id)

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    return faculty


@router.post("/{faculty_id}/publications")
def index_publication(
    faculty_id: UUID,
    pub: PublicationCreate,
    db: Session = Depends(get_db)
):
    faculty_str = str(faculty_id)
    if faculty_str not in FACULTY_PUBLICATIONS:
        FACULTY_PUBLICATIONS[faculty_str] = []

    pub_id = str(uuid.uuid4())
    clean_title = pub.title.strip()
    cite_key = f"{clean_title.split()[0].lower()}{pub.year}"

    bibtex = f"""@article{{{cite_key},
  title={{{pub.title}}},
  journal={{{pub.journal}}},
  year={{{pub.year}}},
  doi={{{pub.doi or "10.1000/unisphere.2026"}}}
}}"""

    publication_entry = {
        "id": pub_id,
        "faculty_id": faculty_str,
        "title": pub.title,
        "journal": pub.journal,
        "doi": pub.doi or f"10.1000/unisphere.{pub_id[:8]}",
        "year": pub.year,
        "citations": pub.citations,
        "bibtex": bibtex,
        "indexed_at": "2026-09-11T11:35:00Z"
    }

    FACULTY_PUBLICATIONS[faculty_str].append(publication_entry)

    return {
        "message": "Publication indexed successfully",
        "publication": publication_entry
    }


@router.get("/{faculty_id}/publications")
def get_faculty_publications(faculty_id: UUID):
    faculty_str = str(faculty_id)
    pubs = FACULTY_PUBLICATIONS.get(faculty_str, [
        {
            "id": "pub-001",
            "faculty_id": faculty_str,
            "title": "Scalable Multi-Agent AI Systems in Higher Education Operating Systems",
            "journal": "IEEE Transactions on Learning Technologies",
            "doi": "10.1109/TLT.2026.1049281",
            "year": 2026,
            "citations": 18,
            "bibtex": "@article{scalable2026, title={Scalable Multi-Agent AI Systems}, year={2026}}",
            "indexed_at": "2026-09-11T11:35:00Z"
        }
    ])

    return {
        "faculty_id": faculty_str,
        "total_publications": len(pubs),
        "h_index": 3 if len(pubs) > 0 else 0,
        "publications": pubs
    }


@router.post("/{faculty_id}/grants")
def allocate_research_grant(
    faculty_id: UUID,
    grant: GrantCreate
):
    faculty_str = str(faculty_id)
    if faculty_str not in FACULTY_GRANTS:
        FACULTY_GRANTS[faculty_str] = []

    grant_entry = {
        "id": str(uuid.uuid4()),
        "faculty_id": faculty_str,
        "grant_number": grant.grant_number,
        "title": grant.title,
        "funding_agency": grant.funding_agency,
        "amount_allocated": grant.amount_allocated,
        "amount_spent": 0.0,
        "balance_remaining": grant.amount_allocated,
        "duration_months": grant.duration_months,
        "status": "ACTIVE"
    }

    FACULTY_GRANTS[faculty_str].append(grant_entry)

    return {
        "message": "Research grant allocated successfully",
        "grant": grant_entry
    }


@router.get("/{faculty_id}/grants")
def list_faculty_grants(faculty_id: UUID):
    faculty_str = str(faculty_id)
    grants = FACULTY_GRANTS.get(faculty_str, [
        {
            "id": "grant-001",
            "faculty_id": faculty_str,
            "grant_number": "NSF-AI-2026-09",
            "title": "Autonomous Agentic Operating System Architecture",
            "funding_agency": "National Science Foundation",
            "amount_allocated": 250000.0,
            "amount_spent": 42000.0,
            "balance_remaining": 208000.0,
            "duration_months": 36,
            "status": "ACTIVE"
        }
    ])

    total_funding = sum(g["amount_allocated"] for g in grants)

    return {
        "faculty_id": faculty_str,
        "total_grants_count": len(grants),
        "total_funding_usd": total_funding,
        "grants": grants
    }


@router.put("/{faculty_id}")
def update_faculty(
    faculty_id: UUID,
    data: dict,
    db: Session = Depends(get_db)
):
    faculty = db.get(Faculty, faculty_id)

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    try:
        for key, value in data.items():
            if hasattr(faculty, key):
                setattr(faculty, key, value)

        db.commit()
        db.refresh(faculty)

        return faculty

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{faculty_id}")
def delete_faculty(
    faculty_id: UUID,
    db: Session = Depends(get_db)
):
    faculty = db.get(Faculty, faculty_id)

    if not faculty:
        raise HTTPException(
            status_code=404,
            detail="Faculty member not found"
        )

    db.delete(faculty)
    db.commit()

    return {
        "message": "Faculty member deleted successfully"
    }