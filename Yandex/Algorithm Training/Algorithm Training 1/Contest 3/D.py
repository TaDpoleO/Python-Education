inp_file = open('input.txt')

s = set()
for line in inp_file:
    s |= set(line.split())
    
print(len(s))