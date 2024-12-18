# ------------------------------------------------------------
# yourkoza's Lexer.py
#
# tokenizer for the language Yorkoza
# ------------------------------------------------------------
import ply.lex as lex

# PLY lexer
# Handling reserved words
# The `reserved` dictionary in the provided code snippet is mapping certain keywords in the Yorkoza
# language to their corresponding token types. Each key-value pair in the dictionary represents a
# keyword and its associated token type. For example, the keyword 'if' is mapped to the token type
# 'IF', 'then' to 'THEN', 'else' to 'ELSE', and so on.
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'end': 'END',
    'while': 'WHILE',
    'join': 'JOIN',
    'in': 'IN',
    'do': 'DO',
    'let': 'LET',
    'for': 'FOR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'show': 'SHOW',
    'risk': 'RISK',
    'save': 'SAVE',
    'equal': 'EQUAL',
}

# List of token names
tokens = list(reserved.values()) + [
    'IDENTIFIER',
    'NUMBER',
    'CHARACTER',
    'LETTER',
    'STRING_LITERAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'BOOLEAN',
    'AND',
    'OR',
    'NOT',
    'IS_EQUAL_TO',
    'IS_NOT_EQUAL_TO',
    'IS_GREATER_THAN',
    'IS_LESS_THAN',
    'GREATER_THAN_OR_EQUAL_TO',
    'LESS_THAN_OR_EQUAL_TO',
    'INCREASE',
    'DECREASE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'COMMENT',
    'TRUE',
    'FALSE',
]


# Regular expression rules for simple tokens
# These lines of code in the lexer file are defining regular expression rules for various arithmetic
# and logical operators, as well as other symbols used in the Yorkoza language. Each line associates a
# regular expression pattern with a token name.
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_IS_EQUAL_TO = r'\=='
t_IS_NOT_EQUAL_TO = r'\!='
t_IS_GREATER_THAN = r'\>'
t_IS_LESS_THAN = r'\<'
t_GREATER_THAN_OR_EQUAL_TO = r'\>='
t_LESS_THAN_OR_EQUAL_TO = r'\<='
t_INCREASE = r'\+\+'
t_DECREASE = r'\--'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r'\,'
#t_TRUE = r'true'
#t_FALSE = r'false'
#t_COMMENT = r'!'

#Regular expression rules
def t_COMMENT(t):
    r'\!.*'
    pass

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value) 
    return t

def t_CHARACTER(t):
    r"'.*'"
    t.value = t.value[1]  # Get the character inside quotes
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t


def t_AND(t):
    r'AND'
    return t


def t_OR(t):
    r'OR'
    return t


def t_NOT(t):
    r'NOT'
    return t


def t_STRING_LITERAL(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
