import math

fin = open('input.txt')
x0, y0, x1, y1 = [int(x) for x in fin.readline().split()]

def сartesianToPolar(x, y):
    R = math.sqrt(x*x+y*y)

    if x > 0 and y >= 0:
        angle = math.atan(y/x)
    elif x > 0 and y < 0:
        angle = math.atan(y/x)+2*math.pi
    elif x < 0:
        angle = math.atan(y/x)+math.pi
    elif x == 0 and y > 0:
        angle = math.pi/2
    elif x == 0 and y < 0:
        angle = 3*math.pi/2
    elif x == 0 and y == 0:
        angle = None

    return R, angle

def answer(x0, y0, x1, y1):
    if x0 == y0 == 0: return сartesianToPolar(x1, y1)[0]
    if x1 == y1 == 0: return сartesianToPolar(x0, y0)[0]
    if (x0 == x1) and (y0 == y1): return 0

    R0, angle0 = сartesianToPolar(x0, y0)
    R1, angle1 = сartesianToPolar(x1, y1)
    
    options = [R0+R1]
    if math.isclose(R0, R1):
        max_angle = max(angle1, angle0)
        min_angle = min(angle1, angle0)
        delta_angle = min(max_angle-min_angle, 2*math.pi-max_angle+min_angle)

        arc_length = R0*delta_angle
        options.append(arc_length)
    elif R0 < R1:
        max_angle = max(angle1, angle0)
        min_angle = min(angle1, angle0)
        delta_angle = min(max_angle-min_angle, 2*math.pi-max_angle+min_angle)

        arc_length = R0*delta_angle
        options.append(arc_length+R1-R0)
    elif R0 > R1:
        max_angle = max(angle1, angle0)
        min_angle = min(angle1, angle0)
        delta_angle = min(max_angle-min_angle, 2*math.pi-max_angle+min_angle)

        arc_length = R1*delta_angle
        options.append(arc_length+R0-R1)

    return min(options)

print(answer(x0, y0, x1, y1))