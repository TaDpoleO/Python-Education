fin = open('input.txt')
N = int(fin.readline())
array = [int(x) for x in fin.readline().split()]
pivot = int(fin.readline())

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

left, right = 0, len(array)-1
equal_index, graterthan_index = partition_three_pointers(array, left, right, pivot)
print(equal_index-left)
print(right-equal_index+1)