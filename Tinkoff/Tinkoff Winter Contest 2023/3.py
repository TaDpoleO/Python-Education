import sys

def answer(M, N, gifts):
    dp = [0]*(N+1)
    dp[0] = M

    for i in range(N):
        money_after_try_to_buy = dp[i] if dp[i] < gifts[i] else dp[i]-gifts[i]
        money_without_try_to_buy = min(gifts[i]-1, dp[i])
        dp[i+1] = max(money_after_try_to_buy, money_without_try_to_buy)

    return dp[-1]

# fin = open('input.txt')
fin = sys.stdin

N, M = [int(x) for x in fin.readline().split()]
gifts = [int(x) for x in fin.readline().split()]

print(answer(M, N, gifts))