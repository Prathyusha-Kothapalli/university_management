"""
UniSphere AI — Academic Advising Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_advisor_assignments():
    response = client.get("/api/v1/academic-advising/assignments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_trigger_academic_intervention():
    payload = {
        "student_id": "stud-101",
        "risk_level": "HIGH",
        "trigger_reason": "Low Midterm Performance in Calculus",
        "recommended_action": "Mandatory Peer Tutoring 2x per week"
    }
    response = client.post("/api/v1/academic-advising/interventions", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["student_id"] == "stud-101"
    assert data["risk_level"] == "HIGH"
    assert data["is_resolved"] is False
