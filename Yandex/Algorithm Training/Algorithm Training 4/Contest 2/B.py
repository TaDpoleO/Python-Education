fin = open('input.txt')
S = fin.readline().rstrip()

N = len(S)
x0 = 277
p = 1073676287

h = [0]*(N+1)
x = [1]*(N+1)

for i in range(N):
    h[i+1] = (h[i]*x0+ord(S[i])) % p
    x[i+1] = (x[i]*x0) % p

# index = 0...N-1
def isEqual(pos1, pos2, slen):
    return (h[pos1+slen]+h[pos2]*x[slen]) % p == (h[pos2+slen]+h[pos1]*x[slen]) % p

min_prefix = N
for i in range(1, N+1):
    if isEqual(0, i, N-i): min_prefix = min(min_prefix, i)

print(min_prefix)