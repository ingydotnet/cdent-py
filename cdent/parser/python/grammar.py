"""
C'Dent Python parser grammar module.
"""

from cdent.parser.base.grammar import Grammar as Base

class Grammar(Base):
    def __init__(self):
        super(Grammar, self).__init__()
        self.__dict__.update({'DocCommentBegin': '/$TQ$BS$WS*$EOL/', 'DocCommentEnd': '/$TQ$WS*$EOL/', 'line_comment_start': '#', 'IncludeCDent': '/from cdent import */', 'DocCommentLine': '/($ANY*$EOL)/', 'TQ': '""""', 'ClassSignatureLine': '/class$WS+$Id$OP$Id?$CP$CN$EOL/', 'Class': ['ClassSignatureLine', 'ClassBody']})
