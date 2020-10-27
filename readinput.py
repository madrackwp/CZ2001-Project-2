def getGraph(path):
    graph = {}
    with open(path, 'r') as f:
        for line in f:
            node = line.split()
            graph.setdefault(node[0], []).append(node[1])
    delete = [i for i in graph if i.isnumeric() is False]
    for i in delete:
        del graph[i]
    for i in graph:
        i = int(i)
    return graph


# print(getGraph())


def readHospitals(path):
    hospitals = []
    with open(path, 'r') as f:
        for line in f:
            try:
                hospitals.append(line)
            except ValueError:
                pass
    return hospitals

# print(readhospitals())
