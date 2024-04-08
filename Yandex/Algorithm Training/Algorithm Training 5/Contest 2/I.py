def get_turns_for_all_rows(ships):
    ships.sort()

    turns = 0
    for i in range(len(ships)):
        turns += abs(ships[i][0]-(i+1))

    return turns

def get_turns_for_col(ships):
    ships.sort(key=lambda x: x[1])
    median_col = ships[len(ships)//2][1]

    turns = 0
    for i in range(len(ships)):
        turns += abs(ships[i][1]-median_col)

    return turns

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())

        ships = [(0, 0)]*N
        for i in range(N):
            ships[i] = tuple([int(x) for x in fin.readline().split()])

        row_turns = get_turns_for_all_rows(ships)
        col_turns = get_turns_for_col(ships)

        print(row_turns+col_turns)


if __name__ == '__main__':
    main()