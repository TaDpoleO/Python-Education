inp_file = open('input.txt')

N = int(inp_file.readline())
array = [int(x) for x in inp_file.readline().split()]
target = int(inp_file.readline())

res, diff = array[0], abs(target-array[0])
for x in array[1:]:
    new_diff = abs(target-x)    
    if new_diff < diff:
        res = x
        diff = new_diff
        
print(res)