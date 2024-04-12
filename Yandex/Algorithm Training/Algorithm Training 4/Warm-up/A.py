fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]
numbers = [int(x) for x in fin.readline().split()]

prefix = [0]*N
for i in range(1, N):
    prefix[i] = prefix[i-1]+abs(numbers[i]-numbers[i-1])

def checkDiff(left, right):
    if prefix[right]-prefix[left] == 0:
        return False
    else:
        return True
    
def bsearch(left, right, check):
    while left < right:
        mid = (left+right+1)//2
        # FFTT, FFFF
        if check(left, mid):
            right = mid-1
        else:
            left = mid

    return left

requests = [[int(x) for x in fin.readline().split()] for _ in range(M)]
for request in requests:
    index = bsearch(request[0], request[1], checkDiff)

    if index == request[1]:
        print('NOT FOUND')
    else:
        print(max(numbers[index], numbers[index+1]))