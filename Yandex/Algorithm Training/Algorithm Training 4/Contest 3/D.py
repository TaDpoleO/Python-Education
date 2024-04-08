import heapq
from collections import defaultdict

def getNextPoints(graph, curr_time, curr_point):
    res = []
    for end_time, start_time, next_point in graph[curr_point]:
        if curr_time <= start_time: res.append((end_time, next_point))
    
    return res

fin = open('input.txt')
N = int(fin.readline())
start, end = [int(x) for x in fin.readline().split()]

R = int(fin.readline())
graph = defaultdict(list)
for _ in range(R):
    x, t0, y, t1 = [int(x) for x in fin.readline().split()]
    graph[x].append((t1, t0, y))

visited = set()
time = defaultdict(lambda: float('inf'))
time[start] = 0

stack = [(0, start)]
while stack:
    curr_time, curr_point = heapq.heappop(stack)

    if curr_point not in visited:
        for end_time, next_point in getNextPoints(graph, curr_time, curr_point):
            if end_time < time[next_point]:
                time[next_point] = end_time
                heapq.heappush(stack, (end_time, next_point))

    visited.add(curr_point)

print(time[end]) if time[end] != float('inf') else print(-1)