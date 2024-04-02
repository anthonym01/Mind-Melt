# ------------------------------------------------------------
# handles ply functions in place of Yourkoza.py
# ------------------------------------------------------------
import ply.lex as lex
from lexTokens import *
from yacc import *

# ---------------------------------------------------------
#Build the Lexer with data from /lexTokens
# ---------------------------------------------------------

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
        print('analyzing node: ',node)
        try:
            if node['type'] == 'assignment':
                try:
                    var_name = node['var_name']
                    var_type = node['var_type']
                    add_variable(var_name, var_type)
                except Exception as e:
                    print('Error on node: ',node,' | ',e)
            
            elif node['type'] == 'expression':
                # Example: Check if variables used in expression are declared
                try:
                    if node['op'] in ['PLUS', 'MINUS', 'TIMES', 'DIVIDE']:
                        check_variable(node['left'])
                        check_variable(node['right'])
                except Exception as e:
                    print('Error on node: ',node,' | ',e)

            elif node['type'] == 'function_call':
                try:
                    function_name = node['function_name']
                    # Example: Check if function exists and argument types match
                    if function_name not in symbol_table:
                        print(f"Function '{function_name}' not defined")
                
                    expected_args = symbol_table[function_name]['args']
                    passed_args = node['arguments']
                    if len(expected_args) != len(passed_args):
                        print(f"Function '{function_name}' expects {len(expected_args)} arguments, but {len(passed_args)} were provided")
                    for i, arg in enumerate(passed_args):
                        expected_type = expected_args[i]['type']
                        # Check if argument type matches expected type
                        if arg['type'] != expected_type:
                            print(f"Argument {i+1} of function '{function_name}' has incorrect type. Expected {expected_type}, got {arg['type']}")
                except Exception as e:
                    print('Error on node: ',node,' | ',e)
        except Exception as e:
            print('Critical error on node: ',node,' | ',e)


def parsex(program_code):
    
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
    semantic_analysis(ast)
    print(symbol_table)
    return ast

parsex('let x equal 0')# Test parse code