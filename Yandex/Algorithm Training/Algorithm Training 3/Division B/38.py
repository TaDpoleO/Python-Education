from collections import deque

fin = open('input.txt')
N, M, S, T, Q = [int(x) for x in fin.readline().split()]
start = (S-1, T-1)

ends = set()
for i in range(Q):
    x, y = [int(x) for x in fin.readline().split()]
    ends.add((x-1, y-1))
    
def getNextPos(row, col, N, M):
    delta = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
    
    res = []
    for step in delta:
        next_row = row+step[0]
        next_col = col+step[1]
        
        if (0 <= next_row) and (next_row <= N-1) and (0 <= next_col) and (next_col <= M-1):
            res.append((next_row, next_col))
            
    return res

def answer(start, ends, N, M):
    if not ends: return 0

    visited = [[None for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]] = 0

    found = dict()
    if start in ends:
        found[start] = 0
        if len(ends) == 1: return 0
    
    stack = deque([start])
    while stack:
        curr_pos = stack.pop()
        
        for next_pos in getNextPos(*curr_pos, N, M):
            if visited[next_pos[0]][next_pos[1]] is None:
                visited[next_pos[0]][next_pos[1]] = visited[curr_pos[0]][curr_pos[1]]+1
                
                if next_pos in ends:
                    found[next_pos] = visited[next_pos[0]][next_pos[1]]
                    if len(found) == len(ends):
                        total_dist = 0
                        for val in found.values():
                            total_dist += val
                        return total_dist
                    
                stack.appendleft(next_pos)
        
    return -1

print(answer(start, ends, N, M))