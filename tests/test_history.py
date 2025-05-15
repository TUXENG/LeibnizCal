from fastapi.testclient import TestClient
from src.main import app
from datetime import datetime, timezone

client = TestClient(app)

def test_history_lifecycle():
    # 1. Clear all to start fresh
    response = client.delete("/history/")
    assert response.status_code == 204

    # 2. Initially, history should be empty
    response = client.get("/history/")
    assert response.status_code == 200
    assert response.json() == []

    # 3. Add a defined integral entry via POST /history/
    new_entry_payload = {
        "id": 0,  # se ignora en el servicio
        "expression": "x**2",
        "result": "8/3",
        "type": "defined",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    response = client.post("/history/", json=new_entry_payload)
    assert response.status_code == 200
    added = response.json()
    assert added["id"] == 1
    assert added["expression"] == "x**2"
    assert added["result"] == "8/3"
    assert added["type"] == "defined"

    # 4. Get all should return one entry
    response = client.get("/history/")
    assert response.status_code == 200
    history_list = response.json()
    assert isinstance(history_list, list) and len(history_list) == 1

    # 5. Delete the entry by id
    response = client.delete("/history/1")
    assert response.status_code == 204

    # 6. After deletion, history should be empty again
    response = client.get("/history/")
    assert response.status_code == 200
    assert response.json() == []

    # 7. Add two entries and then clear all
    client.post("/history/", json={**new_entry_payload})
    client.post("/history/", json={**new_entry_payload})
    response = client.delete("/history/")
    assert response.status_code == 204
    response = client.get("/history/")
    assert response.json() == []