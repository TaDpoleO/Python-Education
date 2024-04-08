def get_total_army(prefix, L, R):
    return prefix[R+1]-prefix[L]

def answer(prefix, K, S):
    left = 0
    right = len(prefix)-1-K

    # FFTT
    while left < right:
        mid = (left+right)//2
        if get_total_army(prefix, mid, mid+K-1) >= S:
            right = mid
        else:
            left = mid+1

    return left

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]
        numbers = [int(x) for x in fin.readline().split()]

        prefix = [0]*(N+1)
        for i in range(N):
            prefix[i+1] = prefix[i]+numbers[i]

        for _ in range(M):
            K, S = [int(x) for x in fin.readline().split()]
            start_army = answer(prefix, K, S)
            if get_total_army(prefix, start_army, start_army+K-1) == S:
                print(start_army+1)
            else:
                print(-1)


if __name__ == '__main__':
    main()