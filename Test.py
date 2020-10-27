from networkx.generators.random_graphs import erdos_renyi_graph

n = 6
p = 0.4
g = erdos_renyi_graph(n, p)
x= g.edges
with open('C:\\Users\\Jonathan Chang\\Documents\\Algo\\CZ2001-Project-2\\dummyGraph2.txt', 'w') as f:
    f.write('FROM TO:\n')
    for a_tuple in x:
        for item in a_tuple:
            f.write(str(item))
            f.write(' ')
        f.write('\n')
    f.close

print(g.nodes)
print(g.edges)
