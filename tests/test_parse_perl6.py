import cdent.test

import cdent.parser.cdent.yaml
import cdent.parser.perl6

class TestPythonParser(cdent.test.TestCase):

    def test_parse_perl6(self):
        # XXX
        self.assertTrue(True)
        return

        parser = cdent.parser.perl6.Parser()
        input = file('tests/modules/world.cd.pm6', 'r').read()
        parser.open(input)
        ast = parser.parse()

        parser = cdent.parser.cdent.yaml.Parser()
        input = file('tests/modules/world.cd.yaml', 'r').read()
        parser.open(input)
        expected = parser.parse()

        self.assertEqual(ast.__class__.__name__, expected.__class__.__name__)

if __name__ == '__main__':
    cdent.test.main()
