inp_file = open('input.txt')

a = int(inp_file.readline().rstrip())
b = int(inp_file.readline().rstrip())
c = int(inp_file.readline().rstrip())

if c<0:
    print('NO SOLUTION')
elif a == 0:
    if b >= 0:
        if b == c**2:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        print('NO SOLUTION')
else: # x = (c**2-b)/a
    x_int = (c**2-b)//a
    x_float = (c**2-b)/a
    if x_int == x_float:
        print(x_int)
    else:
        print('NO SOLUTION')