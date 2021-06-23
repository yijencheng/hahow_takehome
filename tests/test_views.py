import pytest
from flask import json

from flaskr import app

from .utils import MockResponse


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


data = [
    {
        "id": "1",
        "name": "Daredevil",
        "image": "http://i.annihil.us/u/prod/marvel/i/mg/6/90/537ba6d49472b/standard_xlarge.jpg",
    },
    {
        "id": "2",
        "name": "Thor",
        "image": "http://x.annihil.us/u/prod/marvel/i/mg/5/a0/537bc7036ab02/standard_xlarge.jpg",
    },
    {
        "id": "3",
        "name": "Iron Man",
        "image": "http://i.annihil.us/u/prod/marvel/i/mg/6/a0/55b6a25e654e6/standard_xlarge.jpg",
    },
    {
        "id": "4",
        "name": "Hulk",
        "image": "http://i.annihil.us/u/prod/marvel/i/mg/5/a0/538615ca33ab0/standard_xlarge.jpg",
    },
]


def test_get_heros_success(client, mocker):
    mocker.patch(
        "api.hahow.requests.get", return_value=MockResponse(data=data, status_code=200)
    )

    response = client.get("/heroes")

    assert response.status_code == 200
    assert json.loads(response.data) == data


def test_get_hero_by_id(client, mocker):
    mocker.patch(
        "api.hahow.requests.get",
        return_value=MockResponse(status_code=200, data=data[0]),
    )

    response = client.get("/heroes/1")

    assert response.status_code == 200
    assert json.loads(response.data)["id"] == "1"


def test_get_hero_by_id_not_found(client, mocker):
    mocker.patch(
        "api.hahow.requests.get", return_value=MockResponse(status_code=404, data={})
    )

    response = client.get("/heroes/5")

    assert response.status_code == 404
    assert response.data == b"Not found"