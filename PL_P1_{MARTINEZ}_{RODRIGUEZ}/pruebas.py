import ply.lex as lex

# Lista de palabras reservadas 
reserved = {
    'TR': 'TRUE',
    'FL' : 'FALSE',
    'NULL': 'NONE'
}


# Lista de nombres de tokens
tokens = [
    'INTEGER', 'REAL', 'SCIENTIFIC', 'BINARY', 'OCTAL', 'HEXNUM',
    'STRING_WITH_QUOTES', 'STRING_WITHOUT_QUOTES','IGUAL', 'MAYOR',
    'MAYOR_IGUAL', 'MENOR', 'MENOR_IGUAL', 'LLAVE_APERTURA', 'LLAVE_CIERRE', 'DOS_PUNTOS',
    'COMA' ,'ID', 
    
] + list(reserved.values())

# Reglas de expresiones regulares para tokens simples
def t_REAL(t):
    r'[+-]?\b\d+\.\d+\b|\b\d+\.\b'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'[+-]?\b\d+\b'
    t.value = int(t.value)
    return t

def t_SCIENTIFIC(t):
    r'[+-]?\b\d*\.?\d+(e|E)[+-]?\d+\b'
    t.value = float(t.value)
    return t

def t_BINARY(t):
    r'\b0[bB][01]+\b'
    t.value = int(t.value, 2)
    return t

def t_OCTAL(t):
    r'\b0[0-7]+\b'
    t.value = int(t.value, 8)
    return t

def t_HEXNUM(t):
    r'\b0[xX][0-9a-fA-F]+\b'
    t.value = int(t.value, 16)
    return t

# Regla para cadenas de caracteres entre comillas
def t_STRING_WITH_QUOTES(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Quita las comillas del principio y del final
    return t



# Regla para cadenas de caracteres sin comillas
def t_STRING_WITHOUT_QUOTES(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reserved:
        t.type = reserved[t.value.upper()]
    return t
    
# Regla para caráteres de comparación 

def t_IGUAL(t):
    r'=='
    return t

def t_MAYOR_IGUAL(t):
    r'>='
    return t

def t_MENOR_IGUAL(t):
    r'<='
    return t

def t_MAYOR(t):
    r'>'
    return t

def t_MENOR(t):
    r'<'
    return t


# Regla para caráteres delimitadores
def t_LLAVE_APERTURA(t):
    r'\{'
    return t

def t_LLAVE_CIERRE(t):
    r'\}'
    return t

def t_DOS_PUNTOS(t):
    r':'
    return t

def t_COMA(t):
    r','
    return t 

# Expresiones regulares para palabras reservadas

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reserved:
        t.type = reserved[t.value.upper()]
    return t

def t_TRUE(t):
    r'TRUE|True|true'
    return t

def t_FALSE(t):
    r'FALSE|False|false'
    return t

def t_NULO(t):
    r'NONE|none'
    return t

# Regla de seguimiento de números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# Caracteres ignorados (espacios y tabulaciones)
t_ignore  = ' \t'

# Manejo de errores
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba de entrada
data = '''
10
420
-12
-999
0.1289
12
-100.001
10e-1
1E10
5E2
4e-2
0b101
0B110110
0712
0332
01121
0XFED123
0xAA
0X1
0x00F1
"Hello, World!"
identifier

TR
Fl
tr
fl
NULL

x >= y == z < 10

{x: 10, y: 20}
"{x: 10, y: 20}" 

'''

# Dar los datos al lexer
lexer.input(data)

# Tokenize
for tok in lexer:
    print(tok)
