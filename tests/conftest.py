import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.db.store import catalog
@pytest.fixture
def client():
    catalog.cache_clear()
    with TestClient(app) as c:yield c
    catalog.cache_clear()
