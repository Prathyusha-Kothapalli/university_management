import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_department_budget_allocation_and_expense_logging():
    dept_id = str(uuid.uuid4())

    # 1. Allocate budget
    alloc_payload = {
        "department_id": dept_id,
        "fiscal_year": "FY2026-27",
        "total_allocated_usd": 200000.0,
        "lab_equipment_allocation": 80000.0,
        "research_grant_allocation": 70000.0,
        "events_conference_allocation": 50000.0
    }

    alloc_res = client.post("/api/v1/department-budgets/allocate", json=alloc_payload)
    assert alloc_res.status_code == 200
    budget_id = alloc_res.json()["budget"]["budget_id"]

    # 2. Log expense
    expense_payload = {
        "budget_id": budget_id,
        "category": "LAB_EQUIPMENT",
        "amount_usd": 15000.0,
        "description": "High Performance GPU Server",
        "vendor_name": "NVIDIA Systems"
    }

    exp_res = client.post("/api/v1/department-budgets/log-expense", json=expense_payload)
    assert exp_res.status_code == 200
    assert exp_res.json()["expense"]["amount_usd"] == 15000.0


def test_accreditation_dossier():
    dept_id = str(uuid.uuid4())
    payload = {
        "department_id": dept_id,
        "framework": "NAAC",
        "self_study_score": 3.85
    }

    response = client.post("/api/v1/accreditation/submit-dossier", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["dossier"]["framework"] == "NAAC"
    assert data["dossier"]["status"] == "SUBMITTED_FOR_AUDIT"
