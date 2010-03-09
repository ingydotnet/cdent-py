"""\
JavaScript code generator for C'Dent
"""

from cdent.generator import Generator as Base

class Generator(Base):
    LANGUAGE_ID = 'js'
    LINE_COMMENT_PREFIX = '// '
    BLOCK_COMMENT_BEGIN = '/*\n'
    BLOCK_COMMENT_PREFIX = ' * '
    BLOCK_COMMENT_END = ' */\n'

    def gen_class(self, klass): 
        name = klass.name
        self.writeln('(this.%s = function() {}).prototype = {' % name)
        self.indent()
        self.generate(klass.has)
        self.undent()
        self.writeln('}')

    def gen_method(self, method): 
        name = method.name
        self.writeln(name + ': function() {')
        self.indent()
        for node in method.has:
            self.dispatch(node)
        self.undent()
        self.writeln('}')

    def gen_println(self, builtin): 
        self.write('print(', indent=True)
        for node in builtin.args:
            self.dispatch(node)
        self.writeln(');', indent=False)

    def gen_return(self, ret): 
        self.writeln('return;')
