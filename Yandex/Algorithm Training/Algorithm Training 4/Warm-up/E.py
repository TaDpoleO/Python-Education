fin = open('input.txt')
N = int(fin.readline())
rating = [int(x) for x in fin.readline().split()]

delta = [0]*N
for i in range(1, N):
    delta[i] = abs(rating[i] - rating[i-1])

prefix_straitward = [0]*N
for i in range(1, N):
    prefix_straitward[i] = prefix_straitward[i-1]+delta[i]

prefix_backward = [0]*N
for i in range(N-2, -1, -1):
    prefix_backward[i] = prefix_backward[i+1]+delta[i+1]

prefix_prefix_straitward = [0]*N
for i in range(1, N):
    prefix_prefix_straitward[i] = prefix_prefix_straitward[i-1]+prefix_straitward[i]

prefix_prefix_backtward = [0]*N
for i in range(N-2, -1, -1):
    prefix_prefix_backtward[i] = prefix_prefix_backtward[i+1]+prefix_backward[i]

def getRightDeltaSum(index):
    return prefix_prefix_straitward[N-1]-prefix_prefix_straitward[index]-prefix_straitward[index]*(N-1-index)

def getLeftDeltaSum(index):
    return prefix_prefix_backtward[0]-prefix_prefix_backtward[index]-prefix_backward[index]*index

res = [getRightDeltaSum(i)+getLeftDeltaSum(i) for i in range(N)]
print(*res)