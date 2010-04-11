"""\
C'Dent JavaScript parser
"""

from cdent.parser import Parser as Base
from cdent.parser import ParseError

from cdent.parser.javascript.grammar import Grammar

class Parser(Base):
    grammar = Grammar()

    def __init__(self):
        Base.__init__(self)
