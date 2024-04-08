fin = open('input.txt')
N = int(fin.readline())
homes = [int(x) for x in fin.readline().split()]

def answer(homes, N):
    if N % 2 == 0:
        left = homes[N//2-1]
        right = homes[N//2]

        return (left+right)//2
    else:
        return homes[N//2]

print(answer(homes, N))