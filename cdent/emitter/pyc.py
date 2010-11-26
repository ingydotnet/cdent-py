"""\
Python bytecode emitter for C'Dent
"""

from __future__ import absolute_import

import ast
import imp
import marshal
import yaml

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'pyc'

    def __init__(self):
        Base.__init__(self)
        self.mod = ast.Module()
        self.mod.body = []

    def emit_comment(self, comment):
        pass

    def write_line_comment(self, comment):
        pass

    def write_block_comment(self, comment):
        pass

    def emit_includecdent(self, includecdent):
        self.writeln('from cdent.run import *')

    def emit_class(self, class_):
        self.class_ = self._make(
            ast.ClassDef,
            name=class_.name,
            bases=[],
            body=[],
            decorator_list=[]
        )
        self.mod.body.append(self.class_)
        self.emit(class_.has)
        self.write(imp.get_magic())
        self.write("\x00\x00\x00\x00")
        co = compile(self.mod, "<cdent>", "exec")
        self.write(marshal.dumps(co))

    def emit_method(self, method): 
        selfn = self._make(ast.Name, id="self", ctx=ast.Param())
        args = self._make(ast.arguments, args=[selfn], defaults=[], kwarg=None, vararg=None)
        self.method_ = self._make(
            ast.FunctionDef,
            name=method.name,
            args=args,
            body=[],
            decorator_list=[],
        )
        #
        # XXX MUST EMIT FIRST! appending to self.class_.body segfaults with
        # empty method bodies!
        #
        self.emit(method.has)
        self.class_.body.append(self.method_)

    def emit_println(self, println): 
        self.println_ = self._make(ast.Print, values=[], nl=True)
        self.emit(println.args)
        self.method_.body.append(self.println_)

    def emit_string(self, str_):
        strn = self._make(ast.Str, s=str_.val)
        self.println_.values.append(strn)

    def emit_return(self, return_): 
        self.method_.body.append(self._make(ast.Return))

    def cdent_header(self, ast):
        pass

    def cdent_trailer(self, ast):
        pass

    def _make(self, nodetype, *args, **kwargs):
        node = nodetype(*args, **kwargs)
        if "lineno" in node._attributes:
            node.lineno = 0
        if "col_offset" in node._attributes:
            node.col_offset = 0
        return node


