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

globals()['ind'] = ''
def reset():
    globals()['ind'] = ''
def indent():
    globals()['ind'] = globals()['ind'] + ' '
def undent():
    globals()['ind'] = globals()['ind'][0:-1]
def log(s):
    s = ind + s
    if len(s) > 175:
        s = s[0:175]
    print s

class Parser():
    def __init__(self):
        self.stream = None
        indents = []
        self.index = 0
#         y(self.grammar)
#         sys.exit()

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
        if self.stream is None:
            raise Exception("You need to call open() on the parser object")

        self.receiver = Receiver()
        reset()
        self.match('Module')

        return self.receiver.ast

    def match(self, name):
        rule = getattr(self.grammar, name)
        result = self.dispatch(rule)
        return result

    def dispatch(self, rule):
        type = rule.__class__.__name__
        # log("dispatch(%s)" % repr(rule))
        indent()
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
        elif type == 'Indent':
            result = self.match_indent(rule)
        elif type == 'Undent':
            result = self.match_undent(rule)
        else:
            log('>>>' + repr(rule))
            raise Exception("*** Error; type is " + type)
        log(('passed ' if result else 'failed ') + type)
        undent()
        return result

    def match_all(self, all):
        log("match_all(%s)" % all)
        for rule in all._:
            if not self.dispatch(rule):
                return False
        return True

    def match_any(self, any):
        log("match_any(%s)" % any)
        for rule in any._:
            if self.dispatch(rule):
                return True
        return False

    def match_rule(self, rule):
        log("match_rule(%s)" % rule)
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
        log("match_re(%s)" % pattern)
        log("        >%s" % self.current_text())
        m = re.match(pattern, self.stream[self.index:])
        if (m):
            self.index += m.end()
            return True
        else:
            return False

    def match_not(self, rule):
        log("match_not(%s)" % rule)
        index = self.index
        result = not self.dispatch(rule._)
        self.index = index
        return result

    def match_indent(self, rule):
        return True

    def current_text(self):
       text = self.stream[self.index:]
       return repr(text)


class Receiver():
    def __init__(self):
        self.ast = AST()
        self.cur = self.ast


