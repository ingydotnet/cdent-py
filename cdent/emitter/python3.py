"""\
Python code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'py3'
    BLOCK_COMMENT_BEGIN = '"""\\\n'
    BLOCK_COMMENT_PREFIX = ''
    BLOCK_COMMENT_END = '"""\n'

    def emit_includecdent(self, includecdent):
        self.writeln('from cdent.run import *')

    def emit_class(self, class_):
        name = class_.name
        self.writeln('class %s():' % name)
        self.emit(class_.has, indent=True)

    def emit_method(self, method): 
        name = method.name
        self.writeln('def %s(self):' % name)
        self.emit(method.has, indent=True)

    def emit_println(self, println): 
        self.write('print(', indent=True)
        self.emit(println.args)
        self.write(')')
        self.writeln()

    def emit_return(self, return_): 
        self.writeln('return')
