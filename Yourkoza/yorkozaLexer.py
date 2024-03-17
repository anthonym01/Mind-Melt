# ------------------------------------------------------------
# yorkozaLexer.py
#
# tokenizer for the language Yorkoza
# ------------------------------------------------------------
import ply.lex as lex

#List of token names.
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
)


# Regular expression rules for simple tokens
t_PLUS    = r'PLUS'
t_MINUS   = r'MINUS'
t_TIMES   = r'TIMES'
t_LPAREN  = r'\('
t_DIVIDE  = r'DIVIDE'
t_RPAREN  = r'\)'
t_POWER   = r'RAISED_TO'


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


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
3 PLUS 4 TIMES 10
  PLUS -20 TIMES 2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

