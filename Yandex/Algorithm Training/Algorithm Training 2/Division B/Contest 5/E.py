fin = open('threesum.in')
S = int(fin.readline())
N1, *array1 = [int(x) for x in fin.readline().split()]
N2, *array2 = [int(x) for x in fin.readline().split()]
N3, *array3 = [int(x) for x in fin.readline().split()]

dict3 = dict()
for i, num in enumerate(array3):
    if num not in dict3: dict3[num] = i

def answer(array1, array2, array3, S):
    for index1 in range(len(array1)):
        for index2 in range(len(array2)):
            if S-array1[index1]-array2[index2] in dict3:
                return index1, index2, dict3[S-array1[index1]-array2[index2]]
   
    return [-1]

print(*answer(array1, array2, array3, S))