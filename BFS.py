# adjacencyList will be a dictionary


def BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList):
    queue = {}
    visited = [False] * noOfNodes
    result = {}
    currentDistance = 0
    # If the current node is a hospital, need to add the hospital along with the distance

    queue[startingNode] = currentDistance
    visited[startingNode] = True
    while (queue):
        currentNode = queue.pop(startingNode)
        if currentNode in hospitalList:  # This checks if the current node is a hospital
            result[currentNode] = currentDistance

        # checks for all neighbours of the current node
        for neighbour in adjacencyList[currentNode]:
            visited[neighbour] = True
            queue[neighbour] = currentDistance+1

    print(result)


adjacencyList = {1: [2, 3, 4, 5, 6],
                 2: [5],
                 3: [],
                 4: [6],
                 5: [7],
                 6: [7],
                 7: []}
hospitalList = [5, 7]

BFS(adjacencyList, 1, 7, 1, hospitalList)
