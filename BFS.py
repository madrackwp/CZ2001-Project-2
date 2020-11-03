from ReadInput import readHospitals
from WriteToOP import outputWrite


def BFS(adjacencyList, startingNode, requiredHospitals, hospitalList, outputPath):
    queue = [[startingNode]]
    visited = []

    while (queue):
        path = queue.pop(0)
        currentNode = path[-1]

        if (currentNode not in visited):
            try:
                neighbours = adjacencyList[currentNode]
                for neighbour in neighbours:
                    newPath = list(path)
                    newPath.append(neighbour)
                    queue.append(newPath)
            except:
                pass  # currentNode has no neighbours!

        visited.append(currentNode)

        if (currentNode in hospitalList):
            # Print the output into the outputPath
            outputWrite(startingNode, len(path)-1, path, outputPath)
            requiredHospitals -= 1  # Reduce the number of required hospitals
            hospitalList.remove(currentNode)

        if (requiredHospitals == 0):  # This will trigger when the no. of hospitals needed has been met
            break
