def count_cells(K):
    if K == 0: return 0

    count_ships = (1+K)*K//2
    free_cells = count_ships-1
    busy_cells = K*(K+1)*(K+2)//6

    return free_cells+busy_cells

def bsearch(left, right, N):
    # TTFF
    while left < right:
        mid = (left+right+1)//2
        
        if count_cells(mid) <= N:
            left = mid
        else:
            right = mid-1

    return left

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        print(bsearch(0, N, N))


if __name__ == '__main__':
    main()