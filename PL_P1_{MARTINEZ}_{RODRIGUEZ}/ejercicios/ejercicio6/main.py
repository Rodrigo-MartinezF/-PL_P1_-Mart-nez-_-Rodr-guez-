# FICHA CIUDADANO

import ply.lex as lex
import sys

tokens = (
    'NOMBRE_APELLIDOS',
    'DNI',
    'EMAIL',
    'CIUDAD_PAIS',
    'TELEFONO',
    'MATRICULA'


)

t_NOMBRE_APELLIDOS = r'([a-zA-Z]+ ){2}([a-zA-Z]+)'
def t_DNI(token):
    r'\d{8}[A-Z]'
    print("DNI:", token.value)
    return token
