import sys
import ply.lex as lex

class lexerAJSON:
    # Lista de palabras reservadas

    def __init__(self) -> None:
        self.lexer = lex.lex(module=self)
        self.reserved = (
        "tr",
        "fl",
        "NULL",)
        
    reserved = {
        'tr': 'TRUE',
        'fl': 'FALSE',
        'null': 'NULL',
    }

    # Lista de nombres de tokens
    tokens = [
        'INTEGER', 'REAL', 'SCIENTIFIC', 'BINARY', 'OCTAL', 'HEXNUM',
        'STRING_WITH_QUOTES', 'STRING_WITHOUT_QUOTES', 'IGUAL', 'MAYOR',
        'MAYOR_IGUAL', 'MENOR', 'MENOR_IGUAL', 'LLAVE_APERTURA', 'LLAVE_CIERRE', 'DOS_PUNTOS',
        'COMA',
    ] + list(reserved.values())

    def create_reserved_map(self):
        reserved_map = {}
        for r in self.reserved:
            reserved_map[r.lower()] = r
            reserved_map[r.upper()] = r
        return reserved_map



    # Reglas de expresiones regulares para tokens simples
    t_REAL = r'[+-]?\b\d+\.\d+\b|\b\d+\.\b'
    t_INTEGER = r'[+-]?\b\d+\b'
    t_SCIENTIFIC = r'[+-]?\b\d*\.?\d+(e|E)[+-]?\d+\b'
    t_BINARY = r'\b0[bB][01]+\b'
    t_OCTAL = r'\b0[0-7]+\b'
    t_HEXNUM = r'\b0[xX][0-9a-fA-F]+\b'
    t_STRING_WITH_QUOTES = r'\".*?\"'
    t_IGUAL = r'=='
    t_MAYOR_IGUAL = r'>='
    t_MENOR_IGUAL = r'<='
    t_MAYOR = r'>'
    t_MENOR = r'<'
    t_LLAVE_APERTURA = r'\{'
    t_LLAVE_CIERRE = r'\}'
    t_DOS_PUNTOS = r':'
    t_COMA = r','

    # Reglas para identificadores y palabras reservadas
    def t_STRING_WITHOUT_QUOTES(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.value = t.value.lower()  # Normalize to lowercase
        t.type = lexerAJSON.reserved.get(t.value, 'STRING_WITHOUT_QUOTES')  # Check for reserved words
        return t

    # Regla de seguimiento de números de línea
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Caracteres ignorados (espacios y tabulaciones)
    t_ignore = ' \t'

    # Manejo de errores
    def t_error(self, t):
        print(f"Carácter ilegal '{t.value[0]}'")
        t.lexer.skip(1)


    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)

    def test_with_file(self, path):
        file = open(path)
        content = file.read()
        self.test(content)


