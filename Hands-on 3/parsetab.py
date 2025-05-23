
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTnonassocLTLEGTGEEQNEleftPLUSMINUSleftTIMESDIVIDErightUMINUSAND BOOLEAN DIVIDE EQ GE GT LE LPAREN LT MINUS NE NOT NUMBER OR PLUS RPAREN TIMESexpression : LPAREN expression RPARENexpression : NUMBERexpression : BOOLEANexpression : expression PLUS expression\n                 | expression MINUS expression\n                 | expression TIMES expression\n                 | expression DIVIDE expressionexpression : expression GT expression\n                 | expression LT expression\n                 | expression GE expression\n                 | expression LE expression\n                 | expression EQ expression\n                 | expression NE expressionexpression : expression AND expression\n                 | expression OR expression\n                 | NOT expressionexpression : MINUS expression %prec UMINUS'
    
_lr_action_items = {'LPAREN':([0,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'NUMBER':([0,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'BOOLEAN':([0,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'NOT':([0,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[5,8,5,-2,-3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,8,-17,8,-4,-5,-6,-7,8,8,8,8,8,8,8,8,-1,]),'$end':([1,3,4,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[0,-2,-3,-17,-16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,]),'PLUS':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[7,-2,-3,7,-17,7,-4,-5,-6,-7,7,7,7,7,7,7,7,7,-1,]),'TIMES':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[9,-2,-3,9,-17,9,9,9,-6,-7,9,9,9,9,9,9,9,9,-1,]),'DIVIDE':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[10,-2,-3,10,-17,10,10,10,-6,-7,10,10,10,10,10,10,10,10,-1,]),'GT':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[11,-2,-3,11,-17,11,-4,-5,-6,-7,None,None,None,None,None,None,11,11,-1,]),'LT':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[12,-2,-3,12,-17,12,-4,-5,-6,-7,None,None,None,None,None,None,12,12,-1,]),'GE':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[13,-2,-3,13,-17,13,-4,-5,-6,-7,None,None,None,None,None,None,13,13,-1,]),'LE':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[14,-2,-3,14,-17,14,-4,-5,-6,-7,None,None,None,None,None,None,14,14,-1,]),'EQ':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[15,-2,-3,15,-17,15,-4,-5,-6,-7,None,None,None,None,None,None,15,15,-1,]),'NE':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[16,-2,-3,16,-17,16,-4,-5,-6,-7,None,None,None,None,None,None,16,16,-1,]),'AND':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[17,-2,-3,17,-17,-16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,17,-1,]),'OR':([1,3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[18,-2,-3,18,-17,-16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,]),'RPAREN':([3,4,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[-2,-3,34,-17,-16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[1,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',16),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',20),
  ('expression -> BOOLEAN','expression',1,'p_expression_boolean','parser.py',24),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',28),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',29),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',30),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',31),
  ('expression -> expression GT expression','expression',3,'p_expression_compare','parser.py',35),
  ('expression -> expression LT expression','expression',3,'p_expression_compare','parser.py',36),
  ('expression -> expression GE expression','expression',3,'p_expression_compare','parser.py',37),
  ('expression -> expression LE expression','expression',3,'p_expression_compare','parser.py',38),
  ('expression -> expression EQ expression','expression',3,'p_expression_compare','parser.py',39),
  ('expression -> expression NE expression','expression',3,'p_expression_compare','parser.py',40),
  ('expression -> expression AND expression','expression',3,'p_expression_logical','parser.py',44),
  ('expression -> expression OR expression','expression',3,'p_expression_logical','parser.py',45),
  ('expression -> NOT expression','expression',2,'p_expression_logical','parser.py',46),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',53),
]
