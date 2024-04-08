fin = open('input.txt')
N = int(fin.readline())

cols = [False]*N
diags1 = [False]*(2*N-1)
diags2 = [False]*(2*N-1)

def countDinos(curr_point, used_cols, used_diags1, used_diags2):
    if curr_point[0] == N-1: 
        return 1
    else:        
        used_cols[curr_point[1]] = True
        used_diags1[curr_point[0]+curr_point[1]] = True
        used_diags2[curr_point[0]-curr_point[1]+N-1] = True

        res = 0
        for i in range(N):
            if not used_cols[i] and not used_diags1[curr_point[0]+1+i] and not used_diags2[curr_point[0]-i+N]:
                res += countDinos((curr_point[0]+1, i), used_cols, used_diags1, used_diags2)

        used_cols[curr_point[1]] = False
        used_diags1[curr_point[0]+curr_point[1]] = False
        used_diags2[curr_point[0]-curr_point[1]+N-1] = False

        return res       

answer = 0
for i in range(N):
    answer += countDinos((0, i), cols, diags1, diags2)

print(answer)