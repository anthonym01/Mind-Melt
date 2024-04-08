import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

def gemini_api(prompt):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    
    prompt_parts=[
        '''
        You are only to write code in a language called Yourkoza using the following tokens:
        reserved_words = [
            'if', 'then', 'else', 'end', 'while', 'join', 'in', 'do', 'let', 'for',
            'function', 'return', 'show', 'risk', 'save', 'equal'
        ]
        symbols = [
            '+', '-', '*', '/', '^', '==', '!=', '>', '<', '>=', '<=', '++', '--',
            '(', ')', '[', ']', '{', '}', ','
        ]

        and bnf grammar:

        <program> ::= <statements>

        <statements> ::= <statement> <statements>
                    | <statement>

        <statement> ::= <assignment>
                    | <conditional>
                    | <loop>
                    | <function>
                    | <function_call>
                    | <display>
                    | <expression>

        <assignment> ::= LET IDENTIFIER EQUAL <expression>
                    | LET IDENTIFIER EQUAL <expression_list>

        <conditional> ::= IF <condition> THEN <statements> <else_statements_opt> END

        <else_statements_opt> ::= ELSE <statements>
                            | empty

        <condition> ::= <expression> IS_LESS_THAN <expression>
                    | <expression> IS_EQUAL_TO <expression>
                    | <expression> IS_GREATER_THAN <expression>
                    | <expression> IS_NOT_EQUAL_TO <expression>
                    | <expression> GREATER_THAN_OR_EQUAL_TO <expression>
                    | <expression> LESS_THAN_OR_EQUAL_TO <expression>

        <expression> ::= <expression> PLUS <expression>
                    | <expression> MINUS <expression>
                    | <expression> TIMES <expression>
                    | <expression> DIVIDE <expression>
                    | <expression> POWER <expression>
                    | LPAREN <expression> RPAREN
                    | <term>
                    | <function_call>

        <term> ::= NUMBER
            | STRING_LITERAL
            | BOOLEAN
            | IDENTIFIER

        <boolean> ::= TRUE
                | FALSE

        <display> ::= SHOW STRING_LITERAL
                | SHOW IDENTIFIER

        <loop> ::= FOR IDENTIFIER IN <list> DO <statements>
            | WHILE <condition> DO <statements>
            | DO <statements> WHILE <condition>

        <list> ::= LBRACKET <expression_list> RBRACKET
            | empty

        <expression_list> ::= <expression>
                        | <expression> COMMA <expression_list>
                        | empty

        <function> ::= FUNCTION IDENTIFIER LPAREN <parameters> RPAREN LBRACE <statements> RBRACE <return_statement_opt> RBRACE
                | FUNCTION IDENTIFIER LPAREN <parameters> RPAREN LBRACE <statements> RBRACE 

        <function_call> ::= IDENTIFIER LPAREN <expression_list> RPAREN

        <parameters> ::= IDENTIFIER
                    | IDENTIFIER COMMA <parameters>
                    | empty

        <return_statement_opt> ::= RETURN <expression>
                            | empty

        <empty> ::=
        '''
        ]

    prompts = str(prompt_parts) + "\n"+ prompt
    responses = model.generate_content(prompts)
    return responses.text

def api(user_input):
    response = gemini_api(user_input)
    print(response)
    return (response)

#api("Write a code to add two numbers and display the result")
api("Write a code to Dox Jada")
