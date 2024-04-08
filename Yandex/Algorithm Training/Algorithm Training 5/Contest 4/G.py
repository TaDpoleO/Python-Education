def get_total_sum(prefix, p0, p1):
    row0, col0 = p0
    row1, col1 = p1

    return prefix[row1+1][col1+1]+prefix[row0][col0]-prefix[row1+1][col0]-prefix[row0][col1+1]

def isPlus(prefix, row0, col0, K):
    if get_total_sum(prefix, (row0, col0+K), (row0+3*K-1, col0+2*K-1)) != K*K*3: return False
    if get_total_sum(prefix, (row0+K, col0), (row0+2*K-1, col0+3*K-1)) != K*K*3: return False
   
    return True

def hasPlus(prefix, N, M, K):
    for i in range(N-3*K+1):
        for j in range(M-3*K+1):
            if isPlus(prefix, i, j, K): return True
    
    return False

def bsearch(prefix, N, M):
    left = 1
    right = min(N, M)//3

    while left < right:
        mid = (left+right+1)//2

        # TTFF, TTTT
        if hasPlus(prefix, N, M, mid):
            left = mid
        else:
            right = mid-1

    return left

def answer(field, N, M):
    prefix = [[0]*(M+1) for _ in range(N+1)]    

    for i in range(N):
        for j in range(M):
            prefix[i+1][j+1] = field[i][j]+prefix[i+1][j]

        for j in range(M):
            prefix[i+1][j+1] = prefix[i+1][j+1]+prefix[i][j+1]   

    result = bsearch(prefix, N, M)
    return result

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]
        field = [[0]*M for _ in range(N)]

        for i in range(N):
            row = fin.readline().rstrip()
            for j in range(M):
                if row[j] == '#':
                    field[i][j] = 1

        print(answer(field, N, M))


if __name__ == '__main__':    
    main()