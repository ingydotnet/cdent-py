import os
import sys
import StringIO

sys.path.insert(0, '.')

from package.unittest import *

import cdent

class TestPythonParser(TestCase):
    def setUp(self):
        import cdent.parser.cdent.yaml

        parser = cdent.parser.cdent.yaml.Parser()
        input = file('tests/modules/World.cd.yaml', 'r')
        parser.open(input)
        self.ast = parser.parse()

    def run_test(self, lang, suffix, module):
        emitter_module = 'cdent.emitter.%s' % lang
        __import__(emitter_module)

        emitter = getattr(cdent.emitter, lang).Emitter()
        output = StringIO.StringIO()
        emitter.open(output)
        emitter.emit_ast(self.ast)
        got = output.getvalue()
        expected = file('tests/modules/%s' % module).read()

        self.assertTextEquals(got, expected, 'Emit %s' % module)

    def test_emit_perl(self):
        self.run_test('perl', 'pm', 'World.pm')

    def test_emit_python(self):
        self.run_test('python', 'py', 'world.py')

    def test_emit_php(self):
        self.run_test('php', 'php', 'World.php')

    def test_emit_ruby(self):
        self.run_test('ruby', 'rb', 'World.rb')

    def test_emit_javascript(self):
        self.run_test('javascript', 'js', 'World.js')

    def test_emit_scala(self):
        self.run_test('scala', 'scala', 'World.scala')

    def test_emit_java(self):
        self.run_test('java', 'java', 'World.java')

    def test_emit_actionscript(self):
        self.run_test('actionscript', 'as', 'World.as')

    def test_emit_perl6(self):
        self.run_test('perl6', 'pm6', 'World.pm6')

    def test_emit_python3(self):
        self.run_test('python3', 'py3', 'world.py3')

    def test_emit_go(self):
        self.run_test('go', 'go', 'World.go')

    def test_emit_pir(self):
        self.run_test('pir', 'pir', 'World.pir')

#     def test_emit_cd_yaml(self):
#         self.run_test('cdent.yaml', 'cd.yaml', 'World.cd.yaml')

if __name__ == '__main__':
    main()
