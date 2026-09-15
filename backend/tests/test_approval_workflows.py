"""
UniSphere AI — Approval Workflow Engine Test Suite
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_approval_chain():
    payload = {
        "name": "Procurement Purchase Order Chain",
        "module_name": "PROCUREMENT",
        "description": "Multi-stage PO approval for hardware > $10,000",
        "total_steps": 3
    }
    response = client.post("/api/v1/approval-workflows/chains", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Procurement Purchase Order Chain"
    assert data["total_steps"] == 3
