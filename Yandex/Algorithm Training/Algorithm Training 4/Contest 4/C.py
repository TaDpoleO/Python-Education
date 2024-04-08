def partition(curr_point, curr_sum, v_number):
    if curr_point == v_number:
        return curr_sum, teams.copy()
    else:
        teams[curr_point] = 1
        temp_sum = curr_sum
        for i in range(v_number):
            if graph[curr_point][i] != 0 and teams[i] == 2:
                temp_sum += graph[curr_point][i]        
        max_sum1, parts1 = partition(curr_point+1, temp_sum, v_number)

        teams[curr_point] = 2
        temp_sum = curr_sum
        for i in range(v_number):
            if graph[curr_point][i] != 0 and teams[i] == 1:
                temp_sum += graph[curr_point][i]        
        max_sum2, parts2 = partition(curr_point+1, temp_sum, v_number)

        teams[curr_point] = 0

        if max_sum1 > max_sum2:
            return max_sum1, parts1
        else:
            return max_sum2, parts2

fin = open('input.txt')
N = int(fin.readline())
graph = [None]*N

for i in range(N):
    graph[i] = [int(x) for x in fin.readline().split()]

teams = [0]*N
teams[0] = 1

# Real Max
max_sum, parts = partition(1, 0, N)
print(max_sum)
print(*parts)