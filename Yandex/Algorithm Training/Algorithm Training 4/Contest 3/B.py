import heapq
from collections import deque

def getNextPoints(graph, curr_point):
    res = []

    for i, dist in enumerate(graph[curr_point]):
        if (i != curr_point) and (dist >= 0): res.append((dist, i))

    return res

fin = open('input.txt')
N, start, end = [int(x) if i == 0 else int(x)-1 for i, x in enumerate(fin.readline().split())]
graph = [[int(x) for x in fin.readline().split()] for _ in range(N)]

visited = set()
distance = [float('inf')]*N
distance[start] = 0
prev_points = [-1]*N
prev_points[start] = start

stack = [(0, start)]
while stack:
    curr_dist, curr_point = heapq.heappop(stack)    

    if curr_point not in visited:
        for next_dist, next_point in getNextPoints(graph, curr_point):
            if curr_dist+next_dist < distance[next_point]:            
                distance[next_point] = curr_dist+next_dist
                prev_points[next_point] = curr_point
                heapq.heappush(stack, (curr_dist+next_dist, next_point))

    visited.add(curr_point)

if prev_points[end] != -1:
    path, curr_point = deque(), end
    while curr_point != start:
        path.appendleft(curr_point+1)
        curr_point = prev_points[curr_point]
    path.appendleft(start+1)
    print(*path)
else:
    print(-1)