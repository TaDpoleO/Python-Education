from collections import deque

def get_lastLeft_and_firstRight(berries):
    max_right, first_right = float('-inf'), None
    max_left, last_left = float('-inf'), None
    
    total = 0
    for i in range(len(berries)):
        delta = berries[i][0]-berries[i][1]

        if (delta <= 0) and ((berries[i][0] > max_right)):
            max_right = berries[i][0]
            first_right = i
        elif (delta > 0):
            total += berries[i][0]-berries[i][1]

            if (berries[i][1] > max_left):
                max_left = berries[i][1]
                last_left = i

    return last_left, first_right, total

def answer(berries):    
    left_height = 0
    right_height = 0

    last_left, first_right, total_left_height = get_lastLeft_and_firstRight(berries)
    result = deque()

    if last_left is not None:
        result.append(last_left+1)
        left_height = total_left_height+berries[last_left][1]    

    if first_right is not None:
        result.append(first_right+1)
        right_height = total_left_height+berries[first_right][0]
   
    for i in range(len(berries)):
        if i not in [last_left, first_right]:
            if (berries[i][0]-berries[i][1] <= 0):
                result.append(i+1)
            elif (berries[i][0]-berries[i][1] > 0):
                result.appendleft(i+1)            
    
    return max(left_height, right_height), result

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        berries = [tuple([int(x) for x in line.split()]) for line in fin]

        height, order = answer(berries)
        print(height)
        print(*order)


if __name__ == '__main__':
    main()