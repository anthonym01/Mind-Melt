# Yet another interprited language using ply
# flask --app yourkoza run --host=0.0.0.0 --debug --port=8080

port = 8080;

from html import escape
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/code_string', methods=['GET', 'POST'])
def process_code():
    
    print(request.get_data())
    return ["Brackene","Morphine","folorine","adenazine","mathene"]

if __name__ == '__yourkoza__':
    app.run(debug=True, port=8080)