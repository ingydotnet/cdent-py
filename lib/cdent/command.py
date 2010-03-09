"""\
Command line UI module for C'Dent
"""

import os, sys
from optparse import *

class Command():
    def __init__(self, args):
        sys.argv = args
        self.action = None
        self.src = None
        self.to = None

        parser = OptionParser()

        # --compile
        def cb_action(option, opt, value, parser):
            self.action = opt[2:]
        parser.add_option(
            "--compile",
            action="callback", callback=cb_action,
            help="compile from one form to another (required)"
        )

        # --from=LANG_ID
        def cb_from(option, opt, value, parser):
            if self.action != 'compile':
                raise OptionError('--from used before --compile')
            exec "from cdent.compiler." + value + " import Compiler" in globals()
            self.compiler = Compiler()
            self.src = value
        parser.add_option(
            "--from", type="choice",
            choices=['cd', 'js', 'py'],
            action="callback", callback=cb_from,
            help="source language: cd|js|py"
        )

        # --to=LANG_ID
        def cb_to(option, opt, value, parser):
            if self.action != 'compile':
                raise OptionError('--to used before --compile')
            exec "from cdent.generator." + value + " import Generator" in globals()
            self.generator = Generator()
            self.to = value
        parser.add_option(
            "--to", type="choice",
            choices=['cd', 'cpp', 'java', 'js', 'php', 'pm', 'pm6', 'py', 'py3'],
            action="callback", callback=cb_to,
            help="target language: cd|cpp|java|js|php|pm|pm6|py|py3"
        )

        # --input=FILE
        def cb_input(option, opt, value, parser):
            if not os.path.exists(value):
                raise OptionError(value + ' file does not exist', opt)
            self.compiler.input_path = value
        parser.add_option(
            "--input", type="string",
            action="callback", callback=cb_input,
            help="input file -- default is stdin",
        )

        # --output=FILE
        def cb_output(option, opt, value, parser):
            self.generator.output_path = value
        parser.add_option(
            "--output", type="string",
            action="callback", callback=cb_output,
            help="output file -- default is stdout",
        )

        # --version
        def cb_version(option, opt, value, parser):
            self.action = 'version'
        parser.add_option(
            "--version",
            action="callback", callback=cb_version,
            help="print cdent version"
        )

        # parse options
        (opts, args) = parser.parse_args()

        # validate options
        if (args):
            raise OptionError('extra arguments found', args)
        if (not self.action):
            raise OptionError('is required', '--compile | --help | --version')
        if self.action == 'compile':
            if (not self.src):
                raise OptionError('is required', '--from')
            if (not self.to):
                raise OptionError('is required', '--to')

    def main(self):
        getattr(self, self.action)()

    def compile(self):
        self.compiler.open()
        ast = self.compiler.compile_module()
        self.generator.open()
        self.generator.generate_module(ast)

    def version(self):
        import cdent
        print "C'Dent version '%s'" % cdent.version
