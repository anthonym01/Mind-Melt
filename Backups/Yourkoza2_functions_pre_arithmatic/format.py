import ply.lex as lex
import ply.yacc as yacc


keywords = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'in': 'IN',
    'let': 'LET',
    'for': 'FOR',
    'function': 'FUNC',
    'return': 'RETURN',
}

# List of token names
tokens = [
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'MUL',
    'DIVIDE',
    'EQ',
    'LParen',
    'RParen',
    'LBrace',
    'RBrace',
    'Ident',
    'SemiColon',
    'Comment'
] + list(keywords.values())


# Dictionary to store variables and their types
variables = {}
# Stack to keep track of variable scopes
scopes = [{}]

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIVIDE = r'/'
t_EQ = r'='
t_LParen = r'\('
t_RParen = r'\)'
t_LBrace = r'\{'
t_RBrace = r'\}'
t_SemiColon = r';'

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for identifiers (variable names)
def t_Ident(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'Ident')
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore whitespace and tabs
t_ignore = ' \t'
t_ignore_Comment = r'\#.*'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

source = open("./test.y").read()

# Build the lexer
lexer = lex.lex()
# print(source)
lexer.input(source)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

variables = {}

def p_main(p):
    '''main : func_definition
            | empty
    '''
    print(list(p))
    # p[0] = ('main', p[1], p[2])

def p_func_definition(p):
    '''
        func_definition : FUNC Ident LParen RParen LBrace statements RBrace
    '''

    p[0] = ('function', p[2], p[4], p[7])

def p_empty(p):
    '''empty : '''
    pass

def p_term(p):
    '''term : Ident
            | NUMBER
            | STRING
    '''
    p[0] = ('term', p[1])

def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | for_loop
                 | expression_statement
    '''
    p[0] = ('statement', p[1])

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression MUL term
                  | expression DIVIDE term
    '''
    p[0] = ('expression', p[1], p[2], p[3])

def p_expression_statement(p):
    '''expression_statement : expression SemiColon
    '''
    p[0] = ('expression', p[1])

def p_else_if_statement(p):
    '''else_if_statement : ELSE IF expression LBrace statements RBrace else_if_statement
                         | ELSE LBrace statements RBrace
                         | empty
    '''
    pass

def p_else_statement(p):
    '''else_statement : ELSE LBrace statements RBrace
                      | empty
    '''
    pass

def p_for_loop(p):
    '''for_loop : FOR Ident IN expression LBrace statements RBrace
    '''
    pass

def p_if_statement(p):
    '''if_statement : IF expression LBrace statements RBrace else_if_statement else_statement
                    | IF expression LBrace statements RBrace
    '''
    pass
def p_statements(p):
    '''statements : statements statement
                  | statement
                  | empty
    '''
    if len(p) == 3:
        p[0] = ('statements', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('statements', p[1])
    else:
        p[0] = ('statements',)


def p_statement_assign(p):
    'assignment : LET Ident EQ NUMBER SemiColon'
    variables[p[2]] = p[4]
    p[0] = ('assign', p[2], p[4])

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
ast = parser.parse()
print(ast)

# Parsing rules
# def p_statement_assign(p):
#     'statement : ID EQUALS expression'
#     if p[1] in scopes[-1]:
#         raise ValueError(f"Variable '{p[1]}' is already defined in this scope.")
#     scopes[-1][p[1]] = type(p[3])  # Store variable and its type
#     variables[p[1]] = p[3]
#     p[0] = ('assign', p[1], p[3])

# def p_statement_print(p):
#     'statement : PRINT LPAREN expression RPAREN'
#     p[0] = ('print', p[3])

# def p_expression_binop(p):
#     '''expression : expression PLUS expression
#                   | expression MINUS expression
#                   | expression TIMES expression
#                   | expression DIVIDE expression'''
#     if type(p[1]) != int or type(p[3]) != int:
#         raise TypeError("Arithmetic operations only allowed between integers.")
#     if p[2] == '+':
#         p[0] = p[1] + p[3]
#     elif p[2] == '-':
#         p[0] = p[1] - p[3]
#     elif p[2] == '*':
#         p[0] = p[1] * p[3]
#     elif p[2] == '/':
#         p[0] = p[1] / p[3]

# def p_expression_number(p):
#     'expression : NUMBER'
#     p[0] = p[1]

# def p_expression_id(p):
#     'expression : ID'
#     if p[1] not in variables:
#         raise NameError(f"Variable '{p[1]}' is not defined.")
#     p[0] = variables[p[1]]

# def p_error(p):
#     print("Syntax error in input!: ", p)

# # Build the parser
# parser = yacc.yacc()
# ast = parser.parse(open("./test.y").read())
# print(ast)
