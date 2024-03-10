
import sys
from ajson_lexer import lexerAJSON
from ajson_parser import parserAJSON


lexer = lexerAJSON()

lexer.test_with_file("./test1.ajson")

p = parserAJSON()

p.test_with_file("./test1.ajson")