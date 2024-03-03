import ply.lex as lex
import sys

# Definir token PALABRA y token NUMERO

tokens = (
    "PALABRA",
    "NUMERO"

)

#type, value, lineno, lexpos

t_PALABRA = r'[a-zA-Z][a-zA-Z0-9_]*'

def t_NUMERO(token):
    r'[1-9][0-9]*'
    token.vaule = int(token.value)
    return token

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
lexer.input("palabra variable_1 123 19")
for token in lexer:
    print(token.type, token.value)
"""


# Utilizar un fichero en lugar de variable
file = open(sys.argv[1])
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)


