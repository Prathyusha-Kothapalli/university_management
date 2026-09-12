import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base
from app.database.session import get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_hostel_dashboard_overview():
    response = client.get("/api/v1/hostel/dashboard/overview")
    assert response.status_code == 200
    data = response.json()
    assert "total_hostels" in data
    assert "total_rooms" in data
    assert "total_beds" in data
    assert "occupied_beds" in data
    assert "available_beds" in data
    assert "occupancy_percentage" in data


def test_hostel_kpi_cards():
    response = client.get("/api/v1/hostel/dashboard/kpis")
    assert response.status_code == 200
    data = response.json()
    assert "total_students" in data
    assert "total_residents" in data
    assert "available_beds" in data
    assert "open_complaints" in data
    assert "fee_due" in data


def test_hostel_analytics():
    response = client.get("/api/v1/hostel/dashboard/analytics")
    assert response.status_code == 200
    data = response.json()
    assert "occupancy_by_hostel" in data
    assert "occupancy_by_building" in data
    assert "occupied_vs_available" in data
    assert "fee_analytics" in data


def test_hostel_ai_insights():
    response = client.get("/api/v1/hostel/dashboard/ai-insights")
    assert response.status_code == 200
    data = response.json()
    assert "predicted_next_month_occupancy" in data
    assert "forecasted_bed_demand" in data
    assert "ai_summary" in data


def test_hostel_buildings_api():
    response = client.get("/api/v1/hostel/buildings")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_hostel_applications_api():
    response = client.get("/api/v1/hostel/applications")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_hostel_complaints_api():
    response = client.get("/api/v1/hostel/complaints")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_hostel_maintenance_api():
    response = client.get("/api/v1/hostel/maintenance")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_hostel_visitors_api():
    response = client.get("/api/v1/hostel/visitors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_hostel_mess_api():
    response = client.get("/api/v1/hostel/mess")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
