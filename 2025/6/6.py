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
        answertotal = answertotal + val1
    return answertotal    

def part2():
    answertotal = 0
    count = 1 #these next two lines counter for the blank vertical line in all the subsequent math
    vals = [""]
    for x in range(len(dataset[0])-1,-1,-1):
        vals.append("")
        for y in range(0,len(dataset)):
            vals[count] = vals[count] + dataset[y][x]
            if dataset[y][x] == "+" or dataset[y][x] == "*":
                answertotal = answertotal + dosum(vals,dataset[y][x])
                vals = []
                count = -1
        count = count + 1
    return answertotal
            
def dosum(vals,op):
    val1 = int(vals[1]) #ignore the first blank column
    for x in range(2,len(vals)):
        if op == "+":
            val1 = val1 + int(vals[x][:-1])
        elif op == "*":
            val1 = val1 * int(vals[x][:-1])
    return val1
        

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

