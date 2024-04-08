def answer(N):
    if N == 0: return 0
    if N == 1: return 2
   
    dp = [0]*(N+1)
    dp[1] = 2
    dp[2] = 4

    dp_1 = [0]*(N+1)
    dp_1[2] = 1

    dp_11 = [0]*(N+1)
    dp_11[2] = 1

    for i in range(3, N+1):
        dp[i] = dp[i-1]*2-dp_11[i-1]
        dp_1[i] = dp[i-2]
        dp_11[i] = dp_1[i-1]

    return dp[N]

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        print(answer(N))

if __name__ == '__main__':
    main()