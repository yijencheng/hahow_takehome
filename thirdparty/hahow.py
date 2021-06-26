import requests


def get_heros(timeout=0.1):
    endpoint = "https://hahow-recruit.herokuapp.com/heroes"
    resp = requests.get(endpoint, timeout=timeout)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}

    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


def get_hero_by_id(hero_id, timeout=5):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}"
    resp = requests.get(endpoint, timeout=timeout)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}

    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


def get_profile_by_id(hero_id, timeout=5):
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
