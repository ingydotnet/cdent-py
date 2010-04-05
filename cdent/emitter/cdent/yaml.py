"""\
YAML emitter for C'Dent
"""

from __future__ import absolute_import

import yaml

from cdent.emitter import Emitter as Base

class Emitter(Base):
    def emit_ast(self, ast):
        self.output.write(yaml.dump(ast, default_flow_style=False))
