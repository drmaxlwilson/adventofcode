import datetime
import math

with open('8.in') as f:
    dataset = f.readlines()
    dataset = [tuple(map(int,line.rstrip('\n').split(","))) for line in dataset]
    dataset = sorted(dataset)
    # print(dataset)



def part1(connections = 10):
    distances = {}
    for i in range(0,len(dataset)):
        for j in range(i+1,len(dataset)):
            dist = math.sqrt((dataset[i][0]-dataset[j][0])**2 + (dataset[i][1]-dataset[j][1])**2 + (dataset[i][2]-dataset[j][2])**2)
            distances[(dataset[i],dataset[j])] = dist
    distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    # for key in distances.keys():
    #     print(key,distances[key])

    circuits = []
    for key in distances.keys():
        newcirc = set(key)
        for circ in circuits:
            if key[0] in circ or key[1] in circ:
                newcirc.update(set(circ))
                circuits.remove(circ)
        circuits.append(list(newcirc))
        connections -= 1
        if connections == 0:
            break
        
    circuits = sorted(circuits, key=len, reverse=True)
    return (len(circuits[0])*len(circuits[1])*len(circuits[2]))

def part2():
    True

t0 = datetime.datetime.now()
answer = part1(1000)
print("part 1",answer)
t1 = datetime.datetime.now()
answer = part2()
print("part 2",answer)
t2 = datetime.datetime.now()

td1 = t1-t0
td2 = t2-t1
print("Part 1 time: {} ms".format(td1.microseconds/1000))
print("Part 1 time: {} ms".format(td2.microseconds/1000))