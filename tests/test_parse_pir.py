from package.unittest import *

import cdent.parser.cdent.yaml
import cdent.parser.pir

class TestPythonParser(TestCase):

    def test_parse_pir(self):
        parser = cdent.parser.pir.Parser()
        # parser.debug = True
        input = file('tests/modules/World.cd.pir', 'r').read()
        parser.open(input)
        try:
            ast = parser.parse()
        except cdent.parser.ParseError, err:
            print err
            return
            exit(1)

        parser = cdent.parser.cdent.yaml.Parser()
        input = file('tests/modules/World.cd.yaml', 'r').read()
        parser.open(input)
        expected = parser.parse()

        self.assertEqual(ast.__class__.__name__, expected.__class__.__name__)

if __name__ == '__main__':
    main()
