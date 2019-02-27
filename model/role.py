__author__ = 'andrey'


class Role:

    def __init__(self, name=None, definition=None):
        self.name = name
        self.definition = definition

    def __repr__(self):
        return "%s:%s" % (self.name, self.definition)

    def __eq__(self, other):
        return self.name == other.name and self.definition == other.definition
