def split_array(array):
    if not array: return []
    result = []
    
    min_val = array[0]
    cur_len = 0

    for num in array:
        if (min_val > cur_len) and (num > cur_len):
            cur_len += 1
            min_val = min(min_val, num)
        else:
            result.append(cur_len)
            min_val = num
            cur_len = 1
    result.append(cur_len)

    return result

def main():
    with open('input.txt') as fin:
        T = int(fin.readline())
        
        for _ in range(T):
            N = int(fin.readline())
            array = [int(x) for x in fin.readline().split()]

            result = split_array(array)

            print(len(result))
            print(*result)


if __name__ == '__main__':
    main()