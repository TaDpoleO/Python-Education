from collections import defaultdict

fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

graph = defaultdict(set)
for line in fin:
    x, y = [int(x) for x in line.split()]
    graph[x].add(y)
    graph[y].add(x)
    
visited, regions = set(), []
for pos in graph.keys():
    if pos not in visited:
        regions.append([pos])
        visited.add(pos)
        
        stack = [pos]
        while stack:
            curr_pos = stack.pop()
            
            for next_pos in graph[curr_pos]:
                if next_pos not in visited:
                    visited.add(next_pos)                    
                    regions[-1].append(next_pos)                    
                    stack.append(next_pos)

for solo_pos in set(range(1,N+1))-set(visited):
    regions.append([solo_pos])
    
print(len(regions))
for region in regions:
    print(len(region))
    print(*region)