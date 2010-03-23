"""\
C'Dent Python parser
"""

from cdent.parser import Parser as Base

from cdent.parser.python.grammar import Grammar

class Parser(Base):
    def __init__(self):
        self.grammar = Grammar()
