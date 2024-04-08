def bsearch_left(left, right, pivot):
    while abs(right-left) > 10**(-7):
        mid = (left+right)/2

        # check_left: FFTT, FFFF, TTTT
        if cub_func(mid, a, b, c, d) >= pivot:
            left = mid
        else:
            right = mid

    return left

def bsearch_right(left, right, pivot):
    while abs(right-left) > 10**(-7):
        mid = (left+right)/2

        # check_right: TTFF, FFFF, TTTT
        if cub_func(mid, a, b, c, d) <= pivot:
            left = mid
        else:
            right = mid

    return left

def cub_func(x, a, b, c, d):
    return a*x*x*x+b*x*x+c*x+d

fin = open('cubroot.in')
a, b, c, d = [int(x) for x in fin.readline().split()]

x_min = -2000
x_max =  2000

y_min = cub_func(x_min, a, b, c, d)
if y_min < 0:
    x = bsearch_right(x_min, x_max, 0)
else:
    x = bsearch_left(x_min, x_max, 0)

print(x)