import ply.lex as lex
from lexTokens import *
from yacc import *
import sys

lexer = lex.lex()

symbol_table = {}  # Initialize symbol table
function_stack = {}
functioncall_stack = []

# Semantic analysis function
def semantic_analysis(tree):
    symbol_table = {}  # Reset symbol table
    
    # Function to add a variable to the symbol table
    def add_variable(name, type, value, symb_table):
        if name in symb_table:
            raise Exception(f"Variable '{name}' redeclaration error")
        symb_table[name] = (type, value)

    # Function to check if a variable has been declared
    def check_variable(name, symb_table):
        if name not in symb_table:
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

    
    def parse(args, symbols, remove):
        if isinstance(args, tuple):
            for a in args:
                parse(a, symbols, remove)
        else:
            if args != remove:
                symbols.append(args)

    # Traverse the syntax tree and perform semantic analysis
    def traverse(node):
        symb_table = symbol_table if len(functioncall_stack) <= 0 else functioncall_stack[-1:][0]["symbol_table"]
        # print(symb_table)
        if node is None:
            print("`node` provided is `None`")
            return

        if node[0] == 'assignment':
            var_name = node[1]
            var_value = node[2]
            add_variable(var_name, type(var_value).__name__, var_value, symb_table)  # Add variable to symbol table

        elif node[0] == 'expression':
            # Example: Check if variables used in expression are declared
            # Assuming expression is a binary operation (e.g., '+', '-', '*', '/')

            check_variable(node[1], symb_table)
            check_variable(node[3], symb_table)

        elif node[0] == 'function':
            function_stack[node[1]] = (node[2], node[3])
            return

        elif node[0] == 'function_call':
            from operator import itemgetter
            symbols = {}
            def parse_args(args, params, symbols, remove):
                if isinstance(args, tuple) and isinstance(params, tuple):
                    for a, p in zip(args, params):
                        parse_args(a, p, symbols, remove)
                else:
                    if args != remove:
                        symbols[args] = (type(params).__name__, params)
            
            name, args = itemgetter("name", "arguments")(node[1])
            parse_args(function_stack[name][0], args, symbols, "parameters")

            functioncall_stack.append({"name": name, "params": function_stack[name][0], "body": function_stack[name][1], "symbol_table": symbols})

            traverse(function_stack[name][1])

            functioncall_stack.pop()

        
        elif node[0] == "display":
            # checks if there is a function currently on the functioncall stack to determine what symbol table to use due to scope
            if symb_table.get(node[1]) is not None:
                print(symb_table[node[1]][1])

            # if node[1][0] == "expression_list":
            #     s, v = [], ""
            #
            #     parse(node[1], s, "expression_list")
            #     for ch in s:
            #         if symb_table.get(ch) is not None:
            #             v += symb_table[ch][1]
            #             continue
            #
            #         v += ch
            #
            #     print(v)
            else:
                print(node[1])

        elif node[0] == 'conditional':
            # Example: Check if condition expression has boolean type
            _, a, op, b = node[1]

            if symb_table.get(a) is not None:
                a = symb_table[a][1]

            if symb_table.get(b) is not None:
                b = symb_table[b][1]

            if compare(a, op, b):
                traverse(node[2])
                return
            else:
                if node[3] is not None:
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
let x equal 1
let y equal 18

function greetings(name) {
    show "Hey there ", name
}
greetings("John")
show y + 10
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

#parsex(open(filename).read())
parsex(input_code)
