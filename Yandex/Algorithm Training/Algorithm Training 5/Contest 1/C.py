def getPressCount(number):
    result = 0

    a4 = number // 4
    result += a4

    delta = number-a4*4
    if delta == 3:
        result += 2
    else:
        result += delta

    return result

def main():
    fin = open('input.txt')
    N = int(fin.readline())

    result = 0
    for _ in range(N):
        ai = int(fin.readline())
        result += getPressCount(ai)

    print(result)


if __name__ == '__main__':
    main()