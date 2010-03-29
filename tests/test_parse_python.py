import cdent.test

from cdent.parser.python import Parser
from cdent.ast import AST

class TestPythonParser(cdent.test.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_python(self):
        print 'test_parse_python'
        input = file('tests/modules/world.cd.py', 'r').read()
        ast = self.parser.open(input)
        ast = self.parser.parse()

        self.assertEqual(ast, isinstance(ast, AST), "Got an AST object")

if __name__ == '__main__':
    cdent.test.main()
