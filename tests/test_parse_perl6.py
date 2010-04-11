import cdent.test

import cdent.parser.cdent.yaml
import cdent.parser.perl6

class TestPythonParser(cdent.test.TestCase):

    def test_parse_perl6(self):
        parser = cdent.parser.perl6.Parser()
        # parser.debug = True
        input = file('tests/modules/world.cd.pm6', 'r').read()
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
    cdent.test.main()
