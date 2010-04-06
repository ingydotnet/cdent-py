"""\
Perl code emitter for C'Dent
"""

from __future__ import absolute_import

from cdent.emitter import Emitter as Base

class Emitter(Base):
    LANGUAGE_ID = 'pm'

    def emit_includecdent(self, includecdent): 
        self.writeln('use CDent::Run;')

    def emit_class(self, class_): 
        name = class_.name
        self.writeln('package %s;' % name)
        self.writeln('use Moose;')
        self.writeln()
        self.emit(class_.has)
        self.writeln()
        self.writeln('1;')

    def emit_method(self, method): 
        name = method.name
        self.writeln('sub %s {' % name)
        self.writeln('    my $self = shift;')
        self.emit(method.has, indent=True)
        self.writeln('}')

    def emit_println(self, println): 
        self.write('print ', indent=True)
        self.emit(println.args)
        self.writeln(', "\\n";', indent=False)

    def emit_return(self, ret): 
        self.writeln('return;')
