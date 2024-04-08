fin = open('brackets2.in')
N = int(fin.readline())

def genBrackets(length):
    if length % 2 == 1: return
    length = length // 2

    stack = [('', [], 0, 0)]
    while stack:
        curr_seq, curr_stack, opened_number, closed_number = stack.pop()

        if opened_number == closed_number == length:
            print(curr_seq)
        elif opened_number < length:
            if curr_stack:
                if curr_stack[-1] == '[':
                    stack.append((curr_seq+']', curr_stack[:-1], opened_number, closed_number+1))
                elif curr_stack[-1] == '(':
                    stack.append((curr_seq+')', curr_stack[:-1], opened_number, closed_number+1))
            stack.append((curr_seq+'[', curr_stack+['['], opened_number+1, closed_number))
            stack.append((curr_seq+'(', curr_stack+['('], opened_number+1, closed_number))
        elif closed_number < opened_number:
            if curr_stack[-1] == '[':
                stack.append((curr_seq+']', curr_stack[:-1], opened_number, closed_number+1))
            elif curr_stack[-1] == '(':
                stack.append((curr_seq+')', curr_stack[:-1], opened_number, closed_number+1))

genBrackets(N)