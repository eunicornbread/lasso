from Client import Client
from Server import Server
from graphviz import Graph
from graphviz import Digraph

def main():
    
    test = ["1", "2", "3", "4"]
    client = Client(test)
    server = Server()
    # print client.data
    server.store(client.data)
    client.store_merkle_root(server.compute_root())
    # start from zero index
    
    for idx, val in enumerate(test):
        assert(client.query(idx, server))
        print "Passed: element " + str(idx)

    """
    dot = Digraph(comment = 'The Round Table')
    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere')
    dot.node('L', 'Sir Lancelot')
    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint = 'false')
    print(dot.source)
    dot.render('test-output/round-table.gv', view = True)
    """
    
if __name__ == '__main__':
    main()
