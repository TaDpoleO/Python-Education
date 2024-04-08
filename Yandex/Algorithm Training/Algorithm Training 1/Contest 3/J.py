def extendRect(rect, delta):
    minusMin, minusMax, plusMin, plusMax = rect

    return (minusMin-delta, minusMax+delta, plusMin-delta, plusMax+delta)

def intersectRects(rect1, rect2):
    minusMin1, minusMax1, plusMin1, plusMax1 = rect1
    minusMin2, minusMax2, plusMin2, plusMax2 = rect2

    minusMin = max(minusMin1, minusMin2)
    minusMax = min(minusMax1, minusMax2)

    plusMin = max(plusMin1, plusMin2)
    plusMax = min(plusMax1, plusMax2)

    return (minusMin, minusMax, plusMin, plusMax)

fin = open('input.txt')

t, d, n = [int(x) for x in fin.readline().split()]

curr_rect = (0, 0, 0, 0) # minusMin, minusMax, plusMin, plusMax
for _ in range(n):
    x, y = [int(x) for x in fin.readline().split()]
    curr_rect = intersectRects(extendRect(curr_rect, t), extendRect((x-y, x-y, x+y, x+y), d))

points = []
for curr_minus in range(curr_rect[0], curr_rect[1]+1):
    for curr_plus in range(curr_rect[2], curr_rect[3]+1):
        x = (curr_minus+curr_plus)/2
        y = x-curr_minus

        if int(x) == x and int(y) == y: points.append((int(x), int(y)))

print(len(points))
for point in points:
    print(*point)