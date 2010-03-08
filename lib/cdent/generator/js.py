"""\
JavaScript code generator for C'Dent
"""

from cdent.generator import Generator as Base

class Generator(Base):
    def gen_comment(self, comment):
        text = self.comment_re.sub('//', comment.val)
        self.put(text)

    def gen_class(self, klass): 
        name = klass.name
        self.put('(this.' + name + ' = function() {}).prototype = {\n')
        for node in klass.has:
            self.dispatch(node)
        self.put('}\n')

    def gen_method(self, method): 
        name = method.name
        self.put('    ' + name + ': function() {\n')
        for node in method.has:
            self.dispatch(node)
        self.put('    }\n')

    def gen_builtin(self, builtin): 
        name = builtin.name
        self.put('        ' + name + '(')
        for node in builtin.args:
            self.dispatch(node)
        self.put(');\n')

    def gen_return(self, ret): 
        self.put('        return;\n')
