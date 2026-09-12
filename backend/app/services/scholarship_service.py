import uuid
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.scholarship_application import ScholarshipApplication

def evaluate_scholarship_eligibility(gpa: float, family_income: float, merit_rank: int) -> Dict[str, Any]:
    """Evaluates merit vs need-based scholarship qualifications."""
    eligible_awards = []

    if gpa >= 3.8:
        eligible_awards.append({"name": "Presidential Merit Excellence Grant", "amount": 6000.0, "type": "MERIT"})
    elif gpa >= 3.5:
        eligible_awards.append({"name": "Dean's Honor Scholarship", "amount": 3500.0, "type": "MERIT"})

    if family_income < 45000.0:
        eligible_awards.append({"name": "Opportunity Need-Based Financial Aid", "amount": 4500.0, "type": "NEED_BASED"})

    return {
        "gpa": gpa,
        "family_income": family_income,
        "eligible_scholarships_count": len(eligible_awards),
        "eligible_awards": eligible_awards
    }
