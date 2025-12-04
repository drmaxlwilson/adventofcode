with open('3.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

def part1():
    answer = 0
    for bank in dataset:
        # print(bank)
        bestpair = [0,0]
        bestpair[0] = int(bank[0])
        bestpair[1] = int(bank[1])
        for battery in bank[2:]:
            if bestpair[1] > bestpair[0]:
                bestpair[0] = bestpair[1]
                bestpair[1] = 0
            if int(battery) > bestpair[1]:
                bestpair[1] = int(battery)
        answer = answer + int(str(bestpair[0])+str(bestpair[1]))

    print("answer is",answer)

def part2(numbatteries):
    answer = 0
    for bank in dataset:
        bestset = bank[0:numbatteries]
        bank = bank[numbatteries:]
        for i in range(0, len(bank)):
            battery = bank[i]
            for x in range(0,len(bestset)-1):
                if int(bestset[x]) < int(bestset[x+1]):
                    bestset = bestset[0:x] + bestset[x+1:] + "0"
                    break
            if int(battery) > int(bestset[numbatteries-1]):
                bestset = bestset[:-1] + battery
        answer = answer + int(bestset)

    print("answer is",answer)

print("part 1:")
part1()
print("part 2 with 12:")
part2(12)
print("part 2 with 2:")
part2(2)