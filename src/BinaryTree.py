class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

class Tree(object):
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)

    def add(self, value):
        if(self.root == None):
            self.root = Node(value)
        else:
            self._add_helper(value, self.root)
            
    def _add_helper(self, value, node):
        if(value < node.value):
            if(node.left == None):
                node.left = Node(value)
            else:
                self._add_helper(value, node.left)
        else:
            if(node.right == None):
                node.right = Node(value)
            else:
                self._add_helper(value, node.right)

    def count_node(self):
        return self._count_node_helper(self.root)

    def _count_node_helper(self, node):
        if(node == None):
            return 0
        else:
            return 1 + self._count_node_helper(node.left) + self._count_node_helper(node.right)

    def has_node(self, value):
        return self._has_node_helper(value, self.root)

    # Instead of checking every single node in the tree, a better way is to compare
    # the value and decide which node to call - to be implemented
    def _has_node_helper(self, value, node):
        if(node == None):
            return False
        elif(node.value == value):
            return True
        else:
            return self._has_node_helper(value, node.left) or self._has_node_helper(value, node.right)

    def print_inorder(self):
        return self._print_inorder_helper(self.root)

    def _print_inorder_helper(self, node):
        if(node == None):
            return ""
        return self._print_inorder_helper(node.left) + str(node.value) + " " + self._print_inorder_helper(node.right)

    def min_value(self):
        return self._min_value_helper(self.root)

    def _min_value_helper(self, node):
        if node.left == None:
            return node.value
        return self._min_value_helper(node.left)

    def count_leaf(self):
        return self._count_leaf_helper(self.root)

    def _count_leaf_helper(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 1
        return self._count_leaf_helper(node.left) + self._count_leaf_helper(node.right)

    def node_sum(self):
        return self._node_sum_helper(self.root)

    def _node_sum_helper(self, node):
        if node == None:
            return 0
        return node.value + self._node_sum_helper(node.left) + self._node_sum_helper(node.right)

def main():
    tree = Tree()
    tree.add(6)
    tree.add(8)
    tree.add(2)
    tree.add(0)
    tree.add(-1)
    tree.add(5)
    print ">> The value of the root node is " + tree.__repr__()
    print ">> The number of node in the tree is " + str(tree.count_node())
    print ">> The tree contains 8: " + str(tree.has_node(8))
    print ">> The tree contains 9: " + str(tree.has_node(9))
    print ">> Print the tree in order: " + tree.print_inorder()
    print ">> The minimun value of the tree is: " + str(tree.min_value())
    print ">> The number of leaves in the tree is " + str(tree.count_leaf())
    print ">> The sum of all the nodes in the tree is " + str(tree.node_sum())

if __name__ == '__main__':
    main()