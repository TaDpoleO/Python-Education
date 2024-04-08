from collections import defaultdict
import sys

fin = sys.stdin
# fin = open('input.txt')

N, M, K = [int(x) for x in fin.readline().split()]

graph = defaultdict(dict)
for _ in range(M):
    u, d, v = [int(x) for x in fin.readline().split()]    
    graph[u][d] = v
    # graph[v][d] = u

car_route = [int(x) for x in fin.readline().split()]

def getFinalPoint(graph, route, start):

    curr_point, curr_index = start, 0
    while curr_index < len(route):
        curr_car = route[curr_index]

        if curr_car in graph[curr_point]:
            curr_point = graph[curr_point][curr_car]
            curr_index += 1
        else:
            return 0

    return curr_point

print(getFinalPoint(graph, car_route, 1))