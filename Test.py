from networkx.generators.random_graphs import erdos_renyi_graph


def generateRandGraph(n, p, path):

    g = erdos_renyi_graph(n, p)
    x = g.edges
    with open(path, 'w') as f:
        f.write('FROM TO:\n')
        for a_tuple in x:
            for item in a_tuple:
                f.write(str(item))
                f.write(' ')
            f.write('\n')
        f.close
    return g
