# keep the fastapi code running simultaneously with the streamlit frontend.
# You can run the FastAPI app in one terminal and the Streamlit app in another.
# Make sure to have both `uvicorn` and `streamlit` installed in your Python environment.

# file: frontend.py
import streamlit as st
import requests

# Set backend API URL to Docker Compose service name and port
import os

if os.getenv("DOCKER_ENV") == "true":
    API_URL = "http://backend:8000"
else:
    API_URL = "http://localhost:8000"


def get_data():
    response = requests.get(f"{API_URL}/predict")
    return response.json()

st.title("California House Price Prediction")

# Input fields
MedInc = st.number_input("Median Income", value=8.3252)
HouseAge = st.number_input("House Age", value=41)
AveRooms = st.number_input("Average Rooms", value=6.9841)
AveBedrms = st.number_input("Average Bedrooms", value=1.0238)
Population = st.number_input("Population", value=322)
AveOccup = st.number_input("Average Occupants", value=2.5556)
Latitude = st.number_input("Latitude", value=37.88)
Longitude = st.number_input("Longitude", value=-122.23)

if st.button("Predict Price"):
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    if response.status_code == 200:
        price = response.json()["predicted_price"]
        st.success(f"Predicted House Price (in 100k USD): {price}")
    else:
        st.error("Prediction failed!")
