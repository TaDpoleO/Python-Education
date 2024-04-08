import math

def check(number, x):
    r2 = int(math.sqrt(number))
    r3 = int(math.pow(number, 1/3))
    if (r3+1)**3 <= number: r3 = r3+1
    r6 = int(math.pow(number, 1/6))
    if (r6+1)**6 <= number: r6 = r6+1
   
    return r2+r3-r6 >= x

def bsearch(left, right, x):
    while left < right:
        mid = (left+right)//2
        # FFTT, TTTT, search - first T
        if check(mid, x):
            right = mid
        else:
            left = mid+1
            
    return left

fin = open('input.txt')
x = int(fin.readline())
print(bsearch(1, 10**14, x))