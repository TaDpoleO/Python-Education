from collections import defaultdict

fin = open('input.txt')
N = int(fin.readline())

numbers = defaultdict(int)
for _ in range(N):
    d, a = [int(x) for x in fin.readline().split()]
    numbers[d] += a

for num in sorted(numbers):
    print(num, numbers[num])