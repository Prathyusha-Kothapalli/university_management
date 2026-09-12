import uuid
from datetime import datetime
from typing import List, Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.student_lifecycle import (
    AcademicHold,
    StudentConductCase,
    StudentAchievement,
    SupportCase,
    AcademicGoal,
)
from app.schemas.student_lifecycle import (
    AcademicHoldCreate,
    StudentConductCaseCreate,
    SupportCaseCreate,
)


def place_academic_hold(
    db: Session,
    placed_by_id: uuid.UUID,
    hold_data: AcademicHoldCreate
) -> AcademicHold:
    hold = AcademicHold(
        student_id=hold_data.student_id,
        hold_type=hold_data.hold_type,
        reason=hold_data.reason,
        placed_by_id=placed_by_id,
        is_active=True
    )
    db.add(hold)
    db.commit()
    db.refresh(hold)
    return hold


def resolve_academic_hold(db: Session, hold_id: uuid.UUID) -> Optional[AcademicHold]:
    hold = db.get(AcademicHold, hold_id)
    if not hold:
        return None

    hold.is_active = False
    hold.resolved_at = datetime.utcnow()
    db.commit()
    db.refresh(hold)
    return hold


def get_active_student_holds(db: Session, student_id: uuid.UUID) -> List[AcademicHold]:
    return db.execute(
        select(AcademicHold).where(
            and_(AcademicHold.student_id == student_id, AcademicHold.is_active == True)
        )
    ).scalars().all()


def record_disciplinary_incident(
    db: Session,
    reported_by_id: uuid.UUID,
    data: StudentConductCaseCreate
) -> StudentConductCase:
    record = StudentConductCase(
        student_id=data.student_id,
        incident_title=data.incident_title,
        incident_description=data.incident_description,
        severity=data.severity,
        action_taken=data.action_taken,
        reported_by_id=reported_by_id,
        status="UNDER_INVESTIGATION"
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def create_support_case(db: Session, data: SupportCaseCreate) -> SupportCase:
    case_obj = SupportCase(
        student_id=data.student_id,
        subject=data.subject,
        category=data.category,
        priority=data.priority,
        details=data.details,
        status="OPEN"
    )
    db.add(case_obj)
    db.commit()
    db.refresh(case_obj)
    return case_obj
