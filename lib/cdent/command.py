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
        self.parser = None
        self.emitter = None
        self.emit_header = None
        self.emit_trailer = None
        if 'CDENT_EMIT_INFO' in os.environ:
            self.emit_header = bool(int(os.environ['CDENT_EMIT_INFO']))
            self.emit_trailer = bool(int(os.environ['CDENT_EMIT_INFO']))
        if 'CDENT_EMIT_HEADER' in os.environ:
            self.emit_header = bool(int(os.environ['CDENT_EMIT_HEADER']))
        if 'CDENT_EMIT_TRAILER' in os.environ:
            self.emit_trailer = bool(int(os.environ['CDENT_EMIT_TRAILER']))

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
            exec "from cdent.parser." + value + " import Parser" in globals()
            self.parser = Parser()
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
            exec "from cdent.emitter." + value + " import Emitter" in globals()
            self.emitter = Emitter()
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
            self.parser.input_path = value
        parser.add_option(
            "--input", type="string",
            action="callback", callback=cb_input,
            help="input file -- default is stdin",
        )

        # --output=FILE
        def cb_output(option, opt, value, parser):
            self.emitter.output_path = value
        parser.add_option(
            "--output", type="string",
            action="callback", callback=cb_output,
            help="output file -- default is stdout",
        )

        # --emit-info
        def cb_emit_info(option, opt, value, parser):
            self.emit_header = bool(int(value))
            self.emit_trailer = bool(int(value))
        parser.add_option(
            "--emit-info", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_emit_info,
            help="emit info header & trailer -- default is on",
        )

        # --emit-header
        def cb_emit_header(option, opt, value, parser):
            self.emit_header = bool(int(value))
        parser.add_option(
            "--emit-header", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_emit_header,
            help="emit info header -- default is on",
        )

        # --emit-trailer
        def cb_emit_trailer(option, opt, value, parser):
            self.emit_trailer = bool(int(value))
        parser.add_option(
            "--emit-trailer", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_emit_trailer,
            help="emit info trailer -- default is on",
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

        # move options
        if self.emitter:
            if self.emit_header != None:
                self.emitter.emit_header = self.emit_header
            if self.emit_trailer != None:
                self.emitter.emit_trailer = self.emit_trailer

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
        self.parser.open()
        ast = self.parser.parse_module()
        self.emitter.open()
        self.emitter.create_module(ast)

    def version(self):
        import cdent
        print "C'Dent version '%s'" % cdent.version
