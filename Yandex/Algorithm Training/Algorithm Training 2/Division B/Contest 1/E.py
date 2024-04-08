import math

fin = open('input.txt')
d = int(fin.readline())
x, y = [int(x) for x in fin.readline().split()]

def answer(d, x, y):
    if (0 <= x <= d) and (0 <= y <= d-x):
        return 0
    else:
        dist1 = math.sqrt(x*x+y*y) # A
        dist2 = math.sqrt(abs(x-d)*abs(x-d)+y*y) # B
        dist3 = math.sqrt(x*x+abs(y-d)*abs(y-d)) # C

        if dist1 <= dist2 and dist1 <= dist3:
            return 1
        elif dist2 <= dist1 and dist2 <= dist3:
            return 2
        elif dist3 <= dist1 and dist3 <= dist2:
            return 3
    
print(answer(d, x, y))