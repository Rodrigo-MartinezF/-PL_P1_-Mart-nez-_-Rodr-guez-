

import ply.yacc as yacc
from ajson_lexer import tokens  # Importa los tokens del lexer

# Regla de inicio
def p_inicio(p):
    '''
    inicio : ajson
    '''

# Regla para el formato AJSON
def p_ajson(p):
    '''
    ajson : LLAVE_APERTURA pares_clave_valor LLAVE_CIERRE
          | empty
    '''

# Regla para pares clave/valor
def p_pares_clave_valor(p):
    '''
    pares_clave_valor : par_clave_valor
                      | par_clave_valor COMA pares_clave_valor
                      | empty
    '''

# Regla para un par clave/valor
def p_par_clave_valor(p):
    '''
    par_clave_valor : clave DOS_PUNTOS valor
    '''

# Regla para clave
def p_clave(p):
    '''
    clave : STRING_WITH_QUOTES
          | STRING_WITHOUT_QUOTES
    '''

# Regla para valor
def p_valor(p):
    '''
    valor : NUMERO
          | STRING_WITH_QUOTES
          | BOOLEANO
          | NULO
          | operacion_comparacion
          | ajson
    '''

# Regla para operación de comparación
def p_operacion_comparacion(p):
    '''
    operacion_comparacion : NUMERO IGUAL NUMERO
                          | NUMERO MAYOR NUMERO
                          | NUMERO MAYOR_IGUAL NUMERO
                          | NUMERO MENOR NUMERO
                          | NUMERO MENOR_IGUAL NUMERO
    '''

# Regla para valor booleano
def p_booleano(p):
    '''
    BOOLEANO : TRUE
             | FALSE
    '''

# Regla para un elemento vacío
def p_empty(p):
    '''
    empty :
    '''

# Regla para manejar errores de sintaxis
def p_error(p):
    if p:
        print("Error de sintaxis en el token '%s'" % p.value)
    else:
        print("Error de sintaxis al final de la entrada")

# Construir el parser
parser = yacc.yacc()

# Prueba del parser
data = '{ "nombre": "Juan", "edad": 30, "activo": true, "puntuacion": 9.5 }'
parser.parse(data)
