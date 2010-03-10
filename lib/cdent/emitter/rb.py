"""\
JavaScript code emitter for C'Dent
"""

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'rb'

    def emit_class(self, klass): 
        name = klass.name
        self.writeln('class %s' % name)
        self.emit(klass.has, indent=True)
        self.writeln('end')

    def emit_method(self, method): 
        name = method.name
        self.writeln('def %s' % name)
        self.emit(method.has, indent=True)
        self.writeln('end')

    def emit_println(self, println): 
        self.write('puts(', indent=True)
        self.emit(println.args)
        self.writeln(')', indent=False)

    def emit_return(self, ret): 
        self.writeln('return')
