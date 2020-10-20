# adjacencyList will be a dictionary
from ReadInput import readHospitals


def BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList):
    queue = {}
    visited = [False] * noOfNodes
    result = {}
    currentDistance = 0
    # If the current node is a hospital, need to add the hospital along with the distance
    currentPath = [startingNode]
    # This create an entry in the dictionary where the startingNode is the key, and the values are the key and the distance
    queue[startingNode] = [startingNode, currentDistance, currentPath]
    visited[startingNode] = True
    while (queue):
        # This gets the first key in the queue and then removes it
        res = list(queue.keys())[0]
        currentNode = queue.pop(res)
        nodeValue = currentNode[0]
        currentDistance = currentNode[1]
        nodePath = currentNode[2]
        if nodeValue in hospitalList:  # This checks if the current node is a hospital
            # Stores the currentNode which is where the hospital, as the key, and the distance as the value
            result[nodeValue] = [currentDistance, nodePath]

        # checks for all neighbours of the current node
        for neighbour in adjacencyList[nodeValue]:
            if(visited[neighbour] == False):
                visited[neighbour] = True
                # BUG IS HERE: APPENDING ALL NEIGHBOURS================================
                nodePath.append(neighbour)
                # ======================================================================
                queue[neighbour] = [neighbour, currentDistance+1, nodePath]
        currentDistance += 1

    print(result)


adjacencyList = {0: [1, 2, 3, 4, 5],
                 1: [4],
                 2: [],
                 3: [5],
                 4: [6],
                 5: [6, 7],
                 6: [],
                 7: [8],
                 8: []}
# hospitalList = [4, 6, 8]
hospitalList = readHospitals()

BFS(adjacencyList, 0, 9, 1, hospitalList)
