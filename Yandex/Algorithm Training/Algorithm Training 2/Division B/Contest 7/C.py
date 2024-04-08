fin = open('input.txt')
M = int(fin.readline())
events = []

TYPE_START = 10
TYPE_END_M = 15
TYPE_END = 20
TYPE_START_M = 25

segments, id = [], 0

line = fin.readline().rstrip()
while line != '0 0':
    l, r = [int(x) for x in line.split()]
    segments.append((l, r))
    events.append((l, TYPE_START, id))
    events.append((r, TYPE_END, id))
    id += 1
    line = fin.readline().rstrip()
events.append((0, TYPE_START_M, -1))
events.append((M, TYPE_END_M, -1))

def answer(events, segments):
    events.sort()    
    res = []

    curr_started, curr_needed, start_check = set(), set(), False
    for event in events:
        _, event_type, id = event

        if event_type == TYPE_START:
            curr_started.add(id)
        elif event_type == TYPE_START_M:
            start_check = True
            curr_needed = curr_started.copy()
            if not curr_needed: return 'No solution'
        elif event_type == TYPE_END_M:
            start_check = False
            curr_id = curr_needed.pop()
            res.append(segments[curr_id])
            break
        elif event_type == TYPE_END:
            curr_started.remove(id)
            if start_check:
                if id in curr_needed: curr_needed.remove(id)
                if not curr_needed:
                    res.append(segments[id])
                    curr_needed = curr_started.copy()
                    if not curr_needed: return 'No solution'

    res.sort()

    res_str = [str(len(res))]
    for segment in res:
        res_str.append(' '.join(map(str, segment)))
    return '\n'.join(res_str)

print(answer(events, segments))