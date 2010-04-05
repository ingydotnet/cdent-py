"""\
JavaScript code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'js'
    LINE_COMMENT_PREFIX = '// '
    BLOCK_COMMENT_BEGIN = '/*\n'
    BLOCK_COMMENT_PREFIX = ' * '
    BLOCK_COMMENT_END = ' */\n'

    def emit_includecdent(self, includecdent): 
        self.writeln("load('cdent/run.js');")

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('(this.%s = function() {}).prototype = {' % name)
        self.emit(class_.has, indent=True)
        self.writeln('}')

    def emit_method(self, method): 
        name = method.name
        self.writeln(name + ': function() {')
        self.emit(method.has, indent=True)
        self.writeln('}')

    def emit_println(self, println): 
        self.write('print(', indent=True)
        self.emit(println.args)
        self.writeln(');', indent=False)

    def emit_return(self, ret): 
        self.writeln('return;')
