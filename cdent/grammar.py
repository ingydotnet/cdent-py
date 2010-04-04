"""\
Grammar classes
"""

class Base():
    def __init__(self, dict):
        self.__dict__.update(dict)
    def __repr__(obj):
        return '%s(%s)' % (obj.__class__.__name__, repr(obj.__dict__))

class All(Base): pass
class Any(Base): pass
class Re(Base): pass
class Rule(Base): pass
class Indent(Base): pass
class Undent(Base): pass
