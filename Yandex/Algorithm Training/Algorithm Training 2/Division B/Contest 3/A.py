fin = open('input.txt')
s1 = set([int(x) for x in fin.readline().split()])
s2 = set([int(x) for x in fin.readline().split()])

print(len(s1 & s2))