from networkx.generators.random_graphs import erdos_renyi_graph
import random


def generateRandGraph(n, p, path):
    g = erdos_renyi_graph(n, p)
    x = g.edges

    with open(path, 'w') as f:
        f.write('FROM TO:\n')
        for a_tuple in x:
            node1 = a_tuple[0]
            node2 = a_tuple[1]
            if random.random() > 0.5:
                f.write(str(node1))
                f.write(' ')
                f.write(str(node2))
                f.write('\n')
            if random.random() > 0.5:
                f.write(str(node2))
                f.write(' ')
                f.write(str(node1))
                f.write('\n')
        f.close
    return g


n = 10
p = 0.3

generateRandGraph(
    n, p, 'C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Paths\\randomGraph.txt')
