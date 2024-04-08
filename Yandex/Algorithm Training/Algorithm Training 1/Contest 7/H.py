fin = open('input.txt')
K = int(fin.readline())

TYPE_START_GUARD = 5
TYPE_END_GUARD = 20

def check(events):
    prev_time = 0
    all_guards, curr_guard, solo_guard = set(), set(), set()

    for event in events:
        time, event_type = event[0], event[1]
        if (len(curr_guard) == 0) and (time > 0): return 'Wrong Answer'

        if (len(curr_guard) == 1) and (time > prev_time):
            solo_guard |= curr_guard

        if event_type == TYPE_START_GUARD:            
            id = event[2]
            curr_guard.add(id)
            all_guards.add(id)
            
        elif event_type == TYPE_END_GUARD:                        
            id = event[2]
            curr_guard.remove(id)        
        
        prev_time = time

    if prev_time <= 9999: return 'Wrong Answer'
    if solo_guard == all_guards:
        return 'Accepted'
    else:
        return 'Wrong Answer'
       
for i in range(K):
    inp_data = [int(x) for x in fin.readline().split()]
    N = inp_data[0]
    events = [0]*2*N
    for j in range(N):
        events[2*j] = (inp_data[2*j+1], TYPE_START_GUARD, j)
        events[2*j+1] = (inp_data[2*j+2], TYPE_END_GUARD, j)
    events.sort()

    print(check(events))