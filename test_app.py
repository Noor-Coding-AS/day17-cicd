from fastapi.testclient import TestClient
from app import app, add_numbers, multiply_numbers

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["built_by"] == "Asfer Saeed"
    assert data["day"] == "17 of 90"
    print("✅ Root endpoint test passed")

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✅ Health endpoint test passed")

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    print("✅ Add numbers test passed")

def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-2, 3) == -6
    print("✅ Multiply numbers test passed")