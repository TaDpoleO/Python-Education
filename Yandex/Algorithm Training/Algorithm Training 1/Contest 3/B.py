from functools import reduce
print(*sorted(reduce(set.intersection, [set(map(int, x.split())) for x in open('input.txt').readlines()])))