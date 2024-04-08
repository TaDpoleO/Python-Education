fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]
cats_pos = [int(x) for x in fin.readline().split()]

events = [0]*(2*M+N)

TYPE_START_SEG = 10
TYPE_CAT = 15
TYPE_END_SEG = 20

for i in range(M):
    l, r = [int(x) for x in fin.readline().split()]
    events[2*i] = (l, TYPE_START_SEG, i)
    events[2*i+1] = (r, TYPE_END_SEG, i)

for i in range(N):    
    events[2*M+i] = (cats_pos[i], TYPE_CAT, -1)

cats_in_segments = [0]*M

def answer(events, segments):
    events.sort()    

    seen_cats = 0
    for event in events:
        _, event_type, id = event

        if event_type == TYPE_START_SEG:
            segments[id] = seen_cats
        elif event_type == TYPE_END_SEG:
            segments[id] = seen_cats-segments[id]
        elif event_type == TYPE_CAT:
            seen_cats += 1

    return segments

print(' '.join(map(str, answer(events, cats_in_segments))))