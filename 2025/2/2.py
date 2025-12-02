import math
with open('2.test') as f:
    dataset = f.readline()

ranges = dataset.split(",")
answer = 0
for range in ranges:
    pidmin,pidmax = range.split("-")
    if len(pidmin) > 1:
        pidminleft = pidmin[0:math.floor(len(pidmin)/2)]
    else:
        pidminleft = "1"
        
    testval = int(pidminleft + pidminleft)
    while testval <= int(pidmax):
        if len(str(testval)) >= len(str(pidmin)):
            if testval >= int(pidmin) and testval <= int(pidmax):
                answer = answer + testval
        pidminleft = str(int(pidminleft) + 1)
        testval = int(pidminleft + pidminleft)

print("answer is",answer)
#31839939611 is too low