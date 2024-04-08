import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'IDENTIFIER',
    'STRING_LITERAL',
    'INTEGER_LITERAL',
    'TYPE',
    'VOID',
    'EQUALS',
    'COLON',
    'COMMA',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_SQUARE_BRACKET',
    'RIGHT_SQUARE_BRACKET',
    'IF',
    'ELSE',
    'FOR',
    'FN',
    'PRINT',
    'AND',
)

# Regular expression rules for simple tokens
t_EQUALS = r'='
t_COLON = r':'
t_COMMA = r','
t_LEFT_BRACE = r'{'
t_RIGHT_BRACE = r'}'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_SQUARE_BRACKET = r'\['
t_RIGHT_SQUARE_BRACKET = r'\]'
t_IF = r'if'
t_ELSE = r'else'
t_FOR = r'for'
t_FN = r'fn'
t_PRINT = r'print'
t_AND = r'AND'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'void':
        t.type = 'VOID'
    elif t.value == 'str':
        t.type = 'TYPE'
    elif t.value == 'int':
        t.type = 'TYPE'
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_INTEGER_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_program(p):
    '''program : function_definition program
               | empty'''
    pass

def p_function_definition(p):
    '''function_definition : FN IDENTIFIER LEFT_PAREN parameters RIGHT_PAREN RETURNS type LEFT_BRACE statements RIGHT_BRACE'''
    pass

def p_parameters(p):
    '''parameters : parameter COMMA parameters
                  | parameter
                  | empty'''
    pass

def p_parameter(p):
    '''parameter : IDENTIFIER COLON type'''
    pass

def p_type(p):
    '''type : TYPE
            | VOID'''
    pass

def p_statements(p):
    '''statements : statement statements
                  | statement
                  | empty'''
    pass

def p_statement(p):
    '''statement : assignment_statement
                 | if_statement
                 | for_loop
                 | expression_statement'''
    pass

def p_assignment_statement(p):
    '''assignment_statement : LET IDENTIFIER COLON type EQUALS expression SEMICOLON'''
    pass

def p_if_statement(p):
    '''if_statement : IF expression LEFT_BRACE statements RIGHT_BRACE else_if_statement else_statement
                    | IF expression LEFT_BRACE statements RIGHT_BRACE'''
    pass

def p_else_if_statement(p):
    '''else_if_statement : ELSE IF expression LEFT_BRACE statements RIGHT_BRACE else_if_statement
                         | empty'''
    pass

def p_else_statement(p):
    '''else_statement : ELSE LEFT_BRACE statements RIGHT_BRACE
                      | empty'''
    pass

def p_for_loop(p):
    '''for_loop : FOR IDENTIFIER IN expression LEFT_BRACE statements RIGHT_BRACE'''
    pass

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''
    pass

def p_expression(p):
    '''expression : term
                  | expression AND expression'''
    pass

def p_term(p):
    '''term : IDENTIFIER
            | literal'''
    pass

def p_literal(p):
    '''literal : STRING_LITERAL
               | INTEGER_LITERAL
               | array_literal'''
    pass

def p_array_literal(p):
    '''array_literal : LEFT_SQUARE_BRACKET STRING_LITERAL COMMA STRING_LITERAL RIGHT_SQUARE_BRACKET'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Example input
data = '''
fn say_hi(val: str) -> void {
    print(val);
}

fn main() {
    let names: str[] = ["Aundre", "Teddy"];
    let name: str = "";
    let age: int = 12;
    say_hi(name);

    if age == 12 {

    } else if {

    } else {

    }

    for person in names  {
        say_hi(person)
    }

    if age >= 12 AND age <= 16 {

    }
}
'''

# Parse the input
parser.parse(data)