import pytest
from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_add_course_content():
    response = client.post("/courses/add", json={
        "course_id": "ML101",
        "title": "Introduction to Machine Learning",
        "content": "Machine learning is a branch of AI...",
        "prerequisites": ["Linear Algebra", "Statistics"],
        "learning_objectives": ["Understand ML concepts"],
        "tags": ["Machine Learning", "AI"]
    })
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_query_course():
    response = client.get("/courses/query?question=What are the prerequisites for machine learning?")
    assert response.status_code == 200
    # Add more assertions based on expected response
