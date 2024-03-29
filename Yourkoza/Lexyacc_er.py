# ------------------------------------------------------------
# yorkoza's Lexer.py
#
# tokenizer for the language Yorkoza
# ------------------------------------------------------------
import ply.lex as lex
#import json
#from flask import Flask, render_template, request
#import ply.yacc as yacc

# PLY lexer
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
    'while' : 'WHILE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    'show' : 'SHOW',
    'risk' : 'RISK',
    'save' : 'SAVE',
    'be':'BE',
    'equal':'EQUAL',
    'to': 'TO',
    'then':'THEN',
    'input':'INPUT',
}

# List of token names.
tokens = list(reserved.values())+[
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
    #'ELSE',
    'WHILE',
    'FOR',
    'FUNCTION',
    'RETURN',
    'SHOW',
    'RISK',
    'SAVE',
    'COMMENT',
    'BE',
    'EQUAL',
    'TO',
    'THEN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'INPUT',
]


literals = ['{', '}','[',']','(',')',',']

def t_LBRACKET(t):
    r'\['
    t.type = '['      # Set token type to the expected literal
    return t

def t_RBRACKET(t):
    r'\]'
    t.type = ']'      # Set token type to the expected literal
    return t

def t_LPAREN(t):
    r'\('
    t.type = '('      # Set token type to the expected literal
    return t

def t_RPAREN(t):
    r'\)'
    t.type = ')'      # Set token type to the expected literal
    return t

def t_LBRACE(t):
    r'\{'
    t.type = '{'      # Set token type to the expected literal
    return t

def t_RBRACE(t):
    r'\}'
    t.type = '}'      # Set token type to the expected literal
    return t

def t_COMMA(t):
    r'\,'
    t.type = ','      # Set token type to the expected literal
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

# Regular expression rules for simple tokens
t_PLUS    = r'PLUS'
t_MINUS   = r'MINUS'
t_TIMES   = r'TIMES'
#t_LPAREN  = r'\('
t_DIVIDE  = r'DIVIDE'
#t_RPAREN  = r'\)'
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
    # code_output.append(str("Illegal character '%s'" % t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()

def Tokenize(code_string):
    
    tokenx = [] # empty list
    print("Tokenize: ")
    print(code_string)
    
    lexer.input(code_string)
    
    while True:
        tok = lexer.token()
        tokenx.append(str(tok))
        if not tok: 
            break     # No more input
        print(tok)
    return tokenx
    

import ply.yacc as yacc

precedence = (
    ('nonassoc', 'IS_LESS_THAN', 'IS_GREATER_THAN','IS_EQUAL_TO', 'IS_NOT_EQUAL_TO'),  # fix maybe
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
)

# Grammar rules

#Define start symbol of grammar
start = 'program'

def p_program(p):
    '''program : statements
                | expression'''
    p[0] = ('program',p[1])

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 2:
        p[0] = ('statements', p[1],p[2])
    else:
        p[0] = ('statements', p[1])


def p_statement(p):
    '''statement : assignment
                 | conditional
                 | loop
                 | function
                 | display
                 | input
                 | COMMENT'''
    p[0] = ('statement', p[1])


def p_assignment(p):
    '''assignment : LET IDENTIFIER BE EQUAL TO expression'''
    p[0] = ('assignment', p[2], p[5])
   

def p_conditional(p):
    '''conditional : IF condition THEN statements else_statements_opt'''
    p[0] = ('conditional', p[1], p[2], p[4], p[5])

def p_else_statements_opt(p):
    '''else_statements_opt : ELSE statements
                           | empty'''
    if len(p) == 3:
        p[0] = ('else_statements_opt', p[2])


def p_condition(p):
    '''condition : expression IS_LESS_THAN expression
                 | expression IS_EQUAL_TO expression
                 | expression IS_GREATER_THAN expression
                 | expression IS_NOT_EQUAL_TO expression'''
    p[0] = ('condition', p[1], p[2], p[3])

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_input(p):
    '''input : LET IDENTIFIER BE EQUAL TO SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN'''
    p[0] = ('input', p[2], p[9])

def p_display(p):
    '''display : SHOW expression'''
    p[0] = ('display', p[2])

def p_loop(p):
    '''loop : FOR IDENTIFIER IN list DO statements
            | WHILE condition DO statements'''
    p[0] = ('loop', p[1], p[2], p[4], p[6])
   

def p_list(p):
    '''list : LBRACKET expression_list RBRACKET
            | empty'''
    if len(p) == 4:
        p[0] = ('list', p[2])


def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    if len(p) == 2:
        p[0] = ('expression_list', p[1])
    else:
        p[0] = ('expression_list', p[1], p[3])

def p_function(p):
    '''function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE'''
    p[0] = ('function', p[2], p[4], p[7], p[9])

def p_parameters(p):
    '''parameters : IDENTIFIER
                  | parameters COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = ('parameters', p[1])
    else:
        p[0] = ('parameters', p[1], p[3])

def p_return_statement_opt(p):
    '''return_statement_opt : RETURN expression
                            | empty'''
    if len(p) == 3:
        p[0] = ('return_statement_opt', p[2])
    

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    print("Syntax error in input!")
    print(p)
    


# Build the parser
parser = yacc.yacc() 


#from yacc import parser
from parsetab import *
#from Lexer import *

# Define a symbol table to store variable information
symbol_table = {}
symbol_table['add'] = {'args': [{'type': 'int'}, {'type': 'int'}], 'return_type': 'int'}

# Function to add a variable to the symbol table
def add_variable(name, type):
    symbol_table[name] = type

# Function to check if a variable has been declared
def check_variable(name):
    if name not in symbol_table:
        raise Exception(f"Variable '{name}' not declared")

# Semantic analysis function
def semantic_analysis(ast):
    for node in ast:
        if node['type'] == 'assignment':
            var_name = node['var_name']
            var_type = node['var_type']
            add_variable(var_name, var_type)
        elif node['type'] == 'expression':
            # Example: Check if variables used in expression are declared
            if node['op'] in ['PLUS', 'MINUS', 'TIMES', 'DIVIDE']:
                check_variable(node['left'])
                check_variable(node['right'])
        elif node['type'] == 'function_call':
            function_name = node['function_name']
            # Example: Check if function exists and argument types match
            if function_name not in symbol_table:
                raise Exception(f"Function '{function_name}' not defined")
            expected_args = symbol_table[function_name]['args']
            passed_args = node['arguments']
            if len(expected_args) != len(passed_args):
                raise Exception(f"Function '{function_name}' expects {len(expected_args)} arguments, but {len(passed_args)} were provided")
            for i, arg in enumerate(passed_args):
                expected_type = expected_args[i]['type']
                # Check if argument type matches expected type
                if arg['type'] != expected_type:
                    raise Exception(f"Argument {i+1} of function '{function_name}' has incorrect type. Expected {expected_type}, got {arg['type']}")
# Build the parser
#parser = yacc.yacc(tabmodule='./parsetab.py')

#add_variable('x', 'int')
#add_variable('y', 'int')

# Test the full functionality with an example expression
#input_string = "add(x, y)"

#parser = yacc.yacc()


def parse(program_code):

    ast = parser.parse(Tokenize(program_code)[0],lexer)
    #ast = parser.parse(program_code,lexer)
    print("Ast: ")
    print(ast)
    #semantic_analysis(ast)
    return ast

parse("let x be 10")# Test parse code