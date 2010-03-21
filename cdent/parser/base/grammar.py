"""
C'Dent Base parser grammar module.
"""

class Grammar(object):
    def __init__(self):
        super(Grammar, self).__init__()
        self.__dict__.update({'WC': '\\w', 'DocComment': ['DocCommentBegin', 'DocCommentLine*', 'DocCommentEnd'], 'DB': '"', 'EOL': '\\r?\\n', 'Ending': '//', 'WS': '[\\ \\t]', 'BR': '\\n', 'BS': '\\\\', 'AN': '[A-Za-z0-9]', 'OCT': '#', 'DOT': '\\.', 'Comment': '(LineComment|BlankLine)', 'ALL': '[\\s\\S]', 'LC': '[a-z]', 'SQ': "'", 'Module': ['DocComment', 'Comment*', 'IncludeCDent', 'Comment*', 'Class', '(Class|Comment)*', 'Ending', 'Comments*'], 'DS': '\\$', 'NUM': '[0-9]', 'LineComment': '/$line_comment_start($Line)/', 'ANY': '.', 'Line': '/$CHAR*$EOL/', 'BlankLine': '/$WS*$EOL/', 'UC': '[A-Z]'})
