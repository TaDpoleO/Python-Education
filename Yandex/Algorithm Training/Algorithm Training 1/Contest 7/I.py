from collections import defaultdict

fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

TYPE_START_ROUTE = 20
TYPE_END_ROUTE = 10

def checkPossibility(events):
    cities = defaultdict(int)    

    for event in events:
        city, event_type = event[2], event[1]
        if event_type == TYPE_START_ROUTE:
            cities[city] -= 1
        elif event_type == TYPE_END_ROUTE:
            cities[city] += 1

    for num in cities.values():
        if num != 0: return False

    return True

def getMinAutos(events):
    if not checkPossibility(events): return -1

    cities_curr, total = defaultdict(int), 0
    started_route = set()

    for event in events:        
        _, event_type, city, route_id = event

        if event_type == TYPE_START_ROUTE:            
            started_route.add(route_id)           
            if cities_curr[city] == 0:
                total +=1
            else:
                 cities_curr[city] -= 1

        elif event_type == TYPE_END_ROUTE:            
            if route_id in started_route:
                started_route.remove(route_id)
            cities_curr[city] += 1

    return len(started_route)+total

events = [None]*2*M
for i in range(M):
    city1, time1, city2, time2 = [x for x in fin.readline().split()]

    h1, m1 = [int(x) for x in time1.split(':')]
    time1 = h1*60+m1

    h2, m2 = [int(x) for x in time2.split(':')]
    time2 = h2*60+m2

    events[2*i] = (time1, TYPE_START_ROUTE, city1, i)
    events[2*i+1] = (time2, TYPE_END_ROUTE, city2, i)
events.sort()

print(getMinAutos(events))