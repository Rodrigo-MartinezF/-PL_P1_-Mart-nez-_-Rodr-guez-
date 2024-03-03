import ply.lex as lex

# Lista de tokens
tokens = [
    'INTEGER',
    'FLOAT',
    'SCIENTIFIC',
    'BINARY',
    'OCTAL',
    'HEX',
    'ID_NO_QUOTES',
    'STRING_WITH_QUOTES',
    'BOOLEAN',
    'NULL',
    'EQUALS',
    'GREATER',
    'GREATER_EQUAL',
    'LESS',
    'LESS_EQUAL',
    'LBRACE',
    'RBRACE',
    'COLON',
    'COMMA',
]

# Expresiones regulares para los tokens
t_INTEGER = r'-?\d+'
t_FLOAT = r'-?\d+\.\d+'
t_SCIENTIFIC = r'-?\d+[eE]-?\d+'
t_BINARY = r'0[bB][01]+'
t_OCTAL = r'0o[0-7]+'
t_HEX = r'0x[0-9a-fA-F]+'

def t_ID_NO_QUOTES(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING_WITH_QUOTES(t):
    r'"([^"\n]*)?"'
    return t

def t_BOOLEAN(t):
    r'TRUE|FALSE|true|false'
    return t

def t_NULL(t):
    r'NULL|null'
    return t

t_EQUALS = r'=='
t_GREATER = r'>'
t_GREATER_EQUAL = r'>='
t_LESS = r'<'
t_LESS_EQUAL = r'<='

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','

# Ignorar espacios en blanco y tabuladores
t_ignore = ' \t'

# Expresión para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Ejemplo de uso
data = """
10 420 -12 -999
0.1289 .12 -100.001
10e-1 .1E10 5E2 4e-2
0b101 0B110110
0712 0332 01121
0XFED123 0xAA 0X1 0x00F1
identifier1 _identifier2
"string without quotes" "string with \"quotes\""
TRUE True true
FALSE False false
NULL null
== > >= < <=
{ } : ,
"""

lexer.input(data)

# Obtener y mostrar los tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)