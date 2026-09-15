"""
UniSphere AI — Graduation Audit Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_apply_for_graduation():
    payload = {
        "student_id": "stud-grad-101",
        "program_id": "prog-cs-101",
        "expected_graduation_term": "Spring 2026",
        "credits_completed": 124,
        "cgpa": 3.82
    }
    response = client.post("/api/v1/graduation-audit/apply", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "REQUIREMENTS_MET"
    assert data["committee_approval"] is True
