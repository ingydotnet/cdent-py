import sys

sys.path.insert(0, '.')

from cdent.parser.python import Parser
from cdent.ast import *

code = """\
\"""
Foo module
\"""

class Foo():
    def greet():
        print "Hello, world"
"""

parser = Parser()
ast = parser.parse(code)

assert isinstance(ast, AST), "Got an AST object"
