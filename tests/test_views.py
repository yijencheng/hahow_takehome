import pytest
from flask import json

from flaskr import app


@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_data():
    return [
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


class TestHeroesList:
    def test_get_heros_success_without_auth(self, client, mocker, test_data):
        mocker.patch(
            "flaskr.get_heros",
            return_value={"status": "Success", "status_code": 200, "data": test_data},
        )

        response = client.get("/heroes")

        resp_json = json.loads(response.data)

        assert response.status_code == 200
        assert resp_json["heroes"] == test_data
        assert all("profile" not in x for x in resp_json["heroes"])

    def test_get_heros_success_with_auth(self, client, mocker, test_data):
        mocker.patch(
            "flaskr.get_heros",
            return_value={"status": "Success", "status_code": 200, "data": test_data},
        )
        mocker.patch(
            "flaskr.auth",
            return_value={"status": "Success", "status_code": 200, "data": {}},
        )
        mocker.patch(
            "flaskr.get_profile_by_id",
            return_value={
                "status": "Success",
                "status_code": 200,
                "data": {"key": "value"},
            },
        )

        response = client.get("/heroes", headers={"Name": "hahow", "Password": "rocks"})

        resp_json = json.loads(response.data)

        assert response.status_code == 200
        assert all("profile" in x for x in resp_json["heroes"])

    def test_get_heros_wrong_auth(self, client, mocker, test_data):
        mocker.patch(
            "flaskr.get_heros",
            return_value={"status": "Success", "status_code": 200, "data": test_data},
        )
        mocker.patch(
            "flaskr.auth",
            return_value={"status": "Fail", "status_code": 401, "data": {}},
        )
        mocker.patch(
            "flaskr.get_profile_by_id",
            return_value={
                "status": "Success",
                "status_code": 200,
                "data": {"key": "value"},
            },
        )

        response = client.get(
            "/heroes", headers={"Name": "hahow", "Password": "rockssss"}
        )

        assert response.status_code == 401



class TestHero:
    def test_get_hero_by_id_success_without_auth(self, client, mocker, test_data):
        mocker.patch(
            "flaskr.get_hero_by_id",
            return_value={"status": "Success", "data": test_data[0]},
        )

        response = client.get("/heroes/1")

        resp_json = json.loads(response.data)

        assert response.status_code == 200
        assert resp_json["id"] == "1"
        assert "profile" not in resp_json

    def test_get_hero_by_id_not_found(self, client, mocker):
        mocker.patch(
            "flaskr.get_hero_by_id", return_value={"status": "Fail", "error_code": 404}
        )

        response = client.get("/heroes/5")

        assert response.status_code == 404
        assert response.data == b"Not found"

    def test_get_hero_by_id_success_with_auth(self, client, mocker, test_data):
        mocker.patch(
            "flaskr.get_hero_by_id",
            return_value={"status": "Success", "data": test_data[0]},
        )
        mocker.patch("flaskr.auth", return_value=True)
        mocker.patch("flaskr.get_profile_by_id", return_value={"key": "value"})

        response = client.get(
            "/heroes/1", headers={"Name": "hahow", "Password": "rocks"}
        )

        resp_json = json.loads(response.data)

        assert response.status_code == 200
        assert "profile" in resp_json

    def test_get_hero_by_id_wrong_auth(self, client, mocker, test_data):
        mocker.patch(
            "flaskr.get_hero_by_id",
            return_value={"status": "Success", "data": test_data},
        )
        mocker.patch("flaskr.auth", return_value=False)
        mocker.patch("flaskr.get_profile_by_id", return_value={"key": "value"})

        response = client.get(
            "/heroes", headers={"Name": "hahow", "Password": "rockssss"}
        )

        resp_json = json.loads(response.data)

        assert response.status_code == 200
        assert "profile" not in resp_json
