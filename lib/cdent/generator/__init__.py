"""\
Code generator base class for C'Dent
"""

import re

class Generator():
    def __init__(self, path):
        self.path = path
        self.code = []
        self.comment_re = re.compile('^\s*#+', re.MULTILINE);

    def generate(self, ast):
        self.dispatch(ast)
        self.write()

    def gen_module(self, module):
        for node in module.has:
            self.dispatch(node)

    def gen_string(self, string):
        self.put('"' + string.val + '"')

    def write(self):
        if self.path == '-':
            import sys
            f = sys.stdout
        else:
            f = file(self.path, 'w')
        f.write(''.join(self.code)) 

    def dispatch(self, node):
        klass = str(node.__class__)
        type = klass[klass.index('_') + 1:]
        method = 'gen_' + type
        getattr(self, method)(node)

    def put(self, code):
        self.code.append(code)
