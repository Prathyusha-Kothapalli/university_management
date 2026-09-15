"""
UniSphere AI — Digital Certificates & Verification Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_issue_and_verify_certificate():
    issue_payload = {
        "recipient_name": "Eleanor Vance",
        "recipient_email": "eleanor.vance@example.com",
        "certificate_type": "DEGREE",
        "title": "Master of Science in Cybersecurity",
        "description": "Graduated with Highest Distinction"
    }
    issue_res = client.post("/api/v1/digital-certificates/issue", json=issue_payload)
    assert issue_res.status_code == 201
    cert_data = issue_res.json()
    cert_code = cert_data["certificate_number"]

    # Verify public endpoint
    verify_res = client.get(f"/api/v1/digital-certificates/verify/{cert_code}")
    assert verify_res.status_code == 200
    verify_data = verify_res.json()
    assert verify_data["is_valid"] is True
    assert verify_data["recipient_name"] == "Eleanor Vance"
