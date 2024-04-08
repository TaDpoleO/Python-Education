from collections import deque

fin = open('input.txt')
N, D = [int(x) for x in fin.readline().split()]

STUDENT_IN, STUDENT_OUT = 0, 1
events = []
for id, x0 in enumerate([int(x) for x in fin.readline().split()]):
    events.append((x0, STUDENT_IN, id))
    events.append((x0+D, STUDENT_OUT, id))    
events.sort()

answer = [0]*N
id_order_free, id_order_busy, bilet_id_max = deque(), deque(), 0
for event in events:
    pos, type, id = event
    if type == STUDENT_IN:
        if id_order_free:
            curr_id = id_order_free.popleft()
        else:
            curr_id = bilet_id_max+1
        answer[id] = curr_id
        bilet_id_max = max(bilet_id_max, curr_id)
        id_order_busy.append(curr_id)
    elif type == STUDENT_OUT:
        curr = id_order_busy.popleft()
        id_order_free.append(curr)
    
print(bilet_id_max)
print(*answer)