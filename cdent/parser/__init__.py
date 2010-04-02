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
    return
    s = ind + s
    if len(s) > 175:
        s = s[0:175]
    print s

class Parser():
    def __init__(self):
        self.stream = None
        self.index = 0
        self.indents = []
        self.undents = []
        self.indent_please = False
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
        if not self.match('Module'):
            raise Exception('Parse failed')

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
            result = self.request_indent(rule)
        elif type == 'Undent':
            result = self.match_undent(rule)
        else:
            log('>>>' + repr(rule))
            raise Exception("*** Error; type is " + type)
        log(('passed ' if result else 'failed ') + type)
        undent()
        return result

    # TODO Make sure all rep indicators work
    def match_all(self, all):
        log("match_all(%s)" % all)
        for rule in all._:
            if not self.dispatch(rule):
                return False
        return True

    # TODO Make sure all rep indicators work
    def match_any(self, any):
        log("match_any(%s)" % any)
        for rule in any._:
            if self.dispatch(rule):
                return True
        rep = getattr(any, 'x', '1')
        if rep == '1':
            return False
        if rep == '*':
            return True

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
        if not self.match_indent():
            return False
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

    def request_indent(self, rule):
        self.indent_please = True
        return True

    def match_indent(self):
        if self.index > 0 and self.stream[self.index - 1] != '\n':
            return True
        if self.stream[self.index:] == '':
            if not self.indents:
                return True
            while self.indents:
                self.undents.append(self.indents.pop())
            return False
        if self.indents:
            m = re.match(self.indents[-1], self.stream[self.index:])
            if m:
                self.index += m.end()
            else:
                self.undents.append(self.indents.pop())
                while self.indents:
                    m = re.match(self.indents[-1], self.stream[self.index:])
                    if m:
                        self.undents.append(self.indents.pop())
                    else:
                        break
                return False
        if self.indent_please:
            self.indent_please = False
            m = re.match(' +', self.stream[self.index:])
            if not m:
                return False
            indent = self.indents[-1] if self.indents else ''
            index = self.index
            self.index += m.end()
            indent += self.stream[index:self.index]
            self.indents.append(indent)
        return True

    def match_undent(self, rule):
        if self.undents:
            self.undents.pop()
            return True
        return False

    def current_text(self):
       text = self.stream[self.index:]
       return repr(text)


class Receiver():
    def __init__(self):
        self.ast = AST()
        self.cur = self.ast


