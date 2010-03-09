"""\
Meta class for C'Dent
"""

version = '0.01'

id_to_language = {
    'cd':   "C'Dent",
    'cpp':  'C++',
    'java': 'Java',
    'js':   'JavaScript',
    'php':  'PHP',
    'pm':   'Perl',
    'pm6':  'Perl 6',
    'py':   'Python',
    'py3':  'Python 3',
    'rb':   'Ruby',
}

def language(id):
    return id_to_language[id]
