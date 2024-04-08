fin = open('input.txt')
N = int(fin.readline())
numbers = [int(x) for x in fin.readline().split()]

max_num, sum = 0, 0
for num in numbers:
    if num > max_num: max_num = num
    sum += num

print(sum-max_num)