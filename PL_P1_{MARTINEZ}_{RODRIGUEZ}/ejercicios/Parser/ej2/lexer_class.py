# Usando clases para lexer y parser
import sys
import ply.lex as lex

class LexerClass:
    tokens = ('NUMBER',)
    literals = ('+', '-')



    def __init__(self) -> None:  # Fallo aqui
        self.lexer = lex.lex(module = self)

    def t_NUMBER(self, t):
        r'[1-9][0-9]*'
        t.value = int(t.value)
        return t
    
    t_ignore = r' \t'


    def t_NEW_LINE(self, t):
        r'\n+'
        t.value = t.value.count('\n')
        t.lexer.lineno += t.value.count('\n')
        return t

    def t_NEW_LINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)

    def test_with_file(self, path):
        file = open(path)
        content = file.readLines()
        for line in content:
            self.test(line)
