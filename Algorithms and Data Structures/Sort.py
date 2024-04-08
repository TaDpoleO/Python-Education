import heapq
import random

def sort_bubble(array):
    temp_array = array.copy()

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(temp_array)-1):        
            if temp_array[i] > temp_array[i+1]:
                temp_array[i], temp_array[i+1] = temp_array[i+1], temp_array[i]
                swapped = True

    return temp_array

def sort_selection(array):
    temp_array = array.copy()

    for i in range(len(temp_array)):
        lowest_index = i

        for j in range(i+1, len(temp_array)):
            if temp_array[j] < temp_array[lowest_index]:
                lowest_index = j

        temp_array[i], temp_array[lowest_index] = temp_array[lowest_index], temp_array[i]

    return temp_array

def sort_insert(array):    
    temp_array = array.copy()
    
    def insert(arr, num):
        if arr:
            for i in range(len(arr)):
                if num < arr[i]:
                    arr[i], num = num, arr[i]

        arr.append(num)

    buffer = []
    for i in range(len(temp_array)):
        insert(buffer, temp_array[i])

    return buffer

def sort_heap(array):
    temp_array = array.copy()

    heapq.heapify(temp_array)

    res = []
    while temp_array:
        res.append(heapq.heappop(temp_array))

    return res

def sort_merge(array):
    def merge(array1, array2):
        res = [0]*(len(array1)+len(array2))
        
        curr1, curr2, curr_res = 0, 0, 0
        while (curr1 <= len(array1)-1) and (curr2 <= len(array2)-1):
            if array1[curr1] <= array2[curr2]:
                res[curr_res] = array1[curr1]
                curr1 += 1
            else:
                res[curr_res] = array2[curr2]
                curr2 += 1

            curr_res += 1

        while (curr1 <= len(array1)-1):
            res[curr_res] = array1[curr1]
            curr1 += 1
            curr_res += 1

        while (curr2 <= len(array2)-1):
            res[curr_res] = array2[curr2]
            curr2 += 1
            curr_res += 1

        return res
    
    def __sort_merge(array, left, right):
        if left == right: return [array[left]]

        mid = (left+right)//2

        left_arr = __sort_merge(array, left, mid)
        right_arr = __sort_merge(array, mid+1, right)

        return merge(left_arr, right_arr)

    if len(array) < 2: return array
    return __sort_merge(array, 0, len(array)-1)

# Supporting func for quick sort, k-smallest and k-greatest
def partition_three_pointers(array, left, right, pivot):
    eq_index, gt_index, curr_index = left, left, left

    while curr_index <= right:
        curr_val = array[curr_index]

        if curr_val < pivot:
            array[curr_index] = array[gt_index]
            array[gt_index] = array[eq_index]
            array[eq_index] = curr_val
            gt_index += 1
            eq_index += 1
        elif curr_val == pivot:
            array[curr_index] = array[gt_index]
            array[gt_index] = curr_val
            gt_index += 1
        
        curr_index += 1

    return eq_index, gt_index

def sort_quick(array):
    def __sort_quick(array, left, right):
        if left >= right: return

        pivot = array[random.randrange(left, right)]        
        equal_index, graterthan_index = partition_three_pointers(array, left, right, pivot)
    
        __sort_quick(array, left, equal_index-1)
        __sort_quick(array, graterthan_index, right)

    temp_array = array.copy()
    __sort_quick(temp_array, 0, len(temp_array)-1)
    return temp_array

def k_smallest(array, k=1):
    def __k_smallest(array, left, right, k):
        if left >= right: return

        pivot = array[random.randrange(left, right)]        
        equal_index, graterthan_index = partition_three_pointers(array, left, right, pivot)

        if equal_index-left == k:
            return
        elif equal_index-left > k:
            __k_smallest(array, left, equal_index-1, k)
        else:
            if graterthan_index-left >= k:
                return
            else:
                __k_smallest(array, graterthan_index, right, k-graterthan_index+left)

    if k >= len(array): return array
    temp_array = array.copy()
    __k_smallest(temp_array, 0, len(temp_array)-1, k)
    return temp_array[:k]

def k_greatest(array, k=1):
    def __k_greatest(array, left, right, k):
        if left >= right: return

        pivot = array[random.randrange(left, right)]        
        equal_index, graterthan_index = partition_three_pointers(array, left, right, pivot)

        if right-graterthan_index+1 == k:
            return
        elif right-graterthan_index+1 > k:
            __k_greatest(array, graterthan_index, right, k)
        else:
            if right-equal_index+1 >= k:
                return
            else:
                __k_greatest(array, left, equal_index-1, k-right+equal_index-1)

    if k >= len(array): return array
    temp_array = array.copy()
    __k_greatest(temp_array, 0, len(temp_array)-1, k)
    return temp_array[-k:]

if __name__ == '__main__':
    import time

    numbers = [1, 10, 2, 4, 8, 6, 3, 9, 5, 7, 0]

    print(f'    sort_bubble: {sort_bubble(numbers)}')
    print(f' sort_selection: {sort_selection(numbers)}')
    print(f'    sort_insert: {sort_insert(numbers)}')
    print(f'      sort_heap: {sort_heap(numbers)}')    
    print(f'     sort_merge: {sort_merge(numbers)}')
    print(f'     sort_quick: {sort_quick(numbers)}')

    print(f'\n       unsorted: {numbers}')
    k = 5
    print(f'     {k}-smallest: {k_smallest(numbers, k)}')
    print(f'     {k}-greatest: {k_greatest(numbers, k)}')

    print('-'*50)
    print('N*logN Speed test')
    N = 1000000

    test_case = []
    for i in range(N):
        test_case.append(random.randint(0, 2**32-1))
    
    time0 = time.time()
    res = list(sorted(test_case))
    time1 = time.time()
    print(f'    Python Sort: {time1-time0}')

    time0 = time.time()
    res = sort_heap(test_case)
    time1 = time.time()
    print(f'      sort_heap: {time1-time0}')

    time0 = time.time()
    res = sort_merge(test_case)
    time1 = time.time()
    print(f'     sort_merge: {time1-time0}')

    time0 = time.time()
    res = sort_quick(test_case)
    time1 = time.time()
    print(f'     sort_quick: {time1-time0}')

    print('-'*50)
    print('K-Statistic and Sort Speed Test')
    k = len(test_case)//2

    time0 = time.time()
    res = sort_quick(test_case)[:k]
    time1 = time.time()
    print(f'     sort_quick: {time1-time0}')

    time0 = time.time()
    res = k_smallest(test_case, k)
    time1 = time.time()
    print(f'     k_smallest: {time1-time0}')

    time0 = time.time()
    res = k_greatest(test_case, k)
    time1 = time.time()
    print(f'     k_greatest: {time1-time0}')