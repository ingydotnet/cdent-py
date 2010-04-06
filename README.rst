C'Dent - A Portable Module Programming Language
-----------------------------------------------

C'Dent is a programming language that:

1) Is primarily intended to write portable OO modules. C'Dent modules
   are written once, and then compiled to equivalent port modules in any
   number of supported programming languages.
2) Has multiple input syntaxes. Including defined subsets of:
   - Perl
   - Python
   - Ruby
   - JavaScript
   - Java
3) Compiles to a Common'DENominaTor tree form known as C'Dent. C'Dent is
   an OO model that has the notions of modules, classes, methods, and
   expressions.
4) Emits C'Dent trees to several existing programming languages,
   including:
   - C'Dent - the compiled tree form serialized as YAML or XML
   - Perl
   - Python
   - Ruby
   - JavaScript
   - PHP
   - Java
   - Perl 6
   - Python 3
   - C++
   - CIL (.NET Common Intermediate Language)
   - PIR (Parrot Intermediate Runtime)
5) Uses static implicit typing to assign types to all objects at
   compile time, and throw syntax errors for type conflicts. Strong
   typing is required to generate equivalent code in the various
   emitted port languages.

INSTALLATION
------------

Currently the best way to install C'Dent is to get the source code and install
it like so::

    > git clone git://github.com/ingydotnet/cdent.git
    > cd cdent
    > sudo setup.py install

USAGE
-----

After you install C'Dent, you will have a `cdent` compiler in your Unix path.
Try running this command::

    cdent --help

You'll need a program written in C'Dent. There are some in your C'Dent
repository clone. One example is `tests/modules/world.cd.py` which looks like
this::

    """\
    This is World class :)
    """

    class World():
        def greet(self):
            print "Hello, world"

You can compile to Ruby with this command::

    cdent --compile --in=tests/modules/world.cd.py --to=rb

Which produces::

    # *** DO NOT EDIT ***  This is a C'Dent generated Ruby module.
    ###
    # This is World class :)
    ###

    class World
        def greet
            puts("Hello, world")
        end
    end

You can compile it to many other languages by changing the value of `--to=`.

COPYRIGHT
---------

C'Dent is Copyright (c) 2010, Ingy dot Net

C'Dent is licensed under the New BSD License. See the LICENSE file.
