from BFS import *
from GraphGenerator import *
from ReadInput import *
from WriteToOP import wipeTextFile


# =======================================PATHS TO BE CHANGED=======================================
graphPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\testGraph.txt'
opPath = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Outputs\\Output.txt"
hospitalPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\hospitals.txt'
# =================================================================================================

# =======================================VARS TO BE CHANGED========================================
requiredHospitals = 2
# =================================================================================================

# =====================DO NOT CHANGE ANYTHING AT THE BOTTOM OF THIS LINE===========================
adjacencyList = getGraph(graphPath)
wipeTextFile(opPath)
for startingNode in adjacencyList:
    hospitalList = readHospitals(hospitalPath)
    BFS(adjacencyList, startingNode, requiredHospitals, hospitalList, opPath)
