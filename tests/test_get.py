from fastapi.testclient import TestClient
import pytest

from testerozza.app import app
from testerozza.controllers.injectors import inject_manifest_repo


@pytest.mark.asyncio
async def test_get_endpoint_single_call(mock_manifest_repo):
    # Arrange
    subject = TestClient(app)
    app.dependency_overrides[inject_manifest_repo] = mock_manifest_repo

    test_manifest = [
        {
            "request": {"method": "GET", "url": "https://testerozza.com/health"},
            "responses": [{"status_code": 200, "body": {"status": "healthy"}}],
        }
    ]

    # Act
    subject.post(
        "/v1/manifests", json=test_manifest
    )  # Upload a Manifest. This is likely how customers would be writing their tests
    actual = subject.get("https://testerozza.com/health")

    # Assert
    assert 200 == actual.status_code
    assert {"status": "healthy"} == actual.json()


@pytest.mark.asyncio
async def test_get_endpoint_called_multiple_times(mock_manifest_repo):
    # Arrange
    subject = TestClient(app)
    app.dependency_overrides[inject_manifest_repo] = mock_manifest_repo

    test_manifest = [
        {
            "request": {"method": "GET", "url": "https://testerozza.com/health"},
            "responses": [
                {"status_code": 500, "body": {"status": "unhealthy"}},
                {"status_code": 200, "body": {"status": "healthy "}},
            ],
        }
    ]
    expected = test_manifest[0]

    # Act
    subject.post("/v1/manifests", json=test_manifest)

    # Assert
    num_responses = len(expected["responses"])
    # Ensure we make a call to the Echo endpoint to get each of the configured responses.
    for i in range(num_responses):
        actual = subject.get("https://testerozza.com/health")

        assert expected["responses"][i]["status_code"] == actual.status_code
        assert expected["responses"][i]["body"] == actual.json()


@pytest.mark.asyncio
async def test_get_endpoint_not_configured(mock_manifest_repo):
    # Arrange
    subject = TestClient(app)
    app.dependency_overrides[inject_manifest_repo] = mock_manifest_repo

    # Act
    actual = subject.get("https://testerozza.com/health")

    # Assert
    assert 400 == actual.status_code
    assert {
        "message": "/health has not been configured with a response"
    } == actual.json()


@pytest.mark.asyncio
async def test_get_endpoint_too_many_calls(mock_manifest_repo):
    # Arrange
    subject = TestClient(app)
    app.dependency_overrides[inject_manifest_repo] = mock_manifest_repo

    test_manifest = [
        {
            "request": {"method": "GET", "url": "https://testerozza.com/health"},
            "responses": [
                {"status_code": 500, "body": {"status": "unhealthy"}},
                {"status_code": 200, "body": {"status": "healthy "}},
            ],
        }
    ]
    expected = test_manifest[0]

    # Act
    subject.post("/v1/manifests", json=test_manifest)

    # Assert
    num_responses = len(expected["responses"])
    # Ensure we make a call to the Echo endpoint to get each of the configured responses.
    for i in range(num_responses):
        actual = subject.get("https://testerozza.com/health")

        assert expected["responses"][i]["status_code"] == actual.status_code
        assert expected["responses"][i]["body"] == actual.json()

    # Now call the endpoint 1 more time to ensure the standard 400 message is returned.
    actual = subject.get("https://testerozza.com/health")

    # TODO finish debugging
    assert 400 == actual.status_code
    assert {
        "message": "/health has not been configured with a response"
    } == actual.json()
