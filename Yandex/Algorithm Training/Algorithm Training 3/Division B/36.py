from collections import deque

fin = open('input.txt')
N = int(fin.readline())

array = [0]*N
for i in range(N):	
    array[i] = [int(x) for x in fin.readline().split()]
        
start, end = [int(x)-1 for x in fin.readline().split()]

def getShortPath(array, start, end):
    if start == end: return 0

    distance = {start: 0}
    stack, visited = deque([start]), set([start])
    while stack:
        curr_pos = stack.pop()
        
        for next_pos in range(len(array)):                    
            if (array[curr_pos][next_pos] == 1) and (next_pos not in visited):
                if next_pos == end: return distance[curr_pos]+1
                stack.appendleft(next_pos)
                visited.add(next_pos)
                distance[next_pos] = distance[curr_pos]+1
                
    return -1               
    
print(getShortPath(array, start, end))