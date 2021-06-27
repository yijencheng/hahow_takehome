from flask import Flask

from flaskr.views.hero_views import hero_app

app = Flask(__name__)
app.register_blueprint(hero_app)
