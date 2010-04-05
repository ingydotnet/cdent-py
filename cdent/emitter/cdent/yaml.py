"""\
YAML emitter for C'Dent
"""

from __future__ import absolute_import

import yaml

from yaml import load
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

import cdent.ast
from cdent.emitter import Emitter as Base

class Emitter(Base):
    def emit_ast(self, ast):
        tags = {'!': 'tag:cdent.org,2010:'}
        self.output.write(yaml.dump(ast, default_flow_style=False, tags=tags))

    def multi_representer(dumper, data):
        pass

    Dumper.add_multi_representer(AST, multi_representer)
