import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_faculty_publication_indexing():
    faculty_id = str(uuid.uuid4())
    pub_payload = {
        "title": "Autonomous Multi-Tenant University Management Architectures",
        "journal": "ACM Transactions on Autonomous and Adaptive Systems",
        "doi": "10.1145/3600000.3600001",
        "year": 2026,
        "citations": 12
    }

    response = client.post(f"/api/v1/faculty/{faculty_id}/publications", json=pub_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Publication indexed successfully"
    assert data["publication"]["title"] == pub_payload["title"]
    assert "bibtex" in data["publication"]

    # Verify listing
    get_res = client.get(f"/api/v1/faculty/{faculty_id}/publications")
    assert get_res.status_code == 200
    pub_list = get_res.json()
    assert pub_list["total_publications"] >= 1


def test_faculty_grant_allocation():
    faculty_id = str(uuid.uuid4())
    grant_payload = {
        "grant_number": "DARPA-AI-2026",
        "title": "Resilient Multi-Agent Autonomous Systems",
        "funding_agency": "Defense Advanced Research Projects Agency",
        "amount_allocated": 500000.0,
        "duration_months": 24
    }

    response = client.post(f"/api/v1/faculty/{faculty_id}/grants", json=grant_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Research grant allocated successfully"
    assert data["grant"]["amount_allocated"] == 500000.0
    assert data["grant"]["status"] == "ACTIVE"

    # Verify listing
    get_res = client.get(f"/api/v1/faculty/{faculty_id}/grants")
    assert get_res.status_code == 200
    grants_list = get_res.json()
    assert grants_list["total_funding_usd"] >= 500000.0
