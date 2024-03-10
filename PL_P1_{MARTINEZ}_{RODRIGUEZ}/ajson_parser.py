import ply.yacc as yacc
from ajson_lexer import lexerAJSON


import ply.yacc as yacc

class parserAJSON:
    def __init__(self):
        # Diccionario para almacenar los pares clave/valor
        self.ajson_data = {}
        # Inicializar el parser aquí si es necesario, p.ej., self.parser = yacc.yacc(module=self)

    # Función para manejar las claves anidadas
    def handle_nested_key(self, key, value):
        keys = key.split('.')
        current_dict = self.ajson_data
        for k in keys[:-1]:
            if k not in current_dict:
                current_dict[k] = {}
            current_dict = current_dict[k]
        current_dict[keys[-1]] = value

    # Definiciones de producción del parser
    def p_start(self, p):
        '''
        start : object
              | empty
        '''
        p[0] = p[1]

    def p_object(self, p):
        '''
        object : LLAVE_APERTURA pairs LLAVE_CIERRE
               | LLAVE_APERTURA LLAVE_CIERRE
        '''
        if len(p) == 4:
            p[0] = p[2]
        else:
            p[0] = {}

    def p_pairs(self, p):
        '''
        pairs : pair
              | pair COMA pairs
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = {**p[1], **p[3]}

    def p_pair(self, p):
        '''
        pair : STRING_WITH_QUOTES DOS_PUNTOS value
             | STRING_WITHOUT_QUOTES DOS_PUNTOS value
        '''
        p[0] = {p[1]: p[3]}

    def p_value(self, p):
        '''
        value : STRING_WITH_QUOTES
              | number
              | boolean
              | null
              | object
              | comparison_operation
        '''
        p[0] = p[1]

    def p_boolean(self, p):
        '''
        boolean : TRUE
                | FALSE
        '''
        p[0] = True if p[1] == 'TRUE' else False

    def p_null(self, p):
        '''
        null : NULL
        '''
        p[0] = None

    def p_number(self, p):
        '''
        number : INTEGER
                | REAL
                | SCIENTIFIC
                | BINARY
                | OCTAL
                | HEXNUM
        '''
        p[0] = p[1]

    def p_comparison_operation(self, p):
        '''
        comparison_operation : number comparison_operator number
        '''
        p[0] = "{} {} {}".format(p[1], p[2], p[3])

    def p_comparison_operator(self, p):
        '''
        comparison_operator : IGUAL
                            | MAYOR
                            | MAYOR_IGUAL
                            | MENOR
                            | MENOR_IGUAL
        '''
        p[0] = p[1]

    def p_empty(self, p):
        '''
        empty :
        '''
        p[0] = {}

    def p_error(self, p):
        print("Error de sintaxis en la entrada:", p)

    def test(self, data):
        # Asegúrate de tener una instancia de parser aquí, algo como self.parser.parse(data)
        pass

    def test_with_file(self, path):
        file = open(path)
        content = file.read()
        file.close()
        self.test(content)
