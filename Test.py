from networkx.generators.random_graphs import erdos_renyi_graph

n = 6
p = 0.4
g = erdos_renyi_graph(n, p)

print(g.nodes)

print(g.edges)
