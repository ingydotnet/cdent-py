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
    print yaml.dump(o, default_flow_style=False)
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
#         y(self.grammar)
#         sys.exit()
        if self.stream is None:
            raise Exception("You need to call open() on the parser object")

        self.receiver = Receiver()
        self.match('Module')

        return self.receiver.ast

    def match(self, name):
        print "match> " + name
        rule = getattr(self.grammar, name)
        return self.dispatch(rule)

    def dispatch(self, rule):
        type = rule.__class__.__name__
        print " rule> " + repr(rule)
        if type == 'All':
            result = self.match_all(rule)
        elif type == 'Any':
            result = self.match_any(rule)
        elif type == 'Re':
            result = self.match_re(rule)
        elif type == 'Rule':
            result = self.match_rule(rule)
        elif type == 'Not':
            result = self.match_not(rule)
        else:
            print '>>>' + repr(rule)
            raise Exception("*** Error; type is " + type)

        
        print "-rule> " + ('pass' if result else 'fail') + type
        return result

    def match_all(self, all):
        print "  all>"
        for rule in all._:
            if not self.dispatch(rule):
                return False
        return True

    def match_any(self, all):
        for rule in all._:
            if self.dispatch(rule):
                return True
        return False

    def match_rule(self, rule):
        name = rule._
        rep = getattr(rule, 'x', '1')
        count = 0
        while True:
            result = self.match(name)
            if rep == '1': return result
            if rep == '?': return True
            if not result:
                if rep == '+': return (count > 0)
                if rep == '*': return True
            count += 1

    def match_re(self, regexp):
        pattern = regexp._
        print "  re> " + pattern
        m = re.match(pattern, self.stream[self.index:])
        if (m):
            print "   passed> " + self.current_text()
            self.index += m.end()
            return True
        else:
            print "   failed> " + self.current_text()
            return False

    def match_not(self, rule):
        return not self.dispatch(rule._)

    def current_text(self):
       text = self.stream[self.index:]
       return repr(text)

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


