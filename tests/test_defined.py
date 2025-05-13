from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_defined_valid():
    response = client.post(
        "/defined/",
        json={
            "expression": "x**2",
            "variable": "x",
            "lower_limit": 0,
            "upper_limit": 2
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["input"]["expression"] == "x**2"
    assert "result" in data
    assert data["result"] in ["8/3", "2.66666666666667"]

def test_defined_invalid_expression():
    response = client.post(
        "/defined/",
        json={
            "expression": "invalid!!",
            "variable": "x",
            "lower_limit": 0,
            "upper_limit": 1
        }
    )
    assert response.status_code == 400
    assert "detail" in response.json()
