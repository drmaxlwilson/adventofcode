import datetime

with open('7.in') as f:
    dataset = f.readlines()
    dataset = [list(line.rstrip('\n')) for line in dataset]

def part1():
    count_hits = 0
    for y in range(0,len(dataset)-1):
        for x in range(0,len(dataset[0])):
            if dataset[y][x] == "S":
                # print("found S at",x,y)
                dataset[y+1][x] = "|"
            elif dataset[y][x] == "^":
                # print("found ^ at",x,y)
                dataset[y+1][x-1] = "|"
                dataset[y+1][x+1] = "|"
            elif dataset[y][x] == "|":
                if dataset[y+1][x] == "^":
                    # print("split at",x,y)
                    count_hits = count_hits + 1
                else:
                    dataset[y+1][x] = "|"
    return count_hits

def part2():
    for y in range(0,len(dataset)-1):
        for x in range(0,len(dataset[0])):
            if dataset[y][x] == "S":
                dataset[y+1][x] = "1"
            elif dataset[y][x] == "^":
                if dataset[y+1][x-1] == "|":
                    dataset[y+1][x-1] = "0"
                if dataset[y+1][x+1] == "|":
                    dataset[y+1][x+1] = "0"
                if dataset[y-1][x] == ".":
                    dataset[y-1][x] = "0"
                dataset[y+1][x-1] = str(int(dataset[y+1][x-1]) + int(dataset[y-1][x]))
                dataset[y+1][x+1] = str(int(dataset[y+1][x+1]) + int(dataset[y-1][x]))
            elif dataset[y][x] == "|":
                dataset[y][x] = dataset[y-1][x]
                if dataset[y+1][x] == "|":
                    dataset[y+1][x] = "0"
                # print("found one")
                dataset[y+1][x] = str(int(dataset[y+1][x]) + int(dataset[y][x]))
        # print("".join(dataset[y]))
        # temp = input()
    result = 0
    for i in range(0,len(dataset[0])):
        if dataset[len(dataset)-1][i] != ".":
            result += int(dataset[len(dataset)-1][i])
    return result

def printgrid():
    for row in dataset:
       print("".join(row))

t0 = datetime.datetime.now()
answer = part1()
print("part 1",answer)
printgrid()
t1 = datetime.datetime.now()
answer = part2()
print("part 2",answer)
t2 = datetime.datetime.now()

td1 = t1-t0
td2 = t2-t1
print("Part 1 time: {} ms".format(td1.microseconds/1000))
print("Part 1 time: {} ms".format(td2.microseconds/1000))