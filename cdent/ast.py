"""\
Abstact Syntax Tree classes for C'Dent
"""

import yaml

class Base():
    def __repr__(self):
        return yaml.dump(self, default_flow_style=False)

class Container(Base):
    def __init__(self, has=None):
        self.has = has if has else []

class AST(Container): pass
class Module(Container): pass
class Comment(Base): pass
class IncludeCDent(Base): pass
class Class(Container): pass
class Method(Container): pass
class Println(Base): pass
class Return(Base): pass
class String(Base): pass
