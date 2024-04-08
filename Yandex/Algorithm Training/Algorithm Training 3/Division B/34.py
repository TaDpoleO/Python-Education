import sys
sys.setrecursionlimit(200000)

from collections import defaultdict

fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

graph = defaultdict(set)
for line in fin:
    x, y = [int(x) for x in line.split()]    
    graph[x].add(y)
    
def answer(graph):
    def dfs(v):
        colors[v] = 1
        
        for next_v in graph[v]:
            if colors[next_v] == 0:                
                if not dfs(next_v): return False
            elif colors[next_v] == 1:
                return False
        
        colors[v] = 2
        order.append(v)
    
        return True

    colors, order = defaultdict(int), []
    for v in range(1, N+1):
        if colors[v] == 0:
            if not dfs(v): return [-1]

    return reversed(order)

print(*answer(graph))