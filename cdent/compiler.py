"""\
Meta class for the C'Dent compiler
"""

from cdent import __version__

id_to_language = {
    'cd':   "C'Dent",
    'cpp':  'C++',
    'go':   'Go',
    'java': 'Java',
    'js':   'JavaScript',
    'php':  'PHP',
    'pm':   'Perl',
    'pm6':  'Perl 6',
    'py':   'Python',
    'py3':  'Python 3',
    'rb':   'Ruby',
}

id_to_class = {
    'cd.yaml': 'cdent.yaml',
    'cd.xml':  'cdent.xml',
    'cd.json': 'cdent.json',
    'cd.js': 'javascript',
    'cd.pm6': 'perl6',
    'cd.py': 'python',
    'cpp':  'cpp',
    'go':   'go',
    'java': 'java',
    'js':   'javascript',
    'php':  'php',
    'pm':   'perl',
    'pm6':  'perl6',
    'py':   'python',
    'py3':  'python3',
    'rb':   'ruby',
}

def language(id):
    return id_to_language[id]

def class_(id):
    return id_to_class[id]

def version():
    return __version__
