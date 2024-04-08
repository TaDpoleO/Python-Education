fin = open('input.txt')
N = int(fin.readline())
S = fin.readline().rstrip()
# S = [int(x) for x in fin.readline().split()]

x0 = 277
# x0 = 10
p = 1073676287

prefix = [0]*(N+1)
suffix = [0]*(N+1)
x = [1]*(N+1)

for i in range(N):
    # prefix[N-i-1] = (prefix[N-i]+S[i]*x[i]) % p
    # suffix[N-i-1] = (suffix[N-i]+S[N-i-1]*x[i]) % p
    prefix[N-i-1] = (prefix[N-i]+ord(S[i])*x[i]) % p
    suffix[N-i-1] = (suffix[N-i]+ord(S[N-i-1])*x[i]) % p
    x[i+1] = (x[i]*x0) % p    

def isEqual(pos, slen):
    # print((prefix[N-pos-1]-prefix[N+slen-pos-1])//x[pos-slen+1])
    # print((suffix[0]-suffix[slen])//x[N-slen])
    return (prefix[N-pos-1]*x[N-slen]+suffix[slen]*x[pos-slen+1])%p == (suffix[0]*x[pos-slen+1]+prefix[N+slen-pos-1]*x[N-slen])%p

def bsearch(left, right, index):
    while left < right:
        mid = (left+right+1)//2
        # TTTT, TTFF        
        if isEqual(index, mid):
            left = mid
        else:
            right = mid-1

    return left

z = [0]*N
for i in range(N):
    z[i] = bsearch(0, i+1, i)
print(*z)