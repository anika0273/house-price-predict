# FastAPI application for house price prediction
# This application uses a pre-trained model to predict house prices based on various features.
# The model is loaded at startup and predictions are made via a POST endpoint.
# file: app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model once on startup
model = joblib.load("models/house_price_model.joblib")

# Define input schema
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
    # Convert input to numpy array in correct order
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


# Run the application with:
# uvicorn api.app:app --reload
# This will start the FastAPI server and you can access the API at http://127.0.0.1:8000/docs
# CTRL+ C to stop the server.