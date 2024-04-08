import heapq
from collections import defaultdict

fin = open('input.txt')
N, K = [int(x) for x in fin.readline().split()]

graph = defaultdict(list)
for i in range(1,K+1):
    a, b, d = [int(x) for x in fin.readline().split()]
    graph[a].append((d, b))
    graph[b].append((d, a))

start, end = [int(x) for x in fin.readline().split()]

visited = set()
distance = [float('inf')]*(N+1)
distance[start] = 0

stack = [(0, start)]
while stack:
    curr_dist, curr_point = heapq.heappop(stack)    

    if curr_point not in visited:
        for next_dist, next_point in graph[curr_point]:
            if curr_dist+next_dist < distance[next_point]:            
                distance[next_point] = curr_dist+next_dist                
                heapq.heappush(stack, (curr_dist+next_dist, next_point))

    visited.add(curr_point)

print(distance[end]) if distance[end] != float('inf') else print(-1)