import ply.yacc as yacc
import ply.lex as lex

from Lexer import *

precedence = (
    ('nonassoc', 'IS_LESS_THAN', 'IS_GREATER_THAN','IS_EQUAL_TO', 'IS_NOT_EQUAL_TO'),  # fix maybe
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
)

# Grammar rules
def p_program(p):
    '''program : statements'''
    pass

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

def p_statement(p):
    '''statement : assignment
                 | conditional
                 | loop
                 | function
                 | display
                 | input
                 | COMMENT'''
    pass

def p_assignment(p):
    '''assignment : LET IDENTIFIER BE EQUAL TO expression'''
    pass

def p_conditional(p):
    '''conditional : IF condition THEN statements else_statements_opt'''
    pass

def p_else_statements_opt(p):
    '''else_statements_opt : ELSE statements
                           | empty'''
    pass

def p_condition(p):
    '''condition : expression IS_LESS_THAN expression
                 | expression IS_EQUAL_TO expression
                 | expression IS_GREATER_THAN expression
                 | expression IS_NOT_EQUAL_TO expression'''
    pass

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_input(p):
    '''input : LET IDENTIFIER BE EQUAL TO SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN'''
    pass

def p_display(p):
    '''display : SHOW expression'''
    pass

def p_loop(p):
    '''loop : FOR IDENTIFIER IN list DO statements
            | WHILE condition DO statements'''
    pass

def p_list(p):
    '''list : LBRACKET expression_list RBRACKET
            | empty'''
    pass

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    pass

def p_function(p):
    '''function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE'''
    pass

def p_parameters(p):
    '''parameters : IDENTIFIER
                  | parameters COMMA IDENTIFIER'''
    pass

def p_return_statement_opt(p):
    '''return_statement_opt : RETURN expression
                            | empty'''
    pass

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Syntax error in input!")
    


# Build the parser
parser = yacc.yacc()
