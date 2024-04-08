# Yet another interprited language using ply
# flask --app yourkoza run --host=0.0.0.0 --debug --port=8080

port = 8080;

# from html import escape
import json
from flask import Flask, render_template, request

from semantics import parsex
from api import api


app = Flask(__name__)

code_output = ["test"]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/code_string', methods=['GET', 'POST'])
def process_code():

    code_input = json.loads(request.get_data())["code_string"]

    code_output = []
    #code_output = Tokenize(code_input)
    code_output = parsex(code_input)
    
    print("Input: ")
    print(code_input)
    print("Output: ")
    print(code_output)
    
    return code_output # An array of tokens


@app.route('/post/geminaize', methods=['GET', 'POST'])
def gemini_interface():
    code_input = json.loads(request.get_data())["code_query"]
    api_output = api(code_input)
    print("API Output: ")
    print(api_output[11:-3])
    return [api_output[11:-3]]

#```yourkoza
#let sum = 10 + 20
#show "The sum of 10 and 20 is " + sum
#```