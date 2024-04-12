fin = open('input.txt')
s = fin.readline().rstrip()

def answer(s):
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch == ')':
            if (not stack) or (stack[-1] != '('): return 'no'            
            stack.pop()
        elif ch == ']':
            if (not stack) or (stack[-1] != '['): return 'no'            
            stack.pop()
        elif ch == '}':
            if (not stack) or (stack[-1] != '{'): return 'no'            
            stack.pop()

    if stack:
        return 'no'
    else:
        return 'yes'
            
print(answer(s))