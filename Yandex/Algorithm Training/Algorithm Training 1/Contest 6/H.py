def isSliceable(length, segments, number):
    total = 0
    for segment in segments:
        total += segment//length
        
    return total >= number
    
def bin_search(left, right, condition, cond_param):
    while left < right:
        mid = (left+right+1)//2
        # TTTT, TTFF
        if condition(mid, *cond_param):
            left = mid
        else:
            right = mid-1
            
    return left

fin = open('input.txt')
N, K = [int(x) for x in fin.readline().split()]

sum_length = 0
L = [0]*N
for i in range(N):
    li = int(fin.readline())
    L[i] = li
    sum_length += li
    
if sum_length < K:
    print(0)
else:
    # 1, ..., max(L)
    print(bin_search(1, max(L), isSliceable, [L, K]))