inp_file = open('input.txt')

N = int(inp_file.readline())
press_counter = {key+1: int(value)  for key, value in enumerate(inp_file.readline().split())}

K = int(inp_file.readline())
for key in [int(x) for x in inp_file.readline().split()]:
    press_counter[key] -= 1
   
for i in range(1,N+1):
    if press_counter[i] < 0:
        print('YES')
    else:
        print('NO')