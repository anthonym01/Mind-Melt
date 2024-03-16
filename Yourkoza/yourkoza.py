# Yet another interprited language using ply
# flask --app yourkoza run --host=0.0.0.0 --debug

port = 8080;

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"