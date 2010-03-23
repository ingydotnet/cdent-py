"""\
Parser base class for C'Dent
"""

import re

import yaml

class Parser():
    def parse(self, input):
        self.index = 0
        self.stream = input
        self.length = len(self.stream)
