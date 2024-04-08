fin = open('input.txt')
L, K = [int(x) for x in fin.readline().split()]
array = [int(x) for x in fin.readline().split()]

def check(array, index, pivot):
    return array[index] < pivot

def bsearch(array, left, right, check, check_params):
    while left < right:
        mid = (left+right+1)//2
        # TTFF
        if check(array, mid, *check_params):
            left = mid
        else:
            right = mid-1

    return left

res_index = bsearch(array, 0, len(array)-1, check, [L//2])
if L % 2 == 1:
    if array[res_index+1] == L//2:
        print(array[res_index+1])
    else:
        print(array[res_index], array[res_index+1])
else:
    print(array[res_index], array[res_index+1])