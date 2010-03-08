"""\
Command line UI module for C'Dent

:w|!PYTHONPATH=lib python cdent --compile --from=cd --to=js --input=hello-world/World.cd --output=hello-world/World.py
"""

import os, sys
from optparse import *

class Command():
    def __init__(self, args):
        sys.argv = args
        self.action = None
        self.input = '-'
        self.output = '-'
        self.src = None
        self.to = None

        parser = OptionParser()

        def cb_action(option, opt, value, parser):
            self.action = opt[2:]
        parser.add_option(
            "--compile",
            action="callback", callback=cb_action,
            help="compile from one form to another (required)"
        )

        def cb_from(option, opt, value, parser):
            self.src = value
        parser.add_option(
            "--from", type="choice",
            choices=['cd', 'js', 'py'],
            action="callback", callback=cb_from,
            help="source language: cd|js|py"
        )

        def cb_to(option, opt, value, parser):
            self.to = value
        parser.add_option(
            "--to", type="choice",
            choices=['cd', 'cpp', 'java', 'js', 'php', 'pm', 'pm6', 'py', 'py3'],
            action="callback", callback=cb_to,
            help="target language: cd|cpp|java|js|php|pm|pm6|py|py3"
        )

        def cb_input(option, opt, value, parser):
            if not os.path.exists(value):
                raise OptionError(value + ' file does not exist', opt)
            self.input = value
        parser.add_option(
            "--input", type="string",
            action="callback", callback=cb_input,
            help="input file -- default is stdin",
        )

        def cb_output(option, opt, value, parser):
            self.output = value
        parser.add_option(
            "--output", type="string",
            action="callback", callback=cb_output,
            help="output file -- default is stdout",
        )

        def cb_version(option, opt, value, parser):
            self.action = 'version'
        parser.add_option(
            "--version",
            action="callback", callback=cb_version,
            help="print cdent version"
        )

        (opts, args) = parser.parse_args()

        if (args):
            raise OptionError('extra arguments found', 'arguments')
        if (not self.action):
            raise OptionError('is required', '--compile')
        if self.action == 'compile':
            if (not self.src):
                raise OptionError('is required', '--from')
            if (not self.to):
                raise OptionError('is required', '--to')

    def main(self):
        getattr(self, self.action)()

    def compile(self):
        exec "from cdent.compiler." + self.src + " import Compiler"
        exec "from cdent.generator." + self.to + " import Generator"
        ast = Compiler(self.input).compile()
        Generator(self.output).generate(ast)

    def version(self):
        import cdent
        print "C'Dent version '%s'" % cdent.version
