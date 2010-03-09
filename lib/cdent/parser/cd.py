"""\
C'Dent parser for already compiled AST
"""

from cdent.parser import Parser as Base
import cdent.ast

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

class Parser(Base):
    def parse_module(self):
        ast = load(self.input)
        return ast

    def multi_constructor(loader, type, node):
        map = loader.construct_mapping(node)
        obj = getattr(cdent.ast, 'ast_' + type)()
        for k in map.keys():
            setattr(obj, k, map[k])
        return obj

    Loader.add_multi_constructor('tag:cdent.org,2010:', multi_constructor)
