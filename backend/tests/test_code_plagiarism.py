import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_compare_code_ast_plagiarism_flagged():
    code_a = "def calculate_gpa(scores):\n    return sum(scores) / len(scores)"
    code_b = "def calculate_gpa(scores):\n    return sum(scores) / len(scores)"

    payload = {
        "source_code_a": code_a,
        "source_code_b": code_b,
        "language": "python"
    }

    response = client.post("/api/v1/assignments/compare-code", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["similarity_percentage"] == 100.0
    assert data["flagged_plagiarism"] is True
    assert data["verdict"] == "PLAGIARISM_FLAGGED"


def test_compare_code_ast_plagiarism_clean():
    code_a = "def calculate_gpa(scores):\n    return sum(scores) / len(scores)"
    code_b = "class StudentRoster:\n    def __init__(self, name):\n        self.name = name"

    payload = {
        "source_code_a": code_a,
        "source_code_b": code_b,
        "language": "python"
    }

    response = client.post("/api/v1/assignments/compare-code", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["flagged_plagiarism"] is False
    assert data["verdict"] == "PASS_CLEAN"


def test_evaluate_auto_rubric():
    sub_id = str(uuid.uuid4())
    payload = {
        "submission_id": sub_id,
        "test_cases_passed": 9,
        "total_test_cases": 10,
        "code_style_score": 9.5,
        "time_complexity_rating": "O(N)"
    }

    response = client.post("/api/v1/assignments/evaluate-rubric", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["submission_id"] == sub_id
    assert data["total_grade_percentage"] >= 90.0
    assert data["letter_grade"] == "A"
