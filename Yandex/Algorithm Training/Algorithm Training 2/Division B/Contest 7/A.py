fin = open('input.txt')
N = int(fin.readline())
events = [0]*2*N

EVENT_OPEN = 10
EVENT_CLOSE = 20

for i in range(N):
    l, r = [int(x) for x in fin.readline().split()]
    events[2*i] = (l, EVENT_OPEN)
    events[2*i+1] = (r, EVENT_CLOSE)

events.sort()

curr_opened_segments, sum_length = 0, 0
for event in events:
    curr_pos, event_type = event

    if event_type == EVENT_OPEN:
        curr_opened_segments += 1
        if curr_opened_segments == 1:
            last_open = curr_pos
    elif event_type == EVENT_CLOSE:
        curr_opened_segments -= 1
        if curr_opened_segments == 0:
            sum_length += curr_pos-last_open
            
print(sum_length)