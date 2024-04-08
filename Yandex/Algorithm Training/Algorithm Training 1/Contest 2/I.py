inp_file = open('input.txt')
N, M, K = [int(x) for x in inp_file.readline().split()]

mines_pos = []
for k in range(K):
    curr_pos = [int(x)-1 for x in inp_file.readline().split()]
    mines_pos.append((curr_pos[0], curr_pos[1]))
    
def answer(N, M, K, mines_pos):
    def getNextPos(I, J):
        minI = I-1 if I>0 else 0
        maxI = I+1 if I<len(res)-1 else len(res)-1
        
        minJ = J-1 if J>0 else 0
        maxJ = J+1 if J<len(res[0])-1 else len(res[0])-1
      
        next_pos = []
        for i in range(minI, maxI+1):
            for j in range(minJ, maxJ+1):
                if not ((i==I) and (j==J)): next_pos.append((i, j))
        
        return next_pos

    res = [[0 for _ in range(M)] for _ in range(N)]
    
    for mine_pos in mines_pos:
       res[mine_pos[0]][mine_pos[1]] = '*'
           
    for i in range(N):
        for j in range(M):
            if res[i][j] != '*':
                count = 0
                for next_pos in getNextPos(i, j):
                    if res[next_pos[0]][next_pos[1]] == '*': count += 1
                res[i][j] = count
    
    for i in range(N):
        print(*res[i])

answer(N, M, K, mines_pos)