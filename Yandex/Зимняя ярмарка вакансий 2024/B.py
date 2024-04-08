fin = open('input.txt')

N, T, S = [int(x) for x in fin.readline().split()]
speeds = [int(x) for x in fin.readline().split()]

dist = [0]*N
for i in range(N):
    dist[i] = T*speeds[i]

laps = [0]*N
for i in range(N):
    laps[i] = dist[i]//S

last_lap_dist = [0]*N
for i in range(N):
    last_lap_dist[i] = dist[i]-laps[i]*S

overtakes = [0]*N
for i in range(1, N):
    overtakes[i] = laps[0]-laps[i]
    if last_lap_dist[i] >= last_lap_dist[0]: overtakes[i] -= 1

overtakes_count = 0
for i in range(1, N):
    if overtakes[i] > 0: overtakes_count += overtakes[i]

print(overtakes_count)