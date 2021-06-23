from flask import Response
import requests
import json

def get_heros():
    endpoint = "https://hahow-recruit.herokuapp.com/heroes"
    resp = requests.get(endpoint)

    try:
        data = resp.json()
    except Exception:
        return Response(b"The Returned data is not json decodable", status=500)

    return Response(json.dumps(data), status=200, mimetype='application/json')

def get_hero_by_id(hero_id):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}"
    resp = requests.get(endpoint)

    try:
        data = resp.json()
    except Exception:
        return Response(b"The Returned data is not json decodable", status=500)

    return Response(json.dumps(data), status=200, mimetype='application/json')
