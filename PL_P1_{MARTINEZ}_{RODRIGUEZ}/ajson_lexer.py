import ply.lex as lex

# Definición de tokens
tokens = (
    'INTEGER',
    'FLOAT',
    'BINARY',
    'OCTAL',
    'HEXADECIMAL',
    'REAL',
    'SCIENTIFIC_NOTATION'
)


# Expresiones regulares para tokens
def t_INTEGER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'-?(\d+\.\d*|\.\d+)'
    t.value = float(t.value)
    return t

def t_BINARY(t):
    r'-?0[bB][01]+'
    t.value = int(t.value, 2)
    return t

def t_OCTAL(t):
    r'-?0[oO]?[0-7]+'
    t.value = int(t.value, 8)
    return t

def t_HEXADECIMAL(t):
    r'\b0[xX][0-9a-fA-F]+\b'
    t.value = int(t.value, 16)
    return t

def t_REAL(t):
    r'-?\d+(\.\d*|\.\d+|\d+\.)([eE][-+]?\d+)?'
    t.value = float(t.value)
    return t

def t_SCIENTIFIC_NOTATION(t):
    r'-?\d+(\.\d*|\.\d+|\d+\.)([eE][-+]?\d+)'
    t.value = float(t.value)
    return t


# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Función de prueba
def test_lexer(input_string):
    lexer.input(input_string)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.type, tok.value)

# Prueba del reconocedor léxico
if __name__ == '__main__':
    test_lexer("0xFED123 ")
