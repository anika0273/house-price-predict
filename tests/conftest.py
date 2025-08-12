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
def mock_gcs(monkeypatch):
    def dummy_download_model_from_gcs():
        return DummyModel()

    # Patch the function in your app module that downloads the model
    monkeypatch.setattr("api.app.download_model_from_gcs", dummy_download_model_from_gcs)

    # Also patch the model instance used in the app
    import api.app as app_module
    app_module.model = dummy_download_model_from_gcs()
