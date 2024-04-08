fin = open('input.txt')
N = int(fin.readline())
used_digitals = [False]*(N+1)
res = [0]*N

def permute(result, curr_index, used_digitals):
    if curr_index == len(used_digitals)-1:
        print(''.join(res))
    else:
        for i in range(1, N+1):
            if not used_digitals[i]:
                used_digitals[i] = True
                res[curr_index] = str(i)
                permute(result, curr_index+1, used_digitals)
                used_digitals[i] = False

for i in range(1, N+1):
    used_digitals[i] = True
    res[0] = str(i)
    permute(res, 1, used_digitals)
    used_digitals[i] = False