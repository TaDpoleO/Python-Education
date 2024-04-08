from collections import defaultdict

fin = open('input.txt')
numbers = [int(x) for x in fin.readline().split()]

num_counter = defaultdict(int)
for num in numbers:
    num_counter[num] += 1

res = []
for num in numbers:
    if num_counter[num] == 1: res.append(num)

print(' '.join(map(str, res)))