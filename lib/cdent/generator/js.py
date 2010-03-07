"""
JavaScript code generator for C'Dent
"""

import re
from cdent.generator import Base

class Generator(Base):
    def __init__(self):
        Base.__init__(self)
        self.comment_re = re.compile('^\s*#+', re.MULTILINE);

    def generate(self, ast, path):
        self.dispatch(ast)
        self.write(path)

    def gen_module(self, module):
        for node in module.has:
            self.dispatch(node)

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

    def gen_string(self, string):
        self.put('"' + string.val + '"')
