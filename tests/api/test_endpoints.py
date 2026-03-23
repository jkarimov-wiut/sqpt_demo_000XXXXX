from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_add_endpoint():
    r = client.get("/calc/add?a=2&b=3")
    assert r.json()["result"] == 5
