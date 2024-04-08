fin = open('input.txt')
expression = fin.readline().split()

stack = []
for oper in expression:
    if oper == '+':
        y = stack.pop()
        x = stack.pop()
        stack.append(x+y)
    elif oper == '-':
        y = stack.pop()
        x = stack.pop()
        stack.append(x-y)
    elif oper == '*':
        y = stack.pop()
        x = stack.pop()
        stack.append(x*y)
    else:
        stack.append(int(oper))
        
print(stack.pop())