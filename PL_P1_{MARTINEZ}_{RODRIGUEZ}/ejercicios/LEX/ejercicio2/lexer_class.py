import ply.lex as lex

class lexerClass:
    def __init__(self):
        self.lexer = lex.lex(module=self)

tokens = (
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "EQUALS",
    "NUMBER"

)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='

def t_NUMBER(self,t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_NL(self, token):
    r'\n+'
    print("New line", token.lexer.lineno)
    token.lexer.lineno = token.value.count('\n')





