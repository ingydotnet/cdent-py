"""\
PHP code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'php'
    LINE_COMMENT_PREFIX = '// '
    BLOCK_COMMENT_BEGIN = '/**\n'
    BLOCK_COMMENT_PREFIX = ' * '
    BLOCK_COMMENT_END = ' */\n'

    def emit_includecdent(self, includecdent): 
        self.writeln('use CDent::Run;')

    def emit_module(self, module): 
        name = module.name
        self.writeln('<?php')
        self.emit(module.has, indent=False)
        self.writeln('?>')

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('class %s {' % name)
        self.emit(class_.has, indent=True)
        self.writeln('}')

    def emit_method(self, method): 
        name = method.name
        self.writeln('public function %s() {' % name)
        self.emit(method.has, indent=True)
        self.writeln('}')

    def emit_println(self, println): 
        self.write('print(', indent=True)
        self.emit(println.args)
        self.writeln(', "\\n");', indent=False)

    def emit_return(self, ret): 
        self.writeln('return;')
