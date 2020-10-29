from BFS import *
from Test import *
from ReadInput import *

# generateRandGraph(
#     10, 0.3, 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\roadNet-TX.txt\\randoGraph')

path = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\roadNet-TX.txt\\roadNet1000.txt'
adjacencyList = getGraph(
    'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\roadNet-TX.txt\\randoGraph')

opPath = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Outputs\\Output.txt"

hospitalList = readHospitals(
    'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\hospitals.txt')
noOfNodes = len(adjacencyList)
startingNode = 0
requiredHospitals = 2

BFS(adjacencyList, startingNode, noOfNodes, requiredHospitals, hospitalList)


# Get all potential nodes within the graphs
# Iterate through all of them and add them to the graph
