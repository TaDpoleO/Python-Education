fin = open('input.txt')
N = int(fin.readline())

numbers = set(range(1, N+1))

line = fin.readline().rstrip()
while line != 'HELP':
    question_nums = set([int(x) for x in line.split()])
    res = fin.readline().rstrip()
    
    if res == 'YES':
        numbers &= question_nums
    else:
        numbers -= question_nums

    line = fin.readline().rstrip()

print(*sorted(numbers))