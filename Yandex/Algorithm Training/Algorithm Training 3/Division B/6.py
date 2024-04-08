fin = open('input.txt')
M = int(fin.readline())
N = int(fin.readline())

os_partitions = [None]*N
os_valid = [True]*N

for i in range(N):
    os_partitions[i] = [int(x) for x in fin.readline().split()]

for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if os_valid[j]: os_valid[j] = (os_partitions[i][1] < os_partitions[j][0] or os_partitions[j][1] < os_partitions[i][0])

valid_count = 0
for i in range(N):
    valid_count += os_valid[i]
print(valid_count)