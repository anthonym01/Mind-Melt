
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIS_LESS_THANIS_GREATER_THANIS_EQUAL_TOIS_NOT_EQUAL_TOleftPLUSMINUSleftTIMESDIVIDErightPOWERAND BE CHARACTER COMMA COMMENT DECREASE DIVIDE DO ELSE EQUAL FOR FUNCTION IDENTIFIER IF IN INCREASE INPUT INTEGER IS_EQUAL_TO IS_GREATER_THAN IS_LESS_THAN IS_NOT_EQUAL_TO JOIN LBRACE LBRACKET LET LETTER LPAREN MINUS NOT NUMBER OR PLUS POWER RBRACE RBRACKET REAL RETURN RISK RPAREN SAVE SHOW STRING_LITERAL THEN TIMES TO WHILEprogram : statementsstatements : statements statement\n                  | statementstatement : assignment\n                 | conditional\n                 | loop\n                 | function\n                 | display\n                 | input\n                 | COMMENTassignment : LET IDENTIFIER BE EQUAL TO expressionconditional : IF condition THEN statements else_statements_optelse_statements_opt : ELSE statements\n                           | emptycondition : expression IS_LESS_THAN expression\n                 | expression IS_EQUAL_TO expression\n                 | expression IS_GREATER_THAN expression\n                 | expression IS_NOT_EQUAL_TO expressionexpression : expression PLUS term\n                  | expression MINUS term\n                  | termterm : term TIMES factor\n            | term DIVIDE factor\n            | factorfactor : NUMBER\n              | LPAREN expression RPARENinput : LET IDENTIFIER BE EQUAL TO SHOW IDENTIFIER LPAREN STRING_LITERAL RPARENdisplay : SHOW expressionloop : FOR IDENTIFIER IN list DO statements\n            | WHILE condition DO statementslist : LBRACKET expression_list RBRACKET\n            | emptyexpression_list : expression\n                       | expression_list COMMA expressionfunction : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACEparameters : IDENTIFIER\n                  | parameters COMMA IDENTIFIERreturn_statement_opt : RETURN expression\n                            | emptyempty :'
    
