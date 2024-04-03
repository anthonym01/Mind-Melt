import ply.lex as lex
from lexTokens import *
from yacc import *

lexer = lex.lex()

symbol_table = {}  # Initialize symbol table


# Semantic analysis function
def semantic_analysis(tree):
    symbol_table = {}  # Reset symbol table
    
    # Function to add a variable to the symbol table
    def add_variable(name, type):
        if name in symbol_table:
            raise Exception(f"Variable '{name}' redeclaration error")
        symbol_table[name] = type

    # Function to check if a variable has been declared
    def check_variable(name):
        if name not in symbol_table:
            raise Exception(f"Variable '{name}' not declared")

    # Traverse the syntax tree and perform semantic analysis
    def traverse(node):
        if node[0] == 'assignment':
            var_name = node[1]
            var_value = node[2]
            add_variable(var_name, type(var_value).__name__)  # Add variable to symbol table

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
            

        elif node[0] == 'conditional':
            # Example: Check if condition expression has boolean type
            condition = node[1]
            check_boolean(condition)

        # Recursively traverse child nodes
        for child in node[1:]:
            if isinstance(child, tuple):
                traverse(child)

    # Start semantic analysis by traversing the syntax tree
    traverse(tree)
    print('Symbol table: ',symbol_table)

# Example usage:
input_code = """
let x equal 10
let y equal (12+5)
!let x equal 0
show y
let k equal 18
!k equal 4
"""

# Testing area
# Parse code and prime execution
def parsex(program_code):
    
    print("\n----------------------------------------------------------")
    print("Input code: ")
    print(program_code)
    
    print("\n----------------------------------------------------------")
    print("Tokens: ")
    lexer.input(program_code)
    for tokenx in lexer: print(tokenx)
    lexer.input(program_code)
    
    syntax_tree = parser.parse(lexer=lexer)
    
    print("\n-----------------------------------------------------")
    print("Ast Syntax tree: ")
    print(syntax_tree)
    print("\n-------------------------------------------------------------------")
    semantic_analysis(syntax_tree)# send ast tree to be analysizded
    
    return syntax_tree

parsex(input_code)