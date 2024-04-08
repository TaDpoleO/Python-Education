fin = open('input.txt')
N, M, K = [int(x) for x in fin.readline().split()]

array = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j, num in enumerate([int(x) for x in fin.readline().split()]):
        array[i][j+1] = num

prefix = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = prefix[i][j-1]+array[i][j]
    
    for j in range(1, M+1):
        prefix[i][j] = prefix[i-1][j]+prefix[i][j]

def getRectangleSum(prefix, x1, y1, x2, y2):
    return prefix[x1-1][y1-1]+prefix[x2][y2]-prefix[x1-1][y2]-prefix[x2][y1-1]

answer = [0]*K
for i in range(K):
    x1, y1, x2, y2 = [int(x) for x in fin.readline().split()]
    answer[i] = getRectangleSum(prefix, x1, y1, x2, y2)

print('\n'.join(map(str, answer)))