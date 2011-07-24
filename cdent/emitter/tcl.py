
"""\
Tcl code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'tcl'

    def emit_includecdent(self, includecdent): 
        self.writeln('use CDent::Run;')

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('package require Tcl 8.6')
        self.writeln()
        self.writeln('oo::class create %s {' % class_.name)
        self.emit(class_.has, indent=True)
        self.writeln('}')

    def emit_method(self, method): 
        name = method.name
        self.writeln('method %s {} {' % name)
        self.emit(method.has, indent=True)
        self.writeln('}')

    def emit_println(self, println): 
        self.write('puts ', indent=True)
        self.emit(println.args)
        self.writeln()

    def emit_return(self, ret): 
        self.writeln('return;')
