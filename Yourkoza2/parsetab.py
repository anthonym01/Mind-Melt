
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programnonassocIS_LESS_THANIS_GREATER_THANIS_EQUAL_TOIS_NOT_EQUAL_TOGREATER_THAN_OR_EQUAL_TOLESS_THAN_OR_EQUAL_TOleftPLUSMINUSleftTIMESDIVIDErightPOWERAND CHARACTER COMMA COMMENT DECREASE DIVIDE DO ELSE END EQUAL FALSE FOR FUNCTION GREATER_THAN_OR_EQUAL_TO IDENTIFIER IF IN INCREASE INTEGER IS_EQUAL_TO IS_GREATER_THAN IS_LESS_THAN IS_NOT_EQUAL_TO JOIN LBRACE LBRACKET LESS_THAN_OR_EQUAL_TO LET LETTER LPAREN MINUS NOT NUMBER OR PLUS POWER RBRACE RBRACKET REAL RETURN RISK RPAREN SAVE SHOW STRING_LITERAL THEN TIMES TRUE WHILE\n    program : statements\n            | expression\n    \n    statements : statements statement\n               | statement\n    \n    statement : assignment\n              | conditional\n              | loop\n              | function\n              | display\n              | input\n    \n    assignment : LET IDENTIFIER EQUAL expression\n               | LET IDENTIFIER EQUAL expression_list\n               | LET IDENTIFIER EQUAL STRING_LITERAL\n               | LET IDENTIFIER EQUAL REAL\n               | LET IDENTIFIER EQUAL NUMBER\n               | LET IDENTIFIER EQUAL CHARACTER\n               | LET IDENTIFIER EQUAL list\n    \n    comment : COMMENT\n    \n    conditional : IF condition THEN statements else_statements_opt END\n    \n    else_statements_opt : ELSE statements\n                        | empty\n    \n    condition : expression IS_LESS_THAN expression\n              | expression IS_EQUAL_TO expression\n              | expression IS_GREATER_THAN expression\n              | expression IS_NOT_EQUAL_TO expression\n              | expression GREATER_THAN_OR_EQUAL_TO expression\n              | expression LESS_THAN_OR_EQUAL_TO expression\n    \n    expression : expression PLUS term\n               | expression MINUS term\n               | term\n               | expression POWER term\n               | NOT expression\n               | LPAREN expression RPAREN\n               | NUMBER MINUS term\n               | REAL MINUS term\n               | CHARACTER PLUS term\n               | list\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n         | IDENTIFIER\n         | factor\n    \n    factor : NUMBER\n           | LPAREN expression RPAREN\n           | REAL\n    \n    input : LET IDENTIFIER EQUAL SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN\n    \n    display : SHOW expression\n            | SHOW STRING_LITERAL\n            | SHOW IDENTIFIER\n            | SHOW NUMBER\n            | SHOW REAL\n            | SHOW CHARACTER\n            | SHOW list\n            | SHOW function\n            | SHOW conditional\n            | SHOW loop\n            | SHOW input\n            | SHOW comment\n            | SHOW program\n            | SHOW statements\n            | SHOW expression_list\n            | SHOW assignment\n            | SHOW display\n    \n    loop : FOR IDENTIFIER IN list DO statements\n         | WHILE condition DO statements\n         | DO statements WHILE condition\n    \n    list : LBRACKET expression_list RBRACKET\n         | empty\n    \n    expression_list : expression\n                    | expression_list COMMA expression\n                    | empty\n    \n    function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE\n    \n    parameters : IDENTIFIER\n               | parameters COMMA IDENTIFIER\n               | empty\n    \n    return_statement_opt : RETURN expression\n                         | empty\n    \n    empty : \n    '
    
