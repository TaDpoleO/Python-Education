fin = open('input.txt')
N = int(fin.readline())
numbers = [0]
for num in fin.readline().split():
    numbers.append(int(num))
    numbers.append(0)

N = len(numbers)

for i in range(N//2, N):
    found = True
    for j in range(N-1-i):
        if numbers[i+j] != numbers[i-j]: found = False

    if found:
        index = i
        break

answer = []
for j in range(N-index, index+1):
    if numbers[index-j] != 0: answer.append(numbers[index-j])
print(len(answer))
print(*answer)