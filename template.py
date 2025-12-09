import datetime

with open('FILENAME') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

def part1():
    True

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
print("Part 2 time: {} ms".format(td2.microseconds/1000))