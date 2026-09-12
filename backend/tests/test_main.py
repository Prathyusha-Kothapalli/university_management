from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "UniSphere AI Backend"


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert data["info"]["title"] == "UniSphere AI Backend"
    assert "/api/v1/assignments/" in data["paths"]
    assert "/api/v1/exams/" in data["paths"]
    assert "/api/v1/fee-structures/" in data["paths"]
    assert "/api/v1/library-books/" in data["paths"]
    assert "/api/v1/hostels/" in data["paths"]
    assert "/api/v1/placement-drives/" in data["paths"]
    assert "/api/v1/health-center/medical-records" in data["paths"]
    assert "/api/v1/canteen/menu-items" in data["paths"]
    assert "/api/v1/lost-and-found/items" in data["paths"]
