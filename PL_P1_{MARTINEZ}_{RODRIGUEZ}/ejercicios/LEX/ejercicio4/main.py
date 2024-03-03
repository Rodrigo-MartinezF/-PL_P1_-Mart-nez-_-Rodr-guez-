
import ply.lex as lex

#EJERCICIO 4 - Palabras reservadas

#1 Definir palabras reservadas
reserved = (
   'VAR', 'WHILE')
#2 Definir tokens, incluyendo palabras reservadas

tokens = reserved + (
    'LBRACKET',
    'RBRACKET',
    'ID',
    'NUMBER',
)


#3 Crear reserved map
reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r
    reserved_map[r.upper()] = r


#4 Usar reserved map en la definicion de t_ID

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_map.get(t.value,'ID')    # Check for reserved words
    return t


t_LBRACKET = r'\('
t_RBRACKET = r'\)'

def t_NUMBER(token):
    r'\d+'
    token.value = int(token.value)
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

#Ejecutar el lexer con una variable string
lexer.input("var")
for token in lexer:
    print(token.type, token.value)
