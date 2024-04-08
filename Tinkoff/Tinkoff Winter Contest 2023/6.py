# Точно не пройдет по времени :(

import sys

def plusNumber(array, left, right, num):
    for i in range(left, right+1):
        array[i] += num

def getNumber(array, left, right, K, B):
    curr_max = float('-inf')

    for i in range(left, right+1):
        curr_a = array[i]
        f_num = K*(i+1)+B
        curr_max = max(curr_max, min(curr_a, f_num))

    return curr_max

# fin = open('input.txt')
fin = sys.stdin

N, Q = [int(x) for x in fin.readline().split()]
array = [int(x) for x in fin.readline().split()]

for _ in range(Q):
    query = [x for x in fin.readline().split()]
    if query[0] == '?':
        left = int(query[1])-1
        right = int(query[2])-1
        K = int(query[3])
        B = int(query[4])

        print(getNumber(array, left, right, K, B))
    elif query[0] == '+':
        left = int(query[1])-1
        right = int(query[2])-1
        num = int(query[3])

        plusNumber(array, left, right, num)