inp_file = open('input.txt')

N, M = [int(x) for x in inp_file.readline().split()]

s1 = []
for _ in range(N):
    s1.append(int(inp_file.readline()))
s1.sort()
    
s2 = []
for _ in range(M):
    s2.append(int(inp_file.readline()))
s2.sort()
    
s = set(s1) & set(s2)

res1, res2, res3 = [], [], []
if s:    
    for num in s1:
        if num in s:
            res1.append(num)
        else:
            res2.append(num)
    print(len(s))
    print(*res1)


    print(len(res2))
    print(*res2)

    for num in s2:
        if num not in s:
            res3.append(num)

    print(len(res3))
    print(*res3)
else:
    print(0)
    print()
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)