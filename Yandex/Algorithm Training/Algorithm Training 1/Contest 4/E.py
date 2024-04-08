from collections import defaultdict

inp_file = open('input.txt')
N = int(inp_file.readline())

blocks = defaultdict(int)
for _ in range(N):
    w, h = [int(x) for x in inp_file.readline().split()]
    blocks[w] = max(blocks[w], h)
    
print(sum(blocks.values()))