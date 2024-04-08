def answer(N, M, array):
    dp = [[0]*M for _ in range(N)]
    dp[0][0] = array[0][0]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0]+array[i][0]

    for j in range(1, M):
        dp[0][j] = dp[0][j-1]+array[0][j]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])+array[i][j]

    route = []
    cur_sum, i, j = dp[-1][-1], N-1, M-1
    while not (i == 0 and j == 0):
        if (i > 0) and (dp[i-1][j]+array[i][j] == cur_sum):
            route.append('D')
            cur_sum = dp[i-1][j]
            i -= 1
        else:
            route.append('R')
            cur_sum = dp[i][j-1]
            j -= 1

    return dp[N-1][M-1], reversed(route)

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]

        array = [[0]*M for _ in range(N)]
        for i in range(N):
            array[i] = [int(x) for x in fin.readline().split()]

        length, route = answer(N, M, array)
        print(length)
        print(' '.join(route))

if __name__ == '__main__':
    main()