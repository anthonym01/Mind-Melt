import ply.yacc as yacc
#from ply.lex import lex
from lexTokens import *

precedence = (
    (
        'nonassoc',
        'IS_LESS_THAN',
        'IS_GREATER_THAN',
        'IS_EQUAL_TO',
        'IS_NOT_EQUAL_TO',
        'GREATER_THAN_OR_EQUAL_TO',
        'LESS_THAN_OR_EQUAL_TO'
    ),  
    (
        'left',
        'PLUS',
        'MINUS'
    ),
    (
        'left',
        'TIMES',
        'DIVIDE'
    ),
    (
        'right',
        'POWER'
    ),
)

# Grammar rules

#Define start symbol of grammar
start = 'program'

def p_program(p):
    """
    program : statements
    """
    p[0] = p[1]

def p_statements(p):
    """
    statements : statement statements
               | statement
    """
    if len(p) == 3:
        p[0] = ('statements', p[1],p[2])
    elif len(p) == 2:
        p[0] = ('statements', p[1])
    else:
        p[0] = ('statements',)


def p_statement(p):
    """
    statement : assignment
              | conditional
              | loop
              | function
              | function_call
              | display
              | expression
    """
    p[0] = p[1]


def p_assignment(p):
    """
    assignment : LET IDENTIFIER EQUAL expression
               | LET IDENTIFIER EQUAL expression_list
    """
    #if len(p) == 4:
    p[0] = ('assignment', p[2], p[4])


def p_conditional(p):
    """
    conditional : IF condition THEN statements else_statements_opt END
    """
    p[0] = ('conditional', p[2], p[4], p[5])

def p_else_statements_opt(p):
    """
    else_statements_opt : ELSE statements
                        | empty
    """
    if len(p) == 3:
        p[0] = ('else_statements_opt', p[2])


def p_condition(p):
    """
    condition : expression IS_LESS_THAN expression
              | expression IS_EQUAL_TO expression
              | expression IS_GREATER_THAN expression
              | expression IS_NOT_EQUAL_TO expression
              | expression GREATER_THAN_OR_EQUAL_TO expression
              | expression LESS_THAN_OR_EQUAL_TO expression
    """
    p[0] = ('condition', p[1], p[2], p[3])

def p_expression(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
               | LPAREN expression RPAREN
               | term
               | function_call
    """
    if len(p) == 4:
        p[0] = ('expression', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    """
    term : NUMBER
         | STRING_LITERAL
         | BOOLEAN
         | IDENTIFIER
    """
    p[0] = p[1]


def p_boolean(p):
    """
    boolean : TRUE
            | FALSE
    """
    p[0] = ('boolean', p[1])


def p_display(p):
    """
    display : SHOW STRING_LITERAL
            | SHOW IDENTIFIER
    """
    p[0] = ('display', p[2])

def p_loop(p):
    """
    loop : FOR IDENTIFIER IN list DO statements
         | WHILE condition DO statements
         | DO statements WHILE condition
    """
    p[0] = ('loop', p[1], p[2], p[4], p[6])


def p_list(p):
    """
    list : LBRACKET expression_list RBRACKET
         | empty
    """
    if len(p) == 4:
        p[0] = ('list', p[2])


def p_expression_list(p):
    """
    expression_list : expression
                    | expression COMMA expression_list
                    | empty
    """
    if len(p) == 2:
        p[0] = ('expression_list', p[1])
    else:
        p[0] = ('expression_list', p[1], p[3])

def p_function(p):
    """
    function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE
             | FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE 
    """
    p[0] = ('function', p[2], p[4], p[7], p[8])


def p_function_call(p):
    """
    function_call : IDENTIFIER LPAREN STRING_LITERAL RPAREN
                  | IDENTIFIER LPAREN NUMBER RPAREN
    """
    p[0] = ('function_call', p[1], p[3])


def p_parameters(p):
    """
    parameters : IDENTIFIER
               | IDENTIFIER COMMA parameters
               | empty
    """
    if len(p) == 2:
        p[0] = ('parameters', p[1])
    elif len(p) == 4:
        p[0] = ('parameters', p[1], p[3])

def p_return_statement_opt(p):
    """
    return_statement_opt : RETURN expression
                         | empty
    """
    if len(p) == 3:
        p[0] = ('return_statement_opt', p[2])
    

def p_empty(p):
    """
    empty : 
    """
    pass


def p_error(p):
    from semantics import show_puts
    print("\n-------------------------------------------------------------------")
    print(f"SyntaxError: Illegal character {p.value}")
    show_puts.append(f"SyntaxError: Illegal character {p.value} at position {str(p.lexpos)} ")
    #show_puts.append(f"SyntaxError: Illegal character {str(p.lexline)}")
    print('--------------------------------------------------------------------')
    

# Build the parser
parser = yacc.yacc() 
