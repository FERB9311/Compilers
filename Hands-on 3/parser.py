import ply.yacc as yacc
from lexer import tokens, lexer

# Precedencia de operadores (de menor a mayor precedencia)
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),  # Operadores de comparación
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_boolean(p):
    'expression : BOOLEAN'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                 | expression MINUS expression
                 | expression TIMES expression
                 | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_compare(p):
    '''expression : expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression EQ expression
                 | expression NE expression'''
    p[0] = ('compare', p[2], p[1], p[3])

def p_expression_logical(p):
    '''expression : expression AND expression
                 | expression OR expression
                 | NOT expression'''
    if len(p) == 4:
        p[0] = ('logical', p[2], p[1], p[3])
    else:
        p[0] = ('logical', p[1], p[2])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = ('uminus', p[2])

def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}' (posición {p.lexpos})")
    else:
        raise SyntaxError("Expresión incompleta")

parser = yacc.yacc()

def validate_expression(input_str):
    lexer.input(input_str)
    try:
        # Primero verificar tokens
        for tok in lexer:
            pass
        
        # Luego parsear
        parser.parse(input_str, lexer=lexer, tracking=True)
        print("✅ Expresión válida:", input_str)
        return True
    except SyntaxError as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"⚠ Error inesperado: {type(e).__name__} - {e}")
        return False

if __name__ == "__main__":
    print("Validador de expresiones (aritméticas, lógicas y comparaciones)")
    print("Operadores permitidos: + - * / AND OR NOT > < >= <= == !=")
    print("Ejemplos válidos:")
    print("  (5 > 3) AND (2 * 3 == 6)")
    print("  NOT (1 + 2 < 2) OR False")
    
    while True:
        try:
            expr = input("\nIngrese expresión (o 'salir'): ").strip()
            if expr.lower() in ('exit', 'salir', 'quit'):
                break
            if not expr:
                continue
                
            validate_expression(expr)
            
        except KeyboardInterrupt:
            print("\nPrograma terminado")
            break