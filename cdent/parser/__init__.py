"""\
Parser base class for C'Dent
"""

from cdent.ast import *

import yaml

def y(o): print yaml.dump(o)

class Parser():
    def parse(self, input):
        self.index = 0
        self.stream = input
        self.length = len(self.stream)

        self.match('Module')
    
    def match(self, name):
        rule = self.grammar.__dict__[name]
        t = rule.__class__.__name__
        method = getattr(self, 'match_' + t.lower())
        method(rule._)

    def match_all(self, all):
        for rule in all:
            print '>> ' + repr(rule)
