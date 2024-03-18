# Yet another interprited language using ply
# flask --app yourkoza run --host=0.0.0.0 --debug --port=8080

port = 8080;

from html import escape
import json
from flask import Flask, render_template, request

app = Flask(__name__)
code_output = ["test"]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/code_string', methods=['GET', 'POST'])
def process_code():
    lexer = lex.lex()
    
    code_input = json.loads(request.get_data())["code_string"]
    
    code_output = []
    
    # Give the lexer some input
    lexer.input(code_input)
    # Tokenize
    while True:
        tok = lexer.token()
        code_output.append(str(tok))
        if not tok: 
            break     # No more input
        print(tok)
    
    print("Input: ")
    print(code_input)
    print("Output: ")
    print(code_output)
    
    return code_output # An array of lines of code output


# PLY lexer

import ply.lex as lex

# List of token names.
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

# Handling reserved words
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'join' : 'JOIN',
    'in' : 'IN',
    'do' : 'DO',
    'let' : 'LET',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    'show' : 'SHOW',
    'risk' : 'RISK',
    'save' : 'SAVE',
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

# Regular expression rules for simple tokens
t_PLUS    = r'PLUS'
t_MINUS   = r'MINUS'
t_TIMES   = r'TIMES'
t_LPAREN  = r'\('
t_DIVIDE  = r'DIVIDE'
t_RPAREN  = r'\)'
t_POWER   = r'RAISED_TO'

###
### Rules
###

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

#def t_ID(t):
#    # Look up symbol table information and return a tuple
#    t.value = (t.value, symbol_lookup(t.value))
#    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    code_output.append(str("Illegal character '%s'" % t.value[0]))
    t.lexer.skip(1)
