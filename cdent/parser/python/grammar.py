"""
C'Dent Python parser grammar module.
"""

from cdent.grammar import *

class Grammar():
    def __init__(self):
        self.__dict__.update(
{ 'ALL': Re({'_': '[\\s\\S]'}),
  'AN': Re({'_': '[A-Za-z0-9]'}),
  'ANY': Re({'_': '.'}),
  'BR': Re({'_': '\\n'}),
  'BS': Re({'_': '\\\\'}),
  'BlankLine': Re({'_': '[\\ \\t]*\\r?\\n'}),
  'CN': Re({'_': ':'}),
  'Class': All({'_': [Rule({'_': 'ClassSignatureLine'}), Rule({'_': 'ClassBody'})]}),
  'ClassSignatureLine': Re({'_': 'class[\\ \\t]+\\w+\\(\\w+?\\):\\r?\\n'}),
  'Comment': Any({'_': [Rule({'_': 'LineComment'}), Rule({'_': 'BlankLine'})]}),
  'DOT': Re({'_': '\\.'}),
  'DQ': Re({'_': '"'}),
  'DS': Re({'_': '\\$'}),
  'DocComment': All({'_': [Rule({'_': 'DocCommentBegin'}), Rule({'x': '*', '_': 'DocCommentLine'}), Rule({'_': 'DocCommentEnd'})]}),
  'DocCommentBegin': Re({'_': '""""\\\\[\\ \\t]*\\r?\\n'}),
  'DocCommentEnd': Re({'_': '""""[\\ \\t]*\\r?\\n'}),
  'DocCommentLine': Re({'_': '(.*\\r?\\n)'}),
  'EOL': Re({'_': '\\r?\\n'}),
  'Ending': Re({'_': ''}),
  'Id': Re({'_': '\\w+'}),
  'IncludeCDent': Re({'_': 'from cdent import *'}),
  'LC': Re({'_': '[a-z]'}),
  'LP': Re({'_': '\\('}),
  'Line': Re({'_': '.*\\r?\\n'}),
  'LineComment': Re({'_': '#(.*\\r?\\n)'}),
  'Module': All({'_': [Rule({'_': 'DocComment'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'IncludeCDent'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Class'}), Any({'x': '*', '_': [Rule({'_': 'Class'}), Rule({'_': 'Comment'})]}), Rule({'_': 'Ending'}), Rule({'x': '*', '_': 'Comments'})]}),
  'NUM': Re({'_': '[0-9]'}),
  'OCT': Re({'_': '#'}),
  'RP': Re({'_': '\\)'}),
  'SQ': Re({'_': "'"}),
  'TQ': Re({'_': '""""'}),
  'UC': Re({'_': '[A-Z]'}),
  'WC': Re({'_': '\\w'}),
  'WS': Re({'_': '[\\ \\t]'}),
  'line_comment_start': Re({'_': '#'})}
)

