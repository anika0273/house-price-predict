import sys
from unittest.mock import MagicMock, patch

class DummyModel:
    def predict(self, x):
        return [123.45]

# Patch before importing api.app to avoid real GCS calls at import time
patcher = patch("api.app.download_model_from_gcs", return_value=DummyModel())
patcher.start()

import api.app as app_module

from fastapi.testclient import TestClient

client = TestClient(app_module.app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "House Price Prediction API"}

def test_predict_route():
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
    assert "predicted_price" in response.json()
    assert isinstance(response.json()["predicted_price"], float)

patcher.stop()
