"""\
Parser base class for C'Dent
"""

from __future__ import absolute_import

import sys
import re
import traceback

from cdent.ast import *

import yaml
def y(o):
    print yaml.dump(o)
    return o

def die(s):
    raise Exception(s)

def warn(s):
    print 'warning: %s' % s
    return s

class Parser():
    def __init__(self):
        self.stream = None

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
        self.index = 0

    def parse(self):
        if self.stream is None:
            raise Exception("You need to call open() on the parser object")

        self.receiver = Receiver()
        self.match_name('Module')

        return self.receiver.ast

    def match_name(self, name):
        print "match_name> " + name
        rule = getattr(self.grammar, name)
        return self.match(rule)

    def match(self, rule):
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
        return self.match_name(rule._)

    def match_re(self, regexp):
        pattern = regexp._
        print "  re: " + pattern
        m = re.match(pattern, self.stream[self.index:])
        if (m):
            print "  passed"
            self.index += m.end()
            return True
        else:
            print "  failed"
            return False

    def match_fail(self, rule):
        text = self.stream[self.index:].splitlines()[0]
        error = """\
Failed to match rule '%s'
against text '%s'
""" % (rule, text)
        raise Exception(error)


class Receiver():
    def __init__(self):
        self.ast = AST()
        self.cur = self.ast


