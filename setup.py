#!/usr/bin/env python
# coding=utf-8

import os
import sys
import codecs
import glob

from distutils.core import setup, Command

import cdent


class Test(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        build_cmd = self.get_finalized_command('build')
        build_cmd.run()
        sys.path.insert(0, build_cmd.build_lib)
        sys.path.insert(0, 'tests')
        def exit(code):
            pass
        sys.exit = exit

        for test in glob.glob('tests/*.py'):
            name = test[test.index('/') + 1: test.rindex('.')]
            module = __import__(name)
            module.cdent.test.main(module=module, argv=[''])


if __name__ == '__main__':
    packages = []
    for t in os.walk('cdent'):
        packages.append(t[0].replace('/', '.'))

    setup(
        name='cdent',
        version=cdent.__version__,

        description='A Portable Module Programming Language',
        long_description = codecs.open(
            os.path.join(
                os.path.dirname(__file__),
                'README.rst'
            ),
            'r',
            'utf-8'
        ).read(),

        # See: http://pypi.python.org/pypi?:action=list_classifiers
        classifiers = [
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Awk',
            'Programming Language :: C#',
            'Programming Language :: C++',
            'Programming Language :: Erlang',
            'Programming Language :: Haskell',
            'Programming Language :: Java',
            'Programming Language :: JavaScript',
            'Programming Language :: Other Scripting Engines',
            'Programming Language :: Perl',
            'Programming Language :: PHP',
            'Programming Language :: Python',
            'Programming Language :: Ruby',
            'Programming Language :: Scheme',
            'Programming Language :: Tcl',
            'Topic :: Software Development',
            'Topic :: System :: Software Distribution',
            'Topic :: Utilities',
        ],

        author='Ingy dot Net',
        author_email='ingy@ingy.net',
        license='Simplified BSD License',
        url='http://www.cdent.org/',

        packages=packages,
        scripts=['bin/cdent'],

        cmdclass={'test': Test},
    )
