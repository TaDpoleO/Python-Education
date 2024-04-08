fin = open('input.txt')
N = int(fin.readline())

path = [int(x) for x in fin.readline().split()]
path.reverse()

def answer(path):
    stack = []
    seen = set()

    curr_number = 1
    while curr_number < N:
        if curr_number not in seen:
            if not path: return 'NO'

            num = path.pop()
            if num == curr_number:
                curr_number += 1
            else:
                stack.append(num)
                seen.add(num)
        else:
            if not stack or curr_number != stack[-1]:
                return 'NO'
            else:
                stack.pop()
                curr_number += 1

    return 'YES'

print(answer(path))