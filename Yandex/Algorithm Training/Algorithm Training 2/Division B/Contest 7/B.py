fin = open('input.txt')
N = int(fin.readline())
events = [0]*2*N

TYPE_START = 10
TYPE_END = -10

for i in range(N):
    t, l = [int(x) for x in fin.readline().split()]
    events[2*i] = (t, TYPE_START)
    events[2*i+1] = (t+l, TYPE_END)

events.sort()

curr_started, max_events = 0, 0
for event in events:
    curr_time, event_type = event

    if event_type == TYPE_START:
        curr_started += 1
        max_events = max(max_events, curr_started)
    elif event_type == TYPE_END:
        curr_started -= 1
            
print(max_events)