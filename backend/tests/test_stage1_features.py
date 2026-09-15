import uuid
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.database.session import get_db

from app.models.health_center import MedicalRecord, HealthAppointment, PharmacyItem, HealthEmergencyAlert
from app.models.canteen import CanteenMenuItem, CanteenOrder, CanteenMealPlan
from app.models.lost_and_found import LostItem, ItemClaim

from app.main import app

# Create SQLite in-memory database engine with StaticPool so all connections share the same memory DB instance
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all registered tables in SQLite memory engine
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Register dependency override before instantiating TestClient
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_health_center_endpoints():
    # Test Medical Records GET
    res = client.get("/api/v1/health-center/medical-records")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

    # Test Pharmacy GET
    res = client.get("/api/v1/health-center/pharmacy")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

    # Test Emergencies GET
    res = client.get("/api/v1/health-center/emergencies")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_canteen_endpoints():
    # Test Menu Items GET
    res = client.get("/api/v1/canteen/menu-items")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

    # Test Orders GET
    res = client.get("/api/v1/canteen/orders")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_lost_and_found_endpoints():
    # Test Lost Items GET
    res = client.get("/api/v1/lost-and-found/items")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

    # Test Claims GET
    res = client.get("/api/v1/lost-and-found/claims")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
