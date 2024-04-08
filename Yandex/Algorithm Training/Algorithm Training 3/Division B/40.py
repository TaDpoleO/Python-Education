from collections import defaultdict, deque

fin = open('input.txt')
N = int(fin.readline())
M = int(fin.readline())

stations, color_of_station = [[] for i in range(N)], defaultdict(set)
for i in range(M):
    num, *points = [int(x)-1 for x in fin.readline().split()]
    num = num+1
    
    for point in points:
        color_of_station[point].add(i)

        for other_point in points:
            if point != other_point: stations[point].append(other_point)
    
start, end = [int(x)-1 for x in fin.readline().split()]

def getMinPath(stations, start, end, color_of_station):
    if start == end: return 0
    
    stack, distance = deque(), defaultdict(lambda: float('inf'))
    distance[start] = 0

    for color in color_of_station[start]:
        stack.append((start, color, 0))

    while stack:
        curr_station, curr_color, changes = stack.pop()

        for next_station in stations[curr_station]:
            if next_station == end:                
                if curr_color in color_of_station[next_station]:
                    distance[next_station] = min(changes, distance[next_station])
                else:
                    distance[next_station] = min(changes+1, distance[next_station])
            
            if curr_color in color_of_station[next_station]:
                if changes < distance[next_station]:
                    distance[next_station] = changes
                    stack.appendleft((next_station, curr_color, changes))
            else:
                for next_color in (color_of_station[next_station] & color_of_station[curr_station]):
                    if changes+1 < distance[next_station]:
                        distance[next_station] = changes+1
                        stack.appendleft((next_station, next_color, changes+1))

    if distance[end] < float('inf'):
        return distance[end]
    else:        
        return -1

print(getMinPath(stations, start, end, color_of_station))