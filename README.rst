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


C'Dent is Copyright (c) 2010, Ingy dot Net

C'Dent is licensed under the New BSD License. See the LICENSE file.
