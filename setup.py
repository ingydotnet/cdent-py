#!/usr/bin/env python
# coding=utf-8

import os
import sys
sys.path.insert(0, 'lib')
import codecs

from distutils.core import setup

import cdent

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

    packages=['cdent', 'cdent.parser', 'cdent.emitter'],
    scripts=['bin/cdent'],
)
