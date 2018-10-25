from MerkleTree import MerkleTree

class Server(object):
    def __init__(self):
        self.data = None
        self.merkle_tree = MerkleTree()

    def store(self, data):
        self.data = data

    def compute_proof(self, index):
        self.merkle_tree.assign_index()
        self.proof = []
        self._compute_proof_helper(index * 2, self.merkle_tree.merkle_root)
        return self.proof

    def _compute_proof_helper(self, index, node):
        if index < node.index:
            self.insert(node.right)
            self._compute_proof_helper(index, node.left)
        elif index > node.index:
            self.insert(node.left)
            self._compute_proof_helper(index, node.right)
        else:
            self.insert(node)

    def insert(self, node):
        idx = 0
        for val in self.proof:
            if node.index < val.index:
                break
            else:
                idx += 1
        self.proof.insert(idx, node)

    def compute_root(self):
        return self.merkle_tree.compute_merkle_root(self.data)

def main():
    server = Server()
    server.store(["1", "2", "3", "5", "7", "0", "4", "8"])
    merkle_root = server.compute_root()
    # The 7th element in the array with the index of 14 in the tree
    proof = server.compute_proof(2)
    for val in proof:
        print val.index

if __name__ == '__main__':
    main()
