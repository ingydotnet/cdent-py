"""\
package package package
"""

import os, sys, glob
from distutils.core import Command

__version__ = '0.0.1'

has_setuptools = False

from package.errors import *

try:
    from setuptools import setup as real_setup
    has_setuptools = True
except ImportError, err:
    try:
        from distutils.core import setup as real_setup
    except ImportError, err:
        die(ENOSETUP)

def setup():
    try:
        import package.info
    except ImportError, err:
        die(ENOINFO)

    args = package.info.get()
    args['cmdclass'] = {
        'test': Test,
        'devtest': DevTest,
    }

    real_setup(**args)

class Test(Command):
    user_options = []
    test_dir = 'tests'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        build_cmd = self.get_finalized_command('build')
        build_cmd.run()
        sys.path.insert(0, build_cmd.build_lib)
        sys.path.insert(0, self.test_dir)
        def exit(code):
            pass
        sys.exit = exit

        for test in glob.glob(self.test_dir + '/*.py'):
            name = test[test.index('/') + 1: test.rindex('.')]
            module = __import__(name)
            module.cdent.test.main(module=module, argv=[''])

class DevTest(Test):
    test_dir = 'dev-tests'
