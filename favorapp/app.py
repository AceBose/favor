from flask import Flask
from favorapp.views.index import bp as index_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
# return ("Welcome to Favor.app")
