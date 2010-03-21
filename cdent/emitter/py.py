"""\
Python code emitter for C'Dent
"""

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'py'
    BLOCK_COMMENT_BEGIN = '"""\\\n'
    BLOCK_COMMENT_PREFIX = ''
    BLOCK_COMMENT_END = '"""\n'

    def emit_class(self, class_):
        name = class_.name
        self.writeln('class %s():' % name)
        self.emit(class_.has, indent=True)

    def emit_method(self, method): 
        name = method.name
        self.writeln('%s(self):' % name)
        self.emit(method.has, indent=True)

    def emit_println(self, println): 
        self.write('print ', indent=True)
        self.emit(println.args)
        self.writeln()

    def emit_return(self, ret): 
        self.writeln('return')
