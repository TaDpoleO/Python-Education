fin = open('input.txt')
N = int(fin.readline())
array = [int(x) for x in fin.readline().split()]

left, right, curr_sum, max_sum = 0, 0, 0, float('-inf')
while right < len(array):
    curr_sum += array[right]
    max_sum = max(max_sum, curr_sum)

    while (curr_sum < 0) and (left < right):
        curr_sum -= array[left]
        max_sum = max(max_sum, curr_sum)
        left += 1

    if array[left] < 0:
        left += 1
        curr_sum = 0

    right += 1

print(max_sum)