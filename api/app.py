from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import tempfile
from google.cloud import storage


app = FastAPI()


# GCS bucket and file
GCS_BUCKET = "house-price-models-468401"
GCS_FILE_NAME = "house_price_model.joblib"


def download_model_from_gcs():
    """Download model from GCS to a temporary location and load it."""
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(GCS_FILE_NAME)

    temp_path = os.path.join(tempfile.gettempdir(), GCS_FILE_NAME)
    blob.download_to_filename(temp_path)

    return joblib.load(temp_path)


# Load the model at startup
model = download_model_from_gcs()


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
    input_data = np.array([
        [
            features.MedInc,
            features.HouseAge,
            features.AveRooms,
            features.AveBedrms,
            features.Population,
            features.AveOccup,
            features.Latitude,
            features.Longitude
        ]
    ])
    prediction = model.predict(input_data)
    return {"predicted_price": round(float(prediction[0]), 3)}


"""
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
    input_data = np.array([
        [
            features.MedInc,
            features.HouseAge,
            features.AveRooms,
            features.AveBedrms,
            features.Population,
            features.AveOccup,
            features.Latitude,
            features.Longitude
        ]
    ])
    prediction = model.predict(input_data)
    return {"predicted_price": round(float(prediction[0]), 3)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting API server on host 0.0.0.0, port {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port)
# To run the FastAPI app, use the command:
# uvicorn app:app --host
"""