with open('1.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

start = 50
zeros = 0
for row in dataset:
    dir = row[0]
    count = int(row[1:])
    if dir == "L":
        start = start - count
        while start < 0:
            start = start + 100
    else:
        start = start + count
        while start >= 100:
            start = start - 100
    if start == 0:
        zeros = zeros + 1

print("answer is ", zeros)
    

