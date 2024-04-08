def get_max(array, row=None, col=None):
    max_val = float('-inf')
    result = (None, None)

    for i in range(len(array)):
        if i != row:
            for j in range(len(array[0])):
                if (j != col) and (array[i][j] > max_val):
                        max_val = array[i][j]
                        result = (i, j)

    return result

def get_row_and_col(array):
    row1, _ = get_max(array)
    _, col1 = get_max(array, row=row1)
    max1 = get_max(array, row1, col1)

    _, col2 = get_max(array)
    row2, _ = get_max(array, col=col2)
    max2 = get_max(array, row2, col2)

    if array[max1[0]][max1[1]] < array[max2[0]][max2[1]]:
        return (row1+1, col1+1)
    else:
        return (row2+1, col2+1)

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]

        array = [[]*M for _ in range(N)]        
        for i in range(N):
            array[i] = [int(x) for x in fin.readline().split()]
        
        result = get_row_and_col(array)
        print(*result)


if __name__ == '__main__':
    main()