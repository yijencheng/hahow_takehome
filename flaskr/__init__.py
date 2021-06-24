import json

from flask import Flask, Response
from flask_restful import Api, Resource

from thirdparty.hahow import get_hero_by_id, get_heros

from .error_handler import err_response

app = Flask(__name__)
api = Api(app)


@app.route("/")
def test():
    return "Welcome to Flask!"


class HeroList(Resource):
    def get(self):
        resp = get_heros()
        if resp["status"] != "Success":
            return err_response(resp["error_code"])

        return Response(
            json.dumps(resp["data"]), status=200, mimetype="application/json"
        )


class Hero(Resource):
    def get(self, hero_id):
        resp = get_hero_by_id(hero_id)
        if resp["status"] != "Success":
            return err_response(resp["error_code"])

        return Response(
            json.dumps(resp["data"]), status=200, mimetype="application/json"
        )


api.add_resource(HeroList, "/heroes")
api.add_resource(Hero, "/heroes/<int:hero_id>")
