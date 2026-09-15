import uuid
from typing import List, Optional, Dict
from sqlalchemy import select, func, and_
from sqlalchemy.orm import Session

from app.models.curriculum_obe import (
    CourseOutcome,
    ProgramOutcome,
    CoPoMapping,
    WaitlistEntry,
)
from app.schemas.curriculum_obe import (
    CourseOutcomeCreate,
    ProgramOutcomeCreate,
    CoPoMappingCreate,
)


def create_course_outcome(
    db: Session,
    offering_id: uuid.UUID,
    data: CourseOutcomeCreate
) -> CourseOutcome:
    co = CourseOutcome(
        course_offering_id=offering_id,
        code=data.code,
        description=data.description,
        bloom_taxonomy_level=data.bloom_taxonomy_level,
        target_attainment_pct=data.target_attainment_pct,
    )
    db.add(co)
    db.commit()
    db.refresh(co)
    return co


def create_program_outcome(
    db: Session,
    program_id: uuid.UUID,
    data: ProgramOutcomeCreate
) -> ProgramOutcome:
    po = ProgramOutcome(
        program_id=program_id,
        code=data.code,
        title=data.title,
        description=data.description,
    )
    db.add(po)
    db.commit()
    db.refresh(po)
    return po


def map_co_to_po(
    db: Session,
    data: CoPoMappingCreate
) -> CoPoMapping:
    existing = db.execute(
        select(CoPoMapping).where(
            and_(
                CoPoMapping.course_outcome_id == data.course_outcome_id,
                CoPoMapping.program_outcome_id == data.program_outcome_id,
            )
        )
    ).scalar_one_or_none()

    if existing:
        existing.weight = data.weight
        db.commit()
        db.refresh(existing)
        return existing

    mapping = CoPoMapping(
        course_outcome_id=data.course_outcome_id,
        program_outcome_id=data.program_outcome_id,
        weight=data.weight,
    )
    db.add(mapping)
    db.commit()
    db.refresh(mapping)
    return mapping


def calculate_attainment_matrix(db: Session, offering_id: uuid.UUID) -> List[Dict]:
    cos = db.execute(
        select(CourseOutcome).where(CourseOutcome.course_offering_id == offering_id)
    ).scalars().all()

    matrix = []
    for co in cos:
        mappings = db.execute(
            select(CoPoMapping).where(CoPoMapping.course_outcome_id == co.id)
        ).scalars().all()

        mapped_pos = []
        for m in mappings:
            po = db.get(ProgramOutcome, m.program_outcome_id)
            if po:
                mapped_pos.append({
                    "po_code": po.code,
                    "weight": m.weight
                })

        matrix.append({
            "co_code": co.code,
            "bloom_level": co.bloom_taxonomy_level,
            "target_pct": co.target_attainment_pct,
            "mapped_pos": mapped_pos,
        })
    return matrix


def join_course_waitlist(
    db: Session,
    student_id: uuid.UUID,
    offering_id: uuid.UUID
) -> WaitlistEntry:
    current_count = db.execute(
        select(func.count(WaitlistEntry.id)).where(WaitlistEntry.course_offering_id == offering_id)
    ).scalar() or 0

    entry = WaitlistEntry(
        course_offering_id=offering_id,
        student_id=student_id,
        position=current_count + 1,
        status="WAITLISTED",
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry
