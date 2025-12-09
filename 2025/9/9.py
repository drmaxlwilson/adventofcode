import datetime
import math

with open('9.in') as f:
    dataset = f.readlines()
    dataset = [list(map(int,line.rstrip('\n').split(","))) for line in dataset]

def part1():
    maxarea = 0
    for x in range(0,len(dataset)):
        for y in range (x+1,len(dataset)):
            thisarea = (abs(dataset[y][0] - dataset[x][0]) +1) * (abs(dataset[y][1] - dataset[x][1]) + 1)
            if thisarea > maxarea:
                maxarea = thisarea
    return maxarea


def part2():
    True

t0 = datetime.datetime.now()
answer = part1()
print("part 1",answer)
t1 = datetime.datetime.now()
answer = part2()
print("part 2",answer)
t2 = datetime.datetime.now()

td1 = t1-t0
td2 = t2-t1
print("Part 1 time: {} ms".format(td1.microseconds/1000))
print("Part 1 time: {} ms".format(td2.microseconds/1000))