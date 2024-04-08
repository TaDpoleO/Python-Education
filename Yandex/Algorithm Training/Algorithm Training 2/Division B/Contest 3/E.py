fin = open('input.txt')
M = int(fin.readline())

witness_nums = [0]*M
for i in range(M):
    witness_nums[i] = set(fin.readline().rstrip())

N = int(fin.readline())

possible_nums, correct_nums, max_correct = [0]*N, [0]*N, 0
for i in range(N):
    possible_nums[i] = fin.readline().rstrip()
    possible_num = set(possible_nums[i])

    res = True
    for j in range(M):
        if not (witness_nums[j]-possible_num):
            correct_nums[i] += 1
            if correct_nums[i] > max_correct: max_correct = correct_nums[i]

for i in range(N):
    if correct_nums[i] == max_correct: print(possible_nums[i])