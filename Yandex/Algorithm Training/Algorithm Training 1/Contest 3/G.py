inp_file = open('input.txt')

N = int(inp_file.readline())

turtles = set()
for _ in range(N):
    x, y = [int(x) for x in inp_file.readline().split()]
    if (x+y == N-1) and (x>=0) and (y>=0): turtles.add((x, y))

print(len(turtles))