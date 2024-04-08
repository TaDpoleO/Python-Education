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

def isEqual(pos1, pos2, slen):
    return (h[pos1+slen-1]+h[pos2-1]*x[slen]) % p == (h[pos2+slen-1]+h[pos1-1]*x[slen]) % p

Q = int(fin.readline())
for _ in range(Q):
    query = [int(x) for x in fin.readline().split()]
    print('yes') if isEqual(query[1]+1, query[2]+1, query[0]) else print('no')