from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import uvicorn

app = FastAPI()

if os.path.exists("/app/models/house_price_model.joblib"):
    model_path = "/app/models/house_price_model.joblib"  # Cloud Run/Docker path
else:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.abspath(os.path.join(root_dir, "..", "models"))
    model_path = os.path.join(models_dir, "house_price_model.joblib")

try:
    print(f"Loading model from: {model_path}")
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    raise

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"message": "House Price Prediction API"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]])
    prediction = model.predict(input_data)
    return {"predicted_price": round(float(prediction[0]), 3)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting API server on host 0.0.0.0, port {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port)
# To run the FastAPI app, use the command:
# uvicorn app:app --host