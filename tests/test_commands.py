from package.unittest import *

class TestCommands(TestCase):
    def test_commands(self):
        import cdent.command
        cdent.command.Command(['--compile', '--from=cd.py', '--to=rb'])


if __name__ == '__main__':
    main()

