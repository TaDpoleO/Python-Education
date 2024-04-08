def answer(x0, y0, x1, y1, isHome):
    x = x0+x1
    y = y0+y1

    if x > y:
        return 0
    elif x == y:
        if x1 > y0:
            return 0
        else:
            return 1
    elif x < y:
        delta = y-x

        if isHome:
            if x1 > y0:
                return delta
            else:
                return delta+1
        else:
            if x1+delta > y0:
                return delta
            else:
                return delta+1
   

def main():
    fin = open('input.txt')

    x0, y0 = [int(x) for x in fin.readline().split(':')]
    x1, y1 = [int(x) for x in fin.readline().split(':')]
    fst_home = True if fin.readline().rstrip() == '1' else False

    if not fst_home:
        x0, y0, x1, y1 = x1, y1, x0, y0

    if fst_home:
        print(answer(x0, y0, x1, y1, False))
    else:
        print(answer(x0, y0, x1, y1, True))


if __name__ == '__main__':
    main()