import datetime
import math

with open('9.in') as f:
    dataset = f.readlines()
    dataset = [list(map(int,line.rstrip('\n').split(","))) for line in dataset]

def part1():
    maxarea = 0
    for x in range(0,len(dataset)):
        for y in range (x+1,len(dataset)):
            thisarea = (abs(dataset[y][0] - dataset[x][0]) +1) * (abs(dataset[y][1] - dataset[x][1]) + 1)
            if thisarea > maxarea:
                maxarea = thisarea
    return maxarea


def part2():
    dataset.append([dataset[0][0],dataset[0][1]])
    ############
    ### generate edges into a set
    ############
    edgecoords = set()
    minx = maxx = dataset[0][0]
    miny = maxy = dataset[0][1]
    for x in range(0,len(dataset)-1):
        dir = 0
        part = 0
        if dataset[x][0] < dataset[x+1][0]:
            dir = 1
            if dataset[x+1][0] > maxx: maxx = dataset[x+1][0]
        elif dataset[x][0] > dataset[x+1][0]:
            dir = -1
            if dataset[x+1][0] < minx: minx = dataset[x+1][0]
        elif dataset[x][1] < dataset[x+1][1]:
            dir = 1
            part = 1
            if dataset[x+1][1] > maxy: maxy = dataset[x+1][1]
        else:
            dir = -1
            part = 1
            if dataset[x+1][1] < miny: miny = dataset[x+1][1]
        # print("from",dataset[x][part],"to",dataset[x+1][part]+dir,"in",dir)
        for cell in range(dataset[x][part],dataset[x+1][part]+dir,dir):
            if part == 0:
                edgecoords.add((cell,dataset[x][1]))
            else:
                edgecoords.add((dataset[x][0],cell))
    print("edge coordinates",len(edgecoords))
    
    ##############
    ## get all rectangles
    ##############
    rectangles = []
    for x in range(0,len(dataset)):
        for y in range (x+1,len(dataset)):
            minx = min(dataset[x][0],dataset[y][0])
            maxx = max(dataset[x][0],dataset[y][0])
            miny = min(dataset[x][1],dataset[y][1])
            maxy = max(dataset[x][1],dataset[y][1])
            width = maxx - minx +1
            height = maxy - miny + 1
            if width > 2 and height > 2:
                area = width*height
                v1 = (minx,miny)
                v2 = (maxx,miny)
                v3 = (maxx,maxy)
                v4 = (minx,maxy)
                rectangles.append([(v1,v2,v3,v4),area])
    rectangles.sort(key=lambda x: x[1], reverse=True)
    print("rectangles",len(rectangles))

    ###############
    ## check borderless rectangle for intersects (should be zero)
    ##############
    maxsize = 0
    for corners,area in rectangles:
        rectinsideedges = set()
        # print("doing",area)
        for x in range(corners[0][0]+1,corners[1][0]):
            rectinsideedges.add((x,corners[0][1]+1))
        if len(rectinsideedges.intersection(edgecoords)) > 0:
            continue
        for y in range(corners[1][1]+1,corners[2][1]):
            rectinsideedges.add((corners[1][0]-1,y))
        if len(rectinsideedges.intersection(edgecoords)) > 0:
            continue
        for x in range(corners[3][0]+1,corners[2][0]):
            rectinsideedges.add((x,corners[3][1]-1))
        if len(rectinsideedges.intersection(edgecoords)) > 0:
            continue
        for y in range(corners[0][1]+1,corners[3][1]):
            if (corners[0][0]+1,y) in edgecoords:
                hitwall = True
                continue
            rectinsideedges.add((corners[0][0]+1,y))
        # print(rectinsideedges)
        # rectcoords = set(rectinsideedges)
        # print(len(rectinsideedges),len(rectcoords),area,len(edgecoords))
        print(area, rectinsideedges.intersection(edgecoords))
        if len(rectinsideedges.intersection(edgecoords)) == 0:
            if area > maxsize:
                return area

