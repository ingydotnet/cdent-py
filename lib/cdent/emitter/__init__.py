"""\
Code emitter base class for C'Dent
"""

class Emitter():
    LINE_COMMENT_PREFIX = '# '
    BLOCK_COMMENT_BEGIN = '###\n'
    BLOCK_COMMENT_PREFIX = '# '
    BLOCK_COMMENT_END = '###\n'

    language = {
        'pm': 'Perl',
        'py': 'Python',
        'js': 'JavaScript',
    }

    def __init__(self):
        self.output_path = '-'
        self.emit_header = True
        self.emit_trailer = True

    def open(self):
        if self.output_path == '-':
            import sys
            self.output = sys.stdout
        else:
            self.output = file(self.output_path, 'w')
        self.indentation = ''

    def emit(self, container, indent=False):
        if indent:
            self.indent()
        for node in container:
            self.dispatch(node)
        if indent:
            self.undent()

    def dispatch(self, node):
        klass = str(node.__class__)
        type = klass[klass.index('_') + 1:]
        method = 'emit_' + type
        getattr(self, method)(node)

    def write(self, string='', indent=False):
        if indent:
            self.output.write(self.indentation) 
        self.output.write(string) 

    def writeln(self, string='', indent=True):
        if indent:
            self.output.write(self.indentation) 
        self.output.write(string + '\n') 

    def write_line_comment(self, comment):
        self.writeln(self.LINE_COMMENT_PREFIX + comment)

    def write_block_comment(self, comment):
        self.write(self.BLOCK_COMMENT_BEGIN)
        for line in comment.splitlines():
            self.writeln(self.BLOCK_COMMENT_PREFIX + line)
        self.write(self.BLOCK_COMMENT_END)

    def indent(self):
        self.indentation += '    '

    def undent(self):
        try:
            self.indentation = self.indentation[:-4]
        except IndexError:
            self.indentation = ''

    def create_module(self, ast):
        if self.emit_header:
            self.cdent_header(ast)
        self.dispatch(ast.module)
        if self.emit_trailer:
            self.cdent_trailer(ast)

    def emit_module(self, module):
        for node in module.has:
            self.dispatch(node)

    def emit_comment(self, comment):
        if comment.type == 'doc':
            self.write_block_comment(comment.val)
        else :
            for line in comment.val.splitlines():
                if comment.type == 'blank':
                    self.writeln()
                else:
                    self.write_line_comment(line)

    def emit_string(self, string):
        self.write('"' + string.val + '"')

    def cdent_header(self, ast):
        header = "C'Dent generated %s module." % self.language[self.LANGUAGE_ID]
        if self.emit_trailer:
            header += " See trailer at end of file for details."
        self.write_line_comment(header)
        header = "C'Dent is Copyright (c) 2010, Ingy dot Net. All rights reserved."
        self.write_line_comment(header)
#         header = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
#         self.writeln(header)
        self.writeln()

    def cdent_trailer(self, ast):
        from cdent import version
        from time import strftime
        _from = getattr(ast, 'from')
        trailer = """\
# C'Dent compilation details:
---
name: %s
lang: %s
time: %s
user: %s
input:
  path: %s
  lang: %s
output:
  path: %s
  lang: %s
cdent: %s
"""
        trailer = trailer % (
            ast.module.name,
            self.language[self.LANGUAGE_ID],
            strftime("%Y-%m-%d %H:%M:%S"),
            ast.user,
            _from['path'],
            self.language[_from['lang']],
            '???',
            self.language[self.LANGUAGE_ID],
            version,
        )

        self.writeln()
        self.write_block_comment(trailer)

