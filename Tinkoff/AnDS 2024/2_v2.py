import sys

fin = sys.stdin
# fin = open('input.txt')

N = int(fin.readline())
text = fin.readline().rstrip()
min_len, max_len = float('inf'), float('-inf')

curr_len = 0
for letter in text:
    if letter != '#':
        curr_len += 1
    else:        
        min_len = min(min_len, curr_len)
        max_len = max(max_len, curr_len)
        curr_len = 0

min_len = min(min_len, curr_len)
max_len = max(max_len, curr_len)        

print(min_len, max_len)