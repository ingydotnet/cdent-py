"""
C'Dent Python parser grammar module.
"""

from cdent.grammar import *

class Grammar():
    def __init__(self):
        self.__dict__.update(
{ 'BlankLine': Re({'_': '[\\ \\t]*\\r?\\n'}),
  'Class': All({'_': [Rule({'_': 'ClassSignatureLine'}), Rule({'_': 'ClassBody'})]}),
  'ClassSignatureLine': Re({'_': 'class[\\ \\t]+\\w+\\(\\w+?\\):\\r?\\n'}),
  'Comment': Any({'_': [Rule({'_': 'LineComment'}), Rule({'_': 'BlankLine'})]}),
  'DocComment': All({'_': [Rule({'_': 'DocCommentBegin'}), Rule({'_': 'DocCommentLine'}), All({'_': [Not({'_': Rule({'_': 'DocCommentEnd'})}), Rule({'_': 'DocCommentLine'})]}), Rule({'_': 'DocCommentEnd'})]}),
  'DocCommentBegin': Re({'_': '"""\\\\[\\ \\t]*\\r?\\n'}),
  'DocCommentEnd': Re({'_': '"""[\\ \\t]*\\r?\\n'}),
  'DocCommentLine': Re({'_': '(.*\\r?\\n)'}),
  'Ending': Re({'_': ''}),
  'Id': Re({'_': '\\w+'}),
  'IncludeCDent': Re({'_': 'from cdent import \\*'}),
  'Line': Re({'_': '.*\\r?\\n'}),
  'LineComment': Re({'_': '#(.*\\r?\\n)'}),
  'Module': All({'_': [Rule({'_': 'DocComment'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'IncludeCDent'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Class'}), Any({'x': '*', '_': [Rule({'_': 'Class'}), Rule({'_': 'Comment'})]}), Rule({'_': 'Ending'}), Rule({'x': '*', '_': 'Comments'})]}),
  'line_comment_start': Re({'_': '#'})}
)

