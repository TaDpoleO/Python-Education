import math
from collections import defaultdict

def isTriangle(p1, p2, p3):
    side1 = getSide(p1, p2)
    side2 = getSide(p1, p3)
    side3 = getSide(p2, p3)

    if (side1+side2 < side3) or math.isclose(side1+side2, side3): return False
    if (side1+side3 < side2) or math.isclose(side1+side3, side2): return False
    if (side2+side3 < side1) or math.isclose(side2+side3, side1): return False

    return True

def getSide(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

fin = open('input.txt')
N = int(fin.readline())

points = [(0, 0)]*N
for i in range(N):
    x, y = [int(x) for x in fin.readline().split()]
    points[i] = (x, y)

count = 0
for i in range(N):
    sides = defaultdict(list)    
    point1 = points[i]
    for j in range(N):
        if i != j:
            point2 = points[j]
            side = getSide(point1, point2)
            sides[side].append((point1, point2))

    for side, segments in sides.items():
        for i in range(len(segments)):
            point0, point1 = segments[i]
            for j in range(i+1, len(segments)):
                _, point2 = segments[j]        

                if isTriangle(point0, point1, point2): count += 1

print(count)