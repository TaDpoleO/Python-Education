fin = open('input.txt')

N = int(fin.readline())
shirts = [int(x) for x in fin.readline().split()]

M = int(fin.readline())
pants = [int(x) for x in fin.readline().split()]

min_diff, shirts_index, pants_index = shirts[0]-pants[0], 0, 0
i, j = 0, 0
while (i < N) and (j < M):
    curr_diff = shirts[i]-pants[j]
    if abs(curr_diff) < abs(min_diff):
        min_diff, shirts_index, pants_index = curr_diff, i, j
    else:
        if curr_diff < 0:
            i += 1
        else:
            j += 1
            
if i == N:
    while j < M:
        curr_diff = shirts[N-1]-pants[j]
        if abs(curr_diff) < abs(min_diff):
            min_diff, shirts_index, pants_index = curr_diff, N-1, j
        j += 1
else:            
    while i < N:
        curr_diff = shirts[i]-pants[M-1]
        if abs(curr_diff) < abs(min_diff):
            min_diff, shirts_index, pants_index = curr_diff, i, M-1
        i += 1
       
print(shirts[shirts_index], pants[pants_index])