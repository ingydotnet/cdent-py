"""\
Parser base class for C'Dent
"""
from __future__ import absolute_import

import sys
import re

from cdent.ast import *

import yaml
def y(o):
    print yaml.dump(o)
    return o

class Parser():
    def __init__(self):
        self.stream = ''

    def open(self, input):
        if isinstance(input, str):
            if input == '-':
                self.stream = sys.stdin.read()
            else:
                self.stream = input
        elif isinstance(input, file):
            self.stream = input.read()
        else:
            raise Exception("input to open is invalid")

    def parse(self):
        if self.stream.rfind('\n') <= 0:
            raise Exception("no input to parse")
        self.index = 0
        self.strlen = len(self.stream)
        self.ast = AST()
        start_rule = getattr(self.grammar, 'Module')
        self.match(start_rule)
        y(self.ast)

    def match(self, rule):
        text = self.stream[self.index:].splitlines()[0]
        print "match> %s >%s<" % (repr(rule), text)

        type = rule.__class__.__name__
        if type == 'All':
            return self.match_all(rule)
        elif type == 'Any':
            return self.match_any(rule)
        elif type == 'Re':
            return self.match_re(rule)
        elif type == 'Rule':
            return self.match_rule(rule)
        else:
            raise Exception("*** Error; type is " + type)

    def match_all(self, all):
        for rule in all._:
            if not self.match(rule):
                return False
        return True

    def match_any(self, all):
        for rule in all._:
            if self.match(rule):
                return True
        return False

    def match_rule(self, rule):
        return self.match(getattr(self.grammar, rule._))

    def match_re(self, regexp):
        text = self.stream[self.index:].splitlines()[0]
        pattern = regexp._
        m = re.match(pattern, self.stream[self.index:])
        if (m):
            print "Re(%s) match passed>%s" % (repr(pattern), text)
            self.index += m.end()
            return True
        else:
            print "Re(%s) match failed>%s" % (repr(pattern), repr(self.stream))
            return False

    def match_fail(self, rule):
        text = self.stream[self.index:].splitlines()[0]
        error = """\
Failed to match rule '%s'
against text '%s'
""" % (rule, text)
        raise Exception(error)
