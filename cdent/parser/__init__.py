"""\
Parser base class for C'Dent
"""

from __future__ import absolute_import

import sys
import re
import traceback

from cdent.ast import *

class Parser():
    def __init__(self):
#         y(self.grammar)
#         sys.exit()
        self.stream = None
        self.index = 0
        self.indents = []
        self.undents = []
        self.rules = []
        self.indent_please = False
        self.failure_is_ok = 0
        self.log = Log()

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

        self.receiver = Receiver(parser=self)

        if not self.match(name='Module'):
            raise Exception('Parse failed')

        return self.receiver.ast

    def match(self, name=None, rule=None):
        if name:
            self.rules.append(name)
            rule = getattr(self.grammar, name)
        elif not rule:
            raise Exception("match() requires name or rule")
        type = rule.__class__.__name__
        self.log.indent()

        if type == 'All':
            result = self.match_all(rule)
        elif type == 'Any':
            result = self.match_any(rule)
        elif type == 'Re':
            result = self.match_re(rule)
        elif type == 'Rule':
            result = self.match_rule(rule)
        elif type == 'Indent':
            result = self.request_indent(rule)
        elif type == 'Undent':
            result = self.match_undent(rule)
        else:
            log('>>>' + repr(rule))
            raise Exception("*** Error; type is " + type)

        if (result is False and
            not self.failure_is_ok and
            type == 'Rule' and
            not getattr(rule, '!', False)
        ):
            self.report_failure()

        self.log.write(('passed ' if result else 'failed ') + type)
        self.log.undent()

        if name:
            self.rules.pop()

        return result

    def match_all(self, all):
        self.log.write("match_all(%s)" % all)
        def match():
            for rule in all._:
                if not self.match(rule=rule):
                    return False
            return True
        return self.repeat_match(match, all)

    def match_any(self, any):
        self.log.write("match_any(%s)" % any)
        self.failure_is_ok += 1
        def match():
            for rule in any._:
                if self.match(rule=rule):
                    return True
            return False
        result = self.repeat_match(match, any)
        self.failure_is_ok -= 1
        return result

    def match_rule(self, rule):
        self.log.write("match_rule(%s)" % rule)
        not_ = getattr(rule, '!', False)
        index = self.index
        def match():
            result = self.match(name=rule._)
            if not_:
                result ^= True
                self.index = index
            return result
        return self.repeat_match(match, rule)

    def match_re(self, regexp):
        pattern = regexp._
        self.log.write("match_re(%s)" % pattern)
        self.log.write(">>>>>>>>%s" % self.current_text())
        if not self.match_indent():
            return False
        m = re.match(pattern, self.stream[self.index:])
        if (m):
            self.index += m.end()
            return True
        else:
            return False

    def repeat_match(self, match, rule):
        rep = getattr(rule, 'x', '1')
        assert rep in '?1*+'
        if rep in '?*': self.failure_is_ok += 1
        result = match()
        if rep in '?*': self.failure_is_ok -= 1
        if rep == '1': return result
        if rep == '?': return True
        if result is False:
            if rep == '+': return False
            if rep == '*': return True
        self.failure_is_ok += 1
        while result is True:
            result = match()
        self.failure_is_ok -= 1
        return True

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

    def report_failure(self):
        msg = """\
Parse error at line: %(line)s.
Failed to match: %(stack)s
Context:
%(context)s
...
"""
        index = self.index
        stream = self.stream

        line = stream[0:index].count('\n') + 1
        stack = ">".join(self.rules)

        if index > 0 and stream[index - 1] != '\n':
            index = stream.rfind("\n", 0, index) + 1
        lines = stream[index:].split("\n") if index < len(stream) else []
        lines.pop()
        if len(lines) >= 3:
            lines = lines[0:3]
        else:
            lines.append('---EOF---')
        context = "\n".join(lines)

        raise Exception(msg % locals())


class Receiver():
    def __init__(self, parser=None):
        self.ast = AST()
        self.ptr = self.ast
        self.parser = parser


class Log():
    ENABLED = False
    #ENABLED = True
    MAXLEN = 175
    def __init__(self):
        self.ind = -1
    def indent(self):
        self.ind += 1
    def undent(self):
        self.ind -= 1
    def write(self, str):
        if not self.ENABLED: return
        str = ' ' * self.ind + str
        if len(str) > self.MAXLEN:
            str = str[0:self.MAXLEN]
        print str

def y(o):
    import yaml
    print yaml.dump(o, default_flow_style=False)
    return o
