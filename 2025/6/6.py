import datetime

with open('6.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

def part1():
    part1data = [line.split() for line in dataset]
    answertotal = 0
    for x in range(0,len(part1data[0])):
        op = part1data[len(part1data)-1][x]
        val1 = int(part1data[0][x])
        for y in range(1,len(part1data)-1):
            val = part1data[y][x]
            if op == "+":
                val1 = val1 + int(val)
            elif op == "*":
                val1 = val1 * int(val)
            else:
                temp = input("not * or +",op)
        
        answertotal = answertotal + val1
    return answertotal    

t0 = datetime.datetime.now()
answer = part1()
print("part 1",answer)
t1 = datetime.datetime.now()

td1 = t1-t0
print("Part 1 time: {} ms".format(td1.microseconds/1000))


