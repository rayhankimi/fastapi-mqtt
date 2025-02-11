from fastapi.testclient import TestClient
from pymongo import MongoClient
import mongomock

from ..main import app

mock_client = mongomock.MongoClient()
mock_db = mock_client["testdb"]


def override_get_db():
    return mock_db


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
