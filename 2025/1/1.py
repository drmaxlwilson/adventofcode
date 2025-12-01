with open('1.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
DEBUG = True
start = 50
zerostotal = 0

for row in dataset:
    zeros = 0
    dir = row[0]
    count = int(row[1:])
    if dir == "L":
        was = start
        if DEBUG: print(start,"-",count)
        start = start - count
        while start < 0:
            start = start + 100
            zeros = zeros + 1
        if start == 0:
            zeros = zeros + 1
        if DEBUG: print("=", start)
        if was == 0:
            zeros = zeros -1
        if DEBUG: print(zeros, "x 0\n----\n")
    else:
        if DEBUG: print(start,"+",count)
        start = start + count   
        while start >= 100:
            start = start - 100
            zeros = zeros + 1
        if DEBUG: print("=", start)     
        if DEBUG: print(zeros, "x 0\n----\n")
    zerostotal = zerostotal + zeros

print("answer is ", zerostotal)