def getGraph(graphPath):
    graph = {}
    with open(graphPath, 'r') as f:
        for line in f:
            node = line.split()
            try:
                graph.setdefault(int(node[0]), []).append(int(node[1]))
            except ValueError:
                pass
    return graph


def readHospitals(hospitalPath):
    hospitals = []
    with open(hospitalPath, 'r') as f:
        for line in f:
            try:
                n = int(line)
                hospitals.append(n)
            except ValueError:
                pass
    return hospitals
