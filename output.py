def output(num, dist, list):
    f = open("C:\\Users\\lynnm\\Desktop\\AY20-21\\sem 1\\CZ2001 algo\\proj 2 code\\output.txt","a")
    f.write("start node: ")
    f.write(str(num))
    f.write(", shortest dist: ")
    f.write(str(dist))
    f.write(", shortest path: ")
    f.write("[")
    for i in range(len(list)):
        f.write(str(list[i]))
        if i<len(list)-1:
            f.write(",")
    f.write("]\n")
    f.close()