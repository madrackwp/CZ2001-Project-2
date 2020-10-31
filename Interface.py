from BFS import *
from GraphGenerator import *
from readinput import *
from WriteToOP import wipeTextFile


# =======================================PATHS TO BE CHANGED=======================================
<<<<<<< HEAD
graphPath = 'C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Paths\\testGraph.txt'
opPath = "C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Outputs\\Output.txt"
hospitalPath = 'C:\\Users\\user\\Desktop\\Repositories\\CZ2001-Project-2\\Paths\\hospitals.txt'
=======
graphPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\randomGraph.txt'
opPath = "C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Outputs\\Output.txt"
hopsitalPath = 'C:\\Users\\madra\\Documents\\CZ2001\\CZ2001-Project-2\\Paths\\hospitals.txt'
>>>>>>> 8096ec824c4e63d7bd5ea5b7a58b90aa9bd3a9ab
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
