with open('4.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
    dataset = [list(line) for line in dataset]

def part1():
    w = len(dataset[0])
    h = len(dataset)
    moveablerolls = set()
    for y in range(0,h):
        for x in range(0,w):
            if dataset[y][x] == "@":
                countofrolls = 0
                for b in range(y-1,y+2):
                    for a in range(x-1,x+2):
                        if b >= 0 and a >= 0 and b < h and a < w and not (b == y and a == x ):
                            if dataset[b][a] == '@': 
                                countofrolls = countofrolls + 1
                if countofrolls < 4:
                    moveablerolls.add((x,y))
    return moveablerolls

def part2():
    movedsome = True
    movedtotal = 0
    while movedsome:
        movedsome = False
        rolls = part1()
        if len(rolls) > 0:
            movedsome = True
            movedtotal = movedtotal + len(rolls)
            for paperroll in rolls:
                dataset[paperroll[1]][paperroll[0]] = "."
    return movedtotal


answer = part1()
print("part 1",len(answer))

answer = part2()
print("part 2",answer)