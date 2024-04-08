from math import gcd

fin = open('input.txt')

N = int(fin.readline())
nums = [int(x) for x in fin.readline().split()]

dp = [[0]*(N+1) for _ in range(N)]
for i in range(N):
    for j in range(N-1, -1, -1):
        if nums[i] > nums[j]:
            dp[i][j] = dp[i][j+1]+1
        else:
            dp[i][j] = dp[i][j+1]    

inversion_count0 = 0
for i in range(N):
    inversion_count0 += dp[i][i]

inversion_count = 0
for i in range(N):
    for j in range(i+1, N):
        curr_count = inversion_count0
        curr_count = curr_count-dp[i][i]+dp[i][j+1]        
        curr_count = curr_count-dp[j][j]+dp[j][i]
        curr_count = curr_count+(j-i-1)-(dp[i][i]-dp[i][j])
        curr_count = curr_count-(j-i-1)+(dp[j][i+1]-dp[j][j])

        inversion_count += curr_count

x = inversion_count
y = N*(N-1)//2
z = gcd(x, y)

print(f'{x//z}/{y//z}')