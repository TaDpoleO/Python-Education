from collections import defaultdict
import bisect
  
def isAllCellsChanged(points, prefix, suffix, width):
    N = len(points)

    end_i = i = 0
    while (i < N) and (prefix[i][1]-prefix[i][0] <= width):
        end_i = i
        i += 1

    start_i = i = N-1
    while (i >= 0) and (suffix[i][1]-suffix[i][0] <= width):
        start_i = i
        i -= 1
    start_i = bisect.bisect_left(points, (points[start_i][0]-width, float('inf'), float('inf')))
   
    i0 = i1 = start_i
    while i0 < end_i+1:
        x0 = points[i0][0]

        while (i1 < N) and (points[i1][0]-x0 < width):
            i1 += 1
        i1 -= 1

        left_seg = prefix[i0]
        right_seg = suffix[i1]

        min_y, max_y = min(left_seg[0], right_seg[0]), max(left_seg[1], right_seg[1])
        if max_y-min_y+1 <= width:
            return True
        
        i0 += 1
        
    return False

def bsearch_firstT(points, prefix, suffix, left, right):
    while left < right:
        mid = (left+right)//2
        
        # FFTT, TTTT
        res = isAllCellsChanged(points, prefix, suffix, mid)
        if res:
            right = mid
        else:
            left = mid+1

    return left
    
def main():
    with open('input.txt') as fin:
        W, H, N = [int(x) for x in fin.readline().split()]

        points_dict_x = defaultdict(lambda: (float('inf'), float('-inf')))
        points_dict_y = defaultdict(lambda: (float('inf'), float('-inf')))
        for _ in range(N):
            x, y = tuple([int(x) for x in fin.readline().split()])
            points_dict_x[x] = (min(points_dict_x[x][0], y), max(points_dict_x[x][1], y))
            points_dict_y[y] = (min(points_dict_y[y][0], x), max(points_dict_y[y][1], x))

        if len(points_dict_x) < len(points_dict_y):
            points_dict = points_dict_x
        else:
            points_dict = points_dict_y

        points = []
        for x in sorted(points_dict):
            points.append((x, points_dict[x][0], points_dict[x][1]))
        N = len(points)

        prefix = [(float('inf'), float('-inf'))]*N
        for i in range(N-1):
            min_y = min(prefix[i][0], points[i][1])
            max_y = max(prefix[i][1], points[i][2])
            prefix[i+1] = (min_y, max_y)

        suffix = [(float('inf'), float('-inf'))]*N
        for i in range(N-2, -1, -1):
            min_y = min(suffix[i+1][0], points[i+1][1])
            max_y = max(suffix[i+1][1], points[i+1][2])
            suffix[i] = (min_y, max_y)       

        result = bsearch_firstT(points, prefix, suffix, 1, min(W, H))
        print(result)


if __name__ == '__main__':
    main()