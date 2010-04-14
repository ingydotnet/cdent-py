"""\
Command line UI module for C'Dent
"""


import os
import sys
import re

from optparse import *

import cdent.compiler


class Command():
    def __init__(self, args):
        sys.argv = args
        self.action = None
        self.from_ = None
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
        self.in_ = sys.stdin
        self.out = sys.stdout
        self.debug = False

        usage = """

  'cdent' is the compiler for the C'Dent portable module programming language.

        command line usage:  cdent [options]"""

        optparser = OptionParser(usage=usage)

        # --compile
        def cb_action(option, opt, value, oparser):
            self.action = opt[2:]
        optparser.add_option(
            "--compile",
            action="callback", callback=cb_action,
            help="compile from input format to output format (required)"
        )

        # --in=FILE
        def cb_in(option, opt, value, oparser):
            if not os.path.exists(value):
                raise OptionError(value + ' file does not exist', opt)
            self.in_ = file(value, 'r')
            m = re.match(r'.*?\.((?:\cd?\.)?\w+)$', value)
            if m:
                optparser.rargs.append('--from=' + m.groups()[0])
        optparser.add_option(
            "--in", type="string",
            action="callback", callback=cb_in,
            help="input file -- default is stdin",
        )

        # --out=FILE
        def cb_out(option, opt, value, oparser):
            self.out = file(value, 'w')
            m = re.match(r'.*?\.((?:\cd?\.)?\w+)$', value)
            if m:
                optparser.rargs.append('--to=' + m.groups()[0])
        optparser.add_option(
            "--out", type="string",
            action="callback", callback=cb_out,
            help="output file -- default is stdout",
        )

        # --from=LANG_ID
        def cb_from(option, opt, value, oparser):
            if self.action != 'compile':
                raise OptionError('--from used before --compile')
            class_ = cdent.compiler.class_(value)
            exec(
                "from cdent.parser." +
                class_ +
                " import Parser, ParseError"
            ) in globals()
            self.parser = Parser()
            self.from_ = value
        optparser.add_option(
            "--from", type="choice",
            # choices=['cd.json', 'cd.xml', 'cd.yaml', 'cd.js', 'cd.pm6', 'cd.py'],
            choices=['cd.yaml', 'cd.js', 'cd.pm6', 'cd.py'],
            action="callback", callback=cb_from,
            help="input format -- autodetected from input file name"
        )

        # --to=LANG_ID
        def cb_to(option, opt, value, oparser):
            if self.action != 'compile':
                raise OptionError('--to used before --compile')
            class_ = cdent.compiler.class_(value)
            exec "from cdent.emitter." + class_ + " import Emitter" in globals()
            self.emitter = Emitter()
            self.to = value
        optparser.add_option(
            "--to", type="choice",
            choices=['cd.json', 'cd.xml', 'cd.yaml', 'java', 'js', 'php', 'pm', 'pm6', 'py', 'py3', 'rb'],
            action="callback", callback=cb_to,
            help="output format -- autodetected from output file name"
        )

        # --emit-info
        def cb_emit_info(option, opt, value, oparser):
            self.emit_header = bool(int(value))
            self.emit_trailer = bool(int(value))
        optparser.add_option(
            "--emit-info", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_emit_info,
            help="emit info header & trailer -- defaults listed below",
        )

        # --emit-header
        def cb_emit_header(option, opt, value, oparser):
            self.emit_header = bool(int(value))
        optparser.add_option(
            "--emit-header", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_emit_header,
            help="emit info header -- default is on",
        )

        # --emit-trailer
        def cb_emit_trailer(option, opt, value, oparser):
            self.emit_trailer = bool(int(value))
        optparser.add_option(
            "--emit-trailer", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_emit_trailer,
            help="emit info trailer -- default is off",
        )

        # --debug
        def cb_debug(option, opt, value, oparser):
            self.debug = bool(int(value))
        optparser.add_option(
            "--debug", type="choice",
            choices=['0', '1'], metavar="0|1",
            action="callback", callback=cb_debug,
            help="print compilation debugging info -- default is off",
        )

        # --version
        def cb_version(option, opt, value, oparser):
            self.action = 'version'
        optparser.add_option(
            "-v", "--version",
            action="callback", callback=cb_version,
            help="print cdent version"
        )

        # parse options
        (opts, args) = optparser.parse_args()

        # move options
        if self.emitter:
            if self.emit_header != None:
                self.emitter.emit_header = self.emit_header
            if self.emit_trailer != None:
                self.emitter.emit_trailer = self.emit_trailer

        # validate options
        try:
            if (args):
                raise OptionError('extra arguments found', args)
            if (not self.action):
                raise OptionError('is required', '--compile | --help | --version')
            if self.action == 'compile':
                if (not self.from_):
                    raise OptionError('is required', '--from')
                if (not self.to):
                    raise OptionError('is required', '--to')
        except OptionError, err:
            sys.stderr.write(str(err) + '\n\n')
            # optparse can't write this to stderr :(
            optparser.print_help()
            sys.exit(1)

    def main(self):
        getattr(self, self.action)()

    def compile(self):
        self.parser.debug = self.debug
        self.parser.open(self.in_)
        try:
            ast = self.parser.parse()
        except ParseError, err:
            sys.stderr.write(str(err))
            sys.exit(1)
        self.emitter.open(self.out)
        self.emitter.emit_ast(ast)

    def version(self):
        print """
The C'Dent portable module programming language.
Copyright (c) 2010, Ingy dot Net
See: http://www.cdent.org

C'Dent may be copied only under the terms of the BSD license.
See: http://cdent.org/license/

C'Dent Language Specification: version 0.0.1
See: http://cdent.org/specification/

C'Dent Compiler Implementation: cdent.py, version %s 
See: http://pypi.python.org/pypi/cdent/

C'Dent IRC channel: #cdent on irc.freenode.net
""" % cdent.compiler.version()
