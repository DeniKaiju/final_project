from fastapi import status


import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    yield TestClient(app)


def test_root_status_code(client):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK


def test_root_content(client):
    response = client.get('/')
    assert response.json() == {'try': 'OK', 'count': 10}
