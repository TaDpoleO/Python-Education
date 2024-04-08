import random

fin = open('input.txt')
N = int(fin.readline())
array = [int(x) for x in fin.readline().split()]

def sort_quick(temp_array):
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
    
    if len(temp_array) < 2: return
    
    stack = [(0, len(temp_array)-1)]
    while stack:        
        left, right = stack.pop()

        pivot = temp_array[random.randrange(left, right)]
        equal_index, graterthan_index = partition_three_pointers(temp_array, left, right, pivot)

        if left < equal_index-1: stack.append((left, equal_index-1))
        if graterthan_index < right: stack.append((graterthan_index, right))


sort_quick(array)
print(*array)