_lr_action_items = {'COMMENT':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,61,62,63,64,69,71,72,75,79,86,87,],[10,10,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,10,10,10,-19,-20,-22,-23,-26,10,-12,10,-14,10,-11,10,10,10,10,-27,-35,]),'LET':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,61,62,63,64,69,71,72,75,79,86,87,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,11,11,11,-19,-20,-22,-23,-26,11,-12,11,-14,11,-11,11,11,11,11,-27,-35,]),'IF':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,61,62,63,64,69,71,72,75,79,86,87,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,12,12,12,-19,-20,-22,-23,-26,12,-12,12,-14,12,-11,12,12,12,12,-27,-35,]),'FOR':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,61,62,63,64,69,71,72,75,79,86,87,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,13,13,13,-19,-20,-22,-23,-26,13,-12,13,-14,13,-11,13,13,13,13,-27,-35,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,61,62,63,64,69,71,72,75,79,86,87,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,14,14,14,-19,-20,-22,-23,-26,14,-12,14,-14,14,-11,14,14,14,14,-27,-35,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,61,62,63,64,69,71,72,75,79,86,87,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,15,15,15,-19,-20,-22,-23,-26,15,-12,15,-14,15,-11,15,15,15,15,-27,-35,]),'SHOW':([0,2,3,4,5,6,7,8,9,10,17,21,22,23,28,30,41,44,49,50,51,52,53,57,60,61,62,63,64,69,71,72,75,79,86,87,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,16,16,16,-19,-20,-22,-23,-26,16,70,-12,16,-14,16,-11,16,16,16,16,-27,-35,]),'$end':([1,2,3,4,5,6,7,8,9,10,17,21,22,23,28,44,49,50,51,52,53,57,61,63,69,71,72,86,87,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,-40,-19,-20,-22,-23,-26,-30,-12,-14,-11,-13,-29,-27,-35,]),'ELSE':([3,4,5,6,7,8,9,10,17,21,22,23,28,44,49,50,51,52,53,57,61,63,69,71,72,86,87,],[-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,62,-19,-20,-22,-23,-26,-30,-12,-14,-11,-13,-29,-27,-35,]),'RBRACE':([3,4,5,6,7,8,9,10,17,21,22,23,28,44,49,50,51,52,53,57,61,63,69,71,72,79,81,83,85,86,87,88,],[-3,-4,-5,-6,-7,-8,-9,-10,-2,-21,-24,-25,-28,-40,-19,-20,-22,-23,-26,-30,-12,-14,-11,-13,-29,81,-40,87,-39,-27,-35,-38,]),'IDENTIFIER':([11,13,15,42,68,70,],[18,25,27,58,76,77,]),'NUMBER':([12,14,16,24,31,32,33,34,35,36,37,38,55,60,74,84,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'LPAREN':([12,14,16,24,27,31,32,33,34,35,36,37,38,55,60,74,77,84,],[24,24,24,24,42,24,24,24,24,24,24,24,24,24,24,24,80,24,]),'BE':([18,],[29,]),'THEN':([19,21,22,23,45,46,47,48,49,50,51,52,53,],[30,-21,-24,-25,-15,-16,-17,-18,-19,-20,-22,-23,-26,]),'IS_LESS_THAN':([20,21,22,23,49,50,51,52,53,],[31,-21,-24,-25,-19,-20,-22,-23,-26,]),'IS_EQUAL_TO':([20,21,22,23,49,50,51,52,53,],[32,-21,-24,-25,-19,-20,-22,-23,-26,]),'IS_GREATER_THAN':([20,21,22,23,49,50,51,52,53,],[33,-21,-24,-25,-19,-20,-22,-23,-26,]),'IS_NOT_EQUAL_TO':([20,21,22,23,49,50,51,52,53,],[34,-21,-24,-25,-19,-20,-22,-23,-26,]),'PLUS':([20,21,22,23,28,39,45,46,47,48,49,50,51,52,53,66,69,78,88,],[35,-21,-24,-25,35,35,35,35,35,35,-19,-20,-22,-23,-26,35,35,35,35,]),'MINUS':([20,21,22,23,28,39,45,46,47,48,49,50,51,52,53,66,69,78,88,],[36,-21,-24,-25,36,36,36,36,36,36,-19,-20,-22,-23,-26,36,36,36,36,]),'RPAREN':([21,22,23,39,49,50,51,52,53,58,59,76,82,],[-21,-24,-25,53,-19,-20,-22,-23,-26,-36,67,-37,86,]),'DO':([21,22,23,26,40,45,46,47,48,49,50,51,52,53,54,56,73,],[-21,-24,-25,41,-40,-15,-16,-17,-18,-19,-20,-22,-23,-26,64,-32,-31,]),'RBRACKET':([21,22,23,49,50,51,52,53,65,66,78,],[-21,-24,-25,-19,-20,-22,-23,-26,73,-33,-34,]),'COMMA':([21,22,23,49,50,51,52,53,58,59,65,66,76,78,],[-21,-24,-25,-19,-20,-22,-23,-26,-36,68,74,-33,-37,-34,]),'TIMES':([21,22,23,49,50,51,52,53,],[37,-24,-25,37,37,-22,-23,-26,]),'DIVIDE':([21,22,23,49,50,51,52,53,],[38,-24,-25,38,38,-22,-23,-26,]),'IN':([25,],[40,]),'EQUAL':([29,],[43,]),'LBRACKET':([40,],[55,]),'TO':([43,],[60,]),'LBRACE':([67,],[75,]),'STRING_LITERAL':([80,],[82,]),'RETURN':([81,],[84,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,30,41,62,64,75,],[2,44,57,71,72,79,]),'statement':([0,2,30,41,44,57,62,64,71,72,75,79,],[3,17,3,3,17,17,3,3,17,17,3,17,]),'assignment':([0,2,30,41,44,57,62,64,71,72,75,79,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'conditional':([0,2,30,41,44,57,62,64,71,72,75,79,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'loop':([0,2,30,41,44,57,62,64,71,72,75,79,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'function':([0,2,30,41,44,57,62,64,71,72,75,79,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'display':([0,2,30,41,44,57,62,64,71,72,75,79,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'input':([0,2,30,41,44,57,62,64,71,72,75,79,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'condition':([12,14,],[19,26,]),'expression':([12,14,16,24,31,32,33,34,55,60,74,84,],[20,20,28,39,45,46,47,48,66,69,78,88,]),'term':([12,14,16,24,31,32,33,34,35,36,55,60,74,84,],[21,21,21,21,21,21,21,21,49,50,21,21,21,21,]),'factor':([12,14,16,24,31,32,33,34,35,36,37,38,55,60,74,84,],[22,22,22,22,22,22,22,22,22,22,51,52,22,22,22,22,]),'list':([40,],[54,]),'empty':([40,44,81,],[56,63,85,]),'parameters':([42,],[59,]),'else_statements_opt':([44,],[61,]),'expression_list':([55,],[65,]),'return_statement_opt':([81,],[83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','yacc.py',15),
  ('statements -> statements statement','statements',2,'p_statements','yacc.py',19),
  ('statements -> statement','statements',1,'p_statements','yacc.py',20),
  ('statement -> assignment','statement',1,'p_statement','yacc.py',24),
  ('statement -> conditional','statement',1,'p_statement','yacc.py',25),
  ('statement -> loop','statement',1,'p_statement','yacc.py',26),
  ('statement -> function','statement',1,'p_statement','yacc.py',27),
  ('statement -> display','statement',1,'p_statement','yacc.py',28),
  ('statement -> input','statement',1,'p_statement','yacc.py',29),
  ('statement -> COMMENT','statement',1,'p_statement','yacc.py',30),
  ('assignment -> LET IDENTIFIER BE EQUAL TO expression','assignment',6,'p_assignment','yacc.py',34),
  ('conditional -> IF condition THEN statements else_statements_opt','conditional',5,'p_conditional','yacc.py',38),
  ('else_statements_opt -> ELSE statements','else_statements_opt',2,'p_else_statements_opt','yacc.py',42),
  ('else_statements_opt -> empty','else_statements_opt',1,'p_else_statements_opt','yacc.py',43),
  ('condition -> expression IS_LESS_THAN expression','condition',3,'p_condition','yacc.py',47),
  ('condition -> expression IS_EQUAL_TO expression','condition',3,'p_condition','yacc.py',48),
  ('condition -> expression IS_GREATER_THAN expression','condition',3,'p_condition','yacc.py',49),
  ('condition -> expression IS_NOT_EQUAL_TO expression','condition',3,'p_condition','yacc.py',50),
  ('expression -> expression PLUS term','expression',3,'p_expression','yacc.py',54),
  ('expression -> expression MINUS term','expression',3,'p_expression','yacc.py',55),
  ('expression -> term','expression',1,'p_expression','yacc.py',56),
  ('term -> term TIMES factor','term',3,'p_term','yacc.py',66),
  ('term -> term DIVIDE factor','term',3,'p_term','yacc.py',67),
  ('term -> factor','term',1,'p_term','yacc.py',68),
  ('factor -> NUMBER','factor',1,'p_factor','yacc.py',78),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','yacc.py',79),
  ('input -> LET IDENTIFIER BE EQUAL TO SHOW IDENTIFIER LPAREN STRING_LITERAL RPAREN','input',10,'p_input','yacc.py',86),
  ('display -> SHOW expression','display',2,'p_display','yacc.py',90),
  ('loop -> FOR IDENTIFIER IN list DO statements','loop',6,'p_loop','yacc.py',94),
  ('loop -> WHILE condition DO statements','loop',4,'p_loop','yacc.py',95),
  ('list -> LBRACKET expression_list RBRACKET','list',3,'p_list','yacc.py',99),
  ('list -> empty','list',1,'p_list','yacc.py',100),
  ('expression_list -> expression','expression_list',1,'p_expression_list','yacc.py',104),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','yacc.py',105),
  ('function -> FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE return_statement_opt RBRACE','function',10,'p_function','yacc.py',109),
  ('parameters -> IDENTIFIER','parameters',1,'p_parameters','yacc.py',113),
  ('parameters -> parameters COMMA IDENTIFIER','parameters',3,'p_parameters','yacc.py',114),
  ('return_statement_opt -> RETURN expression','return_statement_opt',2,'p_return_statement_opt','yacc.py',118),
  ('return_statement_opt -> empty','return_statement_opt',1,'p_return_statement_opt','yacc.py',119),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',123),
]