"""\
PIR code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'pir'

    def emit_includecdent(self, includecdent):
        pass

    def emit_class(self, class_):
        name = class_.name
        self.writeln('.namespace ["%s"]' % name)
        self.writeln()
        self.emit(class_.has)

    def emit_method(self, method):
        name = method.name
        self.writeln('.method %s' % name)
        self.emit(method.has, indent=True)
        self.writeln('.end')

    def emit_println(self, println):
        self.write('say ', indent=True)
        self.emit(println.args)
        self.writeln('')

    def emit_return(self, ret):
        self.writeln('.return(%s)', ret)
