fin = open('input.txt')
N = int(fin.readline())

graph = [[] for _ in range(N)]

for i in range(N-1):
    point1, point2 = [int(x)-1 for x in fin.readline().split()]

    graph[point1].append(point2)
    graph[point2].append(point1)

max_path, max_point = 0, -1
stack, visited = [(0, 1)], set([0])
while stack:
    curr_point, curr_length = stack.pop()

    for next_point in graph[curr_point]:
        if next_point not in visited:
            visited.add(next_point)
            stack.append((next_point, curr_length+1))
            if curr_length+1 > max_path:
                max_path = curr_length+1
                max_point = next_point
                
stack, visited = [(max_point, 1)], set([max_point])
while stack:
    curr_point, curr_length = stack.pop()

    for next_point in graph[curr_point]:
        if next_point not in visited:
            visited.add(next_point)
            stack.append((next_point, curr_length+1))
            if curr_length+1 > max_path: max_path = curr_length+1

print(max_path)