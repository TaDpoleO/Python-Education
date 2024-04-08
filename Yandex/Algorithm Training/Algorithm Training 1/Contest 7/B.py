fin = open('input.txt')

N, M = [int(x) for x in fin.readline().split()]
events = []

TYPE_START = 0
TYPE_POINT = 1
TYPE_END = 2

for i in range(N):
    start, end = [int(x) for x in fin.readline().split()]
    events.append((min(start, end), TYPE_START))
    events.append((max(start, end), TYPE_END))
    
for id, point in enumerate([int(x) for x in fin.readline().split()]):
    events.append((point, TYPE_POINT, id))

events.sort()

answer = [0]*M
curr_watcher = 0
for event in events:
    if event[1] == TYPE_START:
        curr_watcher += 1
    elif event[1] == TYPE_POINT:
        answer[event[2]] = curr_watcher
    elif event[1] == TYPE_END:
        curr_watcher -= 1
        
print(*answer)