inp_file = open('input.txt')

a = int(inp_file.readline())
b = int(inp_file.readline())
n = int(inp_file.readline())
m = int(inp_file.readline())

# min time
min_1 = (n-1)*(a+1)+1
min_2 = (m-1)*(b+1)+1

# max time
max_1 = (1+a)*n+a
max_2 = (1+b)*m+b

if (max_1 < min_2) or (max_2 < min_1):
    print(-1)
else:
    print(max(min_1, min_2), min(max_1, max_2))    