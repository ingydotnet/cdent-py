"""\
Abstact Syntax Tree classes for C'Dent
"""

import yaml

class ASTBase():
    def __repr__(self):
        return yaml.dump(self, default_flow_style=False)

class ASTContainer(ASTBase):
    def __init__(self, has=None):
        self.has = has if has else []

class AST(ASTContainer):
    yaml_tag = '!AST'
class Module(ASTContainer):
    yaml_tag = '!Module'
class Comment(ASTBase):
    yaml_tag = '!Comment'
class IncludeCDent(ASTBase):
    yaml_tag = '!IncludeCDent'
class Class(ASTContainer):
    yaml_tag = '!Class'
class Method(ASTContainer):
    yaml_tag = '!Method'
class Println(ASTBase):
    yaml_tag = '!Println'
class Return(ASTBase):
    yaml_tag = '!Return'
class String(ASTBase):
    yaml_tag = '!String'

