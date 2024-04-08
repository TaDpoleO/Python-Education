# ПОПРОСИЛИ ПРОВЕРИТЬ ЧУЖОЙ КОД

def find_ways_for_date(n, r, am):
    ways = []
    sum_, left, right = 0, 0, 1

    while right < n:
        diff = am[right] - am[left]
        if diff <= r:
            ways.append(sum_)
            right += 1
        else:
            sum_ += 1
            if right - left > 1:
                left += 1
            else:
                if right == n - 1 and left == n - 2:
                    ways.append(sum_)
                left += 1
                right += 1

    return sum(ways)


def main():
    fin = open('input.txt')

    n, r = [int(x) for x in fin.readline().split()]
    monuments = [int(x) for x in fin.readline().split()]

    print(find_ways_for_date(n, r, monuments))

main()