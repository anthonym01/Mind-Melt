# Yet another interprited language using ply
# flask --app yourkoza run --host=0.0.0.0 --debug

port = 8080;

from html import escape
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
