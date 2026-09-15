import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_online_exam_attempt_lifecycle():
    student_id = str(uuid.uuid4())
    exam_id = str(uuid.uuid4())

    # 1. Start attempt
    start_res = client.post("/api/v1/exam-attempts/start", json={"student_id": student_id, "exam_id": exam_id})
    assert start_res.status_code == 200
    attempt_id = start_res.json()["attempt"]["attempt_id"]

    # 2. Save answer
    ans_res = client.post("/api/v1/exam-attempts/save-answer", json={
        "attempt_id": attempt_id,
        "question_id": "q-101",
        "answer_text": "Option C: O(N log N)",
        "time_spent_seconds": 30.0
    })
    assert ans_res.status_code == 200
    assert ans_res.json()["total_answers_saved"] >= 1

    # 3. Finalize attempt
    fin_res = client.post("/api/v1/exam-attempts/finalize", json={
        "attempt_id": attempt_id,
        "proctoring_anomalies_count": 0
    })
    assert fin_res.status_code == 200
    assert fin_res.json()["attempt_summary"]["status"] == "SUBMITTED"
    assert fin_res.json()["attempt_summary"]["integrity_flag"] == "CLEAN"
