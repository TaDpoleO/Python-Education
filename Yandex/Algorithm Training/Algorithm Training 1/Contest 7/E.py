fin = open('input.txt')
N = int(fin.readline())

TYPE_OPEN = 0
TYPE_CLOSE = 10

events, all_time_count = [], 0
for i in range(N):
    h1, m1, h2, m2 = [int(x) for x in fin.readline().split()]    
    t1, t2 = h1*60 + m1, h2*60 + m2
    if t1 < t2:
        events.append((t1, TYPE_OPEN, i))
        events.append((t2, TYPE_CLOSE, i))
    elif t1 > t2:
        events.append((t1, TYPE_OPEN, i))
        events.append((t2, TYPE_CLOSE, i))
    else:
        all_time_count += 1        
events.sort()

def getAllOpenedTime(events, all_time_count):    
    if not events:
        if all_time_count != 0:
            return 1440
        else:
            return 0

    opened_cashbox, opened_count = set(), all_time_count
    for event in events:
        time, event_type, id = event
        if event_type == TYPE_OPEN:
            opened_cashbox.add(id)
            opened_count += 1
        elif event_type == TYPE_CLOSE:
            if id in opened_cashbox:
                opened_count -= 1            
            
    total_time = 0
    for event in events:
        time, event_type, id = event
        if event_type == TYPE_OPEN:
            opened_count += 1
            if opened_count == N: total_time -= time
        elif event_type == TYPE_CLOSE:
            if opened_count == N: total_time += time
            opened_count -= 1
    
    if total_time >= 0:
        return total_time
    else:
        return 1440+total_time
    
print(getAllOpenedTime(events, all_time_count))