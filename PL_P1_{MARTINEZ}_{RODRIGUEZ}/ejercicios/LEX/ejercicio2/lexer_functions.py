import ply.lex as lex

def lexerFunction():

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

    def t_error(t):
        t.lexer.skip(1)

    def test(lexer, data):
        lexer.input(data)






