"""\
Python code generator for C'Dent
"""

from cdent.generator import Generator as Base

class Generator(Base):
    def gen_comment(self, comment):
        self.writeln('"""\\')
        self.write(comment.val)
        self.writeln('"""')
        self.writeln()

    def gen_class(self, klass):
        name = klass.name
        self.writeln('class %s():' % name)
        self.indent()
        for node in klass.has:
            self.dispatch(node)
        self.undent()

    def gen_method(self, method): 
        name = method.name
        self.writeln('%s(self):' % name)
        self.indent()
        for node in method.has:
            self.dispatch(node)
        self.undent()

    def gen_println(self, builtin): 
        self.write('print ', indent=True)
        for node in builtin.args:
            self.dispatch(node)
        self.writeln()

    def gen_return(self, ret): 
        self.writeln('return')
