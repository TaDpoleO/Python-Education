fin = open('input.txt')
N, i, j = [int(x) for x in fin.readline().split()]

def answer(N, i, j):
    if i > j: i, j = j, i

    return min(j-i-1, i+N-j-1)

print(answer(N, i, j))