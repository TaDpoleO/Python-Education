from collections import deque

fin = open('input.txt')
N = M = K = int(fin.readline())

cave = [[[0 for _ in range(K)] for _ in range(M)] for _ in range(N)] # Или наоборот?
start = (None, None, None)
# i = z, j = y, k = x
# z = 0 >>> Вышли!
for i in range(N):
    fin.readline()
        
    for j in range(N):
        for k, point in enumerate([x for x in fin.readline().rstrip()]):
            if point == '#':
                cave[i][j][k] = 0
            elif point == '.':
                cave[i][j][k] = 1
            elif point == 'S':
                cave[i][j][k] = 1
                start = (i, j, k)

def getNextPos(z_pos, y_pos, x_pos, N, M, K):
    delta = (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)

    res = []
    for step in delta:
        next_z = z_pos+step[0]
        next_y = y_pos+step[1]
        next_x = x_pos+step[2]

        if (0 <= next_z) and (next_z <= N-1) and (0 <= next_y) and (next_y <= M-1) and (0 <= next_x) and (next_x <= K-1) and (cave[next_z][next_y][next_x] == 1):
            res.append((next_z, next_y, next_x))

    return res

def getMinPath(cave, start):
    if start[0] == 0: return 0

    N = len(cave)
    M = len(cave[0])
    K = len(cave[0][0])

    stack, visited = deque([(start, 0)]), set([start])
    while stack:
        curr_pos, level = stack.pop()

        for next_pos in getNextPos(*curr_pos, N, M, K):
            if next_pos[0] == 0: return level+1

            if next_pos not in visited:
                visited.add(next_pos)
                stack.appendleft((next_pos, level+1))

    return -1

print(getMinPath(cave, start))