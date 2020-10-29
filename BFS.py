from readinput import readHospitals
from WriteToOP import outputWrite


def BFS(adjacencyList, startingNode, requiredHospitals, hospitalList, outputPath):
    queue = [[startingNode]]
    visited = []

    while (queue):  # While the queue is not empty
        path = queue.pop(0)
        currentNode = path[-1]

        # Checks if the current node is the hospital
        if (currentNode in hospitalList):
            requiredHospitals -= 1
            outputWrite(currentNode, 0, [], outputPath)
        else:
             # Check if the node has been visited
            if (currentNode not in visited):
                visited.append(currentNode)
                # get the neighbours of these nodes
                try:
                    neighbours = adjacencyList[currentNode]
                except:
                    continue

                for neighbour in neighbours:
                    if (neighbour in visited):
                        continue
                    newPath = list(path)
                    newPath.append(neighbour)
                    queue.append(newPath)

                    if (neighbour in hospitalList):
                        requiredHospitals -= 1
                        hospitalList.remove(neighbour)
                        outputWrite(startingNode, len(newPath) -
                                    1, newPath, outputPath)
                    if (requiredHospitals == 0):
                        break
        if (requiredHospitals == 0):
            break
