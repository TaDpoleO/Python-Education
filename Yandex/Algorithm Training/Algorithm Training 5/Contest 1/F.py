def answer(N, numbers):
    operations = ['+']*(N-1)

    total = sum(numbers)    
    if total % 2 == 1: return ''.join(operations)

    for i in range(N-1):
        if numbers[i] % 2 == 1:
            operations[i] = 'x'
            return ''.join(operations)  


def main():
    fin = open('input.txt')
    N = int(fin.readline())
    numbers = [int(x) for x in fin.readline().split()]
    
    print(answer(N, numbers))


if __name__ == '__main__':
    main()