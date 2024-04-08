from collections import deque

fin = open('input.txt')
N = int(fin.readline())

array = [0]*N
for i in range(N):	
    array[i] = [int(x) for x in fin.readline().split()]
        
start, end = [int(x)-1 for x in fin.readline().split()]

def getShortPath(array, start, end):
    if start == end: return 0

    path = dict()
    stack, visited = deque([start]), set([start])
    while stack:
        curr_pos = stack.pop()
        
        for next_pos in range(len(array)):                    
            if (array[curr_pos][next_pos] == 1) and (next_pos not in visited):
                if next_pos == end: return path, curr_pos, next_pos
                stack.appendleft(next_pos)
                visited.add(next_pos)                
                path[next_pos] = curr_pos                
                
    return -1               

path = getShortPath(array, start, end)
if path == -1:
    print(-1)
elif path == 0:
    print(0)
else:
    path, prev, last = path

    ans = [last]
    while prev != start:
        ans.append(prev)
        prev = path[prev]
    ans.append(prev)

    print(len(ans)-1)
    print(*map(lambda x: x+1, reversed(ans)))