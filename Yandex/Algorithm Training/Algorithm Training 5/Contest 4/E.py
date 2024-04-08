def get_natural_sum(N):
    return N*(N+1)//2

def bsearch(left, right, N):
    while left < right:
        mid = (left+right)//2

        # FFTT
        if get_natural_sum(mid) >= N:
            right = mid
        else:
            left = mid+1

    return left

def answer(N):
    group_number = bsearch(1, N, N)

    prev_group_number = group_number-1
    prev_N = get_natural_sum(prev_group_number)

    index_in_group = N-prev_N

    if group_number % 2 == 1:
        numerator = index_in_group
        denominator = group_number-index_in_group+1
    else:
        numerator = group_number-index_in_group+1
        denominator = index_in_group

    return f'{numerator}/{denominator}'

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        print(answer(N))


if __name__ == '__main__':
    main()