import hashlib
from Server import Server
from Node import Node

class Client(object):
    def __init__(self, string_array):
        self.data = string_array
        self.merkle_root = None

    def store(self, data, server):
        pass

    def store_merkle_root(self, merkle_root):
        self.merkle_root = merkle_root
        # print "merkle root: " + str(merkle_root.__repr__())

    def query(self, index, server):
        proof = server.compute_proof(index) # get the proof from the server
        
        """
        print "proof: "
        for i in proof:
            print i.index
        """
        # print "start computing"
        result = self.compute(2, proof) # compute the merkle root from the proof
        # print "result: " + result.__repr__()
        # Note: result == self.merkle_root returns false because the two node have different children
        # even though they have the same value
        return result.__repr__() == self.merkle_root.__repr__() # compare the two merkle root

    def compute(self, distance, proof):
        if len(proof) == 1:
             # print "final: " + str(proof[0].index)
            return proof[0]
        # print "distance: " + str(distance)
        i = 0
        while i < len(proof) - 1:
            # print "loop i: " + str(i)
            if abs(proof[i].index - proof[i + 1].index) == distance:
                break
            else:
                i += 1
        # print "i: " + str(i)
        node = Node(hashlib.sha256(proof[i].value + proof[i + 1].value).digest())
        node.index = (proof[i].index + proof[i + 1].index) / 2
        # print "new index: " + str(node.index)
        del proof[i]
        del proof[i]
        proof.insert(i, node)
        return self.compute(distance * 2, proof)
        
    def verify(self, proof):
        return 1

def main():
    data = ["1", "2", "3", "5", "7", "0", "4", "8"]
    server = Server()
    server.store(data)
    client = Client(data)
    client.store_merkle_root(server.compute_root())
    for idx, value in enumerate(data):
        print "element " + str(idx) + ": " + str(client.query(idx, server))

if __name__ == '__main__':
    main()