def answer(numbers, N, K):
    numbers_last_position = dict()

    for i in range(N):
        num = numbers[i]
        if num in numbers_last_position:
            if i-numbers_last_position[num] <= K:                
                return 'YES'
            else:
                numbers_last_position[num] = i
        else:
            numbers_last_position[num] = i
    
    return 'NO'
    
def main():
    with open('input.txt') as fin:
        N, K = [int(x) for x in fin.readline().split()]
        numbers = [int(x) for x in fin.readline().split()]

        print(answer(numbers, N, K))      


if __name__ == '__main__':
    main()