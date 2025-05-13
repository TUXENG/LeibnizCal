from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_undefined_valid():
    response = client.post(
        "/undefined/",
        json={
            "expression": "x**2",
            "variable": "x"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["input"]["expression"] == "x**2"
    assert data["result"].endswith("+ C")

def test_undefined_invalid_expression():
    response = client.post(
        "/undefined/",
        json={
            "expression": "123***",
            "variable": "x"
        }
    )
    assert response.status_code == 400
    assert "detail" in response.json()
