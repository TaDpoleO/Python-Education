inp_file = open('input.txt')

s1 = set([x for x in inp_file.readline().split()])
s2 = set(inp_file.readline().rstrip())

print(len(s2-s1))