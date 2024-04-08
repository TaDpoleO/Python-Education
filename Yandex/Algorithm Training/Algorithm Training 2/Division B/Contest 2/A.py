from collections import defaultdict

fin = open('input.txt')
numbers, max_num = defaultdict(int), 0

num = int(fin.readline())
while num != 0:
    numbers[num] += 1
    if num > max_num: max_num = num
    num = int(fin.readline())

if max_num > 0:
    print(numbers[max_num])
else:
    print(0)