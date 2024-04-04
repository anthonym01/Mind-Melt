
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programnonassocIS_LESS_THANIS_GREATER_THANIS_EQUAL_TOIS_NOT_EQUAL_TOGREATER_THAN_OR_EQUAL_TOLESS_THAN_OR_EQUAL_TOleftPLUSMINUSleftTIMESDIVIDErightPOWERAND CHARACTER COMMA COMMENT DECREASE DIVIDE DO ELSE END EQUAL FALSE FOR FUNCTION GREATER_THAN_OR_EQUAL_TO IDENTIFIER IF IN INCREASE INTEGER IS_EQUAL_TO IS_GREATER_THAN IS_LESS_THAN IS_NOT_EQUAL_TO JOIN LBRACE LBRACKET LESS_THAN_OR_EQUAL_TO LET LETTER LPAREN MINUS NOT NUMBER OR PLUS POWER RBRACE RBRACKET REAL RETURN RISK RPAREN SAVE SHOW STRING_LITERAL THEN TIMES TRUE WHILE\n    program : statements\n            | expression\n    \n    statements : statements statement\n               | statement\n    \n    statement : assignment\n              | conditional\n              | loop\n              | function\n              | display\n              | input\n    \n    assignment : LET IDENTIFIER EQUAL expression\n    \n    comment : COMMENT\n    conditional : IF condition THEN statements else_statements_opt END\n    else_statements_opt : ELSE statements\n                        | empty\n    condition : expression IS_LESS_THAN expression\n                 | expression IS_EQUAL_TO expression\n                 | expression IS_GREATER_THAN expression\n                 | expression IS_NOT_EQUAL_TO expression\n                 | expression GREATER_THAN_OR_EQUAL_TO expression\n                 | expression LESS_THAN_OR_EQUAL_TO expression\n    expression : expression PLUS term\n               | expression MINUS term\n               | term\n               | expression POWER term\n               | NOT expression\n               | LPAREN expression RPAREN\n               | NUMBER MINUS term\n               | REAL MINUS term\n               | CHARACTER PLUS term\n               | list\n    term : term TIMES factor\n            | term DIVIDE factor\n            | IDENTIFIER\n            | factor\n    factor : NUMBER\n              | LPAREN expression RPAREN\n    input : LET IDENTIFIER EQUAL SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN\n    display : SHOW expression\n            | SHOW STRING_LITERAL\n            | SHOW IDENTIFIER\n            | SHOW NUMBER\n            | SHOW REAL\n            | SHOW CHARACTER\n            | SHOW list\n            | SHOW function\n            | SHOW conditional\n            | SHOW loop\n            | SHOW input\n            | SHOW comment\n            | SHOW program\n            | SHOW statements\n            | SHOW expression_list\n            | SHOW assignment\n            | SHOW display\n    loop : FOR IDENTIFIER IN list DO statements\n            | WHILE condition DO statementslist : LBRACKET expression_list RBRACKET\n            | emptyexpression_list : expression\n                       | expression_list COMMA expressionfunction : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACEparameters : IDENTIFIER\n                  | parameters COMMA IDENTIFIER\n    return_statement_opt : RETURN expression\n                         | empty\n    \n    empty : \n    '
    
