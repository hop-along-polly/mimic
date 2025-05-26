from mongomock_motor import AsyncMongoMockClient
import pytest

from mimic.db.manifest_repo import ManifestRepo


@pytest.fixture
def mock_db():
    return AsyncMongoMockClient()


@pytest.fixture
def mock_manifest_repo(mock_db):
    def create_mock():
        return ManifestRepo(mock_db)

    return create_mock
