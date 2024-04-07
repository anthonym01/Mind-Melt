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
        #print("Processing node:", node)
        #print("Node length:", len(node))
        if len(node) == 0:
            return  # Empty node, nothing to traverse
        #print(node[0])
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
                    add_variable(var_name, type(var_value).__name__, var_value)  # Add variable to symbol table                
                else:
                    raise SyntaxError(f"Variable {var_name} already exists")
                return
            else:
                print("Invalid assignment node:", node)
                return


        elif node[0] == 'expression':
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
show "boy" 
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
let name equal jada
function greetings(name) {
    show "Hey there "
    show name
    let name equal 9
    show name
}
return name
}

!while age < 21 do
    !show "You are underage"
    !let age equal age + 1
!end

!function greetings(name) {
!    show "Hey there ", name
!}
!greetings("John")
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

