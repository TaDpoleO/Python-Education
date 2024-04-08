from collections import defaultdict

def get_matches_params(point0, point1):
    angle_dx, angle_dy = point1[1]-point0[1], point1[0]-point0[0]
    R = angle_dx**2+angle_dy**2    

    return R, angle_dx, angle_dy

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())

        matches_a = set()
        for _ in range(N):
            x0, y0, x1, y1 = [int(x) for x in fin.readline().split()]

            (x0, y0), (x1, y1) = sorted(((x0, y0), (x1, y1)))
            R, angle_dx, angle_dy = get_matches_params((x0, y0), (x1, y1))

            matches_a.add((R, angle_dx, angle_dy, x0, y0))

        matches_b = set()
        for _ in range(N):
            x0, y0, x1, y1 = [int(x) for x in fin.readline().split()]

            (x0, y0), (x1, y1) = sorted(((x0, y0), (x1, y1)))
            R, angle_dx, angle_dy = get_matches_params((x0, y0), (x1, y1))

            matches_b.add((R, angle_dx, angle_dy, x0, y0))

        deltas = defaultdict(int)
        for match_a in matches_a:
            R_a0, dx_a0, dy_a0, x_a0, y_a0 = match_a

            for match_b in matches_b:
                R_b0, dx_b0, dy_b0, x_b0, y_b0 = match_b

                if (R_a0 == R_b0) and (dx_a0 == dx_b0) and (dy_a0 == dy_b0):
                    delta_x = x_b0-x_a0
                    delta_y = y_b0-y_a0

                    deltas[(delta_x, delta_y)] += 1

        max_delta = 0
        max_dx = max_dy = 0
        for (dx, dy), delta in deltas.items():
            if delta > max_delta:
                max_dx, max_dy = dx, dy
                max_delta = delta

        max_similarity = 0
        new_matches_a = set([(R, angle_dx, angle_dy, x0+max_dx, y0+max_dy) for (R, angle_dx, angle_dy, x0, y0) in matches_a])
        max_similarity = len(new_matches_a & matches_b)

        print(N-max_similarity)


if __name__ == '__main__':
    main()