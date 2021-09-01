import pytest
from fastapi.testclient import TestClient
from {{cookiecutter.project_slug}}.api.check_author import app


@pytest.fixture
def test_client():
    return TestClient(app)


def test_predict_csv(test_client):
    # make prediction with API
    r = test_client.post("/predict/file?sep=%2C",
                         files={"file": (
                             "hyperparameter.csv", open("test/test_files/hyperparameter.csv", "rb"), "text/csv")},
                         headers={"X-Token": "default_token"})
    assert r.status_code == 200
    result = r.json()

    # TODO switch to your usecase when your model is switched
    assert len(result.keys()) == 3
    assert len(result["Trial"].keys()) == 20


def test_predict_non_csv(test_client):
    r = test_client.post("/predict/file?sep=%2C",
                         files={"file": (
                             "test.tf", open("test/test_files/test.tf", "rb"), "text/plain")},
                         headers={"X-Token": "default_token"})
    assert r.status_code == 400
    assert r.json() == {"detail": "Invalid content type"}


def test_predict_json(test_client):
    # TODO change this to your usecase
    r = test_client.post("/predict/data",
                         headers={"X-Token": "default_token"},
                         json={
                             "name": "test",
                             "description": "test",
                             "data": {
                                 "index": [
                                     "10", "11", "12"
                                 ],
                                 "Antigen": [
                                     "A", "B", "C"
                                 ],
                                 "ProductName": [
                                     "Fancy1", "Common2", "Pro42"
                                 ]
                             }
                         })

    assert r.status_code == 200
    result = r.json()

    # TODO switch to your usecase when your model is switched
    assert len(result["index"].keys()) == 3
    assert result["index"]["0"] == "10"


def test_predict_json_wrong_data_semantic(test_client):
    # TODO change this to your usecase
    r = test_client.post("/predict/data",
                         headers={"X-Token": "default_token"},
                         json={
                             "name": "test",
                             "description": "test",
                             "data": {
                                 "index": [
                                     "10", "11", "12"
                                 ],
                                 "Antigen": [
                                     {
                                         "Error": "Here"
                                     }
                                 ],
                                 "ProductName": [
                                     "Fancy1", "Common2", "Pro42"
                                 ]
                             }
                         })
    assert r.status_code == 422


def test_predict_json_columns_different_length(test_client):
    # TODO change this to your usecase
    r = test_client.post("/predict/data",
                         headers={"X-Token": "default_token"},
                         json={
                             "name": "test",
                             "description": "test",
                             "data": {
                                 "index": [
                                     "10", "11", "12"
                                 ],
                                 "Antigen": [
                                     "A", "B"
                                 ],
                                 "ProductName": [
                                     "Fancy1", "Common2", "Pro42", "Infinity"
                                 ]
                             }
                         })
    assert r.status_code == 422
    assert r.json() == {"description": "arrays must all be same length"}
