"""\
C'Dent parser for already compiled AST
"""

from __future__ import absolute_import

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

import cdent.ast
from cdent.parser import Parser as Base
from cdent.parser import ParseError

class Parser(Base):
    def parse(self):
        return load(self.stream)

    def multi_constructor(loader, type, node):
        obj = getattr(cdent.ast, type)()
        obj.__dict__.update(loader.construct_mapping(node))
        return obj

    Loader.add_multi_constructor('tag:cdent.org,2010:', multi_constructor)
