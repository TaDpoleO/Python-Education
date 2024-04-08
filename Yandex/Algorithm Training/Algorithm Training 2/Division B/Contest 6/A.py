def check_left(index, array, pivot):
    return array[index] >= pivot

def bsearch_left(array, left, right, check, check_param):
    while left < right:
        mid = (left+right)//2

        # check_left: FFTT, FFFF, TTTT
        if check(mid, array, *check_param):
            right = mid
        else:
            left = mid+1

    return left

def check_right(index, array, pivot):
    return array[index] <= pivot

def bsearch_right(array, left, right, check, check_param):
    while left < right:
        mid = (left+right+1)//2

        # check_right: TTFF, FFFF, TTTT
        if check(mid, array, *check_param):
            left = mid
        else:
            right = mid-1

    return left

fin = open('input.txt')
N = int(fin.readline())
numbers = [int(x) for x in fin.readline().split()]
numbers.sort()
K = int(fin.readline())

res = []
for _ in range(K):
    l, r = [int(x) for x in fin.readline().split()]
    left = bsearch_left(numbers, 0, len(numbers)-1, check_left, [l])
    right = bsearch_right(numbers, 0, len(numbers)-1, check_right, [r])

    if (left == len(numbers)-1 and numbers[left] < l) or right == 0 and numbers[right] > r:
        res.append(0)
    else:
        res.append(right-left+1)

print(*res)