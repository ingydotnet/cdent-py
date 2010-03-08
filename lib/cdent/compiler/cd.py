"""\
C'Dent compiler for already compiled AST
"""

import cdent.ast

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

class Compiler():
    def __init__(self, path):
        self.path = path

    def compile(self):
        stream = file(self.path, 'r')
        ast = load(stream)
        return ast

    def multi_constructor(loader, type, node):
        map = loader.construct_mapping(node)
        obj = getattr(cdent.ast, 'ast_' + type)()
        for k in map.keys():
            setattr(obj, k, map[k])
        return obj

    Loader.add_multi_constructor('tag:cdent.org,2010:', multi_constructor)
