import requests
from retrying import retry

from .helper import retry_if_resp_502


def get_heros(timeout=3):
    endpoint = "https://hahow-recruit.herokuapp.com/heroes"
    resp = requests.get(endpoint, timeout=timeout)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}

    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


@retry(stop_max_attempt_number=2, retry_on_result=retry_if_resp_502, wait_fixed=500)
def get_hero_by_id(hero_id, timeout=3):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}"
    resp = requests.get(endpoint, timeout=timeout)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}

    resp_json = resp.json()
    if (
        "id" not in resp_json
    ):  # to handle Response 200 OK  {"code":1000,"message":"Backend error"}
        return {"status": "Fail", "status_code": 502}

    return {"status": "Success", "status_code": resp.status_code, "data": resp_json}


def get_profile_by_id(hero_id, timeout=3):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}/profile"
    resp = requests.get(endpoint, timeout=timeout)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}
    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


def auth(name, password, timeout=2):
    endpoint = "https://hahow-recruit.herokuapp.com/auth"
    resp = requests.post(
        endpoint, json={"name": name, "password": password}, timeout=timeout
    )

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}
    return {"status": "Success", "status_code": resp.status_code, "data": {}}
