from package.unittest import *

import cdent.parser.cdent.yaml
import cdent.parser.javascript

class TestPythonParser(TestCase):

    def test_parse_javscript(self):
        parser = cdent.parser.javascript.Parser()
        # parser.debug = True
        input = file('tests/modules/world.cd.js', 'r').read()
        parser.open(input)
        try:
            ast = parser.parse()
        except cdent.parser.ParseError, err:
            print err
            return
            exit(1)


        parser = cdent.parser.cdent.yaml.Parser()
        input = file('tests/modules/world.cd.yaml', 'r').read()
        parser.open(input)
        expected = parser.parse()

        self.assertEqual(ast.__class__.__name__, expected.__class__.__name__)

if __name__ == '__main__':
    main()
