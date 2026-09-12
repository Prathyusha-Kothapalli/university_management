"""
UniSphere AI — Clubs & Student Organizations Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_clubs():
    response = client.get("/api/v1/clubs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_club():
    payload = {
        "name": "Robotics & AI Innovation Club",
        "category": "TECHNOLOGY",
        "description": "Building next-gen drones and AI systems.",
        "annual_budget": 15000.0
    }
    response = client.post("/api/v1/clubs", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Robotics & AI Innovation Club"
    assert data["is_approved"] is True
