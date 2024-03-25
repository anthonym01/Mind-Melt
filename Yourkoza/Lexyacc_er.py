# ------------------------------------------------------------
# Lexical and Yaccing 
# ------------------------------------------------------------
import ply.lex as lex
#import json

# PLY lexer

# List of token names.
tokens = (
    'INTEGER',
    'IDENTIFIER',
    'REAL',
    'NUMBER',
    'CHARACTER',
    'LETTER',
    'STRING_LITERAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'LPAREN',
    'DIVIDE',
    'RPAREN',
    'POWER',
    'AND',
    'OR',
    'NOT',
    'IS_EQUAL_TO',
    'IS_NOT_EQUAL_TO',
    'IS_GREATER_THAN',
    'IS_LESS_THAN',
    'INCREASE',
    'DECREASE',
    'JOIN',
    'IN',
    'DO',
    'LET',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'FUNCTION',
    'RETURN',
    'SHOW',
    'RISK',
    'SAVE',
    'COMMENT',
    'BE',
    'EQUAL',
    'TO',
    'THEN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'INPUT',
)

# Handling reserved words
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'join' : 'JOIN',
    'in' : 'IN',
    'do' : 'DO',
    'let' : 'LET',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'return' : 'RETURN',
    'show' : 'SHOW',
    'risk' : 'RISK',
    'save' : 'SAVE',
    'be':'BE',
    'equal':'EQUAL',
    'to': 'TO',
    'then':'THEN',
    'input':'INPUT',
}

literals = ['{', '}','[',']','(',')',',']

def t_LBRACKET(t):
    r'\['
    t.type = '['      # Set token type to the expected literal
    return t

def t_RBRACKET(t):
    r'\]'
    t.type = ']'      # Set token type to the expected literal
    return t

def t_LPAREN(t):
    r'\('
    t.type = '('      # Set token type to the expected literal
    return t

def t_RPAREN(t):
    r'\)'
    t.type = ')'      # Set token type to the expected literal
    return t

def t_LBRACE(t):
    r'\{'
    t.type = '{'      # Set token type to the expected literal
    return t

def t_RBRACE(t):
    r'\}'
    t.type = '}'      # Set token type to the expected literal
    return t

def t_COMMA(t):
    r'\,'
    t.type = ','      # Set token type to the expected literal
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

# Regular expression rules for simple tokens
t_PLUS    = r'PLUS'
t_MINUS   = r'MINUS'
t_TIMES   = r'TIMES'
#t_LPAREN  = r'\('
t_DIVIDE  = r'DIVIDE'
#t_RPAREN  = r'\)'
t_POWER   = r'RAISED_TO'

###
### Rules
###

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

#def t_ID(t):
#    # Look up symbol table information and return a tuple
#    t.value = (t.value, symbol_lookup(t.value))
#    return t



# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    # code_output.append(str("Illegal character '%s'" % t.value[0]))
    t.lexer.skip(1)

def Tokenize(code_string):
    lexer = lex.lex()
    
    tokens = [] # empty list
    
    lexer.input(code_string)
    while True:
        tok = lexer.token()
        tokens.append(str(tok))
        if not tok: 
            break     # No more input
        print(tok)
    return tokens
    
