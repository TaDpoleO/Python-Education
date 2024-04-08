import time
from math import sqrt

TOL = 0.0008
iTOL = 1250

def seg_diff(seg1, seg2):
    n0, n1 = seg1
    m0, m1 = seg2

    if m0 >= n1 or n0 >= m1:
        return seg1, None
    
    if m0 > n0 and m1 < n1:
        return (n0, m0), (m1, n1)
    
    if m0 <= n0 and m1 >= n1:
        return None, None
    
    if m0 > n0 and m1 >= n1:
        return (n0, m0), None
    
    if m1 < n1 and m0 <= n0:
        return (m1, n1), None

def free_delta_difference(free_deltas, seg):
    buffer = []

    for i in range(len(free_deltas)):
        seg1, seg2 = seg_diff(free_deltas[i], seg)
        if seg1: buffer.append(seg1)
        if seg2: buffer.append(seg2)

    return buffer

def get_free_points(D, points, enemies, T):
    result = dict()

    for x in points:
        y_max = sqrt(D*D-x*x)
        free_deltas_y = [(0, y_max)]

        for x_e, y_e, V_e in enemies:
            R_e = V_e*T
            x_min, x_max = x_e-R_e, x_e+R_e
            if x_min <= x and x <= x_max:
                delta_x = abs(x-x_e)
                delta_y = sqrt(R_e*R_e-delta_x*delta_x)
                y_min, y_max = y_e-delta_y, y_e+delta_y

                free_deltas_y = free_delta_difference(free_deltas_y, (y_min, y_max))
                if not free_deltas_y: break

        if free_deltas_y:
            result[x] = free_deltas_y
            return result

    return result

def get_free_points_time(D, points, enemies, left, right):
    while right-left > TOL:
        mid = (left+right)/2

        # TTFF
        if get_free_points(D, points, enemies, mid):
            left = mid
        else:
            right = mid

    return left

def answer(D, enemies: list):
    enemies.sort(key=lambda x: -x[2])
    points = [x for x in range(-D, D+1)]

    free_time = get_free_points_time(D, points, enemies, 0, 2000)
    free_points = get_free_points(D, points, enemies, free_time)

    buffer = set()
    for point in free_points:
        for x in range(max(point-1, -D)*iTOL, min(point+1, D)*iTOL+1):
            buffer.add(x*TOL)    

    free_time = get_free_points_time(D, buffer, enemies, free_time, 2000)
    free_points = get_free_points(D, buffer, enemies, free_time)

    res_x = list(free_points.keys())[0]
    res_y = free_points[res_x][0][0]

    return free_time, (res_x, res_y)

def main():
    with open('input.txt') as fin:
        D, N = [int(x) for x in fin.readline().split()]
        enemies = [(0, 0, 0)]*N

        for i in range(N):
            enemies[i] = [int(x) for x in fin.readline().split()]

        time, point = answer(D, enemies)
        print(f'{time:.3f}')
        print(f'{point[0]:.3f} {point[1]:.3f}')


if __name__ == '__main__':
    main()