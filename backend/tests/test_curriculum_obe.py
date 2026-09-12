import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_co_po_mapping():
    payload = {
        "course_code": "CS301",
        "program_code": "BTECH_CS",
        "mappings": {
            "CO1": {"PO1": 3, "PO2": 3},
            "CO2": {"PO2": 2, "PO3": 3}
        }
    }

    response = client.post("/api/v1/curriculum/co-po-mapping", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["mapping"]["course_code"] == "CS301"
    assert data["mapping"]["average_correlation_score"] > 0


def test_accreditation_report():
    response = client.get("/api/v1/curriculum/accreditation-report?framework=NAAC&program_code=BTECH_CS")
    assert response.status_code == 200
    data = response.json()
    assert data["accreditation_body"] == "NAAC"
    assert data["accreditation_grade"] == "A++"
    assert "criteria_compliance" in data
