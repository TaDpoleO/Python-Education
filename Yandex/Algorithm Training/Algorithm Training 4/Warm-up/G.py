fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

array = [[] for _ in range(N)]
for i in range(N):
    array[i] = [int(x) for x in fin.readline().split()]

dp = [[0]*M for _ in range(N)]

res = 0
for i in range(M):
    dp[0][i] = array[0][i]
    res = max(res, array[0][i])

for i in range(N):
    dp[i][0] = array[i][0]
    res = max(res, array[i][0])

for i in range(1, N):
    for j in range(1, M):
        if (array[i][j] != 0):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1         
            res = max(res, dp[i][j])

print(res)