_lr_action_items = {'NOT':([0,6,7,20,23,26,28,72,83,84,86,87,88,89,90,91,93,120,140,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'LPAREN':([0,6,7,20,23,26,28,30,31,32,33,34,37,38,39,49,72,83,84,86,87,88,89,90,91,93,120,122,140,],[7,7,7,7,7,7,7,72,72,72,72,72,72,72,72,95,7,7,7,7,7,7,7,7,7,7,7,129,7,]),'NUMBER':([0,6,7,20,23,26,28,30,31,32,33,34,37,38,39,72,83,84,86,87,88,89,90,91,93,120,140,],[8,8,8,8,8,8,53,71,71,71,71,71,71,71,71,8,8,103,8,8,8,8,8,8,8,103,8,]),'REAL':([0,6,7,20,23,26,28,30,31,32,33,34,37,38,39,72,83,84,86,87,88,89,90,91,93,120,140,],[9,9,9,9,9,9,54,73,73,73,73,73,73,73,73,9,9,102,9,9,9,9,9,9,9,102,9,]),'CHARACTER':([0,6,7,20,23,26,28,72,83,84,86,87,88,89,90,91,93,120,140,],[10,10,10,10,10,10,55,10,10,104,10,10,10,10,10,10,10,104,10,]),'IDENTIFIER':([0,6,7,20,22,23,24,26,27,28,30,31,32,37,38,39,68,72,83,84,86,87,88,89,90,91,93,95,106,120,128,140,],[19,19,19,19,43,19,46,19,49,52,19,19,19,19,19,19,96,19,19,19,19,19,19,19,19,19,19,117,122,19,134,19,]),'LBRACKET':([0,6,7,20,23,26,28,72,83,84,86,87,88,89,90,91,92,93,120,140,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'LET':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,124,126,130,131,132,133,136,137,142,],[22,22,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,22,68,-3,-32,-67,22,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,22,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,22,-77,-77,-77,-77,-77,-77,22,-69,-11,-12,-13,-14,-15,-16,-17,22,-22,-23,-24,-25,-26,-27,-65,22,-77,-43,22,22,-19,22,22,22,22,-45,-71,]),'IF':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,124,126,130,131,132,133,136,137,142,],[23,23,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,23,23,-3,-32,-67,23,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,23,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,23,-77,-77,-77,-77,-77,-77,23,-69,-11,-12,-13,-14,-15,-16,-17,23,-22,-23,-24,-25,-26,-27,-65,23,-77,-43,23,23,-19,23,23,23,23,-45,-71,]),'FOR':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,124,126,130,131,132,133,136,137,142,],[24,24,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,24,24,-3,-32,-67,24,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,24,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,24,-77,-77,-77,-77,-77,-77,24,-69,-11,-12,-13,-14,-15,-16,-17,24,-22,-23,-24,-25,-26,-27,-65,24,-77,-43,24,24,-19,24,24,24,24,-45,-71,]),'WHILE':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,124,126,130,131,132,133,136,137,142,],[26,26,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,26,26,-3,-32,-67,93,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,26,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,26,-77,-77,-77,-77,-77,-77,26,-69,-11,-12,-13,-14,-15,-16,-17,26,-22,-23,-24,-25,-26,-27,-65,26,-77,-43,26,26,-19,26,26,26,26,-45,-71,]),'DO':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,120,121,124,126,130,131,132,133,136,137,142,],[25,25,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,25,25,-3,-32,-67,25,94,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,25,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,25,-77,-77,-77,-77,-77,-77,-77,25,-69,-11,-12,-13,-14,-15,-16,-17,25,-22,-23,-24,-25,-26,-27,126,94,25,-77,-43,25,25,-19,25,25,25,25,-45,-71,]),'FUNCTION':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,124,126,130,131,132,133,136,137,142,],[27,27,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,27,27,-3,-32,-67,27,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,27,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,27,-77,-77,-77,-77,-77,-77,27,-69,-11,-12,-13,-14,-15,-16,-17,27,-22,-23,-24,-25,-26,-27,-65,27,-77,-43,27,27,-19,27,27,27,27,-45,-71,]),'SHOW':([0,2,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,25,28,29,35,42,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,124,126,130,131,132,133,136,137,142,],[28,28,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,28,28,-3,-32,-67,28,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,28,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,106,28,-77,-77,-77,-77,-77,-77,28,-69,-11,-12,-13,-14,-15,-16,-17,28,-22,-23,-24,-25,-26,-27,-65,28,106,-43,28,28,-19,28,28,28,28,-45,-71,]),'PLUS':([0,3,5,6,7,8,9,10,11,18,19,20,21,23,26,28,35,36,41,42,45,50,52,53,54,55,56,67,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,93,97,98,99,102,103,104,105,108,109,110,111,112,113,120,121,140,143,],[-77,30,-30,-77,-77,-42,-44,39,-37,-41,-40,-77,-67,-77,-77,-77,30,30,30,-67,30,30,-40,-42,-44,39,-37,-67,-28,-42,-77,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-77,30,30,30,-44,-42,39,-37,30,30,30,30,30,30,-77,-43,-77,30,]),'MINUS':([0,3,5,6,7,8,9,11,18,19,20,21,23,26,28,35,36,41,42,45,50,52,53,54,56,67,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,93,97,98,99,102,103,105,108,109,110,111,112,113,120,121,140,143,],[-77,31,-30,-77,-77,37,38,-37,-41,-40,-77,-67,-77,-77,-77,31,31,31,-67,31,31,-40,37,38,-37,-67,-28,-42,-77,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-77,31,31,31,38,37,-37,31,31,31,31,31,31,-77,-43,-77,31,]),'POWER':([0,3,5,6,7,8,9,11,18,19,20,21,23,26,28,35,36,41,42,45,50,52,53,54,56,67,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,93,97,98,99,102,103,105,108,109,110,111,112,113,120,121,140,143,],[-77,32,-30,-77,-77,-42,-44,-37,-41,-40,-77,-67,-77,-77,-77,32,32,32,-67,32,32,-40,-42,-44,-37,-67,-28,-42,-77,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-77,32,32,32,-44,-42,-37,32,32,32,32,32,32,-77,-43,-77,32,]),'$end':([0,1,2,3,4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,28,29,35,42,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,98,99,100,101,102,103,104,105,108,109,110,111,112,113,115,116,120,121,130,132,137,142,],[-77,0,-1,-2,-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,-77,-3,-32,-67,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,-1,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-69,-11,-12,-13,-14,-15,-16,-17,-22,-23,-24,-25,-26,-27,-65,-64,-77,-43,-19,-63,-45,-71,]),'ELSE':([4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,28,29,35,42,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,130,132,137,142,],[-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,-77,-3,-32,-67,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,-1,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-69,-11,-12,-13,-14,-15,-16,-17,124,-22,-23,-24,-25,-26,-27,-65,-64,-77,-43,-19,-63,-45,-71,]),'END':([4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,28,29,35,42,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,98,99,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,120,121,123,125,130,131,132,137,142,],[-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,-77,-3,-32,-67,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,-1,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-69,-11,-12,-13,-14,-15,-16,-17,-77,-22,-23,-24,-25,-26,-27,-65,-64,-77,-43,130,-21,-19,-20,-63,-45,-71,]),'RBRACE':([4,5,6,8,9,11,12,13,14,15,16,17,18,19,21,28,29,35,42,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,98,99,100,101,102,103,104,105,108,109,110,111,112,113,115,116,120,121,130,132,136,137,138,139,140,141,142,143,],[-4,-30,-77,-42,-44,-37,-5,-6,-7,-8,-9,-10,-41,-40,-67,-77,-3,-32,-67,-2,-47,-40,-42,-44,-51,-37,-8,-6,-7,-10,-57,-58,-1,-60,-5,-9,-67,-18,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-77,-77,-69,-11,-12,-13,-14,-15,-16,-17,-22,-23,-24,-25,-26,-27,-65,-64,-77,-43,-19,-63,138,-45,-77,142,-77,-76,-71,-75,]),'RPAREN':([5,6,7,8,9,11,18,19,21,35,36,70,71,72,73,74,75,76,77,78,79,80,81,82,95,97,117,118,119,121,134,135,],[-30,-77,-77,-42,-44,-37,-41,-40,-67,-32,78,-28,-42,-77,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,121,-72,127,-74,-43,-73,137,]),'RBRACKET':([5,6,8,9,11,18,19,20,21,35,40,41,42,70,71,73,74,75,76,77,78,79,80,81,82,83,98,121,],[-30,-77,-42,-44,-37,-41,-40,-77,-67,-32,82,-68,-67,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-69,-43,]),'COMMA':([5,6,8,9,11,18,19,20,21,28,35,40,41,42,50,52,53,54,56,64,67,70,71,73,74,75,76,77,78,79,80,81,82,83,84,95,98,99,100,102,103,105,117,118,119,120,121,134,],[-30,-77,-42,-44,-37,-41,-40,-77,-67,-77,-32,83,-68,-67,-68,-40,-42,-44,-37,83,-67,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-69,-68,83,-44,-42,-37,-72,128,-74,-77,-43,-73,]),'IS_LESS_THAN':([5,6,8,9,11,18,19,21,23,26,35,45,70,71,73,74,75,76,77,78,79,80,81,82,93,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-77,-77,-32,86,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-43,]),'IS_EQUAL_TO':([5,6,8,9,11,18,19,21,23,26,35,45,70,71,73,74,75,76,77,78,79,80,81,82,93,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-77,-77,-32,87,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-43,]),'IS_GREATER_THAN':([5,6,8,9,11,18,19,21,23,26,35,45,70,71,73,74,75,76,77,78,79,80,81,82,93,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-77,-77,-32,88,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-43,]),'IS_NOT_EQUAL_TO':([5,6,8,9,11,18,19,21,23,26,35,45,70,71,73,74,75,76,77,78,79,80,81,82,93,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-77,-77,-32,89,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-43,]),'GREATER_THAN_OR_EQUAL_TO':([5,6,8,9,11,18,19,21,23,26,35,45,70,71,73,74,75,76,77,78,79,80,81,82,93,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-77,-77,-32,90,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-43,]),'LESS_THAN_OR_EQUAL_TO':([5,6,8,9,11,18,19,21,23,26,35,45,70,71,73,74,75,76,77,78,79,80,81,82,93,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-77,-77,-32,91,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-43,]),'THEN':([5,6,8,9,11,18,19,21,35,44,70,71,73,74,75,76,77,78,79,80,81,82,86,87,88,89,90,91,108,109,110,111,112,113,121,],[-30,-77,-42,-44,-37,-41,-40,-67,-32,85,-28,-42,-44,-29,-31,-38,-39,-33,-34,-35,-36,-66,-77,-77,-77,-77,-77,-77,-22,-23,-24,-25,-26,-27,-43,]),'TIMES':([5,8,9,18,19,52,53,54,70,71,73,74,75,76,77,78,79,80,81,102,103,121,],[33,-42,-44,-41,-40,-40,-42,-44,33,-42,-44,33,33,-38,-39,-43,33,33,33,-44,-42,-43,]),'DIVIDE':([5,8,9,18,19,52,53,54,70,71,73,74,75,76,77,78,79,80,81,102,103,121,],[34,-42,-44,-41,-40,-40,-42,-44,34,-42,-44,34,34,-38,-39,-43,34,34,34,-44,-42,-43,]),'STRING_LITERAL':([28,84,120,129,],[51,101,101,135,]),'COMMENT':([28,],[69,]),'EQUAL':([43,96,],[84,120,]),'IN':([46,],[92,]),'LBRACE':([127,],[133,]),'RETURN':([138,],[140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,28,],[1,62,]),'statements':([0,25,28,85,94,124,126,133,],[2,47,63,107,116,131,132,136,]),'expression':([0,6,7,20,23,26,28,72,83,84,86,87,88,89,90,91,93,120,140,],[3,35,36,41,45,45,50,97,98,99,108,109,110,111,112,113,45,99,143,]),'statement':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[4,29,4,4,29,29,4,4,29,29,4,4,29,29,4,29,]),'term':([0,6,7,20,23,26,28,30,31,32,37,38,39,72,83,84,86,87,88,89,90,91,93,120,140,],[5,5,5,5,5,5,5,70,74,75,79,80,81,5,5,5,5,5,5,5,5,5,5,5,5,]),'list':([0,6,7,20,23,26,28,72,83,84,86,87,88,89,90,91,92,93,120,140,],[11,11,11,11,11,11,56,11,11,105,11,11,11,11,11,11,114,11,105,11,]),'assignment':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[12,12,12,65,12,12,12,12,12,12,12,12,12,12,12,12,]),'conditional':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[13,13,13,58,13,13,13,13,13,13,13,13,13,13,13,13,]),'loop':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[14,14,14,59,14,14,14,14,14,14,14,14,14,14,14,14,]),'function':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[15,15,15,57,15,15,15,15,15,15,15,15,15,15,15,15,]),'display':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[16,16,16,66,16,16,16,16,16,16,16,16,16,16,16,16,]),'input':([0,2,25,28,47,63,85,94,107,116,124,126,131,132,133,136,],[17,17,17,60,17,17,17,17,17,17,17,17,17,17,17,17,]),'factor':([0,6,7,20,23,26,28,30,31,32,33,34,37,38,39,72,83,84,86,87,88,89,90,91,93,120,140,],[18,18,18,18,18,18,18,18,18,18,76,77,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'empty':([0,6,7,20,23,26,28,72,83,84,86,87,88,89,90,91,92,93,95,107,120,138,140,],[21,21,21,42,21,21,67,21,21,42,21,21,21,21,21,21,21,21,119,125,42,141,21,]),'expression_list':([20,28,84,120,],[40,64,100,100,]),'condition':([23,26,93,],[44,48,115,]),'comment':([28,],[61,]),'parameters':([95,],[118,]),'else_statements_opt':([107,],[123,]),'return_statement_opt':([138,],[139,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','yacc.py',39),
  ('program -> expression','program',1,'p_program','yacc.py',40),
  ('statements -> statements statement','statements',2,'p_statements','yacc.py',46),
  ('statements -> statement','statements',1,'p_statements','yacc.py',47),
  ('statement -> assignment','statement',1,'p_statement','yacc.py',59),
  ('statement -> conditional','statement',1,'p_statement','yacc.py',60),
  ('statement -> loop','statement',1,'p_statement','yacc.py',61),
  ('statement -> function','statement',1,'p_statement','yacc.py',62),
  ('statement -> display','statement',1,'p_statement','yacc.py',63),
  ('statement -> input','statement',1,'p_statement','yacc.py',64),
  ('assignment -> LET IDENTIFIER EQUAL expression','assignment',4,'p_assignment','yacc.py',71),
  ('assignment -> LET IDENTIFIER EQUAL expression_list','assignment',4,'p_assignment','yacc.py',72),
  ('assignment -> LET IDENTIFIER EQUAL STRING_LITERAL','assignment',4,'p_assignment','yacc.py',73),
  ('assignment -> LET IDENTIFIER EQUAL REAL','assignment',4,'p_assignment','yacc.py',74),
  ('assignment -> LET IDENTIFIER EQUAL NUMBER','assignment',4,'p_assignment','yacc.py',75),
  ('assignment -> LET IDENTIFIER EQUAL CHARACTER','assignment',4,'p_assignment','yacc.py',76),
  ('assignment -> LET IDENTIFIER EQUAL list','assignment',4,'p_assignment','yacc.py',77),
  ('comment -> COMMENT','comment',1,'p_comment','yacc.py',85),
  ('conditional -> IF condition THEN statements else_statements_opt END','conditional',6,'p_conditional','yacc.py',91),
  ('else_statements_opt -> ELSE statements','else_statements_opt',2,'p_else_statements_opt','yacc.py',97),
  ('else_statements_opt -> empty','else_statements_opt',1,'p_else_statements_opt','yacc.py',98),
  ('condition -> expression IS_LESS_THAN expression','condition',3,'p_condition','yacc.py',106),
  ('condition -> expression IS_EQUAL_TO expression','condition',3,'p_condition','yacc.py',107),
  ('condition -> expression IS_GREATER_THAN expression','condition',3,'p_condition','yacc.py',108),
  ('condition -> expression IS_NOT_EQUAL_TO expression','condition',3,'p_condition','yacc.py',109),
  ('condition -> expression GREATER_THAN_OR_EQUAL_TO expression','condition',3,'p_condition','yacc.py',110),
  ('condition -> expression LESS_THAN_OR_EQUAL_TO expression','condition',3,'p_condition','yacc.py',111),
  ('expression -> expression PLUS term','expression',3,'p_expression','yacc.py',117),
  ('expression -> expression MINUS term','expression',3,'p_expression','yacc.py',118),
  ('expression -> term','expression',1,'p_expression','yacc.py',119),
  ('expression -> expression POWER term','expression',3,'p_expression','yacc.py',120),
  ('expression -> NOT expression','expression',2,'p_expression','yacc.py',121),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','yacc.py',122),
  ('expression -> NUMBER MINUS term','expression',3,'p_expression','yacc.py',123),
  ('expression -> REAL MINUS term','expression',3,'p_expression','yacc.py',124),
  ('expression -> CHARACTER PLUS term','expression',3,'p_expression','yacc.py',125),
  ('expression -> list','expression',1,'p_expression','yacc.py',126),
  ('term -> term TIMES factor','term',3,'p_term','yacc.py',153),
  ('term -> term DIVIDE factor','term',3,'p_term','yacc.py',154),
  ('term -> IDENTIFIER','term',1,'p_term','yacc.py',155),
  ('term -> factor','term',1,'p_term','yacc.py',156),
  ('factor -> NUMBER','factor',1,'p_factor','yacc.py',172),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','yacc.py',173),
  ('factor -> REAL','factor',1,'p_factor','yacc.py',174),
  ('input -> LET IDENTIFIER EQUAL SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN','input',8,'p_input','yacc.py',183),
  ('display -> SHOW expression','display',2,'p_display','yacc.py',189),
  ('display -> SHOW STRING_LITERAL','display',2,'p_display','yacc.py',190),
  ('display -> SHOW IDENTIFIER','display',2,'p_display','yacc.py',191),
  ('display -> SHOW NUMBER','display',2,'p_display','yacc.py',192),
  ('display -> SHOW REAL','display',2,'p_display','yacc.py',193),
  ('display -> SHOW CHARACTER','display',2,'p_display','yacc.py',194),
  ('display -> SHOW list','display',2,'p_display','yacc.py',195),
  ('display -> SHOW function','display',2,'p_display','yacc.py',196),
  ('display -> SHOW conditional','display',2,'p_display','yacc.py',197),
  ('display -> SHOW loop','display',2,'p_display','yacc.py',198),
  ('display -> SHOW input','display',2,'p_display','yacc.py',199),
  ('display -> SHOW comment','display',2,'p_display','yacc.py',200),
  ('display -> SHOW program','display',2,'p_display','yacc.py',201),
  ('display -> SHOW statements','display',2,'p_display','yacc.py',202),
  ('display -> SHOW expression_list','display',2,'p_display','yacc.py',203),
  ('display -> SHOW assignment','display',2,'p_display','yacc.py',204),
  ('display -> SHOW display','display',2,'p_display','yacc.py',205),
  ('loop -> FOR IDENTIFIER IN list DO statements','loop',6,'p_loop','yacc.py',211),
  ('loop -> WHILE condition DO statements','loop',4,'p_loop','yacc.py',212),
  ('loop -> DO statements WHILE condition','loop',4,'p_loop','yacc.py',213),
  ('list -> LBRACKET expression_list RBRACKET','list',3,'p_list','yacc.py',220),
  ('list -> empty','list',1,'p_list','yacc.py',221),
  ('expression_list -> expression','expression_list',1,'p_expression_list','yacc.py',229),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','yacc.py',230),
  ('expression_list -> empty','expression_list',1,'p_expression_list','yacc.py',231),
  ('function -> FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE','function',10,'p_function','yacc.py',240),
  ('parameters -> IDENTIFIER','parameters',1,'p_parameters','yacc.py',246),
  ('parameters -> parameters COMMA IDENTIFIER','parameters',3,'p_parameters','yacc.py',247),
  ('parameters -> empty','parameters',1,'p_parameters','yacc.py',248),
  ('return_statement_opt -> RETURN expression','return_statement_opt',2,'p_return_statement_opt','yacc.py',257),
  ('return_statement_opt -> empty','return_statement_opt',1,'p_return_statement_opt','yacc.py',258),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',266),
]
