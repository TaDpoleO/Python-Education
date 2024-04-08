fin = open('input.txt')

board = [[0]*8 for _ in range(8)]
for i in range(8):
    for j, ch in enumerate(fin.readline().rstrip()):
        if ch == '.':
            board[i][j] = 0
        elif ch == '*':
            board[i][j] = 1
#111 
# 1
def isTetra1Placeable(board, x, y):
    if x > 6 or y > 5: return False    

    if board[x][y] == 0 and board[x][y+1] == 0 and board[x][y+2] == 0 and board[x+1][y+1] == 0:
        return True
    else:
        return False
    
# 1 
#111
def isTetra2Placeable(board, x, y):
    if x > 6 or y > 5: return False    

    if board[x+1][y] == 0 and board[x+1][y+1] == 0 and board[x+1][y+2] == 0 and board[x][y+1] == 0:
        return True
    else:
        return False
    
#1
#11
#1
def isTetra3Placeable(board, x, y):
    if x > 5 or y > 6: return False    

    if board[x][y] == 0 and board[x+1][y] == 0 and board[x+2][y] == 0 and board[x+1][y+1] == 0:
        return True
    else:
        return False
    
# 1
#11
# 1
def isTetra4Placeable(board, x, y):
    if x > 5 or y > 6: return False    

    if board[x][y+1] == 0 and board[x+1][y+1] == 0 and board[x+2][y+1] == 0 and board[x+1][y] == 0:
        return True
    else:
        return False    

count = 0
for i in range(8):
    for j in range(8):
        if isTetra1Placeable(board, i, j): count += 1
        if isTetra2Placeable(board, i, j): count += 1
        if isTetra3Placeable(board, i, j): count += 1
        if isTetra4Placeable(board, i, j): count += 1

print(count)