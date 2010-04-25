"""\
Code emitter base class for C'Dent
"""
from __future__ import absolute_import

import sys
import StringIO

import cdent.compiler

class Emitter():
    # Default comment constants
    LINE_COMMENT_PREFIX = '# '
    BLOCK_COMMENT_BEGIN = '###\n'
    BLOCK_COMMENT_PREFIX = '# '
    BLOCK_COMMENT_END = '###\n'

    def __init__(self):
        self.emit_header = True
        self.emit_trailer = False
        self.indentation = ''

    def open(self, output):
        if isinstance(output, str) and output == '-':
            self.output = sys.stdout
        elif isinstance(output, (file, StringIO.StringIO)):
            self.output = output
        else:
            raise Exception("input to open is invalid")

    def emit(self, container, indent=False):
        if indent:
            self.indent()
        for node in container:
            self.dispatch(node)
        if indent:
            self.undent()

    def dispatch(self, node):
        class_ = str(node.__class__)
        type = class_[class_.rindex('.') + 1:].lower()
        method = 'emit_' + type
        getattr(self, method)(node)

    def write(self, string='', indent=False):
        if indent:
            self.output.write(self.indentation) 
        self.output.write(string) 

    def writeln(self, string='', indent=True):
        if indent and len(string) > 0:
            self.output.write(self.indentation) 
        self.output.write(string + '\n') 

    def write_line_comment(self, comment):
        self.writeln(self.LINE_COMMENT_PREFIX + comment)

    def write_block_comment(self, comment):
        self.write(self.BLOCK_COMMENT_BEGIN, indent=True)
        for line in comment.splitlines():
            self.writeln(self.BLOCK_COMMENT_PREFIX + line)
        self.write(self.BLOCK_COMMENT_END, indent=True)

    def indent(self):
        self.indentation += '    '

    def undent(self):
        try:
            self.indentation = self.indentation[:-4]
        except IndexError:
            self.indentation = ''

    def emit_ast(self, ast):
        if self.emit_header:
            self.cdent_header(ast)
        for node in ast.has:
            self.dispatch(node)
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
        header = (
            "*** DO NOT EDIT ***  This is a C'Dent generated %s module." %
            cdent.compiler.language(self.LANGUAGE_ID)
        )
        if self.emit_trailer:
            header += " See trailer at end of file for details."
        self.write_line_comment(header)
#         header = "C'Dent is Copyright (c) 2010, Ingy dot Net. All rights reserved."
#         self.write_line_comment(header)
#         header = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
#         self.writeln(header)

    def cdent_trailer(self, ast):
        from time import strftime
        cdent_version = cdent.compiler.__version__
        module_name = ast.has.name
        module_lang = cdent.compiler.language(self.LANGUAGE_ID)
        compile_time = strftime("%Y-%m-%d %H:%M:%S")
        compiled_by = ast.user
        input_path = getattr(ast, 'from')['path']
        input_lang = cdent.compiler.language(getattr(ast, 'from')['lang'])
        self.writeln()
        self.write_block_comment(self.trailer_text() % locals())

    def trailer_text(self):
        return """\
# C'Dent compilation details:
---
name: %(module_name)s
lang: %(module_lang)s
time: %(compile_time)s
user: %(compiled_by)s
input:
  path: %(input_path)s
  lang: %(input_lang)s
cdent: %(cdent_version)s
"""

def y(o):
    import yaml
    print yaml.dump(o, default_flow_style=False)
    return o
