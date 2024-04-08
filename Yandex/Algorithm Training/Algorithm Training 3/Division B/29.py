def answer(N, costs):
    if N == 0: return 0, 0, []

    dp = [[float('inf')]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0

    for j in range(N):
        for i in range(N):
            if dp[i][j] < float('inf'):
                if costs[j] > 100:
                    dp[i+1][j+1] = min(dp[i][j]+costs[j], dp[i+1][j+1])
                else:
                    dp[i][j+1] = min(dp[i][j]+costs[j], dp[i][j+1])

                if i > 0:
                    dp[i-1][j+1] = min(dp[i][j], dp[i-1][j+1])

    min_price, K1 = float('inf'), 0
    for i in range(N+1):
        if dp[i][-1] <= min_price:
            min_price = dp[i][-1]
            K1 = i

    discount_days = []
    cur_i = K1
    for j in range(N, 0, -1):
        if cur_i > 0 and costs[j-1] > 100 and dp[cur_i][j] == dp[cur_i-1][j-1]+costs[j-1]:
            cur_i -= 1
        elif cur_i < N and dp[cur_i][j] == dp[cur_i+1][j-1]:
            cur_i += 1
            discount_days.append(j)

    return min_price, K1, discount_days

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())

        prices = [0]*N
        for i in range(N):
            prices[i] = int(fin.readline())

        min_price, K1, discount_days = answer(N, prices)
        print(min_price)
        print(f'{K1} {len(discount_days)}')
        print('\n'.join([str(x) for x in reversed(discount_days)]))

if __name__ == '__main__':
    main()