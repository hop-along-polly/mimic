from fastapi.testclient import TestClient
import pytest

from mimic.app import app
from mimic.controllers.status import get_db_client


class MockDbClient:
    def __init__(self, health_result):
        self._result = health_result

    async def health(self):
        return self._result


@pytest.fixture
def online_db():
    def create_mock():
        return MockDbClient("online")

    return create_mock


@pytest.fixture
def offline_db():
    def create_mock():
        return MockDbClient("offline")

    return create_mock


def test_liveness_probe():
  # arrange
  subject = TestClient(app) 

  # act
  actual = subject.get('/v1/liveness')

  # assert
  assert 200 == actual.status_code
  assert { 'api': 'online' } == actual.json()


def test_readiness_healthy_db(online_db):
    # arrange
    subject = TestClient(app)
    app.dependency_overrides[get_db_client] = online_db

    # act
    actual = subject.get("/v1/readiness")

    # assert
    assert 200 == actual.status_code
    assert {"api": "online", "db": "online"} == actual.json()


def test_readiness_unhealthy_db(offline_db):
    # arrange
    subject = TestClient(app)
    app.dependency_overrides[get_db_client] = offline_db

    # act
    actual = subject.get("/v1/readiness")

    # assert
    assert 200 == actual.status_code
    assert {"api": "online", "db": "offline"} == actual.json()
