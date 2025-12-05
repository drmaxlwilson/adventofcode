
import datetime

with open('5.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

ranges = []
ingredients = []

def process():
    doingranges = True
    for row in dataset:
        if row == "":
            doingranges = False
        if doingranges:
            left,right = row.split("-")
            left = int(left)
            right = int(right)
            toremove = []
            for existingrange in ranges:
                if (left >= existingrange[0] and left <= existingrange[1]) or (right >= existingrange[0] and right <= existingrange[1]) or (left <= existingrange[0] and right >= existingrange[1]):
                    left = min(left,existingrange[0])
                    right = max(right,existingrange[1])
                    toremove.append(existingrange)
            for tr in toremove:
                ranges.remove(tr)
            ranges.append([left,right])
        else:
            if row != "":
                ingredients.append(int(row))    

def part1():
    countoffresh = 0
    for i in ingredients:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                countoffresh = countoffresh + 1
                break
    return countoffresh

def part2():
    totalIDs = 0
    for r in ranges:
        totalIDs = totalIDs + r[1]-r[0]+1
    return totalIDs

t0 = datetime.datetime.now()
process()
t1 = datetime.datetime.now()
answer = part1()
print("part 1",answer)
t2 = datetime.datetime.now()
answer = part2()
print("part 2",answer)
t3 = datetime.datetime.now()

td1 = t1-t0
td2 = t2-t1
td3 = t3-t2
print("Ingest time:{} ms".format(td1.microseconds/1000))
print("Part 1 time:{} ms".format(td2.microseconds/1000))
print("Part 2 time:{} ms".format(td3.microseconds/1000))