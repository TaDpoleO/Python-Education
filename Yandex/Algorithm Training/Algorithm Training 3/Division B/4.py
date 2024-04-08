fin = open('input.txt')
N = int(fin.readline())
K = int(fin.readline())

row = int(fin.readline())
col = int(fin.readline())

def RowAndColToIndex(row, col):    
    index = (row-1)*2+(col-1)    

    return index

def IndexToRowAndCol(index):
    row = index//2+1
    col = index%2+1

    return row, col

index_of_petya = RowAndColToIndex(row, col)
left_index_of_vasya = index_of_petya-K
right_index_of_vasya = index_of_petya+K

if (right_index_of_vasya < N) and (left_index_of_vasya > -1):
    row_left, col_left = IndexToRowAndCol(left_index_of_vasya)
    row_right, col_right = IndexToRowAndCol(right_index_of_vasya)

    if row-row_left < row_right-row:
        print(row_left, col_left)
    else:
        print(row_right, col_right)

elif right_index_of_vasya < N:
    print(*IndexToRowAndCol(right_index_of_vasya))
elif left_index_of_vasya > -1:
    print(*IndexToRowAndCol(left_index_of_vasya))
else:
    print(-1)