import datetime

fin = open('input.txt')
N = int(fin.readline())

TYPE_START = 10
TYPE_END = 5

events = []
for i in range(N):
    d1, m1, y1, d2, m2, y2 = [int(x) for x in fin.readline().split()]
    age18 = datetime.date(y1+18, m1, d1)
    age80 = datetime.date(y1+80, m1, d1)
    death = datetime.date(y2, m2, d2)

    if death > age18:
        events.append((age18, TYPE_START, i+1))
        events.append((min(age80, death), TYPE_END, i+1))
events.sort()

def getOneTimePeople(events):
    if not events: return []

    one_time_people = [set()]

    curr_living = set()
    for event in events:
        if event[1] == TYPE_START:
            curr_living.add(event[2])
        elif event[1] == TYPE_END:
            id = event[2]
            if curr_living-one_time_people[-1]:
                one_time_people.append(curr_living.copy())
            curr_living.remove(id)

    return one_time_people[1:]

people = getOneTimePeople(events)
if people:
    for one_time in people:
        print(*one_time)
else:
    print(0)