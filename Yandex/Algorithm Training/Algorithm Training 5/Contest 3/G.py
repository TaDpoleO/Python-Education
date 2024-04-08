import math

def get_quads(p00, p01):
    dx = p01[0]-p00[0]
    dy = p01[1]-p00[1]

    p10r = (p00[0]+dy, p00[1]-dx)
    p11r = (p01[0]+dy, p01[1]-dx)

    p10l = (p00[0]-dy, p00[1]+dx)
    p11l = (p01[0]-dy, p01[1]+dx)

    return [p10r, p11r], [p10l, p11l]

def answer(points):
    points_set = set(points)
                            
    max_answer = tuple()
    for i in range(len(points)):
        cur_answer = tuple([points[i]])

        for j in range(i+1, len(points)):
            cur_answers = [[points[i], points[j]], [points[i], points[j]]]
            quads = get_quads(points[i], points[j])

            for k in range(len(cur_answers)):
                for point in quads[k]:
                    if point in points_set:
                        cur_answers[k].append(point)

            cur_answer = tuple(cur_answers[0])
            for k in range(len(cur_answers)):
                if len(cur_answers[k]) > len(cur_answer):
                    cur_answer = tuple(cur_answers[k])

            if len(cur_answer) > len(max_answer):
                max_answer = cur_answer

        if len(cur_answer) > len(max_answer):
            max_answer = cur_answer

    return max_answer

def convert_answer(answer):
    N = len(answer)
    if N == 1:
        p00 = answer[0]
        p01 = (p00[0]+1, p01[1])
        p10 = (p00[0], p01[1]+1)
        p11 = (p00[0]+1, p01[1]+1)

        return (p01, p10, p11)
    
    elif N == 2:
        quad1, _ = get_quads(*answer)
        
        return tuple(quad1)

    elif N == 3:
        quads = get_quads(answer[0], answer[1])

        for i in range(len(quads)):
            if answer[2] in quads[i]:
                for p in quads[i]:
                    if p != answer[2]:
                        result = p
            
        return tuple([result])
    else:
        return tuple()
    
def main():
    with open('input.txt') as fin:
        N = int(fin.readline())

        points = [(0, 0)]*N
        for i in range(N):
            points[i] = tuple([int(x) for x in fin.readline().split()])

        result = answer(points)
        result = convert_answer(result)

        print(len(result))
        for res in result:
            print(*res)


if __name__ == '__main__':
    main()