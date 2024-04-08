from collections import deque

fin = open('input.txt')
N = int(fin.readline())

cities = []
for i in range(1, N+1):    
    start_time, start_speed = [int(x) for x in fin.readline().split()]
    cities.append((start_speed, start_time, i))
cities.sort()

roads = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y, dist = [int(x) for x in fin.readline().split()]
    roads[x].append((dist, y))
    roads[y].append((dist, x))

all_roads = [[float('inf')]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    all_roads[i][i] = 0

finish_time, change_point, finished = [None]*(N+1), [None]*(N+1), set()
max_time, max_city = 0, 1
for start_speed, start_time, start_point in cities[::-1]:
    stack, visited = deque([(0, start_point)]), set([start_point])
    while stack:
        curr_dist, curr_point = stack.pop()

        for next_dist, next_point in roads[curr_point]:
            if (next_point not in visited) and (curr_dist+next_dist < all_roads[start_point][next_point]):
                all_roads[start_point][next_point] = curr_dist+next_dist
                stack.appendleft((curr_dist+next_dist, next_point))
                visited.add(next_point)

    finish_time[start_point] = start_time+all_roads[start_point][1]/start_speed
    change_point[start_point] = start_point
    
    for other_point in finished:
        time_with_change = start_time+all_roads[start_point][other_point]/start_speed+finish_time[other_point]

        if time_with_change < finish_time[start_point]:
            finish_time[start_point] = time_with_change
            change_point[start_point] = other_point

    finished.add(start_point)
    if finish_time[start_point] > max_time:
        max_time = finish_time[start_point]
        max_city = start_point

path = []
curr_point = max_city
while curr_point != change_point[curr_point]:
    path.append(curr_point)
    curr_point = change_point[curr_point]
path.append(curr_point)
path.append(1)

print(max_time)
print(*path)