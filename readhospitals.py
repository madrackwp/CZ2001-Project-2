def readhospitals():
    hospitals=[]
    with open('C:\\Users\\Jonathan Chang\\Documents\\Algo\\CZ2001-Project-2\\hospitals.txt','r') as f:
        for line in f:
            try:
                n=int(line)
                hospitals.append(n)
            except ValueError:
                pass
    return hospitals

print(readhospitals())
