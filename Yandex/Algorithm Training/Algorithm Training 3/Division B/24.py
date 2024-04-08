def answer(N, time_to_buy):
    dp = [0]*(N+1)
    dp[1] = time_to_buy[0][0]
    if N == 1: return dp[1]
    dp[2] = min(time_to_buy[1][0]+dp[1], time_to_buy[0][1])
    if N == 2: return dp[2]

    dp_1 = [0]*(N+1)
    dp_1[1] = time_to_buy[0][0]
    dp_1[2] = dp[1]+time_to_buy[1][0]

    dp_2 = [0]*(N+1)
    dp_2[1] = time_to_buy[0][1]
    dp_2[2] = dp[1]+time_to_buy[1][1]

    dp_3 = [0]*(N+1)
    dp_3[1] = time_to_buy[0][2]
    dp_3[2] = dp[1]+time_to_buy[1][2]

    for i in range(3, N+1):
        dp_1[i] = dp[i-1]+time_to_buy[i-1][0]
        dp_2[i] = dp[i-1]+time_to_buy[i-1][1]
        dp_3[i] = dp[i-1]+time_to_buy[i-1][2]

        dp[i] = min(dp_1[i], dp_2[i-1], dp_3[i-2])

    return dp[N]

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        
        time_to_buy = [(0, 0, 0)]*N
        for i in range(N):
            time_to_buy[i] = tuple([int(x) for x in fin.readline().split()])

        print(answer(N, time_to_buy))

if __name__ == '__main__':
    main()