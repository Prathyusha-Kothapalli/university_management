from fastapi.testclient import TestClient
from ai.app.main import app as ai_app

client = TestClient(ai_app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "UniSphere AI" in data["service"]

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
