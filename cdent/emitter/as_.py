"""\
ActionScript code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'as'
    LINE_COMMENT_PREFIX = '// '
    BLOCK_COMMENT_BEGIN = '/**\n'
    BLOCK_COMMENT_PREFIX = ' * '
    BLOCK_COMMENT_END = ' */\n'

    def emit_module(self, module):
        self.writeln('package {')
        self.emit(module.has, indent=True)
        self.writeln('}')

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('public class %s {' % name)
        self.emit(class_.has, indent=True)
        self.writeln('}')

    def emit_method(self, method): 
        name = method.name
        self.writeln('public function %s():void {' % name)
        self.emit(method.has, indent=True)
        self.writeln('}')

    def emit_println(self, println): 
        self.write('trace(', indent=True)
        self.emit(println.args)
        self.write(' + "\\n"')
        self.writeln(');', indent=False)
