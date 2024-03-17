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
    lexer = lex.lex()
    
    code_lines = ["test"]
    
    # Give the lexer some input
    lexer.input("pain pain pain pain")
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break     # No more input
        #print(tok)
        
    print(request.get_data())
    print(request.get_data())
    
    return code_lines


# PLY lexer

import ply.lex as lex

# List of token names. This is always required
tokens = (
    'INTEGER',
    'IDENTIFIER',
    'REAL',
    'NUMBER',
    'CHARACTER',
    'LETTER',
    'STRING_LITERAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'LPAREN',
    'DIVIDE',
    'RPAREN',
    'POWER',
    'AND',
    'OR',
    'NOT',
    'IS_EQUAL_TO',
    'IS_NOT_EQUAL_TO',
    'IS_GREATER_THAN',
    'IS_LESS_THAN',
    'INCREASE',
    'DECREASE',
    'JOIN',
    'IN',
    'DO',
    'LET',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'FUNCTION',
    'RETURN',
    'SHOW',
    'RISK',
    'SAVE',
    'COMMENT',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_DIVIDE  = r'/'
t_RPAREN  = r'\)'
t_POWER = r'\^'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
