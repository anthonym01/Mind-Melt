from os import execlpe
import ply.lex as lex
from lexTokens import *
from yacc import *
import sys

lexer = lex.lex()

symbol_table = {}  # Initialize symbol table

# Semantic analysis function
def semantic_analysis(tree):
    symbol_table = {}  # Reset symbol table
    
    # Function to add a variable to the symbol table
    def add_variable(name, type, value):
        if name in symbol_table:
            raise Exception(f"Variable '{name}' redeclaration error")
        symbol_table[name] = (type, value)

    # Function to check if a variable has been declared
    def check_variable(name):
        if name not in symbol_table:
            raise Exception(f"Variable '{name}' not declared")
    
    def compare(a, op, b):
        if op == ">":
            return a > b
        if op == ">=":
            return a >= b
        if op == "<":
            return a < b
        if op == "<=":
            return a <= b
        if op == "==":
            return a == b
        if op == "!=":
            return a != b

    # Traverse the syntax tree and perform semantic analysis
    def traverse(node):
        if node[0] == 'assignment':
            var_name = node[1]
            var_value = node[2]
            add_variable(var_name, type(var_value).__name__, var_value)  # Add variable to symbol table

        elif node[0] == 'expression':
            # Example: Check if variables used in expression are declared
            # Assuming expression is a binary operation (e.g., '+', '-', '*', '/')
            check_variable(node[1])
            check_variable(node[3])

        elif node[0] == 'function':
            # Example: Check function signature
            function_name = node[1]
            parameters = node[2]
            function_body = node[3]
            # Add function signature to symbol table
        
        elif node[0] == "display":
            if symbol_table.get(node[1]) is not None:
                print(symbol_table[node[1]][1])
            else:
                print(node[1])

        elif node[0] == 'conditional':
            # Example: Check if condition expression has boolean type
            _, a, op, b = node[1]

            if symbol_table.get(a) is not None:
                a = symbol_table[a][1]

            if symbol_table.get(b) is not None:
                b = symbol_table[b][1]

            if compare(a, op, b):
                traverse(node[2])
                return
            else:
                traverse(node[3])
                return

        # Recursively traverse child nodes
        for child in node[1:]:
            if isinstance(child, tuple):
                traverse(child)

    # Start semantic analysis by traversing the syntax tree
    traverse(tree)
    # print('Symbol table: ',symbol_table)

# Example usage:
input_code = """
let age equal 18
let drinking_age equal 21

! Check if you are underage
if age < drinking_age then
    show "You are too young to drink"
else
    show "Have a good one my guy"
end

show age
"""

# Testing area
# Parse code and prime execution
def parsex(program_code):
    
    # print("\n----------------------------------------------------------")
    # print("Input code: ")
    # print(program_code)
    
    # print("\n----------------------------------------------------------")
    # print("Tokens: ")
    lexer.input(program_code)
    # for tokenx in lexer: print(tokenx)
    lexer.input(program_code)
    
    syntax_tree = parser.parse(lexer=lexer)
    
    # print("\n-----------------------------------------------------")
    # print("Ast Syntax tree: ")
    # print(syntax_tree)
    # print("\n-------------------------------------------------------------------")
    semantic_analysis(syntax_tree)# send ast tree to be analysizded
    
    return syntax_tree

filename = sys.argv[1]
if not filename:
    raise Exception("No filename provided")

parsex(open(filename).read())