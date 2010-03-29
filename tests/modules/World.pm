# C'Dent generated Perl module.
# C'Dent is Copyright (c) 2010, Ingy dot Net. All rights reserved.
###
# This is World class :)
###

use CDent::Run;

package World;
use Moose;

sub greet {
    my $self = shift;
    print "Hello, world", "\n";
    return;
}

1;
