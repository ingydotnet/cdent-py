from __future__ import absolute_import

import os

import unittest

class TestCase(unittest.TestCase):
    def tearDown(self):
        if os.path.exists('expected'):
            os.unlink('expected')
        if os.path.exists('got'):
            os.unlink('got')

    def assertTextEquals(self, got, expected, msg=None):
        if got != expected:
            file('expected', 'w').write(expected)
            file('got', 'w').write(got)
            os.system('diff -u expected got')

        self.assertEquals(got, expected, msg)

class main():
    def __init__(self, module='__main__', argv=None):
        unittest.main(module=module, argv=argv)
