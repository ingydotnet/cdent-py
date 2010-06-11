"""
C'Dent Pir parser grammar module.
"""

from cdent.grammar import *

class Grammar():
    def __init__(self):
        self.__dict__.update(
{ 'BlankLine': Re({'_': '[\\ \\t]*\\r?\\n'}),
  'Class': All({'_': [Rule({'_': 'ClassStart'}), Rule({'_': 'ClassBody'}), Rule({'_': 'ClassEnd'})]}),
  'ClassBody': All({'_': [Indent({}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Method'}), Any({'x': '*', '_': [Rule({'_': 'Method'}), Rule({'_': 'Comment'})]})]}),
  'ClassEnd': Re({'_': ''}),
  'ClassStart': Re({'_': '.namespace[\\ \\t]+\\["(\\w+)"\\]\\r?\\n'}),
  'Comment': Any({'_': [Rule({'_': 'LineComment'}), Rule({'_': 'BlankLine'})]}),
  'DocComment': All({'_': [Rule({'_': 'DocCommentBegin'}), All({'x': '*', '_': [Rule({'!': True, '_': 'DocCommentEnd'}), Rule({'_': 'DocCommentLine'})]}), Rule({'_': 'DocCommentEnd'})]}),
  'DocCommentBegin': Re({'_': '#{3}\\r?\\n'}),
  'DocCommentEnd': Re({'_': '#{3}\\r?\\n'}),
  'DocCommentLine': Re({'_': '#[\\ \\t]?(.*\\r?\\n)'}),
  'Id': Re({'_': '\\w+'}),
  'IncludeCDent': Re({'_': 'use CDent;'}),
  'Line': Re({'_': '.*\\r?\\n'}),
  'LineComment': Re({'_': '#(.*\\r?\\n)'}),
  'Method': All({'_': [Rule({'_': 'MethodStart'}), Rule({'_': 'MethodBody'}), Rule({'_': 'MethodEnd'})]}),
  'MethodBody': All({'_': [Indent({}), Rule({'_': 'Statement'}), Any({'x': '*', '_': [Rule({'_': 'Statement'}), Rule({'_': 'Comment'})]}), Undent({})]}),
  'MethodEnd': Re({'_': '.end\\r?\\n'}),
  'MethodStart': Re({'_': '.method[\\ \\t]+(\\w+)\\r?\\n'}),
  'Module': All({'_': [Rule({'_': 'ModuleStart'}), Rule({'x': '?', '_': 'DocComment'}), Rule({'x': '*', '_': 'Comment'}), Rule({'x': '?', '_': 'IncludeCDent'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Class'}), Any({'x': '*', '_': [Rule({'_': 'Class'}), Rule({'_': 'Comment'})]}), Rule({'_': 'ModuleEnd'}), Rule({'x': '*', '_': 'Comment'})]}),
  'ModuleEnd': Re({'_': ''}),
  'ModuleStart': Re({'_': ''}),
  'PrintLn': Re({'_': 'say[\\ \\t]+(.+)\\r?\\n'}),
  'Statement': Any({'_': [Rule({'_': 'PrintLn'}), Rule({'_': 'Comment'})]}),
  'line_comment_start': Re({'_': '#'})}
)

