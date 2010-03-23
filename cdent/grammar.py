"""\
Grammar classes
"""

class Base():
    def __init__(self, dict):
        self.__dict__.update(dict)

class And(Base):
    pass

class Or(Base):
    pass

class Not(Base):
    pass
