class Node(object):
    def __init__(self, value):
        self.node = value
        
    def __repr__(self):
        return str(self.node)

class Tree(object):
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.left) + str(self.node) + str(self.right)
