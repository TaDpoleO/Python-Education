fin = open('input.txt')
buildings = [int(x) for x in fin.readline().split()]
N = len(buildings)

max_dist = 1
for i in range(N):
    if buildings[i] == 1:
        j = i+1
        while j < N and buildings[j] != 2:
            j += 1
        if j == N:
            curr_dist1 = 10
        else:
            curr_dist1 = j-i

        j = i-1
        while j > -1 and buildings[j] != 2:
            j -= 1
        if j == -1:
            curr_dist2 = 10
        else:
            curr_dist2 = i-j

        curr_dist = min(curr_dist1, curr_dist2)
        if curr_dist > max_dist: max_dist = curr_dist
    elif buildings[i] == 2:
        j = i+1
        while j < N and buildings[j] != 1:
            j += 1
        if j == N:
            curr_dist1 = 10
        else:
            curr_dist1 = j-i

        j = i-1
        while j > -1 and buildings[j] != 1:
            j -= 1
        if j == -1:
            curr_dist2 = 10
        else:
            curr_dist2 = i-j

        curr_dist = min(curr_dist1, curr_dist2)
        if curr_dist > max_dist: max_dist = curr_dist        

print(max_dist)