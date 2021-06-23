from flask import Flask
app = Flask(__name__)

# third-party
from api.hahow import get_heros, get_hero_by_id

from flask_restful import Resource, Api
api = Api(app)

@app.route('/')
def test():
    return "Welcome to Flask!"

class HeroList(Resource):
    def get(self):
        return get_heros()

class Hero(Resource):
    def get(self, hero_id):
        return get_hero_by_id(hero_id)

api.add_resource(HeroList, '/heroes')
api.add_resource(Hero, '/heroes/<int:hero_id>')
