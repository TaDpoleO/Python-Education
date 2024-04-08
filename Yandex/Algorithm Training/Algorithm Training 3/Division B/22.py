def answer(N, K):
    dp = [1]*N
    
    for i in range(2, N):
        ways = 0
        for j in range(max(0, i-K), i):
            ways += dp[j]

        dp[i] = ways

    return dp[N-1]

def main():
    with open('input.txt') as fin:
        N, K = [int(x) for x in fin.readline().split()]
        print(answer(N, K))

if __name__ == '__main__':
    main()