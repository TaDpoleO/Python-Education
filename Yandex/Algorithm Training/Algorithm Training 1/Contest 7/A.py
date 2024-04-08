fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]
events = [None]*2*M

TYPE_START = 0
TYPE_END = 1

for i in range(M):
    start, end = [int(x) for x in fin.readline().split()]
    events[2*i] = (start, TYPE_START, i)
    events[2*i+1] = (end, TYPE_END, i)
events.sort()

curr_watch, total_students = 0, N
for event in events:
    pos, event_type, id = event
    if event_type == TYPE_START:
        if curr_watch == 0: total_students += pos-1
        curr_watch += 1       
    elif event_type == TYPE_END:
        curr_watch -= 1
        if curr_watch == 0: total_students -= pos

print(total_students)