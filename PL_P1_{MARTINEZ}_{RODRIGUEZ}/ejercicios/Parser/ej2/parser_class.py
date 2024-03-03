from lexer_class import LexerClass
import ply.yacc as yacc

class ParserClass:
    def __init__(self):  # Fallo (mirar documentacion)
        self.parser = yacc.yacc(module=self)
        self.lexer = LexerClass().lexer

    tokens = LexerClass.tokens

    

    def p_program(self, p):
        ''' program : linea
                    | linea NEW_LINE program'''

    def p_linea(self, p):
        '''linea : plus
                 | minus '''
        
    def p_plus(self, p):
        ''' plus : NUMBER "+" NUMBER '''
        print(p[1], p[2], p[3])
    def p_minus(p):
        ''' minus : NUMBER "-" NUMBER '''

    def test(self, data):
        self.parser.parse(data)

    def test_with_file(self, path):
        file = open(path)
        content = file.read()
        self.test(content)