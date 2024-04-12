def correct_Man_On_Floor(stack):
    while stack and stack[-1] == 0:
        stack.pop()

fin = open('input.txt')
K = int(fin.readline())
N = int(fin.readline())

stack = []
for _ in range(N):
    stack.append(int(fin.readline()))

correct_Man_On_Floor(stack)

def answer(max_man_in_elevator, stack):
    res_time = 0
    while stack:
        res_time += len(stack)*2

        if stack[-1] > max_man_in_elevator:
            count = (stack[-1] // max_man_in_elevator)-1
            res_time += len(stack)*2*count
            stack[-1] -= max_man_in_elevator*count

        curr_man_in_elevator = 0
        while (curr_man_in_elevator < max_man_in_elevator) and stack:            
            if stack[-1]+curr_man_in_elevator <= max_man_in_elevator:
                curr_man_in_elevator += stack.pop()
                correct_Man_On_Floor(stack)
            else:
                stack[-1] -= (max_man_in_elevator-curr_man_in_elevator)
                curr_man_in_elevator = max_man_in_elevator

    return res_time

print(answer(K, stack))