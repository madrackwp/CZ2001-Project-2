from BFS import *
from GraphGenerator import *
from ReadInput import *
from WriteToOP import wipeTextFile

# generateRandGraph(
# 10, 0.3, 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\roadNet-TX.txt\\randoGraph')

# =======================================PATHS TO BE CHANGED=======================================
# graphPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\roadNet-TX.txt\\randoGraph'
graphPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\roadNet-TX.txt'
opPath = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Outputs\\Output.txt"
hopsitalPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\hospitals.txt'
# =================================================================================================

# =======================================VARS TO BE CHANGED========================================

adjacencyList = getGraph(graphPath)
wipeTextFile(opPath)
for startingNode in adjacencyList:
    hospitalList = readHospitals(hopsitalPath)
    BFS(adjacencyList, startingNode, 1, hospitalList, opPath)
