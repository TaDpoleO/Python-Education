def bsearch_left(numbers, left, right, pivot):
    if numbers[-1] < pivot: return len(numbers)

    while left < right:
        mid = (left+right)//2

        # FFTT, FFFF, TTTT
        if numbers[mid] >= pivot:
            right = mid
        else:
            left = mid+1

    return left

def bsearch_right(numbers, left, right, pivot):
    if numbers[0] > pivot: return -1

    while left < right:
        mid = (left+right+1)//2

        # TTFF, FFFF, TTTT
        if numbers[mid] <= pivot:
            left = mid
        else:
            right = mid-1

    return left

def answer(numbers, L, R):
    N = len(numbers)

    left = bsearch_left(numbers, 0, N-1, L)
    right = N-1-bsearch_right(numbers, 0, N-1, R)

    return N-left-right

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        numbers = [int(x) for x in fin.readline().split()]
        numbers.sort()

        K = int(fin.readline())

        result = [0]*K
        for i in range(K):
            result[i] = answer(numbers, *[int(x) for x in fin.readline().split()])

        print(*result)


if __name__ == '__main__':
    main()