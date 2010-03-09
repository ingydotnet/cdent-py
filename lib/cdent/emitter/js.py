"""\
JavaScript code emitter for C'Dent
"""

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'js'
    LINE_COMMENT_PREFIX = '// '
    BLOCK_COMMENT_BEGIN = '/*\n'
    BLOCK_COMMENT_PREFIX = ' * '
    BLOCK_COMMENT_END = ' */\n'

    def emit_class(self, klass): 
        name = klass.name
        self.writeln('(this.%s = function() {}).prototype = {' % name)
        self.indent()
        self.emit(klass.has)
        self.undent()
        self.writeln('}')

    def emit_method(self, method): 
        name = method.name
        self.writeln(name + ': function() {')
        self.indent()
        for node in method.has:
            self.dispatch(node)
        self.undent()
        self.writeln('}')

    def emit_println(self, builtin): 
        self.write('print(', indent=True)
        for node in builtin.args:
            self.dispatch(node)
        self.writeln(');', indent=False)

    def emit_return(self, ret): 
        self.writeln('return;')
