import heapq

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

stack = [(0, start)]
while stack:
    curr_dist, curr_point = heapq.heappop(stack)    

    if curr_point not in visited:
        for next_dist, next_point in getNextPoints(graph, curr_point):
            if curr_dist+next_dist < distance[next_point]:            
                distance[next_point] = curr_dist+next_dist
                heapq.heappush(stack, (curr_dist+next_dist, next_point))

    visited.add(curr_point)

print(distance[end]) if distance[end] != float('inf') else print(-1)