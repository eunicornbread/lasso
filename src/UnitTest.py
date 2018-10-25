import unittest
import hashlib
from MerkleTree import MerkleTree
from Server import Server
from Client import Client

class TestMerkleTree(unittest.TestCase):
    def setUp(self):
        data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        self.merkle_tree = MerkleTree()
        self.merkle_tree.compute_merkle_root(data)
        self.server = Server()
        self.server.store(data)
        self.server.compute_root()
        self.client = Client(data)

    def test_tree_index(self):
        self.merkle_tree.assign_index()
        self.merkle_tree.draw_tree()
        self.assertEqual(self.merkle_tree.merkle_root.index, 15)
        self.assertEqual(self.merkle_tree.merkle_root.left.index, 7)
        self.assertEqual(self.merkle_tree.merkle_root.right.index, 23)
    
    def test_tree_compute(self):
        self.assertEqual(self.merkle_tree.merkle_root.left.left.left.value, hashlib.sha256("12").digest())
        self.assertEqual(self.merkle_tree.merkle_root.left.left.right.value, hashlib.sha256("34").digest())
        self.assertEqual(self.merkle_tree.merkle_root.right.left.right.value, hashlib.sha256("1112").digest())
        self.assertEqual(self.merkle_tree.merkle_root.left.right.value, hashlib.sha256(hashlib.sha256("56").digest() + hashlib.sha256("78").digest()).digest())
        self.assertEqual(self.merkle_tree.merkle_root.right.right.value, hashlib.sha256(hashlib.sha256("1314").digest() + hashlib.sha256("1516").digest()).digest())

    def test_server_compute(self):
        # proof1 index: 1 4 6 11 23
        proof1 = self.server.compute_proof(3)
        self.assertEqual(proof1[0].index, 1)
        self.assertEqual(proof1[1].index, 4)
        self.assertEqual(proof1[3].index, 11)
        # proof2 index: 7 19 25 28 30
        proof2 = self.server.compute_proof(14)
        self.assertEqual(proof2[2].index, 25)
        self.assertEqual(proof2[4].index, 30)
        self.assertEqual(proof2[0].index, 7)
        # proof3 index: 3 9 12 14 23
        proof3 = self.server.compute_proof(7)
        self.assertEqual(proof3[1].index, 9)
        self.assertEqual(proof3[3].index, 14)
        self.assertEqual(proof3[4].index, 23)

    def test_client_compute(self):
        computation1 = self.client.compute(2, self.server.compute_proof(0))
        self.assertEqual(computation1.__repr__(), self.merkle_tree.merkle_root.__repr__())
        computation2 = self.client.compute(2, self.server.compute_proof(5))
        self.assertEqual(computation2.__repr__(), self.merkle_tree.merkle_root.__repr__())
        computation3 = self.client.compute(2, self.server.compute_proof(12))
        self.assertEqual(computation3.__repr__(), self.merkle_tree.merkle_root.__repr__())

if __name__ == '__main__':
    unittest.main()