import ply.lex as lex
import sys
#EJERCICIO 5 - TIPOS DE NUMEROS



tokens = (
    'INTEGER',
    'FLOAT',
    'NUMBER'
)

# 1 - Token integer

def t_INTEGER(token):
    r'\d+'
    token.value = int(token.value)
    return token

# 2 - Token float
def t_FLOAT(token):
    r'\d*\.\d+'
    token.value = float(token.value)
    return token

# 3 - Token number
"""
def t_NUMBER(token):
    r'\d*\.\d+|\d+'
    if '.' in token.value:
        token.value = float(token.value)
    else:
        token.value = int(token.value)
    return token
"""


# COMENTAR 1 y 2 O 3, SON DOS MANERAS DISTINTAS

# 4 - Probar a cambiar orden

# 5 - Otro tipo de numeros




t_ignore = ' \t'

def t_newline(token):
    r'\n+'
    print("New line", token.lexer.lineno)
    token.lexer.lineno = token.value.count('\n')


def t_error(token):
    print("[Lexer] Illegal character", token.value)
    token.lexer.skip(1)



#Construir lexer
lexer = lex.lex()

"""
#Ejecutar el lexer con una variable string
lexer.input("3.5")
for token in lexer:
    print(token.type, token.value)
"""

# Utilizar un fichero en lugar de variable
file = open(sys.argv[1])
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)