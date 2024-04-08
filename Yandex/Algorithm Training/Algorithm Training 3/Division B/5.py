fin = open('input.txt')
N = int(fin.readline())

amount = 0

prev_count = 0
for _ in range(N):
    curr_count = int(fin.readline())
    amount += min(prev_count, curr_count)
    prev_count = curr_count

print(amount)