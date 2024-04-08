def main():
    fin = open('input.txt')

    board = [['x']*10 for _ in range(10)]
    for i in range(1, 9):
        line = fin.readline()[:8]
        for j in range(1, 9):
            board[i][j] = line[j-1]  
   
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 'B':
                dx = [1, -1, 1, -1]
                dy = [1, -1, -1, 1]
            elif board[i][j] == 'R':
                dx = [0, 0, 1, -1]
                dy = [1, -1, 0, 0]                
            else:
                dx = []
                dy = []

            for k in range(len(dx)):
                cur_index = 1
                while board[i+dx[k]*cur_index][j+dy[k]*cur_index] in ('*', 'A'):
                    board[i+dx[k]*cur_index][j+dy[k]*cur_index] = 'A'
                    cur_index += 1  

    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '*':
                count += 1
            
    print(count)


if __name__ == '__main__':
    main()