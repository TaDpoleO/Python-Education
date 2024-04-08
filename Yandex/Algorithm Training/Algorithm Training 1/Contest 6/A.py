fin = open('input.txt')

N, K = [int(x) for x in fin.readline().split()]
arrN = [int(x) for x in fin.readline().split()]
arrN.sort()
arrK = [int(x) for x in fin.readline().split()]

def searchIndex(num, array):
    left, right = 0, len(array)-1
    while left < right:
        mid = (left+right)//2
        
        if array[mid] < num:
            left = mid+1
        else:
            right = mid

    return left
    
for num in arrK:
    index = searchIndex(num, arrN)

    if arrN[index] == num:
        print('YES')
    else:
        print('NO')