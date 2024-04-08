def answer(N, M, array):    
    dp = [[0]*M for _ in range(N)]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0]+array[i][0]

    for j in range(1, M):
        dp[0][j] = dp[0][j-1]+array[0][j]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])+array[i][j]

    return dp[-1][-1]+array[0][0]

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]

        array = [[0]*M for _ in range(N)]
        for i in range(N):
            array[i] = [int(x) for x in fin.readline().split()]

        print(answer(N, M, array))

if __name__ == '__main__':
    main()