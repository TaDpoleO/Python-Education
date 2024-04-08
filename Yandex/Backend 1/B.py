from collections import defaultdict

fin = open('input.txt')

N = int(fin.readline())

rockets = defaultdict(int)
for _ in range(N):
    day, hour, minute, id, status = fin.readline().split()
    day, hour, minute, id = [int(x) for x in (day, hour, minute, id)]

    all_in_minute = day*24*60+hour*60+minute
    if status == 'A':
        rockets[id] -= all_in_minute
    elif status == 'S' or status == 'C':
        rockets[id] += all_in_minute

for key in sorted(rockets.keys()):
    print(rockets[key], end=' ')