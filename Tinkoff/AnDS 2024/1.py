import sys
import math

fin = sys.stdin
# fin = open('input.txt')

coordinates = [(0, 0)]*3
for i in range(3):
    x, y = [float(x) for x in fin.readline().split()]
    coordinates[i] = (x, y)

def getScore(x, y):
    R = math.sqrt(x*x+y*y)

    if R > 1:
        return 0
    elif R > 0.8:
        return 1
    elif R > 0.1:
        return 2
    else:
        return 3

scores = 0
for i in range(3):
    scores += getScore(*coordinates[i])

print(scores)