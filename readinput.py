def getGraph(path):
    graph = {}
    with open(path, 'r') as f:
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

<<<<<<< HEAD
x=getGraph()
print(x)
types1=[type(k) for k in x.keys()]
print(types1)
#print(getGraph())
=======
>>>>>>> 8faf33e45553b1002187d25bc4e7f518fb5d6550

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

print(readHospitals())
