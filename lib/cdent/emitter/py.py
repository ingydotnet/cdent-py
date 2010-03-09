"""\
Python code emitter for C'Dent
"""

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'pm'
    BLOCK_COMMENT_BEGIN = '"""\\\n'
    BLOCK_COMMENT_PREFIX = ''
    BLOCK_COMMENT_END = '"""\n'

    def emit_class(self, klass):
        name = klass.name
        self.writeln('class %s():' % name)
        self.indent()
        for node in klass.has:
            self.dispatch(node)
        self.undent()

    def emit_method(self, method): 
        name = method.name
        self.writeln('%s(self):' % name)
        self.indent()
        for node in method.has:
            self.dispatch(node)
        self.undent()

    def emit_println(self, builtin): 
        self.write('print ', indent=True)
        for node in builtin.args:
            self.dispatch(node)
        self.writeln()

    def emit_return(self, ret): 
        self.writeln('return')
