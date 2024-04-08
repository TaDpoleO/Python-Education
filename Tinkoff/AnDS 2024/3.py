import sys
import math

fin = sys.stdin
# fin = open('input.txt')

N = int(fin.readline())
A = [int(x) for x in fin.readline().split()]

def check(A, mid):
    def calcDeltaS(y1, y2, mid_y):
        y1, y2 = min(y1, y2), max(y1, y2)

        if (mid_y > y2) or math.isclose(mid_y, y2):
            S = (y2-y1)/2+(mid_y-y2)
            return S, 0
        
        elif (y1 > mid_y) or math.isclose(mid_y, y1):
            S = (y2-y1)/2+(y1-mid_y)
            return 0, S
                
        else:
            k = (y2-y1)
            b = y1
            mid_x = (mid_y-b)/k

            S1 = (mid_y-y1)*mid_x/2
            S2 = (y2-mid_y)*(1-mid_x)/2

            return S1, S2

    low_level = 0
    high_level = 0

    for i in range(1, len(A)):
        left = A[i-1]
        right = A[i]

        curr_low, curr_high = calcDeltaS(left, right, mid)
        low_level += curr_low
        high_level += curr_high

    return low_level > high_level

def bsearch(A, left, right, check):
    while (right - left) > 10**-6:
        mid = (left+right)/2

        # FFTT
        if check(A, mid):
            right = mid
        else:
            left = mid

    return left

def answer(A):
    if len(A) == 1: return A[0]

    min_a, max_a = float('inf'), float('-inf')
    for a in A:
        min_a = min(min_a, a)
        max_a = max(max_a, a)

    res = bsearch(A, min_a, max_a, check)
    return res

print(answer(A))