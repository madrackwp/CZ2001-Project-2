def getGraph():
    graph = {}
    with open('C:\\Users\\Jonathan Chang\\Documents\\Algo\\CZ2001-Project-2\\dummyGraph2.txt', 'r') as f:
        for line in f:
            node = line.split()
            try:
                graph.setdefault(int(node[0]), []).append(int(node[1]))
            except ValueError:
                pass
    #delete = [i for i in graph if i.isnumeric() is False]
    #for i in delete:
     #   del graph[i]
    #for i in graph:
   #     i = int(i)
    return graph

x=getGraph()
print(x)
types1=[type(k) for k in x.keys()]
print(types1)
#print(getGraph())


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

print(readHospitals())
