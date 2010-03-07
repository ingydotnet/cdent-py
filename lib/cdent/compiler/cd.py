"""
C'Dent compiler for already compiled AST
"""

from yaml import *
import cdent.ast

def multi_constructor(loader, type, node):
    mapping = loader.construct_mapping(node)
    object = getattr(cdent.ast, 'ast_' + type)()
    for k in mapping.keys():
        setattr(object, k, mapping[k])
    return object

Loader.add_multi_constructor('tag:cdent.org,2010:', multi_constructor)

class Compiler():
    def compile(self, path):
        stream = file(path, 'r')
        ast = load(stream)
        return ast
