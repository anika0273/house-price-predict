# tests/conftest.py

# This ensures your tests won’t try to call Google Cloud Storage or require credentials during testing.

# It will replace your download_model_from_gcs() with a dummy one that returns a simple model object.

# It patches the actual model in your backend app to avoid triggering a real download at import time.

import pytest
from unittest.mock import patch

class DummyModel:
    def predict(self, x):
        return [123.45]

@pytest.fixture(autouse=True)
def patch_download_model():
    with patch("api.app.download_model_from_gcs", return_value=DummyModel()):
        import api.app as app_module
        app_module.model = DummyModel()  # override loaded model with dummy
        yield
