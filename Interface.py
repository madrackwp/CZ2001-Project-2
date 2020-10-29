from BFS import *
from GraphGenerator import *
from readinput import *
from WriteToOP import wipeTextFile


# =======================================PATHS TO BE CHANGED=======================================
graphPath = 'C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Paths\\testGraph.txt'
opPath = "C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Outputs\\Output.txt"
hospitalPath = 'C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Paths\\hospitals.txt'
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
