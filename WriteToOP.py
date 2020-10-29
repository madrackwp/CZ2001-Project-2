def outputWrite(num, dist, list, path):
    f = open(path, "a")
    f.write("start node: ")
    f.write(str(num))
    f.write(", shortest dist: ")
    f.write(str(dist))
    f.write(", shortest path: ")
    f.write("[")
    for i in range(len(list)):
        f.write(str(list[i]))
        if i < len(list)-1:
            f.write(",")
    f.write("]\n")
    f.close()

def wipeTextFile(path):
    file = open(path, "r+")
    file.truncate(0)
    file.close()
