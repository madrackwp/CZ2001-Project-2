def getGraph():
    graph = {}
    with open('C:\\Users\\Jonathan Chang\\Documents\\Algo\\CZ2001-Project-2\\roadNet-TX.txt\\roadNet1000.txt', 'r') as f:
        for line in f:
                node = line.split()
                graph.setdefault(node[0],[]).append(node[1])
    delete = [i for i in graph if i.isnumeric() is False]
    for i in delete:
        del graph[i]
    for i in graph:
        i = int(i)
    return graph 

print(getGraph())