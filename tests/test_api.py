# 📁 tests/test_api.py
from unittest.mock import patch

class DummyModel:
    def predict(self, x):
        return [123.45]

with patch("api.app.download_model_from_gcs", return_value=DummyModel()):
    from api.app import app

from fastapi.testclient import TestClient
#from api.app import app

client = TestClient(app)

def test_home_route():
    """
    ✅ Test that the root (/) endpoint returns 200 OK.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "House Price Prediction API"}

def test_predict_route():
    """
    ✅ Test that /predict returns a valid prediction.
    """
    payload = {
        "MedInc": 8.0,
        "HouseAge": 41.0,
        "AveRooms": 6.0,
        "AveBedrms": 1.0,
        "Population": 1000,
        "AveOccup": 2.5,
        "Latitude": 37.0,
        "Longitude": -122.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json(), "Response must contain predicted_price"
    assert isinstance(response.json()["predicted_price"], float)
