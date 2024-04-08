fin = open('input.txt')
N = int(fin.readline())

graph = [None]*N
for i in range(N):
    graph[i] = [int(x) for x in fin.readline().split()]

def findMinPath(graph, start_point, end_point):
    def findPath(curr_point, curr_dist, visited_count, all_points, remaining_path):
        nonlocal best_path

        if visited_count == all_points:
            if graph[curr_point][end_point] != 0:
                best_path = min(best_path, curr_dist+graph[curr_point][end_point])
                return curr_dist+graph[curr_point][end_point]
            else:
                return float('inf')
        else:
            min_path = float('inf')

            for i in range(len(graph[0])):
                if not visited[i] and graph[curr_point][i] != 0:
                    visited[i] = True
                    if curr_dist+remaining_path < best_path:
                        min_path = min(min_path, findPath(i, curr_dist+graph[curr_point][i], visited_count+1, all_points, remaining_path-min_e[curr_point]))
                    visited[i] = False
            
            return min_path

    N = len(graph[0])
    if N == 1: return 0
    if N == 2:
        if graph[0][1] != 0 and graph[1][0] != 0:
            return graph[0][1]+graph[1][0]
        else:
            return -1
    
    visited = [False]*N
    visited[start_point] = True
    visited[end_point] = True

    if start_point == end_point:
        all_points = N-1
    else:
        all_points = N-2

    min_remaining_path = 0
    min_e = [float('inf')]*N
    for i in range(N):
        for j in range(N):
            if j != i: min_e[i] = min(min_e[i], graph[i][j])
        min_remaining_path += min_e[i]

    best_path = float('inf')
    min_path = findPath(start_point, 0, 0, all_points, min_remaining_path)
    if min_path == float('inf'):
        return -1
    else:
        return min_path

print(findMinPath(graph, 0, 0))