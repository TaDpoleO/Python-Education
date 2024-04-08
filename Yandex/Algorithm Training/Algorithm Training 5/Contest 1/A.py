def hasIntersection(line1, line2):
    return not ((line1[0] > line2[1]) or (line2[0] > line1[1]))

def countTreesInSegment(segment):
    x, y = segment

    return y-x+1

def main():
    fin = open('input.txt')

    P, V = [int(x) for x in fin.readline().split()]
    Q, M = [int(x) for x in fin.readline().split()]

    segments = [(P-V, P+V), (Q-M, Q+M)]
    segments.sort(key=lambda x: x[1])

    if hasIntersection(segments[0], segments[1]):
        result = countTreesInSegment((min(segments[0][0], segments[1][0]), max(segments[0][1], segments[1][1])))
    else:
        result = countTreesInSegment(segments[0])+countTreesInSegment(segments[1])

    print(result)


if __name__ == '__main__':
    main()