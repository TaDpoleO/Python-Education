def changePoint(point, command):
    x, y = point

    if command == 'U':
        y += 1
    elif command == 'D':
        y -= 1
    elif command == 'R':
        x -= 1
    elif command == 'L':
        x += 1

    return x, y

def main():
    fin = open('input.txt')

    N, M = [int(x) for x in fin.readline().split()]
    C = int(fin.readline())
    commands = fin.readline().rstrip()

    cur_point = (0, 0)
    lines = set()

    for i in range(C):
        next_point = changePoint(cur_point, commands[i])

        if cur_point <= next_point:
            lines.add((cur_point, next_point))
        else:
            lines.add((next_point, cur_point))

        cur_point = next_point

    print(len(lines))


if __name__ == '__main__':
    main()