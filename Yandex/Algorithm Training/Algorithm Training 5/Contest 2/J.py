from copy import deepcopy

def rows_first(array):
    array = deepcopy(array)

    N = len(array)
    M = len(array[0])

    rows = [dict() for _ in range(N+1)]
    
    for i in range(N):
        found = False
        buffer = [None, 0]

        for j in range(M):            
            if array[i][j] == '#':
                if not found:
                    buffer[0] = j                    
                buffer[1] += 1

                found = True            
            else:
                if buffer[0] is not None:
                    rows[i+1][tuple(buffer)] = -1
                    buffer = [None, 0]
                
                found = False
        
        if buffer[0] is not None: rows[i+1][tuple(buffer)] = -1

    id = 97
    for i in range(N):
        for key in rows[i+1]:
            if key in rows[i]:
                rows[i+1][key] = rows[i][key]
            else:
                rows[i+1][key] = id
                id += 1
      
    rectangles = dict()
    for i in range(N):
        for key, val in rows[i+1].items():
            if val in rectangles:
                x, y, height, width = rectangles[val]
                rectangles[val] = (x, y, height+1, width)
            else:
                rectangles[val] = (i, key[0], 1, key[1])

    for id, params in rectangles.items():
        x, y, height, width = params
        for i in range(x, x+height):
            for j in range(y, y+width):
                array[i][j] = chr(id)

    if len(rectangles) == 0 or len(rectangles) > 2:
        return None
    elif (len(rectangles) == 1):
        x, y, height, width = rectangles[list(rectangles.keys())[0]]

        if height == width == 1:
            return None
        elif (height != 1) and (width != 1):
            for i in range(x, x+height):
                array[i][y] = 'b'
        else:
            array[x][y] = 'b'
    
    return '\n'.join([''.join(row) for row in array])

def cols_first(array):
    array = deepcopy(array)

    N = len(array)
    M = len(array[0])

    cols = [dict() for _ in range(M+1)]
    
    for j in range(M):    
        found = False
        buffer = [None, 0]

        for i in range(N):        
            if array[i][j] == '#':                
                if not found:
                    buffer[0] = i
                buffer[1] += 1

                found = True            
            else:
                if buffer[0] is not None:
                    cols[j+1][tuple(buffer)] = -1
                    buffer = [None, 0]
                
                found = False
        
        if buffer[0] is not None: cols[j+1][tuple(buffer)] = -1

    id = 97
    for i in range(M):
        for key in cols[i+1]:
            if key in cols[i]:
                cols[i+1][key] = cols[i][key]
            else:
                cols[i+1][key] = id
                id += 1
      
    rectangles = dict()
    for i in range(M):
        for key, val in cols[i+1].items():
            if val in rectangles:
                x, y, height, width = rectangles[val]
                rectangles[val] = (x, y, height, width+1)
            else:
                rectangles[val] = (key[0], i, key[1], 1)

    for id, params in rectangles.items():
        x, y, height, width = params
        for i in range(x, x+height):
            for j in range(y, y+width):
                array[i][j] = chr(id)

    if len(rectangles) == 0 or len(rectangles) > 2:
        return None
    elif (len(rectangles) == 1):
        x, y, height, width = rectangles[list(rectangles.keys())[0]]

        if height == width == 1:
            return None
        elif (height != 1) and (width != 1):
            for i in range(x, x+height):
                array[i][y] = 'b'
        else:
            array[x][y] = 'b'
    
    return '\n'.join([''.join(row) for row in array])    

def main():
    with open('input.txt') as fin:
        N, M = [int(x) for x in fin.readline().split()]

        array = [[0]*M for _ in range(N)]
        for i in range(N):
            array[i] = list(fin.readline().rstrip())

        try_row = rows_first(array)
        
        if try_row:
            print('YES')
            print(try_row)
        else:
            try_col = cols_first(array)

            if try_col:
                print('YES')
                print(try_col)
            else:
                print('NO')


if __name__ == '__main__':
    main()