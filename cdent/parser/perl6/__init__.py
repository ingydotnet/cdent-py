"""\
C'Dent Perl 6 parser
"""

from cdent.parser import Parser as Base
from cdent.parser import ParseError

from cdent.parser.perl6.grammar import Grammar

class Parser(Base):
    grammar = Grammar()

    def __init__(self):
        Base.__init__(self)
