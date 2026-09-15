import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_question_bank_management():
    q_payload = {
        "course_code": "AI401",
        "prompt": "Explain gradient descent convergence.",
        "bloom_level": "Understand",
        "difficulty": "Medium",
        "marks": 10,
        "topic": "Optimization"
    }

    response = client.post("/api/v1/exams/questions", json=q_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Question added to bank"
    assert data["question"]["course_code"] == "AI401"

    get_res = client.get("/api/v1/exams/questions?course_code=AI401")
    assert get_res.status_code == 200
    assert get_res.json()["total_questions"] >= 1


def test_generate_exam_paper():
    gen_payload = {
        "course_code": "AI401",
        "total_marks": 50
    }

    response = client.post("/api/v1/exams/generate-paper", json=gen_payload)
    assert response.status_code == 200
    data = response.json()
    assert "paper_id" in data
    assert len(data["questions"]) > 0


def test_proctor_telemetry_anomaly_logging():
    exam_id = str(uuid.uuid4())
    student_id = str(uuid.uuid4())

    telemetry_payload = {
        "student_id": student_id,
        "tab_switch_count": 5,
        "face_count_detected": 2,
        "mic_audio_db": 45.0,
        "browser_focus_lost_seconds": 22.5
    }

    response = client.post(f"/api/v1/exams/{exam_id}/proctor-log", json=telemetry_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Proctoring telemetry logged"
    assert data["log"]["integrity_threat_score"] > 50
    assert "MULTIPLE_FACES_DETECTED" in data["log"]["anomaly_flags"]
