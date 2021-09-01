import pytest
from fastapi.testclient import TestClient
from {{cookiecutter.project_slug}}.api.check_author import app


@pytest.fixture
def test_client():
    return TestClient(app)


def test_bad_api_call(test_client):
    response = test_client.get("/undefined", headers={"X-Token": "invalid_token"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}



def test_bad_api_token(test_client):
    response = test_client.get("/", headers={"X-Token": "invalid_token"})
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}
