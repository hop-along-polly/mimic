from mongomock_motor import AsyncMongoMockClient
import pytest


@pytest.fixture
def mock_db():
  return AsyncMongoMockClient()
