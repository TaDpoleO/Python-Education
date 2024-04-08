def answer(N, M, array1, array2):
    dp = [[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if array1[i-1] == array2[j-1]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])

    
    result = []
    cur_i, cur_j = N, M

    while dp[cur_i][cur_j] > 0:
        if array1[cur_i-1] == array2[cur_j-1]:
            result.append(array1[cur_i-1])
            delta = 1
        else:
            delta = 0

        if dp[cur_i][cur_j] == dp[cur_i-1][cur_j]-delta:
            cur_i -= 1
        elif dp[cur_i][cur_j] == dp[cur_i][cur_j-1]-delta:
            cur_j -= 1
        else:
            cur_i -= 1
            cur_j -= 1

    return reversed(result)

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        array1 = [int(x) for x in fin.readline().split()]
        M = int(fin.readline())
        array2 = [int(x) for x in fin.readline().split()]

        print(*answer(N, M, array1, array2))

if __name__ == '__main__':
    main()