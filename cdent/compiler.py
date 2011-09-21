"""\
Meta class for the C'Dent compiler
"""

import cdent

id_to_language = {
    'as':       'ActionScript',
    'coffee':   "CoffeeScript",
    'cd':       "C'Dent",
    'cpp':      'C++',
    'go':       'Go',
    'java':     'Java',
    'js':       'JavaScript',
    'nqp':      'NQP (Not Quite Perl)',
    'php':      'PHP',
    'pir':      'PIR',
    'pm':       'Perl',
    'pm6':      'Perl 6',
    'py':       'Python',
    'py3':      'Python 3',
    'pyc':      'Python bytecode',
    'rb':       'Ruby',
    'scala':    'Scala',
    'tcl':      'Tcl',
    'vala':     'Vala',
}

id_to_class = {
    'as':       'actionscript',
    'cd.yaml':  'cdent.yaml',
    'cd.xml':   'cdent.xml',
    'cd.json':  'cdent.json',
    'cd.js':    'javascript',
    'cd.pir':   'pir',
    'cd.pm6':   'perl6',
    'cd.py':    'python',
    'coffee':   'coffee',
    'cpp':      'cpp',
    'go':       'go',
    'java':     'java',
    'js':       'javascript',
    'nqp':      'nqp',
    'php':      'php',
    'pir':      'pir',
    'pm':       'perl',
    'pm6':      'perl6',
    'py':       'python',
    'py3':      'python3',
    'pyc':      'pyc',
    'rb':       'ruby',
    'scala':    'scala',
    'tcl':      'tcl',
    'vala':     'vala',
}

def language(id):
    return id_to_language[id]

def class_(id):
    return id_to_class[id]

def version():
    return cdent.__version__
