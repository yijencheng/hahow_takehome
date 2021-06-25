import requests


def get_heros():
    endpoint = "https://hahow-recruit.herokuapp.com/heroes"
    resp = requests.get(endpoint)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}

    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


def get_hero_by_id(hero_id):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}"
    resp = requests.get(endpoint)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}

    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


def get_profile_by_id(hero_id):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}/profile"
    resp = requests.get(endpoint)

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}
    return {"status": "Success", "status_code": resp.status_code, "data": resp.json()}


def auth(name, password):
    endpoint = "https://hahow-recruit.herokuapp.com/auth"
    resp = requests.post(endpoint, json={"name": name, "password": password})

    if resp.status_code != 200:
        return {"status": "Fail", "status_code": resp.status_code}
    return {"status": "Success", "status_code": resp.status_code, "data": {}}
