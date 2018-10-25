import hashlib
from itertools import izip
from Node import Node
from graphviz import Graph

class MerkleTree(object):
    def __init__(self):
        self.merkle_root = None

    # Iterate two elements at a time
    def pairwise(self, iterable):
        a = iter(iterable)
        return izip(a, a)

    def compute_merkle_root(self, string_array):
        assert len(string_array) % 2 == 0
        node_array = []
        # convert string array to node array
        for x in string_array:
            node_array.append(Node(x))

        result_array = self._compute_merkle_root_helper(node_array)
        merkle_root = result_array[0]
        self.merkle_root = merkle_root
        return merkle_root

    def _compute_merkle_root_helper(self, node_array):
        assert len(node_array) % 2 == 0
    
        result_array = []
        # x, y are node, their value is string
        for x, y in self.pairwise(node_array):
            # print "%s, %s" % (x, y)
            # print "compute " + x + ", " + y + "\n"
            parent_node = Node(hashlib.sha256(x.value + y.value).digest())
            parent_node.left = x
            parent_node.right = y
            result_array.append(parent_node)
        if len(result_array) == 1:
            return result_array
        else:
            return self._compute_merkle_root_helper(result_array)

    def assign_index(self):
        self.index = 0
        self._assign_index_helper(self.merkle_root)

    def _assign_index_helper(self, node):
        if node.left == None and node.right == None:
            node.index = self.index
            self.index += 1
        else:
            self._assign_index_helper(node.left)
            node.index = self.index
            self.index += 1
            self._assign_index_helper(node.right)
    
    def draw_tree(self):
        dot = Graph(comment = 'Merkle Tree')
        self._draw_tree_helper(dot, self.merkle_root)
        # print(dot.source)
        dot.render('test-output/merkle-tree.gv', view = True)

    def _draw_tree_helper(self, dot, node):
        dot.node(str(node.index), str(node.index))
        if node.left != None and node.right != None:
            dot.node(str(node.left.index), str(node.left.index))
            dot.node(str(node.right.index), str(node.right.index))
            dot.edge(str(node.index), str(node.left.index), constraint = 'true')
            dot.edge(str(node.index), str(node.right.index), constraint = 'true')
            self._draw_tree_helper(dot, node.left)
            self._draw_tree_helper(dot, node.right)
        
def main():
    merkle_tree = MerkleTree()
    merkle_tree.compute_merkle_root(["1", "2", "3", "5", "7", "0", "4", "8"])
    # Check if the node of the merkle tree contains the right value
    # The leave node contains the element from the string array
    # The internal node contains the intermediate hash result
    print merkle_tree.merkle_root.left.left.left.__repr__() == "1"
    print merkle_tree.merkle_root.right.left.right.__repr__() == "0"
    print merkle_tree.merkle_root.left.left.__repr__() == hashlib.sha256("12").digest()
    print merkle_tree.merkle_root.right.right.__repr__() == hashlib.sha256("48").digest()
    print merkle_tree.merkle_root.left.__repr__() == hashlib.sha256(hashlib.sha256("12").digest() + hashlib.sha256("35").digest()).digest()
    merkle_tree.assign_index()
    # Check if the merkle tree index is assigned correctly
    print merkle_tree.merkle_root.index
    print merkle_tree.merkle_root.right.right.index
    print merkle_tree.merkle_root.left.right.left.index
    merkle_tree.draw_tree()

if __name__ == '__main__':
    main()