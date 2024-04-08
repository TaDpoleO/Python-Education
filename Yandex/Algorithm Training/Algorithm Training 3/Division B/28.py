def answer(N, M):
    dp = [[0]*(M+2) for _ in range(N+2)]
    dp[2][2] = 1

    dx = [-2, -1]
    dy = [-1, -2]

    for i in range(2, N+2):
        for j in range(2, M+2):
            for k in range(2):
                dp[i][j] += dp[i+dx[k]][j+dy[k]]

    return dp[-1][-1]

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]

        print(answer(N, M))

if __name__ == '__main__':
    main()