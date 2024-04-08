def mergeArrays(arrays):
    big_array = []
    for array, index in arrays:
        for num in array:
            big_array.append((num, index))
    big_array.sort()

    return big_array

fin = open('input.txt')
N, L = [int(x) for x in fin.readline().split()]

answer = [[(None, 0) for _ in range(N)] for _ in range(N)]    

arrays = [None]*N
for i in range(N):
    arrays[i] = ([int(x) for x in fin.readline().split()], i)

def getMediansOfKArryas(answer, arrays):
    big_array = mergeArrays(arrays)

    for num, index in big_array:
        for i in range(index+1, N):
            if answer[index][i][1] < L: answer[index][i] = (num, answer[index][i][1]+1)

        for i in range(index):
            if answer[i][index][1] < L: answer[i][index] = (num, answer[i][index][1]+1)    

getMediansOfKArryas(answer, arrays)

ans = []
for i in range(N):
    for j in range(i+1, N):
        ans.append(answer[i][j][0])

print(*ans, sep='\n')