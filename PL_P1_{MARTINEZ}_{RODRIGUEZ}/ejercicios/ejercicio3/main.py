#EJERCICIO 3 - COMENTARIOS

import ply.lex as lex
tokens = (
    "ONE_LINE_COMMENT",
    "MULTI_LINE_COMMNET",
    "NAME",
    "ASSIGN",
    "NUMER")

#1- Comentario de una linea
#t_ONE_LINE_COMMENT = r'\#([a-zA-Z0-9])*'

def t_ONE_LINE_COMMENT(token):
    r'\#.*'
    print("COMENTARIO 1 linea")
    token.lexer.skip(0)


t_MULTI_LINE_COMMNET = r'/\*\n*[a-zA-Z0-9]\n*/\*'




t_NAME = r'[a-zA-Z][a-zA-Z0-9_]*'
t_ASSIGN = r'='


def t_NUMBER(token):
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





#2a - Comentario multilinea completo
def t_ONE_LINE_COMMENT(token):
    r'\/\*(.|\n)*\*\/'
    print("COMENTARIO 1 linea")
    token.lexer.skip(0)


#2b - Comentario multilinea con estados
states = (
    ('commnet', 'exclusive')
)


def t_MULTI_LINE_COMMNET(token):
    r'\/\*'
    print("Comienzo")
    token.lexer.begin('comment')

def t_comment_MULTI_LINE_COMMNET(token):
    r'\*\/'
    print("Final")
    token.lexer.begin('comment')

def t_comment_content(token):
    r'[/\*]+'
    token.lexer.lineno +=






#Construir lexer
lexer = lex.lex()

#Ejecutar el lexer con una variable string
lexer.input("#Comentario")
for token in lexer:
    print(token.type, token.value)



#toknes = (
#   "ONE_LINE_COMMENT",
#   "MULTI_LINE_COMMNET",
#   "NAME",
#   "ASSIGN",
#   "NUMER")
#