# 📁 tests/test_model.py
import os
import joblib
import numpy as np

def test_model_file_exists():
    """
    ✅ Test that the saved model file exists in the expected path.
    """
    assert os.path.exists("models/house_price_model.joblib"), "Model file not found!"

def test_model_can_predict():
    """
    ✅ Test that the loaded model can make predictions on dummy input.
    """
    model = joblib.load("models/house_price_model.joblib")
    sample = np.array([[8.0, 41.0, 6.0, 1.0, 1000, 2.5, 37.0, -122.0]])
    prediction = model.predict(sample)
    assert prediction.shape == (1,), "Prediction output should be a single value"
    assert prediction[0] > 0, "Prediction should be a positive number"
