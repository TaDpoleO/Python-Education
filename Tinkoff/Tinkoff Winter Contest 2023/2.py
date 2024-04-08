import sys

def answer(array):
    edges = 0
    for edge in array:
        if edge == 0: return False
        edges += min(edge, N-1)
    edges = edges-(N-1)

    if edges >= N-1:
        return True
    else:
        return False    

# fin = open('input.txt')
fin = sys.stdin

T = int(fin.readline())
for _ in range(T):
    N = int(fin.readline())
    array = [int(x) for x in fin.readline().split()]

    if answer(array):
        print('Yes')
    else:
        print('No')