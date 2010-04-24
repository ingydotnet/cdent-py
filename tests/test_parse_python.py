from package.unittest import *

import cdent.parser.cdent.yaml
import cdent.parser.python

class TestPythonParser(TestCase):

    def test_parse_python(self):
        parser = cdent.parser.python.Parser()
        input = file('tests/modules/world.cd.py', 'r').read()
        parser.open(input)
        ast = parser.parse()

        parser = cdent.parser.cdent.yaml.Parser()
        input = file('tests/modules/world.cd.yaml', 'r').read()
        parser.open(input)
        expected = parser.parse()

        self.assertEqual(ast.__class__.__name__, expected.__class__.__name__)

if __name__ == '__main__':
    main()
