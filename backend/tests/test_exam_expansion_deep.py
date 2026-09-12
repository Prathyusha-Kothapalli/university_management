import pytest
import uuid
from fastapi.testclient import TestClient

from app.main import app
from app.models.user import User
from app.core.security import create_access_token
from app.database.session import SessionLocal


@pytest.fixture
def auth_headers():
    db = SessionLocal()
    try:
        user = db.query(User).first()
        if not user:
            user = User(
                id=uuid.uuid4(),
                email="test_exam_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="Exam Admin",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_question_bank_and_exam_paper_assembly(auth_headers: dict):
    client = TestClient(app)
    course_id = str(uuid.uuid4())
    offering_id = str(uuid.uuid4())

    # 1. Add Question
    q_resp = client.post(
        "/api/v1/exam-expansion/question-bank",
        headers=auth_headers,
        json={
            "course_id": course_id,
            "question_type": "MCQ",
            "difficulty_level": "HARD",
            "question_text": "What is the worst-case space complexity of MergeSort?",
            "options": {"A": "O(1)", "B": "O(N)", "C": "O(N^2)", "D": "O(log N)"},
            "correct_answer": "B",
            "points": 5.0,
        },
    )
    assert q_resp.status_code == 201
    q_id = q_resp.json()["id"]

    # 2. Assemble Exam Paper
    paper_resp = client.post(
        "/api/v1/exam-expansion/exam-papers",
        headers=auth_headers,
        json={
            "course_offering_id": offering_id,
            "title": "Algorithms Final Assessment",
            "total_marks": 100.0,
            "duration_minutes": 180,
            "question_ids": [q_id],
        },
    )
    assert paper_resp.status_code == 201
    assert paper_resp.json()["is_published"] is True


def test_proctoring_anomaly_logging(auth_headers: dict):
    client = TestClient(app)
    student_id = str(uuid.uuid4())
    exam_paper_id = str(uuid.uuid4())

    resp = client.post(
        "/api/v1/exam-expansion/proctor-telemetry",
        headers=auth_headers,
        json={
            "student_id": student_id,
            "exam_paper_id": exam_paper_id,
            "anomaly_type": "TAB_SWITCH",
            "confidence_score": 0.99,
            "snapshot_url": "https://s3.amazonaws.com/proctor-snaps/snap123.jpg",
        },
    )
    assert resp.status_code == 201
    assert resp.json()["anomaly_type"] == "TAB_SWITCH"
