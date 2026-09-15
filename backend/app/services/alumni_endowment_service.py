import uuid
from typing import List, Optional
from sqlalchemy import select, func, and_
from sqlalchemy.orm import Session

from app.models.alumni_endowment import (
    AlumniProfile,
    EndowmentFund,
    AlumniDonation,
)
from app.schemas.alumni_endowment import (
    AlumniProfileCreate,
    EndowmentFundCreate,
    DonationCreate,
)


def create_alumni_profile(
    db: Session,
    data: AlumniProfileCreate
) -> AlumniProfile:
    profile = AlumniProfile(
        student_id=data.student_id,
        graduation_year=data.graduation_year,
        current_company=data.current_company,
        current_designation=data.current_designation,
        linkedin_url=data.linkedin_url,
        is_mentor_available=data.is_mentor_available,
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def create_endowment_fund(
    db: Session,
    data: EndowmentFundCreate
) -> EndowmentFund:
    fund = EndowmentFund(
        fund_name=data.fund_name,
        target_amount_usd=data.target_amount_usd,
        current_amount_usd=0.0,
        category=data.category,
        is_active=True,
    )
    db.add(fund)
    db.commit()
    db.refresh(fund)
    return fund


def record_donation(
    db: Session,
    data: DonationCreate
) -> AlumniDonation:
    donation = AlumniDonation(
        alumni_profile_id=data.alumni_profile_id,
        fund_id=data.fund_id,
        amount_usd=data.amount_usd,
        payment_reference=data.payment_reference,
    )
    db.add(donation)

    # Update endowment fund total
    fund = db.get(EndowmentFund, data.fund_id)
    if fund:
        fund.current_amount_usd += data.amount_usd

    db.commit()
    db.refresh(donation)
    return donation
