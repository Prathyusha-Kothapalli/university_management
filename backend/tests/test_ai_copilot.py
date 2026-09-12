import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_ai_copilot_query():
    user_id = str(uuid.uuid4())
    payload = {
        "user_id": user_id,
        "role": "student",
        "query": "What is the attendance policy for end-sem exams?"
    }

    response = client.post("/api/v1/ai-copilot/query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data or "agent_role" in data


def test_ai_copilot_generate_quiz():
    payload = {
        "subject": "Computer Science",
        "topic": "Neural Networks",
        "num_questions": 3
    }

    response = client.post("/api/v1/ai-copilot/generate-quiz", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0
