"""\
Abstact Syntax Tree classes for C'Dent
"""

import yaml

class Base():
    def __repr__(self):
        return yaml.dump(self)

class AST(Base): pass
class Module(Base): pass
class Comment(Base): pass
class IncludeCDent(Base): pass
class Class(Base): pass
class Method(Base): pass
class Println(Base): pass
class Return(Base): pass
class String(Base): pass
