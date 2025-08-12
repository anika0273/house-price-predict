from fastapi.testclient import TestClient

def test_home_route():
    import api.app  # import after patch active
    client = TestClient(api.app.app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "House Price Prediction API"}

def test_predict_route():
    import api.app
    client = TestClient(api.app.app)

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
