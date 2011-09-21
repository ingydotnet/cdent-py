"""\
CoffeeScript code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'coffee'
    BLOCK_COMMENT_PREFIX = ''

    def emit_includecdent(self, includecdent): 
        self.writeln('use CDent::Run;')

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('class %s' % name)
        self.emit(class_.has, indent=True)

    def emit_method(self, method): 
        name = method.name
        self.writeln('%s: () ->' % name)
        self.emit(method.has, indent=True)

    def emit_println(self, println): 
        self.write('print ', indent=True)
        self.emit(println.args)
        self.writeln(', "\\n"', indent=False)

    def emit_return(self, ret): 
        self.writeln('return;')
