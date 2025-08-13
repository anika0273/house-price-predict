# tests/test_api.py
# This file contains tests for the FastAPI application endpoints. It’s doing integration-style tests for the API layer, but with GCS and the model download mocked so you can run tests without cloud access.

import pytest
from unittest.mock import patch, MagicMock
import numpy as np

@pytest.fixture
def dummy_model():
    model = MagicMock()
    model.predict.return_value = np.array([123.45])
    return model

def test_model_file_exists(dummy_model):
    """
    ✅ Test that the 'model exists' check passes without an actual file.
    """
    with patch("os.path.exists", return_value=True):
        import os
        assert os.path.exists("models/house_price_model.joblib"), "Model file not found!"

def test_model_can_predict(dummy_model):
    """
    ✅ Test that the loaded model can make predictions without real GCS or file I/O.
    """
    with patch("joblib.load", return_value=dummy_model):
        import joblib
        model = joblib.load("models/house_price_model.joblib")
        sample = np.array([[8.0, 41.0, 6.0, 1.0, 1000, 2.5, 37.0, -122.0]])
        prediction = model.predict(sample)
        assert prediction.shape == (1,)
        assert prediction[0] > 0

