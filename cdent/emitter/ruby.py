"""\
JavaScript code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'rb'

    def emit_includecdent(self, includecdent): 
        self.writeln("require 'CDent::Run'")

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('class %s' % name)
        self.emit(class_.has, indent=True)
        self.writeln('end')

    def emit_method(self, method): 
        name = method.name
        self.writeln('def %s' % name)
        self.emit(method.has, indent=True)
        self.writeln('end')

    def emit_println(self, println): 
        self.write('puts ', indent=True)
        self.emit(println.args)
        self.writeln('', indent=False)

    def emit_return(self, ret): 
        self.writeln('return')
