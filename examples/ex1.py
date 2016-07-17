import random
import networkx as nx
from itertools import product
from networkx_prolog import to_prolog

if __name__ == '__main__':

    G = nx.Graph()

    for i, j in product(range(10), range(10)):
        r = random.random() 
        if r> 0.5:
            G.add_edge(i, j, weight=r)

    to_prolog(G, 'test_graph.pl')
