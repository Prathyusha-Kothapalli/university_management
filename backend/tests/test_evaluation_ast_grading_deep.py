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
                email="test_ast_admin@university.edu",
                hashed_password="hashed_pass_xyz",
                full_name="AST Evaluator",
                is_active=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


def test_code_ast_and_plagiarism_workflow(auth_headers: dict):
    client = TestClient(app)
    sub_a = str(uuid.uuid4())
    sub_b = str(uuid.uuid4())

    # 1. Save AST
    ast_resp = client.post(
        "/api/v1/ast-grading/ast-analysis",
        headers=auth_headers,
        json={
            "submission_id": sub_a,
            "ast_json": {"type": "Module", "body": [{"type": "FunctionDef", "name": "sort"}]},
            "cyclomatic_complexity": 5,
            "linter_warnings": 1,
        },
    )
    assert ast_resp.status_code == 201
    assert ast_resp.json()["cyclomatic_complexity"] == 5

    # 2. Record Plagiarism Report
    plag_resp = client.post(
        "/api/v1/ast-grading/plagiarism-reports",
        headers=auth_headers,
        json={
            "submission_a_id": sub_a,
            "submission_b_id": sub_b,
            "similarity_score": 0.85,
            "matched_tokens": 142,
        },
    )
    assert plag_resp.status_code == 201
    assert plag_resp.json()["is_flagged"] is True
