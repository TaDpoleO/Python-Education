def getTreesNum(days, A, K, B, M):
    rest_A_days = days // K
    rest_B_days = days // M

    return (days-rest_A_days)*A+(days-rest_B_days)*B

def check(days, A, K, B, M, X):
    return getTreesNum(days, A, K, B, M) < X

def bsearch(left, right, check, check_param):
    while left < right:
        mid = (left+right)//2
        # FFFF, TT(F)F
        if check(mid, *check_param):
            left = mid+1
        else:
            right = mid

    return left

fin = open('input.txt')
A, K, B, M, X = [int(x) for x in fin.readline().split()]
max_days = min(int(X/(A*(K-1)/K))+1, int(X/(B*(M-1)/M))+1)

need_days = bsearch(1, max_days, check, [A, K, B, M, X])
print(need_days)