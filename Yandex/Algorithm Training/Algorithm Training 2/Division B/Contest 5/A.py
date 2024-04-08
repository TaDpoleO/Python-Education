fin = open('input.txt')
N, Q = [int(x) for x in fin.readline().split()]
array = [int(x) for x in fin.readline().split()]

prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i]+array[i]

for i in range(Q):
    l, r = [int(x) for x in fin.readline().split()]
    print(prefix[r]-prefix[l-1])