_lr_action_items = {'NOT':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,106,126,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'LPAREN':([0,6,7,20,23,25,27,29,30,31,32,33,36,37,38,46,68,78,79,81,82,83,84,85,86,106,108,126,],[7,7,7,7,7,7,7,68,68,68,68,68,68,68,68,89,7,7,7,7,7,7,7,7,7,7,115,7,]),'NUMBER':([0,6,7,20,23,25,27,29,30,31,32,33,36,37,38,68,78,79,81,82,83,84,85,86,106,126,],[8,8,8,8,8,8,50,67,67,67,67,67,67,67,67,8,8,8,8,8,8,8,8,8,8,8,]),'REAL':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,106,126,],[9,9,9,9,9,9,51,9,9,9,9,9,9,9,9,9,9,9,]),'CHARACTER':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,106,126,],[10,10,10,10,10,10,52,10,10,10,10,10,10,10,10,10,10,10,]),'IDENTIFIER':([0,6,7,20,22,23,24,25,26,27,29,30,31,36,37,38,64,68,78,79,81,82,83,84,85,86,89,94,106,114,126,],[19,19,19,19,41,19,44,19,46,49,19,19,19,19,19,19,90,19,19,19,19,19,19,19,19,19,104,108,19,120,19,]),'LBRACKET':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,87,106,126,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'LET':([0,2,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,88,92,93,95,103,106,107,110,112,116,117,118,119,122,123,128,],[22,22,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,64,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,22,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,22,22,-61,-11,22,22,-67,-37,22,22,-13,22,22,22,22,-38,-62,]),'IF':([0,2,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,88,92,93,95,103,106,107,110,112,116,117,118,119,122,123,128,],[23,23,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,23,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,23,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,23,23,-61,-11,23,23,-67,-37,23,23,-13,23,23,23,23,-38,-62,]),'FOR':([0,2,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,88,92,93,95,103,106,107,110,112,116,117,118,119,122,123,128,],[24,24,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,24,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,24,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,24,24,-61,-11,24,24,-67,-37,24,24,-13,24,24,24,24,-38,-62,]),'WHILE':([0,2,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,88,92,93,95,103,106,107,110,112,116,117,118,119,122,123,128,],[25,25,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,25,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,25,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,25,25,-61,-11,25,25,-67,-37,25,25,-13,25,25,25,25,-38,-62,]),'FUNCTION':([0,2,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,88,92,93,95,103,106,107,110,112,116,117,118,119,122,123,128,],[26,26,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,26,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,26,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,26,26,-61,-11,26,26,-67,-37,26,26,-13,26,26,26,26,-38,-62,]),'SHOW':([0,2,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,88,92,93,95,103,106,107,110,112,116,117,118,119,122,123,128,],[27,27,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,27,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,27,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,94,27,27,-61,-11,27,27,94,-37,27,27,-13,27,27,27,27,-38,-62,]),'PLUS':([0,3,5,6,7,8,10,11,18,19,20,21,23,25,27,34,35,40,43,47,49,50,52,53,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,91,92,93,96,97,98,99,100,101,106,107,126,129,],[-67,29,-24,-67,-67,-36,38,-31,-35,-34,-67,-59,-67,-67,-67,29,29,29,29,29,-34,-36,38,-31,-22,-36,-67,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-67,-67,-67,-67,-67,-67,29,29,29,29,29,29,29,29,29,-67,-37,-67,29,]),'MINUS':([0,3,5,6,7,8,9,11,18,19,20,21,23,25,27,34,35,40,43,47,49,50,51,53,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,91,92,93,96,97,98,99,100,101,106,107,126,129,],[-67,30,-24,-67,-67,36,37,-31,-35,-34,-67,-59,-67,-67,-67,30,30,30,30,30,-34,36,37,-31,-22,-36,-67,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-67,-67,-67,-67,-67,-67,30,30,30,30,30,30,30,30,30,-67,-37,-67,30,]),'POWER':([0,3,5,6,7,8,11,18,19,20,21,23,25,27,34,35,40,43,47,49,50,53,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,91,92,93,96,97,98,99,100,101,106,107,126,129,],[-67,31,-24,-67,-67,-36,-31,-35,-34,-67,-59,-67,-67,-67,31,31,31,31,31,-34,-36,-31,-22,-36,-67,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-67,-67,-67,-67,-67,-67,31,31,31,31,31,31,31,31,31,-67,-37,-67,31,]),'$end':([0,1,2,3,4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,92,93,103,106,107,116,118,123,128,],[-67,0,-1,-2,-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,-67,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,-1,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-61,-11,-57,-67,-37,-13,-56,-38,-62,]),'ELSE':([4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,92,93,95,103,106,107,116,118,123,128,],[-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,-67,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,-1,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-61,-11,110,-57,-67,-37,-13,-56,-38,-62,]),'END':([4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,92,93,95,103,106,107,109,111,116,117,118,123,128,],[-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,-67,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,-1,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-61,-11,-67,-57,-67,-37,116,-15,-13,-14,-56,-38,-62,]),'RBRACE':([4,5,6,8,11,12,13,14,15,16,17,18,19,21,27,28,34,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,92,93,103,106,107,116,118,122,123,124,125,126,127,128,129,],[-4,-24,-67,-36,-31,-5,-6,-7,-8,-9,-10,-35,-34,-59,-67,-3,-26,-2,-40,-34,-36,-43,-44,-31,-8,-6,-7,-10,-50,-51,-1,-53,-5,-9,-12,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-61,-11,-57,-67,-37,-13,-56,124,-38,-67,128,-67,-66,-62,-65,]),'RPAREN':([5,6,7,8,11,18,19,21,34,35,66,67,68,69,70,71,72,73,74,75,76,77,91,104,105,107,120,121,],[-24,-67,-67,-36,-31,-35,-34,-59,-26,73,-22,-36,-67,-23,-25,-32,-33,-27,-28,-29,-30,-58,107,-63,113,-37,-64,123,]),'RBRACKET':([5,6,8,11,18,19,20,21,34,39,40,66,67,69,70,71,72,73,74,75,76,77,78,92,107,],[-24,-67,-36,-31,-35,-34,-67,-59,-26,77,-60,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-61,-37,]),'COMMA':([5,6,8,11,18,19,20,21,27,34,39,40,47,49,50,53,61,66,67,69,70,71,72,73,74,75,76,77,78,92,104,105,107,120,],[-24,-67,-36,-31,-35,-34,-67,-59,-67,-26,78,-60,-60,-34,-36,-31,78,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-61,-63,114,-37,-64,]),'IS_LESS_THAN':([5,6,8,11,18,19,21,23,25,34,43,66,67,69,70,71,72,73,74,75,76,77,107,],[-24,-67,-36,-31,-35,-34,-59,-67,-67,-26,81,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-37,]),'IS_EQUAL_TO':([5,6,8,11,18,19,21,23,25,34,43,66,67,69,70,71,72,73,74,75,76,77,107,],[-24,-67,-36,-31,-35,-34,-59,-67,-67,-26,82,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-37,]),'IS_GREATER_THAN':([5,6,8,11,18,19,21,23,25,34,43,66,67,69,70,71,72,73,74,75,76,77,107,],[-24,-67,-36,-31,-35,-34,-59,-67,-67,-26,83,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-37,]),'IS_NOT_EQUAL_TO':([5,6,8,11,18,19,21,23,25,34,43,66,67,69,70,71,72,73,74,75,76,77,107,],[-24,-67,-36,-31,-35,-34,-59,-67,-67,-26,84,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-37,]),'GREATER_THAN_OR_EQUAL_TO':([5,6,8,11,18,19,21,23,25,34,43,66,67,69,70,71,72,73,74,75,76,77,107,],[-24,-67,-36,-31,-35,-34,-59,-67,-67,-26,85,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-37,]),'LESS_THAN_OR_EQUAL_TO':([5,6,8,11,18,19,21,23,25,34,43,66,67,69,70,71,72,73,74,75,76,77,107,],[-24,-67,-36,-31,-35,-34,-59,-67,-67,-26,86,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-37,]),'THEN':([5,6,8,11,18,19,21,34,42,66,67,69,70,71,72,73,74,75,76,77,81,82,83,84,85,86,96,97,98,99,100,101,107,],[-24,-67,-36,-31,-35,-34,-59,-26,80,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-67,-67,-67,-67,-16,-17,-18,-19,-20,-21,-37,]),'DO':([5,6,8,11,18,19,21,34,45,66,67,69,70,71,72,73,74,75,76,77,81,82,83,84,85,86,87,96,97,98,99,100,101,102,107,],[-24,-67,-36,-31,-35,-34,-59,-26,88,-22,-36,-23,-25,-32,-33,-27,-28,-29,-30,-58,-67,-67,-67,-67,-67,-67,-67,-16,-17,-18,-19,-20,-21,112,-37,]),'TIMES':([5,8,18,19,49,50,66,67,69,70,71,72,73,74,75,76,107,],[32,-36,-35,-34,-34,-36,32,-36,32,32,-32,-33,-37,32,32,32,-37,]),'DIVIDE':([5,8,18,19,49,50,66,67,69,70,71,72,73,74,75,76,107,],[33,-36,-35,-34,-34,-36,33,-36,33,33,-32,-33,-37,33,33,33,-37,]),'STRING_LITERAL':([27,115,],[48,121,]),'COMMENT':([27,],[65,]),'EQUAL':([41,90,],[79,106,]),'IN':([44,],[87,]),'LBRACE':([113,],[119,]),'RETURN':([124,],[126,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,27,],[1,59,]),'statements':([0,27,80,88,110,112,119,],[2,60,95,103,117,118,122,]),'expression':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,106,126,],[3,34,35,40,43,43,47,91,92,93,96,97,98,99,100,101,93,129,]),'statement':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[4,28,4,28,4,4,28,28,4,4,28,28,4,28,]),'term':([0,6,7,20,23,25,27,29,30,31,36,37,38,68,78,79,81,82,83,84,85,86,106,126,],[5,5,5,5,5,5,5,66,69,70,74,75,76,5,5,5,5,5,5,5,5,5,5,5,]),'list':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,87,106,126,],[11,11,11,11,11,11,53,11,11,11,11,11,11,11,11,11,102,11,11,]),'assignment':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[12,12,62,12,12,12,12,12,12,12,12,12,12,12,]),'conditional':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[13,13,55,13,13,13,13,13,13,13,13,13,13,13,]),'loop':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[14,14,56,14,14,14,14,14,14,14,14,14,14,14,]),'function':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[15,15,54,15,15,15,15,15,15,15,15,15,15,15,]),'display':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[16,16,63,16,16,16,16,16,16,16,16,16,16,16,]),'input':([0,2,27,60,80,88,95,103,110,112,117,118,119,122,],[17,17,57,17,17,17,17,17,17,17,17,17,17,17,]),'factor':([0,6,7,20,23,25,27,29,30,31,32,33,36,37,38,68,78,79,81,82,83,84,85,86,106,126,],[18,18,18,18,18,18,18,18,18,18,71,72,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'empty':([0,6,7,20,23,25,27,68,78,79,81,82,83,84,85,86,87,95,106,124,126,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,111,21,127,21,]),'expression_list':([20,27,],[39,61,]),'condition':([23,25,],[42,45,]),'comment':([27,],[58,]),'parameters':([89,],[105,]),'else_statements_opt':([95,],[109,]),'return_statement_opt':([124,],[125,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','yacc.py',20),
  ('program -> expression','program',1,'p_program','yacc.py',21),
  ('statements -> statements statement','statements',2,'p_statements','yacc.py',27),
  ('statements -> statement','statements',1,'p_statements','yacc.py',28),
  ('statement -> assignment','statement',1,'p_statement','yacc.py',40),
  ('statement -> conditional','statement',1,'p_statement','yacc.py',41),
  ('statement -> loop','statement',1,'p_statement','yacc.py',42),
  ('statement -> function','statement',1,'p_statement','yacc.py',43),
  ('statement -> display','statement',1,'p_statement','yacc.py',44),
  ('statement -> input','statement',1,'p_statement','yacc.py',45),
  ('assignment -> LET IDENTIFIER EQUAL expression','assignment',4,'p_assignment','yacc.py',52),
  ('comment -> COMMENT','comment',1,'p_comment','yacc.py',59),
  ('conditional -> IF condition THEN statements else_statements_opt END','conditional',6,'p_conditional','yacc.py',64),
  ('else_statements_opt -> ELSE statements','else_statements_opt',2,'p_else_statements_opt','yacc.py',69),
  ('else_statements_opt -> empty','else_statements_opt',1,'p_else_statements_opt','yacc.py',70),
  ('condition -> expression IS_LESS_THAN expression','condition',3,'p_condition','yacc.py',77),
  ('condition -> expression IS_EQUAL_TO expression','condition',3,'p_condition','yacc.py',78),
  ('condition -> expression IS_GREATER_THAN expression','condition',3,'p_condition','yacc.py',79),
  ('condition -> expression IS_NOT_EQUAL_TO expression','condition',3,'p_condition','yacc.py',80),
  ('condition -> expression GREATER_THAN_OR_EQUAL_TO expression','condition',3,'p_condition','yacc.py',81),
  ('condition -> expression LESS_THAN_OR_EQUAL_TO expression','condition',3,'p_condition','yacc.py',82),
  ('expression -> expression PLUS term','expression',3,'p_expression','yacc.py',87),
  ('expression -> expression MINUS term','expression',3,'p_expression','yacc.py',88),
  ('expression -> term','expression',1,'p_expression','yacc.py',89),
  ('expression -> expression POWER term','expression',3,'p_expression','yacc.py',90),
  ('expression -> NOT expression','expression',2,'p_expression','yacc.py',91),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','yacc.py',92),
  ('expression -> NUMBER MINUS term','expression',3,'p_expression','yacc.py',93),
  ('expression -> REAL MINUS term','expression',3,'p_expression','yacc.py',94),
  ('expression -> CHARACTER PLUS term','expression',3,'p_expression','yacc.py',95),
  ('expression -> list','expression',1,'p_expression','yacc.py',96),
  ('term -> term TIMES factor','term',3,'p_term','yacc.py',116),
  ('term -> term DIVIDE factor','term',3,'p_term','yacc.py',117),
  ('term -> IDENTIFIER','term',1,'p_term','yacc.py',118),
  ('term -> factor','term',1,'p_term','yacc.py',119),
  ('factor -> NUMBER','factor',1,'p_factor','yacc.py',130),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','yacc.py',131),
  ('input -> LET IDENTIFIER EQUAL SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN','input',8,'p_input','yacc.py',139),
  ('display -> SHOW expression','display',2,'p_display','yacc.py',144),
  ('display -> SHOW STRING_LITERAL','display',2,'p_display','yacc.py',145),
  ('display -> SHOW IDENTIFIER','display',2,'p_display','yacc.py',146),
  ('display -> SHOW NUMBER','display',2,'p_display','yacc.py',147),
  ('display -> SHOW REAL','display',2,'p_display','yacc.py',148),
  ('display -> SHOW CHARACTER','display',2,'p_display','yacc.py',149),
  ('display -> SHOW list','display',2,'p_display','yacc.py',150),
  ('display -> SHOW function','display',2,'p_display','yacc.py',151),
  ('display -> SHOW conditional','display',2,'p_display','yacc.py',152),
  ('display -> SHOW loop','display',2,'p_display','yacc.py',153),
  ('display -> SHOW input','display',2,'p_display','yacc.py',154),
  ('display -> SHOW comment','display',2,'p_display','yacc.py',155),
  ('display -> SHOW program','display',2,'p_display','yacc.py',156),
  ('display -> SHOW statements','display',2,'p_display','yacc.py',157),
  ('display -> SHOW expression_list','display',2,'p_display','yacc.py',158),
  ('display -> SHOW assignment','display',2,'p_display','yacc.py',159),
  ('display -> SHOW display','display',2,'p_display','yacc.py',160),
  ('loop -> FOR IDENTIFIER IN list DO statements','loop',6,'p_loop','yacc.py',165),
  ('loop -> WHILE condition DO statements','loop',4,'p_loop','yacc.py',166),
  ('list -> LBRACKET expression_list RBRACKET','list',3,'p_list','yacc.py',171),
  ('list -> empty','list',1,'p_list','yacc.py',172),
  ('expression_list -> expression','expression_list',1,'p_expression_list','yacc.py',178),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','yacc.py',179),
  ('function -> FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE','function',10,'p_function','yacc.py',186),
  ('parameters -> IDENTIFIER','parameters',1,'p_parameters','yacc.py',190),
  ('parameters -> parameters COMMA IDENTIFIER','parameters',3,'p_parameters','yacc.py',191),
  ('return_statement_opt -> RETURN expression','return_statement_opt',2,'p_return_statement_opt','yacc.py',199),
  ('return_statement_opt -> empty','return_statement_opt',1,'p_return_statement_opt','yacc.py',200),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',208),
]
