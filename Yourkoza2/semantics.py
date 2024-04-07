from os import execlpe
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
    def add_variable(name, type, value, symb_t_reference):
        if name in symb_t_reference:
            raise Exception(f"Variable '{name}' redeclaration error")
        symb_t_reference[name] = (type, value)

    # Function to check if a variable has been declared
    def check_variable(name, symb_t_reference):
        if name not in symb_t_reference:
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
        symb_t_reference = symbol_table if len(functioncall_stack) <= 0 else functioncall_stack[-1:][0]["symbol_table"]
        # print(symb_t_reference)
        if node is None:
            print("`node` provided is `None`")
            return

        if node[0] == 'assignment':
            var_name = node[1]
            #print(node[2])
            if len(node) >= 3:
                if isinstance(node[2],str): 
                    var_value = node[2]
                elif isinstance(node[2],int): 
                    var_value = node[2]
                else:
                    var_value = traverse(node[2])
                    #print(traverse(node[2]))
                #print(f"Assigning {var_value} to {var_name}")
                if var_name not in symbol_table:
                    add_variable(var_name, type(var_value).__name__, var_value, symb_t_reference)   # Add variable to symbol table                
                else:
                    raise SyntaxError(f"Variable {var_name} already exists")
                return
            else:
                print("Invalid assignment node:", node)
                return


        elif node[0] == 'expression':
            #check_variable(node[1], symb_t_reference)
            #check_variable(node[3], symb_t_reference)
            
            if len(node) == 4:  # Binary operation
                operator = node[1]
                left_operand = node[2]
                right_operand = node[3]
                #print(f"Evaluating expression: {left_operand} {operator} {right_operand}")
                
                # Perform operation based on the operator
                if operator in ('+', '-', '*', '^' , '/'):
                    if operator == '+':
                        return left_operand + right_operand
                    elif operator == '-':
                        print(left_operand - right_operand)
                        return left_operand - right_operand
                    elif operator == '*':
                        return left_operand * right_operand
                    elif operator == '^':
                        return left_operand ** right_operand
                    elif operator == '/':
                        if right_operand == 0:
                            raise Exception("Division by zero error")
                        return left_operand / right_operand
                else:
                    print(f"Unsupported operator in assignment: {operator}")
                    return

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
            if symb_t_reference.get(node[1]) is not None:
                print(symb_t_reference[node[1]][1])
            else:
                print(node[1])

        elif node[0] == 'conditional':
            # Example: Check if condition expression has boolean type
            _, a, op, b = node[1]

            if symb_t_reference.get(a) is not None:
                a = symb_t_reference[a][1]

            if symb_t_reference.get(b) is not None:
                b = symb_t_reference[b][1]

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
show "boy test" 
let y equal 3 ^ 4 
show y

let age equal 18
let drinking_age equal 21

! Check if you are underage
if age < drinking_age then
    show "You are too young to drink"
else
    show "Have a good one my guy"
end

!let name equal "John"

function greetings(name) {
    show "Hey there " show name
}
greetings("John")
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



#filename = sys.argv[1]
#if not filename:
#    raise Exception("No filename provided")

#parsex(open(filename).read())
