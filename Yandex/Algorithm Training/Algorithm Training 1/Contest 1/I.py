inp_file = open('input.txt')

A = int(inp_file.readline())
B = int(inp_file.readline())
C = int(inp_file.readline())
D = int(inp_file.readline())
E = int(inp_file.readline())

min_hole = min(D, E)
max_hole = max(D, E)

min_kirpich = min([A, B, C])
next_min_kirpich = min(set([A, B, C])-set([min_kirpich])) if set([A, B, C])-set([min_kirpich]) else min_kirpich

if (min_kirpich <= min_hole) and (next_min_kirpich <= max_hole):
    print('YES')
else:
    print('NO')