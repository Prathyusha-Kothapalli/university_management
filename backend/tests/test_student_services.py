import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)



def test_bulk_student_csv_import():
    prefix = uuid.uuid4().hex[:6].upper()

    csv_data = (
        "roll_number,gpa,semester,academic_standing\n"
        f"STU_{prefix}_001,3.8,4,GOOD\n"
        f"STU_{prefix}_002,3.9,6,DEANS_LIST\n"
        f"STU_{prefix}_003,3.4,2,GOOD\n"
    )


    files = {
        "file": ("students.csv", csv_data.encode("utf-8"), "text/csv")
    }

    response = client.post("/api/v1/students/bulk-import", files=files)
    assert response.status_code == 200
    data = response.json()
    assert data["total_processed"] == 3
    assert data["imported_count"] == 3
    assert data["failed_count"] == 0


def test_generate_student_transcript():
    student_id = str(uuid.uuid4())
    response = client.get(f"/api/v1/students/{student_id}/transcript")
    assert response.status_code == 200
    data = response.json()
    assert data["institution"] == "UniSphere Global University"
    assert data["student_id"] == student_id
    assert "cumulative_gpa" in data
    assert "academic_standing" in data
    assert len(data["course_history"]) > 0
    assert "verification_hash" in data
    assert data["is_official"] is True
