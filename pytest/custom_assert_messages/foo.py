
class Foo:
    def __init__(self, val):
        self.val = val
    
    def __eq__(self, other):
        return self.val == other.val

