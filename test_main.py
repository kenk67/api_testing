from fastapi.testclient import TestClient
from main import app  # Replace 'main' with your FastAPI app file name if different

client = TestClient(app)

def test_get_fruit_description_apple():
    response = client.get("/fruits?fruit=watermelon")
    assert response.status_code == 200
    assert response.json() == {
        "name": "watermelon",
        "description": "Its freaking good"
    }

def test_get_fruit_description_not_found():
    response = client.get("/fruits?fruit=strawberry")
    assert response.status_code == 404
    assert response.json() == {"detail": "Fruit not found"}

def test_get_vehicle_description_car():
    response = client.get("/vehicles?vehicle=car")
    assert response.status_code == 200
    assert response.json() == {
        "name": "car",
        "description": "A car is a road vehicle with four wheels, typically powered by an internal combustion engine or an electric motor."
    }

def test_get_vehicle_description_not_found():
    response = client.get("/vehicles?vehicle=plane")
    assert response.status_code == 404
    assert response.json() == {"detail": "Vehicle not found"}

# New test to verify the /config endpoint
def test_get_config():
    response = client.get("/config")
    assert response.status_code == 200
    # These values should match the secrets set in the GitHub Actions or local .env file
    assert response.json() == {
        "api_version": "1.0",
        "fruit_limit": 6,
        "vehicle_limit": 5
    }
