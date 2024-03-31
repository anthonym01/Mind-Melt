# Yet another interprited language using ply
# flask --app yourkoza run --host=0.0.0.0 --debug --port=8080

port = 8080;

from html import escape
import json
from flask import Flask, render_template, request
import ply.yacc as yacc
import ply.lex as lex
from mainworker import Tokenize
from mainworker import parsex

from parsetab import *

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
    code_output.append(parsex(code_input))
    
    print("Input: ")
    print(code_input)
    print("Output: ")
    print(code_output)
    
    return code_output # An array of tokens
