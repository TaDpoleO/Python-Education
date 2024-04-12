fin = open('input.txt')
M = int(fin.readline())

def check(n, a, b):
    count = n // b
    
    if b*count < n and n < a*(count+1):
        return 'NO'
    else:
        return 'YES'


for _ in range(M):
    print(check(*[int(x) for x in fin.readline().split()]))