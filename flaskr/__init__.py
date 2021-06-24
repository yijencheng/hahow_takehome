import json

from flask import Flask, Response, request
from flask_restful import Api, Resource

from thirdparty.hahow import auth, get_hero_by_id, get_heros, get_profile_by_id

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

        data = {"heroes": resp["data"]}
        name, password = request.headers.get("Name"), request.headers.get("Password")
        if not name or not password:
            return Response(
                response=json.dumps(data),
                status=200,
                mimetype="application/json",
            )

        if auth(name, password):
            for obj in data["heroes"]:
                obj["profile"] = get_profile_by_id(obj["id"])

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json",
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
