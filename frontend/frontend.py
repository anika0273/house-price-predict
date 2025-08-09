# keep the fastapi code running simultaneously with the streamlit frontend.
# You can run the FastAPI app in one terminal and the Streamlit app in another.
# Make sure to have both `uvicorn` and `streamlit` installed in your Python environment.

# file: frontend.py
import streamlit as st
import requests

# Set backend API URL to Docker Compose service name and port
import os

# Get backend API URL from environment variable, fallback to localhost
API_URL = os.getenv("API_URL", "http://localhost:8000")


# Streamlit app for house price prediction
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

    try:
        response = requests.post(f"{API_URL}/predict", json=data)
        response.raise_for_status()  # Raise error for bad HTTP status
        price = response.json().get("predicted_price")
        st.success(f"Predicted House Price (in 100k USD): {price}")
    except requests.exceptions.RequestException as e:
        st.error(f"Prediction failed: {e}")
