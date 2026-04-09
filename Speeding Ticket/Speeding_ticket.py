openfile = open("speeding.in", 'r')
print(openfile)
readfile = openfile.readlines()
for i in range(len(readfile)):
    readfile[i] = readfile[i].strip()
    readfile[i] = readfile[i].split()
    #print(readfile[i])
for i in range(len(readfile)):
    for j in range(0,2):
        print(readfile[i][j])