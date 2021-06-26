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
        authorized = False
        name, password = request.headers.get("Name"), request.headers.get("Password")
        try:
            if name and password:
                auth_resp = auth(name, password)
                if auth_resp["status"] != "Success":
                    return err_response(auth_resp["status_code"])
                authorized = True

            resp = get_heros()
            if resp["status"] != "Success":
                return err_response(resp["status_code"])

            data = {"heroes": resp["data"]}

            # Get extra hero's profile if authorized
            if authorized:
                for obj in data["heroes"]:
                    resp = get_profile_by_id(obj["id"])

                    if resp["status"] != "Success":
                        return err_response(resp["status_code"])

                    obj["profile"] = resp["data"]

            return Response(
                response=json.dumps(data),
                status=200,
                mimetype="application/json",
            )
        except TimeoutError:
            return err_response(504)
        except Exception:
            return err_response(500)


class Hero(Resource):
    def get(self, hero_id):
        authorized = False
        name, password = request.headers.get("Name"), request.headers.get("Password")
        try:
            if name and password:
                auth_resp = auth(name, password)
                if auth_resp["status"] != "Success":
                    return err_response(auth_resp["status_code"])
                authorized = True

            resp = get_hero_by_id(hero_id)
            if resp["status"] != "Success":
                return err_response(resp["status_code"])

            data = resp["data"]

            # Get extra hero's profile if authorized
            if authorized:
                resp = get_profile_by_id(hero_id)
                if resp["status"] != "Success":
                    return err_response(resp["status_code"])

                data["profile"] = resp["data"]

            return Response(json.dumps(data), status=200, mimetype="application/json")
        except TimeoutError:
            return err_response(504)
        except Exception:
            return err_response(500)


api.add_resource(HeroList, "/heroes")
api.add_resource(Hero, "/heroes/<int:hero_id>")
