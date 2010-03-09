"""\
JavaScript code emitter for C'Dent
"""

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'pm'

    def emit_class(self, klass): 
        name = klass.name
        self.writeln('package %s;' % name)
        self.writeln('use Moose;')
        self.writeln()
        for node in klass.has:
            self.dispatch(node)
        self.writeln()
        self.writeln('1;')

    def emit_method(self, method): 
        name = method.name
        self.writeln('sub %s {' % name)
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
