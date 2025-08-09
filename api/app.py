# FastAPI application for house price prediction
# This application uses a pre-trained model to predict house prices based on various features.
# The model is loaded at startup and predictions are made via a POST endpoint.
# file: app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import uvicorn

app = FastAPI()


if os.path.exists("/app/models/house_price_model.joblib"):
    model_path = "/app/models/house_price_model.joblib" # Cloud Run/Docker path


else:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.abspath(os.path.join(root_dir, "..", "models"))
    model_path = os.path.join(models_dir, "house_price_model.joblib")

print(f"Loading model from: {model_path}")
model = joblib.load(model_path)


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


# To run this application, ensure you have FastAPI and Uvicorn installed.
# You can install them using pip:
# pip install fastapi uvicorn
# After that, you can run the application using Uvicorn:
# uvicorn app:app --reload
# This will start the FastAPI server and you can access the API at http://127.0.0.1:8000/docs
# CTRL+ C to stop the server.

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
