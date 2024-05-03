from fastapi.testclient import TestClient
import pytest

from alwayson.app import app
from alwayson.controllers.status import get_db_client


class MockDbClient:
  def __init__(self, health_result):
    self._result = health_result

  async def health(self):
    return self._result


@pytest.fixture
def online_db():
  def create_mock():
    return MockDbClient('online')
  return create_mock


@pytest.fixture
def offline_db():
  def create_mock():
    return MockDbClient('offline')
  return create_mock


def test_status_healthy_db(online_db):
  # arrange
  subject = TestClient(app)
  app.dependency_overrides[get_db_client] = online_db

  # act
  actual = subject.get('/v1/status')

  # assert
  assert 200 == actual.status_code
  assert { 'api': 'online', 'db': 'online' }


def test_status_unhealthy_db(offline_db):
  # arrange
  subject = TestClient(app)
  app.dependency_overrides[get_db_client] = offline_db

  # act
  actual = subject.get('/v1/status')

  # assert
  assert 200 == actual.status_code
  assert { 'api': 'online', 'db': 'offline' }
