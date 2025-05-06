import ply.lex as lex

tokens = (
    'NUMBER', 'BOOLEAN',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'AND', 'OR', 'NOT',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'  # Operadores de comparación
)

# Operadores lógicos
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'

# Operadores aritméticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Operadores de comparación
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'True|False|0|1'
    t.value = True if t.value in ('True', '1') else False
    return t

t_ignore = ' \t'

def t_error(t):
    raise SyntaxError(f"Carácter ilegal '{t.value[0]}' en posición {t.lexpos}")

lexer = lex.lex()