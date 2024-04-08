inp_file = open('input.txt')

N = int(inp_file.readline())

s = set()
for _ in range(N):
    x, _ = [int(x) for x in inp_file.readline().split()]
    s.add(x)
    
print(len(s))