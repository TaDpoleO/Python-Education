def main():
    with open('input.txt') as fin:
        N1 = int(fin.readline())
        numbers1 = set([int(x) for x in fin.readline().split()])

        N2 = int(fin.readline())
        numbers2 = set([int(x) for x in fin.readline().split()])

        N3 = int(fin.readline())
        numbers3 = set([int(x) for x in fin.readline().split()])

        all_numbers = numbers1 | numbers2 | numbers3

        result = []
        for num in sorted(all_numbers):
            if (num in numbers1 and num in numbers2) or (num in numbers2 and num in numbers3) or (num in numbers1 and num in numbers3):
                result.append(str(num))

        print(' '.join(result))


if __name__ == '__main__':
    main()