def part2a():
    dataset.append([dataset[0][0],dataset[0][1]])
    #########
    # get edges
    #########

    horizontals = []
    verticals = []
    for x in range(0,len(dataset)-1):
        if dataset[x][0] == dataset[x+1][0]:
            verticals.append(((dataset[x][0],min(dataset[x][1],dataset[x+1][1])),(dataset[x][0],max(dataset[x][1],dataset[x+1][1]))))
        else:
            horizontals.append(((min(dataset[x][0],dataset[x+1][0]),dataset[x][1]),(max(dataset[x][0],dataset[x+1][0]),dataset[x][1])))

    print("horizontals",horizontals)
    print("verticals",verticals)
    ##########
    # get rectangles
    ##########
    rectangles = []
    for x in range(0,len(dataset)):
        for y in range (x+1,len(dataset)):
            minx = min(dataset[x][0],dataset[y][0])
            maxx = max(dataset[x][0],dataset[y][0])
            miny = min(dataset[x][1],dataset[y][1])
            maxy = max(dataset[x][1],dataset[y][1])
            width = maxx - minx +1
            height = maxy - miny + 1
            if width > 2 and height > 2:
                area = width*height
                v1 = (minx,miny) #  v1 ---> v2
                v2 = (maxx,miny) #. ^.      |
                v3 = (maxx,maxy) #. |.      \/
                v4 = (minx,maxy) #. v4 <--- v3
                rectangles.append([(v1,v2,v3,v4),area])
    rectangles.sort(key=lambda x: x[1], reverse=True)
    print("rectangles",len(rectangles))

    #############
    # per rectangle
    ###############
    for points,area in rectangles:
        rectmid = ((points[1][0]-points[0][0])/2,(points[2][1]-points[1][1])/2)
        # print("doing",points,area)
        problemfound = False
        for line in verticals:
            if problemfound:
                break
            for p in line:
                if (points[0][0] < p[0] and p[0] < points[1][0] and points[1][1] < p[1] and p[1] < points[2][1]):
                    problemfound = True
                    # print("point",p,"inside")
                    break
            if points[0][0] < line[0][0] < points[1][0]:
                if line[0][1] <= points[1][1] and line[1][1] >= points[2][1]:
                    problemfound = True
                    # print("line",line,"cuts the rect")
        if not problemfound: 
            windingnum = 0
            for line in horizontals:
                if problemfound:
                    break
                for p in line:
                    if (points[0][0] < p[0] and p[0] < points[1][0] and points[1][1] < p[1] and p[1] < points[2][1]):
                        problemfound = True
                        # print("point",p,"inside")
                        break
                if points[1][1] < line[0][1] < points[2][1]:
                    if line[0][0] <= points[0][0] and line[1][0] >= points[1][0]:
                        problemfound = True
                        # print("line",line,"cuts the rect")
                        break
                if line[0][1] > rectmid[1]:
                    if line[0][0] <= rectmid[0] < line[1][0]:
                        windingnum += 1
                    if line[0][0] > rectmid[0] >= line[1][0]:
                        windingnum -= 1
        if not problemfound:
            if windingnum == 0:
                True
                # print("mid",rectmid,"is outside")
            else:
                return area
            


        


t0 = datetime.datetime.now()
answer = part1()
print("part 1",answer)
t1 = datetime.datetime.now()
answer = part2a()
print("part 2",answer)
t2 = datetime.datetime.now()
answer = part2()
print("P2 slow",answer)
t3 = datetime.datetime.now()
td1 = t1-t0
td2 = t2-t1
td3 = t3-t2
print("Part 1 time: {} ms".format(td1.microseconds/1000))
print("Part 2 time: {} ms".format(td2.microseconds/1000))
print("P2 Slowwwww: {} days".format(td3.days))
print("P2 Slowwwww: {} s".format(td3.seconds))
print("P2 Slowwwww: {} ms".format(td3.microseconds/1000))