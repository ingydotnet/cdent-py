"""\
Code generator base class for C'Dent
"""

class Generator():
    def __init__(self, path):
        if path == '-':
            import sys
            self.out = sys.stdout
        else:
            self.out = file(path, 'w')
        self.indentation = ''

    def generate(self, ast):
        self.dispatch(ast)

    def dispatch(self, node):
        klass = str(node.__class__)
        type = klass[klass.index('_') + 1:]
        method = 'gen_' + type
        getattr(self, method)(node)

    def write(self, string='', indent=False):
        if indent:
            self.out.write(self.indentation) 
        self.out.write(string) 

    def writeln(self, string='', indent=True):
        if indent:
            self.out.write(self.indentation) 
        self.out.write(string + '\n') 

    def indent(self):
        self.indentation += '    '

    def undent(self):
        try:
            self.indentation = self.indentation[:-4]
        except IndexError:
            self.indentation = ''

    def gen_module(self, module):
        for node in module.has:
            self.dispatch(node)

    def gen_string(self, string):
        self.write('"' + string.val + '"')

