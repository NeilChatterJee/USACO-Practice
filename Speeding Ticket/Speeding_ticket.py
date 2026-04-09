openfile = open("speeding.in", 'r')
print(openfile)
readfile = openfile.readlines()
for i in range(len(readfile)):
    readfile[i] = readfile[i].strip()
    readfile[i] = readfile[i].split()
    #print(readfile[i])
for i in range(len(readfile)):
    for j in range(0,2):
        readfile[i][j] = int(readfile[i][j])
        #print(readfile[i][j])
n = readfile[0][0]
m = readfile[0][1]
for i in range(1, 100):
    if i <= readfile[1][0]:
        if readfile[1][1] < readfile[4][1]:
            speed_disparity1 = readfile[4][1] - readfile[1][1]
print(speed_disparity1)

