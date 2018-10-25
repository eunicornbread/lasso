class Node(object):
    def __init__(self, value):
        self.value = value
        self.index = 0
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)
