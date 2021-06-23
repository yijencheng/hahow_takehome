from json.decoder import JSONDecodeError
from flask import Response
import requests
import json
from .error_handler import err_response

def get_heros():
    endpoint = "https://hahow-recruit.herokuapp.com/heroes"
    resp = requests.get(endpoint)

    if resp.status_code != 200:
        return err_response(resp.status_code)
    
    try:
        data = resp.json()
    except JSONDecodeError:
        return Response("The Returned data is not json decodable", status=500)

    return Response(json.dumps(data), status=200, mimetype='application/json')

def get_hero_by_id(hero_id):
    endpoint = f"https://hahow-recruit.herokuapp.com/heroes/{hero_id}"
    resp = requests.get(endpoint)
    
    if resp.status_code != 200:
        return err_response(resp.status_code)

    try:
        data = resp.json()
    except JSONDecodeError:
        return Response("The Returned data is not json decodable", status=500)

    return Response(json.dumps(data), status=200, mimetype='application/json')
