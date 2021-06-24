import pytest
from flask import json
from flaskr import app


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


def test_get_heros_success_without_auth(client, mocker):
    mocker.patch("flaskr.get_heros", return_value={"status": "Success", "data": data})

    response = client.get("/heroes")

    resp_json_list = json.loads(response.data)

    assert response.status_code == 200
    assert json.loads(response.data)["heroes"] == data
    assert all("profile" not in x for x in resp_json_list["heroes"])


def test_get_heros_success_with_auth(client, mocker):
    mocker.patch("flaskr.get_heros", return_value={"status": "Success", "data": data})
    mocker.patch("flaskr.auth", return_value=True)
    mocker.patch("flaskr.get_profile_by_id", return_value={"key": "value"})

    response = client.get("/heroes", headers={"Name": "hahow", "Password": "rocks"})

    resp_json_list = json.loads(response.data)

    assert response.status_code == 200
    assert json.loads(response.data)["heroes"] == data
    assert all("profile" in x for x in resp_json_list["heroes"])


def test_get_heros_auth_fail(client, mocker):
    mocker.patch("flaskr.get_heros", return_value={"status": "Success", "data": data})
    mocker.patch("flaskr.auth", return_value=False)
    mocker.patch("flaskr.get_profile_by_id", return_value={"key": "value"})

    response = client.get("/heroes", headers={"Name": "hahow", "Password": "rockssss"})

    resp_json_list = json.loads(response.data)

    assert response.status_code == 200
    assert all("profile" not in x for x in resp_json_list)
    assert json.loads(response.data)["heroes"] == data


def test_get_hero_by_id_404(client, mocker):
    mocker.patch("flaskr.get_hero_by_id", return_value={"status": "Fail", "error_code": 404})

    response = client.get("/heroes/5")

    assert response.status_code == 404
    assert response.data == b"Not found"
