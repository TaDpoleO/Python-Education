fin = open('input.txt')
lst = fin.readline().rstrip()

def answer(lst):    
    stack = []
    for ch in lst:
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'

    if not stack:
        return 'YES'
    else:
        return 'NO'

print(answer(lst))