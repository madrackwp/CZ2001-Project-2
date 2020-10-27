# adjacencyList will be a dictionary
from ReadInput import readHospitals

# def BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList):
#     queue = {}
#     visited = [False] * noOfNodes
#     result = {}
#     currentDistance = 0
#     # If the current node is a hospital, need to add the hospital along with the distance
#     currentPath = []
#     # This create an entry in the dictionary where the startingNode is the key, and the values are the key and the distance
#     queue[startingNode] = [startingNode, currentDistance, currentPath]
#     visited[startingNode] = True  # Marks the first node as visited
#     while (queue):  # While the queue is not empty
#         # This gets the first key in the queue and then removes it
#         # Res is the index of first item that is in the object at the start of the queue
#         res = list(queue.keys())[0]
#         currentNode = queue.pop(res)
#         nodeValue = currentNode[0]
#         currentDistance = currentNode[1]
#         nodePath = currentNode[2]
#         nodePath.append(nodeValue)

#         # this current node must be stored somewhere
#         if nodeValue in hospitalList:  # This checks if the current node is a hospital
#             # Stores the currentNode which is where the hospital, as the key, and the distance as the value
#             result[nodeValue] = [currentDistance, nodePath]
#         # If the number of hospitals is met, break out of the loop
#         if len(result) == requiredHospitals:
#             break

#         # checks for all neighbours of the current node
#         for neighbour in adjacencyList[nodeValue]:
#             if(visited[neighbour] == False):
#                 visited[neighbour] = True
#                 # BUG IS HERE: APPENDING ALL NEIGHBOURS================================
#                 # nodePath.append(neighbour)
#                 # ======================================================================
#                 queue[neighbour] = [neighbour, currentDistance+1, nodePath]

#     print(result)


def BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList):
    queue = [[startingNode]]
    visited = []

    while (queue):  # While the queue is not empty
        path = queue.pop(0)
        currentNode = path[-1]

        # Check if the node has been visited
        if (currentNode not in visited):
            visited.append(currentNode)

            # get the neighbours of these nodes
            try:
                neighbours = adjacencyList[currentNode]
            except:
                print("THERE ARE NO NEIGHBOURS!")
                continue

            for neighbour in neighbours:
                if (neighbour in visited):
                    continue
                newPath = list(path)
                newPath.append(neighbour)
                queue.append(newPath)

                if (neighbour in hospitalList):
                    requiredHospitals -= 1
                    print("The shortest path is", newPath)
                    print("The length is", len(newPath))
                    print()
                    hospitalList.remove(neighbour)

                if (requiredHospitals == 0):
                    break


# Output needed for each node will the node number, the distance and the path
# adjacencyList = {0: [1, 2, 3, 4, 5],
#                  1: [4],
#                  2: [],
#                  3: [5],
#                  4: [6],
#                  5: [6, 7],
#                  6: [],
#                  7: [8],
#                  8: []}
# # hospitalList = [4, 6, 8]
# hospitalList = readHospitals()
# requiredHospitals = 2
# startingNode = 0
# noOfNodes = 9
# BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList)
