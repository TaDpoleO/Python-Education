def answer(numbers):
    max_val = max(numbers)
    total = sum(numbers)-max_val

    if max_val > total:
        return max_val-total
    else:
        return max_val+total

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        numbers = [int(x) for x in fin.readline().split()]

        print(answer(numbers))

if __name__ == '__main__':
    main()