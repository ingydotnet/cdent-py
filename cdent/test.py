import os

import unittest
from unittest import main

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
