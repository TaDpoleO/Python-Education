from collections import Counter

def answer(numbers, N):
    num_counter = Counter(numbers)
    min_del = N

    for key in num_counter:
        if key+1 in num_counter:
            if (cur_del := N-num_counter[key]-num_counter[key+1]) < min_del:
                min_del = cur_del

    if min_del == N:
        for key in num_counter:
            if (cur_del := N-num_counter[key]) < min_del:
                min_del = cur_del

    return min_del

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        numbers = [int(x) for x in fin.readline().split()]
        print(answer(numbers, N))


if __name__ == '__main__':
    main()