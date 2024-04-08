fin = open('input.txt')
N = int(fin.readline())
numbers = [int(x) for x in fin.readline().split()]

max_number = max(numbers)

max_number_seen, max_ans = False, 0
for i in range(len(numbers)-1):
    curr_num = numbers[i]

    if max_number_seen and (curr_num % 10 == 5) and (numbers[i+1] < curr_num):
        max_ans = max(max_ans, curr_num)

    if curr_num == max_number: max_number_seen = True

if max_ans == 0:
    print(0)
else:
    count = 0
    for num in numbers:
        if num > max_ans: count += 1

    print(count+1)