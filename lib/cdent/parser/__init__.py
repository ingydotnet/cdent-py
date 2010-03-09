"""\
Parser base class for C'Dent
"""

import yaml
class Parser():
    def __init__(self):
        self.input_path = '-'

    def open(self):
        if self.input_path == '-':
            import sys
            self.input = sys.stdin
        else:
            self.input = file(self.input_path, 'r')
