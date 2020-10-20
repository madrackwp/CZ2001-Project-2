# adjacencyList will be a dictionary
from readinput import readhospitals


def BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList):
    queue = {}
    visited = [False] * noOfNodes
    result = {}
    currentDistance = 0
    # If the current node is a hospital, need to add the hospital along with the distance

    # This create an entry in the dictionary where the startingNode is the key, and the values are the key and the distance
    queue[startingNode] = [startingNode, currentDistance]
    visited[startingNode] = True
    while (queue):
        # This gets the first key in the queue and then removes it
        res = list(queue.keys())[0]
        currentNode = queue.pop(res)
        nodeValue = currentNode[0]
        currentDistance = currentNode[1]
        if nodeValue in hospitalList:  # This checks if the current node is a hospital
            # Stores the currentNode which is where the hospital, as the key, and the distance as the value
            result[nodeValue] = currentDistance

        # checks for all neighbours of the current node
        for neighbour in adjacencyList[nodeValue]:
            if(visited[neighbour] == False):
                visited[neighbour] = True
                queue[neighbour] = [neighbour, currentDistance+1]
        # BUG currentdistance should not increase until the we move on from the nxt layer
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
hospitalList = readhospitals()

BFS(adjacencyList, 0, 9, 1, hospitalList)
