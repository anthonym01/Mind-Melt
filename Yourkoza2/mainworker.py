# ------------------------------------------------------------
# handles ply functions in place of Yourkoza.py
# ------------------------------------------------------------
import ply.lex as lex
from lexTokens import *
from yacc import *

# ---------------------------------------------------------
#Build the Lexer with data from /lexTokens
# ---------------------------------------------------------
#lexer = lex.lex(module=lexTokens)
lexer = lex.lex()

# Define a symbol table to store variable information
symbol_table = {}
#symbol_table['add'] = {'args': [{'type': 'int'}, {'type': 'int'}], 'return_type': 'int'}

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


def parsex(program_code):
    #tokenx = Tokenize(program_code)
    #print(tokenx)
    print("\n-------------------------------------------------------------------")
    print("Tokens: ")
    
    lexer.input(program_code)
    for tokenx in lexer: print(tokenx)
    
    lexer.input(program_code)
    #ast = parser.parse(program_code,lexer)
    ast = parser.parse(lexer=lexer)
    
    print("\n-------------------------------------------------------------------")
    print("Ast: ")
    print(ast)
    
    print("\n-------------------------------------------------------------------")
    print("Symbol table: ")
    #semantic_analysis(ast)
    print(symbol_table)
    return ast

parsex('let x be 2')# Test parse code