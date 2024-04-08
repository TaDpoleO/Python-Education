inp_file = open('input.txt')

s1 = inp_file.readline().rstrip()
s2 = inp_file.readline().rstrip()
   
pairs = set()
for i in range(len(s2)-1):
    pairs.add(s2[i:i+2])
    
count = 0
if pairs:
    for i in range(len(s1)-1):
        if s1[i:i+2] in pairs: count += 1
    
print(count)