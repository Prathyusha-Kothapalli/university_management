"""
UniSphere AI — Admissions Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_admissions_quotas():
    response = client.get("/api/v1/admissions/quotas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_submit_admission_application():
    payload = {
        "applicant_name": "Test Applicant",
        "applicant_email": "test.applicant@example.com",
        "applicant_phone": "1234567890",
        "program_id": "prog-cs-101",
        "high_school_gpa": 3.90,
        "standardized_test_score": 94.5,
        "personal_statement": "Aspiring AI engineer."
    }
    response = client.post("/api/v1/admissions/applications", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["applicant_name"] == "Test Applicant"
    assert "application_number" in data
    assert data["status"] == "SUBMITTED"
