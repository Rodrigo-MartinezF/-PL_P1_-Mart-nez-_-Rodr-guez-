import sys
import ply.lex as lex
import ply.yacc as yacc

literals  = ('=', ';')
tokens = ('ID', 'NUMBER')

t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'[1-9][0-9]*'
    t.value = int(t.value)
    return t


t_ignore = ' \t'
def t_error(t):
    print("[Lex Error]", t.value)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    

lexer = lex.lex()

# ANALISIS 

# AXIOMA
def p_program(p):
    '''program : assign ";"
               | assign ";" program'''
   
    if len(p) == 3: p[0] = [p[1]]
    else: p[0] = p[3] + [p[1]]
    print(p[0])



def p_assign(p):
    '''assign : ID "=" NUMBER'''
    p[0] = p[1] + p[2] + str(p[3])

def p_error(p):
    if p: print("error with", p.value)
    else: print("error: EOF")

parser = yacc.yacc()
file = open(sys.argv[1])
content = file.read()
parser.parse(content)


