def answer(cells):
    board = [[0]*10 for _ in range(10)]

    for i in range(1, 9):
        for j in range(1, 9):
            board[i][j] = 1

    for row, col in cells:
        board[row][col] = 2

    P = 0
    for i, j in cells:
        if board[i][j] == 2:
            P += 4
            if board[i-1][j] == 2: P -= 2
            if board[i][j-1] == 2: P -= 2

    return P

    
def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        cells = [tuple([int(x) for x in line.split()]) for line in fin]

        print(answer(cells))

if __name__ == '__main__':
    main()