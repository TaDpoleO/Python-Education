fin = open('input.txt')
N = int(fin.readline())

matrix = [[] for _ in range(N)]
for i, line in enumerate(fin):
    matrix[i] = [int(x) for x in line.split()]

def answer(matrix):
    if len(matrix) == 1: return False
    visited, path = set(), dict()

    for i in range(N):
        if i not in visited:
            visited.add(i)

            stack = [(i, None)]
            while stack:
                curr_v, prev_v = stack.pop()

                for next_v in range(N):
                    if matrix[curr_v][next_v] == 1:
                        if next_v not in visited:
                            visited.add(next_v)
                            stack.append((next_v, curr_v))
                            path[next_v] = curr_v
                        elif prev_v != next_v:
                            return (path, curr_v, next_v)
                        
    return False

res = answer(matrix)
if res:
    path, prev_v, last_v = res

    ans = [path[last_v], last_v]
    while prev_v != ans[0]:
        ans.append(prev_v)
        prev_v = path[prev_v]

    print('YES')
    print(len(ans))
    print(*map(lambda x: x+1, ans))
else:
    print('NO')