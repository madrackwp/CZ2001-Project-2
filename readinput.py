def getGraph():
    graph = {}
    with open('C:\\Users\\Jonathan Chang\\Documents\\Algo\\CZ2001-Project-2\\dummyGraph2.txt', 'r') as f:
        for line in f:
            node = line.split()
            graph.setdefault(node[0], []).append(node[1])
    delete = [i for i in graph if i.isnumeric() is False]
    for i in delete:
        del graph[i]
    for i in graph:
        i = int(i)
    return graph

print(getGraph())


def readHospitals():
    hospitals = []
    with open('C:\\Users\\Jonathan Chang\\Documents\\Algo\\CZ2001-Project-2\\hospitals.txt', 'r') as f:
        for line in f:
            try:
                n = int(line)
                hospitals.append(n)
            except ValueError:
                pass
    return hospitals

# print(readhospitals())
