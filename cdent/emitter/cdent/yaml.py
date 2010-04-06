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

from cdent.ast import *
import cdent.emitter

class Emitter(cdent.emitter.Emitter):
    def emit_ast(self, ast):
        tags = {'!': 'tag:cdent.org,2010:'}
        self.output.write(yaml.dump(ast, default_flow_style=False, tags=tags))

    def representer(dumper, data):
        return dumper.represent_mapping(data.yaml_tag, data.__dict__)
    Dumper.add_multi_representer(ASTBase, representer)
