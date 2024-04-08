from collections import defaultdict

fin = open('input.txt')
fin.readline()

graph = defaultdict(set)
for line in fin:
    if not line.rstrip(): break
    x, y = [int(x) for x in line.split()]
    graph[x].add(y)
    graph[y].add(x)

stack, visited = [1], set([1])
while stack:
    pos = stack.pop()

    for next_pos in graph[pos]:
        if next_pos not in visited:
            visited.add(next_pos)
            stack.append(next_pos)
    
print(len(visited))
print(*sorted(visited))