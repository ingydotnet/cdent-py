"""\
Parser base class for C'Dent
"""

from __future__ import absolute_import

import sys
import re

from cdent.ast import *


#-----------------------------------------------------------------------------#
class Receiver():
    def __init__(self, parser=None):
        self.parser = parser
        self.ast = AST()
        self.container = self.ast

    def start(self, name):
#         print 'start_%s' % name.lower()
        self.line = self.parser.stream[0:self.parser.index].count('\n') + 1
        method = getattr(self, 'start_' + name.lower(), None)
        if method:
            method()

    def finish(self, name, result):
#         if result: print 'pass_%s' % name.lower()
        method = (
            getattr(self, 'pass_' + name.lower(), None)
            if result else
            getattr(self, 'fail_' + name.lower(), None)
        )
        if method:
            method()
        method = getattr(self, 'finish_' + name.lower(), None)
        if method:
            method()

    def match_text(self, num):
        return self.parser.groups[num]

    def start_module(self):
        module = self.module = Module()
        module.name = 'Module'
        module.line = self.line
        self.ast.has.append(module)
        self.container = module

    def pass_doccommentbegin(self):
        self.comment = Comment()
        self.comment.type = 'doc'
        self.comment.val = ''
        self.comment.line = self.line

    def pass_doccommentline(self):
        self.comment.val += self.match_text(0)

    def pass_doccomment(self):
        self.container.has.append(self.comment)

    def pass_classsignature(self):
        class_ = self.class_ = Class()
        class_.name = self.match_text(0)
        class_.line = self.line
        self.module.has.append(class_)
        self.container = class_

    def pass_methodsignature(self):
        method = self.method = Method()
        method.name = self.match_text(0)
        method.line = self.line
        self.class_.has.append(method)
        self.container = method

    def pass_println(self):
        println = Println()
        println.line = self.line
        string = String()
        string.val = self.match_text(0)[1:-1]
        
        println.args = [string]
        self.method.has.append(println)

    def pass_blankline(self):
        blank = Comment()
        blank.line = self.line
        blank.type = 'blank'
        blank.val = '\n'
        self.container.has.append(blank)

#-----------------------------------------------------------------------------#
class Parser():
    def __init__(self):
#         y(self.grammar)
#         sys.exit()
        self.debug = False
        self.stream = None
        self.index = 0
        self.indents = []
        self.undents = []
        self.rules = []
        self.indent_please = False
        self.failure_is_ok = 0

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

        self.log = Log(enabled=self.debug)
        self.receiver = Receiver(parser=self)

        rule = self.get_rule('Module', False)
        result = self.match(rule)
        if not result:
            raise ParseError(self, msg="Failed to parse Module.")
        if self.index != len(self.stream):
            raise ParseError(self, msg="Failed to parse entire stream.")
        self.pop_rule(result, False)

#         y(self.receiver.ast)
        return self.receiver.ast

    def get_rule(self, name, not_):
        if not not_:
            self.rules.append(name)
            self.receiver.start(name)
        return getattr(self.grammar, name)

    def pop_rule(self, result, not_):
        if not not_:
            name = self.rules.pop()
            self.receiver.finish(name, result)

    def match(self, rule):
        self.log.indent()

        type = rule.__class__.__name__
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

        self.log.write(('passed ' if result else 'failed ') + type)
        self.log.undent()

        return result

    def match_all(self, all):
        self.log.write("match_all(%s)" % all)
        def match():
            for rule in all._:
                if not self.match(rule):
                    return False
            return True
        return self.repeat_match(match, all)

    def match_any(self, any):
        self.log.write("match_any(%s)" % any)
        self.failure_is_ok += 1
        def match():
            for rule in any._:
                if self.match(rule):
                    return True
            return False
        result = self.repeat_match(match, any)
        self.failure_is_ok -= 1
        return result

    def match_rule(self, rule):
        self.log.write("match_rule(%s)" % rule)
        not_ = getattr(rule, '!', False)
        index = self.index
        subrule = self.get_rule(rule._, not_)
        def match():
            result = self.match(subrule)
            if not_:
                result ^= True
                self.index = index
            return result
        result = self.repeat_match(match, rule)
        if not (result or self.failure_is_ok or getattr(rule, '!', False)):
            raise ParseError(self, msg="Failed to match: %(stack)s")
        self.pop_rule(result, not_)
        return result


    def match_re(self, regexp):
        pattern = regexp._
        self.log.write("match_re(%s)" % pattern)
        self.log.write(">>>>>>>>%s" % self.current_text())
        if not self.match_indent():
            return False
        m = re.match(pattern, self.stream[self.index:])
        if (m):
            self.groups = m.groups()
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

#-----------------------------------------------------------------------------#
class ParseError(Exception):
    def __init__(self, parser, msg=None):
        self.parser = parser
        self.msg = "Parse error at line: %(line)s.\n"
        if msg:
            self.msg += msg + "\n"
        self.msg += """\
Context:
%(context)s
...
"""

    def __str__(self):
        index = self.parser.index
        stream = self.parser.stream

        line = stream[0:index].count('\n') + 1
        stack = " > ".join(self.parser.rules)

        if index > 0 and stream[index - 1] != '\n':
            index = stream.rfind("\n", 0, index) + 1
        lines = stream[index:].split("\n") if index < len(stream) else []
        lines.pop()
        if len(lines) >= 3:
            lines = lines[0:3]
        else:
            lines.append('---EOF---')
        context = "\n".join(lines)

        return self.msg % locals()


#-----------------------------------------------------------------------------#
class Log():
    def __init__(self, enabled=False):
        self.ind = -1
        self.enabled = enabled
        self.maxlen = 78
    def indent(self):
        self.ind += 1
    def undent(self):
        self.ind -= 1
    def write(self, str):
        if not self.enabled: return
        str = ' ' * self.ind + str
        if len(str) > self.maxlen:
            str = str[0:self.maxlen]
        print str

#-----------------------------------------------------------------------------#
def y(o):
    import yaml
    print yaml.dump(o, default_flow_style=False)
    return o
