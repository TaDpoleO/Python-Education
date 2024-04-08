fin = open('input.txt')

N, K = [int(x) for x in fin.readline().split()]
arrN = [int(x) for x in fin.readline().split()]
arrK = [int(x) for x in fin.readline().split()]

def search(num, array):
    left, right = 0, len(array)-1
    
    while left < right:
        mid = (left+right)//2
        if array[mid] > num:
            right = mid
        else:
            left = mid+1

    return left

for num in arrK:
    index = search(num, arrN)
    index = index-1 if (index != 0) and abs(arrN[index]-num) >= abs(arrN[index-1]-num) else index
    print(arrN[index])