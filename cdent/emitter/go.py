"""\
Go code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'go'
    LINE_COMMENT_PREFIX = '// '
    BLOCK_COMMENT_BEGIN = '/*\n'
    BLOCK_COMMENT_PREFIX = ' * '
    BLOCK_COMMENT_END = ' */\n'

    def emit_class(self, class_): 
        name = class_.name
        self.writeln("""\
package %(name)s
import fmt "fmt"
""" % locals())
        self.emit(class_.has, indent=False)

    def emit_method(self, method): 
        name = method.name
        self.writeln('func %s() {' % name)
        self.emit(method.has, indent=True)
        self.writeln('}')

    def emit_println(self, println): 
        self.write('fmt.Println(', indent=True)
        self.emit(println.args)
        self.writeln(');', indent=False)

    def emit_return(self, ret): 
        self.writeln('return;')
