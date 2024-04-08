fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

colors = [int(x) for x in fin.readline().split()]
x0 = 1354828
p = 1073676287

suffix = [0]*(N+1)
suffix_rev = [0]*(N+1)
x = [1]*(N+1)

for i in range(N):
    suffix[N-i-1] = (suffix[N-i]+colors[N-i-1]*x[i]) % p    
    suffix_rev[N-i-1] = (suffix_rev[N-i]+colors[i]*x[i]) % p
    x[i+1] = (x[i]*x0) % p

res = []
for i in range(N//2+1):
    if (suffix_rev[N-i]*x[N-i-i]+suffix[i+i]) % p == suffix[i]: res.append(N-i)

res.sort()
print(*res)