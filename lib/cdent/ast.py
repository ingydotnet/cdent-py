"""
Abstact Syntax Tree classes for C'Dent
"""


from yaml import load, dump
try:
    from yaml import CLoader as Loader
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class AST():
    def __init__():
        pass

class ast_module(): pass
class ast_comment(): pass
class ast_class(): pass
class ast_method(): pass
class ast_builtin(): pass
class ast_return(): pass
class ast_string(): pass
