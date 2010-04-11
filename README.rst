C'Dent - A Portable Module Programming Language
-----------------------------------------------

C'Dent is a programming language that:

1) Is primarily intended to write portable OO modules. C'Dent modules
   are written once, and then compiled to equivalent port modules in any
   number of supported programming languages.
2) Has multiple input syntaxes. Including defined subsets of:
   - Perl and Perl 6
   - Python and Python 3000
   - Ruby
   - JavaScript
   - Java
3) Compiles to a Common'DENominaTor tree form known as C'Dent. C'Dent is
   an OO model that has the notions of modules, classes, methods, and
   expressions.
4) Emits C'Dent trees to several existing programming languages,
   including:
   - C'Dent - the compiled tree form serialized as YAML or XML
   - Perl and Perl 6
   - Python and Python 3000
   - Ruby
   - JavaScript
   - PHP
   - Java
   - Scala
   - C and C++
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

DEVELOPMENT STATUS
------------------

C'Dent can currently parse modules with a simplistic grammar of Module/Classes/Methods/Print/Comments to an AST form and generate equivalent output modules in many languages:

C'Dent can currently parse:

* Python
* JavaScript
* Perl 6
* C'Dent/YAML (a C'Dent AST in YAML form)

C'Dent can currently produce:

* Perl
* Perl 6
* Python
* Python 3
* PHP
* Ruby
* Java
* JavaScript
* C'Dent/YAML

Next Steps:

* Add variables and assignments
* Add type detection
* Add Ruby and Perl as input
* Add Scala and C++ as output
* Lots of other stuff

COMMUNITY
---------

Join #cdent on irc.freenode.net.

COPYRIGHT
---------

C'Dent is Copyright (c) 2010, Ingy dot Net

C'Dent is licensed under the New BSD License. See the LICENSE file.
