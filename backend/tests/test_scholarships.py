"""
UniSphere AI — Scholarship Management Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_scholarships():
    response = client.get("/api/v1/scholarships")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_scholarship():
    payload = {
        "title": "Dean's Excellence Award",
        "description": "Award for top performers",
        "scholarship_type": "MERIT",
        "amount_per_student": 5000.0,
        "total_budget": 50000.0,
        "min_gpa_required": 3.75,
        "deadline": "2026-12-31T23:59:59"
    }
    response = client.post("/api/v1/scholarships", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Dean's Excellence Award"
    assert data["remaining_budget"] == 50000.0
