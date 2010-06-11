import os
import sys
import StringIO

from package.unittest import *

class TestPythonParser(TestCase):
    def setUp(self):
        import cdent.parser.cdent.yaml

        parser = cdent.parser.cdent.yaml.Parser()
        input = file('tests/modules/world.cd.yaml', 'r')
        parser.open(input)
        self.ast = parser.parse()

    def test_emit_python(self):
        import cdent.emitter.python

        emitter = cdent.emitter.python.Emitter()
        output = StringIO.StringIO()
        emitter.open(output)
        emitter.emit_ast(self.ast)
        got = output.getvalue()
        expected = file('tests/modules/world.py').read()

        self.assertTextEquals(got, expected, 'Emit world.py')

    def test_emit_perl(self):
        import cdent.emitter.perl

        emitter = cdent.emitter.perl.Emitter()
        output = StringIO.StringIO()
        emitter.open(output)
        emitter.emit_ast(self.ast)
        got = output.getvalue()
        expected = file('tests/modules/World.pm').read()

        self.assertTextEquals(got, expected, 'Emit world.pm')

    def test_emit_pir(self):
        import cdent.emitter.pir

        emitter = cdent.emitter.pir.Emitter()
        output = StringIO.StringIO()
        emitter.open(output)
        emitter.emit_ast(self.ast)
        got = output.getvalue()
        expected = file('tests/modules/World.pir').read()

        self.assertTextEquals(got, expected, 'Emit world.pir')

    def test_emit_go(self):
        import cdent.emitter.go

        emitter = cdent.emitter.go.Emitter()
        output = StringIO.StringIO()
        emitter.open(output)
        emitter.emit_ast(self.ast)
        got = output.getvalue()
        expected = file('tests/modules/World.go').read()

        self.assertTextEquals(got, expected, 'Emit world.go')

    def test_emit_as(self):
        import cdent.emitter.as_

        emitter = cdent.emitter.as_.Emitter()
        output = StringIO.StringIO()
        emitter.open(output)
        emitter.emit_ast(self.ast)
        got = output.getvalue()
        expected = file('tests/modules/World.as').read()

        self.assertTextEquals(got, expected, 'Emit world.as')

if __name__ == '__main__':
    main()

