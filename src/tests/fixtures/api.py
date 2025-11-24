import pytest
from ninja.testing import TestClient

from core.urls import api


@pytest.fixture
def test_client():
    with TestClient(api) as client:
        yield client
