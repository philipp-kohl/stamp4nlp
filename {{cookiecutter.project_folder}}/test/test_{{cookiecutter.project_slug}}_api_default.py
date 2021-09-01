import pytest
from fastapi.testclient import TestClient
from {{cookiecutter.project_slug}}.api.check_author import app


@pytest.fixture
def test_client():
    return TestClient(app)


def test_get_root(test_client):
    response = test_client.get("/", headers={"X-Token": "default_token"})
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.parametrize("api_key", ["description", "info"])
def test_get_description(test_client, api_key):
    response = test_client.get("/"+api_key, headers={"X-Token": "default_token"})
    assert response.status_code == 200
    assert response.json()["project_slug"] == "{{cookiecutter.project_slug}}"
