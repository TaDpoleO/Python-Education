fin = open('input.txt')
N = int(fin.readline())
arr1 = [int(x) for x in fin.readline().split()]
M = int(fin.readline())
arr2 = [int(x) for x in fin.readline().split()]

def merge(array1, left1, right1, array2, left2, right2):
    res = []
    
    curr1, curr2 = left1, left2
    while (curr1 <= right1) and (curr2 <= right2):
        if array1[curr1] <= array2[curr2]:
            res.append(array1[curr1])
            curr1 += 1
        else:
            res.append(array2[curr2])
            curr2 += 1

    while (curr1 <= right1):
        res.append(array1[curr1])
        curr1 += 1

    while (curr2 <= right2):
        res.append(array2[curr2])
        curr2 += 1

    return res

print(*merge(arr1, 0, len(arr1)-1, arr2, 0, len(arr2)-1))