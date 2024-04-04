
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
    ),  # fix maybe
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
            | expression
    """
    p[0] = p[1]

def p_statements(p):
    """
    statements : statements statement
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
              | display
              | input
    """
    p[0] = ('statement', p[1])


def p_assignment(p):
    """
    assignment : LET IDENTIFIER EQUAL expression
    """
    p[0] = ('assignment', p[2], p[4])


def p_comment(p):
    """
    comment : COMMENT
    """
    p[0] = ('comment', p[1])

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
    expression : expression PLUS term
               | expression MINUS term
               | term
               | expression POWER term
               | NOT expression
               | LPAREN expression RPAREN
               | NUMBER MINUS term
               | REAL MINUS term
               | CHARACTER PLUS term
               | list
    """
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '**':  # Handle power operator
            p[0] = p[1] ** p[3]
    elif len(p) == 3:
        if p[1] == 'not':  # Handle NOT operator
            p[0] = not p[2]
        elif p[1] == '-':  # Handle unary minus
            p[0] = -p[2]
        elif p[1] == '+':  # Handle unary plus
            p[0] = p[2]
    else:
        p[0] = p[1]

def p_term(p):
    """
    term : term TIMES factor
         | term DIVIDE factor
         | IDENTIFIER
         | factor
    """
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    """
    factor : NUMBER
           | LPAREN expression RPAREN
           | REAL
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_input(p):
    """
    input : LET IDENTIFIER EQUAL SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN
    """
    p[0] = ('input', p[2], p[9])

def p_display(p):
    """
    display : SHOW expression
            | SHOW STRING_LITERAL
            | SHOW IDENTIFIER
            | SHOW NUMBER
            | SHOW REAL
            | SHOW CHARACTER
            | SHOW list
            | SHOW function
            | SHOW conditional
            | SHOW loop
            | SHOW input
            | SHOW comment
            | SHOW program
            | SHOW statements
            | SHOW expression_list
            | SHOW assignment
            | SHOW display
    """
    p[0] = ('display', p[2])

def p_loop(p):
    """
    loop : FOR IDENTIFIER IN list DO statements
         | WHILE condition DO statements
         | DO statements WHILE condition
         | DO statements UNTIL condition
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
                    | expression_list COMMA expression
                    | empty
    """
    if len(p) == 2:
        p[0] = ('expression_list', p[1])
    else:
        p[0] = ('expression_list', p[1], p[3])

def p_function(p):
    """
    function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE
    """
    p[0] = ('function', p[2], p[4], p[7], p[8])

def p_parameters(p):
    """
    parameters : IDENTIFIER
               | parameters COMMA IDENTIFIER
               | empty
               | IDENTIFIER COLON type
    """
    if len(p) == 2:
        p[0] = ('parameters', p[1])
    else:
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
    print("\n-------------------------------------------------------------------")
    print("Syntax error in input!: ")
    print(p)
    print('--------------------------------------------------------------------')
    

# Build the parser
parser = yacc.yacc() 
