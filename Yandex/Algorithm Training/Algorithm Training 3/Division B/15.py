from collections import deque

fin = open('input.txt')
N = int(fin.readline())

stack1 = deque()
for i, num in enumerate([int(x) for x in fin.readline().split()]):
    stack1.appendleft((num, i))
    
answer = [-1]*N
stack2 = []
while stack1:
    num1, index1 = stack1.pop()
    
    while stack2 and stack2[-1][0] > num1:
        num2, index2 = stack2.pop()
        answer[index2] = index1
        
    stack2.append((num1, index1))
    
print(*answer)