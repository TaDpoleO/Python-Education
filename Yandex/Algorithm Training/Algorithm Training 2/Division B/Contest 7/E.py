import math

def getPolarRectangleSquare(radius1, radius2, angle1, angle2):
    circle1 = math.pi*radius1*radius1
    circle2 = math.pi*radius2*radius2

    delta_angle = angle2-angle1
    if delta_angle < 0: delta_angle += math.pi*2

    return abs(circle2-circle1)*delta_angle/(math.pi*2)

def answer(max_r1, min_r2, events):
    if max_r1 > min_r2 or math.isclose(max_r1, min_r2): return 0

    events.sort()
    all_segments = len(events)//2

    curr_started, curr_started_count, last_start = set(), 0, 0
    for event in events:
        curr_angle, event_type, id = event

        if event_type == TYPE_START:
            curr_started_count += 1
            curr_started.add(id)
            last_start = curr_angle
        elif event_type == TYPE_END:
            if id in curr_started:
                curr_started_count -= 1
    curr_started.clear()
    
    sum_square = 0
    for event in events:
        curr_angle, event_type, _ = event

        if event_type == TYPE_START:
            curr_started_count += 1
            last_start = curr_angle
        elif event_type == TYPE_END:
            if curr_started_count == all_segments:
                sum_square += getPolarRectangleSquare(max_r1, min_r2, last_start, curr_angle)

            curr_started_count -= 1

    return sum_square

TYPE_START = 10    
TYPE_END = -10

fin = open('input.txt')
N = int(fin.readline())
events = [0]*2*N

max_r1, min_r2 = float('-inf'), float('inf')

for i in range(N):
    curr_r1, curr_r2, curr_angle1, curr_angle2 = [float(x) for x in fin.readline().split()]

    max_r1 = max(max_r1, curr_r1)
    min_r2 = min(min_r2, curr_r2)

    events[2*i] = (curr_angle1, TYPE_START, i)
    events[2*i+1] = (curr_angle2, TYPE_END, i)

print(answer(max_r1, min_r2, events))