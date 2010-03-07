class Base():
    def __init__(self):
        self.code = []

    def write(self, path):
        if path == '-':
            import sys
            f = sys.stdout
        else:
            f = file(path, 'w')
        f.write(''.join(self.code)) 

    def dispatch(self, node):
        klass = str(node.__class__)
        type = klass[klass.index('_') + 1:]
        method = 'gen_' + type
        getattr(self, method)(node)

    def put(self, code):
        self.code.append(code)
