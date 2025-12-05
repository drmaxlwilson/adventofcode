with open('5.test') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

ranges = []
ingredients = []

def process():
    doingranges = True
    for row in dataset:
        if row == "":
            doingranges = False
        # print(row,len(row))
        if doingranges:
            left,right = row.split("-")
            ranges.append([int(left),int(right)])
        else:
            if row != "":
                ingredients.append(int(row))    
    ranges.sort()


def part1():
    countoffresh = 0
    for i in ingredients:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                countoffresh = countoffresh + 1
                break
    return countoffresh

#def part2():


process()
answer = part1()
print("part 1",answer)