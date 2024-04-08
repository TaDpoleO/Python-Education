import sys

fin = sys.stdin
# fin = open('input.txt')

N = int(fin.readline())
text = fin.readline().rstrip()
min_len, max_len = float('inf'), float('-inf')
for line in text.split('#'):
    curr_len = len(line)

    min_len = min(min_len, curr_len)
    max_len = max(max_len, curr_len)

print(min_len, max_len)