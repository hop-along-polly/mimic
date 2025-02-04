import pytest
from fastapi.testclient import TestClient

from testerozza.app import app
from testerozza.controllers.injectors import inject_manifest_repo
from testerozza.models import TesterozzaRequest, TesterozzaResponse, ManifestEntry


@pytest.mark.asyncio
async def test_upload_full_manifest(mock_db, mock_manifest_repo):
    # arrange
    subject = TestClient(app)
    app.dependency_overrides[inject_manifest_repo] = mock_manifest_repo

    payload = [
        {
            "request": {"method": "GET", "url": "https://testerozza.com/health"},
            "responses": [{"status_code": 200, "body": {"status": "healthy"}}],
        }
    ]

    # act
    actual = subject.post("/v1/manifests", json=payload)
    record = await mock_db["always-on"]["manifests"].find_one({})

    # assert
    assert 201 == actual.status_code
    assert {} == actual.json()

    # TODO Might be better if I just have a method for reading these things in the repository
    actual = ManifestEntry.decode_and_create(record["request"], record["responses"])
    assert (
        TesterozzaRequest(method="GET", url="https://testerozza.com/health")
        == actual.request
    )
    assert [
        TesterozzaResponse(status_code=200, body={"status": "healthy"})
    ] == actual.responses
