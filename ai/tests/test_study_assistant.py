from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_and_root():
    res = client.get("/")
    assert res.status_code == 200
    res_health = client.get("/health")
    assert res_health.status_code == 200
    assert "study_assistant" in res_health.json()["features"]

def test_get_courses():
    res = client.get("/ai/courses")
    assert res.status_code == 200
    courses = res.json()
    assert len(courses) >= 4
    course_ids = [c["id"] for c in courses]
    assert "CS101" in course_ids
    assert "CS202" in course_ids

def test_study_assistant_avl_trees():
    payload = {
        "question": "What is an AVL Tree and how do rotations work?",
        "course_id": "CS101",
        "mode": "detailed"
    }
    res = client.post("/ai/study-assistant", json=payload)
    assert res.status_code == 200, res.text
    data = res.json()
    assert "answer" in data
    assert "Balance Factor" in data["answer"]
    assert "sources" in data
    assert len(data["sources"]) > 0
    assert "confidence" in data
    assert data["confidence"] > 0.7
    assert "conversation_id" in data
    assert len(data["follow_up_questions"]) > 0

def test_study_assistant_explanation_modes():
    modes = ["beginner", "code", "exam_summary", "detailed"]
    for mode in modes:
        payload = {
            "question": "Explain AVL tree balancing",
            "course_id": "CS101",
            "mode": mode
        }
        res = client.post("/ai/study-assistant", json=payload)
        assert res.status_code == 200
        data = res.json()
        assert data["mode"] == mode
        assert len(data["answer"]) > 50

def test_study_assistant_feedback():
    payload = {
        "conversation_id": "conv_test123",
        "is_helpful": True,
        "comment": "Very clear explanation of rotations!"
    }
    res = client.post("/ai/feedback", json=payload)
    assert res.status_code == 200
    assert res.json()["status"] == "success"

