"""
C'Dent Perl6 parser grammar module.
"""

from cdent.grammar import *

class Grammar():
    def __init__(self):
        self.__dict__.update(
{ 'BlankLine': Re({'_': '[\\ \\t]*\\r?\\n'}),
  'Class': All({'_': [Rule({'_': 'ClassSignature'}), Rule({'_': 'ClassBody'}), Rule({'_': 'ClassEnd'})]}),
  'ClassBody': All({'_': [Indent({}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Method'}), Any({'x': '*', '_': [Rule({'_': 'Method'}), Rule({'_': 'Comment'})]}), Undent({})]}),
  'ClassEnd': Re({'_': '\\}\\r?\\n'}),
  'ClassSignature': Re({'_': 'class[\\ \\t]+(\\w+)[\\ \\t]+\\{\\r?\\n'}),
  'Comment': Any({'_': [Rule({'_': 'LineComment'}), Rule({'_': 'BlankLine'})]}),
  'DocComment': All({'_': [Rule({'_': 'DocCommentBegin'}), All({'x': '*', '_': [Rule({'!': True, '_': 'DocCommentEnd'}), Rule({'_': 'DocCommentLine'})]}), Rule({'_': 'DocCommentEnd'})]}),
  'DocCommentBegin': Re({'_': '#{3}\\r?\\n'}),
  'DocCommentEnd': Re({'_': '#{3}\\r?\\n'}),
  'DocCommentLine': Re({'_': '#[\\ \\t]?(.*\\r?\\n)'}),
  'Ending': Re({'_': ''}),
  'Id': Re({'_': '\\w+'}),
  'IncludeCDent': Re({'_': 'use CDent;'}),
  'Line': Re({'_': '.*\\r?\\n'}),
  'LineComment': Re({'_': '#(.*\\r?\\n)'}),
  'Method': All({'_': [Rule({'_': 'MethodSignature'}), Rule({'_': 'MethodBody'}), Rule({'_': 'MethodEnd'})]}),
  'MethodBody': All({'_': [Indent({}), Rule({'_': 'Statement'}), Any({'x': '*', '_': [Rule({'_': 'Statement'}), Rule({'_': 'Comment'})]}), Undent({})]}),
  'MethodEnd': Re({'_': '\\}\\r?\\n'}),
  'MethodSignature': Re({'_': 'method[\\ \\t]+(\\w+)[\\ \\t]+\\{\\r?\\n'}),
  'Module': All({'_': [Rule({'x': '?', '_': 'DocComment'}), Rule({'x': '*', '_': 'Comment'}), Rule({'x': '?', '_': 'IncludeCDent'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Class'}), Any({'x': '*', '_': [Rule({'_': 'Class'}), Rule({'_': 'Comment'})]}), Rule({'_': 'Ending'}), Rule({'x': '*', '_': 'Comment'})]}),
  'PrintLn': Re({'_': 'say[\\ \\t]+(.+);\\r?\\n'}),
  'Statement': Any({'_': [Rule({'_': 'PrintLn'}), Rule({'_': 'Comment'})]}),
  'line_comment_start': Re({'_': '#'})}
)

