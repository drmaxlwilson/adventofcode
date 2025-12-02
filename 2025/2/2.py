import math
with open('2.in') as f:
    dataset = f.readline()

ranges = dataset.split(",")
answer = 0
for range in ranges:
    # print("doing range",range)
    pidmin,pidmax = range.split("-")
    pidminleft = 1
    found = [] #used so that we dont find 1111 because of 1x4 and 11x2

    #for all numbers where at least doubling it is <= the length of the range maximum
    while (len(str(pidminleft))*2 <= len(pidmax)):
        testval = str(pidminleft)
        #for all versions of that number up until its too long (1, 11, 111, 1111)
        while len(testval) < len(pidmax):
            #add a dup (1, 11, 111, 1111) and make a it a number for testing
            testval = int(testval + str(pidminleft))
            #if not aleady found and in range
            if testval not in found and testval >= int(pidmin) and testval <= int(pidmax):
                answer = answer + testval
                found.append(testval)
                # print("found",testval)
            #make str again for next copy (1, 11, 111, 1111)
            testval = str(testval)
        #next number
        pidminleft = pidminleft + 1
    # temp = input() #just so i can check the solution one range at a time
print("answer is",answer)